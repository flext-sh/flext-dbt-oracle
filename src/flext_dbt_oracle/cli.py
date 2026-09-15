"""CLI facade for DBT Oracle — thin wrapper over public facade."""

from __future__ import annotations

from flext_dbt_oracle import FlextDbtOracle


class FlextDbtOracleCliService:
    """CLI service for DBT Oracle — delegates to public facade."""

    def __init__(self, service: FlextDbtOracle) -> None:
        self.service = service

    def main(self, args: list[str]) -> int:
        """Entry point — currently no commands implemented."""
        _ = args
        return 0


def main(args: list[str]) -> int:
    """Module-level entry point."""
    return FlextDbtOracleCliService(FlextDbtOracle()).main(args)


__all__: list[str] = ["FlextDbtOracleCliService", "main"]
