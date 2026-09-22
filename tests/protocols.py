"""Test protocol definitions for flext-dbt-oracle.

Provides TestsFlextDbtOracleProtocols, combining FlextTestsProtocols with
FlextDbtOracleProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import p as tests_p

from flext_dbt_oracle import p


class TestsFlextDbtOracleProtocols(tests_p, p):
    """Test protocols combining FlextTestsProtocols and FlextDbtOracleProtocols."""

    class Tests(tests_p.Tests):
        """Test-scoped protocol contracts facade."""


p = TestsFlextDbtOracleProtocols

__all__: list[str] = ["TestsFlextDbtOracleProtocols", "p"]
