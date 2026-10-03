"""FLEXT Dbt Oracle Types — MRO composition of parent type namespaces.

Only OraclePayload and OraclePayloadList are domain-specific and actively used
(in protocols.py). All other structured data uses Pydantic models via m.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleTypes
from flext_meltano import FlextMeltanoTypes

from ._typings.base import FlextDbtOracleTypesBase
from ._typings.dbt import FlextDbtOracleTypesDbt


class FlextDbtOracleTypes(FlextMeltanoTypes, FlextDbOracleTypes):
    """MRO facade composing Meltano + DbOracle type namespaces."""

    class DbtOracle(FlextDbtOracleTypesBase, FlextDbtOracleTypesDbt):
        """DbtOracle domain namespace for actively used type definitions."""


t = FlextDbtOracleTypes
__all__: list[str] = ["FlextDbtOracleTypes", "t"]
