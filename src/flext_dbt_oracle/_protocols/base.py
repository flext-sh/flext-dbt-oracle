"""DBT Oracle protocols facade — composes Oracle and Meltano protocols.

The 8 inner Protocol classes that previously lived here
had zero workspace consumers — no implementations, no isinstance/runtime-checkable
dispatch, no static type-checking sites, only stale generated docs.
Per AGENTS.md §3.5 (no dead code) + YAGNI they were deleted; the canonical
FlextDbtOracleProtocols facade remains intact (re-exported via p) and
inherits its actual behavior from the parent FlextDbOracleProtocols +
FlextMeltanoProtocols MRO chain.
"""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleProtocols
from flext_meltano import p


class FlextDbtOracleProtocolsBase(p, FlextDbOracleProtocols):
    """DBT Oracle protocols facade — composes Oracle and Meltano protocols."""


class FlextDbtOracleProtocols(FlextDbtOracleProtocolsBase):
    """Facade re-exporting all protocol families."""

    class DbtOracle(FlextDbtOracleProtocolsBase):
        pass


p = FlextDbtOracleProtocols

__all__: list[str] = ["FlextDbtOracleProtocolsBase", "FlextDbtOracleProtocols", "p"]
