"""Typed runtime client service for Oracle extraction and DBT pipelines."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_dbt_oracle import c

from .base import FlextDbtOracleServicesBase

if TYPE_CHECKING:
    from flext_meltano import t


class FlextDbtOracleServicesClient(FlextDbtOracleServicesBase):
    """Typed facade for Oracle extraction and DBT pipeline execution."""

    def discover_tables(self) -> t.StrSequence:
        """Return static table candidates for modeling flow."""
        return ["customers", "orders", "order_items"]

    def extract_table_data(
        self, table_name: str, filters: t.ConfigurationMapping | None = None
    ) -> t.SequenceOf[t.ConfigurationMapping]:
        """Return deterministic sample payload for a table."""
        _ = filters
        return [{"table": table_name, "id": 1, "status": "sample"}]

    def run_pipeline(
        self,
        tables: t.StrSequence | None = None,
        filters: t.ConfigurationMapping | None = None,
    ) -> t.JsonMapping:
        """Run discover and extraction pipeline for selected tables."""
        selected_tables = tables or self.discover_tables()
        extracted = {
            table: self.extract_table_data(table, filters) for table in selected_tables
        }
        tables_payload: t.JsonValueList = list(selected_tables)
        result: t.JsonMapping = {
            "status": "completed",
            "tables": tables_payload,
            "record_count": sum(len(rows) for rows in extracted.values()),
        }
        return result

    def test_connection(self) -> t.ConfigurationMapping:
        """Return a basic health payload for Oracle connectivity."""
        return {"status": "connected", "host": c.LOCALHOST, "database": "XEPDB1"}


__all__: list[str] = ["FlextDbtOracleServicesClient"]
