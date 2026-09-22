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
<<<<<<< HEAD
    from flext_cli import cli
    from flext_db_oracle import db_oracle, e
    from flext_meltano import meltano
    from pydantic_core import from_json, to_json, to_jsonable_python

    from flext_core import core, d, h, lazy_attribute, r, x
=======
    from flext_db_oracle import e

    from flext_core import d, h, r, x
>>>>>>> origin/0.12.0-dev

    from . import services
    from ._config import FlextDbtOracleConfig, config
    from ._settings import FlextDbtOracleSettings, settings
    from .api import FlextDbtOracle
    from .base import FlextDbtOracleServiceBase, FlextDbtOracleServiceBase as s
    from .cli import FlextDbtOracleCliService, main
    from .constants import FlextDbtOracleConstants, c
    from .models import FlextDbtOracleModels, m
    from .protocols import FlextDbtOracleProtocols, p
    from .services.base import FlextDbtOracleServicesBase
    from .services.client import FlextDbtOracleServicesClient
    from .typings import FlextDbtOracleTypes, t
    from .utilities import FlextDbtOracleUtilities, u
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
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "db_oracle",
    "e",
    "from_json",
    "h",
    "lazy_attribute",
    "m",
    "main",
    "meltano",
    "p",
    "r",
    "s",
    "services",
    "settings",
    "t",
    "to_json",
    "to_jsonable_python",
    "u",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
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
<<<<<<< HEAD
            "flext_cli": ("cli",),
            "flext_core": ("core", "d", "h", "lazy_attribute", "r", "x"),
            "flext_db_oracle": ("db_oracle", "e"),
            "flext_meltano": ("meltano",),
            "pydantic_core": ("from_json", "to_json", "to_jsonable_python"),
=======
            "flext_core": ("d", "h", "r", "x"),
            "flext_db_oracle": ("e",),
>>>>>>> origin/0.12.0-dev
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
