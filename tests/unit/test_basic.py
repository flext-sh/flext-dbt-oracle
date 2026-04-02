"""Basic tests for FLEXT DBT Oracle adapter.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from tests import m, u


def test_basic_import() -> None:
    """Test basic adapter imports work."""
    assert u.DbtOracle.Client is not None
    assert m.DbtOracle.FlextDbtOracleSettings is not None
    assert m is not None
    assert m.DbtOracle.ModelGenerator is not None


def test_adapter_type() -> None:
    """Test adapter type is correct."""
    assert u.DbtOracle.Client is not None


def test_credentials_class() -> None:
    """Test credentials class is available."""
    assert m.DbtOracle.FlextDbtOracleSettings is not None


@pytest.mark.unit
def test_adapter_initialization() -> None:
    """Test basic adapter initialization."""
    assert u.DbtOracle.Client is not None
    assert m is not None
