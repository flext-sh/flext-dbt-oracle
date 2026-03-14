"""Configuration for FLEXT DBT Oracle tests.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import os
import tempfile
from collections.abc import Generator

import pytest
from flext_tests import FlextTestsDocker
from pydantic import TypeAdapter, ValidationError

_GENERAL_DICT_ADAPTER = TypeAdapter(dict[str, str | int | float | bool])


@pytest.fixture(scope="session")
def docker_control() -> FlextTestsDocker:
    """Provide FlextTestsDocker instance for container management."""
    return FlextTestsDocker()


def shared_oracle_container(docker_control: FlextTestsDocker) -> Generator[str]:
    """Start and maintain flext-oracle-db-test container.

    Container auto-starts if not running and remains running after tests.
    """
    result = docker_control.start_existing_container("flext-oracle-db-test")
    if result.is_failure:
        pytest.skip(f"Failed to start Oracle container: {result.error}")
    yield "flext-oracle-db-test"
    try:
        docker_control.get_client().containers.get("flext-oracle-db-test").stop()
    except (
        ValueError,
        TypeError,
        KeyError,
        AttributeError,
        OSError,
        RuntimeError,
        ImportError,
    ):
        pass


@pytest.fixture(scope="session", autouse=True)
def oracle_shared_container_environment() -> None:
    """Setup Oracle environment variables for shared container (pytest-oracle-xe)."""
    os.environ.update({
        "DBT_ORACLE_ORACLE_HOST": "localhost",
        "DBT_ORACLE_ORACLE_PORT": "10521",
        "DBT_ORACLE_ORACLE_USERNAME": "system",
        "DBT_ORACLE_ORACLE_PASSWORD": "oracle",
        "DBT_ORACLE_ORACLE_SERVICE_NAME": "XE",
        "DBT_ORACLE_ORACLE_SCHEMA": "FLEXT_TEST",
    })


@pytest.fixture(autouse=True)
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    os.environ["FLEXT_ENV"] = "test"
    os.environ["FLEXT_LOG_LEVEL"] = "debug"
    temp_dir = tempfile.mkdtemp(prefix="dbt_profiles_")
    os.environ["DBT_PROFILES_DIR"] = temp_dir
    os.environ["DBT_TEST_USER_1"] = "dbt_test_user_1"
    os.environ["DBT_TEST_USER_2"] = "dbt_test_user_2"
    os.environ["DBT_TEST_USER_3"] = "dbt_test_user_3"
    yield
    _ = os.environ.pop("FLEXT_ENV", None)
    _ = os.environ.pop("FLEXT_LOG_LEVEL", None)
    _ = os.environ.pop("DBT_PROFILES_DIR", None)
    _ = os.environ.pop("DBT_TEST_USER_1", None)
    _ = os.environ.pop("DBT_TEST_USER_2", None)
    _ = os.environ.pop("DBT_TEST_USER_3", None)


@pytest.fixture
def dbt_oracle_profile() -> dict[str, object]:
    """Dbt Oracle profile configuration for testing."""
    return {
        "config": {
            "partial_parse": True,
            "printer_width": 120,
            "send_anonymous_usage_stats": False,
            "use_colors": True,
        },
        "test": {
            "outputs": {
                "default": {
                    "type": "oracle",
                    "host": "localhost",
                    "port": 1521,
                    "database": "XEPDB1",
                    "schema": "DBT_TEST",
                    "user": "dbt_test_user",
                    "password": "dbt_test_pass",
                    "protocol": "tcp",
                    "service": "XEPDB1",
                    "threads": 4,
                    "keepalives_idle": 0,
                    "search_path": "DBT_TEST",
                },
                "ci": {
                    "type": "oracle",
                    "host": "oracle-ci.test.com",
                    "port": 1521,
                    "database": "CIDB",
                    "schema": "DBT_CI",
                    "user": "{{ env_var('DBT_TEST_USER_1') }}",
                    "password": "{{ env_var('DBT_TEST_PASS_1') }}",
                    "service": "CIDB",
                    "threads": 2,
                },
            },
            "target": "default",
        },
    }


@pytest.fixture
def dbt_project_config() -> dict[str, object]:
    """Dbt project configuration for testing."""
    return {
        "name": "flext_dbt_oracle_test",
        "version": "0.9.0",
        "profile": "test",
        "model-paths": ["models"],
        "analysis-paths": ["analyses"],
        "test-paths": ["tests"],
        "seed-paths": ["seeds"],
        "macro-paths": ["macros"],
        "snapshot-paths": ["snapshots"],
        "docs-paths": ["docs"],
        "asset-paths": ["assets"],
        "target-path": "target",
        "clean-targets": ["target", "dbt_packages"],
        "require-dbt-version": ">=1.8.0",
        "model_config": {
            "materialized": "table",
            "oracle": {"tablespace": "USERS", "compression": "NONE", "parallel": 4},
        },
        "vars": {
            "test_schema": "DBT_TEST",
            "test_database": "XEPDB1",
            "enable_oracle_features": True,
        },
    }


@pytest.fixture
def oracle_adapter_config() -> dict[str, object]:
    """Oracle adapter configuration for testing."""
    return {
        "type": "oracle",
        "host": "localhost",
        "port": 1521,
        "database": "XEPDB1",
        "schema": "DBT_TEST",
        "user": "dbt_test_user",
        "password": "dbt_test_pass",
        "service": "XEPDB1",
        "protocol": "tcp",
        "threads": 4,
        "keepalives_idle": 0,
        "search_path": "DBT_TEST",
        "oracle_features": {
            "enable_merge": True,
            "enable_parallel": True,
            "enable_hints": True,
            "enable_compression": False,
        },
    }


@pytest.fixture
def dbt_model_definitions() -> dict[str, str]:
    """Dbt model SQL definitions for testing."""
    return {
        "staging_customers": "\n\n          {{ config(materialized='view') }}\n          SELECT\n              customer_id,\n              customer_name,\n              customer_email,\n              created_at,\n              updated_at\n          FROM {{ source('raw', 'customers') }}\n          WHERE customer_id IS NOT NULL\n      ",
        "dim_customers": "\n\n          {{ config(\n              materialized='table',\n              oracle={'tablespace': 'USERS', 'parallel': 2}\n          ) }}\n          SELECT\n              customer_id,\n              customer_name,\n              customer_email,\n              CASE\n                  WHEN customer_email LIKE '%@%.%' THEN 'valid'\n                  ELSE 'invalid'\n              END as email_status,\n              created_at,\n              updated_at,\n              CURRENT_TIMESTAMP as dbt_updated_at\n          FROM {{ ref('staging_customers') }}\n      ",
        "fact_orders": "\n\n          {{ config(\n              materialized='incremental',\n              unique_key='order_id',\n              oracle={'merge_update_columns': ['order_status', 'total_amount']}\n          ) }}\n          SELECT\n              order_id,\n              customer_id,\n              order_date,\n              order_status,\n              total_amount,\n              created_at,\n              updated_at\n          FROM {{ source('raw', 'orders') }}\n          {% if is_incremental() %}\n              WHERE updated_at > (SELECT MAX(updated_at) FROM {{ this }})\n          {% endif %}\n      ",
    }


@pytest.fixture
def dbt_macro_definitions() -> dict[str, str]:
    """Dbt macro definitions for testing."""
    return {
        "oracle_create_table_as": "\n\n          {% macro oracle_create_table_as(temporary, relation, sql) -%}\n              {% if temporary %}\n                  CREATE GLOBAL TEMPORARY TABLE {{ relation }}\n                  ON COMMIT PRESERVE ROWS\n                  AS (\n                      {{ sql }}\n                  )\n              {% else %}\n                  CREATE TABLE {{ relation }}\n                  {% if config.get('oracle', {}).get('tablespace') %}\n                      TABLESPACE {{ config.get('oracle', {}).get('tablespace') }}\n                  {% endif %}\n                  {% if config.get('oracle', {}).get('parallel') %}\n                      PARALLEL {{ config.get('oracle', {}).get('parallel') }}\n                  {% endif %}\n                  AS (\n                      {{ sql }}\n                  )\n              {% endif %}\n          {%- endmacro %}\n      ",
        "oracle_merge_sql": "\n\n          {% macro oracle_merge_sql(target, source, unique_key, dest_columns) -%}\n              MERGE INTO {{ target }} AS target_table\n              USING ({{ source }}) AS source_table\n              ON (target_table.{{ unique_key }} = source_table.{{ unique_key }})\n              WHEN MATCHED THEN\n                  UPDATE SET\n                  {% for column in dest_columns %}\n                      {{ column }} = source_table.{{ column }}\n                      {%- if not loop.last -%},{%- endif %}\n                  {% endfor %}\n              WHEN NOT MATCHED THEN\n                  INSERT ({{ Union[dest_columns, join](', ') }})\n                  VALUES ({{\n                      Union[dest_columns, map]('prepend', 'source_table.') | join(', ')\n                  }})\n          {%- endmacro %}\n      ",
    }


@pytest.fixture
def dbt_test_definitions() -> dict[str, str]:
    """Dbt test definitions for testing."""
    return {
        "test_unique_customer_id": "\n\n          SELECT customer_id, COUNT(*)\n          FROM {{ ref('dim_customers') }}\n          GROUP BY customer_id\n          HAVING COUNT(*) > 1\n      ",
        "test_not_null_order_id": "\n\n          SELECT *\n          FROM {{ ref('fact_orders') }}\n          WHERE order_id IS NULL\n      ",
        "test_valid_email_format": "\n\n          SELECT *\n          FROM {{ ref('dim_customers') }}\n          WHERE email_status = 'invalid'\n          AND customer_email IS NOT NULL\n      ",
    }


@pytest.fixture
def dbt_source_definitions() -> dict[str, object]:
    """Dbt source definitions for testing."""
    return {
        "version": 2,
        "sources": [
            {
                "name": "raw",
                "description": "Raw data from Oracle source system",
                "tables": [
                    {
                        "name": "customers",
                        "description": "Customer master data",
                        "columns": [
                            {
                                "name": "customer_id",
                                "description": "Unique customer identifier",
                                "tests": ["unique", "not_null"],
                            },
                            {
                                "name": "customer_name",
                                "description": "Customer full name",
                                "tests": ["not_null"],
                            },
                            {
                                "name": "customer_email",
                                "description": "Customer email address",
                            },
                        ],
                    },
                    {
                        "name": "orders",
                        "description": "Order transaction data",
                        "columns": [
                            {
                                "name": "order_id",
                                "description": "Unique order identifier",
                                "tests": ["unique", "not_null"],
                            },
                            {
                                "name": "customer_id",
                                "description": "Customer identifier",
                                "tests": ["not_null"],
                            },
                        ],
                    },
                ],
            }
        ],
    }


@pytest.fixture
def oracle_sql_queries() -> dict[str, str]:
    """Oracle SQL queries for testing."""
    return {
        "create_test_schema": "\n\n          CREATE USER DBT_TEST IDENTIFIED BY dbt_test_pass\n          DEFAULT TABLESPACE USERS\n          TEMPORARY TABLESPACE TEMP\n          QUOTA UNLIMITED ON USERS\n      ",
        "grant_permissions": "\n\n          GRANT CONNECT, RESOURCE, CREATE VIEW, CREATE PROCEDURE TO DBT_TEST\n      ",
        "create_customers_table": "\n\n          CREATE TABLE DBT_TEST.customers (\n              customer_id NUMBER(10) PRIMARY KEY,\n              customer_name VARCHAR2(100) NOT NULL,\n              customer_email VARCHAR2(255),\n              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n              updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n          )\n      ",
        "create_orders_table": "\n\n          CREATE TABLE DBT_TEST.orders (\n              order_id NUMBER(10) PRIMARY KEY,\n              customer_id NUMBER(10) NOT NULL,\n              order_date DATE NOT NULL,\n              order_status VARCHAR2(20) DEFAULT 'pending',\n              total_amount NUMBER(10,2),\n              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n              updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n              CONSTRAINT fk_orders_customer\n                  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)\n          )\n      ",
        "insert_test_data": "\n\n          INSERT ALL\n              INTO customers VALUES (1, 'John Doe', 'john@example.com',\n                  SYSTIMESTAMP, SYSTIMESTAMP)\n              INTO customers VALUES (2, 'Jane Smith', 'jane@example.com',\n                  SYSTIMESTAMP, SYSTIMESTAMP)\n              INTO orders VALUES (1, 1, SYSDATE, 'completed', 99.99,\n                  SYSTIMESTAMP, SYSTIMESTAMP)\n              INTO orders VALUES (2, 2, SYSDATE, 'pending', 149.99,\n                  SYSTIMESTAMP, SYSTIMESTAMP)\n          SELECT * FROM dual\n      ",
    }


@pytest.fixture
def dbt_run_config() -> dict[str, object]:
    """Dbt run configuration for testing."""
    return {
        "threads": 4,
        "target": "default",
        "models": ["dim_customers", "fact_orders"],
        "exclude": ["staging_*"],
        "vars": {"start_date": "2023-01-01", "end_date": "2023-12-31"},
        "full_refresh": False,
    }


@pytest.fixture
def dbt_test_config() -> dict[str, object]:
    """Dbt test configuration for testing."""
    return {
        "threads": 2,
        "target": "default",
        "models": ["dim_customers"],
        "data": True,
        "schema": True,
        "store_failures": True,
    }


@pytest.fixture
def performance_test_config() -> dict[str, object]:
    """Performance test configuration."""
    return {
        "large_table_rows": 100000,
        "concurrent_models": 5,
        "memory_threshold": "2GB",
        "execution_time_threshold": 300,
        "parallel_threads": [1, 2, 4, 8],
    }


@pytest.fixture
def dbt_error_scenarios() -> list[dict[str, object]]:
    """Dbt error scenarios for testing."""
    return [
        {
            "name": "connection_failure",
            "error_type": "DatabaseConnectionError",
            "cause": "invalid_credentials",
            "expected_behavior": "fail_fast",
        },
        {
            "name": "compilation_error",
            "error_type": "CompilationError",
            "cause": "invalid_sql_syntax",
            "expected_behavior": "detailed_error_message",
        },
        {
            "name": "runtime_error",
            "error_type": "RuntimeError",
            "cause": "table_not_found",
            "expected_behavior": "graceful_failure",
        },
        {
            "name": "permission_error",
            "error_type": "DatabaseError",
            "cause": "insufficient_privileges",
            "expected_behavior": "clear_error_message",
        },
    ]


def pytest_configure(config: pytest.Config) -> None:
    """Configure pytest markers."""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "e2e: End-to-end tests")
    config.addinivalue_line("markers", "dbt: dbt-specific tests")
    config.addinivalue_line("markers", "oracle: Oracle database tests")
    config.addinivalue_line("markers", "adapter: Adapter functionality tests")
    config.addinivalue_line("markers", "materialization: Materialization tests")
    config.addinivalue_line("markers", "macro: Macro tests")
    config.addinivalue_line("markers", "slow: Slow tests")


class MockConnectionManager:
    """Strategy for connection management (Single Responsibility Principle)."""

    def __init__(self) -> None:
        """Initialize connection manager."""
        super().__init__()
        self.connections: dict[str, dict[str, object]] = {}

    def open_connection(
        self, name: str, config: dict[str, object]
    ) -> dict[str, object]:
        """Open database connection."""
        connection: dict[str, object] = {
            "name": name,
            "state": "open",
            "handle": f"mock_handle_{name}",
            "credentials": config,
        }
        self.connections[name] = connection
        return connection

    def close_connection(self, name: str) -> None:
        """Close database connection."""
        if name in self.connections:
            self.connections[name]["state"] = "closed"
            del self.connections[name]


class MockSqlExecutor:
    """Strategy for SQL execution (Strategy Pattern)."""

    def execute(self, sql: str, *, auto_begin: bool = True) -> tuple[str, list]:
        """Execute SQL statement with reduced branching."""
        _ = auto_begin
        sql_strategies: dict[str, tuple[str, list]] = {
            "CREATE TABLE": ("CREATE", []),
            "INSERT": ("INSERT", []),
            "SELECT": ("SELECT", [{"column1": "value1", "column2": "value2"}]),
        }
        for keyword, result in sql_strategies.items():
            if keyword in sql:
                return result
        return ("UNKNOWN", [])


class MockModelCompiler:
    """Strategy for model compilation (Single Responsibility Principle)."""

    def compile_model(self, model_sql: str, context: dict[str, object]) -> str:
        """Compile dbt model SQL."""
        compiled = model_sql
        vars_value = context.get("vars", {})
        vars_dict: dict[str, str | int | float | bool]
        try:
            vars_dict = _GENERAL_DICT_ADAPTER.validate_python(vars_value)
        except ValidationError:
            vars_dict = {}
        for var, value in vars_dict.items():
            compiled = compiled.replace(f"{{{{ var('{var}') }}}}", str(value))
        return compiled


class MockRelationManager:
    """Strategy for relation management (Single Responsibility Principle)."""

    def get_relation(
        self, database: str, schema: str, identifier: str
    ) -> dict[str, str]:
        """Get relation information."""
        return {
            "database": database,
            "schema": schema,
            "identifier": identifier,
            "type": "table",
        }

    def list_relations_without_caching(self, schema: str) -> list[dict[str, str]]:
        """List relations in schema."""
        return [
            {"schema": schema, "identifier": "customers", "type": "table"},
            {"schema": schema, "identifier": "orders", "type": "table"},
        ]


class MockDbtOracleAdapter:
    """Simplified adapter using composition and Strategy Pattern."""

    def __init__(self, config: dict[str, object]) -> None:
        """Initialize the instance."""
        super().__init__()
        self.config = config
        self.compiled_models: dict[str, object] = {}
        self.connection_manager = MockConnectionManager()
        self.sql_executor = MockSqlExecutor()
        self.model_compiler = MockModelCompiler()
        self.relation_manager = MockRelationManager()

    def open_connection(self, name: str) -> dict[str, object]:
        """Delegate to connection manager strategy."""
        return self.connection_manager.open_connection(name, self.config)

    def close_connection(self, name: str) -> None:
        """Delegate to connection manager strategy."""
        self.connection_manager.close_connection(name)

    def execute(self, sql: str, *, auto_begin: bool = True) -> tuple[str, list]:
        """Delegate to SQL executor strategy."""
        return self.sql_executor.execute(sql, auto_begin=auto_begin)

    def compile_model(self, model_sql: str, context: dict[str, object]) -> str:
        """Delegate to model compiler strategy."""
        return self.model_compiler.compile_model(model_sql, context)

    def get_relation(
        self, database: str, schema: str, identifier: str
    ) -> dict[str, str]:
        """Delegate to relation manager strategy."""
        return self.relation_manager.get_relation(database, schema, identifier)

    def list_relations_without_caching(self, schema: str) -> list[dict[str, str]]:
        """Delegate to relation manager strategy."""
        return self.relation_manager.list_relations_without_caching(schema)


@pytest.fixture
def mock_dbt_oracle_adapter() -> type[MockDbtOracleAdapter]:
    """Mock dbt Oracle adapter using Strategy Pattern for complexity reduction."""
    return MockDbtOracleAdapter


class MockDbtRunner:
    """Mock dbt runner."""

    def __init__(self, project_dir: str, profiles_dir: str) -> None:
        """Initialize the instance."""
        super().__init__()
        self.project_dir = project_dir
        self.profiles_dir = profiles_dir
        self.results: dict[str, object] = {}

    def run_models(self, models: list[str] | None = None) -> dict[str, object]:
        """Run dbt models."""
        results: list[dict[str, object]] = []
        models = models or ["dim_customers", "fact_orders"]
        for model in models:
            result: dict[str, object] = {
                "unique_id": f"model.test.{model}",
                "status": "success",
                "execution_time": 2.5,
                "rows_affected": 1000,
            }
            results.append(result)
        return {"results": results, "elapsed_time": 10.5}

    def run_tests(self, models: list[str] | None = None) -> dict[str, object]:
        """Run dbt tests."""
        _ = models
        results: list[dict[str, object]] = []
        tests = ["test_unique_customer_id", "test_not_null_order_id"]
        for test in tests:
            result: dict[str, object] = {
                "unique_id": f"test.test.{test}",
                "status": "pass",
                "execution_time": 1.2,
                "failures": 0,
            }
            results.append(result)
        return {"results": results, "elapsed_time": 5.0}

    def compile(self, models: list[str] | None = None) -> dict[str, object]:
        """Compile dbt models."""
        compiled: dict[str, str] = {}
        models = models or ["dim_customers", "fact_orders"]
        for model in models:
            compiled[model] = f"SELECT * FROM compiled_{model}"
        return {"compiled": compiled}


@pytest.fixture
def mock_dbt_runner() -> type[MockDbtRunner]:
    """Mock dbt runner for testing."""
    return MockDbtRunner
