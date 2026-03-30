# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Enterprise - dbt-oracle adapter component."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_dbt_oracle.__version__ import (
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__ as __version__,
    __version_info__ as __version_info__,
)

if TYPE_CHECKING:
    from flext_dbt_oracle import (
        _utilities as _utilities,
        adapters as adapters,
        connections as connections,
        constants as constants,
        models as models,
        protocols as protocols,
        settings as settings,
        simple_api as simple_api,
        typings as typings,
        utilities as utilities,
    )
    from flext_dbt_oracle._utilities.connections import (
        FlextDbtOracleConnections as FlextDbtOracleConnections,
        build_oracle_connection_config as build_oracle_connection_config,
    )
    from flext_dbt_oracle._utilities.simple_api import FlextDbtOracle as FlextDbtOracle
    from flext_dbt_oracle.constants import (
        FlextDbtOracleConstants as FlextDbtOracleConstants,
        FlextDbtOracleConstants as c,
    )
    from flext_dbt_oracle.models import (
        FlextDbtOracleModels as FlextDbtOracleModels,
        FlextDbtOracleModels as m,
    )
    from flext_dbt_oracle.protocols import (
        FlextDbtOracleProtocols as FlextDbtOracleProtocols,
        FlextDbtOracleProtocols as p,
    )
    from flext_dbt_oracle.typings import (
        FlextDbtOracleTypes as FlextDbtOracleTypes,
        FlextDbtOracleTypes as t,
    )
    from flext_dbt_oracle.utilities import (
        FlextDbtOracleUtilities as FlextDbtOracleUtilities,
        FlextDbtOracleUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtOracle": ["flext_dbt_oracle._utilities.simple_api", "FlextDbtOracle"],
    "FlextDbtOracleConnections": [
        "flext_dbt_oracle._utilities.connections",
        "FlextDbtOracleConnections",
    ],
    "FlextDbtOracleConstants": [
        "flext_dbt_oracle.constants",
        "FlextDbtOracleConstants",
    ],
    "FlextDbtOracleModels": ["flext_dbt_oracle.models", "FlextDbtOracleModels"],
    "FlextDbtOracleProtocols": [
        "flext_dbt_oracle.protocols",
        "FlextDbtOracleProtocols",
    ],
    "FlextDbtOracleTypes": ["flext_dbt_oracle.typings", "FlextDbtOracleTypes"],
    "FlextDbtOracleUtilities": [
        "flext_dbt_oracle.utilities",
        "FlextDbtOracleUtilities",
    ],
    "_utilities": ["flext_dbt_oracle._utilities", ""],
    "adapters": ["flext_dbt_oracle.adapters", ""],
    "build_oracle_connection_config": [
        "flext_dbt_oracle._utilities.connections",
        "build_oracle_connection_config",
    ],
    "c": ["flext_dbt_oracle.constants", "FlextDbtOracleConstants"],
    "connections": ["flext_dbt_oracle.connections", ""],
    "constants": ["flext_dbt_oracle.constants", ""],
    "d": ["flext_db_oracle", "d"],
    "e": ["flext_db_oracle", "e"],
    "h": ["flext_db_oracle", "h"],
    "m": ["flext_dbt_oracle.models", "FlextDbtOracleModels"],
    "models": ["flext_dbt_oracle.models", ""],
    "p": ["flext_dbt_oracle.protocols", "FlextDbtOracleProtocols"],
    "protocols": ["flext_dbt_oracle.protocols", ""],
    "r": ["flext_db_oracle", "r"],
    "s": ["flext_db_oracle", "s"],
    "settings": ["flext_dbt_oracle.settings", ""],
    "simple_api": ["flext_dbt_oracle.simple_api", ""],
    "t": ["flext_dbt_oracle.typings", "FlextDbtOracleTypes"],
    "typings": ["flext_dbt_oracle.typings", ""],
    "u": ["flext_dbt_oracle.utilities", "FlextDbtOracleUtilities"],
    "utilities": ["flext_dbt_oracle.utilities", ""],
    "x": ["flext_db_oracle", "x"],
}

_EXPORTS: Sequence[str] = [
    "FlextDbtOracle",
    "FlextDbtOracleConnections",
    "FlextDbtOracleConstants",
    "FlextDbtOracleModels",
    "FlextDbtOracleProtocols",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
