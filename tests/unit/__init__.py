# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes

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

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextDbtOracleSettings": "tests.unit.test_config",
    "OracleConnectionConfig": "tests.unit.test_connections",
    "OracleTableAdapter": "tests.unit.test_impl",
    "OracleTableFactory": "tests.unit.test_impl",
    "TestBuildOracleConnectionConfig": "tests.unit.test_connections",
    "TestConfigConstantsUsage": "tests.unit.test_config",
    "TestConfigEdgeCases": "tests.unit.test_config",
    "TestFlextDbtOracleSettings": "tests.unit.test_config",
    "TestOracleConnectionConfig": "tests.unit.test_connections",
    "TestOracleTableAdapter": "tests.unit.test_impl",
    "TestOracleTableFactory": "tests.unit.test_impl",
    "test_adapter_initialization": "tests.unit.test_basic",
    "test_adapter_type": "tests.unit.test_basic",
    "test_basic": "tests.unit.test_basic",
    "test_basic_functionality": "tests.unit.test_imports",
    "test_basic_import": "tests.unit.test_basic",
    "test_config": "tests.unit.test_config",
    "test_connections": "tests.unit.test_connections",
    "test_credentials_class": "tests.unit.test_basic",
    "test_flext_dbt_oracle_imports": "tests.unit.test_imports",
    "test_impl": "tests.unit.test_impl",
    "test_imports": "tests.unit.test_imports",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
