"""Core model objects used by DBT Oracle workflows."""

from __future__ import annotations

from typing import Annotated

from flext_db_oracle import m
from flext_dbt_oracle import c, t
from flext_meltano import FlextMeltanoModels, u


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
                str, u.Field(description="DBT model classification")
            ] = c.DbtOracle.DEFAULT_MODEL_TYPE
            schema_name: Annotated[str, u.Field(description="Target schema name")] = (
                c.DbtOracle.DEFAULT_SCHEMA_NAME
            )
            table_name: Annotated[str, u.Field(description="Target table name")]
            materialization: Annotated[
                c.DbtOracle.Dbt.Materialization,
                u.Field(description="DBT materialization strategy"),
            ] = c.DbtOracle.Dbt.DEFAULT_MATERIALIZATION
            sql_content: Annotated[str, u.Field(description="Model SQL body")]
            description: Annotated[
                str, u.Field(description="Human-readable model description")
            ] = ""
            source_name: Annotated[str, u.Field(description="Source system name")] = (
                c.DbtOracle.DEFAULT_SOURCE_NAME
            )
            columns: t.SequenceOf[t.StrMapping] = u.Field(
                default_factory=tuple,
                description="Normalized column metadata for the DBT model",
            )
            dependencies: t.StrSequence = u.Field(
                default_factory=tuple, description="Upstream DBT model dependencies"
            )

        # NOTE (multi-agent, bead mro-wfc8.1): ModelGenerator moved to
        # u.DbtOracle.ModelBuilder (behavior belongs in utilities, not on/among models).

        class OracleConnectionConfig(m.Value):
            """Configuration for Oracle database connections."""

            host: Annotated[str, u.Field(description="Oracle database host")] = (
                c.DbtOracle.Oracle.DEFAULT_HOST
            )
            port: Annotated[
                t.PortNumber, u.Field(description="Oracle database port")
            ] = c.DbtOracle.Oracle.DEFAULT_PORT
            username: Annotated[
                str, u.Field(description="Oracle database username")
            ] = ""
            password: Annotated[
                t.SecretStr, u.Field(description="Oracle database password")
            ] = t.SecretStr("")
            service_name: Annotated[str, u.Field(description="Oracle service name")] = (
                c.DbtOracle.Oracle.DEFAULT_SERVICE_NAME
            )
            sid: Annotated[str | None, u.Field(description="Oracle SID (optional)")] = (
                None
            )
            protocol: Annotated[
                str, u.Field(description="Oracle connection protocol")
            ] = c.DbtOracle.Oracle.DEFAULT_PROTOCOL

            # NOTE (multi-agent, bead mro-wfc8.1): the former validate_password classmethod
            # was never wired as a @field_validator (silent no-op: password stayed str). The
            # field is now typed t.SecretStr, which coerces str->SecretStr declaratively.

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

        class DbtConnectionProfile(m.Value):
            # NOTE (multi-agent): settings-fallout lane (mro-rn88) — typed model for
            # the dbt Oracle connection profile so base.py stops hand-assembling a raw
            # dict (flext-law §1.2/§3a: build a model, emit model_dump at the edge).
            """Typed dbt profile for Oracle-backed workflows (JSON wire shape)."""

            type: Annotated[str, u.Field(description="dbt adapter type")] = "oracle"
            host: Annotated[str, u.Field(description="Oracle database host")]
            port: Annotated[t.PortNumber, u.Field(description="Oracle database port")]
            user: Annotated[str, u.Field(description="Oracle database username")]
            password: Annotated[str, u.Field(description="Oracle database password")]
            service_name: Annotated[str, u.Field(description="Oracle service name")]
            schema_name: Annotated[
                str,
                u.Field(serialization_alias="schema", description="Target dbt schema"),
            ]
            project: Annotated[str, u.Field(description="dbt project name")]

        class OracleTableAdapter(m.Value):
            """Adapter for Oracle table metadata normalization."""

            schema_name: Annotated[
                str,
                u.Field(serialization_alias="schema", description="Oracle schema name"),
            ]
            table_name: Annotated[
                str,
                u.Field(serialization_alias="table", description="Oracle table name"),
            ]

            @u.computed_field(alias="relation", return_type=str)
            @property
            def relation_name(self) -> str:
                """Fully qualified relation name."""
                return f"{self.schema_name}.{self.table_name}"

            # NOTE (multi-agent, bead mro-wfc8.1): to_metadata() removed — the
            # {schema,table,relation} mapping is model_dump(by_alias=True) (§1.3: no
            # dict-as-contract; §2a: no methods on models).


m = FlextDbtOracleModels

__all__: list[str] = ["FlextDbtOracleModels", "m"]
