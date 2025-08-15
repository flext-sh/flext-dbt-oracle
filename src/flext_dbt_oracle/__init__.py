"""Modern Oracle Database DBT Integration for FLEXT ecosystem."""

from __future__ import annotations

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
from flext_dbt_oracle.models import (
    FlextDbtOracleModel,
    FlextDbtOracleModelGenerator,
)
from flext_dbt_oracle.dbt_services import (
    FlextDbtOracleMonitoringService,
    FlextDbtOracleWorkflowService,
)

# Version information
__version__ = "0.9.0"
__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())
__author__ = "FLEXT Team"
__email__ = "team@flext.sh"

# Public API - Following established flext DBT patterns
__all__: list[str] = [
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
    "__version_info__",
]
