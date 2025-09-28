"""Modern Oracle Database DBT Integration for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle.adapters import OracleTableAdapter, OracleTableFactory
from flext_dbt_oracle.client import FlextDbtOracleClient
from flext_dbt_oracle.config import FlextDbtOracleConfig
from flext_dbt_oracle.exceptions import (
    FlextDbtOracleAuthenticationError,
    FlextDbtOracleCompilationError,
    FlextDbtOracleConfigurationError,
    FlextDbtOracleConnectionError,
    FlextDbtOracleDatabaseError,
    FlextDbtOracleError,
    FlextDbtOracleExecutionError,
    FlextDbtOracleModelError,
    FlextDbtOracleProcessingError,
    FlextDbtOracleQueryError,
    FlextDbtOracleTimeoutError,
    FlextDbtOracleValidationError,
)
from flext_dbt_oracle.models import (
    FlextDbtOracleModel,
    FlextDbtOracleModelGenerator,
)
from flext_dbt_oracle.services import (
    FlextDbtOracleMonitoringService,
    FlextDbtOracleWorkflowService,
)
from flext_dbt_oracle.typings import FlextDbtOracleTypes
from flext_dbt_oracle.utilities import FlextDbtOracleUtilities

__version__ = "0.9.0"
__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())
__author__ = "FLEXT Team"
__email__ = "team@flext.sh"

__all__: FlextDbtOracleTypes.Core.StringList = [
    "FlextDbtOracleAuthenticationError",
    "FlextDbtOracleClient",
    "FlextDbtOracleCompilationError",
    "FlextDbtOracleConfig",
    "FlextDbtOracleConfigurationError",
    "FlextDbtOracleConnectionError",
    "FlextDbtOracleDatabaseError",
    "FlextDbtOracleError",
    "FlextDbtOracleExecutionError",
    "FlextDbtOracleModel",
    "FlextDbtOracleModelError",
    "FlextDbtOracleModelGenerator",
    "FlextDbtOracleMonitoringService",
    "FlextDbtOracleProcessingError",
    "FlextDbtOracleQueryError",
    "FlextDbtOracleTimeoutError",
    "FlextDbtOracleUtilities",
    "FlextDbtOracleValidationError",
    "FlextDbtOracleWorkflowService",
    "OracleTableAdapter",
    "OracleTableFactory",
    "__author__",
    "__email__",
    "__version__",
    "__version_info__",
]
