# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests.unit package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import c, d, e, h, m, p, r, s, t, td, tf, tk, tm, tv, u, x

    from . import _config_parts as _config_parts
    from .test_basic import TestsFlextDbtOracleBasic
    from .test_config import TestsFlextDbtOracleConfig
    from .test_impl import TestsFlextDbtOracleImpl
    from .test_imports import TestsFlextDbtOracleImports
    from .test_module_governance import TestsFlextDbtOracleModuleGovernance
__all__: tuple[str, ...] = (
    "TestsFlextDbtOracleBasic",
    "TestsFlextDbtOracleConfig",
    "TestsFlextDbtOracleImpl",
    "TestsFlextDbtOracleImports",
    "TestsFlextDbtOracleModuleGovernance",
    "_config_parts",
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
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config_parts": ("_config_parts",),
            ".test_basic": ("TestsFlextDbtOracleBasic",),
            ".test_config": ("TestsFlextDbtOracleConfig",),
            ".test_impl": ("TestsFlextDbtOracleImpl",),
            ".test_imports": ("TestsFlextDbtOracleImports",),
            ".test_module_governance": ("TestsFlextDbtOracleModuleGovernance",),
            "flext_tests": (
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
                "x",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
