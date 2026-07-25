"""DBT Oracle protocols for FLEXT ecosystem.

The 8 inner ``DbtOracle.*`` Protocol classes that previously lived here
(``Dbt``, ``OracleIntegration``, ``Modeling``, ``Transformation``, ``Macro``,
``Quality``, ``Performance``, ``Monitoring``) had **zero workspace consumers**
— no implementations, no isinstance/runtime-checkable dispatch, no static
type-checking sites, only stale generated docs. Per AGENTS.md §3.5 (no dead
code) + the standing STRICT YAGNI directive they were deleted; the canonical
``FlextDbtOracleProtocols`` facade remains intact (re-exported via ``p``) and
inherits its actual behavior from the parent ``FlextDbOracleProtocols`` +
``FlextMeltanoProtocols`` MRO chain.
"""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleProtocols
from flext_meltano import p


class FlextDbtOracleProtocols(p, FlextDbOracleProtocols):
    """DBT Oracle protocols facade — composes Oracle and Meltano protocols."""


__all__: list[str] = ["FlextDbtOracleProtocols", "p"]

p = FlextDbtOracleProtocols
