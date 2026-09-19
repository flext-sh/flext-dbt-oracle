"""Base protocols for DBT Oracle integration points."""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleProtocols
from flext_meltano import p


class FlextDbtOracleProtocolsBase(p, FlextDbOracleProtocols):
    """Namespace for DBT Oracle protocol contracts."""

    class DbtOracle(FlextDbOracleProtocols.DbOracle):
        """DBT Oracle protocol namespace extending the Oracle contracts."""


__all__: list[str] = ["FlextDbtOracleProtocolsBase"]
