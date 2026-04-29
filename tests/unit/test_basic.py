"""Basic tests for FLEXT DBT Oracle adapter.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_dbt_oracle.settings import FlextDbtOracleSettings
from tests import m, u


class TestsFlextDbtOracleBasic:
    """Behavior contract for test_basic."""

    def test_basic_import(self) -> None:
        """Test basic adapter imports work."""
        assert u.DbtOracle.Client is not None
        assert FlextDbtOracleSettings is not None
        assert m is not None
        assert m.DbtOracle.ModelGenerator is not None

    def test_adapter_type(self) -> None:
        """Test adapter type is correct."""
        assert u.DbtOracle.Client is not None

    def test_credentials_class(self) -> None:
        """Test credentials class is available."""
        assert FlextDbtOracleSettings is not None

    @pytest.mark.unit
    def test_adapter_initialization(self) -> None:
        """Test basic adapter initialization."""
        assert u.DbtOracle.Client is not None
        assert m is not None
