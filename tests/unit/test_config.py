"""Behavioral tests for FlextDbtOracleSettings public contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal, cast

import pytest

from flext_dbt_oracle.settings import FlextDbtOracleSettings
from tests.constants import c
from tests.typings import t


class TestsFlextDbtOracleConfig:
    """Verify the observable configuration contract of FlextDbtOracleSettings."""

    def setup_method(self) -> None:
        """Reset singleton before each test to avoid cross-test pollution."""
        FlextDbtOracleSettings.reset_for_testing()

    @staticmethod
    def _build(**overrides: object) -> FlextDbtOracleSettings:
        """Construct settings with mandatory identity fields plus overrides."""
        base: dict[str, object] = {
            "oracle_host": "localhost",
            "oracle_username": "testuser",
            "oracle_password": t.SecretStr("testpass").get_secret_value(),
        }
        base.update(overrides)
        return FlextDbtOracleSettings.model_validate(base)

    # ------------------------------------------------------------------ #
    # Construction & field state (public model API)                       #
    # ------------------------------------------------------------------ #

    def test_explicit_fields_are_preserved_on_the_model(self) -> None:
        """Explicitly supplied fields surface unchanged via the public API."""
        settings = self._build(
            oracle_host="db.internal",
            oracle_username="svc",
            oracle_service_name="XEPDB1",
        )
        assert settings.oracle_host == "db.internal"
        assert settings.oracle_username == "svc"
        assert settings.oracle_service_name == "XEPDB1"

    def test_port_is_a_positive_integer(self) -> None:
        """The computed port exposes a usable positive integer."""
        settings = self._build(oracle_service_name="XEPDB1")
        assert isinstance(settings.port, int)
        assert settings.port > 0

    def test_defaults_are_applied_for_omitted_identity_fields(self) -> None:
        """Omitted host/username/password fall back to non-empty defaults."""
        settings = FlextDbtOracleSettings(oracle_service_name="XEPDB1")
        assert isinstance(settings.oracle_host, str)
        assert settings.oracle_host != ""
        assert isinstance(settings.oracle_username, str)
        assert settings.oracle_username != ""
        assert isinstance(settings.oracle_password, t.SecretStr)

    def test_default_service_name_present_when_neither_service_nor_sid_given(
        self,
    ) -> None:
        """A default service name is available when no identifier is supplied."""
        settings = self._build()
        assert settings.oracle_service_name is not None
        assert settings.oracle_service_name != ""

    def test_all_optional_fields_round_trip_through_public_state(self) -> None:
        """A fully populated construction exposes every override verbatim."""
        settings = self._build(
            oracle_service_name="XEPDB1",
            oracle_port=1522,
            protocol="tcps",
            ssl_server_dn_match=True,
            nls_lang="AMERICAN_AMERICA.AL32UTF8",
            nls_date_format="DD/MM/YYYY",
            search_path="schema1,schema2",
            enable_metrics=True,
            log_level=c.LogLevel.DEBUG,
            enable_sql_logging=True,
            pool_min_size=1,
            pool_max_size=20,
            pool_increment=2,
            query_timeout=600,
            fetch_size=2000,
            connect_timeout=60,
            retry_attempts=5,
            retry_delay_seconds=2.0,
        )
        assert settings.port == 1522
        assert settings.protocol == "tcps"
        assert settings.ssl_server_dn_match is True
        assert settings.nls_lang == "AMERICAN_AMERICA.AL32UTF8"
        assert settings.enable_metrics is True
        assert settings.log_level == c.LogLevel.DEBUG
        assert settings.enable_sql_logging is True
        assert settings.pool_max_size == 20
        assert settings.query_timeout == 600
        assert abs(settings.retry_delay_seconds - 2.0) < 1e-9

    def test_default_invariants_hold(self) -> None:
        """Default construction satisfies the documented value invariants."""
        settings = self._build(oracle_service_name="XEPDB1")
        assert settings.protocol in {"tcp", "tcps"}
        assert settings.materialization in {"table", "view", "incremental", "snapshot"}
        assert settings.pool_min_size >= 1
        assert settings.pool_max_size >= settings.pool_min_size
        assert settings.query_timeout > 0
        assert settings.fetch_size > 0

    # ------------------------------------------------------------------ #
    # Validation error paths                                              #
    # ------------------------------------------------------------------ #

    def test_invalid_materialization_is_rejected(self) -> None:
        """An out-of-domain materialization raises a validation error."""
        with pytest.raises(c.ValidationError, match="Input should be"):
            _ = self._build(
                oracle_service_name="XEPDB1",
                materialization=cast(
                    "Literal['incremental', 'snapshot', 'table', 'view']",
                    "invalid_type",
                ),
            )

    def test_invalid_protocol_is_rejected(self) -> None:
        """An out-of-domain protocol raises a validation error."""
        with pytest.raises(c.ValidationError, match="Input should be"):
            _ = self._build(
                oracle_service_name="XEPDB1",
                protocol=cast("Literal['tcp', 'tcps']", "invalid_protocol"),
            )

    def test_pool_max_below_min_is_rejected(self) -> None:
        """The pool-size invariant (max >= min) is enforced at construction."""
        with pytest.raises(c.ValidationError, match="Pool max size"):
            _ = self._build(
                oracle_service_name="XEPDB1",
                pool_min_size=10,
                pool_max_size=5,
            )

    def test_pool_max_equal_to_min_is_accepted(self) -> None:
        """The pool-size invariant permits the max == min boundary."""
        settings = self._build(
            oracle_service_name="XEPDB1",
            pool_min_size=5,
            pool_max_size=5,
        )
        assert settings.pool_min_size == 5
        assert settings.pool_max_size == 5

    def test_numeric_fields_retain_supplied_values(self) -> None:
        """Numeric fields accept and preserve valid in-range values."""
        settings = self._build(
            oracle_service_name="XEPDB1",
            oracle_port=1521,
            pool_min_size=1,
            pool_max_size=50,
            query_timeout=600,
            retry_delay_seconds=0.5,
        )
        assert settings.port == 1521
        assert settings.pool_min_size == 1
        assert settings.pool_max_size == 50
        assert settings.query_timeout == 600
        assert abs(settings.retry_delay_seconds - 0.5) < 1e-9

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
        self,
        materialization: c.DbtOracle.Dbt.Materialization,
    ) -> None:
        """Each supported materialization is preserved on the model."""
        settings = self._build(
            oracle_service_name="XEPDB1",
            materialization=materialization,
        )
        assert settings.materialization == materialization

    @pytest.mark.parametrize("protocol", ["tcp", "tcps"])
    def test_every_valid_protocol_is_accepted(
        self,
        protocol: Literal["tcp", "tcps"],
    ) -> None:
        """Each supported protocol is preserved on the model."""
        settings = self._build(oracle_service_name="XEPDB1", protocol=protocol)
        assert settings.protocol == protocol

    # ------------------------------------------------------------------ #
    # Derived connection identity (computed fields)                       #
    # ------------------------------------------------------------------ #

    def test_database_identifier_uses_service_name_without_sid(self) -> None:
        """Without a SID the identifier resolves to the service name."""
        settings = self._build(oracle_service_name="XEPDB1")
        assert settings.database_identifier == "XEPDB1"

    def test_database_identifier_prefers_sid_over_service_name(self) -> None:
        """A supplied SID takes precedence over the service name."""
        settings = self._build(sid="XE", oracle_service_name="XEPDB1")
        assert settings.database_identifier == "XE"

    def test_effective_schema_uses_explicit_schema_name(self) -> None:
        """An explicit schema name is the effective schema."""
        settings = self._build(oracle_service_name="XEPDB1", schema_name="TEST_SCHEMA")
        assert settings.effective_schema == "TEST_SCHEMA"

    def test_effective_schema_falls_back_to_username(self) -> None:
        """Absent a schema name the effective schema is the username."""
        settings = self._build(oracle_username="owner", oracle_service_name="XEPDB1")
        assert settings.effective_schema == "owner"

    def test_connection_string_uses_slash_separator_for_service_name(self) -> None:
        """The service-name connection string masks the password and uses '/'."""
        settings = self._build(oracle_service_name="XEPDB1")
        assert (
            settings.connection_string
            == f"oracle://testuser:***@localhost:{settings.port}/XEPDB1"
        )

    def test_connection_string_uses_colon_separator_for_sid(self) -> None:
        """The SID connection string masks the password and uses ':'."""
        settings = self._build(sid="XE")
        assert (
            settings.connection_string
            == f"oracle://testuser:***@localhost:{settings.port}:XE"
        )

    # ------------------------------------------------------------------ #
    # Conversion methods (public output contract)                         #
    # ------------------------------------------------------------------ #

    def test_to_connection_config_exposes_expected_shape(self) -> None:
        """to_connection_config returns exactly the connection keys and values."""
        settings = self._build(oracle_service_name="XEPDB1")
        conn_config = settings.to_connection_config()
        assert set(conn_config.keys()) == {
            "host",
            "port",
            "service_name",
            "sid",
            "username",
            "password",
            "protocol",
        }
        assert conn_config["host"] == "localhost"
        assert conn_config["username"] == "testuser"
        assert conn_config["service_name"] == "XEPDB1"
        assert conn_config["password"] == "testpass"

    def test_to_oracle_config_maps_identity_fields(self) -> None:
        """to_oracle_config produces a config carrying the identity fields."""
        settings = self._build(
            oracle_service_name="XEPDB1",
            pool_min_size=2,
            pool_max_size=10,
        )
        oracle_config = settings.to_oracle_config()
        assert oracle_config.host == "localhost"
        assert oracle_config.username == "testuser"
        assert oracle_config.service_name == "XEPDB1"

    def test_performance_settings_reflect_supplied_pool_values(self) -> None:
        """performance_settings exposes the tuning keys with supplied values."""
        settings = self._build(
            oracle_service_name="XEPDB1",
            pool_min_size=2,
            pool_max_size=10,
            query_timeout=300,
        )
        perf_settings = settings.performance_settings
        assert set(perf_settings.keys()) == {
            "pool_min_size",
            "pool_max_size",
            "pool_increment",
            "query_timeout",
            "fetch_size",
            "connect_timeout",
            "retry_attempts",
            "retry_delay",
        }
        assert perf_settings["pool_min_size"] == 2
        assert perf_settings["pool_max_size"] == 10
        assert perf_settings["query_timeout"] == 300

    def test_dbt_settings_reflect_schema_and_materialization(self) -> None:
        """dbt_settings maps database, schema, and the chosen materialization."""
        settings = self._build(
            oracle_service_name="XEPDB1",
            materialization=c.DbtOracle.Dbt.Materialization.TABLE,
        )
        dbt_settings = settings.dbt_settings
        assert set(dbt_settings.keys()) >= {"database", "schema", "materialization"}
        assert dbt_settings["database"] == "XEPDB1"
        assert dbt_settings["schema"] == settings.effective_schema
        assert dbt_settings["materialization"] == "table"


__all__: list[str] = ["TestsFlextDbtOracleConfig"]
