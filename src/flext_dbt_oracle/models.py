"""Core model objects used by DBT Oracle workflows.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/models
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoModels

from flext_dbt_oracle._models.base import FlextDbtOracleModelsBase
from flext_dbt_oracle._models.dbt import FlextDbtOracleModelsDbt


class FlextDbtOracleModels(FlextMeltanoModels, FlextDbtOracleModelsBase):
    """Namespace wrapper for DBT Oracle domain models via _models MRO parts."""

    class DbtOracle(FlextDbtOracleModelsBase, FlextDbtOracleModelsDbt):
        """DbtOracle domain namespace."""


m = FlextDbtOracleModels

__all__: list[str] = ["FlextDbtOracleModels", "m"]
