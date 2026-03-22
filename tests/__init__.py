# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tests import d, e, h, r, s, x

    from . import unit as unit
    from .conftest import (
        MockConnectionManager,
        MockDbtOracleAdapter,
        MockDbtRunner,
        MockModelCompiler,
        MockRelationManager,
        MockSqlExecutor,
        dbt_error_scenarios,
        dbt_macro_definitions,
        dbt_model_definitions,
        dbt_oracle_profile,
        dbt_project_config,
        dbt_run_config,
        dbt_source_definitions,
        dbt_test_config,
        dbt_test_definitions,
        docker_control,
        mock_dbt_oracle_adapter,
        mock_dbt_runner,
        oracle_adapter_config,
        oracle_shared_container_environment,
        oracle_sql_queries,
        performance_test_config,
        pytest_configure,
        set_test_environment,
        shared_oracle_container,
    )
    from .constants import FlextDbtOracleTestConstants, FlextDbtOracleTestConstants as c
    from .models import FlextDbtOracleTestModels, FlextDbtOracleTestModels as m
    from .protocols import FlextDbtOracleTestProtocols, FlextDbtOracleTestProtocols as p
    from .typings import FlextDbtOracleTestTypes, FlextDbtOracleTestTypes as t
    from .unit.test_basic import (
        test_adapter_initialization,
        test_adapter_type,
        test_basic_import,
        test_credentials_class,
    )
    from .unit.test_config import (
        TestConfigConstantsUsage,
        TestConfigEdgeCases,
        TestFlextDbtOracleSettings,
    )
    from .unit.test_connections import (
        TestBuildOracleConnectionConfig,
        TestOracleConnectionConfig,
    )
    from .unit.test_impl import TestOracleTableAdapter, TestOracleTableFactory
    from .unit.test_imports import (
        test_basic_functionality,
        test_flext_dbt_oracle_imports,
    )
    from .utilities import FlextDbtOracleTestUtilities, FlextDbtOracleTestUtilities as u

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextDbtOracleTestConstants": ("tests.constants", "FlextDbtOracleTestConstants"),
    "FlextDbtOracleTestModels": ("tests.models", "FlextDbtOracleTestModels"),
    "FlextDbtOracleTestProtocols": ("tests.protocols", "FlextDbtOracleTestProtocols"),
    "FlextDbtOracleTestTypes": ("tests.typings", "FlextDbtOracleTestTypes"),
    "FlextDbtOracleTestUtilities": ("tests.utilities", "FlextDbtOracleTestUtilities"),
    "MockConnectionManager": ("tests.conftest", "MockConnectionManager"),
    "MockDbtOracleAdapter": ("tests.conftest", "MockDbtOracleAdapter"),
    "MockDbtRunner": ("tests.conftest", "MockDbtRunner"),
    "MockModelCompiler": ("tests.conftest", "MockModelCompiler"),
    "MockRelationManager": ("tests.conftest", "MockRelationManager"),
    "MockSqlExecutor": ("tests.conftest", "MockSqlExecutor"),
    "TestBuildOracleConnectionConfig": (
        "tests.unit.test_connections",
        "TestBuildOracleConnectionConfig",
    ),
    "TestConfigConstantsUsage": ("tests.unit.test_config", "TestConfigConstantsUsage"),
    "TestConfigEdgeCases": ("tests.unit.test_config", "TestConfigEdgeCases"),
    "TestFlextDbtOracleSettings": (
        "tests.unit.test_config",
        "TestFlextDbtOracleSettings",
    ),
    "TestOracleConnectionConfig": (
        "tests.unit.test_connections",
        "TestOracleConnectionConfig",
    ),
    "TestOracleTableAdapter": ("tests.unit.test_impl", "TestOracleTableAdapter"),
    "TestOracleTableFactory": ("tests.unit.test_impl", "TestOracleTableFactory"),
    "c": ("tests.constants", "FlextDbtOracleTestConstants"),
    "d": ("flext_tests", "d"),
    "dbt_error_scenarios": ("tests.conftest", "dbt_error_scenarios"),
    "dbt_macro_definitions": ("tests.conftest", "dbt_macro_definitions"),
    "dbt_model_definitions": ("tests.conftest", "dbt_model_definitions"),
    "dbt_oracle_profile": ("tests.conftest", "dbt_oracle_profile"),
    "dbt_project_config": ("tests.conftest", "dbt_project_config"),
    "dbt_run_config": ("tests.conftest", "dbt_run_config"),
    "dbt_source_definitions": ("tests.conftest", "dbt_source_definitions"),
    "dbt_test_config": ("tests.conftest", "dbt_test_config"),
    "dbt_test_definitions": ("tests.conftest", "dbt_test_definitions"),
    "docker_control": ("tests.conftest", "docker_control"),
    "e": ("flext_tests", "e"),
    "h": ("flext_tests", "h"),
    "m": ("tests.models", "FlextDbtOracleTestModels"),
    "mock_dbt_oracle_adapter": ("tests.conftest", "mock_dbt_oracle_adapter"),
    "mock_dbt_runner": ("tests.conftest", "mock_dbt_runner"),
    "oracle_adapter_config": ("tests.conftest", "oracle_adapter_config"),
    "oracle_shared_container_environment": (
        "tests.conftest",
        "oracle_shared_container_environment",
    ),
    "oracle_sql_queries": ("tests.conftest", "oracle_sql_queries"),
    "p": ("tests.protocols", "FlextDbtOracleTestProtocols"),
    "performance_test_config": ("tests.conftest", "performance_test_config"),
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "r": ("flext_tests", "r"),
    "s": ("flext_tests", "s"),
    "set_test_environment": ("tests.conftest", "set_test_environment"),
    "shared_oracle_container": ("tests.conftest", "shared_oracle_container"),
    "t": ("tests.typings", "FlextDbtOracleTestTypes"),
    "test_adapter_initialization": (
        "tests.unit.test_basic",
        "test_adapter_initialization",
    ),
    "test_adapter_type": ("tests.unit.test_basic", "test_adapter_type"),
    "test_basic_functionality": ("tests.unit.test_imports", "test_basic_functionality"),
    "test_basic_import": ("tests.unit.test_basic", "test_basic_import"),
    "test_credentials_class": ("tests.unit.test_basic", "test_credentials_class"),
    "test_flext_dbt_oracle_imports": (
        "tests.unit.test_imports",
        "test_flext_dbt_oracle_imports",
    ),
    "u": ("tests.utilities", "FlextDbtOracleTestUtilities"),
    "unit": ("tests.unit", ""),
    "x": ("flext_tests", "x"),
}

