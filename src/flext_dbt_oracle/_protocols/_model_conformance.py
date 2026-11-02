# AUTO-GENERATED FILE — Regenerate with: make gen
"""Static instance-to-protocol evidence required by candidate admission.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/_protocols/_model_conformance
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flext_dbt_oracle import m, p

    def _model_protocol_1(value: object) -> p.DbtOracle.DbtConnectionProfile:
        if not isinstance(value, m.DbtOracle.DbtConnectionProfile):
            msg = "model protocol witness received another declaring owner"
            raise TypeError(msg)
        return value

    def _model_protocol_2(value: object) -> p.DbtOracle.Model:
        if not isinstance(value, m.DbtOracle.Model):
            msg = "model protocol witness received another declaring owner"
            raise TypeError(msg)
        return value

    def _model_protocol_3(value: object) -> p.DbtOracle.OracleTableAdapter:
        if not isinstance(value, m.DbtOracle.OracleTableAdapter):
            msg = "model protocol witness received another declaring owner"
            raise TypeError(msg)
        return value
