"""DBT configuration for Oracle transformations.

Provides configuration management for DBT Oracle projects using flext-core patterns.
Integrates with flext-db-oracle for database operations and flext-meltano for DBT execution.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextSettings, get_logger
from flext_db_oracle import FlextDbOracleConfig
from flext_meltano.config import FlextMeltanoConfig
from pydantic import SecretStr

logger = get_logger(__name__)


class FlextDbtOracleConfig(FlextSettings):
    """Configuration for DBT Oracle transformations.

    Combines Oracle database settings with DBT execution configuration.
    Uses composition to integrate flext-db-oracle and flext-meltano configurations.
    """

    # Oracle Database Settings (from flext-db-oracle)
    oracle_host: str = ""
    oracle_port: int = 1521
    oracle_service_name: str = ""
    oracle_sid: str = ""
    oracle_username: str = ""
    oracle_password: str = ""
    oracle_protocol: str = "tcp"
    oracle_pool_min: int = 1
    oracle_pool_max: int = 10
    oracle_timeout: int = 30
    oracle_encoding: str = "utf-8"

    # DBT Execution Settings (from flext-meltano)
    dbt_project_dir: str = "."
    dbt_profiles_dir: str = "."
    dbt_target: str = "dev"
    dbt_threads: int = 4
    dbt_log_level: str = "info"
    dbt_schema: str = "analytics"

    # Oracle-specific DBT Settings
    oracle_schema_mapping: ClassVar[dict[str, str]] = {
        "raw_tables": "stg_raw_tables",
        "views": "stg_views",
        "sequences": "stg_sequences",
        "procedures": "stg_procedures",
        "functions": "stg_functions",
        "packages": "stg_packages",
        "triggers": "stg_triggers",
        "indexes": "stg_indexes",
    }

    oracle_column_mapping: ClassVar[dict[str, str]] = {
        "TABLE_NAME": "table_name",
        "COLUMN_NAME": "column_name",
        "DATA_TYPE": "data_type",
        "DATA_LENGTH": "data_length",
        "DATA_PRECISION": "data_precision",
        "DATA_SCALE": "data_scale",
        "NULLABLE": "nullable",
        "DATA_DEFAULT": "data_default",
        "OWNER": "schema_name",
        "OBJECT_NAME": "object_name",
        "OBJECT_TYPE": "object_type",
        "STATUS": "status",
        "CREATED": "created_date",
        "LAST_DDL_TIME": "last_modified_date",
    }

    # Data Quality Settings
    min_quality_threshold: float = 0.85
    required_oracle_objects: ClassVar[list[str]] = [
        "TABLE_NAME",
        "OWNER",
        "OBJECT_TYPE",
    ]
    validate_connections: bool = True
    max_parallel_connections: int = 5

    # Oracle Materialization Settings
    materialization_mapping: ClassVar[dict[str, str]] = {
        "staging": "view",
        "intermediate": "view",
        "marts": "table",
        "snapshots": "incremental",
    }

    # Oracle Performance Settings
    fetch_size: int = 10000
    batch_size: int = 1000
    enable_parallel_dml: bool = True
    optimizer_mode: str = "ALL_ROWS"

    # Oracle Data Type Mapping
    oracle_type_mapping: ClassVar[dict[str, str]] = {
        "VARCHAR2": "string",
        "NVARCHAR2": "string",
        "CHAR": "string",
        "NCHAR": "string",
        "CLOB": "string",
        "NCLOB": "string",
        "NUMBER": "numeric",
        "FLOAT": "float",
        "BINARY_FLOAT": "float",
        "BINARY_DOUBLE": "float",
        "DATE": "timestamp",
        "TIMESTAMP": "timestamp",
        "TIMESTAMP WITH TIME ZONE": "timestamp",
        "TIMESTAMP WITH LOCAL TIME ZONE": "timestamp",
        "INTERVAL YEAR TO MONTH": "string",
        "INTERVAL DAY TO SECOND": "string",
        "RAW": "string",
        "LONG RAW": "string",
        "BLOB": "string",
        "BFILE": "string",
        "ROWID": "string",
        "UROWID": "string",
    }

    def get_oracle_config(self) -> FlextDbOracleConfig:
        """Get Oracle configuration for flext-db-oracle integration."""
        return FlextDbOracleConfig(
            host=self.oracle_host,
            port=self.oracle_port,
            service_name=self.oracle_service_name,
            sid=self.oracle_sid,
            username=self.oracle_username,
            password=SecretStr(self.oracle_password),
            protocol=self.oracle_protocol,
            pool_min=self.oracle_pool_min,
            pool_max=self.oracle_pool_max,
            timeout=self.oracle_timeout,
            encoding=self.oracle_encoding,
        )

    def get_meltano_config(self) -> FlextMeltanoConfig:
        """Get Meltano configuration for flext-meltano integration."""
        return FlextMeltanoConfig(
            project_root=self.dbt_project_dir,
            environment=self.dbt_target,
        )

    def get_oracle_quality_config(self) -> dict[str, object]:
        """Get data quality configuration for Oracle validation."""
        return {
            "min_quality_threshold": self.min_quality_threshold,
            "required_oracle_objects": self.required_oracle_objects,
            "validate_connections": self.validate_connections,
            "max_parallel_connections": self.max_parallel_connections,
        }

    def get_performance_config(self) -> dict[str, object]:
        """Get Oracle performance configuration for DBT operations."""
        return {
            "fetch_size": self.fetch_size,
            "batch_size": self.batch_size,
            "enable_parallel_dml": self.enable_parallel_dml,
            "optimizer_mode": self.optimizer_mode,
        }

    def get_object_type_for_schema(self, object_type: str) -> str | None:
        """Get schema mapping for a given Oracle object type."""
        return self.oracle_schema_mapping.get(object_type.lower())

    def get_schema_for_object_type(self, object_type: str) -> str | None:
        """Get DBT schema name for a given Oracle object type."""
        return self.oracle_schema_mapping.get(object_type)

    def get_dbt_type_for_oracle_type(self, oracle_type: str) -> str:
        """Get DBT data type for Oracle data type."""
        oracle_type_upper = oracle_type.upper()

        # Handle parameterized types like VARCHAR2(100)
        if "(" in oracle_type_upper:
            base_type = oracle_type_upper.split("(")[0]
            return self.oracle_type_mapping.get(base_type, "string")

        return self.oracle_type_mapping.get(oracle_type_upper, "string")

    def get_materialization_for_layer(self, layer: str) -> str:
        """Get materialization strategy for DBT layer."""
        return self.materialization_mapping.get(layer, "view")

    def validate_oracle_connection(self) -> bool:
        """Validate Oracle connection configuration."""
        required_fields = [
            self.oracle_host,
            self.oracle_username,
            self.oracle_password,
        ]

        # Either service_name or sid must be provided
        has_connection_identifier = bool(self.oracle_service_name or self.oracle_sid)

        return all(required_fields) and has_connection_identifier


__all__: list[str] = [
    "FlextDbtOracleConfig",
]
