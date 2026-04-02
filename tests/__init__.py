# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
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
    from tests.utilities import (
        FlextDbtOracleTestUtilities,
        FlextDbtOracleTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
