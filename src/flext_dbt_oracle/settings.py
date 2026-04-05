"""Settings for DBT Oracle runtime components."""

from __future__ import annotations

from pydantic_settings import SettingsConfigDict

from flext_core.settings import FlextSettings


@FlextSettings.auto_register("dbt-oracle")
class FlextDbtOracleSettings(FlextSettings):
    """DBT Oracle pipeline configuration."""

    model_config = SettingsConfigDict(env_prefix="FLEXT_DBT_ORACLE_", extra="ignore")


__all__ = ["FlextDbtOracleSettings"]
