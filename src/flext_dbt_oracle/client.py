"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_core import FlextLogger, FlextResult
from flext_db_oracle import FlextDbOracleApi
from flext_meltano import FlextMeltanoService

from flext_dbt_oracle.adapters import FlextDbtOracleAdapters
from flext_dbt_oracle.settings import FlextDbtOracleSettings


class FlextDbtOracleClient:
    """DBT client for Oracle data transformations.

    Provides unified interface for Oracle data processing, validation,
    and DBT transformation operations using maximum composition
    with flext-db-oracle and flext-meltano.
    """

    # Shared logger for all DBT Oracle client operations
    logger = FlextLogger(__name__)

    @override
    def __init__(
        self,
        config: FlextDbtOracleSettings | None = None,
    ) -> None:
        """Initialize DBT Oracle client.

        Args:
        config: Configuration for Oracle and DBT operations

        """
        self.config: dict[str, object] = (
            config or FlextDbtOracleSettings.get_global_instance()
        )
        self._oracle_api: FlextDbOracleApi | None = None
        self._meltano_service: FlextMeltanoService | None = None
        self._dbt_plugin: object | None = None  # FlextDbtPlugin interface

        FlextDbtOracleClient.logger.info(
            "Initialized DBT Oracle client with config: %s",
            self.config,
        )

    @property
    def oracle_api(self: object) -> FlextDbOracleApi:
        """Get or create Oracle API instance."""
        if self._oracle_api is None:
            oracle_config: dict[str, object] = self.config.get_oracle_config()
            self._oracle_api = FlextDbOracleApi(oracle_config)
        return self._oracle_api

    @property
    def meltano_service(self: object) -> FlextMeltanoService | None:
        """Get or create FlextMeltanoService instance."""
        if self._meltano_service is None:
            try:
                # Create Meltano service using project directory
                self._meltano_service = FlextMeltanoService()
                FlextDbtOracleClient.logger.info("Created FlextMeltanoService wrapper")
            except Exception as e:
                FlextDbtOracleClient.logger.warning(
                    "Failed to create FlextMeltanoService: %s",
                    e,
                )
        return self._meltano_service

    def test_oracle_connection(self: object) -> FlextResult[dict[str, object]]:
        """Test Oracle database connection.

        Returns:
        FlextResult containing connection test results

        """
        try:
            FlextDbtOracleClient.logger.info("Testing Oracle database connection")

            if not self.config.validate_oracle_connection():
                return FlextResult[dict[str, object]].fail(
                    "Invalid Oracle connection configuration",
                )

            # Test connection using flext-db-oracle API
            connection_result: FlextResult[object] = self.oracle_api.test_connection()

            if connection_result.success:
                FlextDbtOracleClient.logger.info("Oracle connection test successful")
                return FlextResult[dict[str, object]].ok(
                    {
                        "status": "connected",
                        "connection_info": connection_result.value,
                    },
                )
            FlextDbtOracleClient.logger.error(
                "Oracle connection test failed: %s",
                connection_result.error,
            )
            return FlextResult[dict[str, object]].fail(
                f"Oracle connection failed: {connection_result.error}",
            )

        except Exception as e:
            FlextDbtOracleClient.logger.exception(
                "Unexpected error during Oracle connection test",
            )
            return FlextResult[dict[str, object]].fail(f"Connection test error: {e}")

    def extract_oracle_metadata(
        self,
        schema_names: list[str] | None = None,
        object_types: list[str] | None = None,
    ) -> FlextResult[list[FlextDbtOracleAdapters.TableAdapter]]:
        """Extract Oracle database metadata for DBT processing.

        Args:
        schema_names: List of schema names to extract (None = all accessible)
        object_types: List of object types to extract (None = all types)

        Returns:
        FlextResult containing list of Oracle objects

        """
        try:
            FlextDbtOracleClient.logger.info(
                "Extracting Oracle metadata: schemas=%s, types=%s",
                schema_names,
                object_types,
            )

            # Build metadata using available API: tables only
            target_schemas = schema_names or []
            tables: list[FlextDbtOracleAdapters.TableAdapter] = []

            if not target_schemas:
                tables.extend(self._extract_tables_from_default_schema())
            else:
                for schema in target_schemas:
                    tables.extend(self._extract_tables_from_schema(schema))

        except Exception as e:
            return FlextResult[list[FlextDbtOracleAdapters.TableAdapter]].fail(
                f"Oracle metadata extraction failed: {e}",
            )

        FlextDbtOracleClient.logger.info(
            "Extracted %d Oracle objects successfully",
            len(tables),
        )
        return FlextResult[list[FlextDbtOracleAdapters.TableAdapter]].ok(tables)

    def _extract_tables_from_default_schema(
        self,
    ) -> list[FlextDbtOracleAdapters.TableAdapter]:
        """Extract tables from default schema (no schema specified)."""
        tables = []
        table_names_result: FlextResult[object] = self.oracle_api.get_tables()
        if not table_names_result.success:
            FlextDbtOracleClient.logger.warning(
                "Failed to list tables for default schema: %s",
                table_names_result.error,
            )
            return tables

        for table_dict in table_names_result.value or []:
            table_name = self._extract_table_name(table_dict)
            if table_name:
                table_adapter = self._create_table_adapter(table_name, None)
                if table_adapter:
                    tables.append(table_adapter)
        return tables

    def _extract_tables_from_schema(
        self,
        schema: str,
    ) -> list[FlextDbtOracleAdapters.TableAdapter]:
        """Extract tables from a specific schema."""
        tables = []
        table_names_result: FlextResult[object] = self.oracle_api.get_tables(schema)
        if not table_names_result.success:
            FlextDbtOracleClient.logger.warning(
                "Failed to list tables for schema %s: %s",
                schema,
                table_names_result.error,
            )
            return tables

        for table_dict in table_names_result.value or []:
            table_name = self._extract_table_name(table_dict)
            if table_name:
                table_adapter = self._create_table_adapter(table_name, schema)
                if table_adapter:
                    tables.append(table_adapter)
        return tables

    def _extract_table_name(self, table_dict: object) -> str | None:
        """Extract table name from table dictionary."""
        if isinstance(table_dict, dict):
            return str(table_dict.get("name", ""))
        return str(table_dict) if table_dict else None

    def _create_table_adapter(
        self,
        table_name: str,
        schema_name: str | None,
    ) -> FlextDbtOracleAdapters.TableAdapter | None:
        """Create table adapter from API response."""
        meta = self.oracle_api.get_table_metadata(table_name, schema_name)
        if not (meta.success and isinstance(meta.value, dict)):
            return None

        table_metadata = meta.value
        adapter_result = FlextDbtOracleAdapters.TableFactory.from_api_response(
            table_name=table_name,
            api_response=table_metadata,
            schema_name=schema_name,
        )

        return adapter_result.map_or(None)

    def validate_oracle_data(
        self,
        objects: list[FlextDbtOracleAdapters.TableAdapter],
    ) -> FlextResult[dict[str, object]]:
        """Validate Oracle data quality for DBT processing.

        Args:
        objects: List of Oracle objects to validate

        Returns:
        FlextResult containing validation metrics

        """
        try:
            FlextDbtOracleClient.logger.info(
                "Validating %d Oracle objects for data quality",
                len(objects),
            )

            # Basic validation: ensure tables and columns present
            total_tables = len(objects)
            total_columns: list[object] = sum(
                len(getattr(t, "columns", [])) for t in objects
            )
            quality_score = 1.0 if total_tables > 0 and total_columns > 0 else 0.0
            stats: dict[str, object] = {
                "tables": "total_tables",
                "columns": "total_columns",
            }

            FlextDbtOracleClient.logger.info(
                "Oracle data validation completed: quality_score=%.2f",
                quality_score,
            )

            if quality_score < self.config.min_quality_threshold:
                return FlextResult[dict[str, object]].fail(
                    f"Data quality below threshold: {quality_score} < {self.config.min_quality_threshold}",
                )

            return FlextResult[dict[str, object]].ok(
                {
                    **stats,
                    "quality_score": "quality_score",
                    "validation_status": "passed",
                    "threshold": self.config.min_quality_threshold,
                },
            )

        except Exception as e:
            FlextDbtOracleClient.logger.exception(
                "Unexpected error during Oracle validation",
            )
            return FlextResult[dict[str, object]].fail(
                f"Oracle validation error: {e}",
            )

    def transform_with_dbt(
        self,
        objects: list[FlextDbtOracleAdapters.TableAdapter],
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Transform Oracle data using DBT models.

        Args:
        objects: Oracle objects to transform
        model_names: Specific DBT models to run (None = all)

        Returns:
        FlextResult containing transformation results

        """
        try:
            FlextDbtOracleClient.logger.info(
                "Running DBT transformations on %d Oracle objects, models=%s",
                len(objects),
                model_names,
            )

            # Execute requested models using FlextMeltanoService
            meltano_service = self.meltano_service
            if meltano_service is None:
                return FlextResult[dict[str, object]].fail(
                    "FlextMeltanoService not initialized - cannot execute models",
                )

            # Run all models or specific models using Meltano service
            run_result = meltano_service.run_models(
                model_names=model_names,
            )

            if run_result.success:
                executed: dict[str, object] = {
                    "status": "success",
                    "models_executed": model_names or "all",
                    "project_path": self.config.dbt_project_dir,
                    "dbt_result": run_result.value,
                }
                FlextDbtOracleClient.logger.info(
                    "DBT transformation executed for models: %s",
                    model_names or "all",
                )
                return FlextResult[dict[str, object]].ok(executed)

            return FlextResult[dict[str, object]].fail(
                run_result.error or "DBT transformation failed",
            )

        except Exception as e:
            FlextDbtOracleClient.logger.exception(
                "Unexpected error during DBT transformation",
            )
            return FlextResult[dict[str, object]].fail(
                f"DBT transformation error: {e}",
            )

    def run_full_pipeline(
        self,
        schema_names: list[str] | None = None,
        object_types: list[str] | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Run complete Oracle to DBT transformation pipeline.

        Args:
        schema_names: Oracle schemas to process
        object_types: Oracle object types to process
        model_names: DBT models to run

        Returns:
        FlextResult containing complete pipeline results

        """
        FlextDbtOracleClient.logger.info("Starting full Oracle-to-DBT pipeline")

        # Step 1: Test connection
        connection_result: FlextResult[object] = self.test_oracle_connection()
        if not connection_result.success:
            return connection_result

        # Step 2: Extract metadata
        extract_result: FlextResult[object] = self.extract_oracle_metadata(
            schema_names,
            object_types,
        )
        if not extract_result.success:
            return FlextResult[dict[str, object]].fail(
                extract_result.error or "Metadata extraction failed",
            )

        objects = extract_result.value or []

        # Step 3: Validate data quality
        validate_result: FlextResult[object] = self.validate_oracle_data(objects)
        if not validate_result.success:
            return validate_result

        # Step 4: Transform with DBT
        transform_result: FlextResult[object] = self.transform_with_dbt(
            objects,
            model_names or [],
        )
        if not transform_result.success:
            return FlextResult[dict[str, object]].fail(
                transform_result.error or "Transformation failed",
            )

        # Combine results
        pipeline_results: dict[str, object] = {
            "connection_status": connection_result.value,
            "extracted_objects": len(objects),
            "validation_metrics": validate_result.value,
            "transformation_results": transform_result.value,
            "pipeline_status": "completed",
        }

        FlextDbtOracleClient.logger.info(
            "Full Oracle-to-DBT pipeline completed successfully",
        )
        return FlextResult[dict[str, object]].ok(pipeline_results)

    # Note: Previous data preparation and grouping helpers removed.


__all__: list[str] = [
    "FlextDbtOracleClient",
]
