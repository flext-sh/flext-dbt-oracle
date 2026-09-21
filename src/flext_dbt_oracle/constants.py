"""Constants used by the DBT Oracle package."""

from __future__ import annotations

from flext_meltano import c

from ._constants.base import FlextDbtOracleConstantsBase
from ._constants.enums import FlextDbtOracleConstantsEnums


class FlextDbtOracleConstants(c):
    """Domain constants for DBT Oracle workflows — composes _constants parts via MRO."""

    class DbtOracle(FlextDbtOracleConstantsBase, FlextDbtOracleConstantsEnums):
        """DBT Oracle constants namespace."""


c = FlextDbtOracleConstants

__all__: list[str] = ["FlextDbtOracleConstants", "c"]
