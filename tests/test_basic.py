"""Basic tests for FLEXT DBT Oracle adapter."""

import pytest


def test_basic_import() -> None:
    """Test basic adapter imports work."""
    from dbt.adapters.oracle import (
        OracleAdapter,
        OracleConnectionManager,
    )

    assert OracleAdapter is not None
    assert OracleConnectionManager is not None


def test_adapter_type() -> None:
    """Test adapter type is correct."""
    from dbt.adapters.oracle.connections import OracleConnectionManager

    assert OracleConnectionManager.TYPE == "oracle"


def test_credentials_class() -> None:
    """Test credentials class is available."""
    from dbt.adapters.oracle.connections import OracleCredentials

    assert OracleCredentials is not None


@pytest.mark.unit
def test_adapter_initialization() -> None:
    """Test basic adapter initialization."""
    from dbt.adapters.oracle import OracleAdapter

    # This is just a smoke test - adapter needs actual config to work
    assert OracleAdapter.ConnectionManager is not None
