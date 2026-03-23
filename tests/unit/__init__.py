# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes

    from tests.unit.test_basic import (
        test_adapter_initialization,
        test_adapter_type,
        test_basic_import,
        test_credentials_class,
    )
    from tests.unit.test_config import (
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

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "TestBuildOracleConnectionConfig": (
        "tests.unit.test_connections",
        "TestBuildOracleConnectionConfig",
    ),
    "TestConfigConstantsUsage": ("tests.unit.test_config", "TestConfigConstantsUsage"),
    "TestConfigEdgeCases": ("tests.unit.test_config", "TestConfigEdgeCases"),
    "TestFlextDbtOracleSettings": (
        "tests.unit.test_config",
        "TestFlextDbtOracleSettings",
    ),
    "TestOracleConnectionConfig": (
        "tests.unit.test_connections",
        "TestOracleConnectionConfig",
    ),
    "TestOracleTableAdapter": ("tests.unit.test_impl", "TestOracleTableAdapter"),
    "TestOracleTableFactory": ("tests.unit.test_impl", "TestOracleTableFactory"),
    "test_adapter_initialization": (
        "tests.unit.test_basic",
        "test_adapter_initialization",
    ),
    "test_adapter_type": ("tests.unit.test_basic", "test_adapter_type"),
    "test_basic_functionality": ("tests.unit.test_imports", "test_basic_functionality"),
    "test_basic_import": ("tests.unit.test_basic", "test_basic_import"),
    "test_credentials_class": ("tests.unit.test_basic", "test_credentials_class"),
    "test_flext_dbt_oracle_imports": (
        "tests.unit.test_imports",
        "test_flext_dbt_oracle_imports",
    ),
}

__all__ = [
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
]


_LAZY_CACHE: dict[str, FlextTypes.ModuleExport] = {}


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


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
