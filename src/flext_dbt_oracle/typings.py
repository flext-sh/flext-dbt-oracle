"""FLEXT Dbt Oracle Types — MRO composition of parent type namespaces.

Structured data uses Pydantic models via m; no domain-specific aliases are declared.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleTypes
from flext_meltano import FlextMeltanoTypes

from flext_dbt_oracle._typings.base import FlextDbtOracleTypesBase


class FlextDbtOracleTypes(FlextMeltanoTypes, FlextDbOracleTypes):
    """MRO facade composing Meltano + DbOracle type namespaces."""

    class DbtOracle(FlextDbtOracleTypesBase):
        """DbtOracle domain namespace."""


t = FlextDbtOracleTypes
__all__: list[str] = ["FlextDbtOracleTypes", "t"]
