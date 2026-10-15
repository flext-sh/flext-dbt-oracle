"""Test constants for flext-dbt-oracle tests.

Provides TestsFlextDbtOracleConstants, extending FlextTestsConstants with
flext-dbt-oracle-specific constants.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_tests import FlextTestsConstants

from flext_dbt_oracle import FlextDbtOracleConstants


class TestsFlextDbtOracleConstants(FlextDbtOracleConstants, FlextTestsConstants):
    """Test constants for flext-dbt-oracle."""

    class DbtOracle(FlextDbtOracleConstants.DbtOracle):
        """DbtOracle test constants namespace."""

        class Tests(FlextTestsConstants.Tests):
            """DbtOracle-specific test constants."""

            PROJECT_ROOT_PARENT_DEPTH: ClassVar[int] = 1


c = TestsFlextDbtOracleConstants

__all__: list[str] = ["TestsFlextDbtOracleConstants", "c"]
