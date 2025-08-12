"""FLEXT DBT Oracle - Modern Oracle Database DBT Integration.

This package provides enterprise-grade Oracle database integration for DBT using
the established flext DBT pattern with maximum composition from flext-db-oracle
and flext-meltano for reliable data transformation workflows.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

# New DBT Pattern API - Primary Interface
from flext_dbt_oracle.dbt_client import FlextDbtOracleClient
from flext_dbt_oracle.dbt_config import FlextDbtOracleConfig
from flext_dbt_oracle.dbt_exceptions import (
    FlextDbtOracleAuthenticationError,
    FlextDbtOracleCompilationError,
    FlextDbtOracleConfigError,
    FlextDbtOracleConnectionError,
    FlextDbtOracleDatabaseError,
    FlextDbtOracleExecutionError,
    FlextDbtOracleModelError,
    FlextDbtOraclePerformanceError,
    FlextDbtOraclePermissionError,
    FlextDbtOracleProcessingError,
    FlextDbtOracleQueryError,
    FlextDbtOracleResourceError,
    FlextDbtOracleSchemaError,
    FlextDbtOracleTimeoutError,
    FlextDbtOracleTransformationError,
    FlextDbtOracleTypeError,
    FlextDbtOracleValidationError,
)
from flext_dbt_oracle.dbt_models import (
    FlextDbtOracleModel,
    FlextDbtOracleModelGenerator,
)
from flext_dbt_oracle.dbt_services import (
    FlextDbtOracleMonitoringService,
    FlextDbtOracleWorkflowService,
)

# Version information
__version__ = "0.9.0"
__author__ = "FLEXT Team"
__email__ = "team@flext.sh"

# Public API - Following established flext DBT patterns
__all__: list[str] = [
    "annotations", "FlextDbtOracleClient", "FlextDbtOracleConfig", "FlextDbtOracleAuthenticationError",
    "FlextDbtOracleCompilationError", "FlextDbtOracleConfigError", "FlextDbtOracleConnectionError",
    "FlextDbtOracleDatabaseError", "FlextDbtOracleExecutionError", "FlextDbtOracleModelError",
    "FlextDbtOraclePerformanceError", "FlextDbtOraclePermissionError", "FlextDbtOracleProcessingError",
    "FlextDbtOracleQueryError", "FlextDbtOracleResourceError", "FlextDbtOracleSchemaError",
    "FlextDbtOracleTimeoutError", "FlextDbtOracleTransformationError", "FlextDbtOracleTypeError",
    "FlextDbtOracleValidationError", "FlextDbtOracleModel", "FlextDbtOracleModelGenerator",
    "FlextDbtOracleMonitoringService", "FlextDbtOracleWorkflowService", "__version__",
] = [
    # Core DBT Pattern Classes
    "FlextDbtOracleClient",
    "FlextDbtOracleConfig",
    "FlextDbtOracleModel",
    "FlextDbtOracleModelGenerator",
    # Workflow Services
    "FlextDbtOracleWorkflowService",
    "FlextDbtOracleMonitoringService",
    # Exception Classes (flext-core factory pattern)
    "FlextDbtOracleConfigError",
    "FlextDbtOracleConnectionError",
    "FlextDbtOracleAuthenticationError",
    "FlextDbtOracleProcessingError",
    "FlextDbtOracleValidationError",
    "FlextDbtOracleTransformationError",
    "FlextDbtOracleDatabaseError",
    "FlextDbtOracleQueryError",
    "FlextDbtOracleSchemaError",
    "FlextDbtOracleModelError",
    "FlextDbtOracleCompilationError",
    "FlextDbtOracleExecutionError",
    "FlextDbtOracleTypeError",
    "FlextDbtOraclePermissionError",
    "FlextDbtOracleResourceError",
    "FlextDbtOracleTimeoutError",
    "FlextDbtOraclePerformanceError",
    # Metadata
    "__author__",
    "__email__",
    "__version__",
]
