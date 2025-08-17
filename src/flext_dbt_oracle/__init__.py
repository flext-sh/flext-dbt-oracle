"""Modern Oracle Database DBT Integration for FLEXT ecosystem."""

from __future__ import annotations

from flext_dbt_oracle.dbt_client import FlextDbtOracleClient
from flext_dbt_oracle.dbt_config import FlextDbtOracleConfig
from flext_dbt_oracle.dbt_exceptions import (
    FLEXT_DBT_ORACLEError,
    FLEXT_DBT_ORACLEConfigurationError,
    FLEXT_DBT_ORACLEConnectionError,
    FLEXT_DBT_ORACLEProcessingError,
    FLEXT_DBT_ORACLETimeoutError,
    FLEXT_DBT_ORACLEValidationError,
    FlextDbtOracleCompilationError,
    FlextDbtOracleDatabaseError,
    FlextDbtOracleExecutionError,
    FlextDbtOracleModelError,
    FlextDbtOraclePerformanceError,
    FlextDbtOraclePermissionError,
    FlextDbtOracleQueryError,
    FlextDbtOracleResourceError,
    FlextDbtOracleSchemaError,
    FlextDbtOracleTransformationError,
    FlextDbtOracleTypeError,
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
    # Exceptions
    "FLEXT_DBT_ORACLEError",
    "FLEXT_DBT_ORACLEConfigurationError",
    "FLEXT_DBT_ORACLEConnectionError",
    "FLEXT_DBT_ORACLEProcessingError",
    "FLEXT_DBT_ORACLETimeoutError",
    "FLEXT_DBT_ORACLEValidationError",
    "FlextDbtOracleCompilationError",
    "FlextDbtOracleDatabaseError",
    "FlextDbtOracleExecutionError",
    "FlextDbtOracleModelError",
    "FlextDbtOraclePerformanceError",
    "FlextDbtOraclePermissionError",
    "FlextDbtOracleQueryError",
    "FlextDbtOracleResourceError",
    "FlextDbtOracleSchemaError",
    "FlextDbtOracleTransformationError",
    "FlextDbtOracleTypeError",
    # Version
    "__version__",
    "__version_info__",
    "__author__",
    "__email__",
]
