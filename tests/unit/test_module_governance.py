"""Behavioral governance contract for the flext_dbt_oracle package namespace.

The observable contract under test is the *public module namespace* that the
package exposes on import: per FLEXT AGENTS.md §3.1 every package module must
expose only class-shaped facades — never a module-level logger and never a
loose top-level function. These assertions exercise that contract through the
public ``import`` + attribute surface only (the same surface any consumer sees),
not through any private attribute of a unit under test.
"""

from __future__ import annotations

from flext_tests.utilities import ModuleGovernanceMixin

from tests import c


class TestsFlextDbtOracleModuleGovernance(ModuleGovernanceMixin):
    """Behavior contract for the flext_dbt_oracle public module namespace."""

    _test_file = __file__
    _tests_config = c.DbtOracle.Tests

    def test_package_exposes_at_least_one_module(self) -> None:
        # Guards the discovery contract: an empty scan would make every other
        # invariant vacuously true and hide real regressions.
        modules = self._iter_package_modules()

        assert modules, "expected flext_dbt_oracle package to expose modules"


__all__: list[str] = ["TestsFlextDbtOracleModuleGovernance"]
