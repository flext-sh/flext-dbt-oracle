"""CLI entrypoint for DBT Oracle — dispatches through the meltano dbt base.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/cli
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle import FlextDbtOracle, t


def main(args: t.StrSequence | None = None) -> int:
    """Run the flext-dbt-oracle console-script entry point.

    Delegates to the inherited dbt ``cli_main`` dispatcher.

    Args:
        args: Command-line arguments; defaults to ``sys.argv[1:]`` when
            omitted.

    Returns:
        Process exit code from the dispatched dbt command.

    """
    return FlextDbtOracle().cli_main(args)


__all__: list[str] = ["main"]
