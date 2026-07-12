"""Behavioral tests for FLEXT DBT Oracle settings contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

# NOTE (multi-agent): mro-rn88 — Oracle connection scalars are SSOT in DbOracle.*;
# derived identifiers/dsn come from the typed OracleConnectionConfig model.
from flext_db_oracle import FlextDbOracleSettings
from flext_dbt_oracle import m
from flext_dbt_oracle._settings import FlextDbtOracleSettings


class TestsFlextDbtOracleBasic:
    """Observable public contract for FlextDbtOracle settings + connection model."""

    def test_dbt_settings_expose_namespaced_scalar_groups(self) -> None:
        """Dbt settings surface DbOracle connection scalars and DbtOracle knobs."""
        settings = FlextDbtOracleSettings()

        assert settings.DbOracle.host == "localhost"
        assert settings.DbOracle.service_name == "XEPDB1"
        assert settings.DbtOracle.materialization == "table"

    def test_explicit_schema_name_is_the_target_schema(self) -> None:
        """An explicit DbtOracle.schema_name is preserved."""
        settings = FlextDbtOracleSettings(
            DbtOracle=FlextDbtOracleSettings._DbtOracle(schema_name="ANALYTICS")
        )

        assert settings.DbtOracle.schema_name == "ANALYTICS"

    def test_connection_dsn_masks_password_and_uses_service_separator(self) -> None:
        """Service-name connections use '/' and never leak the password."""
        config = m.DbtOracle.OracleConnectionConfig(
            host="db.example.com",
            username="scott",
            password="tiger",
            port=1521,
            service_name="ORCLPDB1",
        )

        assert config.dsn == "tcp://scott:***@db.example.com:1521/ORCLPDB1"
        assert "tiger" not in config.dsn

    def test_connection_dsn_uses_colon_separator_for_sid(self) -> None:
        """SID connections use ':' as the identifier separator."""
        config = m.DbtOracle.OracleConnectionConfig(
            host="db.example.com",
            username="scott",
            port=1521,
            sid="XE",
        )

        assert config.dsn.endswith(":XE")

    def test_database_identifier_prefers_service_name(self) -> None:
        """Without a SID the identifier resolves from the service name."""
        config = m.DbtOracle.OracleConnectionConfig(service_name="SVC")

        assert config.database_identifier == "SVC"

    def test_sid_overrides_service_name_as_identifier(self) -> None:
        """When a SID is provided it wins over the service name."""
        config = m.DbtOracle.OracleConnectionConfig(service_name="SVC", sid="XE")

        assert config.database_identifier == "XE"

    @pytest.mark.parametrize(
        ("pool_min", "pool_max"),
        [(1, 10), (5, 5), (2, 3)],
    )
    def test_valid_pool_bounds_are_accepted(
        self,
        pool_min: int,
        pool_max: int,
    ) -> None:
        """pool_max >= pool_min is a valid DbOracle configuration."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings._DbOracle(
                pool_min=pool_min,
                pool_max=pool_max,
            ),
        )

        assert settings.DbOracle.pool_min == pool_min
        assert settings.DbOracle.pool_max == pool_max

    def test_settings_are_idempotent_under_model_dump_roundtrip(self) -> None:
        """Re-instantiating from model_dump preserves observable dbt state."""
        settings = FlextDbtOracleSettings(
            DbtOracle=FlextDbtOracleSettings._DbtOracle(
                schema_name="SCHEMA_A", materialization="view"
            ),
        )

        rebuilt = FlextDbtOracleSettings.model_validate(settings.model_dump())

        assert rebuilt.DbtOracle.schema_name == settings.DbtOracle.schema_name
        assert rebuilt.DbtOracle.materialization == settings.DbtOracle.materialization


__all__: list[str] = ["TestsFlextDbtOracleBasic"]
