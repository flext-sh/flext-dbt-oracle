# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_dbt_oracle.__version__ import *

if _t.TYPE_CHECKING:
    from flext_db_oracle import d, e, h, r, s, x
    from flext_dbt_oracle._utilities.connections import FlextDbtOracleConnections
    from flext_dbt_oracle.base import FlextDbtOracleServiceBase
    from flext_dbt_oracle.constants import FlextDbtOracleConstants, c
    from flext_dbt_oracle.models import FlextDbtOracleModels, m
    from flext_dbt_oracle.protocols import FlextDbtOracleProtocols, p
    from flext_dbt_oracle.settings import FlextDbtOracleSettings
    from flext_dbt_oracle.typings import FlextDbtOracleTypes, t
    from flext_dbt_oracle.utilities import FlextDbtOracleUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    ("._utilities",),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            ".base": ("FlextDbtOracleServiceBase",),
            ".constants": (
                "FlextDbtOracleConstants",
                "c",
            ),
            ".models": (
                "FlextDbtOracleModels",
                "m",
            ),
            ".protocols": (
                "FlextDbtOracleProtocols",
                "p",
            ),
            ".settings": ("FlextDbtOracleSettings",),
            ".typings": (
                "FlextDbtOracleTypes",
                "t",
            ),
            ".utilities": (
                "FlextDbtOracleUtilities",
                "u",
            ),
            "flext_db_oracle": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__ = [
    "FlextDbtOracleConnections",
    "FlextDbtOracleConstants",
    "FlextDbtOracleModels",
    "FlextDbtOracleProtocols",
    "FlextDbtOracleServiceBase",
    "FlextDbtOracleSettings",
    "FlextDbtOracleTypes",
    "FlextDbtOracleUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]
