"""Unified API facade for DBT Oracle operations."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Self

from pydantic import ValidationError

from flext_core import FlextSettings, FlextTypes
from flext_dbt_oracle import (
    FlextDbtOracleModels,
    FlextDbtOracleUtilities,
    t,
)


class FlextDbtOracle:
    """Facade combining client and service helpers."""

    def __init__(
        self,
        config: FlextDbtOracleModels.DbtOracle.FlextDbtOracleSettings | None = None,
    ) -> None:
        """Initialize API with provided or default settings."""
        super().__init__()
        self.config = config or FlextSettings.get_global().get_namespace(
            "dbt_oracle",
            FlextDbtOracleModels.DbtOracle.FlextDbtOracleSettings,
        )
        self.client = FlextDbtOracleUtilities.DbtOracle.Client(self.config)
        self.workflow_service = FlextDbtOracleUtilities.DbtOracle.Services()

    @classmethod
    def create(cls) -> Self:
        """Create default API instance."""
        return cls()

    def run_oracle_to_dbt_workflow(
        self,
        tables: t.StrSequence | None = None,
    ) -> Mapping[str, Mapping[str, FlextTypes.MetadataValue]]:
        """Run extraction flow and return recommendations."""
        result = self.client.run_pipeline(tables=tables)
        table_payload = result.get("tables")
        try:
            table_count = len(t.SCALAR_LIST_ADAPTER.validate_python(table_payload))
        except ValidationError:
            table_count = 0
        recommendations = self.workflow_service.generate_recommendations(
            table_count=table_count,
        )
        result_dict: Mapping[str, Mapping[str, FlextTypes.MetadataValue]] = {
            "pipeline": result,
            "recommendations": recommendations,
        }
        return result_dict


__all__ = ["FlextDbtOracle"]
