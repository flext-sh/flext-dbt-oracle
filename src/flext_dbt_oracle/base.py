"""Shared service foundation for flext-dbt-oracle components.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_dbt_oracle import FlextDbtOracleSettings, c, m, t
from flext_meltano import FlextMeltanoDbtServiceBase, u


class FlextDbtOracleServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-oracle services."""

    dbt_project_name: Annotated[
        t.NonEmptyStr,
        u.Field(description="Canonical dbt project name for DBT Oracle services"),
    ] = "dbt-oracle"

    @classmethod
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        """Return runtime bootstrap options for DBT Oracle services."""
        return m.RuntimeBootstrapOptions(settings_type=FlextDbtOracleSettings)

    @property
    @override
    def settings(self) -> FlextDbtOracleSettings:
        """The typed dbt-oracle settings namespace."""
        return settings

    @property
    @override
    def connection_profile(self) -> t.JsonMapping:
        """Dbt connection profile for Oracle-backed workflows."""
        active_settings = settings
        return {
            "type": "oracle",
            "host": active_settings.DbtOracle.oracle_host,
            "port": active_settings.DbtOracle.oracle_port,
            "user": active_settings.DbtOracle.oracle_username,
            "password": active_settings.DbtOracle.oracle_password,
            "service_name": active_settings.DbtOracle.oracle_service_name,
            "schema": active_settings.DbtOracle.schema_name or c.DbtOracle.DEFAULT_SCHEMA_NAME,
            "project": self.dbt_project_name,
        }


s = FlextDbtOracleServiceBase

__all__: list[str] = ["FlextDbtOracleServiceBase", "s"]
