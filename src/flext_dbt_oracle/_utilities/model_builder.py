"""Deterministic DBT staging-model metadata generation for DBT Oracle."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_dbt_oracle import c, m

if TYPE_CHECKING:
    from flext_meltano import t


class FlextDbtOracleUtilitiesModelBuilder:
    """DBT Oracle staging-model metadata generation utilities."""

    class ModelBuilder:
        """Deterministic DBT staging-model metadata generation."""

        @staticmethod
        def generate_staging_models(
            source_tables: t.StrSequence,
        ) -> t.SequenceOf[m.DbtOracle.Model]:
            """Create one staging model definition per source table."""
            return [
                m.DbtOracle.Model(
                    name=f"stg_oracle_{table}",
                    table_name=f"stg_{table}",
                    sql_content=c.DbtOracle.Dbt.STAGING_SELECT_TEMPLATE.format(
                        table=table
                    ),
                    description=f"Staging model for {table}",
                )
                for table in source_tables
            ]


__all__: list[str] = ["FlextDbtOracleUtilitiesModelBuilder"]
