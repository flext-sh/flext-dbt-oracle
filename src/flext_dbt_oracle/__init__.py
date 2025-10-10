"""Modern Oracle Database DBT Integration for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_dbt_oracle.__version__ import __version__, __version_info__
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
from flext_dbt_oracle.protocols import FlextDbtOracleProtocols
from flext_dbt_oracle.services import (
    FlextDbtOracleMonitoringService,
    FlextDbtOracleWorkflowService,
)
from flext_dbt_oracle.simple_api import FlextDbtOracle, FlextDbtOracleAPI
from flext_dbt_oracle.typings import FlextDbtOracleTypes
from flext_dbt_oracle.utilities import FlextDbtOracleUtilities
from flext_dbt_oracle.version import VERSION, FlextDbtOracleVersion

PROJECT_VERSION: Final[FlextDbtOracleVersion] = VERSION

__version__: str = VERSION.version
__version_info__: tuple[int | str, ...] = VERSION.version_info

__all__ = [
    "FlextDbtOracle",
    "FlextDbtOracleAPI",
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
    "FlextDbtOracleProtocols",
    "FlextDbtOracleQueryError",
    "FlextDbtOracleTimeoutError",
    "FlextDbtOracleTypes",
    "FlextDbtOracleUtilities",
    "FlextDbtOracleValidationError",
    "FlextDbtOracleWorkflowService",
    "OracleTableAdapter",
    "OracleTableFactory",
    "__version__",
    "__version_info__",
]
