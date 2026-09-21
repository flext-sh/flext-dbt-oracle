"""DBT Oracle domain type aliases composed into the typings facade."""

from __future__ import annotations

from flext_meltano import t


class FlextDbtOracleTypesDbt:
    """DBT Oracle domain type aliases."""

    type OraclePayload = t.JsonMapping
    "Oracle payload type."

    type OraclePayloadList = t.SequenceOf[OraclePayload]
    "List of Oracle payloads."


__all__: list[str] = ["FlextDbtOracleTypesDbt"]
