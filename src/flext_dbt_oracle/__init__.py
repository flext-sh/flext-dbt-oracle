# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""FLEXT Enterprise - dbt-oracle adapter component."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_db_oracle import d, e, h, r, s, x

    from flext_dbt_oracle.__version__ import (
        __all__,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_dbt_oracle.adapters import OracleTableAdapter, OracleTableFactory
    from flext_dbt_oracle.client import FlextDbtOracleClient
    from flext_dbt_oracle.connections import build_oracle_connection_config
    from flext_dbt_oracle.constants import (
        FlextDbtOracleConstants,
        FlextDbtOracleConstants as c,
    )
    from flext_dbt_oracle.models import FlextDbtOracleModels, FlextDbtOracleModels as m
    from flext_dbt_oracle.protocols import (
        FlextDbtOracleProtocols,
        FlextDbtOracleProtocols as p,
    )
    from flext_dbt_oracle.services import FlextDbtOracleServices
    from flext_dbt_oracle.settings import FlextDbtOracleSettings, OracleConnectionConfig
    from flext_dbt_oracle.simple_api import FlextDbtOracle
    from flext_dbt_oracle.typings import FlextDbtOracleTypes, FlextDbtOracleTypes as t
    from flext_dbt_oracle.utilities import (
        FlextDbtOracleUtilities,
        FlextDbtOracleUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, tuple[str, str]] = {
    "FlextDbtOracle": ("flext_dbt_oracle.simple_api", "FlextDbtOracle"),
    "FlextDbtOracleClient": ("flext_dbt_oracle.client", "FlextDbtOracleClient"),
    "FlextDbtOracleConstants": (
        "flext_dbt_oracle.constants",
        "FlextDbtOracleConstants",
    ),
    "FlextDbtOracleModels": ("flext_dbt_oracle.models", "FlextDbtOracleModels"),
    "FlextDbtOracleProtocols": (
        "flext_dbt_oracle.protocols",
        "FlextDbtOracleProtocols",
    ),
    "FlextDbtOracleServices": ("flext_dbt_oracle.services", "FlextDbtOracleServices"),
    "FlextDbtOracleSettings": ("flext_dbt_oracle.settings", "FlextDbtOracleSettings"),
    "FlextDbtOracleTypes": ("flext_dbt_oracle.typings", "FlextDbtOracleTypes"),
    "FlextDbtOracleUtilities": (
        "flext_dbt_oracle.utilities",
        "FlextDbtOracleUtilities",
    ),
    "OracleConnectionConfig": ("flext_dbt_oracle.settings", "OracleConnectionConfig"),
    "OracleTableAdapter": ("flext_dbt_oracle.adapters", "OracleTableAdapter"),
    "OracleTableFactory": ("flext_dbt_oracle.adapters", "OracleTableFactory"),
    "__all__": ("flext_dbt_oracle.__version__", "__all__"),
    "__author__": ("flext_dbt_oracle.__version__", "__author__"),
    "__author_email__": ("flext_dbt_oracle.__version__", "__author_email__"),
    "__description__": ("flext_dbt_oracle.__version__", "__description__"),
    "__license__": ("flext_dbt_oracle.__version__", "__license__"),
    "__title__": ("flext_dbt_oracle.__version__", "__title__"),
    "__url__": ("flext_dbt_oracle.__version__", "__url__"),
    "__version__": ("flext_dbt_oracle.__version__", "__version__"),
    "__version_info__": ("flext_dbt_oracle.__version__", "__version_info__"),
    "build_oracle_connection_config": (
        "flext_dbt_oracle.connections",
        "build_oracle_connection_config",
    ),
    "c": ("flext_dbt_oracle.constants", "FlextDbtOracleConstants"),
    "d": ("flext_db_oracle", "d"),
    "e": ("flext_db_oracle", "e"),
    "h": ("flext_db_oracle", "h"),
    "m": ("flext_dbt_oracle.models", "FlextDbtOracleModels"),
    "p": ("flext_dbt_oracle.protocols", "FlextDbtOracleProtocols"),
    "r": ("flext_db_oracle", "r"),
    "s": ("flext_db_oracle", "s"),
    "t": ("flext_dbt_oracle.typings", "FlextDbtOracleTypes"),
    "u": ("flext_dbt_oracle.utilities", "FlextDbtOracleUtilities"),
    "x": ("flext_db_oracle", "x"),
}

__all__ = [
    "FlextDbtOracle",
    "FlextDbtOracleClient",
    "FlextDbtOracleConstants",
    "FlextDbtOracleModels",
    "FlextDbtOracleProtocols",
    "FlextDbtOracleServices",
    "FlextDbtOracleSettings",
    "FlextDbtOracleTypes",
    "FlextDbtOracleUtilities",
    "OracleConnectionConfig",
    "OracleTableAdapter",
    "OracleTableFactory",
    "__all__",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "build_oracle_connection_config",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


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


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
