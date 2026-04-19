"""Shared service foundation for flext-dbt-oracle components.

Inherits from FlextMeltanoDbtServiceBase which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-oracle domain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_core import FlextSettings
from flext_dbt_oracle import FlextDbtOracleSettings, t
from flext_meltano import FlextMeltanoDbtServiceBase


class FlextDbtOracleServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-oracle services.

    Inherits dbt execution infrastructure from FlextMeltanoDbtServiceBase.
    Adds typed settings for the dbt-oracle domain.
    """

    dbt_project_name: t.NonEmptyStr = "dbt-oracle"

    def _dbt_oracle_settings(
        self,
    ) -> FlextDbtOracleSettings:
        """Return the typed dbt-oracle settings namespace."""
        return FlextSettings.fetch_global().fetch_namespace(
            "dbt_oracle", FlextDbtOracleSettings
        )

    @override
    @property
    @override
    def connection_profile(self) -> Mapping[str, t.Container]:
        """Dbt connection profile for Oracle database."""
        s = self._dbt_oracle_settings()
        return {
            "type": "oracle",
            "host": s.oracle_host,
            "port": s.oracle_port,
            "user": s.oracle_username,
            "service": s.oracle_service_name,
            "protocol": s.protocol,
            "project": self.dbt_project_name,
        }


__all__: list[str] = ["FlextDbtOracleServiceBase"]
