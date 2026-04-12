"""Settings for DBT Oracle runtime components."""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextSettings
from flext_dbt_oracle import c, m


@FlextSettings.auto_register("dbt_oracle")
class FlextDbtOracleSettings(
    m.DbtOracle.FlextDbtOracleSettings,
    FlextSettings,
):
    """DBT Oracle pipeline configuration."""

    model_config: ClassVar[c.SettingsConfigDict] = c.SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_",
        extra="ignore",
    )


__all__: list[str] = ["FlextDbtOracleSettings"]
