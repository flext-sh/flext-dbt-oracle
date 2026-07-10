"""Validation tests for Oracle DBT settings."""

from __future__ import annotations

from typing import Literal, cast

import pytest

from flext_dbt_oracle._settings import FlextDbtOracleSettings
from tests.constants import c
from tests.typings import t


class FlextDbtOracleConfigValidationPart:
    """Configuration validation coverage."""

    def test_config_validation_missing_host(self) -> None:
        """Test default host is applied when not provided explicitly."""
        settings = FlextDbtOracleSettings(
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
            oracle_service_name="XEPDB1",
        )
        assert isinstance(settings.oracle_host, str)
        assert settings.oracle_host != ""

    def test_config_validation_missing_username(self) -> None:
        """Test default username is applied when not provided explicitly."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
            oracle_service_name="XEPDB1",
        )
        assert isinstance(settings.oracle_username, str)
        assert settings.oracle_username != ""

    def test_config_validation_missing_password(self) -> None:
        """Test default password is applied when not provided explicitly."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_service_name="XEPDB1",
        )
        assert isinstance(settings.oracle_password, t.SecretStr)

    def test_config_validation_invalid_materialization(self) -> None:
        """Test validation fails for invalid materialization."""
        materialization: str = "invalid_type"
        with pytest.raises(c.ValidationError, match="Input should be"):
            _ = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=t.SecretStr("testpass").get_secret_value(),
                oracle_service_name="XEPDB1",
                materialization=cast(
                    "Literal['incremental', 'snapshot', 'table', 'view']",
                    materialization,
                ),
            )

    def test_config_validation_invalid_protocol(self) -> None:
        """Test validation fails for invalid protocol."""
        protocol: str = "invalid_protocol"
        with pytest.raises(c.ValidationError, match="Input should be"):
            _ = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=t.SecretStr("testpass").get_secret_value(),
                oracle_service_name="XEPDB1",
                protocol=cast("Literal['tcp', 'tcps']", protocol),
            )

    def test_config_validation_pool_sizes(self) -> None:
        """Test validation of pool sizes."""
        with pytest.raises(c.ValidationError, match="Pool max size"):
            _ = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=t.SecretStr("testpass").get_secret_value(),
                oracle_service_name="XEPDB1",
                pool_min_size=10,
                pool_max_size=5,
            )

    def test_config_field_validation_ranges(self) -> None:
        """Test field validation for numeric ranges."""
        settings = FlextDbtOracleSettings(
            oracle_host="localhost",
            oracle_username="testuser",
            oracle_password=t.SecretStr("testpass").get_secret_value(),
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

    def test_config_materialization_validation_all_valid_types(self) -> None:
        """Test all valid materialization types."""
        materialization_enum = c.DbtOracle.Dbt.Materialization
        valid_materializations: t.SequenceOf[materialization_enum] = [
            materialization_enum.TABLE,
            materialization_enum.VIEW,
            materialization_enum.INCREMENTAL,
            materialization_enum.SNAPSHOT,
        ]
        for materialization in valid_materializations:
            settings = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=t.SecretStr("testpass").get_secret_value(),
                oracle_service_name="XEPDB1",
                materialization=materialization,
            )
            assert settings.materialization == materialization

    def test_config_protocol_validation_all_valid_types(self) -> None:
        """Test all valid protocol types."""
        valid_protocols: t.SequenceOf[Literal["tcp", "tcps"]] = ["tcp", "tcps"]
        for protocol in valid_protocols:
            settings = FlextDbtOracleSettings(
                oracle_host="localhost",
                oracle_username="testuser",
                oracle_password=t.SecretStr("testpass").get_secret_value(),
                oracle_service_name="XEPDB1",
                protocol=protocol,
            )
            assert settings.protocol == protocol
