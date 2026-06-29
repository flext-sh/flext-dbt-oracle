# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_tests import td as td, tf as tf, tk as tk, tm as tm, tv as tv

    from flext_dbt_oracle import d as d, e as e, h as h, r as r, x as x
    from tests.base import (
        TestsFlextDbtOracleServiceBase as TestsFlextDbtOracleServiceBase,
        s as s,
    )
    from tests.constants import (
        TestsFlextDbtOracleConstants as TestsFlextDbtOracleConstants,
        c as c,
    )
    from tests.models import (
        TestsFlextDbtOracleModels as TestsFlextDbtOracleModels,
        m as m,
    )
    from tests.protocols import (
        TestsFlextDbtOracleProtocols as TestsFlextDbtOracleProtocols,
        p as p,
    )
    from tests.settings import (
        TestsFlextDbtOracleSettings as TestsFlextDbtOracleSettings,
    )
    from tests.typings import (
        TestsFlextDbtOracleTypes as TestsFlextDbtOracleTypes,
        t as t,
    )
    from tests.unit.test_basic import (
        TestsFlextDbtOracleBasic as TestsFlextDbtOracleBasic,
    )
    from tests.unit.test_config import (
        TestsFlextDbtOracleConfig as TestsFlextDbtOracleConfig,
    )
    from tests.unit.test_connections import (
        TestsFlextDbtOracleConnections as TestsFlextDbtOracleConnections,
    )
    from tests.unit.test_impl import TestsFlextDbtOracleImpl as TestsFlextDbtOracleImpl
    from tests.unit.test_imports import (
        TestsFlextDbtOracleImports as TestsFlextDbtOracleImports,
    )
    from tests.unit.test_module_governance import (
        TestsFlextDbtOracleModuleGovernance as TestsFlextDbtOracleModuleGovernance,
    )
    from tests.utilities import (
        TestsFlextDbtOracleUtilities as TestsFlextDbtOracleUtilities,
        u as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".base": (
                "TestsFlextDbtOracleServiceBase",
                "s",
            ),
            ".constants": (
                "TestsFlextDbtOracleConstants",
                "c",
            ),
            ".models": (
                "TestsFlextDbtOracleModels",
                "m",
            ),
            ".protocols": (
                "TestsFlextDbtOracleProtocols",
                "p",
            ),
            ".settings": ("TestsFlextDbtOracleSettings",),
            ".typings": (
                "TestsFlextDbtOracleTypes",
                "t",
            ),
            ".unit.test_basic": ("TestsFlextDbtOracleBasic",),
            ".unit.test_config": ("TestsFlextDbtOracleConfig",),
            ".unit.test_connections": ("TestsFlextDbtOracleConnections",),
            ".unit.test_impl": ("TestsFlextDbtOracleImpl",),
            ".unit.test_imports": ("TestsFlextDbtOracleImports",),
            ".unit.test_module_governance": ("TestsFlextDbtOracleModuleGovernance",),
            ".utilities": (
                "TestsFlextDbtOracleUtilities",
                "u",
            ),
            "flext_dbt_oracle": (
                "d",
                "e",
                "h",
                "r",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "TestsFlextDbtOracleBasic",
    "TestsFlextDbtOracleConfig",
    "TestsFlextDbtOracleConnections",
    "TestsFlextDbtOracleConstants",
    "TestsFlextDbtOracleImpl",
    "TestsFlextDbtOracleImports",
    "TestsFlextDbtOracleModels",
    "TestsFlextDbtOracleModuleGovernance",
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
    "x",
]
