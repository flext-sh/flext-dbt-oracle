"""Base type definitions for DBT Oracle — MRO composition of parent type namespaces."""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleTypes
from flext_meltano import t


class FlextDbtOracleTypesBase(t, FlextDbOracleTypes):
    """MRO facade composing Meltano + DbOracle type namespaces."""

    # No domain-specific types are actively used via t.DbtOracle.*
    # All structured data uses Pydantic models via FlextDbtOracleModels (m).


__all__: list[str] = ["FlextDbtOracleTypesBase"]
