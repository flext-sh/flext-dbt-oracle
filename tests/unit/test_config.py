"""Behavioral tests for FlextDbtOracleSettings public contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""
# NOTE (multi-agent): mro-rn88 — settings dedup: Oracle connection scalars are SSOT
# in settings.DbOracle.* (inherited from flext-db-oracle); settings.DbtOracle.* holds
# ONLY dbt-only knobs (schema_name, materialization, nls_*, search_path, log/metrics).

from __future__ import annotations

import pytest
from flext_tests import tm

from flext_db_oracle import FlextDbOracleSettings
from flext_dbt_oracle._settings import FlextDbtOracleSettings
from tests import c


class TestsFlextDbtOracleConfig:
    """Verify the observable configuration contract of FlextDbtOracleSettings."""

    def setup_method(self) -> None:
        """Reset singleton before each test to avoid cross-test pollution."""
        FlextDbtOracleSettings.reset_for_testing()

    def test_connection_scalars_come_from_dboracle_namespace(self) -> None:
        """Oracle connection scalars are supplied via the DbOracle namespace."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings._DbOracle(
                host="db.internal", username="svc", service_name="XEPDB1"
            )
        )
        tm.that(settings.DbOracle.host, eq="db.internal")
        tm.that(settings.DbOracle.username, eq="svc")
        tm.that(settings.DbOracle.service_name, eq="XEPDB1")

    def test_port_is_a_positive_integer(self) -> None:
        """The Oracle port exposes a usable positive integer."""
        db = FlextDbtOracleSettings().DbOracle
        tm.that(db.port, is_=int)
        assert db.port > 0

    def test_defaults_are_applied_for_omitted_identity_fields(self) -> None:
        """Omitted host/username/password fall back to documented defaults."""
        db = FlextDbtOracleSettings().DbOracle
        tm.that(db.host, is_=str)
        tm.that(db.host, ne="")
        tm.that(db.username, is_=str)
        tm.that(db.username, ne="")
        tm.that(db.password, is_=str)

    def test_default_service_name_present(self) -> None:
        """A default service name is available when no identifier is supplied."""
        db = FlextDbtOracleSettings().DbOracle
        tm.that(db.service_name, ne="")

    def test_dbt_only_knobs_round_trip_through_namespace(self) -> None:
        """A fully populated dbt construction exposes every override verbatim."""
        oracle = FlextDbtOracleSettings(
            DbtOracle=FlextDbtOracleSettings._DbtOracle(
                nls_lang="AMERICAN_AMERICA.AL32UTF8",
                nls_date_format="DD/MM/YYYY",
                search_path="schema1,schema2",
                enable_metrics=True,
                enable_sql_logging=True,
                dbt_log_level="DEBUG",
            )
        ).DbtOracle
        tm.that(oracle.nls_lang, eq="AMERICAN_AMERICA.AL32UTF8")
        tm.that(oracle.nls_date_format, eq="DD/MM/YYYY")
        tm.that(oracle.search_path, eq="schema1,schema2")
        tm.that(oracle.enable_metrics, eq=True)
        tm.that(oracle.enable_sql_logging, eq=True)
        tm.that(oracle.dbt_log_level, eq="DEBUG")

    def test_default_invariants_hold(self) -> None:
        """Default construction satisfies the documented value invariants."""
        settings = FlextDbtOracleSettings()
        tm.that(
            {"table", "view", "incremental", "snapshot"},
            has=settings.DbtOracle.materialization,
        )
        assert settings.DbOracle.pool_min >= 1
        assert settings.DbOracle.pool_max >= settings.DbOracle.pool_min

    def test_materialization_is_a_free_scalar_string(self) -> None:
        # NOTE (multi-agent): mro-rn88 — per ADR-005 dbt knobs are SIMPLE scalars;
        # materialization is a plain str (domain checks belong at the consumer).
        """Materialization accepts arbitrary strings (scalar settings)."""
        oracle = FlextDbtOracleSettings(
            DbtOracle=FlextDbtOracleSettings._DbtOracle(materialization="custom")
        ).DbtOracle
        tm.that(oracle.materialization, eq="custom")

    def test_pool_bounds_round_trip_through_dboracle(self) -> None:
        """Pool bounds are DbOracle scalars preserved at construction."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings._DbOracle(pool_min=5, pool_max=5)
        )
        tm.that(settings.DbOracle.pool_min, eq=5)
        tm.that(settings.DbOracle.pool_max, eq=5)

    def test_numeric_fields_retain_supplied_values(self) -> None:
        """Numeric DbOracle fields accept and preserve valid in-range values."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings._DbOracle(
                port=1521, pool_min=1, pool_max=50, timeout=60
            )
        )
        tm.that(settings.DbOracle.port, eq=1521)
        tm.that(settings.DbOracle.pool_min, eq=1)
        tm.that(settings.DbOracle.pool_max, eq=50)
        tm.that(settings.DbOracle.timeout, eq=60)

    @pytest.mark.parametrize(
        "materialization",
        [
            c.DbtOracle.Dbt.Materialization.TABLE,
            c.DbtOracle.Dbt.Materialization.VIEW,
            c.DbtOracle.Dbt.Materialization.INCREMENTAL,
            c.DbtOracle.Dbt.Materialization.SNAPSHOT,
        ],
    )
    def test_every_valid_materialization_is_accepted(
        self, materialization: c.DbtOracle.Dbt.Materialization
    ) -> None:
        """Each supported materialization is preserved on the namespace."""
        oracle = FlextDbtOracleSettings(
            DbtOracle=FlextDbtOracleSettings._DbtOracle(materialization=materialization)
        ).DbtOracle
        tm.that(oracle.materialization, eq=materialization)

    def test_sid_and_service_name_coexist_on_dboracle(self) -> None:
        """Both SID and service name are retained as DbOracle scalar fields."""
        settings = FlextDbOracleSettings(
            DbOracle=FlextDbOracleSettings._DbOracle(sid="XE", service_name="XEPDB1")
        )
        tm.that(settings.DbOracle.sid, eq="XE")
        tm.that(settings.DbOracle.service_name, eq="XEPDB1")

    def test_schema_name_defaults_empty_and_accepts_override(self) -> None:
        """schema_name is an empty-default scalar overridable at construction."""
        tm.that(FlextDbtOracleSettings().DbtOracle.schema_name, eq="")
        oracle = FlextDbtOracleSettings(
            DbtOracle=FlextDbtOracleSettings._DbtOracle(schema_name="TEST_SCHEMA")
        ).DbtOracle
        tm.that(oracle.schema_name, eq="TEST_SCHEMA")


__all__: list[str] = ["TestsFlextDbtOracleConfig"]
