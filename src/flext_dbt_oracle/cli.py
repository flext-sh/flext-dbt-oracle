"""CLI entrypoint for DBT Oracle — dispatches through the meltano dbt base.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/cli
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle import FlextDbtOracle, t


def main(args: t.StrSequence | None = None) -> int:
    """Console-script entry point delegating to the inherited dbt ``cli_main``.

    Returns:
        The resulting ``int``.
    """
    return FlextDbtOracle().cli_main(args)


__all__: list[str] = ["main"]
