"""Base utilities for DBT Oracle — MRO composition of parent utility namespaces.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/_utilities/base
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_db_oracle import u as _db_oracle_u
from flext_meltano import u


class FlextDbtOracleUtilitiesBase(u, _db_oracle_u):
    """MRO facade composing Meltano + DbOracle utility namespaces."""


__all__: list[str] = ["FlextDbtOracleUtilitiesBase"]
