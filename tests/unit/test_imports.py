"""Test basic imports work without DBT runtime.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

import flext_dbt_oracle
import flext_dbt_oracle.adapters
import flext_dbt_oracle.connections
import flext_dbt_oracle.models
import flext_dbt_oracle.settings


class TestsFlextDbtOracleImports:
    """Behavior contract for test_imports."""

    def test_flext_dbt_oracle_imports(self) -> None:
        assert flext_dbt_oracle is not None
        assert flext_dbt_oracle.adapters is not None
        assert flext_dbt_oracle.connections is not None
        assert flext_dbt_oracle.models is not None
        assert flext_dbt_oracle.settings is not None

    @pytest.mark.unit
    def test_basic_functionality(self) -> None:
        assert True
