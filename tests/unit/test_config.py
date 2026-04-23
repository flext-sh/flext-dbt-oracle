"""Advanced tests for Oracle configuration using FLEXT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import (
    Sequence,
)
from typing import Literal, cast

import pytest

from tests import c, m, t

FlextDbtOracleSettings = m.DbtOracle.FlextDbtOracleSettings


class TestFlextDbtOracleSettings:
    """Test DBT Oracle configuration functionality."""

    def test_basic_config_creation(self) -> None:
        """Test creating basic Oracle configuration."""
        settings = m.DbtOracle.FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )
        assert settings.oracle_host == "localhost"
        assert settings.oracle_username == "testuser"
        assert settings.oracle_service_name == "XEPDB1"
        assert isinstance(settings.port, int)
        assert settings.port > 0

    def test_config_with_sid(self) -> None:
        """Test configuration with SID instead of service_name."""
        settings = m.DbtOracle.FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            sid="XE",
        )
        assert settings.oracle_host == "localhost"
        assert settings.oracle_username == "testuser"
        assert settings.sid == "XE"

    def test_config_validation_missing_host(self) -> None:
        """Test default host is applied when not provided explicitly."""
        settings = m.DbtOracle.FlextDbtOracleSettings(
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )
        assert isinstance(settings.oracle_host, str)
        assert settings.oracle_host != ""

    def test_config_validation_missing_username(self) -> None:
        """Test default username is applied when not provided explicitly."""
        settings = m.DbtOracle.FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )
        assert isinstance(settings.oracle_username, str)
        assert settings.oracle_username != ""

    def test_config_validation_missing_password(self) -> None:
        """Test default password is applied when not provided explicitly."""
        settings = m.DbtOracle.FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_service_name="XEPDB1",
        )
        assert isinstance(settings.oracle_password, t.SecretStr)

    def test_config_validation_invalid_materialization(self) -> None:
        """Test validation fails for invalid materialization."""
        materialization: str = "invalid_type"
        with pytest.raises(c.ValidationError, match="Input should be"):
            _ = m.DbtOracle.FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=t.SecretStr("testpass"),
                oracle_service_name="XEPDB1",
                materialization=cast(
                    "Literal['incremental', 'snapshot', 'table', 'view']",
                    materialization,
                ),
            )

    def test_config_validation_invalid_protocol(self) -> None:
        """Test validation fails for invalid protocol."""
        protocol: str = "invalid_protocol"
        with pytest.raises(c.ValidationError, match="Input should be"):
            _ = m.DbtOracle.FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=t.SecretStr("testpass"),
                oracle_service_name="XEPDB1",
                protocol=cast("Literal['tcp', 'tcps']", protocol),
            )

    def test_config_validation_pool_sizes(self) -> None:
        """Test validation of pool sizes."""
        with pytest.raises(c.ValidationError, match="Pool max size"):
            _ = m.DbtOracle.FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=t.SecretStr("testpass"),
                oracle_service_name="XEPDB1",
                pool_min_size=10,
                pool_max_size=5,
            )

    def test_connection_string(self) -> None:
        """Test connection string generation."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )
        conn_str = settings.connection_string
        separator = ":" if "sid" in settings.model_fields_set and settings.sid else "/"
        assert (
            conn_str
            == f"oracle://testuser:***@localhost:{settings.port}{separator}{settings.database_identifier}"
        )

    def test_connection_string_with_sid(self) -> None:
        """Test connection string generation with SID."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            sid="XE",
        )
        conn_str = settings.connection_string
        assert conn_str == f"oracle://testuser:***@localhost:{settings.port}:XE"

    def test_effective_schema(self) -> None:
        """Test effective schema retrieval."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            schema_name="TEST_SCHEMA",
        )
        assert settings.effective_schema == "TEST_SCHEMA"

    def test_database_identifier(self) -> None:
        """Test database identifier retrieval."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )
        assert settings.database_identifier in {"XEPDB1", "XE"}
        config_with_sid = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            sid="XE",
        )
        assert config_with_sid.database_identifier == "XE"

    def test_to_connection_config(self) -> None:
        """Test conversion to connection configuration."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )
        conn_config = settings.to_connection_config()
        expected_keys = {
            "host",
            "port",
            "service_name",
            "sid",
            "username",
            "password",
            "protocol",
        }
        assert set(conn_config.keys()) == expected_keys
        assert conn_config["host"] == "localhost"
        assert conn_config["username"] == "testuser"
        assert conn_config["service_name"] == "XEPDB1"

    def test_to_oracle_config(self) -> None:
        """Test conversion to Oracle settings."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            pool_min_size=2,
            pool_max_size=10,
        )
        oracle_config = settings.to_oracle_config()
        assert oracle_config.host == "localhost"
        assert oracle_config.username == "testuser"
        assert oracle_config.service_name == "XEPDB1"

    def test_performance_settings(self) -> None:
        """Test performance settings retrieval."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            pool_min_size=2,
            pool_max_size=10,
            query_timeout=300,
        )
        perf_settings = settings.performance_settings
        expected_keys = {
            "pool_min_size",
            "pool_max_size",
            "pool_increment",
            "query_timeout",
            "fetch_size",
            "connect_timeout",
            "retry_attempts",
            "retry_delay",
        }
        assert set(perf_settings.keys()) == expected_keys
        assert perf_settings["pool_min_size"] == 2
        assert perf_settings["pool_max_size"] == 10
        assert perf_settings["query_timeout"] == 300

    def test_dbt_settings(self) -> None:
        """Test DBT settings retrieval."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            materialization=c.DbtOracle.Dbt.Materialization.TABLE,
        )
        dbt_settings = settings.dbt_settings
        assert "database" in dbt_settings
        assert "schema" in dbt_settings
        assert "materialization" in dbt_settings
        assert dbt_settings["materialization"] == "table"


class TestConfigEdgeCases:
    """Test configuration edge cases and error conditions."""

    def test_config_with_all_optional_fields(self) -> None:
        """Test configuration with all optional fields set."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            oracle_port=1522,
            protocol="tcps",
            ssl_server_dn_match=True,
            nls_lang="AMERICAN_AMERICA.AL32UTF8",
            nls_date_format="DD/MM/YYYY",
            search_path="schema1,schema2",
            enable_metrics=True,
            log_level=c.LogLevel.DEBUG,
            enable_sql_logging=True,
            pool_min_size=1,
            pool_max_size=20,
            pool_increment=2,
            query_timeout=600,
            fetch_size=2000,
            connect_timeout=60,
            retry_attempts=5,
            retry_delay_seconds=2.0,
        )
        assert settings.port == 1522
        assert settings.protocol == "tcps"
        assert settings.ssl_server_dn_match is True
        assert settings.nls_lang == "AMERICAN_AMERICA.AL32UTF8"
        assert settings.enable_metrics is True
        assert settings.log_level == "DEBUG"

    def test_config_defaults_when_no_service_name_or_sid(self) -> None:
        """Test that default service name is used when neither service_name nor sid provided.

        Test that default service name is used when neither service_name nor sid provided.
        """
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
        )
        assert settings.oracle_service_name is not None

    def test_config_field_validation_ranges(self) -> None:
        """Test field validation for numeric ranges."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            oracle_port=1521,
            pool_min_size=1,
            pool_max_size=50,
            query_timeout=600,
            retry_delay_seconds=0.5,
        )
        assert settings.port == 1521
        assert settings.pool_min_size == 1
        assert settings.pool_max_size == 50
        assert settings.query_timeout == 600
        assert abs(settings.retry_delay_seconds - 0.5) < 1e-9

    def test_config_materialization_validation_all_valid_types(self) -> None:
        """Test all valid materialization types."""
        materialization_enum = c.DbtOracle.Dbt.Materialization
        valid_materializations: Sequence[materialization_enum] = [
            materialization_enum.TABLE,
            materialization_enum.VIEW,
            materialization_enum.INCREMENTAL,
            materialization_enum.SNAPSHOT,
        ]
        for materialization in valid_materializations:
            settings = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=t.SecretStr("testpass"),
                oracle_service_name="XEPDB1",
                materialization=materialization,
            )
            assert settings.materialization == materialization

    def test_config_protocol_validation_all_valid_types(self) -> None:
        """Test all valid protocol types."""
        valid_protocols: Sequence[Literal["tcp", "tcps"]] = ["tcp", "tcps"]
        for protocol in valid_protocols:
            settings = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=t.SecretStr("testpass"),
                oracle_service_name="XEPDB1",
                protocol=protocol,
            )
            assert settings.protocol == protocol


class TestConfigConstantsUsage:
    """Test usage of configuration constants."""

    def test_config_uses_default_constants(self) -> None:
        """Test that configuration uses default constants appropriately."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )
        assert isinstance(settings.port, int)
        assert settings.port > 0
        assert settings.protocol in {"tcp", "tcps"}
        assert settings.materialization in {"table", "view", "incremental", "snapshot"}
        assert settings.pool_min_size >= 1
        assert settings.pool_max_size >= settings.pool_min_size
        assert settings.query_timeout > 0
        assert settings.fetch_size > 0
