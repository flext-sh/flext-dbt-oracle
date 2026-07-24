"""Connection mapping tests for Oracle DBT settings."""

from __future__ import annotations

# NOTE (multi-agent): mro-rn88 — settings dedup: connection identifiers/dsn come from
# the typed m.DbtOracle.OracleConnectionConfig model; schema from settings.DbtOracle.
from flext_dbt_oracle import FlextDbtOracleSettings, m
from flext_tests import tm


class FlextDbtOracleConfigConnectionPart:
    """Connection string and mapping coverage."""

    def test_dsn_masks_password_and_uses_service_separator(self) -> None:
        """Service-name DSN uses '/' and never leaks the password."""
        credential = "testpass"
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            username="testuser",
            password=credential,
            service_name="XEPDB1",
        )
        tm.that(
            config.dsn,
            eq=(
                f"tcp://testuser:***@localhost:{config.port}/{config.database_identifier}"
            ),
        )
        tm.that(config.dsn, lacks=credential)

    def test_dsn_uses_colon_separator_with_sid(self) -> None:
        """SID DSN uses ':' as the identifier separator."""
        credential = "testpass"
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost", username="testuser", password=credential, sid="XE"
        )
        tm.that(config.dsn, eq=f"tcp://testuser:***@localhost:{config.port}:XE")

    def test_effective_schema_from_dbt_namespace(self) -> None:
        """The effective schema is the DbtOracle.schema_name scalar."""
        oracle = FlextDbtOracleSettings(
            DbtOracle={"schema_name": "TEST_SCHEMA"}
        ).DbtOracle
        tm.that(oracle.schema_name, eq="TEST_SCHEMA")

    def test_database_identifier_prefers_sid(self) -> None:
        """database_identifier resolves from service_name, or SID when present."""
        config = m.DbtOracle.OracleConnectionConfig(service_name="XEPDB1")
        tm.that(config.database_identifier, eq="XEPDB1")
        config_with_sid = m.DbtOracle.OracleConnectionConfig(
            service_name="XEPDB1", sid="XE"
        )
        tm.that(config_with_sid.database_identifier, eq="XE")

    def test_connection_config_carries_identity_fields(self) -> None:
        """The typed connection config exposes the supplied identity fields."""
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost", username="testuser", service_name="XEPDB1"
        )
        tm.that(config.host, eq="localhost")
        tm.that(config.username, eq="testuser")
        tm.that(config.service_name, eq="XEPDB1")
