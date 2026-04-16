"""Settings for DBT Oracle runtime components."""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextSettings
from flext_dbt_oracle import m


@FlextSettings.auto_register("dbt_oracle")
class FlextDbtOracleSettings(
    m.DbtOracle.FlextDbtOracleSettings,
    FlextSettings,
):
    """DBT Oracle pipeline configuration."""

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_",
        extra="ignore",
    )


__all__: list[str] = ["FlextDbtOracleSettings"]
