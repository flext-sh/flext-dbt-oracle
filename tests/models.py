"""Test models for flext-dbt-oracle.

Provides TestsFlextDbtOracleModels, combining FlextTestsModels with
FlextDbtOracleModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import m as tests_m

from flext_dbt_oracle import m


class TestsFlextDbtOracleModels(tests_m, m):
    """Test models combining FlextTestsModels with flext-dbt-oracle models."""

    class DbtOracle(m.DbtOracle):
        """DbtOracle test models namespace."""

        class Tests:
            """Test-specific models."""

    class Tests(tests_m.Tests):
        """Test-scoped models facade."""


m = TestsFlextDbtOracleModels

__all__: list[str] = ["TestsFlextDbtOracleModels", "m"]
