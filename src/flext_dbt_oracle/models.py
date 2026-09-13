"""DBT Oracle models — thin MRO facade.

Models are defined in _models.base and re-exported here.
"""

from __future__ import annotations

from ._models.base import FlextDbtOracleModelsBase, FlextDbtOracleModels, m

__all__: list[str] = ["FlextDbtOracleModelsBase", "FlextDbtOracleModels", "m"]
