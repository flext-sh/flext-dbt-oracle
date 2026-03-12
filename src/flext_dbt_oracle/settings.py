"""Settings model used by DBT Oracle runtime components."""

from __future__ import annotations

from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    SecretStr,
    computed_field,
    model_validator,
)

# Re-export from connections.py to avoid duplication
from flext_dbt_oracle.connections import (
    OracleConnectionConfig,
    build_oracle_connection_config,
)
from flext_dbt_oracle.constants import c


class FlextDbtOracleSettings(BaseModel):
    """Configuration for DBT Oracle operations."""

    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    oracle_host: str = Field(
        default=c.Oracle.DEFAULT_HOST,
        description="Oracle database host",
    )
    oracle_username: str = Field(
        default="oracle",
        description="Oracle database username",
    )
    oracle_password: SecretStr = Field(
        default=SecretStr(""),
        description="Oracle database password",
    )
    oracle_port: int = Field(
        default=c.Oracle.DEFAULT_PORT,
        alias="port",
        ge=1,
        description="Oracle database port",
    )
    oracle_service_name: str = Field(
        default=c.Oracle.DEFAULT_SERVICE_NAME,
        description="Oracle service name",
    )

    sid: str | None = Field(default=None, description="Oracle SID (optional)")
    protocol: Literal["tcp", "tcps"] = Field(
        default="tcp",
        description="Connection protocol",
    )
    materialization: Literal["incremental", "snapshot", "table", "view"] = Field(
        default="table",
        description="DBT materialization strategy",
    )
    schema_name: str = Field(default="", description="Target schema name")
    ssl_server_dn_match: bool = Field(
        default=False,
        description="Enable SSL server DN validation",
    )
    nls_lang: str = Field(
        default=c.DbtOracle.NLS_LANG,
        description="Oracle NLS language setting",
    )
    nls_date_format: str = Field(
        default=c.DbtOracle.NLS_DATE_FORMAT,
        description="Oracle NLS date format",
    )
    search_path: str = Field(
        default="", description="Comma-separated schema search path"
    )
    enable_metrics: bool = Field(
        default=False,
        description="Enable metrics collection",
    )
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO",
        description="Runtime log verbosity",
    )
    enable_sql_logging: bool = Field(
        default=False,
        description="Enable SQL query logging",
    )

    # Connection pool settings
    pool_min_size: int = Field(default=1, ge=1, description="Minimum pool size")
    pool_max_size: int = Field(default=10, ge=1, description="Maximum pool size")
    pool_increment: int = Field(default=1, ge=1, description="Pool increment size")

    # Performance settings
    query_timeout: int = Field(
        default=300, ge=1, description="Query timeout in seconds"
    )
    fetch_size: int = Field(default=1000, ge=1, description="Fetch batch size")
    connect_timeout: int = Field(
        default=30, ge=1, description="Connection timeout in seconds"
    )
    retry_attempts: int = Field(default=3, ge=0, description="Number of retry attempts")
    retry_delay: int = Field(
        default=1, ge=0, description="Delay between retries in seconds"
    )
    retry_delay_seconds: float = Field(
        default=1.0,
        ge=0,
        description="Delay between retries in seconds",
    )

    @model_validator(mode="after")
    def validate_pool_sizes(self) -> FlextDbtOracleSettings:
        """Validate pool upper bound against minimum size."""
        if self.pool_max_size < self.pool_min_size:
            msg = "Pool max size must be greater than or equal to pool min size"
            raise ValueError(msg)
        return self

    @computed_field
    @property
    def port(self) -> int:
        """Return the Oracle port (alias for oracle_port)."""
        return self.oracle_port

    def get_database_identifier(self) -> str:
        """Return service name or SID identifier."""
        return self.sid or self.oracle_service_name

    def get_effective_schema(self) -> str:
        """Return the effective schema name."""
        return self.schema_name or self.oracle_username

    def get_connection_string(self) -> str:
        """Generate Oracle connection string."""
        identifier = self.get_database_identifier()
        separator = ":" if self.sid else "/"
        return (
            f"oracle://{self.oracle_username}:***@"
            f"{self.oracle_host}:{self.port}{separator}{identifier}"
        )

    def to_connection_config(self) -> dict[str, str | int | None]:
        """Convert to connection configuration dictionary."""
        return {
            "host": self.oracle_host,
            "port": self.port,
            "service_name": self.oracle_service_name,
            "sid": self.sid,
            "username": self.oracle_username,
            "password": self.oracle_password.get_secret_value(),
            "protocol": self.protocol,
        }

    def to_oracle_config(self) -> OracleConnectionConfig:
        """Convert to OracleConnectionConfig object."""
        return OracleConnectionConfig(
            host=self.oracle_host,
            port=self.port,
            username=self.oracle_username,
            password=self.oracle_password,
            service_name=self.oracle_service_name,
            sid=self.sid,
            protocol=self.protocol,
        )

    def get_performance_settings(self) -> dict[str, int]:
        """Return performance-related settings."""
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

    def get_dbt_settings(self) -> dict[str, str]:
        """Return DBT-specific settings."""
        return {
            "database": self.oracle_service_name,
            "schema": self.get_effective_schema(),
            "materialization": self.materialization,
        }


# Re-export for backward compatibility
__all__ = [
    "FlextDbtOracleSettings",
    "OracleConnectionConfig",
    "build_oracle_connection_config",
]
