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

    from ._config import FlextDbtOracleConfig, config
    from ._settings import FlextDbtOracleSettings, settings
    from .base import FlextDbtOracleServiceBase, s
    from .constants import FlextDbtOracleConstants, FlextDbtOracleConstants as c
    from .models import FlextDbtOracleModels, FlextDbtOracleModels as m
    from .protocols import FlextDbtOracleProtocols, FlextDbtOracleProtocols as p
    from .typings import FlextDbtOracleTypes, FlextDbtOracleTypes as t
    from .utilities import FlextDbtOracleUtilities, FlextDbtOracleUtilities as u

    _ = (
        c,
        FlextDbtOracleConstants,
        t,
        FlextDbtOracleTypes,
        p,
        FlextDbtOracleProtocols,
        m,
        FlextDbtOracleModels,
        u,
        FlextDbtOracleUtilities,
        d,
        e,
        h,
        r,
        x,
        s,
        FlextDbtOracleServiceBase,
        FlextDbtOracleConfig,
        config,
        FlextDbtOracleSettings,
        settings,
    )


_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._config": (
        "FlextDbtOracleConfig",
        "config",
    ),
    "._settings": (
        "FlextDbtOracleSettings",
        "settings",
    ),
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
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES,
    alias_groups=_LAZY_ALIAS_GROUPS,
    sort_keys=False,
)

_DIRECT_IMPORTS: tuple[str, ...] = (
    "FlextDbtOracleConfig",
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
    "build_lazy_import_map",
    "c",
    "config",
    "d",
    "e",
    "h",
    "install_lazy_exports",
    "m",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "u",
    "x",
)

__all__: tuple[str, ...] = (
    "FlextDbtOracleConfig",
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
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=__all__,
)
