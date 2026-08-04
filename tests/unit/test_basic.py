"""Behavioral tests for FLEXT DBT Oracle settings contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_db_oracle import FlextDbOracleSettings
from flext_dbt_oracle import FlextDbtOracleSettings, m
from flext_tests import tm


class TestsFlextDbtOracleBasic:
    """Observable public contract for FlextDbtOracle settings + connection model."""

    def test_dbt_settings_expose_namespaced_scalar_groups(self) -> None:
        """Dbt settings surface DbOracle connection scalars and DbtOracle knobs."""
        settings = FlextDbtOracleSettings()

        tm.that(settings.DbOracle.host, eq="localhost")
        tm.that(settings.DbOracle.service_name, eq="XEPDB1")
        tm.that(settings.DbtOracle.materialization, eq="table")

    def test_explicit_schema_name_is_the_target_schema(self) -> None:
        """An explicit DbtOracle.schema_name is preserved."""
        settings = FlextDbtOracleSettings.model_validate({"DbtOracle": {}})

        tm.that(settings.DbtOracle.schema_name, eq="ANALYTICS")

    def test_connection_dsn_masks_password_and_uses_service_separator(self) -> None:
        """Service-name connections use '/' and never leak the password."""
        credential = "tiger"
        config = m.DbtOracle.OracleConnectionConfig(
            host="db.example.com",
            username="scott",
            password=credential,
            port=1521,
            service_name="ORCLPDB1",
        )

        tm.that(config.dsn, eq="tcp://scott:***@db.example.com:1521/ORCLPDB1")
        tm.that(config.dsn, lacks=credential)

    def test_connection_dsn_uses_colon_separator_for_sid(self) -> None:
        """SID connections use ':' as the identifier separator."""
        config = m.DbtOracle.OracleConnectionConfig(
            host="db.example.com", username="scott", port=1521, sid="XE"
        )

        assert config.dsn.endswith(":XE")

    def test_database_identifier_prefers_service_name(self) -> None:
        """Without a SID the identifier resolves from the service name."""
        config = m.DbtOracle.OracleConnectionConfig(service_name="SVC")

        tm.that(config.database_identifier, eq="SVC")

    def test_sid_overrides_service_name_as_identifier(self) -> None:
        """When a SID is provided it wins over the service name."""
        config = m.DbtOracle.OracleConnectionConfig(service_name="SVC", sid="XE")

        tm.that(config.database_identifier, eq="XE")

    @pytest.mark.parametrize(("pool_min", "pool_max"), [(1, 10), (5, 5), (2, 3)])
    def test_valid_pool_bounds_are_accepted(self, pool_min: int, pool_max: int) -> None:
        """pool_max >= pool_min is a valid DbOracle configuration."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(pool_min=pool_min, pool_max=pool_max)
        )

        tm.that(settings.DbOracle.pool_min, eq=pool_min)
        tm.that(settings.DbOracle.pool_max, eq=pool_max)

    def test_settings_are_idempotent_under_model_dump_roundtrip(self) -> None:
        """Re-instantiating from model_dump preserves observable dbt state."""
        settings = FlextDbtOracleSettings.model_validate({"DbtOracle": {"schema_name": "SCHEMA_A", "materialization": "view"}})

        rebuilt = FlextDbtOracleSettings.model_validate(settings.model_dump())

        tm.that(rebuilt.DbtOracle.schema_name, eq=settings.DbtOracle.schema_name)
        tm.that(
            rebuilt.DbtOracle.materialization, eq=settings.DbtOracle.materialization
        )


__all__: list[str] = ["TestsFlextDbtOracleBasic"]
