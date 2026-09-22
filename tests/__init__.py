# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_cli import cli
    from flext_meltano import meltano
    from flext_tests import (
        active_rules,
        api,
        discover_repository_root,
        install_local_packages,
        load_infra_report,
        split_csv,
        td,
        tf,
        tk,
        tm,
        tv,
    )

    from flext_core import core, d, e, h, lazy_attribute, r, x
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
    "active_rules",
    "api",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "discover_repository_root",
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
    "settings",
    "split_csv",
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
            "flext_cli": ("cli",),
            "flext_core": ("core", "d", "e", "h", "lazy_attribute", "r", "x"),
            "flext_dbt_oracle": ("config", "main", "s", "settings"),
            "flext_meltano": ("meltano",),
            "flext_tests": (
                "active_rules",
                "api",
                "discover_repository_root",
                "install_local_packages",
                "load_infra_report",
                "split_csv",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
