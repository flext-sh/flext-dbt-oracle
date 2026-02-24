"""Advanced tests for Oracle configuration using FLEXT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

import pytest
from flext_dbt_oracle.settings import OracleConnectionConfig
from pydantic import SecretStr, ValidationError

from flext_dbt_oracle import FlextDbtOracleSettings


class TestFlextDbtOracleSettings:
    """Test DBT Oracle configuration functionality."""

    def test_basic_config_creation(self) -> None:
        """Test creating basic Oracle configuration."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )
        assert config.oracle_host == "localhost"
        assert config.oracle_username == "testuser"
        assert config.oracle_service_name == "XEPDB1"
        assert config.port == 1521  # default

    def test_config_with_sid(self) -> None:
        """Test configuration with SID instead of service_name."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            sid="XE",
        )
        assert config.oracle_host == "localhost"
        assert config.oracle_username == "testuser"
        assert config.sid == "XE"

    def test_config_validation_missing_host(self) -> None:
        """Test validation fails when host is missing."""
        with pytest.raises(ValidationError, match="Field required"):
            _ = FlextDbtOracleSettings(  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
                oracle_username="testuser",
                oracle_password=SecretStr("testpass"),
                oracle_service_name="XEPDB1",
            )

    def test_config_validation_missing_username(self) -> None:
        """Test validation fails when username is missing."""
        with pytest.raises(ValidationError, match="Field required"):
            _ = FlextDbtOracleSettings(  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
                oracle_host="localhost",
                oracle_password=SecretStr("testpass"),
                oracle_service_name="XEPDB1",
            )

    def test_config_validation_missing_password(self) -> None:
        """Test validation fails when password is missing."""
        with pytest.raises(ValidationError, match="Field required"):
            _ = FlextDbtOracleSettings(  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_service_name="XEPDB1",
            )

    def test_config_validation_invalid_materialization(self) -> None:
        """Test validation fails for invalid materialization."""
        with pytest.raises(ValidationError, match="Input should be"):
            _ = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=SecretStr("testpass"),
                oracle_service_name="XEPDB1",
                materialization="invalid_type",  # pyright: ignore[reportArgumentType]
            )

    def test_config_validation_invalid_protocol(self) -> None:
        """Test validation fails for invalid protocol."""
        with pytest.raises(ValidationError, match="Input should be"):
            _ = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=SecretStr("testpass"),
                oracle_service_name="XEPDB1",
                protocol="invalid_protocol",  # pyright: ignore[reportArgumentType]
            )

    def test_config_validation_pool_sizes(self) -> None:
        """Test validation of pool sizes."""
        with pytest.raises(ValidationError, match="Pool max size"):
            _ = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=SecretStr("testpass"),
                oracle_service_name="XEPDB1",
                pool_min_size=10,
                pool_max_size=5,  # smaller than min
            )

    def test_get_connection_string(self) -> None:
        """Test connection string generation."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )
        conn_str = config.get_connection_string()
        assert conn_str == "oracle://testuser:***@localhost:1521/XEPDB1"

    def test_get_connection_string_with_sid(self) -> None:
        """Test connection string generation with SID."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            sid="XE",
        )
        conn_str = config.get_connection_string()
        assert conn_str == "oracle://testuser:***@localhost:1521:XE"

    def test_get_effective_schema(self) -> None:
        """Test effective schema retrieval."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            schema_name="TEST_SCHEMA",
        )
        assert config.get_effective_schema() == "TEST_SCHEMA"

    def test_get_database_identifier(self) -> None:
        """Test database identifier retrieval."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )
        assert config.get_database_identifier() == "XEPDB1"

        config_with_sid = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            sid="XE",
        )
        assert config_with_sid.get_database_identifier() == "XE"

    def test_to_connection_config(self) -> None:
        """Test conversion to connection configuration."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )
        conn_config = config.to_connection_config()

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
        """Test conversion to Oracle config."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            pool_min_size=2,
            pool_max_size=10,
        )
        oracle_config = config.to_oracle_config()

        assert isinstance(oracle_config, OracleConnectionConfig)
        assert oracle_config.host == "localhost"
        assert oracle_config.username == "testuser"
        assert oracle_config.service_name == "XEPDB1"

    def test_get_performance_settings(self) -> None:
        """Test performance settings retrieval."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            pool_min_size=2,
            pool_max_size=10,
            query_timeout=300,
        )
        perf_settings = config.get_performance_settings()

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

    def test_get_dbt_settings(self) -> None:
        """Test DBT settings retrieval."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            materialization="table",
        )
        dbt_settings = config.get_dbt_settings()

        assert "database" in dbt_settings
        assert "schema" in dbt_settings
        assert "materialization" in dbt_settings
        assert dbt_settings["materialization"] == "table"


class TestConfigEdgeCases:
    """Test configuration edge cases and error conditions."""

    def test_config_with_all_optional_fields(self) -> None:
        """Test configuration with all optional fields set."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            port=1522,
            protocol="tcps",
            ssl_server_dn_match=True,
            nls_lang="AMERICAN_AMERICA.AL32UTF8",
            nls_date_format="DD/MM/YYYY",
            search_path="schema1,schema2",
            enable_metrics=True,
            log_level="DEBUG",
            enable_sql_logging=True,
            pool_min_size=1,
            pool_max_size=20,
            pool_increment=2,
            query_timeout=600,
            fetch_size=2000,
            connect_timeout=60,
            retry_attempts=5,
            retry_delay=2.0,
        )
        assert config.port == 1522
        assert config.protocol == "tcps"
        assert config.ssl_server_dn_match is True
        assert config.nls_lang == "AMERICAN_AMERICA.AL32UTF8"
        assert config.enable_metrics is True
        assert config.log_level == "DEBUG"

    def test_config_defaults_when_no_service_name_or_sid(self) -> None:
        """Test that default service name is used when neither service_name nor sid provided.

        Test that default service name is used when neither service_name nor sid provided.
        """
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
        )
        # Should use default service name from constants
        assert config.oracle_service_name is not None

    def test_config_field_validation_ranges(self) -> None:
        """Test field validation for numeric ranges."""
        # Test valid ranges
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            oracle_service_name="XEPDB1",
            port=1521,
            pool_min_size=1,
            pool_max_size=50,
            query_timeout=600,
            retry_delay=0.5,
        )
        assert config.port == 1521
        assert config.pool_min_size == 1
        assert config.pool_max_size == 50
        assert config.query_timeout == 600
        assert config.retry_delay == 0.5

    def test_config_materialization_validation_all_valid_types(self) -> None:
        """Test all valid materialization types."""
        valid_materializations: list[
            Literal["table", "view", "incremental", "snapshot"]
        ] = [
            "table",
            "view",
            "incremental",
            "snapshot",
        ]
        for materialization in valid_materializations:
            config = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=SecretStr("testpass"),
                oracle_service_name="XEPDB1",
                materialization=materialization,
            )
            assert config.materialization == materialization

    def test_config_protocol_validation_all_valid_types(self) -> None:
        """Test all valid protocol types."""
        valid_protocols: list[Literal["tcp", "tcps"]] = ["tcp", "tcps"]
        for protocol in valid_protocols:
            config = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=SecretStr("testpass"),
                oracle_service_name="XEPDB1",
                protocol=protocol,
            )
            assert config.protocol == protocol


class TestConfigConstantsUsage:
    """Test usage of configuration constants."""

    def test_config_uses_default_constants(self) -> None:
        """Test that configuration uses default constants appropriately."""
        config = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=SecretStr("testpass"),
            oracle_service_name="XEPDB1",
        )

        # Test that defaults come from constants
        assert config.port == 1521  # DEFAULT_PORT
        assert config.protocol == "tcp"  # DEFAULT_PROTOCOL
        assert config.materialization == "table"  # DEFAULT_MATERIALIZATION

        # Performance defaults
        assert config.pool_min_size >= 1
        assert config.pool_max_size >= config.pool_min_size
        assert config.query_timeout > 0
        assert config.fetch_size > 0
