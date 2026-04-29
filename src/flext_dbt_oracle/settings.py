"""Settings for DBT Oracle runtime components."""

from __future__ import annotations

from typing import Annotated, ClassVar, Literal

from flext_core import FlextSettings, m, u
from flext_dbt_oracle import c, t
from flext_dbt_oracle.models import FlextDbtOracleModels


@FlextSettings.auto_register("dbt_oracle")
class FlextDbtOracleSettings(FlextSettings):
    """DBT Oracle pipeline configuration."""

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_",
        extra="ignore",
        populate_by_name=True,
    )

    oracle_host: Annotated[
        str,
        u.Field(description="Oracle database host"),
    ] = c.DbtOracle.Oracle.DEFAULT_HOST
    oracle_username: Annotated[
        str,
        u.Field(description="Oracle database username"),
    ] = "oracle"
    oracle_password: Annotated[
        t.SecretStr,
        u.Field(description="Oracle database password"),
    ] = t.SecretStr("")
    oracle_port: Annotated[
        t.PortNumber,
        u.Field(description="Oracle database port"),
    ] = c.DbtOracle.Oracle.DEFAULT_PORT
    oracle_service_name: Annotated[
        str,
        u.Field(description="Oracle service name"),
    ] = c.DbtOracle.Oracle.DEFAULT_SERVICE_NAME

    sid: Annotated[
        str | None,
        u.Field(description="Oracle SID (optional)"),
    ] = None
    protocol: Annotated[
        Literal["tcp", "tcps"],
        u.Field(description="Connection protocol"),
    ] = "tcp"
    materialization: Annotated[
        c.DbtOracle.Dbt.Materialization,
        u.Field(description="DBT materialization strategy"),
    ] = c.DbtOracle.Dbt.Materialization.TABLE
    schema_name: Annotated[
        str,
        u.Field(description="Target schema name"),
    ] = ""
    ssl_server_dn_match: Annotated[
        bool,
        u.Field(description="Enable SSL server DN validation"),
    ] = False
    nls_lang: Annotated[
        str,
        u.Field(description="Oracle NLS language setting"),
    ] = c.DbtOracle.NLS_LANG
    nls_date_format: Annotated[
        str,
        u.Field(description="Oracle NLS date format"),
    ] = c.DbtOracle.NLS_DATE_FORMAT
    search_path: Annotated[
        str,
        u.Field(description="Schema search path"),
    ] = ""
    enable_metrics: Annotated[
        bool,
        u.Field(description="Enable metrics collection"),
    ] = False
    log_level: Annotated[
        c.LogLevel,
        u.Field(description="Runtime log verbosity"),
    ] = c.LogLevel.INFO
    enable_sql_logging: Annotated[
        bool,
        u.Field(description="Enable SQL query logging"),
    ] = False

    # Connection pool settings
    pool_min_size: Annotated[
        t.PositiveInt,
        u.Field(description="Minimum pool size"),
    ] = 1
    pool_max_size: Annotated[
        t.PositiveInt,
        u.Field(description="Maximum pool size"),
    ] = 10
    pool_increment: Annotated[
        t.PositiveInt,
        u.Field(description="Pool increment size"),
    ] = 1

    # Performance settings
    query_timeout: Annotated[
        t.PositiveInt,
        u.Field(description="Query timeout in seconds"),
    ] = 300
    fetch_size: Annotated[
        t.PositiveInt,
        u.Field(description="Fetch batch size"),
    ] = 1000
    connect_timeout: Annotated[
        t.PositiveInt,
        u.Field(description="Connection timeout in seconds"),
    ] = 30
    retry_attempts: Annotated[
        t.NonNegativeInt,
        u.Field(description="Number of retry attempts"),
    ] = 3
    retry_delay: Annotated[
        t.NonNegativeInt,
        u.Field(description="Delay between retries"),
    ] = 1
    retry_delay_seconds: Annotated[
        t.NonNegativeFloat,
        u.Field(description="Delay between retries in seconds"),
    ] = 1.0

    @u.model_validator(mode="after")
    def validate_pool_sizes(self) -> FlextDbtOracleSettings:
        """Validate pool upper bound against minimum."""
        if self.pool_max_size < self.pool_min_size:
            msg = "Pool max size must be >= pool min size"
            raise ValueError(msg)
        return self

    @u.computed_field(return_type=int)
    @property
    def port(self) -> int:
        """Return the Oracle port."""
        return self.oracle_port

    @u.computed_field(return_type=str)
    @property
    def database_identifier(self) -> str:
        """Service name or SID identifier."""
        return self.sid or self.oracle_service_name

    @u.computed_field(return_type=str)
    @property
    def effective_schema(self) -> str:
        """Effective schema name."""
        return self.schema_name or self.oracle_username

    @u.computed_field(return_type=str)
    @property
    def connection_string(self) -> str:
        """Oracle connection string."""
        identifier = self.database_identifier
        separator = ":" if self.sid else "/"
        return (
            f"oracle://{self.oracle_username}:***@"
            f"{self.oracle_host}:{self.port}"
            f"{separator}{identifier}"
        )

    def to_connection_config(self) -> dict[str, str | int | None]:
        """Convert to connection configuration dict."""
        return {
            "host": self.oracle_host,
            "port": self.port,
            "service_name": self.oracle_service_name,
            "sid": self.sid,
            "username": self.oracle_username,
            "password": self.oracle_password.get_secret_value(),
            "protocol": self.protocol,
        }

    def to_oracle_config(self) -> FlextDbtOracleModels.DbtOracle.OracleConnectionConfig:
        """Convert to OracleConnectionConfig."""
        return FlextDbtOracleModels.DbtOracle.OracleConnectionConfig(
            host=self.oracle_host,
            port=self.port,
            username=self.oracle_username,
            password=self.oracle_password,
            service_name=self.oracle_service_name,
            sid=self.sid,
            protocol=self.protocol,
        )

    @u.computed_field(return_type=t.IntMapping)
    @property
    def performance_settings(self) -> t.IntMapping:
        """Performance-related settings."""
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

    @u.computed_field(return_type=t.StrMapping)
    @property
    def dbt_settings(self) -> t.StrMapping:
        """DBT-specific settings."""
        return {
            "database": self.oracle_service_name,
            "schema": self.effective_schema,
            "materialization": self.materialization,
        }


__all__: list[str] = ["FlextDbtOracleSettings"]
