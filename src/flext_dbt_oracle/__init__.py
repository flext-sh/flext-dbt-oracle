# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Enterprise - dbt-oracle adapter component."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

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

if TYPE_CHECKING:
    from flext_db_oracle import *

    from flext_dbt_oracle import (
        _utilities,
        adapters,
        connections,
        constants,
        models,
        protocols,
        settings,
        simple_api,
        typings,
        utilities,
    )
    from flext_dbt_oracle._utilities.connections import *
    from flext_dbt_oracle._utilities.simple_api import *
    from flext_dbt_oracle.constants import *
    from flext_dbt_oracle.models import *
    from flext_dbt_oracle.protocols import *
    from flext_dbt_oracle.typings import *
    from flext_dbt_oracle.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextDbtOracle": "flext_dbt_oracle._utilities.simple_api",
    "FlextDbtOracleConnections": "flext_dbt_oracle._utilities.connections",
    "FlextDbtOracleConstants": "flext_dbt_oracle.constants",
    "FlextDbtOracleModels": "flext_dbt_oracle.models",
    "FlextDbtOracleProtocols": "flext_dbt_oracle.protocols",
    "FlextDbtOracleTypes": "flext_dbt_oracle.typings",
    "FlextDbtOracleUtilities": "flext_dbt_oracle.utilities",
    "_utilities": "flext_dbt_oracle._utilities",
    "adapters": "flext_dbt_oracle.adapters",
    "build_oracle_connection_config": "flext_dbt_oracle._utilities.connections",
    "c": ["flext_dbt_oracle.constants", "FlextDbtOracleConstants"],
    "connections": "flext_dbt_oracle.connections",
    "constants": "flext_dbt_oracle.constants",
    "d": "flext_db_oracle",
    "e": "flext_db_oracle",
    "h": "flext_db_oracle",
    "m": ["flext_dbt_oracle.models", "FlextDbtOracleModels"],
    "models": "flext_dbt_oracle.models",
    "p": ["flext_dbt_oracle.protocols", "FlextDbtOracleProtocols"],
    "protocols": "flext_dbt_oracle.protocols",
    "r": "flext_db_oracle",
    "s": "flext_db_oracle",
    "settings": "flext_dbt_oracle.settings",
    "simple_api": "flext_dbt_oracle.simple_api",
    "t": ["flext_dbt_oracle.typings", "FlextDbtOracleTypes"],
    "typings": "flext_dbt_oracle.typings",
    "u": ["flext_dbt_oracle.utilities", "FlextDbtOracleUtilities"],
    "utilities": "flext_dbt_oracle.utilities",
    "x": "flext_db_oracle",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
