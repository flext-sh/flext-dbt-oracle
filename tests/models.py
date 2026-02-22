"""Test models for flext-dbt-oracle tests.

Provides TestsFlextDbtOracleModels, extending FlextTestsModels with flext-dbt-oracle-specific
models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests.models import FlextTestsModels

from flext_dbt_oracle.models import FlextDbtOracleModels


class TestsFlextDbtOracleModels(FlextTestsModels, FlextDbtOracleModels):
    """Models for flext-dbt-oracle tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. FlextTestsModels - for test infrastructure (.Tests.*)
    2. FlextDbtOracleModels - for domain models

    Access patterns:
    - tm.Tests.* (generic test models from FlextTestsModels)
    - tm.* (DBT Oracle domain models)
    - m.* (production models via alternative alias)
    """

    class Tests(FlextTestsModels.Tests):
        """Project-specific test fixtures namespace."""

        class DbtOracle:
            """DBT Oracle-specific test fixtures."""


# Short aliases per FLEXT convention
tm = TestsFlextDbtOracleModels
m = TestsFlextDbtOracleModels

__all__ = [
    "TestsFlextDbtOracleModels",
    "m",
    "tm",
]
