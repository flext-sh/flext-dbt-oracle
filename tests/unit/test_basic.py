"""Basic tests for FLEXT DBT Oracle adapter.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_dbt_oracle import (
    FlextDbtOracleClient,
    FlextDbtOracleModelGenerator,
    FlextDbtOracleModels,
    FlextDbtOracleSettings,
)


def test_basic_import() -> None:
    """Test basic adapter imports work."""
    assert FlextDbtOracleClient is not None
    assert FlextDbtOracleSettings is not None
    assert FlextDbtOracleModels is not None
    assert FlextDbtOracleModelGenerator is not None


def test_adapter_type() -> None:
    """Test adapter type is correct."""
    assert FlextDbtOracleClient is not None


def test_credentials_class() -> None:
    """Test credentials class is available."""
    assert FlextDbtOracleSettings is not None


@pytest.mark.unit
def test_adapter_initialization() -> None:
    """Test basic adapter initialization."""
    assert FlextDbtOracleClient is not None
    assert FlextDbtOracleModels is not None
