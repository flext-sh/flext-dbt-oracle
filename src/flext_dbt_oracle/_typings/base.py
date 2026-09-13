"""DBT Oracle type definitions — MRO composition of parent type namespaces.

Only OraclePayload and OraclePayloadList are domain-specific and actively used
(in protocols.py). All other structured data uses Pydantic models via m.
"""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleTypes
from flext_meltano import t


class FlextDbtOracleTypesBase(t):
    """MRO facade composing Meltano + DbOracle type namespaces."""

    class DbtOracle:
        """DbtOracle domain namespace for actively used type definitions."""

        type OraclePayload = t.JsonMapping
        "Oracle payload type."
        type OraclePayloadList = t.SequenceOf[OraclePayload]
        "List of Oracle payloads."


class FlextDbtOracleTypes(FlextDbtOracleTypesBase):
    """Facade re-exporting all type families."""

    class DbtOracle(FlextDbtOracleTypesBase.DbtOracle):
        pass


t = FlextDbtOracleTypes
__all__: list[str] = ["FlextDbtOracleTypesBase", "FlextDbtOracleTypes", "t"]
