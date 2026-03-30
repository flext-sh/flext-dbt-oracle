# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT Oracle utilities submodules."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle._utilities import (
        connections as connections,
        simple_api as simple_api,
    )
    from flext_dbt_oracle._utilities.connections import (
        FlextDbtOracleConnections as FlextDbtOracleConnections,
        build_oracle_connection_config as build_oracle_connection_config,
    )
    from flext_dbt_oracle._utilities.simple_api import FlextDbtOracle as FlextDbtOracle

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtOracle": ["flext_dbt_oracle._utilities.simple_api", "FlextDbtOracle"],
    "FlextDbtOracleConnections": [
        "flext_dbt_oracle._utilities.connections",
        "FlextDbtOracleConnections",
    ],
    "build_oracle_connection_config": [
        "flext_dbt_oracle._utilities.connections",
        "build_oracle_connection_config",
    ],
    "connections": ["flext_dbt_oracle._utilities.connections", ""],
    "simple_api": ["flext_dbt_oracle._utilities.simple_api", ""],
}

_EXPORTS: Sequence[str] = [
    "FlextDbtOracle",
    "FlextDbtOracleConnections",
    "build_oracle_connection_config",
    "connections",
    "simple_api",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
