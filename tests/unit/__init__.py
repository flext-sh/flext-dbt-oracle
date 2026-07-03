# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if TYPE_CHECKING:
    from flext_dbt_oracle.tests.unit._config_parts.connection import (
        FlextDbtOracleConfigConnectionPart as FlextDbtOracleConfigConnectionPart,
    )
    from flext_dbt_oracle.tests.unit._config_parts.construction import (
        FlextDbtOracleConfigConstructionPart as FlextDbtOracleConfigConstructionPart,
    )
    from flext_dbt_oracle.tests.unit._config_parts.validation import (
        FlextDbtOracleConfigValidationPart as FlextDbtOracleConfigValidationPart,
    )
    from flext_dbt_oracle.tests.unit.test_basic import (
        TestsFlextDbtOracleBasic as TestsFlextDbtOracleBasic,
    )
    from flext_dbt_oracle.tests.unit.test_config import (
        TestsFlextDbtOracleConfig as TestsFlextDbtOracleConfig,
    )
    from flext_dbt_oracle.tests.unit.test_connections import (
        TestsFlextDbtOracleConnections as TestsFlextDbtOracleConnections,
    )
    from flext_dbt_oracle.tests.unit.test_impl import (
        TestsFlextDbtOracleImpl as TestsFlextDbtOracleImpl,
    )
    from flext_dbt_oracle.tests.unit.test_imports import (
        TestsFlextDbtOracleImports as TestsFlextDbtOracleImports,
    )
    from flext_dbt_oracle.tests.unit.test_module_governance import (
        TestsFlextDbtOracleModuleGovernance as TestsFlextDbtOracleModuleGovernance,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("._config_parts",),
    build_lazy_import_map(
        {
            "._config_parts": ("_config_parts",),
            "._config_parts.connection": ("FlextDbtOracleConfigConnectionPart",),
            "._config_parts.construction": ("FlextDbtOracleConfigConstructionPart",),
            "._config_parts.validation": ("FlextDbtOracleConfigValidationPart",),
            ".test_basic": ("TestsFlextDbtOracleBasic",),
            ".test_config": ("TestsFlextDbtOracleConfig",),
            ".test_connections": ("TestsFlextDbtOracleConnections",),
            ".test_impl": ("TestsFlextDbtOracleImpl",),
            ".test_imports": ("TestsFlextDbtOracleImports",),
            ".test_module_governance": ("TestsFlextDbtOracleModuleGovernance",),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
