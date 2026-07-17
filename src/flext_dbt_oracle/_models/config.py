"""flext-dbt-oracle config models — typed business-rule shapes.

Frozen Pydantic shapes for the ``config/dbt_oracle.yaml`` business-rule SSOT.
The ``_config.py`` facade validates the model-less YAML slice into these
classes and exposes the ready objects under ``config.DbtOracle``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class FlextDbtOracleConfigModels:
    """Namespace of typed flext-dbt-oracle config models."""

    class Oracle(BaseModel):
        """Oracle connection defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        host: str = Field(description="Default Oracle host.")
        port: int = Field(
            ge=1,
            le=65535,
            description="Default Oracle listener port.",
        )
        service_name: str = Field(description="Default Oracle service name.")
        protocol: str = Field(description="Default Oracle connection protocol.")

    class Dbt(BaseModel):
        """DBT runtime defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        target: str = Field(description="Default DBT target.")
        profiles_dir: str = Field(description="Default DBT profiles directory.")
        materialization: str = Field(description="Default DBT materialization.")
        log_level: str = Field(description="Default DBT log level.")

    class Defaults(BaseModel):
        """DBT model defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        model_type: str = Field(description="Default model type.")
        source_name: str = Field(description="Default source name.")
        schema_name: str = Field(description="Default schema name.")

    class Formatting(BaseModel):
        """Oracle NLS formatting defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        nls_lang: str = Field(description="Oracle NLS language string.")
        nls_date_format: str = Field(description="Oracle NLS date format.")

    class Runtime(BaseModel):
        """DBT runtime behavior defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        enable_metrics: bool = Field(
            description="Whether to enable metrics collection."
        )
        enable_sql_logging: bool = Field(
            description="Whether to enable SQL query logging."
        )
        performance_recommendation_threshold: int = Field(
            ge=1,
            description="Threshold for performance recommendations.",
        )

    class DbtOracle(BaseModel):
        """Root DBT Oracle business-rule namespace."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        oracle: FlextDbtOracleConfigModels.Oracle = Field(
            description="Oracle connection defaults.",
        )
        dbt: FlextDbtOracleConfigModels.Dbt = Field(
            description="DBT runtime defaults.",
        )
        defaults: FlextDbtOracleConfigModels.Defaults = Field(
            description="DBT model defaults.",
        )
        formatting: FlextDbtOracleConfigModels.Formatting = Field(
            description="Oracle NLS formatting defaults.",
        )
        runtime: FlextDbtOracleConfigModels.Runtime = Field(
            description="DBT runtime behavior defaults.",
        )

    class Root(BaseModel):
        """Root flext-dbt-oracle config validated from ``config/*.yaml``."""

        model_config = ConfigDict(frozen=True, extra="ignore")

        DbtOracle: FlextDbtOracleConfigModels.DbtOracle = Field(
            description="DBT Oracle business-rule config namespace.",
        )


__all__: list[str] = ["FlextDbtOracleConfigModels"]
