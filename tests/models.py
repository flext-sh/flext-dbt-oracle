"""Test models for flext-dbt-oracle.

Provides TestsFlextDbtOracleModels, combining FlextTestsModels with
FlextDbtOracleModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_dbt_oracle import FlextDbtOracleModels


class TestsFlextDbtOracleModels(
    FlextTestsModels,
    FlextDbtOracleModels,
):
    """Test models combining FlextTestsModels with flext-dbt-oracle models."""

    class DbtOracle(FlextDbtOracleModels.DbtOracle):
        """DbtOracle test models namespace."""

        class Tests:
            """Test-specific models."""


m = TestsFlextDbtOracleModels

__all__ = [
    "TestsFlextDbtOracleModels",
    "m",
]
