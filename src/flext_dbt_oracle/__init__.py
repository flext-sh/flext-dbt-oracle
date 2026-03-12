"""FLEXT Enterprise - dbt-oracle adapter component."""

from __future__ import annotations

from importlib import import_module
from typing import TYPE_CHECKING, Any

from flext_core.lazy import cleanup_submodule_namespace

if TYPE_CHECKING:
    from flext_dbt_oracle.__version__ import __version__, __version_info__
    from flext_dbt_oracle.adapters import OracleTableAdapter, OracleTableFactory
    from flext_dbt_oracle.client import FlextDbtOracleClient
    from flext_dbt_oracle.constants import (
        FlextDbtOracleConstants,
        FlextDbtOracleConstants as c,
    )
    from flext_dbt_oracle.models import FlextDbtOracleModels, FlextDbtOracleModels as m
    from flext_dbt_oracle.protocols import (
        FlextDbtOracleProtocols,
        FlextDbtOracleProtocols as p,
    )
    from flext_dbt_oracle.settings import (
        FlextDbtOracleSettings,
        OracleConnectionConfig,
        build_oracle_connection_config,
    )
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
    "FlextDbtOracleConstants": (
        "flext_dbt_oracle.constants",
        "FlextDbtOracleConstants",
    ),
    "FlextDbtOracleModels": ("flext_dbt_oracle.models", "FlextDbtOracleModels"),
    "FlextDbtOracleProtocols": (
        "flext_dbt_oracle.protocols",
        "FlextDbtOracleProtocols",
    ),
    "FlextDbtOracleSettings": ("flext_dbt_oracle.settings", "FlextDbtOracleSettings"),
    "OracleConnectionConfig": ("flext_dbt_oracle.settings", "OracleConnectionConfig"),
    "build_oracle_connection_config": (
        "flext_dbt_oracle.settings",
        "build_oracle_connection_config",
    ),
    "FlextDbtOracleTypes": ("flext_dbt_oracle.typings", "FlextDbtOracleTypes"),
    "FlextDbtOracleUtilities": (
        "flext_dbt_oracle.utilities",
        "FlextDbtOracleUtilities",
    ),
    "OracleTableAdapter": ("flext_dbt_oracle.adapters", "OracleTableAdapter"),
    "OracleTableFactory": ("flext_dbt_oracle.adapters", "OracleTableFactory"),
    "__version__": ("flext_dbt_oracle.__version__", "__version__"),
    "__version_info__": ("flext_dbt_oracle.__version__", "__version_info__"),
    "c": ("flext_dbt_oracle.constants", "FlextDbtOracleConstants"),
    "m": ("flext_dbt_oracle.models", "FlextDbtOracleModels"),
    "p": ("flext_dbt_oracle.protocols", "FlextDbtOracleProtocols"),
    "t": ("flext_dbt_oracle.typings", "FlextDbtOracleTypes"),
    "u": ("flext_dbt_oracle.utilities", "FlextDbtOracleUtilities"),
}

__all__ = [
    "FlextDbtOracle",
    "FlextDbtOracleClient",
    "FlextDbtOracleConstants",
    "FlextDbtOracleModels",
    "FlextDbtOracleProtocols",
    "FlextDbtOracleSettings",
    "FlextDbtOracleTypes",
    "FlextDbtOracleUtilities",
    "OracleConnectionConfig",
    "OracleTableAdapter",
    "OracleTableFactory",
    "__version__",
    "__version_info__",
    "build_oracle_connection_config",
    "c",
    "m",
    "p",
    "t",
    "u",
]


def __getattr__(
    name: str,
) -> Any:  # JUSTIFIED: Ruff (any-type) with PEP 562 dynamic module exports — https://docs.astral.sh/ruff/rules/any-type/
    """Lazy-load module attributes on first access (PEP 562)."""
    if name not in _LAZY_IMPORTS:
        msg = f"module '{__name__}' has no attribute '{name}'"
        raise AttributeError(msg)
    module_path, attr_name = _LAZY_IMPORTS[name]
    module = import_module(module_path)
    value: Any = module.__dict__[attr_name]
    globals()[name] = value
    return value


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
