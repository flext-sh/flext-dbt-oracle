"""Core model objects used by DBT Oracle workflows."""

from __future__ import annotations

from pydantic import BaseModel, Field

type JsonScalar = str | int | float | bool | None
type JsonValue = JsonScalar | dict[str, JsonValue] | list[JsonValue]


class FlextDbtOracleModel(BaseModel):
    """Typed DBT model metadata payload."""

    name: str
    dbt_model_type: str = "staging"
    schema_name: str = "public"
    table_name: str
    materialization: str = "view"
    sql_content: str
    description: str = ""
    source_name: str = "oracle"
    columns: list[dict[str, JsonValue]] = Field(default_factory=list)
    dependencies: list[str] = Field(default_factory=list)


class FlextDbtOracleModelGenerator:
    """Helper for generating deterministic staging model metadata."""

    def __init__(self, config: dict[str, JsonValue] | None = None) -> None:
        """Store optional generation-time configuration."""
        self.config = config or {}

    def generate_staging_models(
        self,
        source_tables: list[str],
    ) -> list[FlextDbtOracleModel]:
        """Create one staging model definition per source table."""
        return [
            FlextDbtOracleModel(
                name=f"stg_oracle_{table}",
                table_name=f"stg_{table}",
                sql_content=f"select * from {{{{ source('oracle', '{table}') }}}}",
                description=f"Staging model for {table}",
            )
            for table in source_tables
        ]


class FlextDbtOracleModels:
    """Namespace wrapper for model class aliases and constructors."""

    DbtModel = FlextDbtOracleModel
    ModelGenerator = FlextDbtOracleModelGenerator

    @classmethod
    def create_generator(
        cls,
        config: dict[str, JsonValue] | None = None,
    ) -> FlextDbtOracleModelGenerator:
        """Create generator instance with optional custom config."""
        return cls.ModelGenerator(config=config)


__all__ = [
    "FlextDbtOracleModel",
    "FlextDbtOracleModelGenerator",
    "FlextDbtOracleModels",
]
