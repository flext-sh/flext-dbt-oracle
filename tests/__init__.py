# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from tests.unit import _LAZY_IMPORTS as _CHILD_LAZY_0

if TYPE_CHECKING:
    from tests.conftest import *
    from tests.constants import *
    from tests.models import *
    from tests.protocols import *
    from tests.typings import *
    from tests.unit import *
    from tests.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    **_CHILD_LAZY_0,
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
    "c": ["tests.constants", "FlextDbtOracleTestConstants"],
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": "flext_db_oracle",
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
    "e": "flext_db_oracle",
    "h": "flext_db_oracle",
    "m": ["tests.models", "FlextDbtOracleTestModels"],
    "mock_dbt_oracle_adapter": "tests.conftest",
    "mock_dbt_runner": "tests.conftest",
    "models": "tests.models",
    "oracle_adapter_config": "tests.conftest",
    "oracle_shared_container_environment": "tests.conftest",
    "oracle_sql_queries": "tests.conftest",
    "p": ["tests.protocols", "FlextDbtOracleTestProtocols"],
    "performance_test_config": "tests.conftest",
    "protocols": "tests.protocols",
    "pytest_configure": "tests.conftest",
    "r": "flext_db_oracle",
    "s": "flext_db_oracle",
    "set_test_environment": "tests.conftest",
    "shared_oracle_container": "tests.conftest",
    "t": ["tests.typings", "FlextDbtOracleTestTypes"],
    "typings": "tests.typings",
    "u": ["tests.utilities", "FlextDbtOracleTestUtilities"],
    "unit": "tests.unit",
    "utilities": "tests.utilities",
    "x": "flext_db_oracle",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
