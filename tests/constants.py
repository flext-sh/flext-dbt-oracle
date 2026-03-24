"""Test constants for flext-dbt-oracle tests.

Provides FlextDbtOracleTestConstants, extending FlextTestsConstants with
flext-dbt-oracle-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleConstants
from flext_meltano import FlextMeltanoConstants
from flext_tests import FlextTestsConstants


class FlextDbtOracleTestConstants(
    FlextTestsConstants, FlextDbOracleConstants, FlextMeltanoConstants,
):
    """Test constants for flext-dbt-oracle."""


c = FlextDbtOracleTestConstants
__all__ = ["FlextDbtOracleTestConstants", "c"]
