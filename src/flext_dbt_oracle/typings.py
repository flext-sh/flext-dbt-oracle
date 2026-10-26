# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Dbt Oracle Types — MRO composition of parent type namespaces.

Structured data uses Pydantic models via m; no domain-specific aliases are declared.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_db_oracle import t
from flext_meltano import t as flext_meltano_t

from flext_dbt_oracle._typings import FlextDbtOracleTypesBase


class FlextDbtOracleTypes(flext_meltano_t, t):
    """MRO facade composing Meltano + DbOracle type namespaces."""

    class DbtOracle(FlextDbtOracleTypesBase):
        """DbtOracle domain namespace."""


t = FlextDbtOracleTypes
__all__: list[str] = ["FlextDbtOracleTypes", "t"]
