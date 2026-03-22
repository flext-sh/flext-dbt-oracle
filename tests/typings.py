"""Test type definitions for flext-dbt-oracle.

Provides FlextDbtOracleTestTypes, combining FlextTestsTypes with
FlextDbtOracleTypes for test-specific type definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_dbt_oracle import FlextDbtOracleTypes


class FlextDbtOracleTestTypes(FlextTestsTypes, FlextDbtOracleTypes):
    """Test types combining FlextTestsTypes with flext-dbt-oracle types."""


t = FlextDbtOracleTestTypes
__all__ = ["FlextDbtOracleTestTypes", "t"]
