"""Validation tests for Oracle DBT settings.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/_config_parts/validation
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

# NOTE (multi-agent): mro-rn88 — settings dedup: Oracle connection scalars via
# settings.DbOracle.* (inherited); per ADR-005 materialization/protocol are free
# scalars (no enum rejection) and pool bounds carry no cross-field validator here.
from flext_db_oracle import FlextDbOracleSettings
from flext_tests import tm


class TestsFlextDbtOracleConfigValidationPart:
    """Configuration validation coverage."""

    @staticmethod
    def test_config_default_host_applied() -> None:
        """Test default host is applied when not provided explicitly."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                username="testuser",
                service_name="XEPDB1",
            ),
        )
        tm.that(settings.DbOracle.host, is_=str)
        tm.that(settings.DbOracle.host, ne="")

    @staticmethod
    def test_config_default_username_applied() -> None:
        """Test default username is applied when not provided explicitly."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                host="localhost",
                service_name="XEPDB1",
            ),
        )
        tm.that(settings.DbOracle.username, is_=str)
        tm.that(settings.DbOracle.username, ne="")

    @staticmethod
    def test_config_default_password_applied() -> None:
        """Test default password is applied when not provided explicitly."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                host="localhost",
                username="testuser",
            ),
        )
        tm.that(settings.DbOracle.password, is_=str)
