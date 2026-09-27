"""FlextDbtOracle public facade — thin MRO re-export over service base."""

from __future__ import annotations

from flext_dbt_oracle import FlextDbtOracleServiceBase


class FlextDbtOracle(FlextDbtOracleServiceBase):
    """Public facade for DBT Oracle — inherits all service capabilities."""


__all__: list[str] = ["FlextDbtOracle"]
