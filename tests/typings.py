"""Test type definitions for flext-dbt-oracle.

Provides TestsFlextDbtOracleTypes, combining FlextTestsTypes with
FlextDbtOracleTypes for test-specific type definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_dbt_oracle import FlextDbtOracleTypes


class TestsFlextDbtOracleTypes(FlextTestsTypes, FlextDbtOracleTypes):
    """Test types combining FlextTestsTypes with flext-dbt-oracle types."""

    class DbtOracle(FlextDbtOracleTypes.DbtOracle):
        """DbtOracle test types namespace."""

        class Tests:
            """Test-specific type aliases."""


t = TestsFlextDbtOracleTypes

__all__ = ["TestsFlextDbtOracleTypes", "t"]
