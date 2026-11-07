# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, td, tf, tk, tm

    from flext_dbt_oracle import (
        FlextDbtOracle,
        FlextDbtOracleConfig,
        FlextDbtOracleConstants,
        FlextDbtOracleModels,
        FlextDbtOracleProtocols,
        FlextDbtOracleServiceBase,
        FlextDbtOracleSettings,
        FlextDbtOracleTypes,
        FlextDbtOracleUtilities,
        FlextDbtOracleVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
        config,
        d,
        e,
        h,
        main,
        r,
        settings,
        x,
    )
    from tests.base import TestsFlextDbtOracleServiceBase, s
    from tests.constants import TestsFlextDbtOracleConstants, c
    from tests.models import TestsFlextDbtOracleModels, m
    from tests.protocols import TestsFlextDbtOracleProtocols, p
    from tests.settings import TestsFlextDbtOracleSettings
    from tests.typings import TestsFlextDbtOracleTypes, t
    from tests.utilities import TestsFlextDbtOracleUtilities, u


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
    "FlextDbtOracleVersion",
    "TestsFlextDbtOracleConstants",
    "TestsFlextDbtOracleModels",
    "TestsFlextDbtOracleProtocols",
    "TestsFlextDbtOracleServiceBase",
    "TestsFlextDbtOracleSettings",
    "TestsFlextDbtOracleTypes",
    "TestsFlextDbtOracleUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "api",
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
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextDbtOracle": "flext_dbt_oracle",
        "FlextDbtOracleConfig": "flext_dbt_oracle",
        "FlextDbtOracleConstants": "flext_dbt_oracle",
        "FlextDbtOracleModels": "flext_dbt_oracle",
        "FlextDbtOracleProtocols": "flext_dbt_oracle",
        "FlextDbtOracleServiceBase": "flext_dbt_oracle",
        "FlextDbtOracleSettings": "flext_dbt_oracle",
        "FlextDbtOracleTypes": "flext_dbt_oracle",
        "FlextDbtOracleUtilities": "flext_dbt_oracle",
        "FlextDbtOracleVersion": "flext_dbt_oracle",
        "TestsFlextDbtOracleConstants": ".constants",
        "TestsFlextDbtOracleModels": ".models",
        "TestsFlextDbtOracleProtocols": ".protocols",
        "TestsFlextDbtOracleServiceBase": ".base",
        "TestsFlextDbtOracleSettings": ".settings",
        "TestsFlextDbtOracleTypes": ".typings",
        "TestsFlextDbtOracleUtilities": ".utilities",
        "__author__": "flext_dbt_oracle",
        "__author_email__": "flext_dbt_oracle",
        "__description__": "flext_dbt_oracle",
        "__license__": "flext_dbt_oracle",
        "__title__": "flext_dbt_oracle",
        "__url__": "flext_dbt_oracle",
        "__version__": "flext_dbt_oracle",
        "__version_info__": "flext_dbt_oracle",
        "api": "flext_tests",
        "c": ".constants",
        "config": "flext_dbt_oracle",
        "d": "flext_dbt_oracle",
        "e": "flext_dbt_oracle",
        "h": "flext_dbt_oracle",
        "m": ".models",
        "main": "flext_dbt_oracle",
        "p": ".protocols",
        "r": "flext_dbt_oracle",
        "s": ".base",
        "settings": "flext_dbt_oracle",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_dbt_oracle",
    },
    public_exports=__all__,
)
