"""Construction and default settings tests for Oracle DBT settings."""

from __future__ import annotations

from flext_dbt_oracle.settings import FlextDbtOracleSettings
from tests import c, t


class FlextDbtOracleConfigConstructionPart:
    """Configuration construction coverage."""

    def test_basic_config_creation(self) -> None:
        """Test creating basic Oracle configuration."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
            oracle_service_name="XEPDB1",
        )
        assert settings.oracle_host == "localhost"
        assert settings.oracle_username == "testuser"
        assert settings.oracle_service_name == "XEPDB1"
        assert isinstance(settings.port, int)
        assert settings.port > 0

    def test_config_with_sid(self) -> None:
        """Test configuration with SID instead of service_name."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
            sid="XE",
        )
        assert settings.oracle_host == "localhost"
        assert settings.oracle_username == "testuser"
        assert settings.sid == "XE"

    def test_config_with_all_optional_fields(self) -> None:
        """Test configuration with all optional fields set."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
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
        """Test default service name when neither service_name nor sid is provided."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
        )
        assert settings.oracle_service_name is not None

    def test_config_uses_default_constants(self) -> None:
        """Test that configuration uses default constants appropriately."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
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
