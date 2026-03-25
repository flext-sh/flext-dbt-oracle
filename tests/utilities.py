"""Test utilities for flext-dbt-oracle.

Provides FlextDbtOracleTestUtilities, combining FlextTestsUtilities with
FlextDbtOracleUtilities for test-specific utility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_dbt_oracle import FlextDbtOracleUtilities


class FlextDbtOracleTestUtilities(
    FlextTestsUtilities,
    FlextDbtOracleUtilities,
):
    """Test utilities combining FlextTestsUtilities with flext-dbt-oracle utilities."""


u = FlextDbtOracleTestUtilities
__all__ = ["FlextDbtOracleTestUtilities", "u"]
