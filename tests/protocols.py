"""Test protocol definitions for flext-dbt-oracle.

Provides FlextDbtOracleTestProtocols, combining FlextTestsProtocols with
FlextDbtOracleProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleProtocols
from flext_meltano import FlextMeltanoProtocols
from flext_tests import FlextTestsProtocols

from flext_dbt_oracle.protocols import FlextDbtOracleProtocols


class FlextDbtOracleTestProtocols(
    FlextTestsProtocols,
    FlextDbtOracleProtocols,
    FlextDbOracleProtocols,
    FlextMeltanoProtocols,
):
    """Test protocols combining FlextTestsProtocols and FlextDbtOracleProtocols."""

    class DbtOracle(FlextDbtOracleProtocols.DbtOracle):
        """DbtOracle test protocols namespace."""

        class Tests:
            """DbtOracle-specific test protocols."""


p = FlextDbtOracleTestProtocols
__all__ = ["FlextDbtOracleTestProtocols", "p"]
