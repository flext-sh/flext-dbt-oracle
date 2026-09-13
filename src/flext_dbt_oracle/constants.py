"""DBT Oracle constants — thin MRO facade.

Constants are defined in _constants.base and re-exported here.
"""

from __future__ import annotations

from ._constants.base import FlextDbtOracleConstantsBase, FlextDbtOracleConstants, c

__all__: list[str] = ["FlextDbtOracleConstantsBase", "FlextDbtOracleConstants", "c"]
