"""Base utilities for DBT Oracle — MRO composition of parent utility namespaces."""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleUtilities
from flext_meltano import u


class FlextDbtOracleUtilitiesBase(u, FlextDbOracleUtilities):
    """MRO facade composing Meltano + DbOracle utility namespaces."""

    class DbtOracle:
        """DBT Oracle domain utilities namespace."""

        # Domain utilities are declared in the facade (utilities.py)
        # This base provides the MRO composition only.


__all__: list[str] = ["FlextDbtOracleUtilitiesBase"]
