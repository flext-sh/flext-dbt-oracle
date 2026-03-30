"""Test models for flext-dbt-oracle.

Provides FlextDbtOracleTestModels, combining FlextTestsModels with
FlextDbtOracleModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_dbt_oracle import FlextDbtOracleModels


class FlextDbtOracleTestModels(
    FlextTestsModels,
    FlextDbtOracleModels,
):
    """Test models combining FlextTestsModels with flext-dbt-oracle models."""

    class Tests(FlextTestsModels.Tests):
        """Project-specific test fixtures namespace."""

        class DbtOracle:
            """DBT Oracle-specific test fixtures."""


m = FlextDbtOracleTestModels

__all__ = [
    "FlextDbtOracleTestModels",
    "m",
]
