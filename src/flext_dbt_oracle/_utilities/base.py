"""Base utilities for DBT Oracle — MRO composition of parent utility namespaces."""

from __future__ import annotations

from flext_db_oracle import u as _db_oracle_u
from flext_meltano import u


class FlextDbtOracleUtilitiesBase(u, _db_oracle_u):
    """MRO facade composing Meltano + DbOracle utility namespaces."""

    class DbtOracle:
        """DBT Oracle domain utilities namespace."""

        # Domain utilities are declared in the facade (utilities.py)
        # This base provides the MRO composition only.


__all__: list[str] = ["FlextDbtOracleUtilitiesBase"]
