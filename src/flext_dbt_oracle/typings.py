"""FLEXT Dbt Oracle Types — MRO composition of parent type namespaces.

Only OraclePayload and OraclePayloadList are domain-specific and actively used
(in protocols.py). All other structured data uses Pydantic models via m.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_db_oracle import FlextDbOracleTypes
from flext_meltano import FlextMeltanoTypes


class FlextDbtOracleTypes(FlextMeltanoTypes, FlextDbOracleTypes):
    """MRO facade composing Meltano + DbOracle type namespaces."""

    class DbtOracle:
        """DbtOracle domain namespace for actively used type definitions."""

        type OraclePayload = Mapping[str, FlextMeltanoTypes.Primitives | None]
        "Oracle payload type."
        type OraclePayloadList = Sequence[OraclePayload]
        "List of Oracle payloads."


t = FlextDbtOracleTypes
__all__ = [
    "FlextDbtOracleTypes",
    "t",
]
