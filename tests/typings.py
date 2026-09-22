"""Test type definitions for flext-dbt-oracle.

Provides TestsFlextDbtOracleTypes, combining FlextTestsTypes with
FlextDbtOracleTypes for test-specific type definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import t as tests_t

from flext_dbt_oracle import t


class TestsFlextDbtOracleTypes(tests_t, t):
    """Test types combining FlextTestsTypes with flext-dbt-oracle types."""

    class DbtOracle(t.DbtOracle):
        """DbtOracle test types namespace."""

        class Tests:
            """Test-specific type aliases."""

    class Tests(tests_t.Tests):
        """Test-scoped type aliases facade."""


t = TestsFlextDbtOracleTypes

__all__: list[str] = ["TestsFlextDbtOracleTypes", "t"]
