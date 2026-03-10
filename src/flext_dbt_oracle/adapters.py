"""Oracle adapter helpers for DBT metadata normalization."""

from __future__ import annotations

from flext_dbt_oracle import c


class OracleTableFactory:
    """Factory for creating Oracle table adapters."""

    @staticmethod
    def create(schema_name: str, table_name: str) -> OracleTableAdapter:  # noqa: F821
        """Create adapter with trimmed, normalized names."""
        return OracleTableAdapter(  # noqa: F821
            schema_name=schema_name.strip() or c.DbtOracle.DEFAULT_SCHEMA_NAME,
            table_name=table_name.strip(),
        )


__all__ = ["OracleTableAdapter", "OracleTableFactory"]  # noqa: F822
