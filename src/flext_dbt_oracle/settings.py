"""Settings model used by DBT Oracle runtime components."""

from __future__ import annotations

from flext_dbt_oracle.connections import (
    OracleConnectionConfig,
    build_oracle_connection_config,
)
from flext_dbt_oracle.models import FlextDbtOracleModels

# Re-export from models facade
FlextDbtOracleSettings = FlextDbtOracleModels.FlextDbtOracleSettings


__all__ = [
    "FlextDbtOracleSettings",
    "OracleConnectionConfig",
    "build_oracle_connection_config",
]
