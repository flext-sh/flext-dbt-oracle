# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests.unit package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from tests.unit import _config_parts


__all__: tuple[str, ...] = ("_config_parts",)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({"_config_parts": "._config_parts"}),
    public_exports=__all__,
)
