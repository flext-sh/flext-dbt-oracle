"""Service base for flext-dbt-oracle tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_dbt_oracle import m
from tests.settings import TestsFlextDbtOracleSettings


class TestsFlextDbtOracleServiceBase(tests_s):
    """DBT Oracle test service base with source and test settings namespaces."""

    @classmethod
    @override
    def fetch_settings(cls) -> TestsFlextDbtOracleSettings:
        """Return the typed DBT Oracle+Tests settings singleton."""
        settings: TestsFlextDbtOracleSettings = TestsFlextDbtOracleSettings.fetch_global()
        return settings

    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextDbtOracleSettings)


s = TestsFlextDbtOracleServiceBase

__all__: list[str] = ["TestsFlextDbtOracleServiceBase", "s"]
