"""Unified API facade for DBT Oracle operations."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from os import getenv

from flext_core import FlextTypes
from pydantic import TypeAdapter, ValidationError

from flext_dbt_oracle.connections import FlextDbtOracleConnections
from flext_dbt_oracle.constants import c
from flext_dbt_oracle.models import FlextDbtOracleModels
from flext_dbt_oracle.utilities import FlextDbtOracleUtilities

_TABLE_LIST_ADAPTER: TypeAdapter[Sequence[FlextTypes.Scalar]] = TypeAdapter(
    Sequence[FlextTypes.Scalar],
)


class FlextDbtOracle:
    """Facade combining client and service helpers."""

    def __init__(
        self,
        config: FlextDbtOracleModels.DbtOracle.FlextDbtOracleSettings | None = None,
    ) -> None:
        """Initialize API with provided or default settings."""
        super().__init__()
        self.config = (
            config
            or FlextDbtOracleModels.DbtOracle.FlextDbtOracleSettings.model_validate({
                "oracle_host": c.DbtOracle.Oracle.DEFAULT_HOST,
                "oracle_username": "user",
                "oracle_password": getenv("FLEXT_DBT_ORACLE_PASSWORD", ""),
            })
        )
        self.client = FlextDbtOracleUtilities.DbtOracle.Client(self.config)
        self.workflow_service = FlextDbtOracleUtilities.DbtOracle.Services()

    @classmethod
    def create(cls) -> FlextDbtOracle:
        """Create default API instance."""
        return cls()

    @staticmethod
    def build_oracle_connection_config(
        host: str,
        username: str,
        password: str,
        service_name: str = c.DbtOracle.Oracle.DEFAULT_SERVICE_NAME,
        *,
        sid: str | None = None,
        port: int = c.DbtOracle.Oracle.DEFAULT_PORT,
        protocol: str = c.DbtOracle.Oracle.DEFAULT_PROTOCOL,
    ) -> FlextDbtOracleModels.DbtOracle.OracleConnectionConfig:
        """Create validated Oracle connection config."""
        return FlextDbtOracleConnections.build_oracle_connection_config(
            host=host,
            username=username,
            password=password,
            service_name=service_name,
            sid=sid,
            port=port,
            protocol=protocol,
        )

    def run_oracle_to_dbt_workflow(
        self,
        tables: Sequence[str] | None = None,
    ) -> Mapping[str, Mapping[str, FlextTypes.MetadataValue]]:
        """Run extraction flow and return recommendations."""
        result = self.client.run_pipeline(tables=tables)
        table_payload = result.get("tables")
        try:
            table_count = len(_TABLE_LIST_ADAPTER.validate_python(table_payload))
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
