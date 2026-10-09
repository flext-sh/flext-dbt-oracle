"""Settings for DBT Oracle — connection scalars reused from ``settings.DbOracle``.

Oracle connection + pool scalars are the SSOT of ``flext-db-oracle`` and are
inherited via MRO as ``settings.DbOracle.*`` (host/port/username/password/
service_name/sid/pool_min/pool_max). This module declares ONLY dbt-specific
knobs under ``settings.DbtOracle.*`` — never a second copy of the Oracle
connection fields.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_db_oracle import FlextDbOracleSettings
from flext_meltano import FlextMeltanoSettings, m


class FlextDbtOracleSettings(FlextDbOracleSettings, FlextMeltanoSettings):
    """DBT Oracle settings; connection via ``DbOracle.*``.

    dbt knobs live under ``DbtOracle.*``.
    """

    model_config = m.SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_",
        env_nested_delimiter="__",
        extra="ignore",
        populate_by_name=True,
    )

    class DbtOracleSettings(m.BaseModel):
        """dbt-specific knobs only (Oracle connection lives in ``DbOracle``).

        Defaults live on the assignment side (checker-visible optional
        constructor parameters).
        """

        schema_name: Annotated[
            str,
            m.Field(description="Target schema name"),
        ] = ""
        materialization: Annotated[
            str,
            m.Field(description="DBT materialization"),
        ] = "table"
        nls_lang: Annotated[
            str,
            m.Field(description="Oracle NLS language"),
        ] = "AMERICAN_AMERICA.AL32UTF8"
        nls_date_format: Annotated[
            str,
            m.Field(description="Oracle NLS date format"),
        ] = "YYYY-MM-DD"
        search_path: Annotated[
            str,
            m.Field(description="Schema search path"),
        ] = ""
        enable_metrics: Annotated[
            bool,
            m.Field(description="Enable metrics collection"),
        ] = False
        dbt_log_level: Annotated[
            str,
            m.Field(description="Runtime log verbosity"),
        ] = "INFO"
        enable_sql_logging: Annotated[
            bool,
            m.Field(description="Enable SQL query logging"),
        ] = False

    DbtOracle: DbtOracleSettings = m.Field(
        default_factory=DbtOracleSettings,
        description="Namespaced dbt-specific settings.",
    )


settings: FlextDbtOracleSettings = FlextDbtOracleSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_dbt_oracle``
import ``settings``."""

__all__: list[str] = ["FlextDbtOracleSettings", "settings"]
