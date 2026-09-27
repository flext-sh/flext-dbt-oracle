"""Base type definitions for DBT Oracle — MRO composition of parent type namespaces."""

from __future__ import annotations

from flext_db_oracle import t as _db_oracle_t
from flext_meltano import t


class FlextDbtOracleTypesBase(t, _db_oracle_t):
    """MRO facade composing Meltano + DbOracle type namespaces."""

    # No domain-specific types are actively used via t.DbtOracle.*
    # All structured data uses Pydantic models via FlextDbtOracleModels (m).


__all__: list[str] = ["FlextDbtOracleTypesBase"]
