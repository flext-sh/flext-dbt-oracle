"""Behavioral tests for FLEXT DBT Oracle settings contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from flext_dbt_oracle.settings import FlextDbtOracleSettings


class TestsFlextDbtOracleBasic:
    """Observable public contract for FlextDbtOracleSettings."""

    def test_defaults_expose_service_based_identifier(self) -> None:
        """Default settings resolve identifier from the Oracle service name."""
        settings = FlextDbtOracleSettings()

        assert settings.database_identifier == settings.oracle_service_name
        assert settings.effective_schema == settings.oracle_username
        assert settings.port == settings.oracle_port

    def test_sid_overrides_service_name_as_identifier(self) -> None:
        """When a SID is provided it wins over the service name."""
        settings = FlextDbtOracleSettings(sid="XE")

        assert settings.database_identifier == "XE"

    def test_explicit_schema_name_wins_over_username(self) -> None:
        """An explicit schema_name is the effective schema."""
        settings = FlextDbtOracleSettings(
            oracle_username="oracle",
            schema_name="ANALYTICS",
        )

        assert settings.effective_schema == "ANALYTICS"

    def test_connection_string_masks_password_and_uses_service_separator(
        self,
    ) -> None:
        """Service-name connections use '/' and never leak the password."""
        settings = FlextDbtOracleSettings(
            oracle_host="db.example.com",
            oracle_username="scott",
            oracle_password="tiger",
            oracle_port=1521,
            oracle_service_name="ORCLPDB1",
        )

        assert settings.connection_string == (
            "oracle://scott:***@db.example.com:1521/ORCLPDB1"
        )
        assert "tiger" not in settings.connection_string

    def test_connection_string_uses_colon_separator_for_sid(self) -> None:
        """SID connections use ':' as the identifier separator."""
        settings = FlextDbtOracleSettings(
            oracle_host="db.example.com",
            oracle_username="scott",
            oracle_port=1521,
            sid="XE",
        )

        assert settings.connection_string.endswith(":XE")

    def test_to_connection_config_reveals_secret_value(self) -> None:
        """The connection config exposes the concrete secret and identifiers."""
        settings = FlextDbtOracleSettings(
            oracle_host="h",
            oracle_username="u",
            oracle_password="s3cret",
            oracle_service_name="SVC",
            sid="XE",
            protocol="tcps",
        )

        config = settings.to_connection_config()

        assert config == {
            "host": "h",
            "port": settings.port,
            "service_name": "SVC",
            "sid": "XE",
            "username": "u",
            "password": "s3cret",
            "protocol": "tcps",
        }

    def test_to_oracle_config_roundtrips_connection_fields(self) -> None:
        """to_oracle_config carries the connection identity fields through."""
        settings = FlextDbtOracleSettings(
            oracle_host="h",
            oracle_username="u",
            oracle_password="pw",
            oracle_service_name="SVC",
            sid="XE",
            protocol="tcp",
        )

        oracle_config = settings.to_oracle_config()

        assert oracle_config.host == "h"
        assert oracle_config.username == "u"
        assert oracle_config.service_name == "SVC"
        assert oracle_config.sid == "XE"
        assert oracle_config.port == settings.port

    @pytest.mark.parametrize(
        ("pool_min", "pool_max"),
        [(1, 10), (5, 5), (2, 3)],
    )
    def test_valid_pool_bounds_are_accepted(
        self,
        pool_min: int,
        pool_max: int,
    ) -> None:
        """pool_max >= pool_min is a valid configuration."""
        settings = FlextDbtOracleSettings(
            pool_min_size=pool_min,
            pool_max_size=pool_max,
        )

        assert settings.pool_min_size == pool_min
        assert settings.pool_max_size == pool_max

    def test_pool_max_below_min_is_rejected(self) -> None:
        """pool_max < pool_min violates the model invariant."""
        with pytest.raises(ValidationError, match="Pool max size"):
            FlextDbtOracleSettings(pool_min_size=5, pool_max_size=2)

    def test_performance_settings_expose_pool_and_timeout_values(self) -> None:
        """performance_settings surfaces the configured pool/timeout knobs."""
        settings = FlextDbtOracleSettings(
            pool_min_size=2,
            pool_max_size=8,
            query_timeout=120,
            fetch_size=500,
        )

        perf = settings.performance_settings

        assert perf["pool_min_size"] == 2
        assert perf["pool_max_size"] == 8
        assert perf["query_timeout"] == 120
        assert perf["fetch_size"] == 500

    @pytest.mark.unit
    def test_settings_are_idempotent_under_model_dump_roundtrip(self) -> None:
        """Re-instantiating from model_dump preserves observable state."""
        settings = FlextDbtOracleSettings(
            oracle_host="host-a",
            oracle_username="user-a",
            schema_name="SCHEMA_A",
            sid="SID_A",
        )

        rebuilt = FlextDbtOracleSettings.model_validate(settings.model_dump())

        assert rebuilt.connection_string == settings.connection_string
        assert rebuilt.database_identifier == settings.database_identifier
        assert rebuilt.effective_schema == settings.effective_schema


__all__: list[str] = ["TestsFlextDbtOracleBasic"]
