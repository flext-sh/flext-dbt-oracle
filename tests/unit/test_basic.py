"""Behavioral tests for FLEXT DBT Oracle settings contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from flext_db_oracle import FlextDbOracleSettings
from flext_tests import tm

from flext_dbt_oracle import FlextDbtOracleSettings


class TestsFlextDbtOracleBasic:
    """Observable public contract for FlextDbtOracle settings."""

    def test_dbt_settings_expose_namespaced_scalar_groups(self) -> None:
        """Dbt settings surface DbOracle connection scalars and DbtOracle knobs."""
        settings = FlextDbtOracleSettings()

        tm.that(settings.DbOracle.host, eq="localhost")
        tm.that(settings.DbOracle.service_name, eq="XEPDB1")
        tm.that(settings.DbtOracle.materialization, eq="table")

    def test_explicit_schema_name_is_the_target_schema(self) -> None:
        """An explicit DbtOracle.schema_name is preserved."""
        settings = FlextDbtOracleSettings.model_validate({
            "DbtOracle": {"schema_name": "ANALYTICS"}
        })

        tm.that(settings.DbtOracle.schema_name, eq="ANALYTICS")

    @pytest.mark.parametrize(("pool_min", "pool_max"), [(1, 10), (5, 5), (2, 3)])
    def test_valid_pool_bounds_are_accepted(self, pool_min: int, pool_max: int) -> None:
        """pool_max >= pool_min is a valid DbOracle configuration."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                pool_min=pool_min, pool_max=pool_max
            )
        )

        tm.that(settings.DbOracle.pool_min, eq=pool_min)
        tm.that(settings.DbOracle.pool_max, eq=pool_max)

    def test_settings_are_idempotent_under_model_dump_roundtrip(self) -> None:
        """Re-instantiating from model_dump preserves observable dbt state."""
        settings = FlextDbtOracleSettings.model_validate({
            "DbtOracle": {"schema_name": "SCHEMA_A", "materialization": "view"}
        })

        rebuilt = FlextDbtOracleSettings.model_validate(settings.model_dump())

        tm.that(rebuilt.DbtOracle.schema_name, eq=settings.DbtOracle.schema_name)
        tm.that(
            rebuilt.DbtOracle.materialization, eq=settings.DbtOracle.materialization
        )
