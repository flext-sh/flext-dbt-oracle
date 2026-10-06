from __future__ import annotations

from flext_dbt_oracle import m


class _DbtOracleNamespace(m.BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = m.ConfigDict(extra="allow", frozen=True)
