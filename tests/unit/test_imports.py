"""Behavioral contract tests for the flext_dbt_oracle public surface.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from flext_tests import tm

from flext_db_oracle import FlextDbOracleSettings
from flext_dbt_oracle import c, m, u
from flext_dbt_oracle._settings import FlextDbtOracleSettings


class TestsFlextDbtOracleImports:
    """Public-contract behavior for DBT Oracle models, settings, and helpers."""

    def test_materialization_enum_members_are_dbt_values(self) -> None:
        materialization = c.DbtOracle.Dbt.Materialization
        tm.that(
            {member.value for member in materialization},
            eq={"table", "view", "incremental", "snapshot"},
        )

    # NOTE (multi-agent): mro-rn88 — settings dedup: Oracle connection scalars are
    # SSOT in settings.DbOracle.* (inherited); settings.DbtOracle.* holds dbt knobs.
    def test_settings_defaults_expose_oracle_connection_contract(self) -> None:
        settings = FlextDbtOracleSettings()

        tm.that(settings.DbOracle.port, eq=c.DbtOracle.Oracle.DEFAULT_PORT)
        tm.that(
            settings.DbOracle.service_name, eq=c.DbtOracle.Oracle.DEFAULT_SERVICE_NAME
        )
        tm.that(settings.DbOracle.host, eq="localhost")
        tm.that(settings.DbtOracle.schema_name, eq="")

    def test_settings_namespace_round_trips_constructor_values(self) -> None:
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings._DbOracle(
                host="db.example.com", password="topsecret", sid="ORCLSID"
            )
        )
        oracle = FlextDbtOracleSettings(
            DbtOracle=FlextDbtOracleSettings._DbtOracle(schema_name="analytics")
        ).DbtOracle

        tm.that(settings.DbOracle.host, eq="db.example.com")
        tm.that(settings.DbOracle.password, eq="topsecret")
        tm.that(settings.DbOracle.sid, eq="ORCLSID")
        tm.that(oracle.schema_name, eq="analytics")

    def test_dbt_settings_namespace_exposes_materialization(self) -> None:
        oracle = FlextDbtOracleSettings(
            DbtOracle=FlextDbtOracleSettings._DbtOracle(
                schema_name="stg", materialization="view"
            )
        ).DbtOracle

        tm.that(oracle.schema_name, eq="stg")
        tm.that(oracle.materialization, eq="view")

    def test_model_defaults_apply_domain_constants(self) -> None:
        model = m.DbtOracle.Model(
            name="orders", table_name="stg_orders", sql_content="select 1"
        )

        tm.that(model.dbt_model_type, eq=c.DbtOracle.DEFAULT_MODEL_TYPE)
        tm.that(model.schema_name, eq=c.DbtOracle.DEFAULT_SCHEMA_NAME)
        tm.that(model.source_name, eq=c.DbtOracle.DEFAULT_SOURCE_NAME)
        tm.that(model.materialization, eq=c.DbtOracle.Dbt.DEFAULT_MATERIALIZATION)
        tm.that(model.columns, eq=())
        tm.that(model.dependencies, eq=())

    @pytest.mark.parametrize(
        "source_tables", [(), ("customers",), ("customers", "orders")]
    )
    def test_generate_staging_models_names_one_model_per_table(
        self, source_tables: tuple[str, ...]
    ) -> None:
        models = u.DbtOracle.ModelBuilder.generate_staging_models(source_tables)

        tm.that(
            [model.name for model in models],
            eq=[f"stg_oracle_{table}" for table in source_tables],
        )
        for table, model in zip(source_tables, models, strict=True):
            tm.that(model.table_name, eq=f"stg_{table}")
            tm.that(model.sql_content, has=f"source('oracle', '{table}')")

    def test_oracle_connection_config_dsn_uses_service_when_no_sid(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="h", username="u", service_name="SVC"
        )

        tm.that(config.database_identifier, eq="SVC")
        assert config.dsn.endswith("/SVC")
        tm.that(config.dsn, has=config.username)

    def test_oracle_connection_config_dsn_uses_sid_when_present(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="h", username="u", sid="SID9", service_name="SVC"
        )

        tm.that(config.database_identifier, eq="SID9")
        assert config.dsn.endswith(":SID9")

    def test_oracle_table_adapter_exposes_qualified_relation(self) -> None:
        adapter = m.DbtOracle.OracleTableAdapter(
            schema_name="sales", table_name="orders"
        )

        tm.that(adapter.relation_name, eq="sales.orders")
        tm.that(
            adapter.model_dump(by_alias=True),
            eq={"schema": "sales", "table": "orders", "relation": "sales.orders"},
        )


__all__: list[str] = ["TestsFlextDbtOracleImports"]
