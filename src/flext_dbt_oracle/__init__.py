"""FLEXT DBT Oracle Adapter - Modern Oracle Database Integration for DBT.

This adapter provides enterprise-grade Oracle database integration for DBT using
flext-infrastructure.databases.flext-db-oracle as the foundation, ensuring zero code
duplication and maximum
reliability for data transformation workflows.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_dbt_oracle.config import (
    DBTOracleConfig,
    DBTOracleSettings,
    OracleCredentialsConfig,
)
from flext_dbt_oracle.connections import OracleConnectionManager
from flext_dbt_oracle.constants import DBTOracleAdapterConstants
from flext_dbt_oracle.impl import OracleAdapter
from flext_dbt_oracle.types import (
    DBTOracleColumnInfo,
    DBTOracleCompilationResult,
    DBTOracleConnectionConfig,
    DBTOracleCredentials,
    DBTOracleExecutionResult,
    DBTOracleIndexInfo,
    DBTOracleModelConfig,
    DBTOracleRelationConfig,
    DBTOracleSchemaInfo,
    DBTOracleTableInfo,
    DBTOracleTestResult,
)

# Version information
__version__ = "0.9.0"
__author__ = "FLEXT Team"
__email__ = "team@flext.sh"

# Public API - following DBT adapter conventions
__all__: list[str] = [
    # Configuration classes
    "DBTOracleAdapterConstants",
    # Type definitions
    "DBTOracleColumnInfo",
    "DBTOracleCompilationResult",
    "DBTOracleConfig",
    "DBTOracleConnectionConfig",
    "DBTOracleCredentials",
    "DBTOracleExecutionResult",
    "DBTOracleIndexInfo",
    "DBTOracleModelConfig",
    "DBTOracleRelationConfig",
    "DBTOracleSchemaInfo",
    "DBTOracleSettings",
    "DBTOracleTableInfo",
    "DBTOracleTestResult",
    # Core adapter classes
    "OracleAdapter",
    "OracleConnectionManager",
    "OracleCredentialsConfig",
    # Metadata
    "__author__",
    "__email__",
    "__version__",
]
