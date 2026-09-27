"""Base protocols for DBT Oracle integration points."""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class FlextDbtOracleProtocolsBase(Protocol):
    """Base DBT Oracle protocol part composed by the protocols facade."""


__all__: list[str] = ["FlextDbtOracleProtocolsBase"]
