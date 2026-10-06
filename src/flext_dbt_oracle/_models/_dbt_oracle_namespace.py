"""Dbt oracle namespace module.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/_models/_dbt_oracle_namespace
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_oracle import m


class _DbtOracleNamespace(m.BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = m.ConfigDict(extra="allow", frozen=True)
