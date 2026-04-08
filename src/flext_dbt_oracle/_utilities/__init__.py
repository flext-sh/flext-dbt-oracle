# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "FlextDbtOracle": ("flext_dbt_oracle._utilities.simple_api", "FlextDbtOracle"),
    "FlextDbtOracleConnections": (
        "flext_dbt_oracle._utilities.connections",
        "FlextDbtOracleConnections",
    ),
    "connections": "flext_dbt_oracle._utilities.connections",
    "simple_api": "flext_dbt_oracle._utilities.simple_api",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
