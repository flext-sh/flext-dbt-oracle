"""Behavioral contract tests for the flext_dbt_oracle public surface.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_dbt_oracle import c, m
from flext_dbt_oracle.settings import FlextDbtOracleSettings


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

    def test_settings_defaults_expose_oracle_connection_contract(self) -> None:
        settings = FlextDbtOracleSettings()

        assert settings.port == c.DbtOracle.Oracle.DEFAULT_PORT
        assert settings.database_identifier == c.DbtOracle.Oracle.DEFAULT_SERVICE_NAME
        # effective_schema falls back to the username when schema_name is empty.
        assert settings.effective_schema == settings.oracle_username

    def test_settings_connection_string_masks_password(self) -> None:
        settings = FlextDbtOracleSettings(oracle_password="topsecret")

        connection_string = settings.connection_string

        assert "topsecret" not in connection_string
        assert "***" in connection_string
        assert settings.oracle_host in connection_string

    def test_settings_sid_overrides_service_name_identifier(self) -> None:
        settings = FlextDbtOracleSettings(sid="ORCLSID")

        assert settings.database_identifier == "ORCLSID"
        # SID identifiers are joined with ':' in the connection string.
        assert ":ORCLSID" in settings.connection_string

    def test_settings_effective_schema_prefers_explicit_schema(self) -> None:
        settings = FlextDbtOracleSettings(schema_name="analytics")

        assert settings.effective_schema == "analytics"

    def test_to_connection_config_returns_public_password_value(self) -> None:
        settings = FlextDbtOracleSettings(
            oracle_password="pw",
            sid="SID1",
        )

        config = settings.to_connection_config()

        assert config["host"] == settings.oracle_host
        assert config["port"] == settings.port
        assert config["sid"] == "SID1"
        assert config["password"] == "pw"

    def test_to_oracle_config_builds_connection_model(self) -> None:
        settings = FlextDbtOracleSettings(oracle_host="db.example.com")

        oracle_config = settings.to_oracle_config()

        assert isinstance(
            oracle_config,
            m.DbtOracle.OracleConnectionConfig,
        )
        assert oracle_config.host == "db.example.com"
        assert oracle_config.port == settings.port

    def test_pool_max_below_min_raises_validation_error(self) -> None:
        with pytest.raises(ValueError, match="Pool max size must be >= pool min size"):
            FlextDbtOracleSettings(pool_min_size=5, pool_max_size=1)

    def test_dbt_settings_reflect_effective_schema_and_materialization(self) -> None:
        settings = FlextDbtOracleSettings(schema_name="stg")

        dbt_settings = settings.dbt_settings

        assert dbt_settings["schema"] == "stg"
        assert dbt_settings["database"] == settings.oracle_service_name
        assert dbt_settings["materialization"] == settings.materialization

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
        generator = m.create_generator()

        models = generator.generate_staging_models(source_tables)

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
        assert adapter.to_metadata() == {
            "schema": "sales",
            "table": "orders",
            "relation": "sales.orders",
        }


__all__: list[str] = ["TestsFlextDbtOracleImports"]
