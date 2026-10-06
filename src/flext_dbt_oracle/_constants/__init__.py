# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle. Constants package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle._constants.base import FlextDbtOracleConstantsBase
    from flext_dbt_oracle._constants.enums import FlextDbtOracleConstantsEnums


__all__: tuple[str, ...] = (
    "FlextDbtOracleConstantsBase",
    "FlextDbtOracleConstantsEnums",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtOracleConstantsBase": ".base",
        "FlextDbtOracleConstantsEnums": ".enums",
    }),
    public_exports=__all__,
)
