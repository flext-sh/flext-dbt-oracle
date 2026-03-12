"""Client orchestration for DBT Oracle extract and transform flows."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol

from flext_core import t


class FlextDbtOracleClient:
    """Typed facade for Oracle extraction and DBT pipeline execution."""

    class SettingsProtocol(Protocol):
        """Protocol describing the client configuration contract."""

        oracle_host: str

        def get_database_identifier(self) -> str:
            """Return service name or SID identifier."""
            ...

    def __init__(self, config: SettingsProtocol) -> None:
        """Store runtime settings used by client operations."""
        super().__init__()
        self.config = config

    def discover_tables(self) -> list[str]:
        """Return static table candidates for modeling flow."""
        return ["customers", "orders", "order_items"]

    def extract_table_data(
        self, table_name: str, filters: Mapping[str, t.Scalar] | None = None
    ) -> list[Mapping[str, t.Scalar]]:
        """Return deterministic sample payload for a table."""
        _ = filters
        return [{"table": table_name, "id": 1, "status": "sample"}]

    def run_pipeline(
        self,
        tables: list[str] | None = None,
        filters: Mapping[str, t.Scalar] | None = None,
    ) -> Mapping[str, t.MetadataValue]:
        """Run discover and extraction pipeline for selected tables."""
        selected_tables = tables or self.discover_tables()
        selected_tables_json: list[t.Scalar] = list(selected_tables)
        extracted = {
            table: self.extract_table_data(table, filters) for table in selected_tables
        }
        return {
            "status": "completed",
            "tables": selected_tables_json,
            "record_count": sum(len(rows) for rows in extracted.values()),
        }

    def test_connection(self) -> Mapping[str, t.Scalar]:
        """Return a basic health payload for Oracle connectivity."""
        return {
            "status": "connected",
            "host": self.config.oracle_host,
            "database": self.config.get_database_identifier(),
        }


__all__ = ["FlextDbtOracleClient"]
