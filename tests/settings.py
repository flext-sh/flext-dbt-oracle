"""Runtime settings for flext-dbt-oracle tests.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/settings
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsSettings

from flext_dbt_oracle import FlextDbtOracleSettings


class TestsFlextDbtOracleSettings(FlextDbtOracleSettings, FlextTestsSettings):
    """DBT Oracle settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextDbtOracleSettings"]
