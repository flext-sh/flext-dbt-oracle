"""Base protocols for DBT Oracle integration points."""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleProtocols
from flext_meltano import p


class FlextDbtOracleProtocolsBase(p, FlextDbOracleProtocols):
    """Namespace for DBT Oracle protocol contracts."""

    class DbtOracle:
        """DBT Oracle protocol namespace."""


__all__: list[str] = ["FlextDbtOracleProtocolsBase"]
