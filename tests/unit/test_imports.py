"""Behavioral contract tests for the flext_dbt_oracle public surface.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_db_oracle import FlextDbOracleSettings
from flext_dbt_oracle import c, m, u
from flext_dbt_oracle._settings import FlextDbtOracleSettings


class TestsFlextDbtOracleImports:
    """Public-contract behavior for DBT Oracle models, settings, and helpers."""

    def test_materialization_enum_members_are_dbt_values(self) -> None:
        materialization = c.DbtOracle.Dbt.Materialization
        assert {member.value for member in materialization} == {
            "table",
            "view",
            "incremental",
            "snapshot",
        }

    # NOTE (multi-agent): mro-rn88 — settings dedup: Oracle connection scalars are
    # SSOT in settings.DbOracle.* (inherited); settings.DbtOracle.* holds dbt knobs.
    def test_settings_defaults_expose_oracle_connection_contract(self) -> None:
        settings = FlextDbtOracleSettings()

        assert settings.DbOracle.port == c.DbtOracle.Oracle.DEFAULT_PORT
        assert settings.DbOracle.service_name == c.DbtOracle.Oracle.DEFAULT_SERVICE_NAME
        assert settings.DbOracle.host == "localhost"
        assert settings.DbtOracle.schema_name == ""

    def test_settings_namespace_round_trips_constructor_values(self) -> None:
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings._DbOracle(
                host="db.example.com",
                password="topsecret",
                sid="ORCLSID",
            ),
        )
        oracle = FlextDbtOracleSettings(
            DbtOracle=FlextDbtOracleSettings._DbtOracle(schema_name="analytics"),
        ).DbtOracle

        assert settings.DbOracle.host == "db.example.com"
        assert settings.DbOracle.password == "topsecret"
        assert settings.DbOracle.sid == "ORCLSID"
        assert oracle.schema_name == "analytics"

    def test_dbt_settings_namespace_exposes_materialization(self) -> None:
        oracle = FlextDbtOracleSettings(
            DbtOracle=FlextDbtOracleSettings._DbtOracle(
                schema_name="stg", materialization="view"
            ),
        ).DbtOracle

        assert oracle.schema_name == "stg"
        assert oracle.materialization == "view"

    def test_model_defaults_apply_domain_constants(self) -> None:
        model = m.DbtOracle.Model(
            name="orders",
            table_name="stg_orders",
            sql_content="select 1",
        )

        assert model.dbt_model_type == c.DbtOracle.DEFAULT_MODEL_TYPE
        assert model.schema_name == c.DbtOracle.DEFAULT_SCHEMA_NAME
        assert model.source_name == c.DbtOracle.DEFAULT_SOURCE_NAME
        assert model.materialization == c.DbtOracle.Dbt.DEFAULT_MATERIALIZATION
        assert model.columns == ()
        assert model.dependencies == ()

    @pytest.mark.parametrize(
        "source_tables",
        [
            (),
            ("customers",),
            ("customers", "orders"),
        ],
    )
    def test_generate_staging_models_names_one_model_per_table(
        self,
        source_tables: tuple[str, ...],
    ) -> None:
        models = u.DbtOracle.ModelBuilder.generate_staging_models(source_tables)

        assert [model.name for model in models] == [
            f"stg_oracle_{table}" for table in source_tables
        ]
        for table, model in zip(source_tables, models, strict=True):
            assert model.table_name == f"stg_{table}"
            assert f"source('oracle', '{table}')" in model.sql_content

    def test_oracle_connection_config_dsn_uses_service_when_no_sid(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="h",
            username="u",
            service_name="SVC",
        )

        assert config.database_identifier == "SVC"
        assert config.dsn.endswith("/SVC")
        assert config.username in config.dsn

    def test_oracle_connection_config_dsn_uses_sid_when_present(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="h",
            username="u",
            sid="SID9",
            service_name="SVC",
        )

        assert config.database_identifier == "SID9"
        assert config.dsn.endswith(":SID9")

    def test_oracle_table_adapter_exposes_qualified_relation(self) -> None:
        adapter = m.DbtOracle.OracleTableAdapter(
            schema_name="sales",
            table_name="orders",
        )

        assert adapter.relation_name == "sales.orders"
        assert adapter.model_dump(by_alias=True) == {
            "schema": "sales",
            "table": "orders",
            "relation": "sales.orders",
        }


__all__: list[str] = ["TestsFlextDbtOracleImports"]
