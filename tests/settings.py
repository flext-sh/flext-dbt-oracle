"""Runtime settings for flext-dbt-oracle tests."""

from __future__ import annotations

from flext_tests.settings import FlextTestsSettings

from flext_dbt_oracle import FlextDbtOracleSettings


class TestsFlextDbtOracleSettings(FlextDbtOracleSettings, FlextTestsSettings):
    """DBT Oracle settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextDbtOracleSettings"]
