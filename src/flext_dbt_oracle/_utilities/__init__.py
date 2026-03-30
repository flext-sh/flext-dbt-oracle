# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT Oracle utilities submodules."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle._utilities import connections, simple_api
    from flext_dbt_oracle._utilities.connections import *
    from flext_dbt_oracle._utilities.simple_api import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextDbtOracle": "flext_dbt_oracle._utilities.simple_api",
    "FlextDbtOracleConnections": "flext_dbt_oracle._utilities.connections",
    "build_oracle_connection_config": "flext_dbt_oracle._utilities.connections",
    "connections": "flext_dbt_oracle._utilities.connections",
    "simple_api": "flext_dbt_oracle._utilities.simple_api",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
