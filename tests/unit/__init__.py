# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests.unit import (
        test_basic as test_basic,
        test_config as test_config,
        test_connections as test_connections,
        test_impl as test_impl,
        test_imports as test_imports,
    )
    from tests.unit.test_basic import (
        test_adapter_initialization as test_adapter_initialization,
        test_adapter_type as test_adapter_type,
        test_basic_import as test_basic_import,
        test_credentials_class as test_credentials_class,
    )
    from tests.unit.test_config import (
        FlextDbtOracleSettings as FlextDbtOracleSettings,
        TestConfigConstantsUsage as TestConfigConstantsUsage,
        TestConfigEdgeCases as TestConfigEdgeCases,
        TestFlextDbtOracleSettings as TestFlextDbtOracleSettings,
    )
    from tests.unit.test_connections import (
        OracleConnectionConfig as OracleConnectionConfig,
        TestBuildOracleConnectionConfig as TestBuildOracleConnectionConfig,
        TestOracleConnectionConfig as TestOracleConnectionConfig,
    )
    from tests.unit.test_impl import (
        OracleTableAdapter as OracleTableAdapter,
        OracleTableFactory as OracleTableFactory,
        TestOracleTableAdapter as TestOracleTableAdapter,
        TestOracleTableFactory as TestOracleTableFactory,
    )
    from tests.unit.test_imports import (
        test_basic_functionality as test_basic_functionality,
        test_flext_dbt_oracle_imports as test_flext_dbt_oracle_imports,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtOracleSettings": ["tests.unit.test_config", "FlextDbtOracleSettings"],
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
}

_EXPORTS: Sequence[str] = [
    "FlextDbtOracleSettings",
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
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
