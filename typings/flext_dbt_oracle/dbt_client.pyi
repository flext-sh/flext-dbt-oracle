from _typeshed import Incomplete
from flext_core import FlextResult
from flext_db_oracle import FlextDbOracleApi
from flext_db_oracle.typings import FlextDbOracleTable as FlextOracleObject
from flext_meltano import FlextDbtHub

from flext_dbt_oracle.dbt_config import FlextDbtOracleConfig

__all__ = ["FlextDbtOracleClient"]

class FlextDbtOracleClient:
    config: Incomplete
    def __init__(self, config: FlextDbtOracleConfig | None = None) -> None: ...
    @property
    def oracle_api(self) -> FlextDbOracleApi: ...
    @property
    def dbt_hub(self) -> FlextDbtHub: ...
    def test_oracle_connection(self) -> FlextResult[dict[str, object]]: ...
    def extract_oracle_metadata(
        self,
        schema_names: list[str] | None = None,
        object_types: list[str] | None = None,
    ) -> FlextResult[list[FlextOracleObject]]: ...
    def validate_oracle_data(
        self, objects: list[FlextOracleObject]
    ) -> FlextResult[dict[str, object]]: ...
    def transform_with_dbt(
        self, objects: list[FlextOracleObject], model_names: list[str] | None = None
    ) -> FlextResult[dict[str, object]]: ...
    def run_full_pipeline(
        self,
        schema_names: list[str] | None = None,
        object_types: list[str] | None = None,
        model_names: list[str] | None = None,
    ) -> FlextResult[dict[str, object]]: ...
