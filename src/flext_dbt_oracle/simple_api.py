"""FLEXT DBT ORACLE API - Unified facade for DBT Oracle operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Unified facade for FLEXT DBT Oracle operations with complete FLEXT integration.
"""

from __future__ import annotations

from pathlib import Path

from flext_core import (
    FlextContainer,
    FlextContext,
    FlextLogger,
    FlextResult,
    FlextService,
)

from flext_dbt_oracle.client import FlextDbtOracleClient
from flext_dbt_oracle.services import (
    FlextDbtOracleMonitoringService,
    FlextDbtOracleWorkflowService,
)
from flext_dbt_oracle.settings import FlextDbtOracleSettings


class FlextDbtOracle(FlextService[FlextDbtOracleSettings]):
    """Unified DBT Oracle facade with complete FLEXT ecosystem integration.

    This is the single unified class for the flext-dbt-oracle domain providing
    access to all DBT Oracle domain functionality with centralized patterns.

    UNIFIED CLASS PATTERN: One class per module with nested helpers only.
    CENTRALIZED APPROACH: All operations follow centralized patterns:
    - FlextDbtOracle.* for DBT Oracle-specific operations
    - Centralized validation through FlextDbtOracleWorkflowService
    - No wrappers, aliases, or fallbacks
    - Direct use of flext-core centralized services

    FLEXT INTEGRATION: Complete integration with flext-core patterns:
    - FlextContainer for dependency injection
    - FlextContext for operation context
    - FlextLogger for structured logging
    - FlextResult for railway-oriented error handling

    PYTHON 3.13+ COMPATIBILITY: Uses modern patterns and latest type features.
    """

    def __init__(self, config: FlextDbtOracleSettings | None = None) -> None:
        """Initialize the unified DBT Oracle service."""
        super().__init__()
        self._config = config or FlextDbtOracleSettings()
        self._client: FlextDbtOracleClient | None = None
        self._workflow_service: FlextDbtOracleWorkflowService | None = None
        self._monitoring_service: FlextDbtOracleMonitoringService | None = None

        # Complete FLEXT ecosystem integration
        self._container = FlextContainer.get_global().clear()().get_or_create()
        self._context = FlextContext()
        self.logger = FlextLogger(__name__)

    @classmethod
    def create(cls) -> FlextDbtOracle:
        """Create a new FlextDbtOracle instance (factory method)."""
        return cls()

    @property
    def client(self) -> FlextDbtOracleClient:
        """Get the DBT Oracle client instance."""
        if self._client is None:
            self._client = FlextDbtOracleClient(self._config)
        return self._client

    @property
    def workflow_service(self) -> FlextDbtOracleWorkflowService:
        """Get the workflow service instance."""
        if self._workflow_service is None:
            self._workflow_service = FlextDbtOracleWorkflowService(self._config)
        return self._workflow_service

    @property
    def monitoring_service(self) -> FlextDbtOracleMonitoringService:
        """Get the monitoring service instance."""
        if self._monitoring_service is None:
            self._monitoring_service = FlextDbtOracleMonitoringService(self._config)
        return self._monitoring_service

    @property
    def config(self) -> FlextDbtOracleSettings:
        """Get the current configuration."""
        return self._config

    # =============================================================================
    # MAIN WORKFLOW OPERATIONS - Enhanced with FlextResult error handling
    # =============================================================================

    def run_oracle_to_dbt_workflow(
        self,
        table_names: list[str] | None = None,
        schema_name: str | None = None,
        *,
        generate_models: bool = True,
        run_tests: bool = False,
    ) -> FlextResult[dict[str, object]]:
        """Run complete Oracle-to-DBT workflow.

        Args:
        table_names: List of table names to process (None for all)
        schema_name: Oracle schema name
        generate_models: Whether to generate DBT models
        run_tests: Whether to run DBT tests

        Returns:
        FlextResult containing workflow results

        """
        try:
            self.logger.info("Running Oracle-to-DBT workflow")
            return self.workflow_service.run_oracle_to_dbt_workflow(
                table_names=table_names,
                schema_name=schema_name,
                generate_models=generate_models,
                run_tests=run_tests,
            )
        except Exception as e:
            return FlextResult[dict[str, object]].fail(
                f"Workflow execution failed: {e}",
            )

    def generate_dbt_models_from_oracle(
        self,
        table_names: list[str] | None = None,
        schema_name: str | None = None,
        output_dir: Path | str | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Generate DBT models from Oracle tables.

        Args:
        table_names: List of table names to process
        schema_name: Oracle schema name
        output_dir: Output directory for generated models

        Returns:
        FlextResult containing model generation results

        """
        try:
            self.logger.info("Generating DBT models from Oracle tables")
            return self.workflow_service.generate_dbt_models_from_oracle(
                table_names=table_names,
                schema_name=schema_name,
                output_dir=output_dir,
            )
        except Exception as e:
            return FlextResult[dict[str, object]].fail(f"Model generation failed: {e}")

    def extract_oracle_metadata(
        self,
        table_names: list[str] | None = None,
        schema_name: str | None = None,
        *,
        include_constraints: bool = True,
        include_indexes: bool = True,
    ) -> FlextResult[dict[str, object]]:
        """Extract Oracle database metadata.

        Args:
        table_names: List of table names to process
        schema_name: Oracle schema name
        include_constraints: Whether to include constraint information
        include_indexes: Whether to include index information

        Returns:
        FlextResult containing metadata extraction results

        """
        try:
            self.logger.info("Extracting Oracle metadata")
            return self.workflow_service.extract_oracle_metadata(
                table_names=table_names,
                schema_name=schema_name,
                include_constraints=include_constraints,
                include_indexes=include_indexes,
            )
        except Exception as e:
            return FlextResult[dict[str, object]].fail(
                f"Metadata extraction failed: {e}",
            )

    def monitor_dbt_execution(
        self,
        command: str,
        timeout_seconds: int = 300,
    ) -> FlextResult[dict[str, object]]:
        """Monitor DBT command execution with metrics.

        Args:
        command: DBT command to execute
        timeout_seconds: Timeout for command execution

        Returns:
        FlextResult containing monitoring results

        """
        try:
            self.logger.info("Monitoring DBT execution: %s", command)
            return self.monitoring_service.monitor_dbt_execution(
                command=command,
                timeout_seconds=timeout_seconds,
            )
        except Exception as e:
            return FlextResult[dict[str, object]].fail(f"Monitoring failed: {e}")

    def validate_oracle_connection(self) -> FlextResult[bool]:
        """Validate Oracle database connection.

        Returns:
        FlextResult containing connection validation result

        """
        try:
            self.logger.info("Validating Oracle connection")
            return self.client.validate_connection()
        except Exception as e:
            return FlextResult[bool].fail(f"Connection validation failed: {e}")

    def get_oracle_table_info(
        self,
        table_name: str,
        schema_name: str | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Get detailed information about an Oracle table.

        Args:
        table_name: Name of the table
        schema_name: Schema name

        Returns:
        FlextResult containing table information

        """
        try:
            self.logger.info("Getting Oracle table info: %s", table_name)
            return self.client.get_table_info(
                table_name=table_name,
                schema_name=schema_name,
            )
        except Exception as e:
            return FlextResult[dict[str, object]].fail(
                f"Table info retrieval failed: {e}",
            )


# Alias for backward compatibility
FlextDbtOracleAPI = FlextDbtOracle

__all__ = [
    "FlextDbtOracle",
    "FlextDbtOracleAPI",
]
