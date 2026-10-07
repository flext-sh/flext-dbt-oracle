"""DBT Oracle protocols for FLEXT ecosystem.

The 8 inner ``DbtOracle.*`` Protocol classes that previously lived here
(``Dbt``, ``OracleIntegration``, ``Modeling``, ``Transformation``, ``Macro``,
``Quality``, ``Performance``, ``Monitoring``) had **zero workspace consumers**
— no implementations, no isinstance/runtime-checkable dispatch, no static
type-checking sites, only stale generated docs. Per AGENTS.md §3.5 (no dead
code) + the standing STRICT YAGNI directive they were deleted; the canonical
``FlextDbtOracleProtocols`` facade remains intact (re-exported via ``p``) and
composes the parent ``FlextDbOracleProtocols.DbOracle`` protocol namespace
through its own ``DbtOracle`` namespace.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/protocols
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleProtocols
from flext_meltano import FlextMeltanoProtocols

from flext_dbt_oracle._protocols.base import FlextDbtOracleProtocolsBase


class FlextDbtOracleProtocols(FlextMeltanoProtocols, FlextDbOracleProtocols):
    """DBT Oracle protocols facade — composes Oracle and Meltano protocols."""

    class DbtOracle(FlextDbtOracleProtocolsBase, FlextDbOracleProtocols.DbOracle):
        """DBT Oracle protocol namespace composing the parent contracts."""


p = FlextDbtOracleProtocols

__all__: list[str] = ["FlextDbtOracleProtocols", "p"]
