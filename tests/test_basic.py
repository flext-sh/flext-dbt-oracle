"""Basic tests for FLEXT DBT Oracle adapter."""

from dbt.adapters.oracle import (
from dbt.adapters.oracle.connections import (
from dbt.adapters.oracle.connections import OracleCredentials
from dbt.adapters.oracle import OracleAdapter


import pytest


def test_basic_import() -> None:
    """Test basic adapter imports work."""

        OracleAdapter,
        OracleConnectionManager,
    )

    assert OracleAdapter is not None
    assert OracleConnectionManager is not None


def test_adapter_type() -> None:
    """Test adapter type is correct."""

        OracleConnectionManager,
    )

    if OracleConnectionManager.TYPE != "oracle":

        raise AssertionError(f"Expected {"oracle"}, got {OracleConnectionManager.TYPE}")


def test_credentials_class() -> None:
    """Test credentials class is available."""


    assert OracleCredentials is not None


@pytest.mark.unit
def test_adapter_initialization() -> None:
    """Test basic adapter initialization."""


    # This is just a smoke test - adapter needs actual config to work
    assert OracleAdapter.ConnectionManager is not None
