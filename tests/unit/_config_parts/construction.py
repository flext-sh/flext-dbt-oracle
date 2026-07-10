"""Construction and default settings tests for Oracle DBT settings."""

from __future__ import annotations

# NOTE (multi-agent): mro-rn88 — settings dedup: Oracle connection scalars via
# settings.DbOracle.* (inherited); settings.DbtOracle.* holds dbt-only knobs.
from flext_db_oracle import FlextDbOracleSettings
from flext_dbt_oracle._settings import FlextDbtOracleSettings


class FlextDbtOracleConfigConstructionPart:
    """Configuration construction coverage."""

    def test_basic_config_creation(self) -> None:
        """Test creating basic Oracle configuration via DbOracle namespace."""
        settings = FlextDbOracleSettings(
            DbOracle={
                "host": "localhost",
                "username": "testuser",
                "service_name": "XEPDB1",
            },
        )
        assert settings.DbOracle.host == "localhost"
        assert settings.DbOracle.username == "testuser"
        assert settings.DbOracle.service_name == "XEPDB1"
        assert isinstance(settings.DbOracle.port, int)
        assert settings.DbOracle.port > 0

    def test_config_with_sid(self) -> None:
        """Test configuration with SID instead of service_name."""
        settings = FlextDbOracleSettings(
            DbOracle={"host": "localhost", "username": "testuser", "sid": "XE"},
        )
        assert settings.DbOracle.host == "localhost"
        assert settings.DbOracle.username == "testuser"
        assert settings.DbOracle.sid == "XE"

    def test_config_with_all_dbt_optional_fields(self) -> None:
        """Test dbt configuration with all optional knobs set."""
        oracle = FlextDbtOracleSettings(
            DbtOracle={
                "nls_lang": "AMERICAN_AMERICA.AL32UTF8",
                "nls_date_format": "DD/MM/YYYY",
                "search_path": "schema1,schema2",
                "enable_metrics": True,
                "dbt_log_level": "DEBUG",
                "enable_sql_logging": True,
            },
        ).DbtOracle
        assert oracle.nls_lang == "AMERICAN_AMERICA.AL32UTF8"
        assert oracle.nls_date_format == "DD/MM/YYYY"
        assert oracle.enable_metrics is True
        assert oracle.dbt_log_level == "DEBUG"
        assert oracle.enable_sql_logging is True

    def test_config_defaults_when_no_service_name_or_sid(self) -> None:
        """Test default service name when neither service_name nor sid is provided."""
        settings = FlextDbOracleSettings(
            DbOracle={"host": "localhost", "username": "testuser"},
        )
        assert settings.DbOracle.service_name is not None

    def test_config_uses_default_constants(self) -> None:
        """Test that configuration uses default constants appropriately."""
        settings = FlextDbtOracleSettings()
        assert isinstance(settings.DbOracle.port, int)
        assert settings.DbOracle.port > 0
        assert settings.DbtOracle.materialization in {
            "table",
            "view",
            "incremental",
            "snapshot",
        }
        assert settings.DbOracle.pool_min >= 1
        assert settings.DbOracle.pool_max >= settings.DbOracle.pool_min
