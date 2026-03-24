"""Core model objects used by DBT Oracle workflows."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Annotated, ClassVar, Literal

from flext_core import FlextModels, t
from flext_db_oracle import FlextDbOracleModels
from flext_meltano import FlextMeltanoModels
from pydantic import (
    ConfigDict,
    Field,
    SecretStr,
    computed_field,
    model_validator,
)

from flext_dbt_oracle.constants import c


class FlextDbtOracleModels(FlextDbOracleModels, FlextMeltanoModels):
    """Namespace wrapper for DBT Oracle domain models.

    Inherits from FlextMeltanoModels (Singer/Meltano) and FlextDbOracleModels
    (Oracle DB) to compose the full DBT Oracle domain namespace.
    """

    class DbtOracle:
        """DbtOracle domain namespace."""

        class Model(FlextModels.Value):
            """Typed DBT model metadata payload."""

            name: str
            dbt_model_type: str = c.DbtOracle.DEFAULT_MODEL_TYPE
            schema_name: str = c.DbtOracle.DEFAULT_SCHEMA_NAME
            table_name: str
            materialization: str = c.Dbt.DEFAULT_MATERIALIZATION
            sql_content: str
            description: str = ""
            source_name: str = c.DbtOracle.DEFAULT_SOURCE_NAME
            columns: Annotated[Sequence[t.StrMapping], Field(default_factory=list)]
            dependencies: Annotated[t.StrSequence, Field(default_factory=list)]

        class ModelGenerator:
            """Helper for generating deterministic staging model metadata."""

            def __init__(
                self,
                config: t.StrMapping | None = None,
            ) -> None:
                """Store optional generation-time configuration."""
                super().__init__()
                self.config = config or {}

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

    class OracleConnectionConfig(FlextModels.Value):
        """Configuration for Oracle database connections."""

        host: Annotated[
            str,
            Field(
                default=c.Oracle.DEFAULT_HOST,
                description="Oracle database host",
            ),
        ]
        port: Annotated[
            t.PortNumber,
            Field(
                default=c.Oracle.DEFAULT_PORT,
                description="Oracle database port",
            ),
        ]
        username: Annotated[
            str,
            Field(default="", description="Oracle database username"),
        ]
        password: Annotated[
            str | SecretStr,
            Field(
                default=SecretStr(""),
                description="Oracle database password",
            ),
        ]
        service_name: Annotated[
            str,
            Field(
                default=c.Oracle.DEFAULT_SERVICE_NAME,
                description="Oracle service name",
            ),
        ]
        sid: Annotated[
            str | None, Field(default=None, description="Oracle SID (optional)")
        ]
        protocol: Annotated[
            str,
            Field(
                default=c.Oracle.DEFAULT_PROTOCOL,
                description="Oracle connection protocol",
            ),
        ]

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

    class OracleTableAdapter(FlextModels.Value):
        """Adapter for Oracle table metadata normalization."""

        schema_name: Annotated[str, Field(description="Oracle schema name")]
        table_name: Annotated[str, Field(description="Oracle table name")]

        def get_relation_name(self) -> str:
            """Return fully qualified relation name as schema.table."""
            return f"{self.schema_name}.{self.table_name}"

        def to_metadata(self) -> t.StrMapping:
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
            schema_name: str,
            table_name: str,
        ) -> FlextDbtOracleModels.OracleTableAdapter:
            """Create adapter with trimmed, normalized names."""
            return FlextDbtOracleModels.OracleTableAdapter(
                schema_name=schema_name.strip() or c.DbtOracle.DEFAULT_SCHEMA_NAME,
                table_name=table_name.strip(),
            )

    class FlextDbtOracleSettings(FlextModels.Value):
        """Configuration for DBT Oracle operations."""

        model_config: ClassVar[ConfigDict] = ConfigDict(
            extra="ignore",
            populate_by_name=True,
            frozen=False,
        )

        oracle_host: Annotated[
            str,
            Field(
                default=c.Oracle.DEFAULT_HOST,
                description="Oracle database host",
            ),
        ]
        oracle_username: Annotated[
            str,
            Field(
                default="oracle",
                description="Oracle database username",
            ),
        ]
        oracle_password: Annotated[
            SecretStr,
            Field(
                default=SecretStr(""),
                description="Oracle database password",
            ),
        ]
        oracle_port: Annotated[
            t.PortNumber,
            Field(
                default=c.Oracle.DEFAULT_PORT,
                alias="port",
                description="Oracle database port",
            ),
        ]
        oracle_service_name: Annotated[
            str,
            Field(
                default=c.Oracle.DEFAULT_SERVICE_NAME,
                description="Oracle service name",
            ),
        ]

        sid: Annotated[
            str | None, Field(default=None, description="Oracle SID (optional)")
        ]
        protocol: Annotated[
            Literal["tcp", "tcps"],
            Field(
                default="tcp",
                description="Connection protocol",
            ),
        ]
        materialization: Annotated[
            Literal["incremental", "snapshot", "table", "view"],
            Field(
                default="table",
                description="DBT materialization strategy",
            ),
        ]
        schema_name: Annotated[str, Field(default="", description="Target schema name")]
        ssl_server_dn_match: Annotated[
            bool,
            Field(
                default=False,
                description="Enable SSL server DN validation",
            ),
        ]
        nls_lang: Annotated[
            str,
            Field(
                default=c.DbtOracle.NLS_LANG,
                description="Oracle NLS language setting",
            ),
        ]
        nls_date_format: Annotated[
            str,
            Field(
                default=c.DbtOracle.NLS_DATE_FORMAT,
                description="Oracle NLS date format",
            ),
        ]
        search_path: Annotated[
            str,
            Field(
                default="",
                description="Comma-separated schema search path",
            ),
        ]
        enable_metrics: Annotated[
            bool,
            Field(
                default=False,
                description="Enable metrics collection",
            ),
        ]
        log_level: Annotated[
            Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
            Field(
                default="INFO",
                description="Runtime log verbosity",
            ),
        ]
        enable_sql_logging: Annotated[
            bool,
            Field(
                default=False,
                description="Enable SQL query logging",
            ),
        ]

        # Connection pool settings
        pool_min_size: Annotated[
            t.PositiveInt,
            Field(default=1, description="Minimum pool size"),
        ]
        pool_max_size: Annotated[
            t.PositiveInt,
            Field(
                default=10,
                description="Maximum pool size",
            ),
        ]
        pool_increment: Annotated[
            t.PositiveInt,
            Field(
                default=1,
                description="Pool increment size",
            ),
        ]

        # Performance settings
        query_timeout: Annotated[
            t.PositiveInt,
            Field(
                default=300,
                description="Query timeout in seconds",
            ),
        ]
        fetch_size: Annotated[
            t.PositiveInt,
            Field(default=1000, description="Fetch batch size"),
        ]
        connect_timeout: Annotated[
            t.PositiveInt,
            Field(
                default=30,
                description="Connection timeout in seconds",
            ),
        ]
        retry_attempts: Annotated[
            t.NonNegativeInt,
            Field(
                default=3,
                description="Number of retry attempts",
            ),
        ]
        retry_delay: Annotated[
            t.NonNegativeInt,
            Field(
                default=1,
                description="Delay between retries in seconds",
            ),
        ]
        retry_delay_seconds: Annotated[
            t.NonNegativeFloat,
            Field(
                default=1.0,
                description="Delay between retries in seconds",
            ),
        ]

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

        def to_connection_config(self) -> Mapping[str, str | int | None]:
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

        def get_performance_settings(self) -> Mapping[str, int]:
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

        def get_dbt_settings(self) -> t.StrMapping:
            """Return DBT-specific settings."""
            return {
                "database": self.oracle_service_name,
                "schema": self.get_effective_schema(),
                "materialization": self.materialization,
            }

    @classmethod
    def create_generator(
        cls,
        config: t.StrMapping | None = None,
    ) -> FlextDbtOracleModels.DbtOracle.ModelGenerator:
        """Create generator instance with optional custom config."""
        return cls.DbtOracle.ModelGenerator(config=config)


m = FlextDbtOracleModels

__all__ = [
    "FlextDbtOracleModels",
    "m",
]
