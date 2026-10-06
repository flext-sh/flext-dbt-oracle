"""Behavior contract for the dbt Oracle connection profile.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_connection_profile
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import p

from flext_dbt_oracle import FlextDbtOracleServiceBase, m


class TestsFlextDbtOracleConnectionProfile:
    """Public contract of the typed dbt Oracle connection profile."""

    @staticmethod
    def test_connection_profile_returns_typed_oracle_wire_shape() -> None:
        """connection_profile returns the typed dbt Oracle wire shape."""
        profile = FlextDbtOracleServiceBase().connection_profile

        assert isinstance(profile, m.DbtOracle.DbtConnectionProfile)
        assert isinstance(profile, p.Meltano.DbtConnectionProfile)
        assert profile.model_dump(by_alias=True) == {
            "type": "oracle",
            "host": profile.host,
            "port": profile.port,
            "user": profile.user,
            "password": profile.password,
            "service_name": profile.service_name,
            "schema": profile.schema_name,
            "project": "dbt-oracle",
        }
