"""Test protocol definitions for flext-dbt-oracle.

Provides TestsFlextDbtOracleProtocols, combining p with
FlextDbtOracleProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import p

from flext_dbt_oracle.protocols import FlextDbtOracleProtocols


class TestsFlextDbtOracleProtocols(p, FlextDbtOracleProtocols):
    """Test protocols combining p and FlextDbtOracleProtocols.

    Provides access to:
    - p.Tests.Docker.* (from p)
    - p.Tests.Factory.* (from p)
    - p.DbtOracle.* (from FlextDbtOracleProtocols)
    """

    class Tests(p.Tests):
        """Project-specific test protocols.

        Extends p.Tests with DbtOracle-specific protocols.
        """

        class DbtOracle:
            """DbtOracle-specific test protocols."""


__all__ = ["TestsFlextDbtOracleProtocols", "p"]

p = TestsFlextDbtOracleProtocols
