"""Connection mapping tests for Oracle DBT settings."""

from __future__ import annotations

from flext_dbt_oracle.settings import FlextDbtOracleSettings
from tests import c, t


class FlextDbtOracleConfigConnectionPart:
    """Connection string and mapping coverage."""

    def test_connection_string(self) -> None:
        """Test connection string generation."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
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
            oracle_password=t.SecretStr("testpass").get_secret_value(),
            sid="XE",
        )
        conn_str = settings.connection_string
        assert conn_str == f"oracle://testuser:***@localhost:{settings.port}:XE"

    def test_effective_schema(self) -> None:
        """Test effective schema retrieval."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
            oracle_service_name="XEPDB1",
            schema_name="TEST_SCHEMA",
        )
        assert settings.effective_schema == "TEST_SCHEMA"

    def test_database_identifier(self) -> None:
        """Test database identifier retrieval."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
            oracle_service_name="XEPDB1",
        )
        assert settings.database_identifier in {"XEPDB1", "XE"}
        config_with_sid = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
            sid="XE",
        )
        assert config_with_sid.database_identifier == "XE"

    def test_to_connection_config(self) -> None:
        """Test conversion to connection configuration."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
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
            oracle_password=t.SecretStr("testpass").get_secret_value(),
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
            oracle_password=t.SecretStr("testpass").get_secret_value(),
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
            oracle_password=t.SecretStr("testpass").get_secret_value(),
            oracle_service_name="XEPDB1",
            materialization=c.DbtOracle.Dbt.Materialization.TABLE,
        )
        dbt_settings = settings.dbt_settings
        assert "database" in dbt_settings
        assert "schema" in dbt_settings
        assert "materialization" in dbt_settings
        assert dbt_settings["materialization"] == "table"
