"""Utility helpers for SQL and payload validation."""

from __future__ import annotations

from flext_db_oracle import FlextDbOracleUtilities
from flext_dbt_oracle.constants import c
from flext_dbt_oracle.settings import FlextDbtOracleSettings
from flext_dbt_oracle.typings import t
from flext_meltano import u


class FlextDbtOracleUtilities(u, FlextDbOracleUtilities):
    """Namespace for DBT Oracle utility helpers."""

    class DbtOracle:
        """DBT Oracle domain utilities namespace."""

        class Client:
            """Typed facade for Oracle extraction and DBT pipeline execution."""

            def __init__(
                self,
                settings: FlextDbtOracleSettings,
            ) -> None:
                """Store runtime settings used by client operations."""
                super().__init__()
                self.settings = settings

            def discover_tables(self) -> t.StrSequence:
                """Return static table candidates for modeling flow."""
                return ["customers", "orders", "order_items"]

            def extract_table_data(
                self,
                table_name: str,
                filters: t.ConfigurationMapping | None = None,
            ) -> t.SequenceOf[t.ConfigurationMapping]:
                """Return deterministic sample payload for a table."""
                _ = filters
                return [{"table": table_name, "id": 1, "status": "sample"}]

            def run_pipeline(
                self,
                tables: t.StrSequence | None = None,
                filters: t.ConfigurationMapping | None = None,
            ) -> t.MappingKV[str, t.JsonValue]:
                """Run discover and extraction pipeline for selected tables."""
                selected_tables = tables or self.discover_tables()
                extracted = {
                    table: self.extract_table_data(table, filters)
                    for table in selected_tables
                }
                tables_payload: list[t.JsonValue] = list(selected_tables)
                result: t.MappingKV[str, t.JsonValue] = {
                    "status": "completed",
                    "tables": tables_payload,
                    "record_count": sum(len(rows) for rows in extracted.values()),
                }
                return result

            def test_connection(self) -> t.ConfigurationMapping:
                """Return a basic health payload for Oracle connectivity."""
                return {
                    "status": "connected",
                    "host": c.LOCALHOST,
                    "database": "XEPDB1",
                }


__all__: list[str] = ["FlextDbtOracleUtilities", "u"]

u = FlextDbtOracleUtilities
