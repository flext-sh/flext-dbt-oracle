"""Construction and default settings tests for Oracle DBT settings."""

from __future__ import annotations

# NOTE (multi-agent): mro-rn88 — settings dedup: Oracle connection scalars via
# settings.DbOracle.* (inherited); settings.DbtOracle.* holds dbt-only knobs.
from flext_db_oracle import FlextDbOracleSettings
from flext_dbt_oracle import FlextDbtOracleSettings
from flext_tests import tm


class FlextDbtOracleConfigConstructionPart:
    """Configuration construction coverage."""

    def test_basic_config_creation(self) -> None:
        """Test creating basic Oracle configuration via DbOracle namespace."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                host="localhost", username="testuser", service_name="XEPDB1"
            )
        )
        tm.that(settings.DbOracle.host, eq="localhost")
        tm.that(settings.DbOracle.username, eq="testuser")
        tm.that(settings.DbOracle.service_name, eq="XEPDB1")
        tm.that(settings.DbOracle.port, is_=int)
        assert settings.DbOracle.port > 0

    def test_config_with_sid(self) -> None:
        """Test configuration with SID instead of service_name."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                host="localhost", username="testuser", sid="XE"
            )
        )
        tm.that(settings.DbOracle.host, eq="localhost")
        tm.that(settings.DbOracle.username, eq="testuser")
        tm.that(settings.DbOracle.sid, eq="XE")

    def test_config_with_all_dbt_optional_fields(self) -> None:
        """Test dbt configuration with all optional knobs set."""
        oracle = FlextDbtOracleSettings.model_validate({
            "DbtOracle": {
                "nls_lang": "AMERICAN_AMERICA.AL32UTF8",
                "nls_date_format": "DD/MM/YYYY",
                "search_path": "schema1,schema2",
                "enable_metrics": True,
                "dbt_log_level": "DEBUG",
                "enable_sql_logging": True,
            }
        }).DbtOracle
        tm.that(oracle.nls_lang, eq="AMERICAN_AMERICA.AL32UTF8")
        tm.that(oracle.nls_date_format, eq="DD/MM/YYYY")
        tm.that(oracle.enable_metrics, eq=True)
        tm.that(oracle.dbt_log_level, eq="DEBUG")
        tm.that(oracle.enable_sql_logging, eq=True)

    def test_config_defaults_when_no_service_name_or_sid(self) -> None:
        """Test default service name when neither service_name nor sid is provided."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                host="localhost", username="testuser"
            )
        )
        tm.that(settings.DbOracle.service_name, none=False)

    def test_config_uses_default_constants(self) -> None:
        """Test that configuration uses default constants appropriately."""
        settings = FlextDbtOracleSettings()
        tm.that(settings.DbOracle.port, is_=int)
        assert settings.DbOracle.port > 0
        tm.that(
            {"table", "view", "incremental", "snapshot"},
            has=settings.DbtOracle.materialization,
        )
        assert settings.DbOracle.pool_min >= 1
        assert settings.DbOracle.pool_max >= settings.DbOracle.pool_min
