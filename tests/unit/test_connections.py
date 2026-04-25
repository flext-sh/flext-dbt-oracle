"""Tests for Oracle connection primitives.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_dbt_oracle import FlextDbtOracleConnections
from tests import c, m


class TestsFlextDbtOracleConnections:
    """Test suite for OracleConnectionConfig class."""

    def test_default_values(self) -> None:
        settings = m.DbtOracle.OracleConnectionConfig()
        assert settings.host == "localhost"
        assert settings.port == 1521
        assert settings.service_name == "XEPDB1"
        assert settings.sid is None
        assert settings.protocol == "tcp"

    def test_custom_values(self) -> None:
        settings = m.DbtOracle.OracleConnectionConfig(
            host="db.example.com",
            port=1522,
            service_name="PROD",
            username="admin",
            password="secret",
            protocol="tcps",
        )
        assert settings.host == "db.example.com"
        assert settings.port == 1522
        assert settings.service_name == "PROD"
        assert settings.username == "admin"
        assert settings.protocol == "tcps"

    def test_get_database_identifier_service_name(self) -> None:
        settings = m.DbtOracle.OracleConnectionConfig(service_name="XEPDB1")
        assert settings.database_identifier == "XEPDB1"

    def test_get_database_identifier_sid(self) -> None:
        settings = m.DbtOracle.OracleConnectionConfig(sid="XE")
        assert settings.database_identifier == "XE"

    def test_get_dsn_with_service_name(self) -> None:
        settings = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            port=1521,
            service_name="XEPDB1",
            username="testuser",
            password="testpass",
        )
        assert settings.dsn == "tcp://testuser:***@localhost:1521/XEPDB1"

    def test_get_dsn_with_sid(self) -> None:
        settings = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            port=1521,
            sid="XE",
            username="testuser",
            password="testpass",
        )
        assert settings.dsn == "tcp://testuser:***@localhost:1521:XE"

    def test_port_validation(self) -> None:
        port: int = 0
        with pytest.raises(c.ValidationError, match="greater than or equal to 1"):
            _ = m.DbtOracle.OracleConnectionConfig(port=port)

    """Test suite for the public connection facade builder."""

    def test_basic_build(self) -> None:
        settings = FlextDbtOracleConnections.build_oracle_connection_config(
            host="localhost",
            username="testuser",
            password="testpass",
        )
        assert isinstance(settings, m.DbtOracle.OracleConnectionConfig)
        assert settings.host == "localhost"
        assert settings.username == "testuser"
        assert settings.service_name == "XEPDB1"

    def test_build_with_sid(self) -> None:
        settings = FlextDbtOracleConnections.build_oracle_connection_config(
            host="localhost",
            username="testuser",
            password="testpass",
            sid="XE",
        )
        assert settings.sid == "XE"
        assert settings.database_identifier == "XE"

    def test_build_with_custom_port(self) -> None:
        settings = FlextDbtOracleConnections.build_oracle_connection_config(
            host="localhost",
            username="testuser",
            password="testpass",
            port=1522,
        )
        assert settings.port == 1522
