"""Construction and default settings tests for Oracle DBT settings.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/_config/construction
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

# NOTE (multi-agent): mro-rn88 — settings dedup: Oracle connection scalars via
# settings.DbOracle.* (inherited); settings.DbtOracle.* holds dbt-only knobs.
from flext_db_oracle import FlextDbOracleSettings

from flext_dbt_oracle import FlextDbtOracleSettings
from tests import c, tm


class TestsFlextDbtOracleConfigConstructionPart:
    """Configuration construction coverage."""

    @staticmethod
    def test_basic_config_creation() -> None:
        """Test creating basic Oracle configuration via DbOracle namespace."""
        settings = FlextDbtOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                host="localhost",
                username="testuser",
                service_name="XEPDB1",
            ),
        )
        tm.that(settings.DbOracle.host, eq="localhost")
        tm.that(settings.DbOracle.username, eq="testuser")
        tm.that(settings.DbOracle.service_name, eq="XEPDB1")
        tm.that(settings.DbOracle.port, is_=int)
        tm.that(settings.DbOracle.port > 0, truth=True)

    @staticmethod
    def test_config_with_sid() -> None:
        """Test configuration with SID instead of service_name."""
        settings = FlextDbtOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                host="localhost",
                username="testuser",
                sid="XE",
            ),
        )
        tm.that(settings.DbOracle.host, eq="localhost")
        tm.that(settings.DbOracle.username, eq="testuser")
        tm.that(settings.DbOracle.sid, eq="XE")

    @staticmethod
    def test_config_defaults_when_no_service_name_or_sid() -> None:
        """Test default service name when neither service_name nor sid is provided."""
        settings = FlextDbtOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                host="localhost",
                username="testuser",
            ),
        )
        tm.that(settings.DbOracle.service_name, none=False)

    @staticmethod
    def test_config_uses_default_constants() -> None:
        """Use the upstream Oracle namespace and declared dbt materializations."""
        settings = FlextDbtOracleSettings()
        db = tm.instance(settings.DbOracle, FlextDbOracleSettings.DbOracleSettings)
        tm.that(db.port, is_=int)
        tm.that(db.port > 0, truth=True)
        tm.that(
            settings.DbtOracle.materialization in c.DbtOracle.Dbt.Materialization,
            truth=True,
        )
        tm.that(db.pool_min, is_=int)
        tm.that(db.pool_max, is_=int)
