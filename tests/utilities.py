"""Test utilities for flext-dbt-oracle.

Provides TestsFlextDbtOracleUtilities, combining FlextTestsUtilities with
FlextDbtOracleUtilities for test-specific utility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import u as tests_u

from flext_dbt_oracle import u


class TestsFlextDbtOracleUtilities(tests_u, u):
    """Test utilities combining FlextTestsUtilities with flext-dbt-oracle utilities."""

    class DbtOracle(u.DbtOracle):
        """DbtOracle test utilities namespace."""

        class Tests:
            """Test-specific utilities."""

    class Tests(tests_u.Tests):
        """Test-scoped utilities facade."""


u = TestsFlextDbtOracleUtilities

__all__: list[str] = ["TestsFlextDbtOracleUtilities", "u"]
