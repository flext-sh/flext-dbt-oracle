"""Core model objects used by DBT Oracle workflows."""

from __future__ import annotations

from flext_meltano import m

from ._models.base import FlextDbtOracleModelsBase
from ._models.dbt import FlextDbtOracleModelsDbt


class FlextDbtOracleModels(m):
    """Namespace wrapper for DBT Oracle domain models — composes _models parts via MRO."""

    class DbtOracle(FlextDbtOracleModelsBase, FlextDbtOracleModelsDbt):
        """DbtOracle domain namespace."""


m = FlextDbtOracleModels

__all__: list[str] = ["FlextDbtOracleModels", "m"]
