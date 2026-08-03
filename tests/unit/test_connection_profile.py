"""Behavior contract for the dbt Oracle connection profile."""

from __future__ import annotations

from flext_dbt_oracle import FlextDbtOracleServiceBase, m
from flext_meltano import p


def test_connection_profile_returns_typed_oracle_wire_shape() -> None:
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
