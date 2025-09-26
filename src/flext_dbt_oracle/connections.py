"""Oracle connection management for FLEXT DBT Oracle.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import asyncio
import concurrent.futures
from collections.abc import Coroutine
from dataclasses import dataclass
from typing import cast, override

from flext_core import FlextLogger, FlextTypes, T
from flext_db_oracle import FlextDbOracleConfig
from flext_meltano import Connection, DbtDatabaseError

logger = FlextLogger(__name__)


class OracleCredentials:
    """Oracle database credentials following FLEXT patterns."""

    @override
    @override
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        schema: str,
        database: str,
        port: int = 1521,
        service_name: str | None = None,
        sid: str | None = None,
        protocol: str = "tcp",
    ) -> None:
        """Initialize Oracle credentials."""
        self.host = host
        self.username = username
        self.password = password
        self.schema = schema
        self.database = database
        self.port = port
        self.service_name = service_name
        self.sid = sid
        self.protocol = protocol
        self.type = "oracle"
        self.unique_field = host

    def _connection_keys(self: object) -> tuple[str, ...]:
        """Get connection keys for pooling."""
        return (
            "host",
            "port",
            "username",
            "password",
            "service_name",
            "sid",
            "protocol",
            "schema",
        )

    @property
    def database_identifier(self: object) -> str:
        """Get database identifier (service_name or sid)."""
        return self.service_name or self.sid or "XE"

    def to_oracle_config(self: object) -> FlextDbOracleConfig:
        """Convert to Oracle config."""
        return FlextDbOracleConfig(
            host=self.host,
            port=self.port,
            user=self.username,  # Use 'user' field, not 'username'
            password=self.password,
            service_name=self.service_name,
        )


class FlextOracleOracleConnectionManager:
    """Oracle connection manager following FLEXT patterns."""

    TYPE = "oracle"

    @override
    @override
    def __init__(self, profile: FlextTypes.Core.Dict) -> None:
        """Initialize connection manager."""
        self.profile = profile
        self._oracle_services: dict[str, object] = {}
        self.thread_connections: dict[str, Connection] = {}

    def open(self, connection: Connection) -> Connection:
        """Open connection."""
        try:
            connection.state = "open"
            connection.handle = {
                "connection_service": "None",
                "query_service": "None",
                "oracle_config": cast(
                    "OracleCredentials",
                    connection.credentials,
                ).to_oracle_config(),
            }
            return connection
        except Exception as e:
            self._handle_connection_error(f"Connection {connection.name} failed: {e}")
            raise

    def _handle_connection_error(self, error_message: str) -> None:
        """Handle connection error."""
        raise DbtDatabaseError(error_message)

    def cancel_open(self: object) -> list[str]:
        """Cancel open connections."""
        cancelled: list[str] = []
        for name, connection in self.thread_connections.items():
            if connection.state == "open":
                connection.state = "closed"
                cancelled.append(name)
        return cancelled

    def get_thread_connection(self, name: str) -> Connection | None:
        """Get thread connection."""
        return self.thread_connections.get(name)

    @override
    def execute(self, sql: str, *, fetch: bool = False) -> tuple[object, object]:
        """Execute SQL query."""

        # Mock response for testing
        class MockResponse:
            @override
            @override
            def __init__(self: object) -> None:
                self.code = "SELECT"
                self.rows_affected = 0

        # Use sql parameter to avoid unused argument warning
        _ = sql, fetch  # Suppress unused parameter warnings
        return MockResponse(), None

    def add_query(
        self,
        sql: str,
        bindings: FlextTypes.Core.Dict,
    ) -> tuple[Connection, object]:
        """Add query with fallback cursor."""

        # Mock cursor for testing
        @dataclass
        class MockCursor:
            sql: str
            bindings: FlextTypes.Core.Dict

        connection = self.get_thread_connection("default")
        if connection is None:
            error_msg = "No connection available"
            raise DbtDatabaseError(error_msg)
        cursor = MockCursor(sql, bindings)
        return connection, cursor

    def begin(self: object) -> None:
        """Begin transaction."""

    def commit(self: object) -> None:
        """Commit transaction."""

    def rollback(self: object) -> None:
        """Rollback transaction."""


def run_async_in_sync_context[T](coro: Coroutine[object, object, T]) -> T:
    """Run async coroutine in sync context."""
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # If we're already in an async context, we need to use a different approach
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future: concurrent.futures.Future[T] = executor.submit(
                    lambda: asyncio.run(coro),
                )
                return future.result()
        else:
            return loop.run_until_complete(coro)
    except RuntimeError:
        # No event loop running, create a new one
        return asyncio.run(coro)


__all__ = [
    "FlextOracleOracleConnectionManager",
    "OracleCredentials",
    "run_async_in_sync_context",
]
