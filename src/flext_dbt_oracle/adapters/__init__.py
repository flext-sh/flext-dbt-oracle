"""FLEXT DBT Oracle Adapters - Database adaptation layer.

This module provides Oracle database adapters for FLEXT DBT integration,
implementing connection pooling, query execution, and schema management
specific to Oracle databases.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from .oracle.connections import FlextOracleConnectionManager
from .oracle.impl import OracleAdapter as FlextOracleAdapter

__all__: list[str] = [
    "FlextOracleAdapter",
    "FlextOracleConnectionManager",
]
