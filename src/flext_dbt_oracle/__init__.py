# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import __author__ as __author__
from .__version__ import __author_email__ as __author_email__
from .__version__ import __description__ as __description__
from .__version__ import __license__ as __license__
from .__version__ import __title__ as __title__
from .__version__ import __url__ as __url__
from .__version__ import __version__ as __version__
from .__version__ import __version_info__ as __version_info__

if TYPE_CHECKING:
    from flext_db_oracle import d as d
    from flext_db_oracle import e as e
    from flext_db_oracle import h as h
    from flext_db_oracle import r as r
    from flext_db_oracle import x as x

    from ._config import FlextDbtOracleConfig as FlextDbtOracleConfig
    from ._config import config as config
    from ._settings import FlextDbtOracleSettings as FlextDbtOracleSettings
    from ._settings import settings as settings
    from .base import FlextDbtOracleServiceBase as FlextDbtOracleServiceBase

    s: type[FlextDbtOracleServiceBase]
    from .constants import FlextDbtOracleConstants as FlextDbtOracleConstants

    c: type[FlextDbtOracleConstants]
    from .models import FlextDbtOracleModels as FlextDbtOracleModels

    m: type[FlextDbtOracleModels]
    from .protocols import FlextDbtOracleProtocols as FlextDbtOracleProtocols

    p: type[FlextDbtOracleProtocols]
    from .typings import FlextDbtOracleTypes as FlextDbtOracleTypes

    t: type[FlextDbtOracleTypes]
    from .utilities import FlextDbtOracleUtilities as FlextDbtOracleUtilities

    u: type[FlextDbtOracleUtilities]

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._config": ("FlextDbtOracleConfig", "config"),
    "._settings": ("FlextDbtOracleSettings", "settings"),
    ".base": ("FlextDbtOracleServiceBase", "s"),
    ".constants": ("FlextDbtOracleConstants", "c"),
    ".models": ("FlextDbtOracleModels", "m"),
    ".protocols": ("FlextDbtOracleProtocols", "p"),
    ".typings": ("FlextDbtOracleTypes", "t"),
    ".utilities": ("FlextDbtOracleUtilities", "u"),
    "flext_db_oracle": ("d", "e", "h", "r", "x"),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
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

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
