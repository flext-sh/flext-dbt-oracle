"""Validation tests for Oracle DBT settings."""

from __future__ import annotations

# NOTE (multi-agent): mro-rn88 — settings dedup: Oracle connection scalars via
# settings.DbOracle.* (inherited); per ADR-005 materialization/protocol are free
# scalars (no enum rejection) and pool bounds carry no cross-field validator here.
from flext_db_oracle import FlextDbOracleSettings
from flext_dbt_oracle import FlextDbtOracleSettings
from flext_tests import tm
from tests import c, t


class FlextDbtOracleConfigValidationPart:
    """Configuration validation coverage."""

    def test_config_default_host_applied(self) -> None:
        """Test default host is applied when not provided explicitly."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(username="testuser", service_name="XEPDB1")
        )
        tm.that(settings.DbOracle.host, is_=str)
        tm.that(settings.DbOracle.host, ne="")

    def test_config_default_username_applied(self) -> None:
        """Test default username is applied when not provided explicitly."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(host="localhost", service_name="XEPDB1")
        )
        tm.that(settings.DbOracle.username, is_=str)
        tm.that(settings.DbOracle.username, ne="")

    def test_config_default_password_applied(self) -> None:
        """Test default password is applied when not provided explicitly."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(host="localhost", username="testuser")
        )
        tm.that(settings.DbOracle.password, is_=str)

    def test_config_numeric_ranges_round_trip(self) -> None:
        """Test numeric DbOracle fields accept and preserve valid ranges."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                host="localhost",
                username="testuser",
                service_name="XEPDB1",
                port=1521,
                pool_min=1,
                pool_max=50,
                timeout=60,
            )
        )
        tm.that(settings.DbOracle.port, eq=1521)
        tm.that(settings.DbOracle.pool_min, eq=1)
        tm.that(settings.DbOracle.pool_max, eq=50)
        tm.that(settings.DbOracle.timeout, eq=60)

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
            oracle = FlextDbtOracleSettings.model_validate(
                {"DbtOracle": {"materialization": materialization}}
            ).DbtOracle
            tm.that(oracle.materialization, eq=materialization)
