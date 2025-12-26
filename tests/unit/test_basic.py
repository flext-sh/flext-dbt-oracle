"""Basic tests for FLEXT DBT Oracle adapter.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest



    FlextDbtOracleClient,
    FlextDbtOracleModel,
    FlextDbtOracleModelGenerator,
    FlextDbtOracleSettings,
)


def test_basic_import() -> None:
    """Test basic adapter imports work."""
    assert FlextDbtOracleClient is not None
    assert FlextDbtOracleSettings is not None
    assert FlextDbtOracleModel is not None
    assert FlextDbtOracleModelGenerator is not None


def test_adapter_type() -> None:
    """Test adapter type is correct."""
    # This test will need to be updated based on actual implementation
    # For now, just test that the class exists
    assert FlextDbtOracleClient is not None


def test_credentials_class() -> None:
    """Test credentials class is available."""
    # This test will need to be updated based on actual implementation
    # For now, just test that the config class exists
    assert FlextDbtOracleSettings is not None


@pytest.mark.unit
def test_adapter_initialization() -> None:
    """Test basic adapter initialization."""
    # This test will need to be updated based on actual implementation
    # For now, just test that the classes exist
    assert FlextDbtOracleClient is not None
    assert FlextDbtOracleModel is not None
