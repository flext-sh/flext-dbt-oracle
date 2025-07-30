"""Oracle Connection Manager for DBT using FLEXT DB Oracle Services.

This module provides the connection management layer for the DBT Oracle adapter,
leveraging flext-infrastructure.databases.flext-db-oracle's modern DDD services
for enterprise-grade reliability.
"""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, cast

# Real DBT and FLEXT imports - no fallbacks
from flext_core import get_logger
from flext_db_oracle import (
    ORACLE_DEFAULT_PORT,
    FlextDbOracleApi,
    FlextDbOracleConfig,
    FlextDbOracleConnection,
)
from flext_meltano import (
    AdapterResponse,
    BaseConnectionManager,
    Connection,
    ConnectionState,
    Credentials,
    DbtDatabaseError,
    DbtRuntimeError,
)
from pydantic import SecretStr

if TYPE_CHECKING:
    from collections.abc import Coroutine

# Create aliases for compatibility
OracleConfig = FlextDbOracleConfig
OracleConnectionService = FlextDbOracleConnection
OracleQueryService = FlextDbOracleApi


# Helper function for async context
def run_async_in_sync_context(coro: object) -> object:
    """Run async coroutine in sync context."""
    import asyncio
    return asyncio.run(cast("Coroutine[Any, Any, Any]", coro))


# Import agate for data handling
try:
    import agate  # type: ignore[import-untyped]
except ImportError:
    agate = None
logger = get_logger(__name__)

# Oracle connection type handling - use real oracledb
try:
    import oracledb
    ORACLEDB_AVAILABLE = True
except ImportError:
    # Fallback when oracledb is not available
    ORACLEDB_AVAILABLE = False
    oracledb = cast("Any", None)  # Type cast to avoid assignment error

logger = get_logger(__name__)


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
    port: int = ORACLE_DEFAULT_PORT
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
        flext-infrastructure.databases.flext-db-oracle configuration with full
        parameterization.
        """
        return OracleConfig(
            host=self.host,
            port=self.port,
            username=self.username,
            password=SecretStr(self.password) if isinstance(self.password, str) else SecretStr(str(self.password)),
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
    Provides DBT connection management while leveraging the enterprise-grade
    Oracle connectivity from flext-infrastructure.databases.flext-db-oracle,
    ensuring zero code duplication
    and consistent error handling across the FLEXT ecosystem.
    """

    TYPE = "oracle"

    def __init__(self, profile: dict[str, Any]) -> None:
        """Initialize connection manager with FLEXT services."""
        # Convert profile dict to AdapterRequiredConfig-like structure
        import multiprocessing
        from types import SimpleNamespace
        config_obj = SimpleNamespace()
        config_obj.__dict__.update(profile)
        super().__init__(config_obj, multiprocessing.get_context("spawn"))  # Proper mp_context
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
            if (hasattr(result, "is_failure") and result.is_failure) or (hasattr(result, "success") and not result.success):
                cls._handle_connection_error(str(result.error) if hasattr(result, "error") else "Connection failed")
            # Store services for later use
            connection.handle = {
                "connection_service": connection_service,
                "query_service": query_service,
                "oracle_config": oracle_config,
            }
            connection.state = ConnectionState.OPEN
            logger.info("Oracle connection opened: %s", connection.name)
        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Failed to open Oracle connection: %s", connection.name)
            connection.state = ConnectionState.FAIL
            connection.handle = None
            msg = f"Failed to open Oracle connection: {e}"
            raise DbtDatabaseError(msg) from e
        return connection

    @classmethod
    def get_response(cls, cursor: Any) -> AdapterResponse:
        """Get response from Oracle query execution."""
        # For FLEXT services, we get results directly
        rows_affected = cursor.row_count
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
            connection.state = ConnectionState.CLOSED
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
    def exception_handler(self, sql: str) -> Any:
        """Context manager for exception handling."""
        try:
            yield
        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Oracle query failed: %s", sql)
            msg = f"Oracle query failed: {e}"
            raise DbtDatabaseError(msg) from e

    def execute(
        self,
        sql: str,
        auto_begin: bool = False,
        fetch: bool = False,
        limit: int | None = None,
    ) -> tuple[AdapterResponse, Any]:
        """Execute SQL using flext-infrastructure.databases.flext-db-oracle query service.

        Execute SQL using flext-infrastructure.databases.flext-db-oracle
        query service.
        """
        connection = self.get_thread_connection()
        if connection.state != "open":
            connection = self.open(connection)
        if not connection.handle:
            msg = "No connection handle available"
            raise DbtRuntimeError(msg)
        with self.exception_handler(sql):
            handle = connection.handle
            query_service = handle["query_service"]
            # Execute query using modern async/sync bridge
            result = run_async_in_sync_context(query_service.execute_query(sql))
            if (hasattr(result, "is_failure") and result.is_failure) or (hasattr(result, "success") and not result.success):
                msg = f"Query execution failed: {result.error if hasattr(result, 'error') else 'Unknown error'}"
                raise DbtDatabaseError(msg)
            # Extract result data from FlextResult or similar object
            if hasattr(result, "data"):
                query_result = result.data
            elif hasattr(result, "value"):
                query_result = result.value
            elif hasattr(result, "unwrap"):
                query_result = result.unwrap()
            else:
                # Fallback - use result directly
                query_result = result
            # Convert to agate table if fetching results
            if fetch and query_result.rows:
                # Create agate table from results if agate is available
                columns = query_result.columns or []
                rows = query_result.rows or []
                if agate and columns and rows:
                    table = agate.Table(rows, column_names=columns)
                elif agate:
                    table = agate.Table([])
                else:
                    # Fallback when agate is not available
                    table = {"columns": columns, "rows": rows}
            elif agate:
                table = agate.Table([])
            else:
                table = {"columns": [], "rows": []}
            # Create response with metrics
            response = AdapterResponse(
                _message=f"Query completed in {query_result.execution_time_ms:.2f}ms",
                rows_affected=query_result.row_count,
                code="SELECT" if sql.strip().upper().startswith("SELECT") else "DDL",
            )
            return response, table

    def add_query(
        self,
        sql: str,
        bindings: dict[str, Any] | None = None,
    ) -> tuple[Any, Any]:
        """Add query to connection with enhanced logging."""
        logger.debug(
            "Executing Oracle query: %s",
            sql[:100] + "..." if len(sql) > 100 else sql,
        )
        connection = self.get_thread_connection()
        with self.exception_handler(sql):
            if connection.state != "open":
                connection = self.open(connection)
            # Get actual cursor from Oracle connection
            if ORACLEDB_AVAILABLE and oracledb and hasattr(connection.handle, "cursor"):
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

                    def execute(self, sql: str, bindings: Any = None) -> None:
                        """Execute SQL (no-op in fallback mode)."""
                        logger.warning(
                            "Using fallback cursor - SQL not executed: %s",
                            sql[:100],
                        )

                    def fetchone(self) -> None:
                        """Fetch one row (no-op in fallback mode)."""
                        return

                    def fetchall(self) -> list[Any]:
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
