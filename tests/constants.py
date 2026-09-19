"""Test constants for flext-dbt-oracle tests.

Provides TestsFlextDbtOracleConstants, extending FlextTestsConstants with
flext-dbt-oracle-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_tests import c as tests_c

from flext_dbt_oracle import c


class TestsFlextDbtOracleConstants(c, tests_c):
    """Test constants for flext-dbt-oracle."""

    class DbtOracle(c.DbtOracle):
        """DbtOracle test constants namespace."""

        class Tests:
            """Test-specific constants."""

            PROJECT_ROOT_PARENT_DEPTH: Final[int] = 1
            SRC_DIR: Final[str] = "src"
            PACKAGE_DIR: Final[str] = "flext_dbt_oracle"

    class Tests(tests_c.Tests):
        """Test-scoped constants facade."""


c = TestsFlextDbtOracleConstants

__all__: list[str] = ["TestsFlextDbtOracleConstants", "c"]
