"""Service base for flext-dbt-oracle tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_dbt_oracle import m, p
from tests.settings import TestsFlextDbtOracleSettings


class TestsFlextDbtOracleServiceBase(tests_s):
    """DBT Oracle test service base with source and test settings namespaces."""

    # NOTE (multi-agent): flext-tests owns fetch_settings; this project
    # declares only its more-specific bootstrap settings type (canonical
    # pattern per flext-cli tests/base.py). The `settings = ()` stub was a
    # fake that silenced the contract violation — removed at the root.
    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> p.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextDbtOracleSettings)


s = TestsFlextDbtOracleServiceBase

__all__: list[str] = ["TestsFlextDbtOracleServiceBase", "s"]
