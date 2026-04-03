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
    from flext_dbt_oracle import (
        conftest,
        constants,
        models,
        protocols,
        test_basic,
        test_config,
        test_connections,
        test_impl,
        test_imports,
        typings,
        unit,
        utilities,
    )
    from flext_dbt_oracle.conftest import (
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
        set_test_environment,
    )
    from flext_dbt_oracle.constants import (
        FlextDbtOracleTestConstants,
        FlextDbtOracleTestConstants as c,
    )
    from flext_dbt_oracle.models import (
        FlextDbtOracleTestModels,
        FlextDbtOracleTestModels as m,
        Tests,
    )
    from flext_dbt_oracle.protocols import (
        FlextDbtOracleTestProtocols,
        FlextDbtOracleTestProtocols as p,
    )
    from flext_dbt_oracle.typings import (
        FlextDbtOracleTestTypes,
        FlextDbtOracleTestTypes as t,
    )
    from flext_dbt_oracle.unit import (
        FlextDbtOracleSettings,
        TestFlextDbtOracleSettings,
        TestOracleConnectionConfig,
        TestOracleTableAdapter,
        test_adapter_initialization,
        test_basic_functionality,
        test_basic_import,
        test_flext_dbt_oracle_imports,
    )
    from flext_dbt_oracle.utilities import (
        FlextDbtOracleTestUtilities,
        FlextDbtOracleTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    ("flext_dbt_oracle.unit",),
    {
        "FlextDbtOracleTestConstants": "flext_dbt_oracle.constants",
        "FlextDbtOracleTestModels": "flext_dbt_oracle.models",
        "FlextDbtOracleTestProtocols": "flext_dbt_oracle.protocols",
        "FlextDbtOracleTestTypes": "flext_dbt_oracle.typings",
        "FlextDbtOracleTestUtilities": "flext_dbt_oracle.utilities",
        "Tests": "flext_dbt_oracle.models",
        "c": ("flext_dbt_oracle.constants", "FlextDbtOracleTestConstants"),
        "conftest": "flext_dbt_oracle.conftest",
        "constants": "flext_dbt_oracle.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "dbt_error_scenarios": "flext_dbt_oracle.conftest",
        "dbt_macro_definitions": "flext_dbt_oracle.conftest",
        "dbt_model_definitions": "flext_dbt_oracle.conftest",
        "dbt_oracle_profile": "flext_dbt_oracle.conftest",
        "dbt_project_config": "flext_dbt_oracle.conftest",
        "dbt_run_config": "flext_dbt_oracle.conftest",
        "dbt_source_definitions": "flext_dbt_oracle.conftest",
        "dbt_test_config": "flext_dbt_oracle.conftest",
        "dbt_test_definitions": "flext_dbt_oracle.conftest",
        "docker_control": "flext_dbt_oracle.conftest",
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_dbt_oracle.models", "FlextDbtOracleTestModels"),
        "mock_dbt_oracle_adapter": "flext_dbt_oracle.conftest",
        "mock_dbt_runner": "flext_dbt_oracle.conftest",
        "models": "flext_dbt_oracle.models",
        "oracle_adapter_config": "flext_dbt_oracle.conftest",
        "oracle_shared_container_environment": "flext_dbt_oracle.conftest",
        "oracle_sql_queries": "flext_dbt_oracle.conftest",
        "p": ("flext_dbt_oracle.protocols", "FlextDbtOracleTestProtocols"),
        "performance_test_config": "flext_dbt_oracle.conftest",
        "protocols": "flext_dbt_oracle.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "set_test_environment": "flext_dbt_oracle.conftest",
        "t": ("flext_dbt_oracle.typings", "FlextDbtOracleTestTypes"),
        "test_basic": "flext_dbt_oracle.test_basic",
        "test_config": "flext_dbt_oracle.test_config",
        "test_connections": "flext_dbt_oracle.test_connections",
        "test_impl": "flext_dbt_oracle.test_impl",
        "test_imports": "flext_dbt_oracle.test_imports",
        "typings": "flext_dbt_oracle.typings",
        "u": ("flext_dbt_oracle.utilities", "FlextDbtOracleTestUtilities"),
        "unit": "flext_dbt_oracle.unit",
        "utilities": "flext_dbt_oracle.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
