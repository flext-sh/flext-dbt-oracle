"""Connection mapping tests for Oracle DBT settings."""

from __future__ import annotations

# NOTE (multi-agent): mro-rn88 — settings dedup: connection identifiers/dsn come from
# the typed m.DbtOracle.OracleConnectionConfig model; schema from settings.DbtOracle.
from flext_dbt_oracle import m
from flext_dbt_oracle._settings import FlextDbtOracleSettings


class FlextDbtOracleConfigConnectionPart:
    """Connection string and mapping coverage."""

    def test_dsn_masks_password_and_uses_service_separator(self) -> None:
        """Service-name DSN uses '/' and never leaks the password."""
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            username="testuser",
            password="testpass",
            service_name="XEPDB1",
        )
        assert config.dsn == (
            f"tcp://testuser:***@localhost:{config.port}/{config.database_identifier}"
        )
        assert "testpass" not in config.dsn

    def test_dsn_uses_colon_separator_with_sid(self) -> None:
        """SID DSN uses ':' as the identifier separator."""
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            username="testuser",
            password="testpass",
            sid="XE",
        )
        assert config.dsn == f"tcp://testuser:***@localhost:{config.port}:XE"

    def test_effective_schema_from_dbt_namespace(self) -> None:
        """The effective schema is the DbtOracle.schema_name scalar."""
        oracle = FlextDbtOracleSettings(
            DbtOracle=FlextDbtOracleSettings._DbtOracle(schema_name="TEST_SCHEMA"),
        ).DbtOracle
        assert oracle.schema_name == "TEST_SCHEMA"

    def test_database_identifier_prefers_sid(self) -> None:
        """database_identifier resolves from service_name, or SID when present."""
        config = m.DbtOracle.OracleConnectionConfig(service_name="XEPDB1")
        assert config.database_identifier == "XEPDB1"
        config_with_sid = m.DbtOracle.OracleConnectionConfig(
            service_name="XEPDB1",
            sid="XE",
        )
        assert config_with_sid.database_identifier == "XE"

    def test_connection_config_carries_identity_fields(self) -> None:
        """The typed connection config exposes the supplied identity fields."""
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            username="testuser",
            service_name="XEPDB1",
        )
        assert config.host == "localhost"
        assert config.username == "testuser"
        assert config.service_name == "XEPDB1"
