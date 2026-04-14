"""Core model objects used by DBT Oracle workflows."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Annotated, ClassVar, Literal

from flext_db_oracle import m
from flext_dbt_oracle import c, t, u
from flext_meltano import FlextMeltanoModels


class FlextDbtOracleModels(FlextMeltanoModels, m):
    """Namespace wrapper for DBT Oracle domain models.

    Inherits from FlextMeltanoModels (Singer/Meltano) and m
    (Oracle DB) to compose the full DBT Oracle domain namespace.
    """

    class DbtOracle:
        """DbtOracle domain namespace."""

        class Model(m.Value):
            """Typed DBT model metadata payload."""

            name: Annotated[str, u.Field(description="DBT model name")]
            dbt_model_type: Annotated[
                str,
                u.Field(description="DBT model classification"),
            ] = c.DbtOracle.DEFAULT_MODEL_TYPE
            schema_name: Annotated[
                str,
                u.Field(description="Target schema name"),
            ] = c.DbtOracle.DEFAULT_SCHEMA_NAME
            table_name: Annotated[str, u.Field(description="Target table name")]
            materialization: Annotated[
                t.DbtOracle.Materialization,
                u.Field(description="DBT materialization strategy"),
            ] = c.DbtOracle.Dbt.DEFAULT_MATERIALIZATION
            sql_content: Annotated[str, u.Field(description="Model SQL body")]
            description: Annotated[
                str,
                u.Field(description="Human-readable model description"),
            ] = ""
            source_name: Annotated[
                str,
                u.Field(description="Source system name"),
            ] = c.DbtOracle.DEFAULT_SOURCE_NAME
            columns: Annotated[
                Sequence[t.StrMapping],
                u.Field(
                    default_factory=list,
                    description="Column metadata payloads",
                ),
            ]
            dependencies: Annotated[
                t.StrSequence,
                u.Field(
                    default_factory=list,
                    description="Upstream model dependencies",
                ),
            ]

        class ModelGenerator:
            """Helper for generating deterministic staging model metadata."""

            def __init__(
                self,
                settings: t.StrMapping | None = None,
            ) -> None:
                """Store optional generation-time configuration."""
                super().__init__()
                self.settings = settings or {}

            def generate_staging_models(
                self,
                source_tables: t.StrSequence,
            ) -> Sequence[FlextDbtOracleModels.DbtOracle.Model]:
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

        class OracleConnectionConfig(m.Value):
            """Configuration for Oracle database connections."""

            host: Annotated[
                str,
                u.Field(description="Oracle database host"),
            ] = c.DbtOracle.Oracle.DEFAULT_HOST
            port: Annotated[
                t.PortNumber,
                u.Field(description="Oracle database port"),
            ] = c.DbtOracle.Oracle.DEFAULT_PORT
            username: Annotated[
                str,
                u.Field(description="Oracle database username"),
            ] = ""
            password: Annotated[
                str | t.SecretStr,
                u.Field(description="Oracle database password"),
            ] = t.SecretStr("")
            service_name: Annotated[
                str,
                u.Field(description="Oracle service name"),
            ] = c.DbtOracle.Oracle.DEFAULT_SERVICE_NAME
            sid: Annotated[
                str | None,
                u.Field(description="Oracle SID (optional)"),
            ] = None
            protocol: Annotated[
                str,
                u.Field(description="Oracle connection protocol"),
            ] = c.DbtOracle.Oracle.DEFAULT_PROTOCOL

            @classmethod
            def validate_password(cls, v: str | t.SecretStr) -> t.SecretStr:
                """Convert string passwords to t.SecretStr."""
                if isinstance(v, str):
                    return t.SecretStr(v)
                return v

            @u.computed_field(return_type=str)
            @property
            def database_identifier(self) -> str:
                """Database identifier."""
                if self.sid:
                    return self.sid
                return self.service_name

            @u.computed_field(return_type=str)
            @property
            def dsn(self) -> str:
                """Connection string in DSN format."""
                if self.sid:
                    return (
                        f"{self.protocol}://{self.username}:***@"
                        f"{self.host}:{self.port}:{self.sid}"
                    )
                return (
                    f"{self.protocol}://{self.username}:***@"
                    f"{self.host}:{self.port}/{self.service_name}"
                )

        class OracleTableAdapter(m.Value):
            """Adapter for Oracle table metadata normalization."""

            schema_name: Annotated[
                str,
                u.Field(description="Oracle schema name"),
            ]
            table_name: Annotated[
                str,
                u.Field(description="Oracle table name"),
            ]

            @u.computed_field(return_type=str)
            @property
            def relation_name(self) -> str:
                """Fully qualified relation name."""
                return f"{self.schema_name}.{self.table_name}"

            def to_metadata(self) -> t.StrMapping:
                """Return metadata dict."""
                return {
                    "schema": self.schema_name,
                    "table": self.table_name,
                    "relation": self.relation_name,
                }

        class OracleTableFactory:
            """Factory for creating Oracle table adapters."""

            @staticmethod
            def create(
                schema_name: str,
                table_name: str,
            ) -> FlextDbtOracleModels.DbtOracle.OracleTableAdapter:
                """Create adapter with trimmed, normalized names."""
                return FlextDbtOracleModels.DbtOracle.OracleTableAdapter(
                    schema_name=schema_name.strip() or c.DbtOracle.DEFAULT_SCHEMA_NAME,
                    table_name=table_name.strip(),
                )

        class FlextDbtOracleSettings(m.Value):
            """Configuration for DBT Oracle operations."""

            model_config: ClassVar[c.ConfigDict] = c.ConfigDict(
                populate_by_name=True,
                frozen=False,
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
                u.Field(
                    alias="port",
                    description="Oracle database port",
                ),
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
                t.DbtOracle.Materialization,
                u.Field(description="DBT materialization strategy"),
            ] = "table"
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
            def validate_pool_sizes(
                self,
            ) -> FlextDbtOracleModels.DbtOracle.FlextDbtOracleSettings:
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

            def to_connection_config(
                self,
            ) -> Mapping[str, str | int | None]:
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

            def to_oracle_config(
                self,
            ) -> FlextDbtOracleModels.DbtOracle.OracleConnectionConfig:
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

    @classmethod
    def create_generator(
        cls,
        settings: t.StrMapping | None = None,
    ) -> FlextDbtOracleModels.DbtOracle.ModelGenerator:
        """Create generator instance with optional settings."""
        return cls.DbtOracle.ModelGenerator(settings=settings)


m = FlextDbtOracleModels

__all__: list[str] = [
    "FlextDbtOracleModels",
    "m",
]
