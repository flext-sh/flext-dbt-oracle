"""Oracle adapter helpers for DBT metadata normalization."""

from __future__ import annotations

from collections.abc import Mapping

from pydantic import BaseModel, ConfigDict, Field

from .constants import c


class OracleTableAdapter(BaseModel):
    """Normalized Oracle table descriptor."""

    model_config = ConfigDict(extra="forbid")

    schema_name: str = Field(description="Oracle schema name")
    table_name: str = Field(description="Oracle table name")

    def get_relation_name(self) -> str:
        """Build canonical schema.table relation name."""
        return f"{self.schema_name}.{self.table_name}"

    def to_metadata(self) -> Mapping[str, t.JsonValue]:
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
            schema_name=schema_name.strip() or c.DbtOracle.DEFAULT_SCHEMA_NAME,
            table_name=table_name.strip(),
        )


__all__ = ["OracleTableAdapter", "OracleTableFactory"]
