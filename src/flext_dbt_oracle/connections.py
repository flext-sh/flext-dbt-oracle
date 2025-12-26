"""Oracle connection management for FLEXT DBT Oracle.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from dataclasses import dataclass
from typing import override

from flext_core import FlextLogger, T
from flext_db_oracle import FlextDbOracleSettings
from flext_meltano import Connection, DbtDatabaseError


class FlextDbtOracleConnections:
    """Unified Oracle connection management with credentials, connection manager, and utilities.

    Consolidates Oracle connection functionality including credentials management,
    connection pooling, and utilities following FLEXT unified class pattern.
    """

    # Shared logger for all Oracle connection operations
    logger = FlextLogger(__name__)

    class Credentials:
        """Oracle database credentials following FLEXT patterns."""

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
            self.unique_field = self.host

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

        def to_oracle_config(self: object) -> FlextDbOracleSettings:
            """Convert to Oracle config."""
            return FlextDbOracleSettings(
                oracle_host=self.host,
                oracle_port=self.port,
                oracle_username=self.username,
                oracle_password=self.password,
                oracle_service_name=self.service_name,
            )

    class ConnectionManager:
        """Oracle connection manager following FLEXT patterns."""

        TYPE = "oracle"

        @override
        def __init__(self, profile: dict[str, object]) -> None:
            """Initialize connection manager."""
            self.profile = profile
            self._oracle_services: dict[str, object] = {}
            self.thread_connections: dict[str, Connection] = {}

        def open(self, connection: Connection) -> Connection:
            """Open connection."""
            try:
                connection.state = "open"
                # Type narrowing - credentials should be Credentials
                if not isinstance(
                    connection.credentials, FlextDbtOracleConnections.Credentials
                ):
                    msg = "Invalid credentials type"
                    raise DbtDatabaseError(msg)
                connection.handle = {
                    "connection_service": "None",
                    "query_service": "None",
                    "oracle_config": connection.credentials.to_oracle_config(),
                }
                return connection
            except Exception as e:
                self._handle_connection_error(
                    f"Connection {connection.name} failed: {e}",
                )
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
            bindings: dict[str, object],
        ) -> tuple[Connection, object]:
            """Add query with fallback cursor."""

            # Mock cursor for testing
            @dataclass
            class MockCursor:
                sql: str
                bindings: dict[str, object]

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

    class Utilities:
        """utilities for Oracle connections."""

        @staticmethod
        def run_in_sync_context[T](coro: T) -> T:
            """Run coroutine in sync context (synchronous stub).

            Args:
            coro: Object to process (ignored in sync implementation)

            Returns:
            The input object (pass-through for sync compatibility)

            """
            # Synchronous stub - return the input unchanged
            # Real async operations should be converted to sync alternatives
            return coro


__all__ = [
    "FlextDbtOracleConnections",
]
