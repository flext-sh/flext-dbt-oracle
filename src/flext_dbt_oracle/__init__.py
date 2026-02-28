"""FLEXT Enterprise - dbt-oracle adapter component."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_dbt_oracle.__version__ import __version__, __version_info__
    from flext_dbt_oracle.adapters import OracleTableAdapter, OracleTableFactory
    from flext_dbt_oracle.client import FlextDbtOracleClient
    from flext_dbt_oracle.constants import c
    from flext_dbt_oracle.models import FlextDbtOracleModels, FlextDbtOracleModels as m
    from flext_dbt_oracle.protocols import FlextDbtOracleProtocols
    from flext_dbt_oracle.services import FlextDbtOracleServices
    from flext_dbt_oracle.settings import FlextDbtOracleSettings
    from flext_dbt_oracle.simple_api import FlextDbtOracle
    from flext_dbt_oracle.typings import FlextDbtOracleTypes, FlextDbtOracleTypes as t
    from flext_dbt_oracle.utilities import (
        FlextDbtOracleUtilities,
        FlextDbtOracleUtilities as u,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextDbtOracle": ("flext_dbt_oracle.simple_api", "FlextDbtOracle"),
    "FlextDbtOracleClient": ("flext_dbt_oracle.client", "FlextDbtOracleClient"),
    "FlextDbtOracleModels": ("flext_dbt_oracle.models", "FlextDbtOracleModels"),
    "FlextDbtOracleProtocols": (
        "flext_dbt_oracle.protocols",
        "FlextDbtOracleProtocols",
    ),
    "FlextDbtOracleSettings": ("flext_dbt_oracle.settings", "FlextDbtOracleSettings"),
    "FlextDbtOracleTypes": ("flext_dbt_oracle.typings", "FlextDbtOracleTypes"),
    "u": ("flext_dbt_oracle.utilities", "FlextDbtOracleUtilities"),
    "OracleTableAdapter": ("flext_dbt_oracle.adapters", "OracleTableAdapter"),
    "OracleTableFactory": ("flext_dbt_oracle.adapters", "OracleTableFactory"),
    "__version__": ("flext_dbt_oracle.__version__", "__version__"),
    "__version_info__": ("flext_dbt_oracle.__version__", "__version_info__"),
    "c": ("flext_dbt_oracle.constants", "c"),
    "m": ("flext_dbt_oracle.models", "FlextDbtOracleModels"),
    "t": ("flext_dbt_oracle.typings", "FlextDbtOracleTypes"),
}

__all__ = [
    "FlextDbtOracle",
    "FlextDbtOracleClient",
    "FlextDbtOracleModels",
    "FlextDbtOracleProtocols",
    "FlextDbtOracleServices",
    "FlextDbtOracleSettings",
    "FlextDbtOracleTypes",
    "FlextDbtOracleUtilities",
    "OracleTableAdapter",
    "OracleTableFactory",
    "__version__",
    "__version_info__",
    "c",
    "m",
    "t",
    "u",
]


def __getattr__(name: str) -> Any:  # noqa: ANN401
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
