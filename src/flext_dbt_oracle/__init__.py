# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports
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
    from flext_meltano import d, e, h, r, x

    from flext_dbt_oracle._config import FlextDbtOracleConfig, config
    from flext_dbt_oracle._settings import FlextDbtOracleSettings, settings
    from flext_dbt_oracle.api import FlextDbtOracle
    from flext_dbt_oracle.base import FlextDbtOracleServiceBase, s
    from flext_dbt_oracle.cli import main
    from flext_dbt_oracle.constants import FlextDbtOracleConstants, c
    from flext_dbt_oracle.models import FlextDbtOracleModels, m
    from flext_dbt_oracle.protocols import FlextDbtOracleProtocols, p
    from flext_dbt_oracle.typings import FlextDbtOracleTypes, t
    from flext_dbt_oracle.utilities import FlextDbtOracleUtilities, u


__all__: tuple[str, ...] = (
    "FlextDbtOracle",
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
    "main",
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
    MappingProxyType({
        "FlextDbtOracle": ".api",
        "FlextDbtOracleConfig": "._config",
        "FlextDbtOracleConstants": ".constants",
        "FlextDbtOracleModels": ".models",
        "FlextDbtOracleProtocols": ".protocols",
        "FlextDbtOracleServiceBase": ".base",
        "FlextDbtOracleSettings": "._settings",
        "FlextDbtOracleTypes": ".typings",
        "FlextDbtOracleUtilities": ".utilities",
        "c": ".constants",
        "config": "._config",
        "d": "flext_meltano",
        "e": "flext_meltano",
        "h": "flext_meltano",
        "m": ".models",
        "main": ".cli",
        "p": ".protocols",
        "r": "flext_meltano",
        "s": ".base",
        "settings": "._settings",
        "t": ".typings",
        "u": ".utilities",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)
