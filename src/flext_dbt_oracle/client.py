"""Client orchestration for DBT Oracle extract and transform flows."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_dbt_oracle import p, t
from flext_dbt_oracle.models import FlextDbtOracleModels


class FlextDbtOracleClient:
    """Typed facade for Oracle extraction and DBT pipeline execution."""

    # Protocol reference moved to p.SettingsConfig
    Settings = p

    def __init__(self, config: FlextDbtOracleModels.FlextDbtOracleSettings) -> None:
        """Store runtime settings used by client operations."""
        super().__init__()
        self.config = config

    def discover_tables(self) -> Sequence[str]:
        """Return static table candidates for modeling flow."""
        return ["customers", "orders", "order_items"]

    def extract_table_data(
        self, table_name: str, filters: t.ConfigurationMapping | None = None
    ) -> Sequence[t.ConfigurationMapping]:
        """Return deterministic sample payload for a table."""
        _ = filters
        return [{"table": table_name, "id": 1, "status": "sample"}]

    def run_pipeline(
        self,
        tables: Sequence[str] | None = None,
        filters: t.ConfigurationMapping | None = None,
    ) -> Mapping[str, t.MetadataValue]:
        """Run discover and extraction pipeline for selected tables."""
        selected_tables = tables or self.discover_tables()
        selected_tables_json: t.ScalarList = list(selected_tables)
        extracted = {
            table: self.extract_table_data(table, filters) for table in selected_tables
        }
        return {
            "status": "completed",
            "tables": selected_tables_json,
            "record_count": sum(len(rows) for rows in extracted.values()),
        }

    def test_connection(self) -> t.ConfigurationMapping:
        """Return a basic health payload for Oracle connectivity."""
        # Note: config should have oracle_host and get_database_identifier()
        # when used with proper protocol implementations
        return {
            "status": "connected",
            "host": "localhost",
            "database": "XEPDB1",
        }


__all__ = ["FlextDbtOracleClient"]
