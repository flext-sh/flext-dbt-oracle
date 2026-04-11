# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_dbt_oracle.test_basic import (
        test_adapter_initialization,
        test_adapter_type,
        test_basic_import,
        test_credentials_class,
    )
    from flext_dbt_oracle.test_config import (
        FlextDbtOracleSettings,
        TestConfigConstantsUsage,
        TestConfigEdgeCases,
        TestFlextDbtOracleSettings,
    )
    from flext_dbt_oracle.test_connections import (
        TestBuildOracleConnectionConfig,
        TestOracleConnectionConfig,
    )
    from flext_dbt_oracle.test_impl import (
        TestOracleTableAdapter,
        TestOracleTableFactory,
    )
    from flext_dbt_oracle.test_imports import (
        test_basic_functionality,
        test_flext_dbt_oracle_imports,
    )
    from flext_dbt_oracle.test_module_governance import (
        PACKAGE_ROOT,
        test_package_modules_do_not_define_module_level_loggers,
        test_package_modules_do_not_define_top_level_functions,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_basic": (
            "test_adapter_initialization",
            "test_adapter_type",
            "test_basic_import",
            "test_credentials_class",
        ),
        ".test_config": (
            "FlextDbtOracleSettings",
            "TestConfigConstantsUsage",
            "TestConfigEdgeCases",
            "TestFlextDbtOracleSettings",
        ),
        ".test_connections": (
            "TestBuildOracleConnectionConfig",
            "TestOracleConnectionConfig",
        ),
        ".test_impl": (
            "TestOracleTableAdapter",
            "TestOracleTableFactory",
        ),
        ".test_imports": (
            "test_basic_functionality",
            "test_flext_dbt_oracle_imports",
        ),
        ".test_module_governance": (
            "PACKAGE_ROOT",
            "test_package_modules_do_not_define_module_level_loggers",
            "test_package_modules_do_not_define_top_level_functions",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__ = [
    "PACKAGE_ROOT",
    "FlextDbtOracleSettings",
    "TestBuildOracleConnectionConfig",
    "TestConfigConstantsUsage",
    "TestConfigEdgeCases",
    "TestFlextDbtOracleSettings",
    "TestOracleConnectionConfig",
    "TestOracleTableAdapter",
    "TestOracleTableFactory",
    "test_adapter_initialization",
    "test_adapter_type",
    "test_basic_functionality",
    "test_basic_import",
    "test_credentials_class",
    "test_flext_dbt_oracle_imports",
    "test_package_modules_do_not_define_module_level_loggers",
    "test_package_modules_do_not_define_top_level_functions",
]
