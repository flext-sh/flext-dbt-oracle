# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import (
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__ as __version__,
    __version_info__ as __version_info__,
)

if TYPE_CHECKING:
    from enum import StrEnum, unique
    from typing import Final

    from flext_db_oracle import FlextDbOracleConstants, d, e, h, r, x

    from ._config import FlextDbtOracleConfig, config
    from ._settings import FlextDbtOracleSettings, settings
    from .base import FlextDbtOracleServiceBase, FlextDbtOracleServiceBase as s
    from .constants import FlextDbtOracleConstants, FlextDbtOracleConstants as c
    from .models import FlextDbtOracleModels, FlextDbtOracleModels as m
    from .protocols import FlextDbtOracleProtocols, FlextDbtOracleProtocols as p
    from .typings import FlextDbtOracleTypes, FlextDbtOracleTypes as t
    from .utilities import FlextDbtOracleUtilities, FlextDbtOracleUtilities as u
__all__: tuple[str, ...] = (
    "Final",
    "FlextDbOracleConstants",
    "FlextDbtOracleConfig",
    "FlextDbtOracleConstants",
    "FlextDbtOracleModels",
    "FlextDbtOracleProtocols",
    "FlextDbtOracleServiceBase",
    "FlextDbtOracleSettings",
    "FlextDbtOracleTypes",
    "FlextDbtOracleUtilities",
    "StrEnum",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "config",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "u",
    "unique",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config": ("FlextDbtOracleConfig", "config"),
            "._settings": ("FlextDbtOracleSettings", "settings"),
            ".base": ("FlextDbtOracleServiceBase", "s"),
            ".constants": ("FlextDbtOracleConstants", "c"),
            ".models": ("FlextDbtOracleModels", "m"),
            ".protocols": ("FlextDbtOracleProtocols", "p"),
            ".typings": ("FlextDbtOracleTypes", "t"),
            ".utilities": ("FlextDbtOracleUtilities", "u"),
            "enum": ("StrEnum", "unique"),
            "flext_db_oracle": ("FlextDbOracleConstants", "d", "e", "h", "r", "x"),
            "typing": ("Final",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
