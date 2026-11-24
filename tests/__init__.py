# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, d, e, h, r, td, tf, tk, tm, x

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
        config,
        main,
        settings,
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
        "api": "flext_tests",
        "c": ".constants",
        "config": "flext_dbt_oracle",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "m": ".models",
        "main": "flext_dbt_oracle",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "settings": "flext_dbt_oracle",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_tests",
    },
    public_exports=__all__,
)
