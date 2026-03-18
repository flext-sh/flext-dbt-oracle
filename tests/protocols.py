"""Test protocol definitions for flext-dbt-oracle.

Provides TestsFlextDbtOracleProtocols, combining FlextTestsProtocols with
FlextDbtOracleProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import p

from flext_dbt_oracle.protocols import FlextDbtOracleProtocols


class TestsFlextDbtOracleProtocols(FlextTestsProtocols, FlextDbtOracleProtocols):
    """Test protocols combining FlextTestsProtocols and FlextDbtOracleProtocols.

    Provides access to:
    - p.Tests.Docker.* (from FlextTestsProtocols)
    - p.Tests.Factory.* (from FlextTestsProtocols)
    - p.DbtOracle.* (from FlextDbtOracleProtocols)
    """

    class Tests(FlextTestsProtocols.Tests):
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with DbtOracle-specific protocols.
        """

        class DbtOracle:
            """DbtOracle-specific test protocols."""


__all__ = ["TestsFlextDbtOracleProtocols", "p"]

p = TestsFlextDbtOracleProtocols
