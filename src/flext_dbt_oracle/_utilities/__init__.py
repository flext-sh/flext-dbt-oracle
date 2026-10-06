# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle. Utilities package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle._utilities.base import FlextDbtOracleUtilitiesBase
    from flext_dbt_oracle._utilities.model_builder import (
        FlextDbtOracleUtilitiesModelBuilder,
    )


__all__: tuple[str, ...] = (
    "FlextDbtOracleUtilitiesBase",
    "FlextDbtOracleUtilitiesModelBuilder",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtOracleUtilitiesBase": ".base",
        "FlextDbtOracleUtilitiesModelBuilder": ".model_builder",
    }),
    public_exports=__all__,
)
