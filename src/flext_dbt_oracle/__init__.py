"""Modern Oracle Database DBT Integration for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes

from flext_dbt_oracle.dbt_client import FlextDbtOracleClient
from flext_dbt_oracle.dbt_config import FlextDbtOracleConfig
from flext_dbt_oracle.dbt_exceptions import (
    FLEXT_DBT_ORACLEConfigurationError,
    FLEXT_DBT_ORACLEConnectionError,
    FLEXT_DBT_ORACLEError,
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
from flext_dbt_oracle.dbt_services import (
    FlextDbtOracleMonitoringService,
    FlextDbtOracleWorkflowService,
)
from flext_dbt_oracle.models import (
    FlextDbtOracleModel,
    FlextDbtOracleModelGenerator,
)

# Version information
__version__ = "0.9.0"
__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())
__author__ = "FLEXT Team"
__email__ = "team@flext.sh"

# Public API - Following established flext DBT patterns
__all__: FlextTypes.Core.StringList = [
    "FLEXT_DBT_ORACLEConfigurationError",
    "FLEXT_DBT_ORACLEConnectionError",
    # Exceptions
    "FLEXT_DBT_ORACLEError",
    "FLEXT_DBT_ORACLEProcessingError",
    "FLEXT_DBT_ORACLETimeoutError",
    "FLEXT_DBT_ORACLEValidationError",
    # Core DBT Pattern Classes
    "FlextDbtOracleClient",
    "FlextDbtOracleCompilationError",
    "FlextDbtOracleConfig",
    "FlextDbtOracleDatabaseError",
    "FlextDbtOracleExecutionError",
    "FlextDbtOracleModel",
    "FlextDbtOracleModelError",
    "FlextDbtOracleModelGenerator",
    "FlextDbtOracleMonitoringService",
    "FlextDbtOraclePerformanceError",
    "FlextDbtOraclePermissionError",
    "FlextDbtOracleQueryError",
    "FlextDbtOracleResourceError",
    "FlextDbtOracleSchemaError",
    "FlextDbtOracleTransformationError",
    "FlextDbtOracleTypeError",
    # Workflow Services
    "FlextDbtOracleWorkflowService",
    "__author__",
    "__email__",
    # Version
    "__version__",
    "__version_info__",
]