__all__ = [
    "FlextDbtOracleTestConstants",
    "FlextDbtOracleTestModels",
    "FlextDbtOracleTestProtocols",
    "FlextDbtOracleTestTypes",
    "FlextDbtOracleTestUtilities",
    "MockConnectionManager",
    "MockDbtOracleAdapter",
    "MockDbtRunner",
    "MockModelCompiler",
    "MockRelationManager",
    "MockSqlExecutor",
    "TestBuildOracleConnectionConfig",
    "TestConfigConstantsUsage",
    "TestConfigEdgeCases",
    "TestFlextDbtOracleSettings",
    "TestOracleConnectionConfig",
    "TestOracleTableAdapter",
    "TestOracleTableFactory",
    "c",
    "d",
    "dbt_error_scenarios",
    "dbt_macro_definitions",
    "dbt_model_definitions",
    "dbt_oracle_profile",
    "dbt_project_config",
    "dbt_run_config",
    "dbt_source_definitions",
    "dbt_test_config",
    "dbt_test_definitions",
    "docker_control",
    "e",
    "h",
    "m",
    "mock_dbt_oracle_adapter",
    "mock_dbt_runner",
    "oracle_adapter_config",
    "oracle_shared_container_environment",
    "oracle_sql_queries",
    "p",
    "performance_test_config",
    "pytest_configure",
    "r",
    "s",
    "set_test_environment",
    "shared_oracle_container",
    "t",
    "test_adapter_initialization",
    "test_adapter_type",
    "test_basic_functionality",
    "test_basic_import",
    "test_credentials_class",
    "test_flext_dbt_oracle_imports",
    "u",
    "unit",
    "x",
]


_LAZY_CACHE: dict[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
