"""DBT Oracle protocols for FLEXT ecosystem.

The 8 inner ``DbtOracle.*`` Protocol classes that previously lived here
(``Dbt``, ``OracleIntegration``, ``Modeling``, ``Transformation``, ``Macro``,
``Quality``, ``Performance``, ``Monitoring``) had **zero workspace consumers**
— no implementations, no isinstance/runtime-checkable dispatch, no static
type-checking sites, only stale generated docs. Per AGENTS.md §3.5 (no dead
code) + the standing STRICT YAGNI directive they were deleted; the canonical
``FlextDbtOracleProtocols`` facade remains intact (re-exported via ``p``) and
composes its actual behavior from the parent ``FlextDbOracleProtocols`` facade
plus the local private protocol namespace.
"""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleProtocols as db_oracle_p
from flext_meltano import p

from ._protocols.base import FlextDbtOracleProtocolsBase


class FlextDbtOracleProtocols(p, db_oracle_p):
    """DBT Oracle protocols facade — composes Oracle and Meltano protocols."""

    class DbtOracle(
        FlextDbtOracleProtocolsBase.DbtOracle,
        db_oracle_p.DbOracle,
    ):
        """DbtOracle protocol namespace."""


p = FlextDbtOracleProtocols

__all__: list[str] = ["FlextDbtOracleProtocols", "p"]
