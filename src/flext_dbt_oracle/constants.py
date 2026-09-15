"""Constants used by the DBT Oracle package."""

from __future__ import annotations

from flext_meltano import c

from flext_dbt_oracle._constants import FlextDbtOracleConstantsEnums


class FlextDbtOracleConstants(c, FlextDbtOracleConstantsEnums):
    """Domain constants for DBT Oracle workflows — composes _constants parts via MRO."""

    # All domain constants are declared in _constants/enums.py (FlextDbtOracleConstantsEnums)
    # This facade provides the MRO composition only.


c = FlextDbtOracleConstants

__all__: list[str] = ["FlextDbtOracleConstants", "c"]
