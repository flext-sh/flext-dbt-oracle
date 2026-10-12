"""FlextDbtOracleConfig — frozen config singleton for flext-dbt-oracle (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``DbtOracle:`` key and
are exposed through the open ``config.DbtOracle`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.DbtOracle.<domain>[<key>...]``.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import FlextMeltanoConfig, m

from flext_dbt_oracle._models.config import FlextDbtOracleModelsConfig


class FlextDbtOracleConfig(FlextMeltanoConfig):
    """DbtOracle config auto-loaded model-less from ``config/*.yaml``."""

    DbtOracle: Annotated[
        FlextDbtOracleModelsConfig.DbtOracleNamespace,
        m.Field(
            description=(
                "Open namespace exposing ``config/*.yaml`` under ``DbtOracle``."
            ),
        ),
    ] = FlextDbtOracleModelsConfig.DbtOracleNamespace()


config: FlextDbtOracleConfig = FlextDbtOracleConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_dbt_oracle import``
``config``."""

__all__: list[str] = ["FlextDbtOracleConfig", "config"]
