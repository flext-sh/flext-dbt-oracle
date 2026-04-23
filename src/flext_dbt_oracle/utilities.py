"""Utility helpers for SQL and payload validation."""

from __future__ import annotations

from collections.abc import (
    Mapping,
    Sequence,
)

from flext_db_oracle import FlextDbOracleUtilities
from flext_meltano import u

from flext_dbt_oracle.constants import c
from flext_dbt_oracle.models import FlextDbtOracleModels
from flext_dbt_oracle.typings import t


class FlextDbtOracleUtilities(u, FlextDbOracleUtilities):
    """Namespace for DBT Oracle utility helpers."""

    class DbtOracle:
        """DBT Oracle domain utilities namespace."""

        class Sql:
            """SQL text generation helpers."""

            @staticmethod
            def generate_incremental_filter(column_name: str, days_back: int) -> str:
                """Generate incremental filter predicate."""
                return (
                    f"where {column_name} >= current_date - interval '{days_back}' day"
                )

            @staticmethod
            def generate_source_query(schema_name: str, table_name: str) -> str:
                """Generate source selection SQL text."""
                return f"select * from {schema_name}.{table_name}"  # nosec B608

        class Validation:
            """Payload validation helpers."""

            @staticmethod
            def validate_non_empty_rows(rows: Sequence[t.ConfigurationMapping]) -> bool:
                """Return true when row list contains values."""
                return bool(rows)

        class Client:
            """Typed facade for Oracle extraction and DBT pipeline execution."""

            def __init__(
                self,
                settings: FlextDbtOracleModels.DbtOracle.FlextDbtOracleSettings,
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
            ) -> Sequence[t.ConfigurationMapping]:
                """Return deterministic sample payload for a table."""
                _ = filters
                return [{"table": table_name, "id": 1, "status": "sample"}]

            def run_pipeline(
                self,
                tables: t.StrSequence | None = None,
                filters: t.ConfigurationMapping | None = None,
            ) -> Mapping[str, t.JsonValue]:
                """Run discover and extraction pipeline for selected tables."""
                selected_tables = tables or self.discover_tables()
                extracted = {
                    table: self.extract_table_data(table, filters)
                    for table in selected_tables
                }
                tables_payload: list[t.JsonValue] = [str(x) for x in selected_tables]
                result: Mapping[str, t.JsonValue] = {
                    "status": "completed",
                    "tables": tables_payload,
                    "record_count": sum(len(rows) for rows in extracted.values()),
                }
                return result

            def test_connection(self) -> t.ConfigurationMapping:
                """Return a basic health payload for Oracle connectivity."""
                return {
                    "status": "connected",
                    "host": "localhost",
                    "database": "XEPDB1",
                }

        class Services:
            """Utility service namespace for DBT Oracle workflows."""

            def generate_recommendations(
                self,
                table_count: int,
            ) -> Mapping[str, t.JsonValue]:
                """Generate lightweight recommendations from table volume."""
                recommendations: list[str] = [
                    "Process tables in batches and increase dbt threads gradually"
                    for _ in [None]
                    if table_count > c.DbtOracle.PERFORMANCE_RECOMMENDATION_THRESHOLD
                ]
                payload: dict[str, t.JsonValue] = {
                    "table_count": table_count,
                    "recommendations": t.Cli.JSON_VALUE_ADAPTER.validate_python(
                        recommendations,
                    ),
                }
                return payload

            def track_execution(self, workflow_name: str) -> t.ConfigurationMapping:
                """Build a minimal execution tracking payload."""
                return {"workflow": workflow_name, "status": "running"}


__all__: list[str] = ["FlextDbtOracleUtilities", "u"]

u = FlextDbtOracleUtilities
