# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utility helpers for SQL and payload validation.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/utilities
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleUtilities
from flext_meltano import FlextMeltanoUtilities

from flext_dbt_oracle._utilities import (
    FlextDbtOracleUtilitiesBase,
    FlextDbtOracleUtilitiesModelBuilder,
)


class FlextDbtOracleUtilities(FlextMeltanoUtilities, FlextDbOracleUtilities):
    """Namespace for DBT Oracle utility helpers."""

    class DbtOracle(FlextDbtOracleUtilitiesBase, FlextDbtOracleUtilitiesModelBuilder):
        """DBT Oracle domain utilities namespace."""


u = FlextDbtOracleUtilities
__all__: list[str] = ["FlextDbtOracleUtilities", "u"]
