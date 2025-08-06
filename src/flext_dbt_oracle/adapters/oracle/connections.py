"""Oracle Connection Manager for DBT using FLEXT DB Oracle Services.

This module provides the connection management layer for the DBT Oracle adapter,
leveraging flext-infrastructure.databases.flext-db-oracle's modern DDD services
for enterprise-grade reliability.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import asyncio
import multiprocessing
from contextlib import contextmanager
from typing import Iterator
from dataclasses import dataclass
from types import SimpleNamespace
from typing import TYPE_CHECKING, ClassVar, cast

import agate  # type: ignore[import-untyped]
from flext_core import get_logger
from flext_db_oracle import (
    FlextDbOracleApi,
    FlextDbOracleConfig,
    FlextDbOracleConnection,
)
from flext_db_oracle.constants import FlextOracleDbConstants
from pydantic import SecretStr

if TYPE_CHECKING:
    from collections.abc import Coroutine


# Create local DBT exceptions since they're not available in dependencies
class DbtDatabaseError(Exception):
    """Database-related DBT adapter error."""


class DbtRuntimeError(Exception):
    """Runtime DBT adapter error."""


# Mock ConnectionState for runtime since it might not be available in all DBT versions
class ConnectionState:
    """Mock ConnectionState for runtime compatibility with different DBT versions."""

    OPEN = "open"
    FAIL = "fail"
    CLOSED = "closed"


if TYPE_CHECKING:
    from dbt.adapters.base.connections import BaseConnectionManager
    from dbt.adapters.contracts.connection import (
        AdapterResponse,
        Connection,
        Credentials,
    )
else:
    # Mock for runtime
    class AdapterResponse:
        """Adapter response class."""

        def __init__(self, _rows_affected: int = 0, **kwargs: object) -> None:
            """Initialize adapter response."""
            self._rows_affected = _rows_affected
            for k, v in kwargs.items():
                setattr(self, k, v)

    class Connection:
        """Connection class."""

        def __init__(self) -> None:
            """Initialize connection."""
            self.state: str = "closed"
            self.credentials: object | None = None
            self.handle: object | None = None
            self.name: str = ""

    class Credentials:
        """Credentials class."""

        def __init__(self) -> None:
            """Initialize credentials."""

    class BaseConnectionManager:
        """Base connection manager class."""

        def __init__(self, config_obj: object, mp_context: object) -> None:
            """Initialize connection manager."""
            self.config_obj = config_obj
            self.mp_context = mp_context

        def get_thread_connection(self) -> Connection:
            """Get thread connection."""
            return Connection()  # type: ignore[call-arg]

        def open(self, connection: Connection) -> Connection:
            """Open connection."""
            return connection

        @contextmanager
        def exception_handler(self, sql: str):
            """Exception handler context manager."""
            try:
                yield
            except Exception:
                pass

    # ConnectionState is already defined above at line 45-50


# Create aliases for compatibility
OracleConfig = FlextDbOracleConfig
OracleConnectionService = FlextDbOracleConnection
OracleQueryService = FlextDbOracleApi

logger = get_logger(__name__)


# Helper function for async context
def run_async_in_sync_context(coro: object) -> object:
    """Run async coroutine in sync context."""
    return asyncio.run(cast("Coroutine[object, object, object]", coro))


@dataclass
class OracleCredentials(Credentials):
    """Oracle database credentials for DBT.

    Extends DBT's base Credentials class with Oracle-specific configuration
    using flext-infrastructure.databases.flext-db-oracle standards for consistency
    across the FLEXT ecosystem.
    """

    # Oracle connection parameters - required first
    host: str
    username: str
    password: str
    schema: str  # Required by DBT
    # DBT-specific settings - required
    database: str
    # Oracle connection parameters with defaults
    port: int = FlextOracleDbConstants.ORACLE_DEFAULT_PORT
    service_name: str | None = None
    sid: str | None = None
    protocol: str = "tcp"
    # Connection pool configuration
    pool_min_size: int = 1
    pool_max_size: int = 5
    pool_increment: int = 1
    # Advanced Oracle settings
    ssl_server_dn_match: bool = False
    nls_lang: str | None = None
    nls_date_format: str = "YYYY-MM-DD HH24:MI:SS"
    # Optional DBT-specific settings
    search_path: str | None = None
    # DBT required attributes
    _ALIASES: ClassVar[dict[str, str]] = {
        "dbname": "database",
        "pass": "password",
        "user": "username",
    }

    @property
    def type(self) -> str:
        """Return adapter type."""
        return "oracle"

    @property
    def unique_field(self) -> str:
        """Return unique identifier for connection."""
        return self.host

    def _connection_keys(self) -> tuple[str, ...]:
        """Return keys used for connection pooling."""
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
    def database_identifier(self) -> str:
        """Get database identifier for flext-infrastructure.databases.flext-db-oracle.

        Get database identifier for
        flext-infrastructure.databases.flext-db-oracle.
        """
        return self.service_name or self.sid or "ORCL"

    def to_oracle_config(self) -> OracleConfig:
        """Convert DBT credentials to flext-infrastructure.databases.flext-db-oracle configuration.

        Convert DBT credentials to
        flext-infrastructure.databases.flext-db-oracle configuration.
        """
        return OracleConfig(
            host=self.host,
            port=self.port,
            username=self.username,
            password=SecretStr(self.password)
            if isinstance(self.password, str)
            else SecretStr(str(self.password)),
            service_name=self.service_name or "XEPDB1",  # Default service name
            sid=self.sid,
            protocol=self.protocol,
            # Enhanced parameterization for DBT workloads
            pool_min=self.pool_min_size,
            pool_max=self.pool_max_size,
            pool_increment=self.pool_increment,
            timeout=300,  # DBT queries can be long-running
        )


class FlextOracleOracleConnectionManager(BaseConnectionManager):
    """Oracle connection manager using flext-infrastructure.databases.flext-db-oracle services.

    Oracle connection manager using
    flext-infrastructure.databases.flext-db-oracle services.
    """

    TYPE = "oracle"

    def __init__(self, config: object, mp_context: object = None) -> None:
        """Initialize connection manager with FLEXT services."""
        # Handle both old profile dict and new config + mp_context pattern
        if isinstance(config, dict):
            profile = config
        else:
            # Convert config object to dict for compatibility
            profile = getattr(config, "__dict__", {})

        if mp_context is None:
            mp_context = multiprocessing.get_context("spawn")

        # Convert profile dict to AdapterRequiredConfig-like structure

        config_obj = SimpleNamespace()
        config_obj.__dict__.update(profile)
        super().__init__(config_obj, mp_context)  # type: ignore[arg-type]
        self._oracle_services: dict[
            str,
            tuple[OracleConnectionService, OracleQueryService],
        ] = {}

    @classmethod
    def open(cls, connection: Connection) -> Connection:
        """Open Oracle connection using flext-infrastructure.databases.flext-db-oracle services.

        Open Oracle connection using
        flext-infrastructure.databases.flext-db-oracle services.
        """
        if connection.state == "open":
            logger.debug("Connection already open: %s", connection.name)
            return connection
        credentials = connection.credentials
        if not isinstance(credentials, OracleCredentials):
            msg = "Invalid credentials type"
            raise DbtRuntimeError(msg)
        try:
            # Create Oracle configuration using enhanced parameterization
            oracle_config = credentials.to_oracle_config()
            logger.info(
                "Created Oracle DB config for DBT with parameterization: "
                "pool_size=%d, timeout=%d",
                oracle_config.pool_max,
                oracle_config.timeout,
            )
            # Initialize FLEXT services
            connection_service = OracleConnectionService(oracle_config)
            query_service = OracleQueryService(oracle_config)
            # Test connection using modern async/sync bridge
            result = run_async_in_sync_context(connection_service.test_connection())
            if (hasattr(result, "is_failure") and result.is_failure) or (
                hasattr(result, "success") and not result.success
            ):
                cls._handle_connection_error(
                    str(result.error)
                    if hasattr(result, "error")
                    else "Connection failed",
                )
            # Store services for later use
            connection.handle = {
                "connection_service": connection_service,
                "query_service": query_service,
                "oracle_config": oracle_config,
            }
            connection.state = ConnectionState.OPEN  # type: ignore[assignment]
            logger.info("Oracle connection opened: %s", connection.name)
        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Failed to open Oracle connection: %s", connection.name)
            connection.state = ConnectionState.FAIL  # type: ignore[assignment]
            connection.handle = None
            error_msg: str = f"Failed to open Oracle connection: {e}"
            raise DbtDatabaseError(error_msg) from e
        return connection

    @classmethod
    def get_response(cls, cursor: object) -> AdapterResponse:
        """Get response from Oracle query execution."""
        # For FLEXT services, we get results directly
        rows_affected = getattr(cursor, "row_count", 0)
        return AdapterResponse(
            _message="Query completed successfully",
            rows_affected=rows_affected,
            code="SELECT",
        )

    def cancel_open(self) -> list[str]:
        """Cancel open connections."""
        for connection in self.thread_connections.values():
            try:
                handle = connection.handle
                if isinstance(handle, dict) and "connection_service" in handle:
                    # Close FLEXT connection service using modern async/sync bridge
                    run_async_in_sync_context(
                        handle["connection_service"].close_pool(),
                    )
            except (RuntimeError, ValueError, TypeError) as e:
                logger.warning("Error closing connection: %s", e)
            connection.state = ConnectionState.CLOSED  # type: ignore[assignment]
            connection.handle = None
        return []

    @classmethod
    def _handle_connection_error(cls, error: str | None) -> None:
        """Handle connection errors by raising appropriate exception."""
        error_message = (
            f"Connection test failed: {error}" if error else "Connection test failed"
        )
        raise DbtDatabaseError(error_message)

    @contextmanager
    def exception_handler(self, sql: str) -> Iterator[None]:
        """Context manager for exception handling."""
        try:
            yield
        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Oracle query failed: %s", sql)
            sql_error_msg: str = f"Oracle query failed: {e}"
            raise DbtDatabaseError(sql_error_msg) from e

    def execute(
        self,
        sql: str,
        auto_begin: bool = False,
        fetch: bool = False,
        limit: int | None = None,
    ) -> tuple[AdapterResponse, object]:
        """Execute SQL using flext-infrastructure.databases.flext-db-oracle query service.

        Execute SQL using flext-infrastructure.databases.flext-db-oracle query service.
        """
        connection = self.get_thread_connection()
        if connection.state != "open":
            connection = self.open(connection)
        if not connection.handle:
            msg = "No connection handle available"
            raise DbtRuntimeError(msg)

        executor = OracleQueryExecutor(connection.handle, fetch=fetch)
        return executor.execute(sql)


class OracleQueryExecutor:
    """Strategy pattern for Oracle query execution with SOLID principles."""

    def __init__(self, handle: dict[str, object], *, fetch: bool = False) -> None:
        """Initialize query executor."""
        self.handle = handle
        self.fetch = fetch
        self.result_extractor = QueryResultExtractor()
        self.table_factory = AgateTableFactory()

    def execute(self, sql: str) -> tuple[AdapterResponse, object]:
        """Execute query and return response."""
        query_service = self.handle["query_service"]
        raw_result = run_async_in_sync_context(query_service.execute_query(sql))  # type: ignore[attr-defined]

        self._validate_result(raw_result)
        query_result = self.result_extractor.extract(raw_result)
        table = self.table_factory.create(query_result, fetch=self.fetch)
        response = self._create_response(query_result, sql)

        return response, table

    def _validate_result(self, result: object) -> None:
        """Validate query execution result."""
        if (hasattr(result, "is_failure") and result.is_failure) or (
            hasattr(result, "success") and not result.success
        ):
            error_msg = result.error if hasattr(result, "error") else "Unknown error"
            msg: str = f"Query execution failed: {error_msg}"
            raise DbtDatabaseError(msg)

    def _create_response(self, query_result: object, sql: str) -> AdapterResponse:
        """Create adapter response with metrics."""
        execution_time = getattr(query_result, "execution_time_ms", 0.0)
        rows_affected = getattr(query_result, "row_count", 0)
        return AdapterResponse(
            _message=f"Query completed in {execution_time:.2f}ms",
            rows_affected=rows_affected,
            code="SELECT" if sql.strip().upper().startswith("SELECT") else "DDL",
        )


class QueryResultExtractor:
    """Extract query result data from various result types."""

    def extract(self, result: object) -> object:
        """Extract result data using strategy pattern."""
        if hasattr(result, "data"):
            return result.data
        if hasattr(result, "value"):
            return result.value
        if hasattr(result, "unwrap"):
            return result.unwrap()
        return result


class AgateTableFactory:
    """Factory for creating agate tables with fallback strategy."""

    def __init__(self) -> None:
        """Initialize AgateTableFactory."""
        pass

    def get_thread_connection(self) -> Connection:
        """Mock method for compatibility."""
        return Connection()  # type: ignore[call-arg]

    def open(self, connection: Connection) -> Connection:
        """Mock method for compatibility."""
        return connection

    @contextmanager
    def exception_handler(self, sql: str) -> Iterator[None]:
        """Mock exception handler."""
        try:
            yield
        except Exception:
            pass

    def create(self, query_result: object, *, fetch: bool) -> object:
        """Create table using appropriate strategy."""
        if not fetch:
            return agate.Table([]) if agate else {"columns": [], "rows": []}

        if not hasattr(query_result, "rows") or not query_result.rows:
            return agate.Table([]) if agate else {"columns": [], "rows": []}

        return self._create_from_rows(query_result)

    def _create_from_rows(self, query_result: object) -> object:
        """Create table from query result rows."""
        columns = getattr(query_result, "columns", []) or []
        rows = getattr(query_result, "rows", []) or []

        if agate and columns and rows:
            return agate.Table(rows, column_names=columns)
        if agate:
            return agate.Table([])
        return {"columns": columns, "rows": rows}

    def add_query(
        self,
        sql: str,
        bindings: dict[str, object] | None = None,
    ) -> tuple[object, object]:
        """Add query to connection with enhanced logging."""
        max_sql_log_length = 100
        logger.debug(
            "Executing Oracle query: %s",
            sql[:max_sql_log_length] + "..." if len(sql) > max_sql_log_length else sql,
        )
        connection = self.get_thread_connection()
        with self.exception_handler(sql):
            if connection.state != "open":
                connection = self.open(connection)
            # Get actual cursor from Oracle connection
            if hasattr(connection.handle, "cursor"):
                cursor = connection.handle.cursor()
                # Store execution context for debugging using public attributes
                # Note: Using setattr to avoid direct private attribute access
                cursor.flext_sql = sql
                cursor.flext_bindings = bindings or {}
            else:
                # Development/testing fallback cursor
                class FallbackCursor:
                    """Fallback cursor for development/testing."""

                    def __init__(self) -> None:
                        self.sql = sql
                        self.bindings = bindings or {}
                        self.row_count = 0
                        self.arraysize = 1

                    def execute(self, sql: str, _bindings: object = None) -> None:
                        """Execute SQL (no-op in fallback mode)."""
                        logger.warning(
                            "Using fallback cursor - SQL not executed: %s",
                            sql[:100],
                        )

                    def fetchone(self) -> None:
                        """Fetch one row (no-op in fallback mode)."""
                        return

                    def fetchall(self) -> list[object]:
                        """Fetch all rows (empty in fallback mode)."""
                        return []

                    def close(self) -> None:
                        """Close cursor (no-op in fallback mode)."""

                cursor = FallbackCursor()
            return connection, cursor

    def begin(self) -> None:
        """Begin transaction (Oracle auto-commit mode)."""
        # Oracle in DBT typically uses auto-commit mode
        # Transactions are handled at the SQL level
        connection = self.get_thread_connection()
        if connection.state != "open":
            self.open(connection)
        logger.debug("Oracle transaction begin (auto-commit mode)")

    def commit(self) -> None:
        """Commit transaction (Oracle auto-commit mode)."""
        # Oracle in DBT typically uses auto-commit mode
        connection = self.get_thread_connection()
        if connection.state == "open":
            logger.debug("Oracle transaction commit (auto-commit mode)")

    def rollback(self) -> None:
        """Rollback transaction (Oracle auto-commit mode)."""
        # Oracle in DBT typically uses auto-commit mode
        connection = self.get_thread_connection()
        if connection.state == "open":
            logger.debug("Oracle transaction rollback (auto-commit mode)")


# Create aliases for backwards compatibility
OracleConnectionManager = FlextOracleOracleConnectionManager
FlextOracleConnectionManager = FlextOracleOracleConnectionManager
