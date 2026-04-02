# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Enterprise - dbt-oracle adapter component."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_dbt_oracle.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_db_oracle.exceptions import FlextDbOracleExceptions as e
    from flext_dbt_oracle import (
        _utilities,
        adapters,
        base,
        connections,
        constants,
        models,
        protocols,
        settings,
        simple_api,
        typings,
        utilities,
    )
    from flext_dbt_oracle._utilities import (
        FlextDbtOracle,
        FlextDbtOracleConnections,
        build_oracle_connection_config,
    )
    from flext_dbt_oracle.base import FlextDbtOracleServiceBase
    from flext_dbt_oracle.constants import (
        FlextDbtOracleConstants,
        FlextDbtOracleConstants as c,
    )
    from flext_dbt_oracle.models import FlextDbtOracleModels, FlextDbtOracleModels as m
    from flext_dbt_oracle.protocols import (
        FlextDbtOracleProtocols,
        FlextDbtOracleProtocols as p,
    )
    from flext_dbt_oracle.typings import FlextDbtOracleTypes, FlextDbtOracleTypes as t
    from flext_dbt_oracle.utilities import (
        FlextDbtOracleUtilities,
        FlextDbtOracleUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    ("flext_dbt_oracle._utilities",),
    {
        "FlextDbtOracleConstants": "flext_dbt_oracle.constants",
        "FlextDbtOracleModels": "flext_dbt_oracle.models",
        "FlextDbtOracleProtocols": "flext_dbt_oracle.protocols",
        "FlextDbtOracleServiceBase": "flext_dbt_oracle.base",
        "FlextDbtOracleTypes": "flext_dbt_oracle.typings",
        "FlextDbtOracleUtilities": "flext_dbt_oracle.utilities",
        "_utilities": "flext_dbt_oracle._utilities",
        "adapters": "flext_dbt_oracle.adapters",
        "base": "flext_dbt_oracle.base",
        "c": ("flext_dbt_oracle.constants", "FlextDbtOracleConstants"),
        "connections": "flext_dbt_oracle.connections",
        "constants": "flext_dbt_oracle.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_db_oracle.exceptions", "FlextDbOracleExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_dbt_oracle.models", "FlextDbtOracleModels"),
        "models": "flext_dbt_oracle.models",
        "p": ("flext_dbt_oracle.protocols", "FlextDbtOracleProtocols"),
        "protocols": "flext_dbt_oracle.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "settings": "flext_dbt_oracle.settings",
        "simple_api": "flext_dbt_oracle.simple_api",
        "t": ("flext_dbt_oracle.typings", "FlextDbtOracleTypes"),
        "typings": "flext_dbt_oracle.typings",
        "u": ("flext_dbt_oracle.utilities", "FlextDbtOracleUtilities"),
        "utilities": "flext_dbt_oracle.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)
