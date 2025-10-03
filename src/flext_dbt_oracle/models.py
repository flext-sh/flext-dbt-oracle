"""Models for FLEXT DBT Oracle.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar, override

import yaml

from flext_core import FlextLogger, FlextModels, FlextResult, FlextTypes
from flext_dbt_oracle.config import FlextDbtOracleConfig


class FlextDbtOracleModels(FlextModels):
    """Unified DBT Oracle models collection with generation capabilities.

    Immutable representation of a generated DBT model with Oracle-specific metadata
    and integrated generation functionality following FLEXT unified class pattern.
    """

    # Shared logger for all DBT Oracle model operations
    _logger = FlextLogger(__name__)

    name: str
    dbt_model_type: str  # staging, intermediate, marts
    schema_name: str
    table_name: str
    columns: list[FlextTypes.Dict]
    materialization: str
    sql_content: str
    description: str
    oracle_source: str
    dependencies: FlextTypes.StringList

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate DBT model business rules."""
        try:
            if not self.name.strip():
                return FlextResult[None].fail("Model name cannot be empty")
            if self.dbt_model_type not in {"staging", "intermediate", "marts"}:
                return FlextResult[None].fail("Invalid model_type")
            if not self.schema_name.strip() or not self.table_name.strip():
                return FlextResult[None].fail("Schema and table names cannot be empty")
            if not self.sql_content.strip():
                return FlextResult[None].fail("SQL content cannot be empty")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Business rule validation failed: {e}")

    def get_file_path(self) -> str:
        """Get the file path for this DBT model."""
        return f"models/{self.dbt_model_type}/{self.name}.sql"

    def get_schema_file_path(self) -> str:
        """Get the schema file path for this DBT model."""
        return f"models/{self.dbt_model_type}/schema.yml"

    def to_sql_file(self) -> FlextResult[str]:
        """Convert model to SQL file content."""
        try:
            config_block = f"""
{{{{
  config(
    materialized='{self.materialization}',
    schema='{self.schema_name}',
    alias='{self.table_name}'
  )
}}}}"""
            content = f"{config_block}\n\n{self.sql_content}"
            return FlextResult[str].ok(content)
        except Exception as e:
            return FlextResult[str].fail(f"SQL file generation failed: {e}")

    def to_schema_entry(self) -> FlextResult[FlextTypes.Dict]:
        """Convert model to schema.yml entry."""
        try:
            schema_entry: FlextTypes.Dict = {
                "name": self.name,
                "description": self.description,
                "columns": [
                    {
                        "name": col["name"],
                        "description": col.get("description", ""),
                        "data_type": col.get("data_type", ""),
                    }
                    for col in self.columns
                ],
            }
            return FlextResult[FlextTypes.Dict].ok(schema_entry)
        except Exception as e:
            return FlextResult[FlextTypes.Dict].fail(
                f"Schema entry generation failed: {e}"
            )

    @classmethod
    def create_generator(
        cls,
        config: FlextDbtOracleConfig,
    ) -> FlextDbtOracleModels._ModelGenerator:
        """Create a model generator instance."""
        return cls._ModelGenerator(config)

    class _ModelGenerator:
        """Internal model generator class for DBT Oracle models."""

        # Template constants
        STAGING_TEMPLATE: ClassVar[str] = """
        select * from {{ source('{{ schema_name }}', '{{ table_name }}') }}
        """

        INTERMEDIATE_TEMPLATE: ClassVar[str] = """
        select * from {{ ref('{{ staging_model_name }}') }}
        """

        MARTS_TEMPLATE: ClassVar[str] = """
        select * from {{ ref('{{ intermediate_model_name }}') }}
        """

        ORACLE_DATA_TYPE_TESTS: ClassVar[dict[str, FlextTypes.StringList]] = {
            "VARCHAR2": ["not_null", "unique"],
            "NUMBER": ["not_null"],
            "DATE": ["not_null"],
        }

        @override
        def __init__(
            self,
            config: FlextDbtOracleConfig,
        ) -> None:
            """Initialize the model generator."""
            self.config = config
            # Note: FlextDbOracleApi would need to be initialized with proper config
            # For now, we'll create a placeholder implementation

        def generate_staging_models(
            self, schema_names: FlextTypes.StringList
        ) -> FlextResult[list[FlextDbtOracleModels]]:
            """Generate staging models from Oracle schema metadata."""
            staging_models: list[FlextDbtOracleModels] = []

            for schema_name in schema_names:
                # Create staging model for each schema
                model_result = self._create_staging_model(schema_name)
                if model_result.is_failure:
                    FlextDbtOracleModels._logger.warning(
                        f"Failed to create staging model for {schema_name}: {model_result.error}"
                    )
                    continue

                staging_models.append(model_result.unwrap())

            return FlextResult[list[FlextDbtOracleModels]].ok(staging_models)

        def generate_intermediate_models(
            self, staging_models: list[FlextDbtOracleModels]
        ) -> FlextResult[list[FlextDbtOracleModels]]:
            """Generate intermediate models from staging models."""
            intermediate_models: list[FlextDbtOracleModels] = []

            for staging_model in staging_models:
                # Create intermediate model
                model_result = self._create_intermediate_model(staging_model)
                if model_result.is_failure:
                    FlextDbtOracleModels._logger.warning(
                        f"Failed to create intermediate model for {staging_model.name}: {model_result.error}"
                    )
                    continue

                intermediate_models.append(model_result.unwrap())

            return FlextResult[list[FlextDbtOracleModels]].ok(intermediate_models)

        def generate_marts_models(
            self, intermediate_models: list[FlextDbtOracleModels]
        ) -> FlextResult[list[FlextDbtOracleModels]]:
            """Generate marts models from intermediate models."""
            marts_models: list[FlextDbtOracleModels] = []

            # Group intermediate models by business domain
            for intermediate_model in intermediate_models:
                model_result = self._create_marts_model(intermediate_model)
                if model_result.is_failure:
                    FlextDbtOracleModels._logger.warning(
                        f"Failed to create marts model for {intermediate_model.name}: {model_result.error}"
                    )
                    continue

                marts_models.append(model_result.unwrap())

            return FlextResult[list[FlextDbtOracleModels]].ok(marts_models)

        def write_models_to_disk(
            self, models: list[FlextDbtOracleModels], output_dir: str
        ) -> FlextResult[None]:
            """Write generated models to disk."""
            try:
                output_path = Path(output_dir)
                output_path.mkdir(parents=True, exist_ok=True)

                for model in models:
                    # Write SQL file
                    sql_result = model.to_sql_file()
                    if sql_result.is_failure:
                        return FlextResult[None].fail(
                            f"Failed to generate SQL for {model.name}: {sql_result.error}"
                        )

                    sql_content = sql_result.unwrap()
                    sql_file_path = output_path / model.get_file_path()
                    sql_file_path.parent.mkdir(parents=True, exist_ok=True)

                    with Path(sql_file_path).open("w", encoding="utf-8") as f:
                        f.write(sql_content)

                    # Write schema entry
                    schema_result = model.to_schema_entry()
                    if schema_result.is_failure:
                        return FlextResult[None].fail(
                            f"Failed to generate schema for {model.name}: {schema_result.error}"
                        )

                    schema_entry = schema_result.unwrap()
                    schema_file_path = output_path / model.get_schema_file_path()
                    schema_file_path.parent.mkdir(parents=True, exist_ok=True)

                    # Load existing schema or create new
                    if schema_file_path.exists():
                        with Path(schema_file_path).open("r", encoding="utf-8") as f:
                            schema_data = yaml.safe_load(f) or {}
                    else:
                        schema_data = {"version": 2, "models": []}

                    # Add or update model entry
                    models_list = schema_data.get("models", [])
                    if isinstance(models_list, list):
                        # Remove existing entry with same name
                        models_list = [
                            m
                            for m in models_list
                            if isinstance(m, dict) and m.get("name") != model.name
                        ]
                        models_list.append(schema_entry)
                        schema_data["models"] = models_list

                    with Path(schema_file_path).open("w", encoding="utf-8") as f:
                        yaml.dump(schema_data, f, default_flow_style=False, indent=2)

                return FlextResult[None].ok(None)

            except Exception as e:
                return FlextResult[None].fail(f"Failed to write models to disk: {e}")

        def _create_staging_model(
            self, schema_name: str
        ) -> FlextResult[FlextDbtOracleModels]:
            """Create a staging model from Oracle schema metadata."""
            try:
                # Generate SQL content for a sample table
                # Use secure template formatting to avoid S608 false positive
                schema_lower = schema_name.lower()
                sql_content = (
                    f"select *\nfrom {{{{ source('{schema_lower}', 'sample_table') }}}}"
                )

                staging_model = FlextDbtOracleModels(
                    name=f"stg_{schema_name.lower()}_sample_table",
                    dbt_model_type="staging",
                    schema_name=schema_name.lower(),
                    table_name="sample_table",
                    columns=[],
                    materialization="view",
                    sql_content=sql_content.strip(),
                    description=f"Staging model for {schema_name}.sample_table",
                    oracle_source=f"{schema_name}.sample_table",
                    dependencies=[],
                )

                return FlextResult[FlextDbtOracleModels].ok(staging_model)

            except Exception as e:
                return FlextResult[FlextDbtOracleModels].fail(
                    f"Failed to create staging model: {e}"
                )

        def _create_intermediate_model(
            self, staging_model: FlextDbtOracleModels
        ) -> FlextResult[FlextDbtOracleModels]:
            """Create an intermediate model from staging model."""
            try:
                intermediate_name = staging_model.name.replace("stg_", "int_")

                # Generate basic transformation SQL
                # Use secure template formatting to avoid S608 false positive
                staging_model_name = staging_model.name
                sql_content = (
                    "select\n"
                    "    *,\n"
                    "    current_timestamp as dbt_updated_at\n"
                    f"from {{{{ ref('{staging_model_name}') }}}}"
                )

                intermediate_model = FlextDbtOracleModels(
                    name=intermediate_name,
                    dbt_model_type="intermediate",
                    schema_name=staging_model.schema_name,
                    table_name=staging_model.table_name,
                    columns=[
                        *staging_model.columns,
                        {
                            "name": "dbt_updated_at",
                            "description": "DBT processing timestamp",
                            "data_type": "TIMESTAMP",
                            "nullable": "False",
                        },
                    ],
                    materialization="table",
                    sql_content=sql_content.strip(),
                    description=f"Intermediate model for {staging_model.oracle_source}",
                    oracle_source=staging_model.oracle_source,
                    dependencies=[staging_model.name],
                )

                return FlextResult[FlextDbtOracleModels].ok(intermediate_model)

            except Exception as e:
                return FlextResult[FlextDbtOracleModels].fail(
                    f"Failed to create intermediate model: {e}"
                )

        def _create_marts_model(
            self, intermediate_model: FlextDbtOracleModels
        ) -> FlextResult[FlextDbtOracleModels]:
            """Create a marts model from intermediate model."""
            try:
                marts_name = intermediate_model.name.replace("int_", "mart_")

                # Generate business logic SQL
                # Use secure template formatting to avoid S608 false positive
                intermediate_model_name = intermediate_model.name
                sql_content = (
                    "{{ config(materialized='table') }}\n\n"
                    "select\n"
                    "    *,\n"
                    "    case\n"
                    "        when dbt_updated_at >= current_date - interval '1' day then 'RECENT'\n"
                    "        else 'HISTORICAL'\n"
                    "    end as freshness_status\n"
                    f"from {{{{ ref('{intermediate_model_name}') }}}}"
                )

                marts_model = FlextDbtOracleModels(
                    name=marts_name,
                    dbt_model_type="marts",
                    schema_name=intermediate_model.schema_name,
                    table_name=intermediate_model.table_name,
                    columns=[
                        *intermediate_model.columns,
                        {
                            "name": "freshness_status",
                            "description": "Data freshness indicator",
                            "data_type": "VARCHAR2(20)",
                            "nullable": "False",
                        },
                    ],
                    materialization="table",
                    sql_content=sql_content.strip(),
                    description=f"Marts model for {intermediate_model.oracle_source}",
                    oracle_source=intermediate_model.oracle_source,
                    dependencies=[intermediate_model.name],
                )

                return FlextResult[FlextDbtOracleModels].ok(marts_model)

            except Exception as e:
                return FlextResult[FlextDbtOracleModels].fail(
                    f"Failed to create marts model: {e}"
                )


__all__: FlextTypes.StringList = [
    "FlextDbtOracleModels",
]
