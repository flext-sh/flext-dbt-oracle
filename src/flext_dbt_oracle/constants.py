"""Constants used by the DBT Oracle package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/constants
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoConstants

from flext_dbt_oracle._constants.base import FlextDbtOracleConstantsBase
from flext_dbt_oracle._constants.enums import FlextDbtOracleConstantsEnums


class FlextDbtOracleConstants(FlextMeltanoConstants):
    """Domain constants for DBT Oracle workflows — composes _constants parts via MRO."""

    class DbtOracle(FlextDbtOracleConstantsBase, FlextDbtOracleConstantsEnums):
        """DBT Oracle constants namespace."""


c = FlextDbtOracleConstants

__all__: list[str] = ["FlextDbtOracleConstants", "c"]
