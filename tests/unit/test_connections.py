"""Tests for Oracle connection primitives.

Behavioral tests for the OracleConnectionConfig public contract: default field
values, custom field values, the ``database_identifier`` / ``dsn`` computed
fields, their precedence invariants, serialization idempotence, and the
validation error path. No implementation details are exercised.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_tests import tm
from tests import c, m


class TestsFlextDbtOracleConnections:
    """Behavioral suite for the OracleConnectionConfig public contract."""

    def test_defaults_expose_documented_field_values(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig()

        tm.that(config.host, eq="localhost")
        tm.that(config.port, eq=1521)
        tm.that(config.service_name, eq="XEPDB1")
        tm.that(config.sid, none=True)
        tm.that(config.protocol, eq="tcp")
        tm.that(config.username, eq="")

    def test_custom_values_are_preserved_on_public_fields(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="db.example.com",
            port=1522,
            service_name="PROD",
            username="admin",
            password="secret",
            protocol="tcps",
        )

        tm.that(config.host, eq="db.example.com")
        tm.that(config.port, eq=1522)
        tm.that(config.service_name, eq="PROD")
        tm.that(config.username, eq="admin")
        tm.that(config.protocol, eq="tcps")

    @pytest.mark.parametrize(
        ("sid", "service_name", "expected"),
        [
            (None, "XEPDB1", "XEPDB1"),
            (None, "PROD", "PROD"),
            ("XE", "XEPDB1", "XE"),
            ("ORCL", "PROD", "ORCL"),
        ],
    )
    def test_database_identifier_prefers_sid_over_service_name(
        self, sid: str | None, service_name: str, expected: str
    ) -> None:
        config = m.DbtOracle.OracleConnectionConfig(sid=sid, service_name=service_name)

        tm.that(config.database_identifier, eq=expected)

    def test_dsn_uses_service_name_path_when_no_sid(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            port=1521,
            service_name="XEPDB1",
            username="testuser",
            password="testpass",
        )

        tm.that(config.dsn, eq="tcp://testuser:***@localhost:1521/XEPDB1")

    def test_dsn_uses_sid_path_when_sid_present(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            port=1521,
            sid="XE",
            username="testuser",
            password="testpass",
        )

        tm.that(config.dsn, eq="tcp://testuser:***@localhost:1521:XE")

    def test_dsn_never_leaks_plaintext_password(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            username="testuser", password="topsecret", service_name="XEPDB1"
        )

        tm.that(config.dsn, lacks="topsecret")
        tm.that(config.dsn, has=":***@")

    @pytest.mark.parametrize("protocol", ["tcp", "tcps"])
    def test_dsn_honours_configured_protocol_scheme(self, protocol: str) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            protocol=protocol, host="h", port=1521, service_name="SVC"
        )

        assert config.dsn.startswith(f"{protocol}://")

    def test_model_dump_exposes_computed_fields(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            sid="XE", username="u", password="p"
        )
        dumped = config.model_dump()

        tm.that(dumped["database_identifier"], eq="XE")
        tm.that(dumped["dsn"], eq=config.dsn)

    def test_computed_fields_are_idempotent(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(service_name="XEPDB1")

        tm.that(config.dsn, eq=config.dsn)
        tm.that(config.database_identifier, eq=config.database_identifier)

    @pytest.mark.parametrize("port", [0, -1])
    def test_out_of_range_port_raises_validation_error(self, port: int) -> None:
        with pytest.raises(c.ValidationError, match="greater than or equal to 1"):
            _ = m.DbtOracle.OracleConnectionConfig(port=port)
