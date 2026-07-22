"""Runtime settings for flext-dbt-oracle tests."""

from __future__ import annotations

from flext_dbt_oracle import FlextDbtOracleSettings
from flext_tests import FlextTestsSettings


class TestsFlextDbtOracleSettings(FlextDbtOracleSettings, FlextTestsSettings):
    """DBT Oracle settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextDbtOracleSettings"]
