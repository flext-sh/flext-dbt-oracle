"""Advanced tests for Oracle connections using FLEXT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Never
from unittest.mock import Mock, patch

import pytest
from flext_meltano import Connection, DbtDatabaseError

from flext_dbt_oracle import (
    FlextOracleOracleConnectionManager,
    OracleCredentials,
    run_async_in_sync_context,
)


class TestOracleCredentials:
    """Test Oracle credentials functionality."""

    def test_oracle_credentials_creation(self) -> None:
        """Test creating Oracle credentials."""
        creds = OracleCredentials(
            host="localhost",
            username="testuser",
            password="testpass",
            schema="testschema",
            database="oracle",
        )
        assert creds.host == "localhost"
        assert creds.username == "testuser"
        assert creds.type == "oracle"
        assert creds.unique_field == "localhost"

    def test_connection_keys(self) -> None:
        """Test connection keys for pooling."""
        creds = OracleCredentials(
            host="localhost",
            username="testuser",
            password="testpass",
            schema="testschema",
            database="oracle",
        )
        keys = creds._connection_keys()
        expected_keys = (
            "host",
            "port",
            "username",
            "password",
            "service_name",
            "sid",
            "protocol",
            "schema",
        )
        assert keys == expected_keys

    def test_database_identifier(self) -> None:
        """Test database identifier generation."""
        creds = OracleCredentials(
            host="localhost",
            username="testuser",
            password="testpass",
            schema="testschema",
            database="oracle",
            service_name="XEPDB1",
        )
        assert creds.database_identifier == "XEPDB1"

        creds_with_sid = OracleCredentials(
            host="localhost",
            username="testuser",
            password="testpass",
            schema="testschema",
            database="oracle",
            sid="XE",
        )
        assert creds_with_sid.database_identifier == "XE"

    def test_to_oracle_config(self) -> None:
        """Test conversion to Oracle config."""
        creds = OracleCredentials(
            host="localhost",
            username="testuser",
            password="testpass",
            schema="testschema",
            database="oracle",
            service_name="XEPDB1",
        )
        config = creds.to_oracle_config()
        assert config.host == "localhost"
        assert config.username == "testuser"
        assert config.service_name == "XEPDB1"


class TestConnectionManager:
    """Test Oracle connection manager functionality."""

    def test_connection_manager_init(self) -> None:
        """Test connection manager initialization."""
        profile = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            manager = FlextOracleOracleConnectionManager(profile)
            assert manager.TYPE == "oracle"
            assert hasattr(manager, "_oracle_services")

    @patch("flext_dbt_oracle.adapters.oracle.connections.run_async_in_sync_context")
    @patch("flext_dbt_oracle.adapters.oracle.connections.OracleConnectionService")
    @patch("flext_dbt_oracle.adapters.oracle.connections.OracleQueryService")
    def test_open_connection_success(
        self,
        mock_query_service: Mock,
        mock_connection_service: Mock,
        mock_async_run: Mock,
    ) -> None:
        """Test successful connection opening."""
        # Setup mocks
        mock_conn_instance = Mock()
        mock_connection_service.return_value = mock_conn_instance
        mock_query_instance = Mock()
        mock_query_service.return_value = mock_query_instance

        # Mock successful connection test
        mock_result = Mock()
        mock_result.is_failure = False
        mock_result.success = True
        mock_async_run.return_value = mock_result

        # Create connection object
        connection = Mock(spec=Connection)
        connection.state = "closed"
        connection.name = "test_connection"
        connection.credentials = OracleCredentials(
            host="localhost",
            username="testuser",
            password="testpass",
            schema="testschema",
            database="oracle",
        )

        # Test connection opening
        profile = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            manager = FlextOracleOracleConnectionManager(profile)
            result = manager.open(connection)

            assert result.state == "open"
            assert connection.handle is not None

    def test_handle_connection_error(self) -> None:
        """Test connection error handling."""
        profile = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            manager = FlextOracleOracleConnectionManager(profile)

            with pytest.raises(
                DbtDatabaseError,
                match="Connection test failed: Test error",
            ):
                manager._handle_connection_error("Test error")

    def test_cancel_open_connections(self) -> None:
        """Test canceling open connections."""
        profile = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            manager = FlextOracleOracleConnectionManager(profile)

            # Create mock connection
            mock_connection = Mock()
            mock_connection.handle = {
                "connection_service": Mock(),
                "query_service": Mock(),
                "oracle_config": Mock(),
            }
            mock_connection.state = "open"

            manager.thread_connections = {"test": mock_connection}

            with patch(
                "flext_dbt_oracle.adapters.oracle.connections.run_async_in_sync_context",
            ):
                result = manager.cancel_open()
                assert result == []
                assert mock_connection.state == "closed"


class TestAsyncHelpers:
    """Test async helper functions."""

    def test_run_async_in_sync_context(self) -> None:
        """Test async to sync context conversion."""

        async def test_coro() -> str:
            return "test_result"

        result = run_async_in_sync_context(test_coro())
        assert result == "test_result"

    def test_run_async_in_sync_context_with_exception(self) -> None:
        """Test async context with exception."""

        async def failing_coro() -> Never:
            msg = "Test error"
            raise ValueError(msg)

        with pytest.raises(ValueError, match="Test error"):
            run_async_in_sync_context(failing_coro())


class TestExecuteQueries:
    """Test query execution functionality."""

    @patch("flext_dbt_oracle.adapters.oracle.connections.run_async_in_sync_context")
    @patch("multiprocessing.get_context")
    @pytest.mark.usefixtures("_mock_oracle_connection")
    def test_execute_query_success(
        self,
        mock_async_run: Mock,
    ) -> None:
        """Test successful query execution."""
        # Setup mocks
        mock_result = Mock()
        mock_result.is_failure = False
        mock_result.success = True
        mock_result.data = Mock()
        mock_result.data.rows = []
        mock_result.data.columns = ["col1", "col2"]
        mock_result.data.execution_time_ms = 100.0
        mock_result.data.row_count = 0
        mock_async_run.return_value = mock_result

        # Create connection manager
        profile = {"host": "localhost", "username": "test"}
        manager = FlextOracleOracleConnectionManager(profile)

        # Mock connection
        mock_connection = Mock()
        mock_connection.state = "open"
        mock_connection.handle = {
            "query_service": Mock(),
            "connection_service": Mock(),
            "oracle_config": Mock(),
        }

        # Mock query service
        mock_query_service = mock_connection.handle["query_service"]
        mock_query_service.execute_query.return_value = mock_result

        # Mock the get_thread_connection method
        manager.get_thread_connection = Mock(return_value=mock_connection)

        with patch.object(manager, "exception_handler") as mock_exception_handler:
            mock_exception_handler.__enter__ = Mock(return_value=None)
            mock_exception_handler.__exit__ = Mock(return_value=None)

            response, _table = manager.execute("SELECT 1", fetch=True)

            assert response.code in {"SELECT", "DDL"}
            assert response.rows_affected == 0


class TestFallbackCursor:
    """Test fallback cursor functionality."""

    @patch("multiprocessing.get_context")
    def test_add_query_with_fallback_cursor(self) -> None:
        """Test adding query with fallback cursor when oracledb not available."""
        profile = {"host": "localhost", "username": "test"}
        manager = FlextOracleOracleConnectionManager(profile)

        # Mock connection
        mock_connection = Mock()
        mock_connection.state = "open"
        mock_connection.handle = Mock()

        manager.get_thread_connection = Mock(return_value=mock_connection)

        # Patch ORACLEDB_AVAILABLE to False to trigger fallback cursor
        with (
            patch.object(manager, "exception_handler") as mock_exception_handler,
            patch(
                "flext_dbt_oracle.adapters.oracle.connections.ORACLEDB_AVAILABLE",
                new=False,
            ),
        ):
            mock_exception_handler.__enter__ = Mock(return_value=None)
            mock_exception_handler.__exit__ = Mock(return_value=None)

            connection, cursor = manager.add_query("SELECT 1", {"param": "value"})

            assert connection == mock_connection
            assert hasattr(cursor, "sql")
            assert hasattr(cursor, "bindings")
            assert cursor.sql == "SELECT 1"
            assert cursor.bindings == {"param": "value"}


class TestTransactionMethods:
    """Test transaction methods."""

    @patch("multiprocessing.get_context")
    def test_begin_transaction(self) -> None:
        """Test beginning transaction."""
        profile = {"host": "localhost", "username": "test"}
        manager = FlextOracleOracleConnectionManager(profile)

        mock_connection = Mock()
        mock_connection.state = "open"
        manager.get_thread_connection = Mock(return_value=mock_connection)

        # Should not raise any exception
        manager.begin()

    @patch("multiprocessing.get_context")
    def test_commit_transaction(self) -> None:
        """Test committing transaction."""
        profile = {"host": "localhost", "username": "test"}
        manager = FlextOracleOracleConnectionManager(profile)

        mock_connection = Mock()
        mock_connection.state = "open"
        manager.get_thread_connection = Mock(return_value=mock_connection)

        # Should not raise any exception
        manager.commit()

    @patch("multiprocessing.get_context")
    def test_rollback_transaction(self) -> None:
        """Test rolling back transaction."""
        profile = {"host": "localhost", "username": "test"}
        manager = FlextOracleOracleConnectionManager(profile)

        mock_connection = Mock()
        mock_connection.state = "open"
        manager.get_thread_connection = Mock(return_value=mock_connection)

        # Should not raise any exception
        manager.rollback()
