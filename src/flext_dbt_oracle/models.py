"""Core model objects used by DBT Oracle workflows."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextModels
from flext_db_oracle.models import FlextDbOracleModels
from flext_dbt_oracle.constants import c
from flext_dbt_oracle.typings import t
from flext_meltano.models import FlextMeltanoModels
from pydantic import Field


class FlextDbtOracleModels(FlextMeltanoModels, FlextDbOracleModels):
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
            columns: list[dict[str, object]] = Field(default=[])
            dependencies: list[str] = Field(default_factory=list)

        class ModelGenerator:
            """Helper for generating deterministic staging model metadata."""

            def __init__(
                self,
                config: Mapping[str, t.GeneralValueType] | None = None,
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

    @classmethod
    def create_generator(
        cls,
        config: Mapping[str, t.GeneralValueType] | None = None,
    ) -> FlextDbtOracleModels.DbtOracle.ModelGenerator:
        """Create generator instance with optional custom config."""
        return cls.DbtOracle.ModelGenerator(config=config)


m = FlextDbtOracleModels

__all__ = [
    "FlextDbtOracleModels",
    "m",
]
