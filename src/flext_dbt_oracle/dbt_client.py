"""DBT client for Oracle operations.

Provides high-level interface for DBT Oracle transformations.
Integrates flext-db-oracle and flext-meltano for complete data pipeline operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core import FlextResult, get_logger
from flext_db_oracle import FlextDbOracleAPI
from flext_meltano import create_dbt_hub

from .dbt_config import FlextDbtOracleConfig
from .dbt_exceptions import (
    FlextDbtOracleConnectionError,
    FlextDbtOracleProcessingError,
    FlextDbtOracleValidationError,
)

if TYPE_CHECKING:
    from flext_db_oracle.entities import FlextOracleObject
    from flext_meltano import FlextDbtHub

logger = get_logger(__name__)


class FlextDbtOracleClient:
    """DBT client for Oracle data transformations.

    Provides unified interface for Oracle data processing, validation,
    and DBT transformation operations using maximum composition
    with flext-db-oracle and flext-meltano.
    """

    def __init__(
        self,
        config: FlextDbtOracleConfig | None = None,
    ) -> None:
        """Initialize DBT Oracle client.

        Args:
            config: Configuration for Oracle and DBT operations

        """
        self.config = config or FlextDbtOracleConfig()
        self._oracle_api: FlextDbOracleAPI | None = None
        self._dbt_hub: FlextDbtHub | None = None

        logger.info("Initialized DBT Oracle client with config: %s", self.config)

    @property
    def oracle_api(self) -> FlextDbOracleAPI:
        """Get or create Oracle API instance."""
        if self._oracle_api is None:
            oracle_config = self.config.get_oracle_config()
            self._oracle_api = FlextDbOracleAPI(oracle_config)
        return self._oracle_api

    @property
    def dbt_hub(self) -> FlextDbtHub:
        """Get or create DBT hub instance."""
        if self._dbt_hub is None:
            meltano_config = self.config.get_meltano_config()
            self._dbt_hub = create_dbt_hub(meltano_config)
        return self._dbt_hub

    def test_oracle_connection(self) -> FlextResult[dict[str, Any]]:
        """Test Oracle database connection.

        Returns:
            FlextResult containing connection test results

        """
        try:
            logger.info("Testing Oracle database connection")

            if not self.config.validate_oracle_connection():
                return FlextResult.fail(
                    "Invalid Oracle connection configuration",
                    error=FlextDbtOracleConnectionError(
                        "Invalid Oracle connection configuration",
                    ),
                )

            # Test connection using flext-db-oracle API
            connection_result = self.oracle_api.test_connection()

            if connection_result.success:
                logger.info("Oracle connection test successful")
                return FlextResult.ok(
                    {
                        "status": "connected",
                        "connection_info": connection_result.data,
                    },
                )
            logger.error("Oracle connection test failed: %s", connection_result.error)
            return FlextResult.fail(
                f"Oracle connection failed: {connection_result.error}",
                error=FlextDbtOracleConnectionError(
                    f"Oracle connection failed: {connection_result.error}",
                ),
            )

        except Exception as e:
            logger.exception("Unexpected error during Oracle connection test")
            return FlextResult.fail(
                f"Connection test error: {e}",
                error=FlextDbtOracleConnectionError(f"Connection test error: {e}"),
            )

    def extract_oracle_metadata(
        self,
        schema_names: list[str] | None = None,
        object_types: list[str] | None = None,
    ) -> FlextResult[list[FlextOracleObject]]:
        """Extract Oracle database metadata for DBT processing.

        Args:
            schema_names: List of schema names to extract (None = all accessible)
            object_types: List of object types to extract (None = all types)

        Returns:
            FlextResult containing list of Oracle objects

        """
        try:
            logger.info(
                "Extracting Oracle metadata: schemas=%s, types=%s",
                schema_names,
                object_types,
            )

            # Use flext-db-oracle API for metadata extraction
            if schema_names:
                metadata_result = self.oracle_api.get_objects_by_schemas(
                    schema_names, object_types,
                )
            else:
                metadata_result = self.oracle_api.get_all_objects(object_types)

            if metadata_result.success:
                objects = metadata_result.data or []
                logger.info("Successfully extracted %d Oracle objects", len(objects))
                return FlextResult.ok(objects)
            logger.error("Oracle metadata extraction failed: %s", metadata_result.error)
            return FlextResult.fail(
                f"Metadata extraction failed: {metadata_result.error}",
                error=FlextDbtOracleProcessingError(
                    f"Metadata extraction failed: {metadata_result.error}",
                ),
            )

        except Exception as e:
            logger.exception("Unexpected error during Oracle metadata extraction")
            return FlextResult.fail(
                f"Metadata extraction error: {e}",
                error=FlextDbtOracleProcessingError(f"Metadata extraction error: {e}"),
            )

    def validate_oracle_data(
        self,
        objects: list[FlextOracleObject],
    ) -> FlextResult[dict[str, Any]]:
        """Validate Oracle data quality for DBT processing.

        Args:
            objects: List of Oracle objects to validate

        Returns:
            FlextResult containing validation metrics

        """
        try:
            logger.info("Validating %d Oracle objects for data quality", len(objects))

            # Use flext-db-oracle API for validation
            validation_result = self.oracle_api.validate_objects(objects)

            if not validation_result.success:
                logger.error("Oracle validation failed: %s", validation_result.error)
                return FlextResult.fail(
                    f"Oracle validation failed: {validation_result.error}",
                    error=FlextDbtOracleValidationError(
                        f"Oracle validation failed: {validation_result.error}",
                    ),
                )

            # Get statistics using flext-db-oracle API
            stats_result = self.oracle_api.get_object_statistics(objects)
            if not stats_result.success:
                return FlextResult.fail(
                    f"Statistics generation failed: {stats_result.error}",
                    error=FlextDbtOracleValidationError(
                        f"Statistics generation failed: {stats_result.error}",
                    ),
                )

            stats = stats_result.data or {}
            quality_score = stats.get("quality_score", 0.0)

            logger.info(
                "Oracle data validation completed: quality_score=%.2f", quality_score,
            )

            if quality_score < self.config.min_quality_threshold:
                return FlextResult.fail(
                    f"Data quality below threshold: {quality_score} < {self.config.min_quality_threshold}",
                    error=FlextDbtOracleValidationError(
                        f"Data quality below threshold: {quality_score} < {self.config.min_quality_threshold}",
                    ),
                )

            return FlextResult.ok(
                {
                    **stats,
                    "quality_score": quality_score,
                    "validation_status": "passed",
                    "threshold": self.config.min_quality_threshold,
                },
            )

        except Exception as e:
            logger.exception("Unexpected error during Oracle validation")
            return FlextResult.fail(
                f"Oracle validation error: {e}",
                error=FlextDbtOracleValidationError(f"Oracle validation error: {e}"),
            )

    def transform_with_dbt(
        self,
        objects: list[FlextOracleObject],
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Transform Oracle data using DBT models.

        Args:
            objects: Oracle objects to transform
            model_names: Specific DBT models to run (None = all)

        Returns:
            FlextResult containing transformation results

        """
        try:
            logger.info(
                "Running DBT transformations on %d Oracle objects, models=%s",
                len(objects),
                model_names,
            )

            # Prepare Oracle data for DBT using flext-db-oracle API
            prepared_result = self._prepare_oracle_data_for_dbt(objects)
            if not prepared_result.success:
                return FlextResult.fail(
                    f"Data preparation failed: {prepared_result.error}",
                    error=FlextDbtOracleProcessingError(
                        f"Data preparation failed: {prepared_result.error}",
                    ),
                )

            transformed_data = prepared_result.data or {}

            # Use flext-meltano DBT hub for execution
            hub = self.dbt_hub

            if model_names:
                # Run specific models
                result = hub.run_models(model_names, data=transformed_data)
            else:
                # Run all models
                result = hub.run_project(data=transformed_data)

            if result.success:
                logger.info("DBT transformation completed successfully")
            else:
                logger.error("DBT transformation failed: %s", result.error)
                return FlextResult.fail(
                    f"DBT transformation failed: {result.error}",
                    error=FlextDbtOracleProcessingError(
                        f"DBT transformation failed: {result.error}",
                    ),
                )

            return result

        except Exception as e:
            logger.exception("Unexpected error during DBT transformation")
            return FlextResult.fail(
                f"DBT transformation error: {e}",
                error=FlextDbtOracleProcessingError(f"DBT transformation error: {e}"),
            )

    def run_full_pipeline(
        self,
        schema_names: list[str] | None = None,
        object_types: list[str] | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Run complete Oracle to DBT transformation pipeline.

        Args:
            schema_names: Oracle schemas to process
            object_types: Oracle object types to process
            model_names: DBT models to run

        Returns:
            FlextResult containing complete pipeline results

        """
        logger.info("Starting full Oracle-to-DBT pipeline")

        # Step 1: Test connection
        connection_result = self.test_oracle_connection()
        if not connection_result.success:
            return connection_result

        # Step 2: Extract metadata
        extract_result = self.extract_oracle_metadata(schema_names, object_types)
        if not extract_result.success:
            return extract_result

        objects = extract_result.data or []

        # Step 3: Validate data quality
        validate_result = self.validate_oracle_data(objects)
        if not validate_result.success:
            return validate_result

        # Step 4: Transform with DBT
        transform_result = self.transform_with_dbt(objects, model_names)
        if not transform_result.success:
            return transform_result

        # Combine results
        pipeline_results = {
            "connection_status": connection_result.data,
            "extracted_objects": len(objects),
            "validation_metrics": validate_result.data,
            "transformation_results": transform_result.data,
            "pipeline_status": "completed",
        }

        logger.info("Full Oracle-to-DBT pipeline completed successfully")
        return FlextResult.ok(pipeline_results)

    def _prepare_oracle_data_for_dbt(
        self, objects: list[FlextOracleObject],
    ) -> FlextResult[dict[str, Any]]:
        """Prepare Oracle objects for DBT processing using flext-db-oracle API.

        Converts Oracle objects to format suitable for DBT models using
        maximum composition with flext-db-oracle functionality.

        Args:
            objects: List of Oracle objects

        Returns:
            FlextResult containing prepared data for DBT

        """
        try:
            prepared_data = {}

            # Group objects by type using flext-db-oracle classification
            grouped_result = self.oracle_api.group_objects_by_type(objects)
            if not grouped_result.success:
                return FlextResult.fail(
                    f"Object grouping failed: {grouped_result.error}",
                )

            grouped_objects = grouped_result.data or {}

            # Apply schema mapping from config
            for object_type, type_objects in grouped_objects.items():
                schema_name = self.config.get_schema_for_object_type(object_type)
                if not schema_name:
                    logger.warning("No schema mapping for object type: %s", object_type)
                    continue

                # Convert objects to tabular format using flext-db-oracle API
                tabular_result = self.oracle_api.objects_to_tabular(type_objects)
                if tabular_result.success and tabular_result.data:
                    # Apply column mapping
                    mapped_data = [
                        self._map_oracle_columns(row) for row in tabular_result.data
                    ]
                    prepared_data[schema_name] = mapped_data

            logger.debug(
                "Prepared Oracle data for DBT: %s",
                {k: len(v) for k, v in prepared_data.items()},
            )

            return FlextResult.ok(prepared_data)

        except Exception as e:
            logger.exception("Error preparing Oracle data for DBT")
            return FlextResult.fail(f"Data preparation error: {e}")

    def _map_oracle_columns(self, object_data: dict[str, Any]) -> dict[str, Any]:
        """Map Oracle object columns using configuration mapping."""
        mapped_columns = {}

        for oracle_col, dbt_col in self.config.oracle_column_mapping.items():
            if oracle_col in object_data:
                mapped_columns[dbt_col] = object_data[oracle_col]

        # Add unmapped columns with original names (lowercased)
        for col, value in object_data.items():
            if col not in self.config.oracle_column_mapping:
                mapped_columns[col.lower()] = value

        return mapped_columns


__all__: list[str] = [
    "FlextDbtOracleClient",
]
