"""Settings model used by DBT Oracle runtime components."""

from __future__ import annotations

from collections.abc import Mapping
from flext_core import FlextSettings
from pydantic import BaseModel, Field, SecretStr, model_validator
from pydantic_settings import SettingsConfigDict

from flext_dbt_oracle.constants import c


class OracleConnectionConfig(BaseModel):
    """Minimal Oracle connection payload model."""

    host: str
    port: int
    service_name: str
    sid: str | None
    username: str
    password: str
    protocol: str


@FlextSettings.auto_register("dbt_oracle")
class FlextDbtOracleSettings(FlextSettings):
    """Validated configuration payload for Oracle and DBT operations."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_",
        case_sensitive=False,
        extra="ignore",
    )

    oracle_host: str
    oracle_username: str
    oracle_password: SecretStr
    oracle_service_name: str = c.Oracle.DEFAULT_SERVICE_NAME
    sid: str | None = None
    port: int = Field(default=c.Oracle.DEFAULT_PORT, ge=1)
    protocol: str = c.Oracle.DEFAULT_PROTOCOL
    schema_name: str = c.DbtOracle.DEFAULT_SCHEMA_NAME
    materialization: str = c.Dbt.Materialization.TABLE

    pool_min_size: int = Field(default=1, ge=1)
    pool_max_size: int = Field(default=10, ge=1)
    pool_increment: int = Field(default=1, ge=1)
    query_timeout: int = Field(default=300, ge=1)
    fetch_size: int = Field(default=1000, ge=1)
    connect_timeout: int = Field(default=30, ge=1)
    retry_attempts: int = Field(default=3, ge=0)
    retry_delay_seconds: float = Field(default=1.0, ge=0.0)

    ssl_server_dn_match: bool = False
    nls_lang: str = c.DbtOracle.NLS_LANG
    nls_date_format: str = c.DbtOracle.NLS_DATE_FORMAT
    search_path: str = ""
    enable_metrics: bool = True
    enable_sql_logging: bool = False

    dbt_project_dir: str = c.Dbt.DEFAULT_PROJECT_DIR
    dbt_profiles_dir: str = c.Dbt.DEFAULT_PROFILES_DIR
    dbt_target: str = c.Dbt.DEFAULT_TARGET
    dbt_threads: int = Field(default=c.Dbt.DEFAULT_THREADS, ge=1)

    @model_validator(mode="after")
    def validate_pool(self) -> FlextDbtOracleSettings:
        """Ensure pool sizes remain in a valid range."""
        if self.pool_max_size < self.pool_min_size:
            msg = "Pool max size must be greater than or equal to pool min size"
            raise ValueError(msg)
        return self

    @model_validator(mode="after")
    def validate_network_protocol(self) -> FlextDbtOracleSettings:
        """Validate supported Oracle network protocols."""
        if self.protocol not in {"tcp", "tcps"}:
            msg = "Invalid protocol"
            raise ValueError(msg)
        return self

    def get_database_identifier(self) -> str:
        """Return SID when configured, otherwise service name."""
        return self.sid or self.oracle_service_name

    def get_effective_schema(self) -> str:
        """Return effective schema used for DBT models."""
        return self.schema_name

    def get_connection_string(self) -> str:
        """Build masked connection string for logs and diagnostics."""
        identifier = self.get_database_identifier()
        separator = ":" if self.sid else "/"
        return (
            f"oracle://{self.oracle_username}:***@"
            f"{self.oracle_host}:{self.port}{separator}{identifier}"
        )

    def to_connection_config(self) -> Mapping[str, str | int | None]:
        """Serialize connection values into primitive dictionary payload."""
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
        """Convert runtime settings to OracleConnectionConfig."""
        return OracleConnectionConfig(
            host=self.oracle_host,
            port=self.port,
            service_name=self.oracle_service_name,
            sid=self.sid,
            username=self.oracle_username,
            password=self.oracle_password.get_secret_value(),
            protocol=self.protocol,
        )

    def get_performance_settings(self) -> Mapping[str, int | float]:
        """Return performance tuning parameters for execution engines."""
        return {
            "pool_min_size": self.pool_min_size,
            "pool_max_size": self.pool_max_size,
            "pool_increment": self.pool_increment,
            "query_timeout": self.query_timeout,
            "fetch_size": self.fetch_size,
            "connect_timeout": self.connect_timeout,
            "retry_attempts": self.retry_attempts,
            "retry_delay": self.retry_delay_seconds,
        }

    def get_dbt_settings(self) -> Mapping[str, str]:
        """Return DBT-targeted configuration payload."""
        return {
            "database": self.get_database_identifier(),
            "schema": self.get_effective_schema(),
            "materialization": self.materialization,
            "target": self.dbt_target,
        }


__all__ = ["FlextDbtOracleSettings"]
