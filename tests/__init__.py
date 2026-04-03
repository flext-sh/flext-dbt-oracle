# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.decorators import FlextDecorators as d
from flext_core.exceptions import FlextExceptions as e
from flext_core.handlers import FlextHandlers as h
from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_core.mixins import FlextMixins as x
from flext_core.result import FlextResult as r
from flext_core.service import FlextService as s
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
    TestBuildOracleConnectionConfig,
    TestOracleConnectionConfig,
)
from tests.unit.test_impl import TestOracleTableAdapter, TestOracleTableFactory
from tests.unit.test_imports import (
    test_basic_functionality,
    test_flext_dbt_oracle_imports,
)
from tests.utilities import (
    FlextDbtOracleTestUtilities,
    FlextDbtOracleTestUtilities as u,
)

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants

    constants = _tests_constants
    import tests.models as _tests_models

    models = _tests_models
    import tests.protocols as _tests_protocols

    protocols = _tests_protocols
    import tests.typings as _tests_typings

    typings = _tests_typings
    import tests.unit as _tests_unit

    unit = _tests_unit
    import tests.unit.test_basic as _tests_unit_test_basic

    test_basic = _tests_unit_test_basic
    import tests.unit.test_config as _tests_unit_test_config

    test_config = _tests_unit_test_config
    import tests.unit.test_connections as _tests_unit_test_connections

    test_connections = _tests_unit_test_connections
    import tests.unit.test_impl as _tests_unit_test_impl

    test_impl = _tests_unit_test_impl
    import tests.unit.test_imports as _tests_unit_test_imports

    test_imports = _tests_unit_test_imports
    import tests.utilities as _tests_utilities

    utilities = _tests_utilities

    _ = (
        FlextDbtOracleSettings,
        FlextDbtOracleTestConstants,
        FlextDbtOracleTestModels,
        FlextDbtOracleTestProtocols,
        FlextDbtOracleTestTypes,
        FlextDbtOracleTestUtilities,
        MockConnectionManager,
        MockDbtOracleAdapter,
        MockDbtRunner,
        MockModelCompiler,
        MockRelationManager,
        MockSqlExecutor,
        TestBuildOracleConnectionConfig,
        TestConfigConstantsUsage,
        TestConfigEdgeCases,
        TestFlextDbtOracleSettings,
        TestOracleConnectionConfig,
        TestOracleTableAdapter,
        TestOracleTableFactory,
        c,
        conftest,
        constants,
        d,
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
        e,
        h,
        m,
        mock_dbt_oracle_adapter,
        mock_dbt_runner,
        models,
        oracle_adapter_config,
        oracle_shared_container_environment,
        oracle_sql_queries,
        p,
        performance_test_config,
        protocols,
        pytest_configure,
        r,
        s,
        set_test_environment,
        shared_oracle_container,
        t,
        test_adapter_initialization,
        test_adapter_type,
        test_basic,
        test_basic_functionality,
        test_basic_import,
        test_config,
        test_connections,
        test_credentials_class,
        test_flext_dbt_oracle_imports,
        test_impl,
        test_imports,
        typings,
        u,
        unit,
        utilities,
        x,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("tests.unit",),
    {
        "FlextDbtOracleTestConstants": "tests.constants",
        "FlextDbtOracleTestModels": "tests.models",
        "FlextDbtOracleTestProtocols": "tests.protocols",
        "FlextDbtOracleTestTypes": "tests.typings",
        "FlextDbtOracleTestUtilities": "tests.utilities",
        "MockConnectionManager": "tests.conftest",
        "MockDbtOracleAdapter": "tests.conftest",
        "MockDbtRunner": "tests.conftest",
        "MockModelCompiler": "tests.conftest",
        "MockRelationManager": "tests.conftest",
        "MockSqlExecutor": "tests.conftest",
        "c": ("tests.constants", "FlextDbtOracleTestConstants"),
        "conftest": "tests.conftest",
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "dbt_error_scenarios": "tests.conftest",
        "dbt_macro_definitions": "tests.conftest",
        "dbt_model_definitions": "tests.conftest",
        "dbt_oracle_profile": "tests.conftest",
        "dbt_project_config": "tests.conftest",
        "dbt_run_config": "tests.conftest",
        "dbt_source_definitions": "tests.conftest",
        "dbt_test_config": "tests.conftest",
        "dbt_test_definitions": "tests.conftest",
        "docker_control": "tests.conftest",
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("tests.models", "FlextDbtOracleTestModels"),
        "mock_dbt_oracle_adapter": "tests.conftest",
        "mock_dbt_runner": "tests.conftest",
        "models": "tests.models",
        "oracle_adapter_config": "tests.conftest",
        "oracle_shared_container_environment": "tests.conftest",
        "oracle_sql_queries": "tests.conftest",
        "p": ("tests.protocols", "FlextDbtOracleTestProtocols"),
        "performance_test_config": "tests.conftest",
        "protocols": "tests.protocols",
        "pytest_configure": "tests.conftest",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "set_test_environment": "tests.conftest",
        "shared_oracle_container": "tests.conftest",
        "t": ("tests.typings", "FlextDbtOracleTestTypes"),
        "typings": "tests.typings",
        "u": ("tests.utilities", "FlextDbtOracleTestUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)

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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
