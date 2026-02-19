"""Oracle adapter helpers for DBT metadata normalization."""

from __future__ import annotations

from dataclasses import dataclass

type JsonScalar = str | int | float | bool | None
type JsonValue = JsonScalar | dict[str, JsonValue] | list[JsonValue]


@dataclass(slots=True)
class OracleTableAdapter:
    """Normalized Oracle table descriptor."""

    schema_name: str
    table_name: str

    def get_relation_name(self) -> str:
        """Build canonical schema.table relation name."""
        return f"{self.schema_name}.{self.table_name}"

    def to_metadata(self) -> dict[str, JsonValue]:
        """Convert adapter fields into structured metadata."""
        return {
            "schema": self.schema_name,
            "table": self.table_name,
            "relation": self.get_relation_name(),
        }


class OracleTableFactory:
    """Factory for creating Oracle table adapters."""

    @staticmethod
    def create(schema_name: str, table_name: str) -> OracleTableAdapter:
        """Create adapter with trimmed, normalized names."""
        return OracleTableAdapter(
            schema_name=schema_name.strip() or "public",
            table_name=table_name.strip(),
        )


__all__ = ["OracleTableAdapter", "OracleTableFactory"]
