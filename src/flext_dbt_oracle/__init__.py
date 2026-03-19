# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""FLEXT Enterprise - dbt-oracle adapter component."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes
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
    from flext_dbt_oracle.constants import FlextDbtOracleConstants, c
    from flext_dbt_oracle.models import FlextDbtOracleModels, m
    from flext_dbt_oracle.protocols import FlextDbtOracleProtocols, p
    from flext_dbt_oracle.services import FlextDbtOracleServices
    from flext_dbt_oracle.settings import (
        FlextDbtOracleSettings,
        OracleConnectionConfig,
        build_oracle_connection_config,
    )
    from flext_dbt_oracle.simple_api import FlextDbtOracle
    from flext_dbt_oracle.typings import (
        ColumnSpec,
        FlextDbtOracleTypes,
        OraclePayload,
        OraclePayloadList,
        t,
    )
    from flext_dbt_oracle.utilities import FlextDbtOracleUtilities, u

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "ColumnSpec": ("flext_dbt_oracle.typings", "ColumnSpec"),
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
    "OraclePayload": ("flext_dbt_oracle.typings", "OraclePayload"),
    "OraclePayloadList": ("flext_dbt_oracle.typings", "OraclePayloadList"),
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
        "flext_dbt_oracle.settings",
        "build_oracle_connection_config",
    ),
    "c": ("flext_dbt_oracle.constants", "c"),
    "d": ("flext_db_oracle", "d"),
    "e": ("flext_db_oracle", "e"),
    "h": ("flext_db_oracle", "h"),
    "m": ("flext_dbt_oracle.models", "m"),
    "p": ("flext_dbt_oracle.protocols", "p"),
    "r": ("flext_db_oracle", "r"),
    "s": ("flext_db_oracle", "s"),
    "t": ("flext_dbt_oracle.typings", "t"),
    "u": ("flext_dbt_oracle.utilities", "u"),
    "x": ("flext_db_oracle", "x"),
}

__all__ = [
    "ColumnSpec",
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
    "OraclePayload",
    "OraclePayloadList",
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


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
