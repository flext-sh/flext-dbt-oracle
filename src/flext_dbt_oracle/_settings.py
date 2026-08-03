"""Settings for DBT Oracle — connection scalars reused from ``settings.DbOracle``.

Oracle connection + pool scalars are the SSOT of ``flext-db-oracle`` and are
inherited via MRO as ``settings.DbOracle.*`` (host/port/username/password/
service_name/sid/pool_min/pool_max). This module declares ONLY dbt-specific
knobs under ``settings.DbtOracle.*`` — never a second copy of the Oracle
connection fields.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic_settings import SettingsConfigDict

# NOTE (multi-agent): mro-rn88 — inherit FlextDbOracleSettings so Oracle connection
# scalars come from settings.DbOracle.* (SSOT); FlextMeltanoSettings adds the dbt/
# meltano runtime surface. No duplicated oracle_* / pool_* fields here.
from flext_db_oracle import FlextDbOracleSettings
from flext_meltano import FlextMeltanoSettings, m


class FlextDbtOracleSettings(FlextDbOracleSettings, FlextMeltanoSettings):
    """DBT Oracle settings; connection via ``DbOracle.*``, dbt knobs via ``DbtOracle.*``."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_",
        env_nested_delimiter="__",
        extra="ignore",
        populate_by_name=True,
    )

    class _DbtOracle(m.BaseModel):
        """dbt-specific knobs only (Oracle connection lives in ``DbOracle``)."""

        schema_name: Annotated[str, m.Field(default="", description="Target schema name")]
        materialization: Annotated[
            str, m.Field(default="table", description="DBT materialization")
        ]
        nls_lang: Annotated[
            str,
            m.Field(
                default="AMERICAN_AMERICA.AL32UTF8", description="Oracle NLS language"
            ),
        ]
        nls_date_format: Annotated[
            str, m.Field(default="YYYY-MM-DD", description="Oracle NLS date format")
        ]
        search_path: Annotated[str, m.Field(default="", description="Schema search path")]
        enable_metrics: Annotated[
            bool, m.Field(default=False, description="Enable metrics collection")
        ]
        dbt_log_level: Annotated[
            str, m.Field(default="INFO", description="Runtime log verbosity")
        ]
        enable_sql_logging: Annotated[
            bool, m.Field(default=False, description="Enable SQL query logging")
        ]

    if TYPE_CHECKING:
        DbtOracle: _DbtOracle
    else:
        DbtOracle: _DbtOracle = m.Field(
            default_factory=_DbtOracle, description="Namespaced dbt-specific settings."
        )


settings: FlextDbtOracleSettings = FlextDbtOracleSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_dbt_oracle import settings``."""

__all__: list[str] = ["FlextDbtOracleSettings", "settings"]
