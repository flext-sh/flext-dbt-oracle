"""Core model objects used by DBT Oracle workflows."""

from __future__ import annotations

from typing import Annotated

from flext_core import u
from flext_db_oracle import m
from flext_dbt_oracle.constants import c
from flext_dbt_oracle.typings import t
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
                c.DbtOracle.Dbt.Materialization,
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
                t.SequenceOf[t.StrMapping],
                u.Field(
                    default_factory=tuple,
                    description="Normalized column metadata for the DBT model",
                ),
            ]
            dependencies: Annotated[
                t.StrSequence,
                u.Field(
                    default_factory=tuple,
                    description="Upstream DBT model dependencies",
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
            ) -> t.SequenceOf[FlextDbtOracleModels.DbtOracle.Model]:
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
