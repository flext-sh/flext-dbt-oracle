"""FLEXT DBT ORACLE - Oracle Database Transformations with simplified imports.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Version 0.7.0 - DBT Oracle with simplified public API:
- All common imports available from root: from flext_dbt_oracle import OracleAdapter
- Built on flext-core foundation for robust Oracle database transformations
- Deprecation warnings for internal imports
"""

from __future__ import annotations

import contextlib
import importlib.metadata
import warnings

# Foundation patterns - ALWAYS from flext-core
from flext_core import (
    BaseConfig,
    BaseConfig as OracleBaseConfig,  # Configuration base
    DomainBaseModel,
    DomainBaseModel as BaseModel,  # Base for Oracle models
    DomainError as OracleError,  # Oracle-specific errors
    ValidationError as ValidationError,  # Validation errors
)
from flext_core.domain.shared_types import ServiceResult

try:
    __version__ = importlib.metadata.version("flext-dbt-oracle")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.7.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


class FlextDbtOracleDeprecationWarning(DeprecationWarning):
    """Custom deprecation warning for FLEXT DBT ORACLE import changes."""


def _show_deprecation_warning(old_import: str, new_import: str) -> None:
    """Show deprecation warning for import paths."""
    message_parts = [
        f"⚠️  DEPRECATED IMPORT: {old_import}",
        f"✅ USE INSTEAD: {new_import}",
        "🔗 This will be removed in version 1.0.0",
        "📖 See FLEXT DBT ORACLE docs for migration guide",
    ]
    warnings.warn(
        "\n".join(message_parts),
        FlextDbtOracleDeprecationWarning,
        stacklevel=3,
    )


# ================================
# SIMPLIFIED PUBLIC API EXPORTS
# ================================

# Re-export commonly used imports from flext-core are now imported at top

# DBT Oracle Adapters exports - simplified imports
with contextlib.suppress(ImportError):
    from dbt.adapters.oracle import (
        OracleAdapter,
        OracleConnectionManager,
        OracleRelation,
    )

# DBT Oracle Transformations exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_dbt_oracle.transformations import (
        OracleMacroUtils,
        OracleModelBuilder,
        OracleTransformer,
    )

# ================================
# PUBLIC API EXPORTS
# ================================

__all__ = [
    "BaseModel",  # from flext_dbt_oracle import BaseModel
    # Deprecation utilities
    "FlextDbtOracleDeprecationWarning",
    # DBT Oracle Adapters (simplified access)
    "OracleAdapter",  # from flext_dbt_oracle import OracleAdapter
    # Core Patterns (from flext-core)
    "OracleBaseConfig",  # from flext_dbt_oracle import OracleBaseConfig
    "OracleConnectionManager",  # from flext_dbt_oracle import OracleConnectionManager
    "OracleError",  # from flext_dbt_oracle import OracleError
    # DBT Oracle Macros (simplified access)
    "OracleMacroUtils",  # from flext_dbt_oracle import OracleMacroUtils
    # DBT Oracle Models (simplified access)
    "OracleModelBuilder",  # from flext_dbt_oracle import OracleModelBuilder
    "OracleRelation",  # from flext_dbt_oracle import OracleRelation
    # DBT Oracle Transformations (simplified access)
    "OracleTransformer",  # from flext_dbt_oracle import OracleTransformer
    "ServiceResult",  # from flext_dbt_oracle import ServiceResult
    "ValidationError",  # from flext_dbt_oracle import ValidationError
    # Version
    "__version__",
    "__version_info__",
]
