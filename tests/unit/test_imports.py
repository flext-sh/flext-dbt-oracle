"""Behavioral contract tests for the flext_dbt_oracle public surface.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from flext_db_oracle import FlextDbOracleSettings
from flext_tests import tm

from flext_dbt_oracle import FlextDbtOracleSettings, c, m, u

if TYPE_CHECKING:
    from flext_core import t


class TestsFlextDbtOracleImports:
    """Public-contract behavior for DBT Oracle models, settings, and helpers."""

    @staticmethod
    def test_materialization_enum_members_are_dbt_values() -> None:
        """Test materialization enum members are dbt values."""
        materialization = c.DbtOracle.Dbt.Materialization
        tm.that(
            {member.value for member in materialization},
            eq={"table", "view", "incremental", "snapshot"},
        )

    # NOTE (multi-agent): mro-rn88 — settings dedup: Oracle connection scalars are
    # SSOT in settings.DbOracle.* (inherited); settings.DbtOracle.* holds dbt knobs.
    @staticmethod
    def test_settings_defaults_expose_oracle_connection_contract() -> None:
        """Test settings defaults expose oracle connection contract."""
        settings = FlextDbtOracleSettings()
        upstream = FlextDbOracleSettings.DbOracleSettings()

        tm.that(settings.DbOracle.port, eq=upstream.port)
        tm.that(settings.DbOracle.service_name, eq=upstream.service_name)
        tm.that(settings.DbOracle.host, eq=upstream.host)
        tm.that(settings.DbtOracle.schema_name, eq="")

    @staticmethod
    def test_settings_namespace_round_trips_constructor_values() -> None:
        """Test settings namespace round trips constructor values."""
        credential = "topsecret"
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                host="db.example.com",
                password=credential,
                sid="ORCLSID",
            ),
        )
        oracle = FlextDbtOracleSettings.model_validate({
            "DbtOracle": {"schema_name": "analytics"},
        }).DbtOracle

        tm.that(settings.DbOracle.host, eq="db.example.com")
        tm.that(settings.DbOracle.password, eq=credential)
        tm.that(settings.DbOracle.sid, eq="ORCLSID")
        tm.that(oracle.schema_name, eq="analytics")

    @staticmethod
    def test_dbt_settings_namespace_exposes_materialization() -> None:
        """Test dbt settings namespace exposes materialization."""
        oracle = FlextDbtOracleSettings.model_validate({
            "DbtOracle": {"schema_name": "stg", "materialization": "view"},
        }).DbtOracle

        tm.that(oracle.schema_name, eq="stg")
        tm.that(oracle.materialization, eq="view")

    @staticmethod
    def test_model_defaults_apply_domain_constants() -> None:
        """Test model defaults apply domain constants."""
        model = m.DbtOracle.Model(
            name="orders",
            table_name="stg_orders",
            sql_content="select 1",
        )

        tm.that(model.dbt_model_type, eq=c.DbtOracle.DEFAULT_MODEL_TYPE)
        tm.that(model.schema_name, eq=c.DbtOracle.DEFAULT_SCHEMA_NAME)
        tm.that(model.source_name, eq=c.DbtOracle.DEFAULT_SOURCE_NAME)
        tm.that(model.materialization, eq=c.DbtOracle.Dbt.DEFAULT_MATERIALIZATION)
        tm.that(model.columns, eq=())
        tm.that(model.dependencies, eq=())

    @staticmethod
    @pytest.mark.parametrize(
        "source_tables",
        [(), ("customers",), ("customers", "orders")],
    )
    def test_generate_staging_models_names_one_model_per_table(
        source_tables: t.VariadicTuple[str],
    ) -> None:
        """Test generate staging models names one model per table."""
        models = u.DbtOracle.ModelBuilder.generate_staging_models(source_tables)

        tm.that(
            [model.name for model in models],
            eq=[f"stg_oracle_{table}" for table in source_tables],
        )
        for table, model in zip(source_tables, models, strict=True):
            tm.that(model.table_name, eq=f"stg_{table}")
            tm.that(model.sql_content, has=f"source('oracle', '{table}')")

    @staticmethod
    def test_oracle_table_adapter_exposes_qualified_relation() -> None:
        """Test oracle table adapter exposes qualified relation."""
        adapter = m.DbtOracle.OracleTableAdapter(
            schema_name="sales",
            table_name="orders",
        )

        tm.that(adapter.relation_name, eq="sales.orders")
        tm.that(
            adapter.model_dump(by_alias=True),
            eq={"schema": "sales", "table": "orders", "relation": "sales.orders"},
        )
