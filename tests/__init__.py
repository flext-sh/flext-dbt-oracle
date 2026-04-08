# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants
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
        pytest_plugins,
        set_test_environment,
        shared_oracle_container,
    )

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        FlextDbtOracleTestConstants,
        FlextDbtOracleTestConstants as c,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import FlextDbtOracleTestModels, FlextDbtOracleTestModels as m

    protocols = _tests_protocols
    import tests.test_module_governance as _tests_test_module_governance
    from tests.protocols import (
        FlextDbtOracleTestProtocols,
        FlextDbtOracleTestProtocols as p,
    )

    test_module_governance = _tests_test_module_governance
    import tests.typings as _tests_typings
    from tests.test_module_governance import (
        PACKAGE_ROOT,
        test_package_modules_do_not_define_module_level_loggers,
        test_package_modules_do_not_define_top_level_functions,
    )

    typings = _tests_typings
    import tests.unit as _tests_unit
    from tests.typings import FlextDbtOracleTestTypes, FlextDbtOracleTestTypes as t

    unit = _tests_unit
    import tests.utilities as _tests_utilities
    from tests.unit import (
        FlextDbtOracleSettings,
        TestBuildOracleConnectionConfig,
        TestConfigConstantsUsage,
        TestConfigEdgeCases,
        TestFlextDbtOracleSettings,
        TestOracleConnectionConfig,
        TestOracleTableAdapter,
        TestOracleTableFactory,
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
    )

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.utilities import (
        FlextDbtOracleTestUtilities,
        FlextDbtOracleTestUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("tests.unit",),
    {
        "FlextDbtOracleTestConstants": (
            "tests.constants",
            "FlextDbtOracleTestConstants",
        ),
        "FlextDbtOracleTestModels": ("tests.models", "FlextDbtOracleTestModels"),
        "FlextDbtOracleTestProtocols": (
            "tests.protocols",
            "FlextDbtOracleTestProtocols",
        ),
        "FlextDbtOracleTestTypes": ("tests.typings", "FlextDbtOracleTestTypes"),
        "FlextDbtOracleTestUtilities": (
            "tests.utilities",
            "FlextDbtOracleTestUtilities",
        ),
        "MockConnectionManager": ("tests.conftest", "MockConnectionManager"),
        "MockDbtOracleAdapter": ("tests.conftest", "MockDbtOracleAdapter"),
        "MockDbtRunner": ("tests.conftest", "MockDbtRunner"),
        "MockModelCompiler": ("tests.conftest", "MockModelCompiler"),
        "MockRelationManager": ("tests.conftest", "MockRelationManager"),
        "MockSqlExecutor": ("tests.conftest", "MockSqlExecutor"),
        "PACKAGE_ROOT": ("tests.test_module_governance", "PACKAGE_ROOT"),
        "c": ("tests.constants", "FlextDbtOracleTestConstants"),
        "conftest": "tests.conftest",
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
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
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("tests.models", "FlextDbtOracleTestModels"),
        "mock_dbt_oracle_adapter": ("tests.conftest", "mock_dbt_oracle_adapter"),
        "mock_dbt_runner": ("tests.conftest", "mock_dbt_runner"),
        "models": "tests.models",
        "oracle_adapter_config": ("tests.conftest", "oracle_adapter_config"),
        "oracle_shared_container_environment": (
            "tests.conftest",
            "oracle_shared_container_environment",
        ),
        "oracle_sql_queries": ("tests.conftest", "oracle_sql_queries"),
        "p": ("tests.protocols", "FlextDbtOracleTestProtocols"),
        "performance_test_config": ("tests.conftest", "performance_test_config"),
        "protocols": "tests.protocols",
        "pytest_configure": ("tests.conftest", "pytest_configure"),
        "pytest_plugins": ("tests.conftest", "pytest_plugins"),
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "set_test_environment": ("tests.conftest", "set_test_environment"),
        "shared_oracle_container": ("tests.conftest", "shared_oracle_container"),
        "t": ("tests.typings", "FlextDbtOracleTestTypes"),
        "test_module_governance": "tests.test_module_governance",
        "test_package_modules_do_not_define_module_level_loggers": (
            "tests.test_module_governance",
            "test_package_modules_do_not_define_module_level_loggers",
        ),
        "test_package_modules_do_not_define_top_level_functions": (
            "tests.test_module_governance",
            "test_package_modules_do_not_define_top_level_functions",
        ),
        "typings": "tests.typings",
        "u": ("tests.utilities", "FlextDbtOracleTestUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

__all__ = [
    "PACKAGE_ROOT",
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
    "pytest_plugins",
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
    "test_module_governance",
    "test_package_modules_do_not_define_module_level_loggers",
    "test_package_modules_do_not_define_top_level_functions",
    "typings",
    "u",
    "unit",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
