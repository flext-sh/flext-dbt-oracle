"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import threading
from pathlib import Path
from typing import ClassVar

from flext_meltano.config import FlextMeltanoConfig
from pydantic import Field, SecretStr, field_validator, model_validator

from flext_core import FlextConfig, FlextConstants, FlextLogger, FlextTypes
from flext_db_oracle import FlextDbOracleModels

logger = FlextLogger(__name__)


class FlextDbtOracleConfig(FlextConfig):
    """Configuration for DBT Oracle transformations.

    Follows standardized [Project]Config pattern:
    - Extends FlextConfig from flext-core
    - Uses SecretStr for sensitive data
    - All defaults from FlextConstants
    - Proper Pydantic 2 validation
    - Singleton pattern with proper typing

    Combines Oracle database settings with DBT execution configuration.
    """

    # Singleton pattern attributes
    _global_instance: ClassVar[FlextDbtOracleConfig | None] = None
    _lock: ClassVar[threading.Lock] = threading.Lock()

    # Oracle Database Configuration - using Field() with proper defaults
    oracle_host: str = Field(default=localhost, description="Oracle database host")

    oracle_port: int = Field(
        default=1521, ge=1, le=65535, description="Oracle database port"
    )

    oracle_service_name: str = Field(default="", description="Oracle service name")

    oracle_sid: str = Field(default="", description="Oracle SID")

    oracle_username: str = Field(default="", description="Oracle username")

    oracle_password: SecretStr = Field(
        default_factory=lambda: SecretStr(""), description="Oracle password (sensitive)"
    )

    oracle_protocol: str = Field(default=tcp, description="Oracle connection protocol")

    oracle_pool_min: int = Field(
        default=1, ge=1, description="Minimum Oracle connection pool size"
    )

    oracle_pool_max: int = Field(
        default=FlextConstants.Container.DEFAULT_WORKERS * 5,
        ge=1,
        description="Maximum Oracle connection pool size",
    )

    oracle_timeout: int = Field(
        default=FlextConstants.Network.DEFAULT_TIMEOUT,
        ge=1,
        description="Oracle connection timeout in seconds",
    )

    oracle_encoding: str = Field(
        default="utf-8", description="Oracle connection encoding"
    )

    # DBT Execution Configuration - using Field() with proper defaults
    dbt_project_dir: str = Field(default=".", description="DBT project directory")

    dbt_profiles_dir: str = Field(default=".", description="DBT profiles directory")

    dbt_target: str = Field(default=dev, description="DBT target environment")

    dbt_threads: int = Field(
        default=FlextConstants.Container.MAX_WORKERS,
        ge=1,
        description="Number of DBT threads",
    )

    dbt_log_level: str = Field(
        default=FlextConstants.Logging.DEFAULT_LEVEL, description="DBT logging level"
    )

    dbt_schema: str = Field(default=analytics, description="DBT default schema")

    # Data Quality Configuration
    min_quality_threshold: float = Field(
        default=0.85, ge=0.0, le=1.0, description="Minimum data quality threshold"
    )

    validate_connections: bool = Field(
        default=True, description="Enable connection validation"
    )

    max_parallel_connections: int = Field(
        default=5, ge=1, description="Maximum parallel Oracle connections"
    )

    # Oracle Performance Configuration
    fetch_size: int = Field(
        default=10000, ge=1, description="Oracle fetch size for queries"
    )

    batch_size: int = Field(
        default=1000, ge=1, description="Batch size for Oracle operations"
    )

    enable_parallel_dml: bool = Field(
        default=True, description="Enable Oracle parallel DML"
    )

    optimizer_mode: str = Field(default=ALL_ROWS, description="Oracle optimizer mode")

    # Oracle-specific mappings (ClassVar - not configurable)
    oracle_schema_mapping: ClassVar[FlextTypes.Core.Headers] = {
        "raw_tables": "stg_raw_tables",
        "views": "stg_views",
        "sequences": "stg_sequences",
        "procedures": "stg_procedures",
        "functions": "stg_functions",
        "packages": "stg_packages",
        "triggers": "stg_triggers",
        "indexes": "stg_indexes",
    }

    oracle_column_mapping: ClassVar[FlextTypes.Core.Headers] = {
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

    required_oracle_objects: ClassVar[FlextTypes.Core.StringList] = [
        "TABLE_NAME",
        "OWNER",
        "OBJECT_TYPE",
    ]

    materialization_mapping: ClassVar[FlextTypes.Core.Headers] = {
        "staging": "view",
        "intermediate": "view",
        "marts": "table",
        "snapshots": "incremental",
    }

    oracle_type_mapping: ClassVar[FlextTypes.Core.Headers] = {
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

    # Pydantic 2 field validators
    @field_validator("dbt_target")
    @classmethod
    def validate_dbt_target(cls, v: str) -> str:
        """Validate DBT target environment."""
        valid_targets = {
            "dev",
            "development",
            "staging",
            "prod",
            "production",
            "test",
            "local",
        }
        if v.lower() not in valid_targets:
            valid_list = ", ".join(sorted(valid_targets))
            msg = f"Invalid DBT target: {v}. Must be one of: {valid_list}"
            raise ValueError(msg)
        return v.lower()

    @field_validator("dbt_log_level")
    @classmethod
    def validate_dbt_log_level(cls, v: str) -> str:
        """Validate DBT log level."""
        if v.upper() not in FlextConstants.Logging.VALID_LEVELS:
            valid_levels = ", ".join(FlextConstants.Logging.VALID_LEVELS)
            msg = f"Invalid DBT log level: {v}. Must be one of: {valid_levels}"
            raise ValueError(msg)
        return v.upper()

    @field_validator("optimizer_mode")
    @classmethod
    def validate_optimizer_mode(cls, v: str) -> str:
        """Validate Oracle optimizer mode."""
        valid_modes = {
            "ALL_ROWS",
            "FIRST_ROWS",
            "FIRST_ROWS_1",
            "FIRST_ROWS_10",
            "FIRST_ROWS_100",
            "FIRST_ROWS_1000",
        }
        if v.upper() not in valid_modes:
            valid_list = ", ".join(sorted(valid_modes))
            msg = f"Invalid optimizer mode: {v}. Must be one of: {valid_list}"
            raise ValueError(msg)
        return v.upper()

    @model_validator(mode="after")
    def validate_oracle_connection_config(self) -> FlextDbtOracleConfig:
        """Validate Oracle connection configuration."""
        # Either service_name or sid must be provided
        if not self.oracle_service_name and not self.oracle_sid:
            msg = "Either oracle_service_name or oracle_sid must be provided"
            raise ValueError(msg)

        # Cannot have both service_name and sid
        if self.oracle_service_name and self.oracle_sid:
            msg = "Cannot specify both oracle_service_name and oracle_sid"
            raise ValueError(msg)

        return self

    # Configuration helper methods
    def get_oracle_config(self) -> FlextDbOracleModels.OracleConfig:
        """Get Oracle configuration for flext-db-oracle integration."""
        return FlextDbOracleModels.OracleConfig(
            host=self.oracle_host,
            port=self.oracle_port,
            service_name=self.oracle_service_name,
            sid=self.oracle_sid,
            username=self.oracle_username,
            password=self.oracle_password.get_secret_value(),
            pool_min=self.oracle_pool_min,
            pool_max=self.oracle_pool_max,
            timeout=self.oracle_timeout,
            domain_events=[],  # Initialize empty domain events list
        )

    def get_meltano_config(self) -> FlextMeltanoConfig:
        """Get Meltano configuration for flext-meltano integration."""
        # Map dbt_target to environment
        environment_mapping = {
            "dev": "development",
            "development": "development",
            "staging": "staging",
            "prod": "production",
            "production": "production",
            "test": "test",
            "local": "local",
        }

        environment = environment_mapping.get(self.dbt_target, "development")

        return FlextMeltanoConfig(
            project_root=Path(self.dbt_project_dir),
            environment=environment,
        )

    def get_oracle_quality_config(self) -> FlextTypes.Core.Dict:
        """Get data quality configuration for Oracle validation."""
        return {
            "min_quality_threshold": self.min_quality_threshold,
            "required_oracle_objects": self.required_oracle_objects,
            "validate_connections": self.validate_connections,
            "max_parallel_connections": self.max_parallel_connections,
        }

    def get_performance_config(self) -> FlextTypes.Core.Dict:
        """Get Oracle performance configuration."""
        return {
            "fetch_size": self.fetch_size,
            "batch_size": self.batch_size,
            "enable_parallel_dml": self.enable_parallel_dml,
            "optimizer_mode": self.optimizer_mode,
        }

    def get_dbt_config(self) -> FlextTypes.Core.Dict:
        """Get DBT configuration dictionary."""
        return {
            "project_dir": self.dbt_project_dir,
            "profiles_dir": self.dbt_profiles_dir,
            "target": self.dbt_target,
            "threads": self.dbt_threads,
            "log_level": self.dbt_log_level,
            "schema": self.dbt_schema,
        }

    # Utility methods for Oracle-DBT mapping
    def get_schema_for_object_type(self, object_type: str) -> str | None:
        """Get DBT schema name for Oracle object type."""
        return self.oracle_schema_mapping.get(object_type.lower())

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
        return self.materialization_mapping.get(layer.lower(), "view")

    def validate_oracle_connection(self) -> bool:
        """Validate Oracle connection configuration."""
        required_fields = [
            self.oracle_host,
            self.oracle_username,
            bool(self.oracle_password.get_secret_value()),
        ]

        # Either service_name or sid must be provided
        has_connection_identifier = bool(self.oracle_service_name or self.oracle_sid)

        return all(required_fields) and has_connection_identifier

    @classmethod
    def create_for_environment(
        cls, environment: str, **overrides: object
    ) -> FlextDbtOracleConfig:
        """Create configuration for specific environment."""
        env_overrides: dict[str, object] = {"dbt_target": "environment"}

        if environment == "production":
            env_overrides.update({
                "dbt_threads": min(4, FlextConstants.Container.MAX_WORKERS),
                "validate_connections": "True",
                "enable_parallel_dml": "True",
            })
        elif environment == "development":
            env_overrides.update({
                "dbt_threads": 1,
                "validate_connections": "False",
                "enable_parallel_dml": "False",
            })

        all_overrides = {**env_overrides, **overrides}
        # Pydantic BaseSettings handles kwargs validation and type conversion automatically
        return cls(**all_overrides)

    # Singleton pattern override for proper typing
    @classmethod
    def get_global_instance(cls) -> FlextDbtOracleConfig:
        """Get the global singleton instance of FlextDbtOracleConfig."""
        if cls._global_instance is None:
            with cls._lock:
                if cls._global_instance is None:
                    cls._global_instance = cls()
        return cls._global_instance

    @classmethod
    def reset_global_instance(cls) -> None:
        """Reset the global FlextDbtOracleConfig instance (mainly for testing)."""
        cls._global_instance = None


__all__: FlextTypes.Core.StringList = [
    "FlextDbtOracleConfig",
]
