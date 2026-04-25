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
    from flext_tests import td, tf, tk, tm, tv

    from flext_dbt_oracle import d, e, h, r, s, x
    from tests.conftest import (
        MockConnectionManager,
        MockDbtOracleAdapter,
        MockDbtRunner,
        MockModelCompiler,
        MockRelationManager,
        MockSqlExecutor,
    )
    from tests.constants import TestsFlextDbtOracleConstants, c
    from tests.models import TestsFlextDbtOracleModels, m
    from tests.protocols import TestsFlextDbtOracleProtocols, p
    from tests.typings import TestsFlextDbtOracleTypes, t
    from tests.unit.test_basic import TestsFlextDbtOracleBasic
    from tests.unit.test_config import TestsFlextDbtOracleConfig
    from tests.unit.test_connections import TestsFlextDbtOracleConnections
    from tests.unit.test_impl import TestsFlextDbtOracleImpl
    from tests.unit.test_imports import TestsFlextDbtOracleImports
    from tests.unit.test_module_governance import TestsFlextDbtOracleModuleGovernance
    from tests.utilities import TestsFlextDbtOracleUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".conftest": (
                "MockConnectionManager",
                "MockDbtOracleAdapter",
                "MockDbtRunner",
                "MockModelCompiler",
                "MockRelationManager",
                "MockSqlExecutor",
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
                "s",
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
    "MockConnectionManager",
    "MockDbtOracleAdapter",
    "MockDbtRunner",
    "MockModelCompiler",
    "MockRelationManager",
    "MockSqlExecutor",
    "TestsFlextDbtOracleBasic",
    "TestsFlextDbtOracleConfig",
    "TestsFlextDbtOracleConnections",
    "TestsFlextDbtOracleConstants",
    "TestsFlextDbtOracleImpl",
    "TestsFlextDbtOracleImports",
    "TestsFlextDbtOracleModels",
    "TestsFlextDbtOracleModuleGovernance",
    "TestsFlextDbtOracleProtocols",
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
