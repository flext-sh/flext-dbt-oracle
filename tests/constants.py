"""Test constants for flext-dbt-oracle tests.

Provides TestsFlextDbtOracleConstants, extending FlextTestsConstants with
flext-dbt-oracle-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_dbt_oracle import FlextDbtOracleConstants


class TestsFlextDbtOracleConstants(
    FlextTestsConstants,
    FlextDbtOracleConstants,
):
    """Test constants for flext-dbt-oracle."""

    class DbtOracle(FlextDbtOracleConstants.DbtOracle):
        """DbtOracle test constants namespace."""

        class Tests:
            """Test-specific constants."""


c = TestsFlextDbtOracleConstants

__all__: list[str] = ["TestsFlextDbtOracleConstants", "c"]
