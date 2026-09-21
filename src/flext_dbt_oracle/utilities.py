"""Utility helpers for SQL and payload validation."""

from __future__ import annotations

from flext_db_oracle import u as _db_oracle_u
from flext_meltano import u

from ._utilities.base import FlextDbtOracleUtilitiesBase
from ._utilities.model_builder import FlextDbtOracleUtilitiesModelBuilder


class FlextDbtOracleUtilities(u, _db_oracle_u):
    """Namespace for DBT Oracle utility helpers."""

    class DbtOracle(FlextDbtOracleUtilitiesBase, FlextDbtOracleUtilitiesModelBuilder):
        """DBT Oracle domain utilities namespace."""


__all__: list[str] = ["FlextDbtOracleUtilities", "u"]

u = FlextDbtOracleUtilities
