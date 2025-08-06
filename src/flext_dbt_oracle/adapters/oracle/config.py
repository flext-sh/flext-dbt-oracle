"""Configuration management for the DBT Oracle Adapter using flext-core patterns.

This module provides comprehensive configuration handling with validation,
type safety, and enterprise features using standardized flext-core patterns.
Enhanced to fully utilize flext-infrastructure.databases.flext-db-oracle
parameterization and modern typing.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from flext_core import FlextConstants, get_logger
from flext_db_oracle import FlextDbOracleConfig as OracleConfig
from pydantic import BaseModel, Field, SecretStr, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from .constants import DBTOracleAdapterConstants

if TYPE_CHECKING:
    from .types import (
        NonEmptyStr,
        Port,
        PositiveInt,
        TimeoutSeconds,
    )

logger = get_logger(__name__)


# ==============================================================================
# CONSTANTS - Imported from dedicated constants.py for maximum flext-core integration
# ==============================================================================
# All DBT Oracle Adapter constants are now centralized in ./constants.py
# This eliminates duplication and ensures flext-core compliance


# ==============================================================================
# DBT ORACLE SETTINGS - Using flext-core BaseSettings patterns
# ==============================================================================


class DBTOracleSettings(BaseSettings):
    """Modern DBT Oracle Settings using flext-core BaseSettings patterns.

    Provides environment variable integration, validation, and dependency injection
    using standardized flext-core patterns for enterprise configuration management.
    """

    model_config = SettingsConfigDict(
        env_prefix="DBT_ORACLE_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Project identification
    project_name: str = Field(
        default="flext-data.dbt.flext-dbt-oracle",
        description="Project name",
    )
    project_version: str = Field(default=FlextConstants.VERSION)

    # Oracle connection settings (directly defined)
    oracle_host: str = Field(..., description="Oracle database host")
    oracle_port: int = Field(1521, description="Oracle database port")
    oracle_service_name: str = Field(..., description="Oracle service name")
    oracle_sid: str | None = Field(
        None,
        description="Oracle SID (alternative to service_name)",
    )
    oracle_username: str = Field(..., description="Oracle username")
    oracle_password: str = Field(..., description="Oracle password")
    oracle_protocol: str = Field("tcp", description="Oracle protocol")
    oracle_pool_min_size: int = Field(1, description="Minimum pool size")
    oracle_pool_max_size: int = Field(10, description="Maximum pool size")
    oracle_query_timeout: int = Field(30, description="Query timeout in seconds")
    log_level: str = Field("INFO", description="Logging level")
    environment: str = Field("development", description="Environment")

    # DBT-specific settings
    database: str = Field(
        default="oracle",
        description="Oracle uses service/SID, not database concept",
    )
    schema_name: str = Field(
        default="SYSTEM",
        description="Default schema name",
    )
    materialization: str = Field(
        default=DBTOracleAdapterConstants.Materializations.DEFAULT,
        description="Default materialization strategy",
    )

    # Performance and logging now inherited from mixins

    # Model configuration for environment variables

    def to_dbt_config(self) -> DBTOracleConfig:
        """Convert settings to DBTOracleConfig.

        Returns:
            DBTOracleConfig instance with environment values

        """
        return DBTOracleConfig(
            host=self.oracle_host,
            port=self.oracle_port,
            service_name=self.oracle_service_name,
            sid=self.oracle_sid,
            username=self.oracle_username,
            password=self.oracle_password,
            protocol=self.oracle_protocol,
            database=self.database,
            schema_name=self.schema_name,
            materialization=self.materialization,
            pool_min_size=self.oracle_pool_min_size,
            pool_max_size=self.oracle_pool_max_size,
            query_timeout=self.oracle_query_timeout,
            log_level=self.log_level,
            project_name=self.project_name,
            project_version=self.project_version,
            environment=self.environment,
        )


class DBTOracleConfig(BaseModel):
    """Configuration for the DBT Oracle Adapter with comprehensive validation.

    Supports Oracle connection configuration and DBT-specific settings with
    enterprise-grade configuration management, validation, secrets handling,
    and environment variable integration.
    """

    # Project identification using flext-core patterns
    project_name: str = Field(
        default="flext-data.dbt.flext-dbt-oracle",
        description="Project name",
    )
    project_version: str = Field(
        default=FlextConstants.VERSION,
        description="Project version",
    )
    environment: str = Field(
        default="development",
        description="Environment name",
    )

    # Oracle Database connection using flext-core types
    host: NonEmptyStr = Field(
        ...,
        description="Oracle database host",
    )
    port: Port = Field(
        default=DBTOracleAdapterConstants.OracleDB.DEFAULT_PORT,
        description="Oracle database port",
    )
    service_name: NonEmptyStr | None = Field(
        default=DBTOracleAdapterConstants.OracleDB.DEFAULT_SERVICE_NAME,
        description="Oracle service name",
    )
    sid: NonEmptyStr | None = Field(
        default=None,
        description="Oracle SID (alternative to service_name)",
    )
    username: NonEmptyStr = Field(
        ...,
        description="Oracle username",
    )
    password: NonEmptyStr = Field(
        ...,
        description="Oracle password",
    )
    protocol: NonEmptyStr = Field(
        default=DBTOracleAdapterConstants.OracleDB.DEFAULT_PROTOCOL,
        description="Oracle protocol (tcp or tcps)",
    )

    # DBT-specific configuration using flext-core types
    database: str = "oracle"  # Oracle uses service/SID, not database concept
    schema_name: str = DBTOracleAdapterConstants.OracleDB.DEFAULT_SCHEMA
    materialization: str = Field(
        default=DBTOracleAdapterConstants.Materializations.DEFAULT,
        description="Default materialization strategy",
        pattern="^(table|view|incremental|snapshot)$",
    )

    # Connection pool configuration using flext-core types and constants
    pool_min_size: PositiveInt = Field(
        default=DBTOracleAdapterConstants.Performance.DEFAULT_POOL_MIN_SIZE,
        description="Connection pool minimum size",
        le=DBTOracleAdapterConstants.Performance.MAX_POOL_SIZE,
    )
    pool_max_size: PositiveInt = Field(
        default=DBTOracleAdapterConstants.Performance.DEFAULT_POOL_MAX_SIZE,
        description="Connection pool maximum size",
        le=DBTOracleAdapterConstants.Performance.MAX_POOL_SIZE,
    )
    pool_increment: PositiveInt = Field(
        default=1,
        description="Connection pool increment",
        le=10,
    )
    query_timeout: TimeoutSeconds = Field(
        default=DBTOracleAdapterConstants.OracleDB.DEFAULT_TIMEOUT,
        description="Query timeout in seconds",
        le=300,
    )
    fetch_size: PositiveInt = Field(
        default=DBTOracleAdapterConstants.Performance.DEFAULT_FETCH_SIZE,
        description="Default fetch size for queries",
    )
    connect_timeout: TimeoutSeconds = Field(
        default=DBTOracleAdapterConstants.OracleDB.DEFAULT_TIMEOUT,
        description="Connection timeout in seconds",
    )
    retry_attempts: PositiveInt = Field(
        default=DBTOracleAdapterConstants.ErrorHandling.DEFAULT_RETRY_ATTEMPTS,
        description="Number of retry attempts",
    )
    retry_delay: float = Field(
        default=DBTOracleAdapterConstants.ErrorHandling.DEFAULT_RETRY_DELAY,
        description="Retry delay in seconds",
        ge=0.1,
        le=10.0,
    )

    # Oracle-specific settings
    ssl_server_dn_match: bool = Field(
        default=False,
        description="Verify SSL server DN for secure connections",
    )
    nls_lang: NonEmptyStr | None = Field(
        default=None,
        description="Oracle NLS_LANG setting",
    )
    nls_date_format: NonEmptyStr = Field(
        default="YYYY-MM-DD HH24:MI:SS",
        description="Oracle NLS_DATE_FORMAT setting",
    )
    search_path: NonEmptyStr | None = Field(
        default=None,
        description="DBT search path for schemas",
    )

    # Advanced configuration
    enable_metrics: bool = Field(
        default=True,
        description="Enable detailed metrics collection",
    )

    # Logging and observability using flext-core constants
    log_level: str = Field(
        default="INFO",
        description="Logging level",
    )
    enable_sql_logging: bool = Field(
        default=False,
        description="Enable SQL query logging (can be verbose)",
    )

    # Configuration inherits from BaseConfig but customizes prefix
    class Config:
        """Pydantic configuration for Oracle adapter settings."""

        env_prefix = "DBT_ORACLE_"
        case_sensitive = False
        extra = "forbid"  # Prevent unknown configuration keys
        allow_population_by_field_name = True  # Allow field aliases

    @field_validator("materialization")
    @classmethod
    def validate_materialization(cls, v: str) -> str:
        """Validate materialization strategy using constants."""
        if v not in DBTOracleAdapterConstants.Materializations.VALID:
            msg = (
                f"Invalid materialization: {v}. Must be one of "
                f"{DBTOracleAdapterConstants.Materializations.VALID}"
            )
            raise ValueError(msg)
        return v

    @field_validator("protocol")
    @classmethod
    def validate_protocol(cls, v: str) -> str:
        """Validate protocol using constants."""
        if v not in {"tcp", "tcps"}:
            msg = (
                f"Invalid protocol: {v}. Must be one of "
                f"{{'tcp', 'tcps'}}"
            )
            raise ValueError(msg)
        return v

    @field_validator("host")
    @classmethod
    def validate_host_required(cls, v: str) -> str:
        """Validate host is provided."""
        if not v:
            msg = "Host is required"
            raise ValueError(msg)
        return v

    @field_validator("service_name")
    @classmethod
    def validate_service_name_or_sid(
        cls,
        v: str | None,
        info: ValidationInfo,
    ) -> str | None:
        """Validate either service_name or sid is provided."""
        if info.data:
            sid = info.data.get("sid")
            if not v and not sid:
                # Provide default service name for DBT
                return DBTOracleAdapterConstants.OracleDB.DEFAULT_SERVICE_NAME
        return v

    @field_validator("username")
    @classmethod
    def validate_username_required(cls, v: str) -> str:
        """Validate username is provided."""
        if not v:
            msg = "Username is required"
            raise ValueError(msg)
        return v

    @field_validator("password")
    @classmethod
    def validate_password_required(cls, v: str) -> str:
        """Validate password is provided."""
        if not v:
            msg = "Password is required"
            raise ValueError(msg)
        return v

    @field_validator("pool_max_size")
    @classmethod
    def validate_pool_sizes(cls, v: int, info: ValidationInfo) -> int:
        """Validate pool max size is greater than min size."""
        if info.data:
            min_size = info.data.get("pool_min_size", 1)
            if v < min_size:
                msg: str = (
                    f"Pool max size ({v}) must be greater than min size ({min_size})"
                )
                raise ValueError(
                    msg,
                )
        return v

    def get_connection_string(self) -> str:
        """Generate Oracle connection string for logging/display purposes.

        Returns:
            Connection string with masked password

        """
        # Prefer SID if provided explicitly, otherwise use service_name
        if self.sid:
            return f"oracle://{self.username}:***@{self.host}:{self.port}:{self.sid}"
        return (
            f"oracle://{self.username}:***@{self.host}:{self.port}/{self.service_name}"
        )

    def get_effective_schema(self) -> str:
        """Get the effective schema name.

        Returns:
            DBT schema name

        """
        return self.schema_name

    def get_database_identifier(self) -> str:
        """Get database identifier for flext-infrastructure.databases.flext-db-oracle.

        Returns:
            Database identifier (service_name, sid, or default)

        """
        return self.service_name or self.sid or "ORCL"

    def to_connection_config(self) -> dict[str, object]:
        """Convert to connection configuration for flext-infrastructure.databases.

        Convert to connection configuration for
        flext-infrastructure.databases.flext-db-oracle.

        Returns:
            Dictionary suitable for OracleConnection configuration

        """
        return {
            "host": self.host,
            "port": self.port,
            "service_name": self.service_name,
            "sid": self.sid,
            "username": self.username,
            "password": self.password,
            "protocol": self.protocol,
        }

    def to_oracle_config(self) -> OracleConfig:
        """Convert to modern flext-infrastructure.databases.flext-db-oracle OracleConfig.

        Convert to modern flext-infrastructure.databases.flext-db-oracle
        OracleConfig.

        Returns:
            OracleConfig instance with proper parameterization for DBT operations

        """
        # OracleConfig is always available from flext-db-oracle

        return OracleConfig(
            host=self.host,
            port=self.port,
            service_name=self.service_name,
            sid=self.sid,
            username=self.username,
            password=SecretStr(self.password),
            protocol=self.protocol,
            # Performance settings optimized for DBT analytical workloads
            pool_min=self.pool_min_size,
            pool_max=self.pool_max_size,
            pool_increment=self.pool_increment,
            timeout=int(self.query_timeout),
        )

    def get_performance_settings(self) -> dict[str, object]:
        """Get performance-related settings.

        Returns:
            Dictionary of performance configuration

        """
        return {
            "pool_min_size": self.pool_min_size,
            "pool_max_size": self.pool_max_size,
            "pool_increment": self.pool_increment,
            "query_timeout": self.query_timeout,
            "fetch_size": self.fetch_size,
            "connect_timeout": self.connect_timeout,
            "retry_attempts": self.retry_attempts,
            "retry_delay": self.retry_delay,
        }

    def get_dbt_settings(self) -> dict[str, object]:
        """Get DBT-specific settings.

        Returns:
            Dictionary of DBT configuration

        """
        return {
            "database": self.database,
            "schema": self.schema_name,
            "materialization": self.materialization,
            "search_path": self.search_path,
            "nls_lang": self.nls_lang,
            "nls_date_format": self.nls_date_format,
        }

    def validate_configuration(self) -> bool:
        """Perform comprehensive configuration validation for DBT Oracle Adapter.

        Returns:
            True if configuration is valid and complete

        Raises:
            ValueError: If configuration is invalid

        """
        try:
            # This will trigger all field validators
            self.__class__(**self.dict())

            # Validate DBT Oracle Adapter configuration completeness
            if not all([self.host, self.username, self.password]):
                self._raise_config_incomplete_error()

            # Validate either service_name or sid is provided
            if not self.service_name and not self.sid:
                # This is handled by the validator, but double-check
                self.service_name = DBTOracleAdapterConstants.OracleDB.DEFAULT_SERVICE_NAME

        except (RuntimeError, ValueError, TypeError):
            logger.exception("Configuration validation failed")
            raise
        else:
            logger.info("DBT Oracle Adapter configuration validation successful")
            return True

    def _raise_config_incomplete_error(self) -> None:
        """Raise error for incomplete DBT Oracle Adapter configuration."""
        msg = (
            "DBT Oracle Adapter configuration incomplete: host, username, and "
            "password are required"
        )
        raise ValueError(msg)


# Rebuild model after type imports are available
DBTOracleConfig.model_rebuild()


class OracleCredentialsConfig(DBTOracleConfig):
    """Configuration specifically for DBT credentials with additional validation.

    Extends DBTOracleConfig with DBT-specific credential requirements
    and compatibility features for the DBT framework.
    """

    # Additional DBT-required fields that may not be in base config
    type: str = Field(
        default="oracle",
        description="DBT adapter type",
        pattern="^oracle$",
    )

    # DBT credential aliases for compatibility
    _ALIASES: ClassVar[dict[str, str]] = {
        "dbname": "database",
        "pass": "password",
        "user": "username",
    }

    @property
    def unique_field(self) -> str:
        """Return unique identifier for connection.

        Returns:
            Host as unique identifier

        """
        return self.host

    def connection_keys(self) -> set[str]:
        """Return keys used for connection pooling.

        Returns:
            Set of keys that identify unique connections

        """
        return {
            "host",
            "port",
            "username",
            "password",
            "service_name",
            "sid",
            "protocol",
            "schema",
        }
