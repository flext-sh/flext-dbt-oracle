"""Basic tests for FLEXT DBT Oracle adapter.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_dbt_oracle.adapters import FlextOracleAdapter as OracleAdapter
from flext_dbt_oracle.adapters.oracle.connections import (
    FlextOracleOracleConnectionManager as OracleConnectionManager,
    OracleCredentials,
)


def test_basic_import() -> None:
    """Test basic adapter imports work."""
    assert OracleAdapter is not None
    assert OracleConnectionManager is not None


def test_adapter_type() -> None:
    """Test adapter type is correct."""
    if OracleConnectionManager.TYPE != "oracle":
        msg: str = f"Expected 'oracle', got {OracleConnectionManager.TYPE}"
        raise AssertionError(msg)


def test_credentials_class() -> None:
    """Test credentials class is available."""
    assert OracleCredentials is not None


@pytest.mark.unit
def test_adapter_initialization() -> None:
    """Test basic adapter initialization."""
    # This is just a smoke test - adapter needs actual config to work
    assert OracleAdapter.ConnectionManager is not None
