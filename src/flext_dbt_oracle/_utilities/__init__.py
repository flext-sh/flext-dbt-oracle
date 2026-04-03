# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_dbt_oracle import connections, simple_api
    from flext_dbt_oracle.connections import (
        FlextDbtOracleConnections,
        host,
        password,
        port,
        protocol,
        service_name,
        sid,
        username,
    )
    from flext_dbt_oracle.simple_api import FlextDbtOracle

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextDbtOracle": "flext_dbt_oracle.simple_api",
    "FlextDbtOracleConnections": "flext_dbt_oracle.connections",
    "connections": "flext_dbt_oracle.connections",
    "host": "flext_dbt_oracle.connections",
    "password": "flext_dbt_oracle.connections",
    "port": "flext_dbt_oracle.connections",
    "protocol": "flext_dbt_oracle.connections",
    "service_name": "flext_dbt_oracle.connections",
    "sid": "flext_dbt_oracle.connections",
    "simple_api": "flext_dbt_oracle.simple_api",
    "username": "flext_dbt_oracle.connections",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
