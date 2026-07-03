"""Test protocol definitions for flext-dbt-oracle.

Provides TestsFlextDbtOracleProtocols, combining FlextTestsProtocols with
FlextDbtOracleProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_dbt_oracle import FlextDbtOracleProtocols


class TestsFlextDbtOracleProtocols(
    FlextTestsProtocols,
    FlextDbtOracleProtocols,
):
    """Test protocols combining FlextTestsProtocols and FlextDbtOracleProtocols."""


p = TestsFlextDbtOracleProtocols

__all__: list[str] = ["TestsFlextDbtOracleProtocols", "p"]
