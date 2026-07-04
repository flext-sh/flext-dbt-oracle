"""Shared service foundation for flext-dbt-oracle components.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_dbt_oracle import FlextDbtOracleSettings, c, t
from flext_meltano import FlextMeltanoDbtServiceBase, u


class FlextDbtOracleServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-oracle services."""

    settings_type: Annotated[
        type | None,
        u.Field(description="Settings class for DBT Oracle service initialization"),
    ] = FlextDbtOracleSettings
    dbt_project_name: Annotated[
        t.NonEmptyStr,
        u.Field(description="Canonical dbt project name for DBT Oracle services"),
    ] = "dbt-oracle"

    @property
    @override
    def settings(self) -> FlextDbtOracleSettings:
        """The typed dbt-oracle settings namespace."""
        return FlextDbtOracleSettings.fetch_global()

    @property
    @override
    def connection_profile(self) -> t.JsonMapping:
        """Dbt connection profile for Oracle-backed workflows."""
        active_settings = self.settings
        return {
            "type": "oracle",
            "host": active_settings.oracle_host,
            "port": active_settings.oracle_port,
            "user": active_settings.oracle_username,
            "password": active_settings.oracle_password.get_secret_value(),
            "service_name": active_settings.oracle_service_name,
            "schema": active_settings.schema_name or c.DbtOracle.DEFAULT_SCHEMA_NAME,
            "project": self.dbt_project_name,
        }


s = FlextDbtOracleServiceBase

__all__: list[str] = ["FlextDbtOracleServiceBase", "s"]
