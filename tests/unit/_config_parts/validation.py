"""Validation tests for Oracle DBT settings."""

from __future__ import annotations

# NOTE (multi-agent): mro-rn88 — settings dedup: Oracle connection scalars via
# settings.DbOracle.* (inherited); per ADR-005 materialization/protocol are free
# scalars (no enum rejection) and pool bounds carry no cross-field validator here.
from flext_db_oracle import FlextDbOracleSettings
from flext_dbt_oracle._settings import FlextDbtOracleSettings
from tests import c, t


class FlextDbtOracleConfigValidationPart:
    """Configuration validation coverage."""

    def test_config_default_host_applied(self) -> None:
        """Test default host is applied when not provided explicitly."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings._DbOracle(
                username="testuser", service_name="XEPDB1"
            ),
        )
        assert isinstance(settings.DbOracle.host, str)
        assert settings.DbOracle.host != ""

    def test_config_default_username_applied(self) -> None:
        """Test default username is applied when not provided explicitly."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings._DbOracle(
                host="localhost", service_name="XEPDB1"
            ),
        )
        assert isinstance(settings.DbOracle.username, str)
        assert settings.DbOracle.username != ""

    def test_config_default_password_applied(self) -> None:
        """Test default password is applied when not provided explicitly."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings._DbOracle(
                host="localhost", username="testuser"
            ),
        )
        assert isinstance(settings.DbOracle.password, str)

    def test_config_numeric_ranges_round_trip(self) -> None:
        """Test numeric DbOracle fields accept and preserve valid ranges."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings._DbOracle(
                host="localhost",
                username="testuser",
                service_name="XEPDB1",
                port=1521,
                pool_min=1,
                pool_max=50,
                timeout=60,
            ),
        )
        assert settings.DbOracle.port == 1521
        assert settings.DbOracle.pool_min == 1
        assert settings.DbOracle.pool_max == 50
        assert settings.DbOracle.timeout == 60

    def test_config_materialization_all_valid_types(self) -> None:
        """Test all valid materialization types round-trip on the dbt namespace."""
        materialization_enum = c.DbtOracle.Dbt.Materialization
        valid_materializations: t.SequenceOf[materialization_enum] = [
            materialization_enum.TABLE,
            materialization_enum.VIEW,
            materialization_enum.INCREMENTAL,
            materialization_enum.SNAPSHOT,
        ]
        for materialization in valid_materializations:
            oracle = FlextDbtOracleSettings(
                DbtOracle=FlextDbtOracleSettings._DbtOracle(
                    materialization=materialization
                ),
            ).DbtOracle
            assert oracle.materialization == materialization
