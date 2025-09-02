"""DBT model management for Oracle transformations.

Provides programmatic DBT model generation and management for Oracle data sources.
Integrates with flext-db-oracle for schema analysis and flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar

import yaml
from flext_core import FlextLogger, FlextModels, FlextResult
from flext_db_oracle import (
    FlextDbOracleApi,
    FlextDbOracleTable as FlextOracleObject,
)

from flext_dbt_oracle.dbt_config import FlextDbtOracleConfig

logger = FlextLogger(__name__)


class FlextDbtOracleModel(FlextModels):
    """Value object representing a DBT Oracle model.

    Immutable representation of a generated DBT model with Oracle-specific metadata.
    """

    name: str
    dbt_model_type: str  # staging, intermediate, marts
    schema_name: str
    table_name: str
    columns: list[dict[str, object]]
    materialization: str
    sql_content: str
    description: str
    oracle_source: str
    dependencies: list[str]

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate DBT model business rules."""
        try:
            if not self.name.strip():
                return FlextResult[None].fail("Model name cannot be empty")
            if self.dbt_model_type not in {"staging", "intermediate", "marts"}:
                return FlextResult[None].fail("Invalid model_type")
            if not self.schema_name.strip() or not self.table_name.strip():
                return FlextResult[None].fail("Schema and table names are required")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Model validation failed: {e}")

    def get_file_path(self, base_path: Path) -> Path:
        """Get the file path for this model."""
        return base_path / f"models/{self.dbt_model_type}/{self.name}.sql"

    def get_schema_file_path(self, base_path: Path) -> Path:
        """Get the schema.yml file path for this model."""
        return base_path / f"models/{self.dbt_model_type}/schema.yml"

    def to_sql_file(self) -> str:
        """Generate SQL file content for this model."""
        header = f"""{{{{
  config(
    materialized='{self.materialization}',
    schema='{self.schema_name}'
  )
}}}}

/*
  DBT model: {self.name}
  Description: {self.description}
  Oracle source: {self.oracle_source}
  Generated automatically by flext-dbt-oracle
*/

"""
        return header + self.sql_content

    def to_schema_entry(self) -> dict[str, object]:
        """Generate schema.yml entry for this model."""
        return {
            "name": self.name,
            "description": self.description,
            "columns": [
                {
                    "name": col["name"],
                    "description": col.get(
                        "description",
                        f"{col['name']} from Oracle {self.oracle_source}",
                    ),
                    "data_type": col.get("data_type", "string"),
                    "tests": col.get("tests", []),
                }
                for col in self.columns
            ],
        }


