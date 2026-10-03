"""DBT Oracle domain models composed into the models facade."""

from __future__ import annotations

from typing import Annotated

from flext_meltano import m, t, u

from flext_dbt_oracle import c


class FlextDbtOracleModelsDbt:
    """DBT Oracle domain models namespace."""

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

    class DbtConnectionProfile(m.Value):
        """Typed dbt profile for Oracle-backed workflows (JSON wire shape)."""

        type: Annotated[str, u.Field(description="dbt adapter type")] = "oracle"
        host: Annotated[str, u.Field(description="Oracle database host")]
        port: Annotated[t.PortNumber, u.Field(description="Oracle database port")]
        user: Annotated[str, u.Field(description="Oracle database username")]
        password: Annotated[str, u.Field(description="Oracle database password")]
        service_name: Annotated[str, u.Field(description="Oracle service name")]
        schema_name: Annotated[
            str, u.Field(serialization_alias="schema", description="Target dbt schema")
        ]
        project: Annotated[str, u.Field(description="dbt project name")]

    class OracleTableAdapter(m.Value):
        """Adapter for Oracle table metadata normalization."""

        schema_name: Annotated[
            str, u.Field(serialization_alias="schema", description="Oracle schema name")
        ]
        table_name: Annotated[
            str, u.Field(serialization_alias="table", description="Oracle table name")
        ]

        @u.computed_field
        @property
        def relation(self) -> str:
            """Fully qualified relation name."""
            return f"{self.schema_name}.{self.table_name}"

        @property
        def relation_name(self) -> str:
            """Fully qualified relation name under its stable public name."""
            return self.relation


__all__: list[str] = ["FlextDbtOracleModelsDbt"]
