"""DBT Oracle types — thin MRO facade.

Types are defined in _typings.base and re-exported here.
"""

from __future__ import annotations

from ._typings.base import FlextDbtOracleTypesBase, FlextDbtOracleTypes, t

__all__: list[str] = ["FlextDbtOracleTypesBase", "FlextDbtOracleTypes", "t"]
