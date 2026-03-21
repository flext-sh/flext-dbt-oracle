"""Oracle adapter helpers for DBT metadata normalization."""

from __future__ import annotations

from flext_dbt_oracle.models import FlextDbtOracleModels

# Re-export from models facade
OracleTableAdapter = FlextDbtOracleModels.OracleTableAdapter
OracleTableFactory = FlextDbtOracleModels.OracleTableFactory


__all__ = ["OracleTableAdapter", "OracleTableFactory"]
