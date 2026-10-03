"""Behavior contract for the flext-dbt-oracle console entry point."""

from __future__ import annotations

import pytest

from flext_dbt_oracle import main


class TestsFlextDbtOracleCli:
    """The console script dispatches through the inherited dbt ``cli_main``."""

    def test_unknown_subcommand_exits_with_failure(self) -> None:
        """An unsupported dbt subcommand propagates the base failure exit."""
        with pytest.raises(SystemExit) as exit_info:
            main(["not-a-dbt-command"])

        assert exit_info.value.code == 1
