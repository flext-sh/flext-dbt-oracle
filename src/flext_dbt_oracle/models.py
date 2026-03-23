"""Core model objects used by DBT Oracle workflows."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Annotated, ClassVar, Literal

from annotated_types import Ge, Gt
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    SecretStr,
    computed_field,
    model_validator,
)

from flext_dbt_oracle.constants import c
from flext_dbt_oracle.typings import ColumnSpec

_PositiveInt = Annotated[int, Gt(0)]
_NonNegativeInt = Annotated[int, Ge(0)]
_NonNegativeFloat = Annotated[float, Ge(0.0)]
_PortNumber = Annotated[int, Ge(1)]


class FlextDbtOracleModels(BaseModel):
    """Namespace wrapper for DBT Oracle domain models.

    Inherits from FlextMeltanoModels (Singer/Meltano) and FlextDbOracleModels
    (Oracle DB) to compose the full DBT Oracle domain namespace.
    """

    class DbtOracle:
        """DbtOracle domain namespace."""

        class Model(BaseModel):
            """Typed DBT model metadata payload."""

            name: str
            dbt_model_type: str = c.DbtOracle.DEFAULT_MODEL_TYPE
            schema_name: str = c.DbtOracle.DEFAULT_SCHEMA_NAME
            table_name: str
            materialization: str = c.Dbt.DEFAULT_MATERIALIZATION
            sql_content: str
            description: str = ""
            source_name: str = c.DbtOracle.DEFAULT_SOURCE_NAME
            columns: list[ColumnSpec] = Field(default=[])
            dependencies: list[str] = Field(default=[])

        class ModelGenerator:
            """Helper for generating deterministic staging model metadata."""

            def __init__(
                self,
                config: Mapping[str, str] | None = None,
            ) -> None:
                """Store optional generation-time configuration."""
                super().__init__()
                self.config = config or {}

            def generate_staging_models(
                self,
                source_tables: list[str],
            ) -> list[FlextDbtOracleModels.DbtOracle.Model]:
                """Create one staging model definition per source table."""
                return [
                    FlextDbtOracleModels.DbtOracle.Model(
                        name=f"stg_oracle_{table}",
                        table_name=f"stg_{table}",
                        sql_content=f"select * from {{{{ source('oracle', '{table}') }}}}",  # nosec B608
                        description=f"Staging model for {table}",
                    )
                    for table in source_tables
                ]

    class OracleConnectionConfig(BaseModel):
        """Configuration for Oracle database connections."""

        host: str = Field(
            default=c.Oracle.DEFAULT_HOST, description="Oracle database host"
        )
        port: _PortNumber = Field(
            default=c.Oracle.DEFAULT_PORT, description="Oracle database port"
        )
        username: str = Field(default="", description="Oracle database username")
        password: str | SecretStr = Field(
            default=SecretStr(""), description="Oracle database password"
        )
        service_name: str = Field(
            default=c.Oracle.DEFAULT_SERVICE_NAME, description="Oracle service name"
        )
        sid: str | None = Field(default=None, description="Oracle SID (optional)")
        protocol: str = Field(
            default=c.Oracle.DEFAULT_PROTOCOL, description="Oracle connection protocol"
        )

        @classmethod
        def validate_password(cls, v: str | SecretStr) -> SecretStr:
            """Convert string passwords to SecretStr."""
            if isinstance(v, str):
                return SecretStr(v)
            return v

        def get_database_identifier(self) -> str:
            """Return the database identifier (SID if set, otherwise service_name)."""
            if self.sid:
                return self.sid
            return self.service_name

        def get_dsn(self) -> str:
            """Return the connection string in DSN format.

            Format:
            - With service_name: "tcp://username:***@host:port/service_name"
            - With sid: "tcp://username:***@host:port:sid"
            """
            if self.sid:
                return f"{self.protocol}://{self.username}:***@{self.host}:{self.port}:{self.sid}"
            return f"{self.protocol}://{self.username}:***@{self.host}:{self.port}/{self.service_name}"

    class OracleTableAdapter(BaseModel):
        """Adapter for Oracle table metadata normalization."""

        schema_name: Annotated[str, Field(description="Oracle schema name")]
        table_name: Annotated[str, Field(description="Oracle table name")]

        def get_relation_name(self) -> str:
            """Return fully qualified relation name as schema.table."""
            return f"{self.schema_name}.{self.table_name}"

        def to_metadata(self) -> dict[str, str]:
            """Return metadata dict with schema, table, and relation."""
            return {
                "schema": self.schema_name,
                "table": self.table_name,
                "relation": self.get_relation_name(),
            }

    class OracleTableFactory:
        """Factory for creating Oracle table adapters."""

        @staticmethod
        def create(
            schema_name: str, table_name: str
        ) -> FlextDbtOracleModels.OracleTableAdapter:
            """Create adapter with trimmed, normalized names."""
            return FlextDbtOracleModels.OracleTableAdapter(
                schema_name=schema_name.strip() or c.DbtOracle.DEFAULT_SCHEMA_NAME,
                table_name=table_name.strip(),
            )

    class FlextDbtOracleSettings(BaseModel):
        """Configuration for DBT Oracle operations."""

        model_config: ClassVar[ConfigDict] = ConfigDict(
            extra="ignore", populate_by_name=True
        )

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
        oracle_port: _PortNumber = Field(
            default=c.Oracle.DEFAULT_PORT,
            alias="port",
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
        pool_min_size: _PositiveInt = Field(default=1, description="Minimum pool size")
        pool_max_size: _PositiveInt = Field(default=10, description="Maximum pool size")
        pool_increment: _PositiveInt = Field(
            default=1, description="Pool increment size"
        )

        # Performance settings
        query_timeout: _PositiveInt = Field(
            default=300, description="Query timeout in seconds"
        )
        fetch_size: _PositiveInt = Field(default=1000, description="Fetch batch size")
        connect_timeout: _PositiveInt = Field(
            default=30, description="Connection timeout in seconds"
        )
        retry_attempts: _NonNegativeInt = Field(
            default=3, description="Number of retry attempts"
        )
        retry_delay: _NonNegativeInt = Field(
            default=1, description="Delay between retries in seconds"
        )
        retry_delay_seconds: _NonNegativeFloat = Field(
            default=1.0,
            description="Delay between retries in seconds",
        )

        @model_validator(mode="after")
        def validate_pool_sizes(self) -> FlextDbtOracleModels.FlextDbtOracleSettings:
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

        def to_oracle_config(self) -> FlextDbtOracleModels.OracleConnectionConfig:
            """Convert to OracleConnectionConfig t.NormalizedValue."""
            return FlextDbtOracleModels.OracleConnectionConfig(
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

    @classmethod
    def create_generator(
        cls,
        config: Mapping[str, str] | None = None,
    ) -> FlextDbtOracleModels.DbtOracle.ModelGenerator:
        """Create generator instance with optional custom config."""
        return cls.DbtOracle.ModelGenerator(config=config)


__all__ = [
    "FlextDbtOracleModels",
    "m",
]

m = FlextDbtOracleModels

# Re-export facade models for backward compatibility
OracleConnectionConfig = FlextDbtOracleModels.OracleConnectionConfig
OracleTableAdapter = FlextDbtOracleModels.OracleTableAdapter
OracleTableFactory = FlextDbtOracleModels.OracleTableFactory
FlextDbtOracleSettings = FlextDbtOracleModels.FlextDbtOracleSettings
