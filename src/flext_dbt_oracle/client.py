"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_db_oracle import FlextDbOracleApi
from flext_meltano import FlextMeltanoService

from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_dbt_oracle.adapters import FlextDbtOracleAdapters
from flext_dbt_oracle.config import FlextDbtOracleConfig


class FlextDbtOracleClient:
    """DBT client for Oracle data transformations.

    Provides unified interface for Oracle data processing, validation,
    and DBT transformation operations using maximum composition
    with flext-db-oracle and flext-meltano.
    """

    # Shared logger for all DBT Oracle client operations
    _logger = FlextLogger(__name__)

    @override
    def __init__(
        self,
        config: FlextDbtOracleConfig | None = None,
    ) -> None:
        """Initialize DBT Oracle client.

        Args:
            config: Configuration for Oracle and DBT operations

        """
        self.config: FlextTypes.Dict = (
            config or FlextDbtOracleConfig.get_global_instance()
        )
        self._oracle_api: FlextDbOracleApi | None = None
        self._meltano_service: FlextMeltanoService | None = None
        self._dbt_plugin: object | None = None  # FlextDbtPlugin interface

        FlextDbtOracleClient._logger.info(
            "Initialized DBT Oracle client with config: %s", self.config
        )

    @property
    def oracle_api(self: object) -> FlextDbOracleApi:
        """Get or create Oracle API instance."""
        if self._oracle_api is None:
            oracle_config: FlextTypes.Dict = self.config.get_oracle_config()
            self._oracle_api = FlextDbOracleApi(oracle_config)
        return self._oracle_api

    @property
    def meltano_service(self: object) -> FlextMeltanoService | None:
        """Get or create FlextMeltanoService instance."""
        if self._meltano_service is None:
            try:
                # Create Meltano service using project directory
                self._meltano_service = FlextMeltanoService()
                FlextDbtOracleClient._logger.info("Created FlextMeltanoService wrapper")
            except Exception as e:
                FlextDbtOracleClient._logger.warning(
                    "Failed to create FlextMeltanoService: %s", e
                )
        return self._meltano_service

    def test_oracle_connection(self: object) -> FlextResult[FlextTypes.Dict]:
        """Test Oracle database connection.

        Returns:
            FlextResult containing connection test results

        """
        try:
            FlextDbtOracleClient._logger.info("Testing Oracle database connection")

            if not self.config.validate_oracle_connection():
                return FlextResult[FlextTypes.Dict].fail(
                    "Invalid Oracle connection configuration",
                )

            # Test connection using flext-db-oracle API
            connection_result: FlextResult[object] = self.oracle_api.test_connection()

            if connection_result.success:
                FlextDbtOracleClient._logger.info("Oracle connection test successful")
                return FlextResult[FlextTypes.Dict].ok(
                    {
                        "status": "connected",
                        "connection_info": connection_result.value,
                    },
                )
            FlextDbtOracleClient._logger.error(
                "Oracle connection test failed: %s", connection_result.error
            )
            return FlextResult[FlextTypes.Dict].fail(
                f"Oracle connection failed: {connection_result.error}",
            )

        except Exception as e:
            FlextDbtOracleClient._logger.exception(
                "Unexpected error during Oracle connection test"
            )
            return FlextResult[FlextTypes.Dict].fail(f"Connection test error: {e}")

    def extract_oracle_metadata(
        self,
        schema_names: FlextTypes.StringList | None = None,
        object_types: FlextTypes.StringList | None = None,
    ) -> FlextResult[list[FlextDbtOracleAdapters.TableAdapter]]:
        """Extract Oracle database metadata for DBT processing.

        Args:
            schema_names: List of schema names to extract (None = all accessible)
            object_types: List of object types to extract (None = all types)

        Returns:
            FlextResult containing list of Oracle objects

        """
        try:
            FlextDbtOracleClient._logger.info(
                "Extracting Oracle metadata: schemas=%s, types=%s",
                schema_names,
                object_types,
            )

            # Build metadata using available API: tables only
            target_schemas = schema_names or []
            tables: list[FlextDbtOracleAdapters.TableAdapter] = []
            if not target_schemas:
                # If no schemas provided, try a simple default: current user schema via get_tables(None)
                table_names_result: FlextResult[object] = self.oracle_api.get_tables()
                if table_names_result.success:
                    for table_dict in table_names_result.value or []:
                        # Extract table name from dictionary with proper type casting
                        table_name = (
                            str(table_dict.get("name", ""))
                            if isinstance(table_dict, dict)
                            else str(table_dict)
                        )
                        meta = self.oracle_api.get_table_metadata(table_name)
                        if meta.success and isinstance(meta.value, dict):
                            # Convert dict metadata using adapter factory
                            table_metadata = meta.value
                            # Create adapter from API response
                            adapter_result = (
                                FlextDbtOracleAdapters.TableFactory.from_api_response(
                                    table_name=table_name,
                                    api_response=table_metadata,
                                    schema_name=None,  # Will be inferred from response
                                )
                            )
                            if adapter_result.is_success:
                                tables.append(adapter_result.unwrap())
                else:
                    return FlextResult[list[FlextDbtOracleAdapters.TableAdapter]].fail(
                        f"Failed to list tables: {table_names_result.error}",
                    )
            else:
                for schema in target_schemas:
                    table_names_result: FlextResult[object] = (
                        self.oracle_api.get_tables(schema)
                    )
                    if not table_names_result.success:
                        FlextDbtOracleClient._logger.warning(
                            "Failed to list tables for schema %s: %s",
                            schema,
                            table_names_result.error,
                        )
                        continue
                    for table_dict in table_names_result.value or []:
                        # Extract table name from dictionary with proper type casting
                        table_name = (
                            str(table_dict.get("name", ""))
                            if isinstance(table_dict, dict)
                            else str(table_dict)
                        )
                        meta = self.oracle_api.get_table_metadata(table_name, schema)
                        if meta.success and isinstance(meta.value, dict):
                            # Convert dict metadata using adapter factory
                            table_metadata = meta.value
                            # Create adapter from API response
                            adapter_result = (
                                FlextDbtOracleAdapters.TableFactory.from_api_response(
                                    table_name=table_name,
                                    api_response=table_metadata,
                                    schema_name=schema,
                                )
                            )
                            if adapter_result.is_success:
                                tables.append(adapter_result.unwrap())

            FlextDbtOracleClient._logger.info(
                "Successfully extracted %d Oracle tables", len(tables)
            )
            return FlextResult[list[FlextDbtOracleAdapters.TableAdapter]].ok(tables)

        except Exception as e:
            FlextDbtOracleClient._logger.exception(
                "Unexpected error during Oracle metadata extraction"
            )
            return FlextResult[list[FlextDbtOracleAdapters.TableAdapter]].fail(
                f"Metadata extraction error: {e}",
            )

    def validate_oracle_data(
        self,
        objects: list[FlextDbtOracleAdapters.TableAdapter],
    ) -> FlextResult[FlextTypes.Dict]:
        """Validate Oracle data quality for DBT processing.

        Args:
            objects: List of Oracle objects to validate

        Returns:
            FlextResult containing validation metrics

        """
        try:
            FlextDbtOracleClient._logger.info(
                "Validating %d Oracle objects for data quality", len(objects)
            )

            # Basic validation: ensure tables and columns present
            total_tables = len(objects)
            total_columns: FlextTypes.List = sum(
                len(getattr(t, "columns", [])) for t in objects
            )
            quality_score = 1.0 if total_tables > 0 and total_columns > 0 else 0.0
            stats: FlextTypes.Dict = {
                "tables": "total_tables",
                "columns": "total_columns",
            }

            FlextDbtOracleClient._logger.info(
                "Oracle data validation completed: quality_score=%.2f",
                quality_score,
            )

            if quality_score < self.config.min_quality_threshold:
                return FlextResult[FlextTypes.Dict].fail(
                    f"Data quality below threshold: {quality_score} < {self.config.min_quality_threshold}",
                )

            return FlextResult[FlextTypes.Dict].ok(
                {
                    **stats,
                    "quality_score": "quality_score",
                    "validation_status": "passed",
                    "threshold": self.config.min_quality_threshold,
                },
            )

        except Exception as e:
            FlextDbtOracleClient._logger.exception(
                "Unexpected error during Oracle validation"
            )
            return FlextResult[FlextTypes.Dict].fail(
                f"Oracle validation error: {e}",
            )

    def transform_with_dbt(
        self,
        objects: list[FlextDbtOracleAdapters.TableAdapter],
        model_names: FlextTypes.StringList | None = None,
    ) -> FlextResult[FlextTypes.Dict]:
        """Transform Oracle data using DBT models.

        Args:
            objects: Oracle objects to transform
            model_names: Specific DBT models to run (None = all)

        Returns:
            FlextResult containing transformation results

        """
        try:
            FlextDbtOracleClient._logger.info(
                "Running DBT transformations on %d Oracle objects, models=%s",
                len(objects),
                model_names,
            )

            # Execute requested models using FlextMeltanoService
            meltano_service = self.meltano_service
            if meltano_service is None:
                return FlextResult[FlextTypes.Dict].fail(
                    "FlextMeltanoService not initialized - cannot execute models",
                )

            # Run all models or specific models using Meltano service
            run_result = meltano_service.run_models(
                model_names=model_names,
            )

            if run_result.success:
                executed: FlextTypes.Dict = {
                    "status": "success",
                    "models_executed": model_names or "all",
                    "project_path": self.config.dbt_project_dir,
                    "dbt_result": run_result.unwrap(),
                }
                FlextDbtOracleClient._logger.info(
                    "DBT transformation executed for models: %s",
                    model_names or "all",
                )
                return FlextResult[FlextTypes.Dict].ok(executed)

            return FlextResult[FlextTypes.Dict].fail(
                run_result.error or "DBT transformation failed",
            )

        except Exception as e:
            FlextDbtOracleClient._logger.exception(
                "Unexpected error during DBT transformation"
            )
            return FlextResult[FlextTypes.Dict].fail(
                f"DBT transformation error: {e}",
            )

    def run_full_pipeline(
        self,
        schema_names: FlextTypes.StringList | None = None,
        object_types: FlextTypes.StringList | None = None,
        model_names: FlextTypes.StringList | None = None,
    ) -> FlextResult[FlextTypes.Dict]:
        """Run complete Oracle to DBT transformation pipeline.

        Args:
            schema_names: Oracle schemas to process
            object_types: Oracle object types to process
            model_names: DBT models to run

        Returns:
            FlextResult containing complete pipeline results

        """
        FlextDbtOracleClient._logger.info("Starting full Oracle-to-DBT pipeline")

        # Step 1: Test connection
        connection_result: FlextResult[object] = self.test_oracle_connection()
        if not connection_result.success:
            return connection_result

        # Step 2: Extract metadata
        extract_result: FlextResult[object] = self.extract_oracle_metadata(
            schema_names, object_types
        )
        if not extract_result.success:
            return FlextResult[FlextTypes.Dict].fail(
                extract_result.error or "Metadata extraction failed",
            )

        objects = extract_result.value or []

        # Step 3: Validate data quality
        validate_result: FlextResult[object] = self.validate_oracle_data(objects)
        if not validate_result.success:
            return validate_result

        # Step 4: Transform with DBT
        transform_result: FlextResult[object] = self.transform_with_dbt(
            objects, model_names or []
        )
        if not transform_result.success:
            return FlextResult[FlextTypes.Dict].fail(
                transform_result.error or "Transformation failed",
            )

        # Combine results
        pipeline_results: FlextTypes.Dict = {
            "connection_status": connection_result.value,
            "extracted_objects": len(objects),
            "validation_metrics": validate_result.value,
            "transformation_results": transform_result.value,
            "pipeline_status": "completed",
        }

        FlextDbtOracleClient._logger.info(
            "Full Oracle-to-DBT pipeline completed successfully"
        )
        return FlextResult[FlextTypes.Dict].ok(pipeline_results)

    # Note: Previous data preparation and grouping helpers removed.


__all__: FlextTypes.StringList = [
    "FlextDbtOracleClient",
]
