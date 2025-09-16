"""Modern Oracle Database DBT Integration for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes

from flext_dbt_oracle.adapters import OracleTableAdapter, OracleTableFactory
from flext_dbt_oracle.client import FlextDbtOracleClient
from flext_dbt_oracle.config import FlextDbtOracleConfig
from flext_dbt_oracle.exceptions import (
    FLEXT_DBT_ORACLEAuthenticationError,
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
    FlextDbtOracleQueryError,
)
from flext_dbt_oracle.models import (
    FlextDbtOracleModel,
    FlextDbtOracleModelGenerator,
)
from flext_dbt_oracle.services import (
    FlextDbtOracleMonitoringService,
    FlextDbtOracleWorkflowService,
)

# Version information
__version__ = "0.9.0"
__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())
__author__ = "FLEXT Team"
__email__ = "team@flext.sh"

# Public API - Following established flext DBT patterns
__all__: FlextTypes.Core.StringList = [
    # Configuration Error Types
    "FLEXT_DBT_ORACLEAuthenticationError",
    "FLEXT_DBT_ORACLEConfigurationError",
    "FLEXT_DBT_ORACLEConnectionError",
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
    "FlextDbtOracleQueryError",
    "FlextDbtOracleWorkflowService",
    # Adapter Pattern Classes (SOLID Interface Segregation)
    "OracleTableAdapter",
    "OracleTableFactory",
    # Metadata
    "__author__",
    "__email__",
    "__version__",
    "__version_info__",
]
