"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import time
from pathlib import Path

from flext_db_oracle.models import FlextDbOracleModels

from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_db_oracle import FlextDbOracleApi
from flext_dbt_oracle.client import FlextDbtOracleClient
from flext_dbt_oracle.config import FlextDbtOracleConfig
from flext_dbt_oracle.constants import FlextDbtOracleConstants
from flext_dbt_oracle.models import FlextDbtOracleModel

# Type alias for Oracle table objects
FlextOracleObject = FlextDbOracleModels.Table

logger = FlextLogger(__name__)


class FlextDbtOracleWorkflowService:
    """Unified Oracle-to-DBT workflow service with monitoring capabilities.

    Provides high-level workflow orchestration that combines metadata extraction,
    model generation, and DBT execution into cohesive data transformation pipelines,
    with integrated monitoring functionality following FLEXT unified class pattern.
    """

    def __init__(
        self,
        config: FlextDbtOracleConfig | None = None,
    ) -> None:
        """Initialize workflow service.

        Args:
            config: Configuration for Oracle and DBT operations

        """
        self.config: dict[str, object] = config or FlextDbtOracleConfig()
        self.client = FlextDbtOracleClient(self.config)

        # Initialize Oracle API for model generation
        oracle_config: dict[str, object] = self.config.get_oracle_config()
        self.oracle_api = FlextDbOracleApi(oracle_config)
        self.model_generator = FlextDbtOracleModel.create_generator(
            self.config,
            self.oracle_api,
        )

        # Initialize monitoring service
        self.monitoring_service = self._MonitoringService(self.config)

        logger.info("Initialized Oracle DBT workflow service")

    def run_metadata_to_models_workflow(
        self,
        schema_names: FlextTypes.Core.StringList | None = None,
        object_types: FlextTypes.Core.StringList | None = None,
        output_path: Path | str | None = None,
    ) -> FlextResult[FlextTypes.Core.Dict]:
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
            connection_result: FlextResult[object] = (
                self.client.test_oracle_connection()
            )
            if not connection_result.success:
                return connection_result

            # Step 2: Extract Oracle metadata
            logger.info("Extracting Oracle metadata...")
            metadata_result = self.client.extract_oracle_metadata(
                schema_names,
                object_types,
            )
            if not metadata_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    metadata_result.error or "Metadata extraction failed",
                )

            oracle_objects = metadata_result.value or []
            logger.info("Extracted metadata for %d Oracle objects", len(oracle_objects))

            # Step 3: Generate staging models
            logger.info("Generating staging models...")
            staging_result = self.model_generator.generate_staging_models(
                oracle_objects,
            )
            if not staging_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    staging_result.error or "Staging model generation failed",
                )

            staging_models = staging_result.value or []

            # Step 4: Generate intermediate models
            logger.info("Generating intermediate models...")
            intermediate_result = self.model_generator.generate_intermediate_models(
                staging_models,
            )
            if not intermediate_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    intermediate_result.error or "Intermediate model generation failed",
                )

            intermediate_models = intermediate_result.value or []

            # Step 5: Generate marts models
            logger.info("Generating marts models...")
            marts_result = self.model_generator.generate_marts_models(
                intermediate_models,
            )
            if not marts_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    marts_result.error or "Marts model generation failed",
                )

            marts_models = marts_result.value or []

            # Step 6: Write all models to disk
            all_models = staging_models + intermediate_models + marts_models
            logger.info("Writing %d models to disk...", len(all_models))

            write_result = self.model_generator.write_models_to_disk(
                all_models,
                output_dir,
            )
            if not write_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    write_result.error or "Failed writing models",
                )

            # Collect workflow results
            workflow_results: FlextTypes.Core.Dict = {
                "connection_status": connection_result.value,
                "extracted_objects": len(oracle_objects),
                "generated_models": {
                    "staging": len(staging_models),
                    "intermediate": len(intermediate_models),
                    "marts": len(marts_models),
                    "total": len(all_models),
                },
                "written_files": write_result.value,
                "output_path": str(output_dir),
                "processed_schemas": schema_names or "all accessible",
                "processed_object_types": object_types or "all types",
                "workflow_status": "completed",
            }

            logger.info(
                "Metadata-to-models workflow completed successfully: %s",
                workflow_results,
            )
            return FlextResult[FlextTypes.Core.Dict].ok(workflow_results)

        except Exception as e:
            logger.exception("Unexpected error in metadata-to-models workflow")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"Metadata-to-models workflow failed: {e}",
            )

    def run_full_transformation_pipeline(
        self,
        schema_names: FlextTypes.Core.StringList | None = None,
        object_types: FlextTypes.Core.StringList | None = None,
        model_names: FlextTypes.Core.StringList | None = None,
        *,
        generate_models: bool = True,
        models_output_path: Path | str | None = None,
    ) -> FlextResult[FlextTypes.Core.Dict]:
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
                    return FlextResult[FlextTypes.Core.Dict].fail(
                        models_result.error or "Model generation failed",
                    )

                pipeline_results["model_generation"] = models_result.value

            # Step 2: Run DBT transformation pipeline
            logger.info("Running DBT transformation pipeline...")
            transformation_result = self.client.run_full_pipeline(
                schema_names,
                object_types,
                model_names,
            )
            if not transformation_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    transformation_result.error or "Transformation failed",
                )

            pipeline_results["transformation"] = transformation_result.value

            # Combine results
            full_results = {
                "pipeline_type": "full_transformation",
                "model_generation_enabled": generate_models,
                "results": pipeline_results,
                "pipeline_status": "completed",
            }

            logger.info("Full Oracle transformation pipeline completed successfully")
            return FlextResult[FlextTypes.Core.Dict].ok(full_results)

        except Exception as e:
            logger.exception("Unexpected error in full transformation pipeline")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"Full transformation pipeline failed: {e}",
            )

    def validate_workflow_prerequisites(
        self: object,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Validate all prerequisites for running Oracle-to-DBT workflows.

        Returns:
            FlextResult containing validation results

        """
        try:
            logger.info("Validating workflow prerequisites...")
            validation_results: FlextTypes.Core.Dict = {}

            # Step 1: Validate configuration
            if not self.config.validate_oracle_connection():
                return FlextResult[FlextTypes.Core.Dict].fail(
                    "Invalid Oracle connection configuration",
                )
            validation_results["config_validation"] = "passed"

            # Step 2: Test Oracle connection
            connection_result: FlextResult[object] = (
                self.client.test_oracle_connection()
            )
            if not connection_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    connection_result.error or "Connection failed",
                )
            validation_results["oracle_connection"] = connection_result.value or {}

            # Step 3: Validate DBT setup
            try:
                _ = self.client.dbt_hub
                dbt_validation: FlextTypes.Core.Dict = {
                    "status": "available",
                    "hub_initialized": True,
                }
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
            has_errors = False
            for result in validation_results.values():
                if isinstance(result, dict):
                    status = result.get("status")
                    if status == "error" or "error" in result:
                        has_errors = True
                        break
            if has_errors:
                overall_status = "failed"

            final_results: FlextTypes.Core.Dict = {
                "overall_status": overall_status,
                "validations": validation_results,
                "prerequisites_met": overall_status == "passed",
            }

            logger.info(
                "Workflow prerequisites validation completed: %s",
                overall_status,
            )
            return FlextResult[FlextTypes.Core.Dict].ok(final_results)

        except Exception as e:
            logger.exception("Unexpected error during prerequisites validation")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"Prerequisites validation failed: {e}",
            )

    def get_workflow_recommendations(
        self,
        oracle_objects: list[FlextOracleObject] | None = None,
    ) -> FlextResult[FlextTypes.Core.Dict]:
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
                metadata_result: FlextResult[object] = (
                    self.client.extract_oracle_metadata()
                )
                if not metadata_result.success:
                    return FlextResult[FlextTypes.Core.Dict].fail(
                        metadata_result.error or "Metadata extraction failed",
                    )
                oracle_objects = metadata_result.value or []

            if not oracle_objects:
                return FlextResult[FlextTypes.Core.Dict].ok(
                    {
                        "message": "No Oracle objects found for analysis",
                        "recommendations": [],
                    },
                )

            # Analyze objects and generate recommendations
            recommendations: list[FlextTypes.Core.Dict] = []

            # Analyze object distribution
            object_counts: dict[str, int] = {}
            schema_counts: dict[str, int] = {}
            for obj in oracle_objects:
                obj_type = "TABLE"
                schema_name = obj.schema_name

                object_counts[obj_type] = object_counts.get(obj_type, 0) + 1
                schema_counts[schema_name] = schema_counts.get(schema_name, 0) + 1

            # Performance recommendations
            total_objects = len(oracle_objects)
            if (
                total_objects
                > FlextDbtOracleConstants.Performance.LARGE_OBJECT_COUNT_THRESHOLD
            ):
                recommendations.append(
                    {
                        "type": "performance",
                        "priority": "high",
                        "message": f"Large number of objects ({total_objects}). Consider processing by schema.",
                        "suggestion": "Use schema_names parameter to process schemas in batches",
                    },
                )

            # Schema recommendations
            if (
                len(schema_counts)
                > FlextDbtOracleConstants.SchemaRecommendations.MANY_SCHEMAS_THRESHOLD
            ):
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
            if (
                total_objects
                > FlextDbtOracleConstants.ModelOptimization.MODERATE_OBJECT_COUNT
            ):
                recommendations.append(
                    {
                        "type": "configuration",
                        "priority": "medium",
                        "message": "Large dataset detected. Consider performance optimizations.",
                        "suggestion": f"Increase threads to {min(FlextDbtOracleConstants.ModelOptimization.MAX_THREADS, max(FlextDbtOracleConstants.ModelOptimization.MIN_THREADS, total_objects // FlextDbtOracleConstants.ModelOptimization.OBJECTS_PER_THREAD))} and batch_size to {FlextDbtOracleConstants.ModelOptimization.LARGE_BATCH_SIZE}",
                    },
                )

            results: FlextTypes.Core.Dict = {
                "analysis": {
                    "total_objects": total_objects,
                    "object_type_distribution": object_counts,
                    "schema_distribution": schema_counts,
                    "most_common_object_type": (
                        max(object_counts, key=lambda k: object_counts[k])
                        if object_counts
                        else None
                    )
                    if object_counts
                    else None,
                    "largest_schema": (
                        max(schema_counts, key=lambda k: schema_counts[k])
                        if schema_counts
                        else None
                    )
                    if schema_counts
                    else None,
                },
                "recommendations": recommendations,
                "suggested_config": {
                    "dbt_threads": min(
                        FlextDbtOracleConstants.ModelOptimization.MAX_THREADS,
                        max(
                            FlextDbtOracleConstants.ModelOptimization.MIN_THREADS,
                            total_objects
                            // FlextDbtOracleConstants.ModelOptimization.OBJECTS_PER_THREAD,
                        ),
                    )
                    if total_objects
                    > FlextDbtOracleConstants.ModelOptimization.LARGE_DATASET_THRESHOLD
                    else FlextDbtOracleConstants.ModelOptimization.MIN_THREADS,
                    "batch_size": FlextDbtOracleConstants.ModelOptimization.LARGE_BATCH_SIZE
                    if total_objects
                    > FlextDbtOracleConstants.Performance.LARGE_OBJECT_COUNT_THRESHOLD
                    else FlextDbtOracleConstants.ModelOptimization.DEFAULT_BATCH_SIZE,
                    "enable_parallel_dml": total_objects
                    > FlextDbtOracleConstants.ModelOptimization.LARGE_DATASET_THRESHOLD,
                },
            }

            logger.info("Generated %d workflow recommendations", len(recommendations))
            return FlextResult[FlextTypes.Core.Dict].ok(results)

        except Exception as e:
            logger.exception("Unexpected error generating workflow recommendations")
            return FlextResult[FlextTypes.Core.Dict].fail(
                f"Recommendations generation failed: {e}",
            )

    @classmethod
    def create_monitoring_service(
        cls,
        config: FlextDbtOracleConfig,
    ) -> _MonitoringService:
        """Factory method to create monitoring service instance."""
        return cls._MonitoringService(config)

    class _MonitoringService:
        """Nested helper class for monitoring workflow execution."""

        def __init__(
            self,
            config: FlextDbtOracleConfig,
        ) -> None:
            """Initialize monitoring service.

            Args:
                config: Configuration for monitoring settings

            """
            self.config: dict[str, object] = config
            logger.info("Initialized Oracle DBT monitoring service")

        def track_workflow_execution(
            self,
            workflow_type: str,
            workflow_params: FlextTypes.Core.Dict,
        ) -> FlextTypes.Core.Dict:
            """Track workflow execution metrics.

            Args:
                workflow_type: Type of workflow being executed
                workflow_params: Parameters passed to workflow

            Returns:
                Dictionary containing execution tracking information

            """
            tracking_info: FlextTypes.Core.Dict = {
                "workflow_type": workflow_type,
                "start_time": time.time(),
                "parameters": workflow_params,
                "tracking_id": f"{workflow_type}_{int(time.time())}",
            }

            logger.info(
                "Started tracking workflow execution: %s",
                tracking_info["tracking_id"],
            )
            return tracking_info

        def log_workflow_completion(
            self,
            tracking_info: FlextTypes.Core.Dict,
            result: FlextResult[object],
        ) -> None:
            """Log workflow completion metrics.

            Args:
                tracking_info: Tracking information from track_workflow_execution
                result: Workflow execution result

            """
            end_time = time.time()
            start_time = tracking_info.get("start_time")
            if isinstance(start_time, (int, float)):
                duration = end_time - float(start_time)
            else:
                duration = 0.0

            completion_info: FlextTypes.Core.Dict = {
                "tracking_id": tracking_info["tracking_id"],
                "workflow_type": tracking_info["workflow_type"],
                "duration_seconds": round(duration, 2),
                "success": result.success,
                "result_summary": str(result.value)[:200] if result.value else None,
                "error_summary": str(result.error)[:200] if result.error else None,
            }

            if result.success:
                logger.info("Workflow completed successfully: %s", completion_info)
            else:
                logger.error("Workflow failed: %s", completion_info)


__all__: FlextTypes.Core.StringList = [
    "FlextDbtOracleWorkflowService",
]
