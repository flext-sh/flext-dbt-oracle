"""DBT Oracle protocols — thin MRO facade.

Protocols are defined in _protocols.base and re-exported here.
"""

from __future__ import annotations

from ._protocols.base import FlextDbtOracleProtocolsBase, FlextDbtOracleProtocols, p

__all__: list[str] = ["FlextDbtOracleProtocolsBase", "FlextDbtOracleProtocols", "p"]
