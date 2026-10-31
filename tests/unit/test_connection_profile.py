"""Behavior contract for the dbt Oracle connection profile.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_connection_profile
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle import FlextDbtOracleServiceBase
from tests import c, m, p, tm


class TestsFlextDbtOracleConnectionProfile:
    """Public contract of the typed dbt Oracle connection profile."""

    @staticmethod
    def test_connection_profile_returns_typed_oracle_wire_shape() -> None:
        """connection_profile returns the typed dbt Oracle wire shape."""
        service = FlextDbtOracleServiceBase()
        profile = tm.instance(
            service.connection_profile, m.DbtOracle.DbtConnectionProfile
        )

        tm.that(profile, is_=p.Meltano.DbtConnectionProfile)
        tm.that(
            profile.model_dump(by_alias=True),
            eq={
                "type": "oracle",
                "host": profile.host,
                "port": profile.port,
                "user": profile.user,
                "password": profile.password,
                c.ContextKey.SERVICE_NAME: profile.service_name,
                "schema": profile.schema_name,
                "project": service.dbt_project_name,
            },
        )
