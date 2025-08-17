from pathlib import Path
from typing import ClassVar

from _typeshed import Incomplete
from flext_core import FlextResult, FlextValueObject
from flext_db_oracle import FlextDbOracleApi, FlextDbOracleTable as FlextOracleObject

from flext_dbt_oracle.dbt_config import FlextDbtOracleConfig

__all__ = ["FlextDbtOracleModel", "FlextDbtOracleModelGenerator"]

class FlextDbtOracleModel(FlextValueObject):
    name: str
    dbt_model_type: str
    schema_name: str
    table_name: str
    columns: list[dict[str, object]]
    materialization: str
    sql_content: str
    description: str
    oracle_source: str
    dependencies: list[str]
    def validate_business_rules(self) -> FlextResult[None]: ...
    def get_file_path(self, base_path: Path) -> Path: ...
    def get_schema_file_path(self, base_path: Path) -> Path: ...
    def to_sql_file(self) -> str: ...
    def to_schema_entry(self) -> dict[str, object]: ...

class FlextDbtOracleModelGenerator:
    STAGING_TEMPLATE: ClassVar[str]
    INTERMEDIATE_TEMPLATE: ClassVar[str]
    MARTS_TEMPLATE: ClassVar[str]
    ORACLE_DATA_TYPE_TESTS: ClassVar[dict[str, list[str]]]
    config: Incomplete
    oracle_api: Incomplete
    def __init__(
        self, config: FlextDbtOracleConfig, oracle_api: FlextDbOracleApi
    ) -> None: ...
    def generate_staging_models(
        self, oracle_objects: list[FlextOracleObject]
    ) -> FlextResult[list[FlextDbtOracleModel]]: ...
    def generate_intermediate_models(
        self, staging_models: list[FlextDbtOracleModel]
    ) -> FlextResult[list[FlextDbtOracleModel]]: ...
    def generate_marts_models(
        self, intermediate_models: list[FlextDbtOracleModel]
    ) -> FlextResult[list[FlextDbtOracleModel]]: ...
    def write_models_to_disk(
        self, models: list[FlextDbtOracleModel], output_path: Path
    ) -> FlextResult[dict[str, int]]: ...
