"""Oracle adapter helpers for DBT metadata normalization."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field

from flext_dbt_oracle import c


class OracleTableAdapter(BaseModel):
    """Adapter for Oracle table metadata normalization."""

    schema_name: Annotated[str, Field(description="Oracle schema name")]
    table_name: Annotated[str, Field(description="Oracle table name")]

    def get_relation_name(self) -> str:
        """Return fully qualified relation name as schema.table."""
        return f"{self.schema_name}.{self.table_name}"

    def to_metadata(self) -> dict[str, str]:
        """Return metadata dict with schema, table, and relation."""
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
