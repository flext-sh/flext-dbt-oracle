"""Settings for DBT Oracle — namespaced under ``settings.DbtOracle``.

Universal fields via MRO; project fields in the ``DbtOracle`` group with simple
scalar types (env-settable). Connection strings / Oracle config objects are
built by consumers from these scalars, not stored as complex settings fields.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field, model_validator
from pydantic_settings import SettingsConfigDict

from flext_meltano import FlextMeltanoSettings


class FlextDbtOracleSettings(FlextMeltanoSettings):
    """DBT Oracle pipeline settings; fields under ``settings.DbtOracle.*``."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_",
        env_nested_delimiter="__",
        extra="ignore",
        populate_by_name=True,
    )

    class _DbtOracle(BaseModel):
        """Namespaced DBT Oracle settings."""

        oracle_host: Annotated[str, Field(default="localhost", description="Oracle host")]
        oracle_username: Annotated[str, Field(default="oracle", description="Oracle username")]
        oracle_password: Annotated[str, Field(default="", description="Oracle password")]
        oracle_port: Annotated[int, Field(default=1521, ge=1, le=65535, description="Oracle port")]
        oracle_service_name: Annotated[str, Field(default="XEPDB1", description="Oracle service name")]
        sid: Annotated[str | None, Field(default=None, description="Oracle SID (optional)")]
        protocol: Annotated[str, Field(default="tcp", description="Connection protocol (tcp/tcps)")]
        materialization: Annotated[str, Field(default="table", description="DBT materialization")]
        schema_name: Annotated[str, Field(default="", description="Target schema name")]
        ssl_server_dn_match: Annotated[bool, Field(default=False, description="SSL server DN match")]
        nls_lang: Annotated[
            str,
            Field(default="AMERICAN_AMERICA.AL32UTF8", description="Oracle NLS language"),
        ]
        nls_date_format: Annotated[str, Field(default="YYYY-MM-DD", description="Oracle NLS date format")]
        search_path: Annotated[str, Field(default="", description="Schema search path")]
        enable_metrics: Annotated[bool, Field(default=False, description="Enable metrics collection")]
        dbt_log_level: Annotated[str, Field(default="INFO", description="Runtime log verbosity")]
        enable_sql_logging: Annotated[bool, Field(default=False, description="Enable SQL query logging")]
        pool_min_size: Annotated[int, Field(default=1, ge=1, description="Minimum pool size")]
        pool_max_size: Annotated[int, Field(default=10, ge=1, description="Maximum pool size")]
        pool_increment: Annotated[int, Field(default=1, ge=1, description="Pool increment size")]
        query_timeout: Annotated[int, Field(default=300, ge=1, description="Query timeout (s)")]
        fetch_size: Annotated[int, Field(default=1000, ge=1, description="Fetch batch size")]
        connect_timeout: Annotated[int, Field(default=30, ge=1, description="Connection timeout (s)")]
        retry_attempts: Annotated[int, Field(default=3, ge=0, description="Retry attempts")]
        retry_delay: Annotated[int, Field(default=1, ge=0, description="Delay between retries")]
        retry_delay_seconds: Annotated[float, Field(default=1.0, ge=0, description="Retry delay (s)")]

        @model_validator(mode="after")
        def _validate_pool_sizes(self) -> "FlextDbtOracleSettings._DbtOracle":
            """Validate pool upper bound against minimum."""
            if self.pool_max_size < self.pool_min_size:
                raise ValueError("Pool max size must be >= pool min size")
            return self

    if TYPE_CHECKING:
        DbtOracle: _DbtOracle
    else:
        DbtOracle: _DbtOracle = Field(
            default_factory=_DbtOracle,
            description="Namespaced DBT Oracle settings.",
        )


settings: FlextDbtOracleSettings = FlextDbtOracleSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_dbt_oracle import settings``."""

__all__: list[str] = ["FlextDbtOracleSettings", "settings"]
