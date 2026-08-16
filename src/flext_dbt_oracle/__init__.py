# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

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
    from flext_db_oracle import d, e, h, r, x

    from ._config import FlextDbtOracleConfig, config
    from ._settings import FlextDbtOracleSettings, settings
    from .base import FlextDbtOracleServiceBase, FlextDbtOracleServiceBase as s
    from .constants import FlextDbtOracleConstants, FlextDbtOracleConstants as c
    from .models import FlextDbtOracleModels, FlextDbtOracleModels as m
    from .protocols import FlextDbtOracleProtocols, FlextDbtOracleProtocols as p
    from .typings import FlextDbtOracleTypes, FlextDbtOracleTypes as t
    from .utilities import FlextDbtOracleUtilities, FlextDbtOracleUtilities as u
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
    MappingProxyType(
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
                "flext_db_oracle": ("d", "e", "h", "r", "x"),
            }),
            alias_groups=MappingProxyType({}),
            sort_keys=False,
        )
    ),
    public_exports=__all__,
)
