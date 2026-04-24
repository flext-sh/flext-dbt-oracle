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
    from tests.unit.test_config import TestsFlextDbtOracleConfig
    from tests.unit.test_connections import (
        TestBuildOracleConnectionConfig,
        TestOracleConnectionConfig,
    )
    from tests.unit.test_impl import TestsFlextDbtOracleImpl
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
            ".unit.test_config": ("TestsFlextDbtOracleConfig",),
            ".unit.test_connections": (
                "TestBuildOracleConnectionConfig",
                "TestOracleConnectionConfig",
            ),
            ".unit.test_impl": ("TestsFlextDbtOracleImpl",),
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
    "TestBuildOracleConnectionConfig",
    "TestOracleConnectionConfig",
    "TestsFlextDbtOracleConfig",
    "TestsFlextDbtOracleConstants",
    "TestsFlextDbtOracleImpl",
    "TestsFlextDbtOracleModels",
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
