"""Shared service foundation for flext-dbt-oracle components.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

# NOTE (multi-agent): settings-fallout lane (mro-rn88) — import the module `settings`
# singleton for the strict `from <pkg> import settings` access form (was bare/undefined).
from flext_dbt_oracle import FlextDbtOracleSettings, c, m, settings, t
from flext_meltano import FlextMeltanoDbtServiceBase, p, u


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
    def connection_profile(self) -> p.Meltano.DbtConnectionProfile:
        """Dbt connection profile for Oracle-backed workflows."""
        # NOTE (multi-agent): mro-rn88 ADR-006 thin-driver — connection scalars from
        # settings.DbOracle.* (SSOT, no duplication); dbt schema from settings.DbtOracle.
        db = settings.DbOracle
        return m.DbtOracle.DbtConnectionProfile(
            host=db.host,
            port=db.port,
            user=db.username,
            password=db.password,
            service_name=db.service_name,
            schema_name=settings.DbtOracle.schema_name
            or c.DbtOracle.DEFAULT_SCHEMA_NAME,
            project=self.dbt_project_name,
        )


s = FlextDbtOracleServiceBase

__all__: list[str] = ["FlextDbtOracleServiceBase", "s"]
