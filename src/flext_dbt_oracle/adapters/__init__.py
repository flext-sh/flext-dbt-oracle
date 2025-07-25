"""FLEXT DBT Oracle Adapters - Database adaptation layer.

This module provides Oracle database adapters for FLEXT DBT integration,
implementing connection pooling, query execution, and schema management
specific to Oracle databases.
"""

from __future__ import annotations

from .oracle.adapter import FlextOracleAdapter
from .oracle.connections import FlextOracleConnectionManager

__all__ = [
    "FlextOracleAdapter",
    "FlextOracleConnectionManager",
]
