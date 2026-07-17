"""Shared service foundation for flext-dbt-oracle components.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

# NOTE (multi-agent): settings-fallout lane (mro-rn88) — import the module `settings`
# singleton for the strict `from <pkg> import settings` access form (was bare/undefined).
from flext_dbt_oracle import FlextDbtOracleSettings, c, m, r, settings, t, u
from flext_meltano import FlextMeltanoDbtServiceBase, p


class FlextDbtOracleServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-oracle services."""

    dbt_project_name: Annotated[
        t.NonEmptyStr,
        u.Field(description="Canonical dbt project name for DBT Oracle services"),
    ] = "dbt-oracle"

    @classmethod
    def _runtime_bootstrap_options(cls) -> p.RuntimeBootstrapOptions:
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

    def generate_staging_models(
        self,
        source_tables: t.StrSequence,
    ) -> p.Result[m.DbtOracle.ModelGenerationResult]:
        """Generate DBT staging models for the given source tables."""
        models = u.DbtOracle.ModelBuilder.generate_staging_models(source_tables)
        return r[m.DbtOracle.ModelGenerationResult].ok(
            m.DbtOracle.ModelGenerationResult(
                models_generated=len(models),
                model_names=tuple(model.name for model in models),
            ),
        )


s = FlextDbtOracleServiceBase

__all__: list[str] = ["FlextDbtOracleServiceBase", "s"]
