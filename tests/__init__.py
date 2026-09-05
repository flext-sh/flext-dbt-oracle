# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from . import unit as unit
    from flext_dbt_oracle import FlextDbtOracleConstants
    from flext_tests import FlextTestsConstants, d, e, h, r, td, tf, tk, tm, tv, x
    from typing import Final

    from .base import (
        TestsFlextDbtOracleServiceBase,
        TestsFlextDbtOracleServiceBase as s,
    )
    from .constants import (
        TestsFlextDbtOracleConstants,
        TestsFlextDbtOracleConstants as c,
    )
    from .models import TestsFlextDbtOracleModels, TestsFlextDbtOracleModels as m
    from .protocols import (
        TestsFlextDbtOracleProtocols,
        TestsFlextDbtOracleProtocols as p,
    )
    from .settings import TestsFlextDbtOracleSettings
    from .typings import TestsFlextDbtOracleTypes, TestsFlextDbtOracleTypes as t
    from .utilities import (
        TestsFlextDbtOracleUtilities,
        TestsFlextDbtOracleUtilities as u,
    )
__all__: tuple[str, ...] = (
    "Final",
    "FlextDbtOracleConstants",
    "FlextTestsConstants",
    "TestsFlextDbtOracleConstants",
    "TestsFlextDbtOracleModels",
    "TestsFlextDbtOracleProtocols",
    "TestsFlextDbtOracleServiceBase",
    "TestsFlextDbtOracleSettings",
    "TestsFlextDbtOracleTypes",
    "TestsFlextDbtOracleUtilities",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "unit",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextDbtOracleServiceBase", "s"),
            ".constants": ("TestsFlextDbtOracleConstants", "c"),
            ".models": ("TestsFlextDbtOracleModels", "m"),
            ".protocols": ("TestsFlextDbtOracleProtocols", "p"),
            ".settings": ("TestsFlextDbtOracleSettings",),
            ".typings": ("TestsFlextDbtOracleTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextDbtOracleUtilities", "u"),
            "flext_dbt_oracle": ("FlextDbtOracleConstants",),
            "flext_tests": (
                "FlextTestsConstants",
                "d",
                "e",
                "h",
                "r",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
            "typing": ("Final",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
