"""Utility helpers for SQL and payload validation."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_db_oracle import FlextDbOracleUtilities
from flext_meltano import FlextMeltanoUtilities

from flext_dbt_oracle import t


class FlextDbtOracleUtilities(FlextMeltanoUtilities, FlextDbOracleUtilities):
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
            def validate_non_empty_rows(rows: Sequence[Mapping[str, t.Scalar]]) -> bool:
                """Return true when row list contains values."""
                return bool(rows)


__all__ = ["FlextDbtOracleUtilities", "u"]

u = FlextDbtOracleUtilities
