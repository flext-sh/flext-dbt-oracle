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
    from flext_dbt_oracle import (
        test_basic,
        test_config,
        test_connections,
        test_impl,
        test_imports,
    )
    from flext_dbt_oracle.test_basic import (
        test_adapter_initialization,
        test_basic_import,
    )
    from flext_dbt_oracle.test_config import (
        FlextDbtOracleSettings,
        TestFlextDbtOracleSettings,
    )
    from flext_dbt_oracle.test_connections import TestOracleConnectionConfig
    from flext_dbt_oracle.test_impl import TestOracleTableAdapter
    from flext_dbt_oracle.test_imports import (
        test_basic_functionality,
        test_flext_dbt_oracle_imports,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextDbtOracleSettings": "flext_dbt_oracle.test_config",
    "TestFlextDbtOracleSettings": "flext_dbt_oracle.test_config",
    "TestOracleConnectionConfig": "flext_dbt_oracle.test_connections",
    "TestOracleTableAdapter": "flext_dbt_oracle.test_impl",
    "c": ("flext_core.constants", "FlextConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("flext_core.models", "FlextModels"),
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("flext_core.typings", "FlextTypes"),
    "test_adapter_initialization": "flext_dbt_oracle.test_basic",
    "test_basic": "flext_dbt_oracle.test_basic",
    "test_basic_functionality": "flext_dbt_oracle.test_imports",
    "test_basic_import": "flext_dbt_oracle.test_basic",
    "test_config": "flext_dbt_oracle.test_config",
    "test_connections": "flext_dbt_oracle.test_connections",
    "test_flext_dbt_oracle_imports": "flext_dbt_oracle.test_imports",
    "test_impl": "flext_dbt_oracle.test_impl",
    "test_imports": "flext_dbt_oracle.test_imports",
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
