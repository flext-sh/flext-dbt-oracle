"""Behavior contract for the flext-dbt-oracle console entry point.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_cli
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import pytest

from flext_dbt_oracle import main


class TestsFlextDbtOracleCli:
    """The console script dispatches through the inherited dbt ``cli_main``."""

    @staticmethod
    def test_unknown_subcommand_exits_with_failure() -> None:
        """An unsupported dbt subcommand propagates the base failure exit."""
        with pytest.raises(SystemExit) as exit_info:
            main(["not-a-dbt-command"])

        assert exit_info.value.code == 1
