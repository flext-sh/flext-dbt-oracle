"""DBT services for Oracle workflow orchestration.

Provides high-level services for orchestrating complete Oracle-to-DBT workflows.
Integrates all components for end-to-end data transformation pipelines.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import TYPE_CHECKING, Any

from flext_core import FlextResult, get_logger
from flext_db_oracle import FlextDbOracleAPI

from .dbt_client import FlextDbtOracleClient
from .dbt_config import FlextDbtOracleConfig
from .dbt_exceptions import (
    FlextDbtOracleProcessingError,
    FlextDbtOracleResourceError,
)
from .dbt_models import FlextDbtOracleModelGenerator

if TYPE_CHECKING:
    from flext_db_oracle.entities import FlextOracleObject

logger = get_logger(__name__)


class FlextDbtOracleWorkflowService:
    """Service for orchestrating complete Oracle-to-DBT workflows.

    Provides high-level workflow orchestration that combines metadata extraction,
    model generation, and DBT execution into cohesive data transformation pipelines.
    """

    def __init__(
        self,
        config: FlextDbtOracleConfig | None = None,
    ) -> None:
        """Initialize workflow service.

        Args:
            config: Configuration for Oracle and DBT operations

        """
        self.config = config or FlextDbtOracleConfig()
        self.client = FlextDbtOracleClient(self.config)

        # Initialize Oracle API for model generation
        oracle_config = self.config.get_oracle_config()
        self.oracle_api = FlextDbOracleAPI(oracle_config)
        self.model_generator = FlextDbtOracleModelGenerator(
            self.config, self.oracle_api,
        )

        logger.info("Initialized Oracle DBT workflow service")

    def run_metadata_to_models_workflow(
        self,
        schema_names: list[str] | None = None,
        object_types: list[str] | None = None,
        output_path: Path | str | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Run complete metadata extraction to model generation workflow.

        Args:
            schema_names: Oracle schemas to process (None = all accessible)
            object_types: Oracle object types to process (None = all types)
            output_path: Path to write generated models (None = current directory)

        Returns:
            FlextResult containing workflow results and statistics

        """
        try:
            output_dir = Path(output_path) if output_path else Path.cwd()
            logger.info(
                "Starting metadata-to-models workflow: schemas=%s, types=%s, output=%s",
                schema_names,
                object_types,
                output_dir,
            )

            # Step 1: Test Oracle connection
            logger.info("Testing Oracle connection...")
            connection_result = self.client.test_oracle_connection()
            if not connection_result.success:
                return connection_result

            # Step 2: Extract Oracle metadata
            logger.info("Extracting Oracle metadata...")
            metadata_result = self.client.extract_oracle_metadata(
                schema_names, object_types,
            )
            if not metadata_result.success:
                return metadata_result

            oracle_objects = metadata_result.data or []
            logger.info("Extracted metadata for %d Oracle objects", len(oracle_objects))

            # Step 3: Generate staging models
            logger.info("Generating staging models...")
            staging_result = self.model_generator.generate_staging_models(
                oracle_objects,
            )
            if not staging_result.success:
                return staging_result

            staging_models = staging_result.data or []

            # Step 4: Generate intermediate models
            logger.info("Generating intermediate models...")
            intermediate_result = self.model_generator.generate_intermediate_models(
                staging_models,
            )
            if not intermediate_result.success:
                return intermediate_result

            intermediate_models = intermediate_result.data or []

            # Step 5: Generate marts models
            logger.info("Generating marts models...")
            marts_result = self.model_generator.generate_marts_models(
                intermediate_models,
            )
            if not marts_result.success:
                return marts_result

            marts_models = marts_result.data or []

            # Step 6: Write all models to disk
            all_models = staging_models + intermediate_models + marts_models
            logger.info("Writing %d models to disk...", len(all_models))

            write_result = self.model_generator.write_models_to_disk(
                all_models, output_dir,
            )
            if not write_result.success:
                return write_result

            # Collect workflow results
            workflow_results = {
                "connection_status": connection_result.data,
                "extracted_objects": len(oracle_objects),
                "generated_models": {
                    "staging": len(staging_models),
                    "intermediate": len(intermediate_models),
                    "marts": len(marts_models),
                    "total": len(all_models),
                },
                "written_files": write_result.data,
                "output_path": str(output_dir),
                "processed_schemas": schema_names or "all accessible",
                "processed_object_types": object_types or "all types",
                "workflow_status": "completed",
            }

            logger.info(
                "Metadata-to-models workflow completed successfully: %s",
                workflow_results,
            )
            return FlextResult.ok(workflow_results)

        except Exception as e:
            logger.exception("Unexpected error in metadata-to-models workflow")
            return FlextResult.fail(
                f"Metadata-to-models workflow failed: {e}",
                error=FlextDbtOracleProcessingError(
                    f"Metadata-to-models workflow failed: {e}",
                ),
            )

    def run_full_transformation_pipeline(
        self,
        schema_names: list[str] | None = None,
        object_types: list[str] | None = None,
        model_names: list[str] | None = None,
        generate_models: bool = True,
        models_output_path: Path | str | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Run complete Oracle transformation pipeline with optional model generation.

        Args:
            schema_names: Oracle schemas to process
            object_types: Oracle object types to process
            model_names: Specific DBT models to run (None = all)
            generate_models: Whether to generate models before running DBT
            models_output_path: Path for generated models

        Returns:
            FlextResult containing complete pipeline results

        """
        try:
            logger.info("Starting full Oracle transformation pipeline")
            pipeline_results = {}

            # Step 1: Generate models if requested
            if generate_models:
                logger.info("Generating DBT models from Oracle metadata...")
                models_result = self.run_metadata_to_models_workflow(
                    schema_names,
                    object_types,
                    models_output_path,
                )
                if not models_result.success:
                    return models_result

                pipeline_results["model_generation"] = models_result.data

            # Step 2: Run DBT transformation pipeline
            logger.info("Running DBT transformation pipeline...")
            transformation_result = self.client.run_full_pipeline(
                schema_names,
                object_types,
                model_names,
            )
            if not transformation_result.success:
                return transformation_result

            pipeline_results["transformation"] = transformation_result.data

            # Combine results
            full_results = {
                "pipeline_type": "full_transformation",
                "model_generation_enabled": generate_models,
                "results": pipeline_results,
                "pipeline_status": "completed",
            }

            logger.info("Full Oracle transformation pipeline completed successfully")
            return FlextResult.ok(full_results)

        except Exception as e:
            logger.exception("Unexpected error in full transformation pipeline")
            return FlextResult.fail(
                f"Full transformation pipeline failed: {e}",
                error=FlextDbtOracleProcessingError(
                    f"Full transformation pipeline failed: {e}",
                ),
            )

    def validate_workflow_prerequisites(self) -> FlextResult[dict[str, Any]]:
        """Validate all prerequisites for running Oracle-to-DBT workflows.

        Returns:
            FlextResult containing validation results

        """
        try:
            logger.info("Validating workflow prerequisites...")
            validation_results = {}

            # Step 1: Validate configuration
            if not self.config.validate_oracle_connection():
                return FlextResult.fail(
                    "Invalid Oracle connection configuration",
                    error=FlextDbtOracleResourceError(
                        "Invalid Oracle connection configuration",
                    ),
                )
            validation_results["config_validation"] = "passed"

            # Step 2: Test Oracle connection
            connection_result = self.client.test_oracle_connection()
            if not connection_result.success:
                return connection_result
            validation_results["oracle_connection"] = connection_result.data

            # Step 3: Validate DBT setup
            try:
                _ = self.client.dbt_hub
                dbt_validation = {"status": "available", "hub_initialized": True}
            except Exception as e:
                logger.warning("DBT hub validation failed: %s", e)
                dbt_validation = {"status": "error", "error": str(e)}

            validation_results["dbt_setup"] = dbt_validation

            # Step 4: Check required directories and permissions
            try:
                project_dir = Path(self.config.dbt_project_dir)
                if not project_dir.exists():
                    project_dir.mkdir(parents=True)

                validation_results["directory_access"] = {
                    "project_dir": str(project_dir),
                    "writable": project_dir.is_dir(),
                }
            except Exception as e:
                validation_results["directory_access"] = {"error": str(e)}

            overall_status = "passed"
            if any(
                result.get("status") == "error" or "error" in result
                for result in validation_results.values()
                if isinstance(result, dict)
            ):
                overall_status = "failed"

            final_results = {
                "overall_status": overall_status,
                "validations": validation_results,
                "prerequisites_met": overall_status == "passed",
            }

            logger.info(
                "Workflow prerequisites validation completed: %s", overall_status,
            )
            return FlextResult.ok(final_results)

        except Exception as e:
            logger.exception("Unexpected error during prerequisites validation")
            return FlextResult.fail(
                f"Prerequisites validation failed: {e}",
                error=FlextDbtOracleResourceError(
                    f"Prerequisites validation failed: {e}",
                ),
            )

    def get_workflow_recommendations(
        self,
        oracle_objects: list[FlextOracleObject] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Get recommendations for optimal workflow configuration.

        Args:
            oracle_objects: Oracle objects to analyze (None = extract from database)

        Returns:
            FlextResult containing workflow recommendations

        """
        try:
            logger.info("Generating workflow recommendations...")

            # Extract objects if not provided
            if oracle_objects is None:
                metadata_result = self.client.extract_oracle_metadata()
                if not metadata_result.success:
                    return metadata_result
                oracle_objects = metadata_result.data or []

            if not oracle_objects:
                return FlextResult.ok(
                    {
                        "message": "No Oracle objects found for analysis",
                        "recommendations": [],
                    },
                )

            # Analyze objects and generate recommendations
            recommendations = []

            # Analyze object distribution
            object_counts = {}
            schema_counts = {}
            for obj in oracle_objects:
                obj_type = obj.object_type
                schema_name = obj.schema_name

                object_counts[obj_type] = object_counts.get(obj_type, 0) + 1
                schema_counts[schema_name] = schema_counts.get(schema_name, 0) + 1

            # Performance recommendations
            total_objects = len(oracle_objects)
            if total_objects > 100:
                recommendations.append(
                    {
                        "type": "performance",
                        "priority": "high",
                        "message": f"Large number of objects ({total_objects}). Consider processing by schema.",
                        "suggestion": "Use schema_names parameter to process schemas in batches",
                    },
                )

            # Schema recommendations
            if len(schema_counts) > 10:
                recommendations.append(
                    {
                        "type": "organization",
                        "priority": "medium",
                        "message": f"Many schemas detected ({len(schema_counts)}). Consider grouping.",
                        "suggestion": "Focus on core business schemas for initial implementation",
                    },
                )

            # Object type recommendations
            table_count = object_counts.get("TABLE", 0)
            view_count = object_counts.get("VIEW", 0)

            if view_count > table_count:
                recommendations.append(
                    {
                        "type": "modeling",
                        "priority": "medium",
                        "message": "More views than tables detected. Views may have dependencies.",
                        "suggestion": "Start with base tables, then add views in dependency order",
                    },
                )

            # Configuration recommendations based on data volume
            if total_objects > 50:
                recommendations.append(
                    {
                        "type": "configuration",
                        "priority": "medium",
                        "message": "Large dataset detected. Consider performance optimizations.",
                        "suggestion": f"Increase threads to {min(8, max(4, total_objects // 25))} and batch_size to 5000",
                    },
                )

            results = {
                "analysis": {
                    "total_objects": total_objects,
                    "object_type_distribution": object_counts,
                    "schema_distribution": schema_counts,
                    "most_common_object_type": max(object_counts, key=object_counts.get)
                    if object_counts
                    else None,
                    "largest_schema": max(schema_counts, key=schema_counts.get)
                    if schema_counts
                    else None,
                },
                "recommendations": recommendations,
                "suggested_config": {
                    "dbt_threads": min(8, max(4, total_objects // 25))
                    if total_objects > 50
                    else 4,
                    "batch_size": 5000 if total_objects > 100 else 1000,
                    "enable_parallel_dml": total_objects > 50,
                },
            }

            logger.info("Generated %d workflow recommendations", len(recommendations))
            return FlextResult.ok(results)

        except Exception as e:
            logger.exception("Unexpected error generating workflow recommendations")
            return FlextResult.fail(
                f"Recommendations generation failed: {e}",
                error=FlextDbtOracleProcessingError(
                    f"Recommendations generation failed: {e}",
                ),
            )


class FlextDbtOracleMonitoringService:
    """Service for monitoring Oracle-to-DBT workflow execution.

    Provides monitoring, logging, and metrics collection for workflow execution.
    """

    def __init__(
        self,
        config: FlextDbtOracleConfig,
    ) -> None:
        """Initialize monitoring service.

        Args:
            config: Configuration for monitoring settings

        """
        self.config = config
        logger.info("Initialized Oracle DBT monitoring service")

    def track_workflow_execution(
        self,
        workflow_type: str,
        workflow_params: dict[str, Any],
    ) -> dict[str, Any]:
        """Track workflow execution metrics.

        Args:
            workflow_type: Type of workflow being executed
            workflow_params: Parameters passed to workflow

        Returns:
            Dictionary containing execution tracking information

        """
        tracking_info = {
            "workflow_type": workflow_type,
            "start_time": time.time(),
            "parameters": workflow_params,
            "tracking_id": f"{workflow_type}_{int(time.time())}",
        }

        logger.info(
            "Started tracking workflow execution: %s", tracking_info["tracking_id"],
        )
        return tracking_info

    def log_workflow_completion(
        self,
        tracking_info: dict[str, Any],
        result: FlextResult[Any],
    ) -> None:
        """Log workflow completion metrics.

        Args:
            tracking_info: Tracking information from track_workflow_execution
            result: Workflow execution result

        """
        end_time = time.time()
        duration = end_time - tracking_info["start_time"]

        completion_info = {
            "tracking_id": tracking_info["tracking_id"],
            "workflow_type": tracking_info["workflow_type"],
            "duration_seconds": round(duration, 2),
            "success": result.success,
            "result_summary": str(result.data)[:200] if result.data else None,
            "error_summary": str(result.error)[:200] if result.error else None,
        }

        if result.success:
            logger.info("Workflow completed successfully: %s", completion_info)
        else:
            logger.error("Workflow failed: %s", completion_info)


__all__: list[str] = [
    "FlextDbtOracleMonitoringService",
    "FlextDbtOracleWorkflowService",
]
