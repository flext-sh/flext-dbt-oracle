# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_meltano import meltano
    from flext_tests import (
        api,
        cli,
        core,
        d,
        e,
        h,
        install_local_packages,
        lazy_attribute,
        load_infra_report,
        r,
        services,
        td,
        tf,
        tk,
        tm,
        tv,
        x,
    )

    from flext_dbt_oracle import config, main, s, settings

    from . import unit
    from .base import TestsFlextDbtOracleServiceBase
    from .constants import TestsFlextDbtOracleConstants, c
    from .models import TestsFlextDbtOracleModels, m
    from .protocols import TestsFlextDbtOracleProtocols, p
    from .settings import TestsFlextDbtOracleSettings
    from .typings import TestsFlextDbtOracleTypes, t
    from .utilities import TestsFlextDbtOracleUtilities, u


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
    "cli",
    "config",
    "core",
    "d",
    "e",
    "h",
    "install_local_packages",
    "lazy_attribute",
    "load_infra_report",
    "m",
    "main",
    "meltano",
    "p",
    "r",
    "s",
    "services",
    "settings",
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
            ".base": ("TestsFlextDbtOracleServiceBase",),
            ".constants": ("TestsFlextDbtOracleConstants", "c"),
            ".models": ("TestsFlextDbtOracleModels", "m"),
            ".protocols": ("TestsFlextDbtOracleProtocols", "p"),
            ".settings": ("TestsFlextDbtOracleSettings",),
            ".typings": ("TestsFlextDbtOracleTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextDbtOracleUtilities", "u"),
            "flext_dbt_oracle": ("config", "main", "s", "settings"),
            "flext_meltano": ("meltano",),
            "flext_tests": (
                "api",
                "cli",
                "core",
                "d",
                "e",
                "h",
                "install_local_packages",
                "lazy_attribute",
                "load_infra_report",
                "r",
                "services",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
