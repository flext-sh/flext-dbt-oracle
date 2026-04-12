"""Settings for DBT Oracle runtime components."""

from __future__ import annotations

from typing import ClassVar

from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings


@FlextSettings.auto_register("dbt-oracle")
class FlextDbtOracleSettings(FlextSettings):
    """DBT Oracle pipeline configuration."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="FLEXT_DBT_ORACLE_",
        extra="ignore",
    )


__all__ = ["FlextDbtOracleSettings"]