class FlextDbtOracleModelGenerator:
    """Generator for DBT Oracle models.

    Programmatically generates DBT models from Oracle database objects
    using flext-db-oracle API and configuration patterns.
    """

    # Model templates by type
    STAGING_TEMPLATE: ClassVar[str] = """
select
{columns}
from {source_reference}
"""

    INTERMEDIATE_TEMPLATE: ClassVar[str] = """
select
{columns}
from {{ ref('{upstream_model}') }}
where {filter_conditions}
"""

    MARTS_TEMPLATE: ClassVar[str] = """
select
{aggregated_columns}
from {{ ref('{upstream_model}') }}
group by {group_by_columns}
"""

    # Oracle-specific column mappings
    ORACLE_DATA_TYPE_TESTS: ClassVar[dict[str, list[str]]] = {
        "string": ["not_null"],
        "numeric": ["not_null", "positive"],
        "timestamp": ["not_null"],
        "float": ["not_null"],
    }

    def __init__(
        self,
        config: FlextDbtOracleConfig,
        oracle_api: FlextDbOracleApi,
    ) -> None:
        """Initialize model generator.

        Args:
            config: DBT Oracle configuration
            oracle_api: Oracle API instance

        """
        self.config = config
        self.oracle_api = oracle_api
        logger.info("Initialized DBT Oracle model generator")

    def generate_staging_models(
        self,
        oracle_objects: list[FlextOracleObject],
    ) -> FlextResult[list[FlextDbtOracleModel]]:
        """Generate staging models from Oracle objects.

        Args:
            oracle_objects: List of Oracle objects to model

        Returns:
            FlextResult containing list of generated staging models

        """
        try:
            logger.info(
                "Generating staging models for %d Oracle objects",
                len(oracle_objects),
            )

            staging_models = []

            for oracle_obj in oracle_objects:
                try:
                    # Get column information using flext-db-oracle API
                    columns_result = self.oracle_api.get_columns(
                        oracle_obj.name,
                        oracle_obj.schema_name,
                    )
                    if not columns_result.success:
                        logger.warning(
                            "Failed to get columns for object %s: %s",
                            oracle_obj.name,
                            columns_result.error,
                        )
                        continue

                    columns = columns_result.value or []

                    # Generate model
                    model = self._create_staging_model(oracle_obj, columns)
                    if model:
                        staging_models.append(model)

                except Exception as e:
                    logger.warning(
                        "Error generating model for %s: %s",
                        oracle_obj.name,
                        e,
                    )
                    continue

            logger.info("Generated %d staging models", len(staging_models))
            return FlextResult[list[FlextDbtOracleModel]].ok(staging_models)

        except Exception as e:
            logger.exception("Error generating staging models")
            return FlextResult[list[FlextDbtOracleModel]].fail(
                f"Staging model generation failed: {e}",
            )

    def generate_intermediate_models(
        self,
        staging_models: list[FlextDbtOracleModel],
    ) -> FlextResult[list[FlextDbtOracleModel]]:
        """Generate intermediate models from staging models.

        Args:
            staging_models: List of staging models to build upon

        Returns:
            FlextResult containing list of generated intermediate models

        """
        try:
            logger.info(
                "Generating intermediate models from %d staging models",
                len(staging_models),
            )

            intermediate_models = []

            # Group staging models by schema/domain
            schema_groups: dict[str, list[FlextDbtOracleModel]] = {}
            for model in staging_models:
                schema = model.schema_name
                if schema not in schema_groups:
                    schema_groups[schema] = []
                schema_groups[schema].append(model)

            # Generate intermediate models for each schema
            for schema_name, models in schema_groups.items():
                intermediate_model = self._create_intermediate_model(
                    schema_name,
                    models,
                )
                if intermediate_model:
                    intermediate_models.append(intermediate_model)

            logger.info("Generated %d intermediate models", len(intermediate_models))
            return FlextResult[list[FlextDbtOracleModel]].ok(intermediate_models)

        except Exception as e:
            logger.exception("Error generating intermediate models")
            return FlextResult[list[FlextDbtOracleModel]].fail(
                f"Intermediate model generation failed: {e}",
            )

    def generate_marts_models(
        self,
        intermediate_models: list[FlextDbtOracleModel],
    ) -> FlextResult[list[FlextDbtOracleModel]]:
        """Generate marts models from intermediate models.

        Args:
            intermediate_models: List of intermediate models to build upon

        Returns:
            FlextResult containing list of generated marts models

        """
        try:
            logger.info(
                "Generating marts models from %d intermediate models",
                len(intermediate_models),
            )

            marts_models = []

            for intermediate_model in intermediate_models:
                marts_model = self._create_marts_model(intermediate_model)
                if marts_model:
                    marts_models.append(marts_model)

            logger.info("Generated %d marts models", len(marts_models))
            return FlextResult[list[FlextDbtOracleModel]].ok(marts_models)

        except Exception as e:
            logger.exception("Error generating marts models")
            return FlextResult[list[FlextDbtOracleModel]].fail(
                f"Marts model generation failed: {e}",
            )

    def write_models_to_disk(
        self,
        models: list[FlextDbtOracleModel],
        output_path: Path,
    ) -> FlextResult[dict[str, int]]:
        """Write generated models to disk.

        Args:
            models: List of models to write
            output_path: Base output directory

        Returns:
            FlextResult containing write statistics

        """
        try:
            logger.info("Writing %d models to disk at %s", len(models), output_path)

            written_files = 0
            written_schemas = 0

            # Ensure output directories exist
            for model_type in ["staging", "intermediate", "marts"]:
                (output_path / "models" / model_type).mkdir(parents=True, exist_ok=True)

            # Group models by type for schema file generation
            models_by_type: dict[str, list[FlextDbtOracleModel]] = {}
            for model in models:
                if model.dbt_model_type not in models_by_type:
                    models_by_type[model.dbt_model_type] = []
                models_by_type[model.dbt_model_type].append(model)

            # Write SQL files and collect schema entries
            for model in models:
                # Write SQL file
                sql_file_path = model.get_file_path(output_path)
                sql_file_path.write_text(model.to_sql_file(), encoding="utf-8")
                written_files += 1

                logger.debug("Wrote model file: %s", sql_file_path)

            # Write schema.yml files
            for model_type, type_models in models_by_type.items():
                schema_file_path = output_path / "models" / model_type / "schema.yml"

                schema_content = {
                    "version": 2,
                    "models": [model.to_schema_entry() for model in type_models],
                }

                # Write YAML content
                with schema_file_path.open("w", encoding="utf-8") as f:
                    yaml.safe_dump(
                        schema_content,
                        f,
                        default_flow_style=False,
                        sort_keys=False,
                    )

                written_schemas += 1
                logger.debug("Wrote schema file: %s", schema_file_path)

            statistics = {
                "sql_files": written_files,
                "schema_files": written_schemas,
                "total_models": len(models),
            }

            logger.info("Successfully wrote models to disk: %s", statistics)
            return FlextResult[dict[str, int]].ok(statistics)

        except Exception as e:
            logger.exception("Error writing models to disk")
            return FlextResult[dict[str, int]].fail(
                f"Model writing failed: {e}",
            )

    def _create_staging_model(
        self,
        oracle_obj: FlextOracleObject,
        columns: list[dict[str, object]],
    ) -> FlextDbtOracleModel | None:
        """Create a staging model from an Oracle object."""
        try:
            # Generate column definitions
            column_defs = []
            dbt_columns: list[dict[str, object]] = []

            for col in columns:
                oracle_type_raw = col.get("data_type", "VARCHAR2")
                dbt_type = self.config.get_dbt_type_for_oracle_type(
                    str(oracle_type_raw),
                )

                # Map Oracle column name using config
                oracle_name = str(col.get("column_name", ""))
                dbt_name = self.config.oracle_column_mapping.get(
                    oracle_name,
                    oracle_name.lower(),
                )

                # Generate column SQL with casting if needed
                if dbt_type != "string":
                    column_def = f"    cast({oracle_name} as {dbt_type}) as {dbt_name}"
                else:
                    column_def = f"    {oracle_name} as {dbt_name}"

                column_defs.append(column_def)

                # Add to DBT column metadata
                dbt_columns.append(
                    {
                        "name": dbt_name,
                        "description": f"Oracle column {oracle_name} mapped to {dbt_name}",
                        "data_type": dbt_type,
                        "tests": self.ORACLE_DATA_TYPE_TESTS.get(
                            dbt_type,
                            ["not_null"],
                        ),
                    },
                )

            # Generate SQL content
            sql_content = self.STAGING_TEMPLATE.format(
                columns=",\n".join(column_defs),
                source_reference=f'{{ source("oracle", "{oracle_obj.schema_name}.{oracle_obj.name}") }}',
            ).strip()

            # Determine materialization
            materialization = self.config.get_materialization_for_layer("staging")

            # Create model
            return FlextDbtOracleModel(
                name=f"stg_{oracle_obj.schema_name}_{oracle_obj.name}".lower(),
                model_type="staging",
                schema_name=oracle_obj.schema_name,
                table_name=oracle_obj.name,
                columns=dbt_columns,
                materialization=materialization,
                sql_content=sql_content,
                description=(
                    f"Staging model for Oracle table {oracle_obj.schema_name}.{oracle_obj.name}"
                ),
                oracle_source=f"{oracle_obj.schema_name}.{oracle_obj.name}",
                dependencies=[],
            )

        except Exception as e:
            logger.warning(
                "Error creating staging model for %s: %s",
                oracle_obj.name,
                e,
            )
            return None

    def _create_intermediate_model(
        self,
        schema_name: str,
        staging_models: list[FlextDbtOracleModel],
    ) -> FlextDbtOracleModel | None:
        """Create an intermediate model from staging models."""
        try:
            if not staging_models:
                return None

            # Use the first model as the primary reference
            primary_model = staging_models[0]

            # Generate columns from primary model
            columns = primary_model.columns.copy()

            # Generate SQL content
            sql_content = self.INTERMEDIATE_TEMPLATE.format(
                columns="*",  # Select all columns for intermediate
                upstream_model=primary_model.name,
                filter_conditions="1=1",  # Placeholder filter
            ).strip()

            # Determine materialization
            materialization = self.config.get_materialization_for_layer("intermediate")

            # Create model
            return FlextDbtOracleModel(
                name=f"int_{schema_name}_combined".lower(),
                model_type="intermediate",
                schema_name=schema_name,
                table_name=f"{schema_name}_combined",
                columns=columns,
                materialization=materialization,
                sql_content=sql_content,
                description=f"Intermediate model combining {schema_name} staging tables",
                oracle_source=f"Multiple {schema_name} objects",
                dependencies=[model.name for model in staging_models],
            )

        except Exception as e:
            logger.warning(
                "Error creating intermediate model for %s: %s",
                schema_name,
                e,
            )
            return None

    def _create_marts_model(
        self,
        intermediate_model: FlextDbtOracleModel,
    ) -> FlextDbtOracleModel | None:
        """Create a marts model from an intermediate model."""
        try:
            # Generate aggregated columns
            agg_columns: list[str] = []
            group_columns: list[str] = []

            for col in intermediate_model.columns:
                data_type = str(col.get("data_type", ""))
                col_name = str(col.get("name", ""))
                if data_type in {"numeric", "float"}:
                    agg_columns.append(f"    sum({col_name}) as total_{col_name}")
                elif data_type == "string" and col_name not in {
                    "created_date",
                    "last_modified_date",
                }:
                    group_columns.append(col_name)
                    agg_columns.append(f"    {col_name}")

            # Default aggregation if no numeric columns
            if not any("sum(" in col for col in agg_columns):
                agg_columns.append("    count(*) as record_count")

            # Generate SQL content
            sql_content = self.MARTS_TEMPLATE.format(
                aggregated_columns=",\n".join(agg_columns),
                upstream_model=intermediate_model.name,
                group_by_columns=", ".join(list(group_columns))
                if group_columns
                else "1",
            ).strip()

            # Determine materialization
            materialization = self.config.get_materialization_for_layer("marts")

            # Generate mart columns
            mart_columns: list[dict[str, object]] = [
                {
                    "name": "record_count",
                    "description": "Total number of records",
                    "data_type": "numeric",
                    "tests": ["not_null", "positive"],
                },
            ]

            # Add grouped columns
            for col in intermediate_model.columns:
                col_name2 = str(col.get("name", ""))
                if col_name2 in group_columns:
                    mart_columns.append(
                        {
                            "name": col_name2,
                            "description": f"Grouped by {col_name2}",
                            "data_type": str(col.get("data_type", "string")),
                            "tests": ["not_null"],
                        },
                    )

            # Create model
            return FlextDbtOracleModel(
                name=f"mart_{intermediate_model.schema_name}_summary".lower(),
                model_type="marts",
                schema_name=intermediate_model.schema_name,
                table_name=f"{intermediate_model.schema_name}_summary",
                columns=mart_columns,
                materialization=materialization,
                sql_content=sql_content,
                description=f"Marts model with aggregated metrics for {intermediate_model.schema_name}",
                oracle_source=intermediate_model.oracle_source,
                dependencies=[intermediate_model.name],
            )

        except Exception as e:
            logger.warning(
                "Error creating marts model for %s: %s",
                intermediate_model.name,
                e,
            )
            return None


__all__: list[str] = [
    "FlextDbtOracleModel",
    "FlextDbtOracleModelGenerator",
]
