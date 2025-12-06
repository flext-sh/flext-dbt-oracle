"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar, Self

from flext_core import FlextConfig, FlextResult
from flext_db_oracle import FlextDbOracleModels
from flext_meltano.config import FlextMeltanoConfig
from pydantic import Field, SecretStr, field_validator, model_validator
from pydantic_settings import SettingsConfigDict

from flext_dbt_oracle.constants import FlextDbtOracleConstants


@FlextConfig.auto_register("dbt_oracle")
class FlextDbtOracleConfig(FlextConfig.AutoConfig):
    """Configuration for DBT Oracle transformations.

    **ARCHITECTURAL PATTERN**: Zero-Boilerplate Auto-Registration

    This class uses FlextConfig.AutoConfig for automatic:
    - Singleton pattern (thread-safe)
    - Namespace registration (accessible via config.dbt_oracle)
    - Environment variable loading from FLEXT_DBT_ORACLE_* variables
    - .env file loading (production/development)
    - Automatic type conversion and validation via Pydantic v2

    Follows standardized [Project]Config pattern:
    - Uses SecretStr for sensitive data
    - All defaults from FlextConstants
    - Proper Pydantic 2 validation

    Combines Oracle database settings with DBT execution configuration.
    """

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_",
        case_sensitive=False,
        extra="allow",
        validate_assignment=True,
        arbitrary_types_allowed=True,
        populate_by_name=True,
        use_enum_values=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    # Oracle Database Configuration - using Field() with proper defaults
    oracle_host: str = Field(default="localhost", description="Oracle database host")

    oracle_port: int = Field(
        default=1521,
        ge=1,
        le=65535,
        description="Oracle database port",
    )

    oracle_service_name: str = Field(default="", description="Oracle service name")

    oracle_sid: str = Field(default="", description="Oracle SID")

    oracle_username: str = Field(default="", description="Oracle username")

    oracle_password: SecretStr = Field(
        default_factory=lambda: SecretStr(""),
        description="Oracle password (sensitive)",
    )

    oracle_protocol: str = Field(
        default="tcp",
        description="Oracle connection protocol",
    )

    oracle_pool_min: int = Field(
        default=2,
        ge=1,
        description="Minimum Oracle connection pool size",
    )

    oracle_pool_max: int = Field(
        default=20,
        ge=1,
        description="Maximum Oracle connection pool size",
    )

    oracle_timeout: int = Field(
        default=30,
        ge=1,
        description="Oracle connection timeout in seconds",
    )

    oracle_encoding: str = Field(
        default="utf-8",
        description="Oracle connection encoding",
    )

    # DBT Execution Configuration - using Field() with proper defaults
    dbt_project_dir: str = Field(default=".", description="DBT project directory")

    dbt_profiles_dir: str = Field(default=".", description="DBT profiles directory")

    dbt_target: str = Field(default="dev", description="DBT target environment")

    dbt_threads: int = Field(
        default=10,
        ge=1,
        description="Number of DBT threads",
    )

    dbt_log_level: FlextDbtOracleConstants.Literals.DbtLogLevelLiteral = Field(
        default="info",
        description="DBT logging level",
    )

    dbt_schema: str = Field(default="analytics", description="DBT default schema")

    # Data Quality Configuration
    min_quality_threshold: float = Field(
        default=0.8,
        ge=0.0,
        le=1.0,
        description="Minimum data quality threshold",
    )

    validate_connections: bool = Field(
        default=True,
        description="Enable connection validation",
    )

    max_parallel_connections: int = Field(
        default=4,
        ge=1,
        description="Maximum parallel Oracle connections",
    )

    # Oracle Performance Configuration
    fetch_size: int = Field(
        default=10000,
        ge=1,
        description="Oracle fetch size for queries",
    )

    batch_size: int = Field(
        default=1000,
        ge=1,
        description="Batch size for Oracle operations",
    )

    enable_parallel_dml: bool = Field(
        default=True,
        description="Enable Oracle parallel DML",
    )

    optimizer_mode: str = Field(default="ALL_ROWS", description="Oracle optimizer mode")

    # Oracle-specific mappings (ClassVar - not configurable)
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

    required_oracle_objects: ClassVar[list[str]] = [
        "TABLE_NAME",
        "OWNER",
        "OBJECT_TYPE",
    ]

    materialization_mapping: ClassVar[dict[str, str]] = {
        "staging": "view",
        "intermediate": "view",
        "marts": "table",
        "snapshots": "incremental",
    }

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
    def validate_oracle_connection_config(self) -> Self:
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

    def get_oracle_quality_config(self) -> dict[str, object]:
        """Get data quality configuration for Oracle validation."""
        return {
            "min_quality_threshold": self.min_quality_threshold,
            "required_oracle_objects": self.required_oracle_objects,
            "validate_connections": self.validate_connections,
            "max_parallel_connections": self.max_parallel_connections,
        }

    def get_performance_config(self) -> dict[str, object]:
        """Get Oracle performance configuration."""
        return {
            "fetch_size": self.fetch_size,
            "batch_size": self.batch_size,
            "enable_parallel_dml": self.enable_parallel_dml,
            "optimizer_mode": self.optimizer_mode,
        }

    def get_dbt_config(self) -> dict[str, object]:
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
    def create_for_development(cls, **overrides: object) -> FlextResult[Self]:
        """Create configuration optimized for development environment."""
        dev_config = {
            "dbt_target": "development",
            "dbt_threads": 1,
            "validate_connections": False,
            "enable_parallel_dml": False,
            "oracle_pool_min": 1,
            "oracle_pool_max": 2,
        }
        config_data = {**dev_config, **overrides}
        try:
            instance = cls.get_or_create_shared_instance(
                project_name="flext-dbt-oracle",
                **config_data,
            )
            return FlextResult[Self].ok(instance)
        except Exception as e:
            return FlextResult[Self].fail(f"Development config creation failed: {e}")

    @classmethod
    def create_for_production(cls, **overrides: object) -> FlextResult[Self]:
        """Create configuration optimized for production environment."""
        prod_config = {
            "dbt_target": "production",
            "dbt_threads": min(4, 10),
            "validate_connections": True,
            "enable_parallel_dml": True,
            "oracle_pool_min": 5,
            "oracle_pool_max": 20,
        }
        config_data = {**prod_config, **overrides}
        try:
            instance = cls.get_or_create_shared_instance(
                project_name="flext-dbt-oracle",
                **config_data,
            )
            return FlextResult[Self].ok(instance)
        except Exception as e:
            return FlextResult[Self].fail(f"Production config creation failed: {e}")

    @classmethod
    def create_for_testing(cls, **overrides: object) -> FlextResult[Self]:
        """Create configuration optimized for testing environment."""
        test_config = {
            "dbt_target": "test",
            "dbt_threads": 1,
            "validate_connections": False,
            "enable_parallel_dml": False,
            "oracle_pool_min": 1,
            "oracle_pool_max": 1,
            "min_quality_threshold": 0.5,  # Lower threshold for tests
        }
        config_data = {**test_config, **overrides}
        try:
            instance = cls.get_or_create_shared_instance(
                project_name="flext-dbt-oracle",
                **config_data,
            )
            return FlextResult[Self].ok(instance)
        except Exception as e:
            return FlextResult[Self].fail(f"Testing config creation failed: {e}")

    @classmethod
    def create_for_environment(
        cls,
        environment: str,
        **overrides: object,
    ) -> FlextResult[Self]:
        """Create configuration for specific environment."""
        if environment == "production":
            return cls.create_for_production(**overrides)
        if environment == "development":
            return cls.create_for_development(**overrides)
        if environment == "testing":
            return cls.create_for_testing(**overrides)
        return FlextResult[Self].fail(f"Unknown environment: {environment}")

    @classmethod
    def get_global_instance(cls) -> Self:
        """Get the global singleton instance using enhanced FlextConfig pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-dbt-oracle")

    @classmethod
    def reset_global_instance(cls) -> None:
        """Reset the global instance (mainly for testing)."""
        cls.reset_shared_instance(project_name="flext-dbt-oracle")


__all__: list[str] = [
    "FlextDbtOracleConfig",
]
