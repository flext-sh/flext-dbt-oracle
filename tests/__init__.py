# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, install_local_packages, td, tf, tk, tm

    from flext_dbt_oracle import config, d, e, h, main, meltano, r, settings, x
    from tests.base import TestsFlextDbtOracleServiceBase, s
    from tests.constants import TestsFlextDbtOracleConstants, c
    from tests.models import TestsFlextDbtOracleModels, m
    from tests.protocols import TestsFlextDbtOracleProtocols, p
    from tests.settings import TestsFlextDbtOracleSettings
    from tests.typings import TestsFlextDbtOracleTypes, t
    from tests.utilities import TestsFlextDbtOracleUtilities, u


__all__: tuple[str, ...] = (
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
    "install_local_packages",
    "m",
    "main",
    "meltano",
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
    MappingProxyType({
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
        "d": "flext_dbt_oracle",
        "e": "flext_dbt_oracle",
        "h": "flext_dbt_oracle",
        "install_local_packages": "flext_tests",
        "m": ".models",
        "main": "flext_dbt_oracle",
        "meltano": "flext_dbt_oracle",
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
    }),
    public_exports=__all__,
)
