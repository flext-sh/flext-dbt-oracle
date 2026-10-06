# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle. Protocols package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle._protocols.base import FlextDbtOracleProtocolsBase


__all__: tuple[str, ...] = ("FlextDbtOracleProtocolsBase",)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({"FlextDbtOracleProtocolsBase": ".base"}),
    public_exports=__all__,
)
