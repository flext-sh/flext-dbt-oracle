"""Base model definitions for DBT Oracle — MRO composition of parent model namespaces."""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleModels


class FlextDbtOracleModelsBase(FlextDbOracleModels):
    """MRO facade composing the DbOracle model namespace for DBT Oracle."""


__all__: list[str] = ["FlextDbtOracleModelsBase"]
