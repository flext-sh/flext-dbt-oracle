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
    from flext_db_oracle import e
    from flext_meltano import d, h, r, x

    from . import services
    from .__version__ import FlextDbtOracleVersion
    from ._config import FlextDbtOracleConfig, config
    from ._settings import FlextDbtOracleSettings, settings
    from .api import FlextDbtOracle
    from .base import FlextDbtOracleServiceBase, FlextDbtOracleServiceBase as s
    from .cli import FlextDbtOracleCliService, main
    from .constants import FlextDbtOracleConstants, FlextDbtOracleConstants as c
    from .models import FlextDbtOracleModels, FlextDbtOracleModels as m
    from .protocols import FlextDbtOracleProtocols, FlextDbtOracleProtocols as p
    from .services.base import FlextDbtOracleServicesBase
    from .services.client import FlextDbtOracleServicesClient
    from .typings import FlextDbtOracleTypes, FlextDbtOracleTypes as t
    from .utilities import FlextDbtOracleUtilities, FlextDbtOracleUtilities as u
__all__: tuple[str, ...] = (
    "FlextDbtOracle",
    "FlextDbtOracleCliService",
    "FlextDbtOracleConfig",
    "FlextDbtOracleConstants",
    "FlextDbtOracleModels",
    "FlextDbtOracleProtocols",
    "FlextDbtOracleServiceBase",
    "FlextDbtOracleServicesBase",
    "FlextDbtOracleServicesClient",
    "FlextDbtOracleSettings",
    "FlextDbtOracleTypes",
    "FlextDbtOracleUtilities",
    "FlextDbtOracleVersion",
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
    "main",
    "p",
    "r",
    "s",
    "services",
    "settings",
    "t",
    "u",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".__version__": ("FlextDbtOracleVersion",),
            "._config": ("FlextDbtOracleConfig", "config"),
            "._settings": ("FlextDbtOracleSettings", "settings"),
            ".api": ("FlextDbtOracle",),
            ".base": ("FlextDbtOracleServiceBase", "s"),
            ".cli": ("FlextDbtOracleCliService", "main"),
            ".constants": ("FlextDbtOracleConstants", "c"),
            ".models": ("FlextDbtOracleModels", "m"),
            ".protocols": ("FlextDbtOracleProtocols", "p"),
            ".services": ("services",),
            ".services.base": ("FlextDbtOracleServicesBase",),
            ".services.client": ("FlextDbtOracleServicesClient",),
            ".typings": ("FlextDbtOracleTypes", "t"),
            ".utilities": ("FlextDbtOracleUtilities", "u"),
            "flext_db_oracle": ("e",),
            "flext_meltano": ("d", "h", "r", "x"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
