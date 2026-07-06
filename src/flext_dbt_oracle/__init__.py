# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports
from flext_dbt_oracle.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_db_oracle import d, e, h, r, x
    from flext_dbt_oracle.base import FlextDbtOracleServiceBase, s
    from flext_dbt_oracle.constants import FlextDbtOracleConstants, c
    from flext_dbt_oracle.models import FlextDbtOracleModels, m
    from flext_dbt_oracle.protocols import FlextDbtOracleProtocols, p
    from flext_dbt_oracle.settings import FlextDbtOracleSettings
    from flext_dbt_oracle.typings import FlextDbtOracleTypes, t
    from flext_dbt_oracle.utilities import FlextDbtOracleUtilities, u
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".base": (
            "FlextDbtOracleServiceBase",
            "s",
        ),
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
            "x",
        ),
    },
)


__all__: tuple[str, ...] = (
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
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=__all__,
)
