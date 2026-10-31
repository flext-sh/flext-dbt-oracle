"""Behavioral tests for FlextDbtOracleSettings public contract.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""
# NOTE (multi-agent): mro-rn88 — settings dedup: Oracle connection scalars are SSOT
# in settings.DbOracle.* (inherited from flext-db-oracle); settings.DbtOracle.* holds
# ONLY dbt-only knobs (schema_name, materialization, nls_*, search_path, log/metrics).

from __future__ import annotations

import pytest
from flext_db_oracle import FlextDbOracleSettings

from flext_dbt_oracle import FlextDbtOracleSettings
from tests import c, config, m, t, tm
from tests.unit._config.construction import TestsFlextDbtOracleConfigConstructionPart


class TestsFlextDbtOracleConfig(TestsFlextDbtOracleConfigConstructionPart):
    """Verify the observable configuration contract of FlextDbtOracleSettings."""

    @staticmethod
    @pytest.mark.parametrize(
        "payload", [{}, {"policy": None}, {"policy": [False, {"limit": 3}]}]
    )
    def test_open_config_namespace_contract(payload: t.JsonDict) -> None:
        """Shared namespace preserves arbitrary values and rejects mutation."""
        namespace = type(config.DbtOracle).model_validate(payload)
        tm.that(
            namespace.model_dump(mode="json"),
            eq=payload,
        )
        tm.rejects_assignment(
            namespace, "policy", "changed", expected=m.ValidationError
        )
        schemas = (
            namespace.model_json_schema(),
            m.Meltano.MeltanoNamespace.model_json_schema(),
        )
        for schema in schemas:
            del schema["title"]
        tm.that(schemas[0], eq=schemas[1])

    @staticmethod
    def setup_method() -> None:
        """Reset singleton before each test to avoid cross-test pollution."""
        FlextDbtOracleSettings.reset_for_testing()

    @staticmethod
    def test_connection_scalars_come_from_dboracle_namespace() -> None:
        """Oracle connection scalars are supplied via the DbOracle namespace."""
        settings = FlextDbtOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                host="db.internal",
                username="svc",
                service_name="XEPDB1",
            ),
        )
        tm.that(settings.DbOracle.host, eq="db.internal")
        tm.that(settings.DbOracle.username, eq="svc")
        tm.that(settings.DbOracle.service_name, eq="XEPDB1")

    @staticmethod
    def test_port_is_a_positive_integer() -> None:
        """The Oracle port exposes a usable positive integer."""
        db = FlextDbtOracleSettings().DbOracle
        tm.that(db.port, is_=int)
        tm.that(db.port > 0, truth=True)

    @staticmethod
    def test_defaults_are_applied_for_omitted_identity_fields() -> None:
        """Omitted host/username/password fall back to documented defaults."""
        db = FlextDbtOracleSettings().DbOracle
        tm.that(db.host, is_=str)
        tm.that(db.host, ne="")
        tm.that(db.username, is_=str)
        tm.that(db.username, ne="")
        tm.that(db.password, is_=str)

    @staticmethod
    def test_default_service_name_present() -> None:
        """A default service name is available when no identifier is supplied."""
        db = FlextDbtOracleSettings().DbOracle
        tm.that(db.service_name, ne="")

    @staticmethod
    def test_dbt_only_knobs_round_trip_through_namespace() -> None:
        """A fully populated dbt construction exposes every override verbatim."""
        oracle = FlextDbtOracleSettings.model_validate({
            "DbtOracle": {
                "nls_lang": "AMERICAN_AMERICA.AL32UTF8",
                "nls_date_format": "DD/MM/YYYY",
                "search_path": "schema1,schema2",
                "enable_metrics": True,
                "enable_sql_logging": True,
                "dbt_log_level": "DEBUG",
            },
        }).DbtOracle
        tm.that(oracle.nls_lang, eq="AMERICAN_AMERICA.AL32UTF8")
        tm.that(oracle.nls_date_format, eq="DD/MM/YYYY")
        tm.that(oracle.search_path, eq="schema1,schema2")
        tm.ok(oracle.enable_metrics)
        tm.ok(oracle.enable_sql_logging)
        tm.that(oracle.dbt_log_level, eq="DEBUG")

    @staticmethod
    def test_default_namespaces_follow_their_declared_scalar_models() -> None:
        """Namespaces retain upstream scalar types and declared materializations."""
        settings = FlextDbtOracleSettings()
        db = tm.instance(settings.DbOracle, FlextDbOracleSettings.DbOracleSettings)
        tm.that(
            settings.DbtOracle.materialization in c.DbtOracle.Dbt.Materialization,
            truth=True,
        )
        tm.that(db.pool_min, is_=int)
        tm.that(db.pool_max, is_=int)

    @staticmethod
    @pytest.mark.parametrize(("pool_min", "pool_max"), [(0, 1), (3, 7), (11, 11)])
    def test_pool_scalars_preserve_the_upstream_namespace_contract(
        pool_min: int, pool_max: int
    ) -> None:
        """Inherited settings preserve supplied pool values, including zero."""
        supplied = FlextDbOracleSettings.DbOracleSettings(
            pool_min=pool_min,
            pool_max=pool_max,
        )
        settings = FlextDbtOracleSettings(DbOracle=supplied)

        db = tm.instance(settings.DbOracle, FlextDbOracleSettings.DbOracleSettings)
        tm.that(db.pool_min, eq=pool_min)
        tm.that(db.pool_max, eq=pool_max)

    @staticmethod
    def test_materialization_is_a_free_scalar_string() -> None:
        # NOTE (multi-agent): mro-rn88 — per ADR-005 dbt knobs are SIMPLE scalars;
        # materialization is a plain str (domain checks belong at the consumer).
        """Materialization accepts arbitrary strings (scalar settings)."""
        oracle = FlextDbtOracleSettings.model_validate({
            "DbtOracle": {"materialization": "custom"},
        }).DbtOracle
        tm.that(oracle.materialization, eq="custom")

    @staticmethod
    def test_pool_bounds_round_trip_through_dboracle() -> None:
        """Pool bounds are DbOracle scalars preserved at construction."""
        settings = FlextDbtOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(pool_min=5, pool_max=5),
        )
        tm.that(settings.DbOracle.pool_min, eq=5)
        tm.that(settings.DbOracle.pool_max, eq=5)

    @staticmethod
    def test_numeric_fields_retain_supplied_values() -> None:
        """Numeric DbOracle fields accept and preserve valid in-range values."""
        settings = FlextDbtOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                port=1521,
                pool_min=1,
                pool_max=50,
                timeout=60,
            ),
        )
        tm.that(settings.DbOracle.port, eq=1521)
        tm.that(settings.DbOracle.pool_min, eq=1)
        tm.that(settings.DbOracle.pool_max, eq=50)
        tm.that(settings.DbOracle.timeout, eq=60)

    @staticmethod
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
        materialization: c.DbtOracle.Dbt.Materialization,
    ) -> None:
        """Each supported materialization is preserved on the namespace."""
        oracle = FlextDbtOracleSettings.model_validate({
            "DbtOracle": {"materialization": materialization},
        }).DbtOracle
        tm.that(oracle.materialization, eq=materialization)

    @staticmethod
    def test_sid_and_service_name_coexist_on_dboracle() -> None:
        """Both SID and service name are retained as DbOracle scalar fields."""
        settings = FlextDbtOracleSettings(
            DbOracle=FlextDbOracleSettings.DbOracleSettings(
                sid="XE",
                service_name="XEPDB1",
            ),
        )
        tm.that(settings.DbOracle.sid, eq="XE")
        tm.that(settings.DbOracle.service_name, eq="XEPDB1")

    @staticmethod
    def test_schema_name_preserves_declared_defaults_and_override() -> None:
        """schema_name preserves its typed default owner and explicit input."""
        defaults = FlextDbtOracleSettings.DbtOracleSettings()
        selected = FlextDbtOracleSettings(DbtOracle=defaults)
        tm.that(selected.DbtOracle.schema_name, eq=defaults.schema_name)
        oracle = FlextDbtOracleSettings.model_validate({
            "DbtOracle": {"schema_name": "TEST_SCHEMA"},
        }).DbtOracle
        tm.that(oracle.schema_name, eq="TEST_SCHEMA")
