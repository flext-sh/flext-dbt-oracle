# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext dbt oracle package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_dbt_oracle.__version__ import *

if _t.TYPE_CHECKING:
    import flext_dbt_oracle._utilities as _flext_dbt_oracle__utilities

    _utilities = _flext_dbt_oracle__utilities
    import flext_dbt_oracle.adapters as _flext_dbt_oracle_adapters
    from flext_dbt_oracle._utilities import (
        FlextDbtOracle,
        FlextDbtOracleConnections,
        build_oracle_connection_config,
    )

    adapters = _flext_dbt_oracle_adapters
    import flext_dbt_oracle.base as _flext_dbt_oracle_base

    base = _flext_dbt_oracle_base
    import flext_dbt_oracle.connections as _flext_dbt_oracle_connections
    from flext_dbt_oracle.base import (
        FlextDbtOracleServiceBase,
        FlextDbtOracleServiceBase as s,
    )

    connections = _flext_dbt_oracle_connections
    import flext_dbt_oracle.constants as _flext_dbt_oracle_constants

    constants = _flext_dbt_oracle_constants
    import flext_dbt_oracle.models as _flext_dbt_oracle_models
    from flext_dbt_oracle.constants import (
        FlextDbtOracleConstants,
        FlextDbtOracleConstants as c,
    )

    models = _flext_dbt_oracle_models
    import flext_dbt_oracle.protocols as _flext_dbt_oracle_protocols
    from flext_dbt_oracle.models import FlextDbtOracleModels, FlextDbtOracleModels as m

    protocols = _flext_dbt_oracle_protocols
    import flext_dbt_oracle.settings as _flext_dbt_oracle_settings
    from flext_dbt_oracle.protocols import (
        FlextDbtOracleProtocols,
        FlextDbtOracleProtocols as p,
    )

    settings = _flext_dbt_oracle_settings
    import flext_dbt_oracle.simple_api as _flext_dbt_oracle_simple_api

    simple_api = _flext_dbt_oracle_simple_api
    import flext_dbt_oracle.typings as _flext_dbt_oracle_typings

    typings = _flext_dbt_oracle_typings
    import flext_dbt_oracle.utilities as _flext_dbt_oracle_utilities
    from flext_dbt_oracle.typings import FlextDbtOracleTypes, FlextDbtOracleTypes as t

    utilities = _flext_dbt_oracle_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_dbt_oracle.utilities import (
        FlextDbtOracleUtilities,
        FlextDbtOracleUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("flext_dbt_oracle._utilities",),
    {
        "FlextDbtOracleConstants": "flext_dbt_oracle.constants",
        "FlextDbtOracleModels": "flext_dbt_oracle.models",
        "FlextDbtOracleProtocols": "flext_dbt_oracle.protocols",
        "FlextDbtOracleServiceBase": "flext_dbt_oracle.base",
        "FlextDbtOracleTypes": "flext_dbt_oracle.typings",
        "FlextDbtOracleUtilities": "flext_dbt_oracle.utilities",
        "__author__": "flext_dbt_oracle.__version__",
        "__author_email__": "flext_dbt_oracle.__version__",
        "__description__": "flext_dbt_oracle.__version__",
        "__license__": "flext_dbt_oracle.__version__",
        "__title__": "flext_dbt_oracle.__version__",
        "__url__": "flext_dbt_oracle.__version__",
        "__version__": "flext_dbt_oracle.__version__",
        "__version_info__": "flext_dbt_oracle.__version__",
        "_utilities": "flext_dbt_oracle._utilities",
        "adapters": "flext_dbt_oracle.adapters",
        "base": "flext_dbt_oracle.base",
        "c": ("flext_dbt_oracle.constants", "FlextDbtOracleConstants"),
        "connections": "flext_dbt_oracle.connections",
        "constants": "flext_dbt_oracle.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_dbt_oracle.models", "FlextDbtOracleModels"),
        "models": "flext_dbt_oracle.models",
        "p": ("flext_dbt_oracle.protocols", "FlextDbtOracleProtocols"),
        "protocols": "flext_dbt_oracle.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_dbt_oracle.base", "FlextDbtOracleServiceBase"),
        "settings": "flext_dbt_oracle.settings",
        "simple_api": "flext_dbt_oracle.simple_api",
        "t": ("flext_dbt_oracle.typings", "FlextDbtOracleTypes"),
        "typings": "flext_dbt_oracle.typings",
        "u": ("flext_dbt_oracle.utilities", "FlextDbtOracleUtilities"),
        "utilities": "flext_dbt_oracle.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)

__all__ = [
    "FlextDbtOracle",
    "FlextDbtOracleConnections",
    "FlextDbtOracleConstants",
    "FlextDbtOracleModels",
    "FlextDbtOracleProtocols",
    "FlextDbtOracleServiceBase",
    "FlextDbtOracleTypes",
    "FlextDbtOracleUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "_utilities",
    "adapters",
    "base",
    "build_oracle_connection_config",
    "c",
    "connections",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "settings",
    "simple_api",
    "t",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
