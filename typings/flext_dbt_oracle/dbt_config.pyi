from typing import ClassVar

from flext_core import FlextSettings
from flext_db_oracle import FlextDbOracleConfig
from flext_meltano.config import FlextMeltanoConfig

__all__ = ["FlextDbtOracleConfig"]

class FlextDbtOracleConfig(FlextSettings):
    oracle_host: str
    oracle_port: int
    oracle_service_name: str
    oracle_sid: str
    oracle_username: str
    oracle_password: str
    oracle_protocol: str
    oracle_pool_min: int
    oracle_pool_max: int
    oracle_timeout: int
    oracle_encoding: str
    dbt_project_dir: str
    dbt_profiles_dir: str
    dbt_target: str
    dbt_threads: int
    dbt_log_level: str
    dbt_schema: str
    oracle_schema_mapping: ClassVar[dict[str, str]]
    oracle_column_mapping: ClassVar[dict[str, str]]
    min_quality_threshold: float
    required_oracle_objects: ClassVar[list[str]]
    validate_connections: bool
    max_parallel_connections: int
    materialization_mapping: ClassVar[dict[str, str]]
    fetch_size: int
    batch_size: int
    enable_parallel_dml: bool
    optimizer_mode: str
    oracle_type_mapping: ClassVar[dict[str, str]]
    def get_oracle_config(self) -> FlextDbOracleConfig: ...
    def get_meltano_config(self) -> FlextMeltanoConfig: ...
    def get_oracle_quality_config(self) -> dict[str, object]: ...
    def get_performance_config(self) -> dict[str, object]: ...
    def get_object_type_for_schema(self, object_type: str) -> str | None: ...
    def get_schema_for_object_type(self, object_type: str) -> str | None: ...
    def get_dbt_type_for_oracle_type(self, oracle_type: str) -> str: ...
    def get_materialization_for_layer(self, layer: str) -> str: ...
    def validate_oracle_connection(self) -> bool: ...
