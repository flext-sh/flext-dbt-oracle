# AUTO-GENERATED FILE — Regenerate with: make gen
"""Static instance-to-protocol evidence required by candidate admission.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/_protocols/_model_conformance
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flext_dbt_oracle import FlextDbtOracleModels, FlextDbtOracleProtocols

    def model_protocol_1(
        value: (FlextDbtOracleModels.DbtOracle.DbtConnectionProfile),
    ) -> FlextDbtOracleProtocols.DbtOracle.DbtConnectionProfile:
        return value

    def model_protocol_2(
        value: (FlextDbtOracleModels.DbtOracle.Model),
    ) -> FlextDbtOracleProtocols.DbtOracle.Model:
        return value

    def model_protocol_3(
        value: (FlextDbtOracleModels.DbtOracle.OracleTableAdapter),
    ) -> FlextDbtOracleProtocols.DbtOracle.OracleTableAdapter:
        return value
