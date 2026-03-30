# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_db_oracle import d, e, h, r, s, x

    from tests import conftest, constants, models, protocols, typings, unit, utilities
    from tests.conftest import (
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
    from tests.constants import (
        FlextDbtOracleTestConstants,
        FlextDbtOracleTestConstants as c,
    )
    from tests.models import FlextDbtOracleTestModels, FlextDbtOracleTestModels as m
    from tests.protocols import (
        FlextDbtOracleTestProtocols,
        FlextDbtOracleTestProtocols as p,
    )
    from tests.typings import FlextDbtOracleTestTypes, FlextDbtOracleTestTypes as t
    from tests.unit import (
        test_basic,
        test_config,
        test_connections,
        test_impl,
        test_imports,
    )
    from tests.unit.test_basic import (
        test_adapter_initialization,
        test_adapter_type,
        test_basic_import,
        test_credentials_class,
    )
    from tests.unit.test_config import (
        FlextDbtOracleSettings,
        TestConfigConstantsUsage,
        TestConfigEdgeCases,
        TestFlextDbtOracleSettings,
    )
    from tests.unit.test_connections import (
        OracleConnectionConfig,
        TestBuildOracleConnectionConfig,
        TestOracleConnectionConfig,
    )
    from tests.unit.test_impl import (
        OracleTableAdapter,
        OracleTableFactory,
        TestOracleTableAdapter,
        TestOracleTableFactory,
    )
    from tests.unit.test_imports import (
        test_basic_functionality,
        test_flext_dbt_oracle_imports,
    )
    from tests.utilities import (
        FlextDbtOracleTestUtilities,
        FlextDbtOracleTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtOracleSettings": ["tests.unit.test_config", "FlextDbtOracleSettings"],
    "FlextDbtOracleTestConstants": ["tests.constants", "FlextDbtOracleTestConstants"],
    "FlextDbtOracleTestModels": ["tests.models", "FlextDbtOracleTestModels"],
    "FlextDbtOracleTestProtocols": ["tests.protocols", "FlextDbtOracleTestProtocols"],
    "FlextDbtOracleTestTypes": ["tests.typings", "FlextDbtOracleTestTypes"],
    "FlextDbtOracleTestUtilities": ["tests.utilities", "FlextDbtOracleTestUtilities"],
    "MockConnectionManager": ["tests.conftest", "MockConnectionManager"],
    "MockDbtOracleAdapter": ["tests.conftest", "MockDbtOracleAdapter"],
    "MockDbtRunner": ["tests.conftest", "MockDbtRunner"],
    "MockModelCompiler": ["tests.conftest", "MockModelCompiler"],
    "MockRelationManager": ["tests.conftest", "MockRelationManager"],
    "MockSqlExecutor": ["tests.conftest", "MockSqlExecutor"],
    "OracleConnectionConfig": ["tests.unit.test_connections", "OracleConnectionConfig"],
    "OracleTableAdapter": ["tests.unit.test_impl", "OracleTableAdapter"],
    "OracleTableFactory": ["tests.unit.test_impl", "OracleTableFactory"],
    "TestBuildOracleConnectionConfig": [
        "tests.unit.test_connections",
        "TestBuildOracleConnectionConfig",
    ],
    "TestConfigConstantsUsage": ["tests.unit.test_config", "TestConfigConstantsUsage"],
    "TestConfigEdgeCases": ["tests.unit.test_config", "TestConfigEdgeCases"],
    "TestFlextDbtOracleSettings": [
        "tests.unit.test_config",
        "TestFlextDbtOracleSettings",
    ],
    "TestOracleConnectionConfig": [
        "tests.unit.test_connections",
        "TestOracleConnectionConfig",
    ],
    "TestOracleTableAdapter": ["tests.unit.test_impl", "TestOracleTableAdapter"],
    "TestOracleTableFactory": ["tests.unit.test_impl", "TestOracleTableFactory"],
    "c": ["tests.constants", "FlextDbtOracleTestConstants"],
    "conftest": ["tests.conftest", ""],
    "constants": ["tests.constants", ""],
    "d": ["flext_db_oracle", "d"],
    "dbt_error_scenarios": ["tests.conftest", "dbt_error_scenarios"],
    "dbt_macro_definitions": ["tests.conftest", "dbt_macro_definitions"],
    "dbt_model_definitions": ["tests.conftest", "dbt_model_definitions"],
    "dbt_oracle_profile": ["tests.conftest", "dbt_oracle_profile"],
    "dbt_project_config": ["tests.conftest", "dbt_project_config"],
    "dbt_run_config": ["tests.conftest", "dbt_run_config"],
    "dbt_source_definitions": ["tests.conftest", "dbt_source_definitions"],
    "dbt_test_config": ["tests.conftest", "dbt_test_config"],
    "dbt_test_definitions": ["tests.conftest", "dbt_test_definitions"],
    "docker_control": ["tests.conftest", "docker_control"],
    "e": ["flext_db_oracle", "e"],
    "h": ["flext_db_oracle", "h"],
    "m": ["tests.models", "FlextDbtOracleTestModels"],
    "mock_dbt_oracle_adapter": ["tests.conftest", "mock_dbt_oracle_adapter"],
    "mock_dbt_runner": ["tests.conftest", "mock_dbt_runner"],
    "models": ["tests.models", ""],
    "oracle_adapter_config": ["tests.conftest", "oracle_adapter_config"],
    "oracle_shared_container_environment": [
        "tests.conftest",
        "oracle_shared_container_environment",
    ],
    "oracle_sql_queries": ["tests.conftest", "oracle_sql_queries"],
    "p": ["tests.protocols", "FlextDbtOracleTestProtocols"],
    "performance_test_config": ["tests.conftest", "performance_test_config"],
    "protocols": ["tests.protocols", ""],
    "pytest_configure": ["tests.conftest", "pytest_configure"],
    "r": ["flext_db_oracle", "r"],
    "s": ["flext_db_oracle", "s"],
    "set_test_environment": ["tests.conftest", "set_test_environment"],
    "shared_oracle_container": ["tests.conftest", "shared_oracle_container"],
    "t": ["tests.typings", "FlextDbtOracleTestTypes"],
    "test_adapter_initialization": [
        "tests.unit.test_basic",
        "test_adapter_initialization",
    ],
    "test_adapter_type": ["tests.unit.test_basic", "test_adapter_type"],
    "test_basic": ["tests.unit.test_basic", ""],
    "test_basic_functionality": ["tests.unit.test_imports", "test_basic_functionality"],
    "test_basic_import": ["tests.unit.test_basic", "test_basic_import"],
    "test_config": ["tests.unit.test_config", ""],
    "test_connections": ["tests.unit.test_connections", ""],
    "test_credentials_class": ["tests.unit.test_basic", "test_credentials_class"],
    "test_flext_dbt_oracle_imports": [
        "tests.unit.test_imports",
        "test_flext_dbt_oracle_imports",
    ],
    "test_impl": ["tests.unit.test_impl", ""],
    "test_imports": ["tests.unit.test_imports", ""],
    "typings": ["tests.typings", ""],
    "u": ["tests.utilities", "FlextDbtOracleTestUtilities"],
    "unit": ["tests.unit", ""],
    "utilities": ["tests.utilities", ""],
    "x": ["flext_db_oracle", "x"],
}

__all__ = [
    "FlextDbtOracleSettings",
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
    "OracleConnectionConfig",
    "OracleTableAdapter",
    "OracleTableFactory",
    "TestBuildOracleConnectionConfig",
    "TestConfigConstantsUsage",
    "TestConfigEdgeCases",
    "TestFlextDbtOracleSettings",
    "TestOracleConnectionConfig",
    "TestOracleTableAdapter",
    "TestOracleTableFactory",
    "c",
    "conftest",
    "constants",
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
    "models",
    "oracle_adapter_config",
    "oracle_shared_container_environment",
    "oracle_sql_queries",
    "p",
    "performance_test_config",
    "protocols",
    "pytest_configure",
    "r",
    "s",
    "set_test_environment",
    "shared_oracle_container",
    "t",
    "test_adapter_initialization",
    "test_adapter_type",
    "test_basic",
    "test_basic_functionality",
    "test_basic_import",
    "test_config",
    "test_connections",
    "test_credentials_class",
    "test_flext_dbt_oracle_imports",
    "test_impl",
    "test_imports",
    "typings",
    "u",
    "unit",
    "utilities",
    "x",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


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


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
