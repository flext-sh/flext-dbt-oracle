"""Utility helpers for SQL and payload validation."""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleUtilities
from flext_meltano import FlextMeltanoUtilities

from ._utilities.base import FlextDbtOracleUtilitiesBase
from ._utilities.model_builder import FlextDbtOracleUtilitiesModelBuilder


class FlextDbtOracleUtilities(FlextMeltanoUtilities, FlextDbOracleUtilities):
    """Namespace for DBT Oracle utility helpers."""

    class DbtOracle(FlextDbtOracleUtilitiesBase, FlextDbtOracleUtilitiesModelBuilder):
        """DBT Oracle domain utilities namespace."""


u = FlextDbtOracleUtilities

__all__: list[str] = ["FlextDbtOracleUtilities", "u"]
