"""Settings for DBT Oracle runtime components."""

from __future__ import annotations

from typing import ClassVar

from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings
from flext_dbt_oracle.models import FlextDbtOracleModels


@FlextSettings.auto_register("dbt_oracle")
class FlextDbtOracleSettings(
    FlextDbtOracleModels.DbtOracle.FlextDbtOracleSettings,
    FlextSettings,
):
    """DBT Oracle pipeline configuration."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_",
        extra="ignore",
    )


__all__ = ["FlextDbtOracleSettings"]
