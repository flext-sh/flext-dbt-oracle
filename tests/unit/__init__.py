# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import tests.unit.test_basic as _tests_unit_test_basic

    test_basic = _tests_unit_test_basic
    import tests.unit.test_config as _tests_unit_test_config
    from tests.unit.test_basic import (
        test_adapter_initialization,
        test_adapter_type,
        test_basic_import,
        test_credentials_class,
    )

    test_config = _tests_unit_test_config
    import tests.unit.test_connections as _tests_unit_test_connections
    from tests.unit.test_config import (
        FlextDbtOracleSettings,
        TestConfigConstantsUsage,
        TestConfigEdgeCases,
        TestFlextDbtOracleSettings,
    )

    test_connections = _tests_unit_test_connections
    import tests.unit.test_impl as _tests_unit_test_impl
    from tests.unit.test_connections import (
        TestBuildOracleConnectionConfig,
        TestOracleConnectionConfig,
    )

    test_impl = _tests_unit_test_impl
    import tests.unit.test_imports as _tests_unit_test_imports
    from tests.unit.test_impl import TestOracleTableAdapter, TestOracleTableFactory

    test_imports = _tests_unit_test_imports
    from flext_core.constants import FlextConstants as c
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.models import FlextModels as m
    from flext_core.protocols import FlextProtocols as p
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_core.typings import FlextTypes as t
    from flext_core.utilities import FlextUtilities as u
    from tests.unit.test_imports import (
        test_basic_functionality,
        test_flext_dbt_oracle_imports,
    )
_LAZY_IMPORTS = {
    "FlextDbtOracleSettings": "tests.unit.test_config",
    "TestBuildOracleConnectionConfig": "tests.unit.test_connections",
    "TestConfigConstantsUsage": "tests.unit.test_config",
    "TestConfigEdgeCases": "tests.unit.test_config",
    "TestFlextDbtOracleSettings": "tests.unit.test_config",
    "TestOracleConnectionConfig": "tests.unit.test_connections",
    "TestOracleTableAdapter": "tests.unit.test_impl",
    "TestOracleTableFactory": "tests.unit.test_impl",
    "c": ("flext_core.constants", "FlextConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("flext_core.models", "FlextModels"),
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("flext_core.typings", "FlextTypes"),
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
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "FlextDbtOracleSettings",
    "TestBuildOracleConnectionConfig",
    "TestConfigConstantsUsage",
    "TestConfigEdgeCases",
    "TestFlextDbtOracleSettings",
    "TestOracleConnectionConfig",
    "TestOracleTableAdapter",
    "TestOracleTableFactory",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
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
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
