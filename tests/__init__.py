# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

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
    from .constants import (
        TestsFlextDbtOracleConstants,
        TestsFlextDbtOracleConstants as c,
    )
    from .models import TestsFlextDbtOracleModels, TestsFlextDbtOracleModels as m, tm
    from .protocols import (
        TestsFlextDbtOracleProtocols,
        TestsFlextDbtOracleProtocols as p,
    )
    from .typings import TestsFlextDbtOracleTypes, TestsFlextDbtOracleTypes as t
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
    from .utilities import (
        TestsFlextDbtOracleUtilities,
        TestsFlextDbtOracleUtilities as u,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "MockConnectionManager": ("tests.conftest", "MockConnectionManager"),
    "MockDbtOracleAdapter": ("tests.conftest", "MockDbtOracleAdapter"),
    "MockDbtRunner": ("tests.conftest", "MockDbtRunner"),
    "MockModelCompiler": ("tests.conftest", "MockModelCompiler"),
    "MockRelationManager": ("tests.conftest", "MockRelationManager"),
    "MockSqlExecutor": ("tests.conftest", "MockSqlExecutor"),
    "TestBuildOracleConnectionConfig": ("tests.unit.test_connections", "TestBuildOracleConnectionConfig"),
    "TestConfigConstantsUsage": ("tests.unit.test_config", "TestConfigConstantsUsage"),
    "TestConfigEdgeCases": ("tests.unit.test_config", "TestConfigEdgeCases"),
    "TestFlextDbtOracleSettings": ("tests.unit.test_config", "TestFlextDbtOracleSettings"),
    "TestOracleConnectionConfig": ("tests.unit.test_connections", "TestOracleConnectionConfig"),
    "TestOracleTableAdapter": ("tests.unit.test_impl", "TestOracleTableAdapter"),
    "TestOracleTableFactory": ("tests.unit.test_impl", "TestOracleTableFactory"),
    "TestsFlextDbtOracleConstants": ("tests.constants", "TestsFlextDbtOracleConstants"),
    "TestsFlextDbtOracleModels": ("tests.models", "TestsFlextDbtOracleModels"),
    "TestsFlextDbtOracleProtocols": ("tests.protocols", "TestsFlextDbtOracleProtocols"),
    "TestsFlextDbtOracleTypes": ("tests.typings", "TestsFlextDbtOracleTypes"),
    "TestsFlextDbtOracleUtilities": ("tests.utilities", "TestsFlextDbtOracleUtilities"),
    "c": ("tests.constants", "TestsFlextDbtOracleConstants"),
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
    "m": ("tests.models", "TestsFlextDbtOracleModels"),
    "mock_dbt_oracle_adapter": ("tests.conftest", "mock_dbt_oracle_adapter"),
    "mock_dbt_runner": ("tests.conftest", "mock_dbt_runner"),
    "oracle_adapter_config": ("tests.conftest", "oracle_adapter_config"),
    "oracle_shared_container_environment": ("tests.conftest", "oracle_shared_container_environment"),
    "oracle_sql_queries": ("tests.conftest", "oracle_sql_queries"),
    "p": ("tests.protocols", "TestsFlextDbtOracleProtocols"),
    "performance_test_config": ("tests.conftest", "performance_test_config"),
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "set_test_environment": ("tests.conftest", "set_test_environment"),
    "shared_oracle_container": ("tests.conftest", "shared_oracle_container"),
    "t": ("tests.typings", "TestsFlextDbtOracleTypes"),
    "test_adapter_initialization": ("tests.unit.test_basic", "test_adapter_initialization"),
    "test_adapter_type": ("tests.unit.test_basic", "test_adapter_type"),
    "test_basic_functionality": ("tests.unit.test_imports", "test_basic_functionality"),
    "test_basic_import": ("tests.unit.test_basic", "test_basic_import"),
    "test_credentials_class": ("tests.unit.test_basic", "test_credentials_class"),
    "test_flext_dbt_oracle_imports": ("tests.unit.test_imports", "test_flext_dbt_oracle_imports"),
    "tm": ("tests.models", "tm"),
    "u": ("tests.utilities", "TestsFlextDbtOracleUtilities"),
    "unit": ("tests.unit", ""),
}

__all__ = [
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
    "TestsFlextDbtOracleConstants",
    "TestsFlextDbtOracleModels",
    "TestsFlextDbtOracleProtocols",
    "TestsFlextDbtOracleTypes",
    "TestsFlextDbtOracleUtilities",
    "c",
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
    "m",
    "mock_dbt_oracle_adapter",
    "mock_dbt_runner",
    "oracle_adapter_config",
    "oracle_shared_container_environment",
    "oracle_sql_queries",
    "p",
    "performance_test_config",
    "pytest_configure",
    "set_test_environment",
    "shared_oracle_container",
    "t",
    "test_adapter_initialization",
    "test_adapter_type",
    "test_basic_functionality",
    "test_basic_import",
    "test_credentials_class",
    "test_flext_dbt_oracle_imports",
    "tm",
    "u",
    "unit",
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
