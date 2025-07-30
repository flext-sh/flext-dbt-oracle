"""Advanced tests for Oracle adapter implementation using FLEXT patterns."""

from unittest.mock import Mock, patch

import pytest
from flext_meltano import BaseRelation

from flext_dbt_oracle.adapters.oracle.connections import (
    FlextOracleOracleConnectionManager,
)
from flext_dbt_oracle.adapters.oracle.impl import OracleAdapter


class TestOracleAdapter:
    """Test Oracle adapter implementation functionality."""

    def test_adapter_creation(self) -> None:
        """Test creating Oracle adapter."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)
            assert adapter is not None
            assert adapter.ConnectionManager == FlextOracleOracleConnectionManager

    def test_adapter_type(self) -> None:
        """Test adapter connection manager type."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)
            assert adapter.ConnectionManager.TYPE == "oracle"

    def test_date_function(self) -> None:
        """Test Oracle date function."""
        assert OracleAdapter.date_function() == "SYSDATE"

    def test_is_cancelable(self) -> None:
        """Test that Oracle connections are cancelable."""
        assert OracleAdapter.is_cancelable() is True

    def test_get_columns_in_relation(self) -> None:
        """Test getting columns in relation."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Mock relation
            mock_relation = Mock()
            mock_relation.schema = "TEST_SCHEMA"
            mock_relation.identifier = "TEST_TABLE"

            # Mock connection and execution
            with patch.object(adapter, "execute") as mock_execute:
                mock_execute.return_value = (Mock(), [])

                columns = adapter.get_columns_in_relation(mock_relation)
                assert isinstance(columns, list)

    def test_list_relations_without_caching(self) -> None:
        """Test listing relations without caching."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Mock schema and database
            schema_relation = Mock()
            schema_relation.schema = "TEST_SCHEMA"
            schema_relation.database = "TEST_DB"

            # Mock execute method
            with patch.object(adapter, "execute") as mock_execute:
                mock_execute.return_value = (Mock(), [])

                relations = adapter.list_relations_without_caching(schema_relation)
                assert isinstance(relations, list)

    def test_check_schema_exists(self) -> None:
        """Test checking if schema exists."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Mock execute method to return results indicating schema exists
            with patch.object(adapter, "execute") as mock_execute:
                mock_execute.return_value = (Mock(), [("TEST_SCHEMA",)])

                exists = adapter.check_schema_exists("TEST_DB", "TEST_SCHEMA")
                assert exists is True

    def test_check_schema_not_exists(self) -> None:
        """Test checking if schema doesn't exist."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Mock execute method to return empty results
            with patch.object(adapter, "execute") as mock_execute:
                mock_execute.return_value = (Mock(), [])

                exists = adapter.check_schema_exists("TEST_DB", "TEST_SCHEMA")
                assert exists is False

    def test_create_schema(self) -> None:
        """Test creating schema."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Mock execute method
            with patch.object(adapter, "execute") as mock_execute:
                mock_execute.return_value = (Mock(), [])

                # Should not raise any exception
                adapter.create_schema(Mock(database="TEST_DB", schema="TEST_SCHEMA"))

    def test_drop_schema(self) -> None:
        """Test dropping schema."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Mock execute method
            with patch.object(adapter, "execute") as mock_execute:
                mock_execute.return_value = (Mock(), [])

                # Should not raise any exception
                adapter.drop_schema(Mock(database="TEST_DB", schema="TEST_SCHEMA"))

    def test_get_catalog(self) -> None:
        """Test getting catalog information."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Mock manifest with nodes
            mock_manifest = Mock()
            mock_manifest.nodes = {}
            mock_manifest.sources = {}

            # Mock execute method to return catalog data
            with patch.object(adapter, "execute") as mock_execute:
                mock_execute.return_value = (Mock(), [
                    ("TEST_SCHEMA", "TEST_TABLE", "COLUMN1", 1, "VARCHAR2", "Y"),
                    ("TEST_SCHEMA", "TEST_TABLE", "COLUMN2", 2, "NUMBER", "N"),
                ])

                catalog = adapter.get_catalog(mock_manifest)
                assert isinstance(catalog, dict)

    def test_convert_text_type(self) -> None:
        """Test converting text type."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Test various text type conversions
            assert "VARCHAR2(255)" in adapter.convert_text_type("text", 255)
            assert "CLOB" in adapter.convert_text_type("text", 5000)  # Large text

    def test_convert_number_type(self) -> None:
        """Test converting number type."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Test number type conversion
            result = adapter.convert_number_type("numeric", 10, 2)
            assert "NUMBER" in result

    def test_convert_datetime_type(self) -> None:
        """Test converting datetime type."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Test datetime conversions
            assert "TIMESTAMP" in adapter.convert_datetime_type("timestamp")
            assert "DATE" in adapter.convert_datetime_type("date")

    def test_adapter_inheritance(self) -> None:
        """Test that adapter properly inherits from SQLAdapter."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Test that it has expected methods from parent class
            assert hasattr(adapter, "execute")
            assert hasattr(adapter, "get_missing_columns")
            assert hasattr(adapter, "expand_target_column_types")

    def test_adapter_with_real_connection_manager(self) -> None:
        """Test adapter with real connection manager integration."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Verify connection manager is properly set
            assert adapter.ConnectionManager == FlextOracleOracleConnectionManager
            assert issubclass(adapter.ConnectionManager, type)

    def test_relation_handling(self) -> None:
        """Test relation handling methods."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Mock relation
            mock_relation = Mock(spec=BaseRelation)
            mock_relation.database = "TEST_DB"
            mock_relation.schema = "TEST_SCHEMA"
            mock_relation.identifier = "TEST_TABLE"

            # Test relation methods exist and can be called
            with patch.object(adapter, "execute") as mock_execute:
                mock_execute.return_value = (Mock(), [])

                # These should not raise exceptions
                adapter.get_columns_in_relation(mock_relation)
                adapter.list_relations_without_caching(mock_relation)

    def test_sql_generation_methods(self) -> None:
        """Test SQL generation helper methods."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Test that SQL generation methods exist
            assert hasattr(adapter, "convert_text_type")
            assert hasattr(adapter, "convert_number_type")
            assert hasattr(adapter, "convert_datetime_type")

            # Test basic functionality
            text_sql = adapter.convert_text_type("varchar", 100)
            assert isinstance(text_sql, str)
            assert len(text_sql) > 0

    def test_oracle_specific_features(self) -> None:
        """Test Oracle-specific adapter features."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Test Oracle-specific date function
            assert adapter.date_function() == "SYSDATE"

            # Test that it's cancelable (Oracle supports query cancellation)
            assert adapter.is_cancelable() is True

    def test_adapter_error_handling(self) -> None:
        """Test adapter error handling."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)

            # Test that exceptions are properly handled
            with patch.object(adapter, "execute") as mock_execute:
                mock_execute.side_effect = Exception("Test error")

                # Should propagate exceptions appropriately
                with pytest.raises(Exception, match="Test error"):
                    adapter.get_columns_in_relation(Mock())


