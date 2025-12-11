"""Modern Oracle Database DBT Integration for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Final

from flext_dbt_oracle.adapters import OracleTableAdapter, OracleTableFactory
from flext_dbt_oracle.client import FlextDbtOracleClient
from flext_dbt_oracle.config import FlextDbtOracleSettings
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
    "FlextDbtOracleClient",
    "FlextDbtOracleModel",
    "FlextDbtOracleModelGenerator",
    "FlextDbtOracleMonitoringService",
    "FlextDbtOracleProtocols",
    "FlextDbtOracleSettings",
    "FlextDbtOracleTypes",
    "FlextDbtOracleUtilities",
    "FlextDbtOracleWorkflowService",
    "OracleTableAdapter",
    "OracleTableFactory",
    "__version__",
    "__version_info__",
]
