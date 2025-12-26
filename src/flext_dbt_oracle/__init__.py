"""FLEXT Enterprise - dbt-oracle adapter component."""

from __future__ import annotations

# Import local classes
from flext_dbt_oracle.adapters import OracleTableAdapter, OracleTableFactory
from flext_dbt_oracle.client import FlextDbtOracleClient
from flext_dbt_oracle.models import (
    FlextDbtOracleModelGenerator,
    FlextDbtOracleModels,
)
from flext_dbt_oracle.protocols import FlextDbtOracleProtocols
from flext_dbt_oracle.services import (
    FlextDbtOracleMonitoringService,
    FlextDbtOracleWorkflowService,
)
from flext_dbt_oracle.settings import FlextDbtOracleSettings
from flext_dbt_oracle.simple_api import FlextDbtOracle, FlextDbtOracleAPI
from flext_dbt_oracle.typings import FlextDbtOracleTypes
from flext_dbt_oracle.utilities import FlextDbtOracleUtilities

__version__ = "1.0.0"
__version_info__ = (1, 0, 0)

__all__ = [
    "FlextDbtOracle",
    "FlextDbtOracleAPI",
    "FlextDbtOracleClient",
    "FlextDbtOracleModelGenerator",
    "FlextDbtOracleModels",
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