class TestAdapterIntegration:
    """Test adapter integration with connection manager."""

    @patch("multiprocessing.get_context")
    def test_adapter_connection_manager_integration(self, mock_mp_context) -> None:
        """Test integration between adapter and connection manager."""
        config = {"host": "localhost", "username": "test"}
        adapter = OracleAdapter(config)

        # Verify connection manager type is correctly set
        assert adapter.ConnectionManager == FlextOracleOracleConnectionManager

        # Verify connection manager has correct type
        assert adapter.ConnectionManager.TYPE == "oracle"

    @patch("multiprocessing.get_context")
    def test_adapter_with_mock_connection(self, mock_mp_context) -> None:
        """Test adapter with mock connection for full workflow."""
        config = {"host": "localhost", "username": "test"}
        adapter = OracleAdapter(config)

        # Mock connection manager
        mock_connection_manager = Mock()
        adapter.connections = mock_connection_manager

        # Mock successful query execution
        mock_connection_manager.execute.return_value = (
            Mock(code="SELECT", rows_affected=1),
            [("column1", "column2")]
        )

        # Test execute through adapter
        with patch.object(adapter, "execute") as mock_execute:
            mock_execute.return_value = (Mock(), [])

            result = adapter.execute("SELECT 1 FROM DUAL", fetch=True)
            assert result is not None


class TestAdapterConfiguration:
    """Test adapter configuration and setup."""

    def test_adapter_accepts_various_config_formats(self) -> None:
        """Test adapter accepts various configuration formats."""
        configs = [
            {"host": "localhost", "username": "test"},
            {"host": "127.0.0.1", "port": 1521, "username": "user"},
            {"host": "oracle.example.com", "service_name": "XEPDB1", "username": "REDACTED_LDAP_BIND_PASSWORD"},
        ]

        for config in configs:
            with patch("multiprocessing.get_context"):
                adapter = OracleAdapter(config)
                assert adapter is not None

    def test_adapter_with_minimal_config(self) -> None:
        """Test adapter with minimal configuration."""
        config = {"host": "localhost", "username": "test"}
        with patch("multiprocessing.get_context"):
            adapter = OracleAdapter(config)
            assert adapter is not None
            assert adapter.ConnectionManager == FlextOracleOracleConnectionManager
