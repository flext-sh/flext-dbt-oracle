"""Base model definitions for DBT Oracle — MRO composition of parent model namespaces."""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleModels
from flext_meltano import m


class FlextDbtOracleModelsBase(m, FlextDbOracleModels):
    """MRO facade composing Meltano + DbOracle model namespaces."""


__all__: list[str] = ["FlextDbtOracleModelsBase"]
