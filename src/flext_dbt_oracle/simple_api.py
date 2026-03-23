"""Unified API facade for DBT Oracle operations."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from os import getenv

from pydantic import SecretStr, TypeAdapter, ValidationError

from flext_dbt_oracle.client import FlextDbtOracleClient
from flext_dbt_oracle.constants import c
from flext_dbt_oracle.services import FlextDbtOracleServices
from flext_dbt_oracle.settings import FlextDbtOracleSettings
from flext_dbt_oracle.typings import t

_TABLE_LIST_ADAPTER = TypeAdapter(Sequence[t.Scalar])


class FlextDbtOracle:
    """Facade combining client and service helpers."""

    def __init__(self, config: FlextDbtOracleSettings | None = None) -> None:
        """Initialize API with provided or default settings."""
        super().__init__()
        self.config = config or FlextDbtOracleSettings(
            oracle_host=c.Oracle.DEFAULT_HOST,
            oracle_username="user",
            oracle_password=SecretStr(getenv("FLEXT_DBT_ORACLE_PASSWORD", "")),
        )
        self.client = FlextDbtOracleClient(self.config)
        self.workflow_service = FlextDbtOracleServices()

    @classmethod
    def create(cls) -> FlextDbtOracle:
        """Create default API instance."""
        return cls()

    def run_oracle_to_dbt_workflow(
        self, tables: Sequence[str] | None = None
    ) -> Mapping[str, Mapping[str, t.MetadataValue]]:
        """Run extraction flow and return recommendations."""
        result = self.client.run_pipeline(tables=tables)
        table_payload = result.get("tables")
        try:
            table_count = len(_TABLE_LIST_ADAPTER.validate_python(table_payload))
        except ValidationError:
            table_count = 0
        recommendations = self.workflow_service.generate_recommendations(
            table_count=table_count
        )
        result_dict: Mapping[str, Mapping[str, t.MetadataValue]] = {
            "pipeline": result,
            "recommendations": recommendations,
        }
        return result_dict


__all__ = ["FlextDbtOracle"]
