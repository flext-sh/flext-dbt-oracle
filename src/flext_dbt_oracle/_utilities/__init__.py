# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import flext_dbt_oracle._utilities.connections as _flext_dbt_oracle__utilities_connections

    connections = _flext_dbt_oracle__utilities_connections
    import flext_dbt_oracle._utilities.simple_api as _flext_dbt_oracle__utilities_simple_api
    from flext_dbt_oracle._utilities.connections import FlextDbtOracleConnections

    simple_api = _flext_dbt_oracle__utilities_simple_api
    from flext_dbt_oracle._utilities.simple_api import FlextDbtOracle
_LAZY_IMPORTS = {
    "FlextDbtOracle": ("flext_dbt_oracle._utilities.simple_api", "FlextDbtOracle"),
    "FlextDbtOracleConnections": (
        "flext_dbt_oracle._utilities.connections",
        "FlextDbtOracleConnections",
    ),
    "connections": "flext_dbt_oracle._utilities.connections",
    "simple_api": "flext_dbt_oracle._utilities.simple_api",
}

__all__ = [
    "FlextDbtOracle",
    "FlextDbtOracleConnections",
    "connections",
    "simple_api",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
