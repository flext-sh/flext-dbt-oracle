from pathlib import Path

from _typeshed import Incomplete
from flext_core import FlextResult
from flext_db_oracle.typings import FlextDbOracleTable as FlextOracleObject

from flext_dbt_oracle.dbt_config import FlextDbtOracleConfig

__all__ = ["FlextDbtOracleMonitoringService", "FlextDbtOracleWorkflowService"]

class FlextDbtOracleWorkflowService:
    config: Incomplete
    client: Incomplete
    oracle_api: Incomplete
    model_generator: Incomplete
    def __init__(self, config: FlextDbtOracleConfig | None = None) -> None: ...
    def run_metadata_to_models_workflow(
        self,
        schema_names: list[str] | None = None,
        object_types: list[str] | None = None,
        output_path: Path | str | None = None,
    ) -> FlextResult[dict[str, object]]: ...
    def run_full_transformation_pipeline(
        self,
        schema_names: list[str] | None = None,
        object_types: list[str] | None = None,
        model_names: list[str] | None = None,
        *,
        generate_models: bool = True,
        models_output_path: Path | str | None = None,
    ) -> FlextResult[dict[str, object]]: ...
    def validate_workflow_prerequisites(self) -> FlextResult[dict[str, object]]: ...
    def get_workflow_recommendations(
        self, oracle_objects: list[FlextOracleObject] | None = None
    ) -> FlextResult[dict[str, object]]: ...

class FlextDbtOracleMonitoringService:
    config: Incomplete
    def __init__(self, config: FlextDbtOracleConfig) -> None: ...
    def track_workflow_execution(
        self, workflow_type: str, workflow_params: dict[str, object]
    ) -> dict[str, object]: ...
    def log_workflow_completion(
        self, tracking_info: dict[str, object], result: FlextResult[object]
    ) -> None: ...
