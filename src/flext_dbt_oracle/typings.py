"""FLEXT Dbt Oracle Types — MRO composition of parent type namespaces.

Only OraclePayload and OraclePayloadList are domain-specific and actively used
(in protocols.py). All other structured data uses Pydantic models via m.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Mapping,
    Sequence,
)
from typing import Literal

from flext_core import u
from flext_db_oracle import FlextDbOracleTypes
from flext_meltano import t

from flext_dbt_oracle.constants import c


class FlextDbtOracleTypes(t, FlextDbOracleTypes):
    """MRO facade composing Meltano + DbOracle type namespaces."""

    SCALAR_LIST_ADAPTER: u.TypeAdapter[Sequence[t.Scalar]] = u.TypeAdapter(
        Sequence[t.Scalar]
    )
    PRIMITIVES_MAPPING_ADAPTER: u.TypeAdapter[Mapping[str, t.Primitives]] = (
        u.TypeAdapter(Mapping[str, t.Primitives])
    )

    class DbtOracle:
        """DbtOracle domain namespace for actively used type definitions."""

        type Materialization = c.DbtOracle.Dbt.Materialization
        "Supported DBT materialization strategies."
        type LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        "Supported runtime log levels."
        type OraclePayload = t.JsonMapping
        "Oracle payload type."
        type OraclePayloadList = Sequence[OraclePayload]
        "List of Oracle payloads."


t = FlextDbtOracleTypes
__all__: list[str] = [
    "FlextDbtOracleTypes",
    "t",
]
