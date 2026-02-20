"""Unified API facade for DBT Oracle operations."""

from __future__ import annotations

from os import getenv

from flext_dbt_oracle.client import FlextDbtOracleClient
from flext_dbt_oracle.services import FlextDbtOracleWorkflowService
from flext_dbt_oracle.settings import FlextDbtOracleSettings
from pydantic import SecretStr

type JsonScalar = str | int | float | bool | None
type JsonValue = JsonScalar | dict[str, JsonValue] | list[JsonValue]


class FlextDbtOracle:
    """Facade combining client and service helpers."""

    def __init__(self, config: FlextDbtOracleSettings | None = None) -> None:
        """Initialize API with provided or default settings."""
        self.config = config or FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="user",
            oracle_password=SecretStr(getenv("FLEXT_DBT_ORACLE_PASSWORD", "")),
        )
        self.client = FlextDbtOracleClient(self.config)
        self.workflow_service = FlextDbtOracleWorkflowService()

    @classmethod
    def create(cls) -> FlextDbtOracle:
        """Create default API instance."""
        return cls()

    def run_oracle_to_dbt_workflow(
        self,
        tables: list[str] | None = None,
    ) -> dict[str, JsonValue]:
        """Run extraction flow and return recommendations."""
        result = self.client.run_pipeline(tables=tables)
        table_payload = result.get("tables")
        table_count = len(table_payload) if isinstance(table_payload, list) else 0
        recommendations = self.workflow_service.generate_recommendations(
            table_count=table_count
        )
        return {
            "pipeline": result,
            "recommendations": recommendations,
        }


__all__ = ["FlextDbtOracle"]
