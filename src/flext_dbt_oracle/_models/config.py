"""DBT Oracle config namespace models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/_models/config
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import m


class FlextDbtOracleModelsConfig:
    """Config namespace models for model-less ``config/*.yaml`` exposure."""

    class DbtOracleNamespace(m.BaseModel):
        """Open, frozen namespace exposing every ``config/*.yaml`` domain."""

        model_config = m.ConfigDict(extra="allow", frozen=True)


__all__: list[str] = ["FlextDbtOracleModelsConfig"]
