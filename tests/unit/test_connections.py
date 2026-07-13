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

from tests import c, m


class TestsFlextDbtOracleConnections:
    """Behavioral suite for the OracleConnectionConfig public contract."""

    def test_defaults_expose_documented_field_values(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig()

        assert config.host == "localhost"
        assert config.port == 1521
        assert config.service_name == "XEPDB1"
        assert config.sid is None
        assert config.protocol == "tcp"
        assert config.username == ""

    def test_custom_values_are_preserved_on_public_fields(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="db.example.com",
            port=1522,
            service_name="PROD",
            username="admin",
            password="secret",
            protocol="tcps",
        )

        assert config.host == "db.example.com"
        assert config.port == 1522
        assert config.service_name == "PROD"
        assert config.username == "admin"
        assert config.protocol == "tcps"

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
        self,
        sid: str | None,
        service_name: str,
        expected: str,
    ) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            sid=sid,
            service_name=service_name,
        )

        assert config.database_identifier == expected

    def test_dsn_uses_service_name_path_when_no_sid(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            port=1521,
            service_name="XEPDB1",
            username="testuser",
            password="testpass",
        )

        assert config.dsn == "tcp://testuser:***@localhost:1521/XEPDB1"

    def test_dsn_uses_sid_path_when_sid_present(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            port=1521,
            sid="XE",
            username="testuser",
            password="testpass",
        )

        assert config.dsn == "tcp://testuser:***@localhost:1521:XE"

    def test_dsn_never_leaks_plaintext_password(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            username="testuser",
            password="topsecret",
            service_name="XEPDB1",
        )

        assert "topsecret" not in config.dsn
        assert ":***@" in config.dsn

    @pytest.mark.parametrize("protocol", ["tcp", "tcps"])
    def test_dsn_honours_configured_protocol_scheme(self, protocol: str) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            protocol=protocol,
            host="h",
            port=1521,
            service_name="SVC",
        )

        assert config.dsn.startswith(f"{protocol}://")

    def test_model_dump_exposes_computed_fields(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            sid="XE",
            username="u",
            password="p",
        )
        dumped = config.model_dump()

        assert dumped["database_identifier"] == "XE"
        assert dumped["dsn"] == config.dsn

    def test_computed_fields_are_idempotent(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(service_name="XEPDB1")

        assert config.dsn == config.dsn
        assert config.database_identifier == config.database_identifier

    @pytest.mark.parametrize("port", [0, -1])
    def test_out_of_range_port_raises_validation_error(self, port: int) -> None:
        with pytest.raises(
            c.ValidationError,
            match="greater than or equal to 1",
        ):
            _ = m.DbtOracle.OracleConnectionConfig(port=port)
