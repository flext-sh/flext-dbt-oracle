"""Tests for Oracle connection primitives.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from flext_dbt_oracle import FlextDbtOracleConnections
from tests import m


class TestOracleConnectionConfig:
    """Test suite for OracleConnectionConfig class."""

    def test_default_values(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig()
        assert config.host == "localhost"
        assert config.port == 1521
        assert config.service_name == "XEPDB1"
        assert config.sid is None
        assert config.protocol == "tcp"

    def test_custom_values(self) -> None:
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

    def test_get_database_identifier_service_name(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(service_name="XEPDB1")
        assert config.get_database_identifier() == "XEPDB1"

    def test_get_database_identifier_sid(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(sid="XE")
        assert config.get_database_identifier() == "XE"

    def test_get_dsn_with_service_name(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            port=1521,
            service_name="XEPDB1",
            username="testuser",
            password="testpass",
        )
        assert config.get_dsn() == "tcp://testuser:***@localhost:1521/XEPDB1"

    def test_get_dsn_with_sid(self) -> None:
        config = m.DbtOracle.OracleConnectionConfig(
            host="localhost",
            port=1521,
            sid="XE",
            username="testuser",
            password="testpass",
        )
        assert config.get_dsn() == "tcp://testuser:***@localhost:1521:XE"

    def test_port_validation(self) -> None:
        port: int = 0
        with pytest.raises(ValidationError, match="greater than or equal to 1"):
            _ = m.DbtOracle.OracleConnectionConfig(port=port)


class TestBuildOracleConnectionConfig:
    """Test suite for the public connection facade builder."""

    def test_basic_build(self) -> None:
        config = FlextDbtOracleConnections.build_oracle_connection_config(
            host="localhost",
            username="testuser",
            password="testpass",
        )
        assert isinstance(config, m.DbtOracle.OracleConnectionConfig)
        assert config.host == "localhost"
        assert config.username == "testuser"
        assert config.service_name == "XEPDB1"

    def test_build_with_sid(self) -> None:
        config = FlextDbtOracleConnections.build_oracle_connection_config(
            host="localhost",
            username="testuser",
            password="testpass",
            sid="XE",
        )
        assert config.sid == "XE"
        assert config.get_database_identifier() == "XE"

    def test_build_with_custom_port(self) -> None:
        config = FlextDbtOracleConnections.build_oracle_connection_config(
            host="localhost",
            username="testuser",
            password="testpass",
            port=1522,
        )
        assert config.port == 1522
