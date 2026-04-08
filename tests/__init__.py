# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.constants import (
        TestsFlextDbtOracleConstants,
        TestsFlextDbtOracleConstants as c,
    )
    from tests.models import TestsFlextDbtOracleModels, TestsFlextDbtOracleModels as m
    from tests.protocols import (
        TestsFlextDbtOracleProtocols,
        TestsFlextDbtOracleProtocols as p,
    )
    from tests.typings import TestsFlextDbtOracleTypes, TestsFlextDbtOracleTypes as t
    from tests.utilities import (
        TestsFlextDbtOracleUtilities,
        TestsFlextDbtOracleUtilities as u,
    )
_LAZY_IMPORTS = {
    "TestsFlextDbtOracleConstants": ("tests.constants", "TestsFlextDbtOracleConstants"),
    "TestsFlextDbtOracleModels": ("tests.models", "TestsFlextDbtOracleModels"),
    "TestsFlextDbtOracleProtocols": ("tests.protocols", "TestsFlextDbtOracleProtocols"),
    "TestsFlextDbtOracleTypes": ("tests.typings", "TestsFlextDbtOracleTypes"),
    "TestsFlextDbtOracleUtilities": ("tests.utilities", "TestsFlextDbtOracleUtilities"),
    "c": ("tests.constants", "TestsFlextDbtOracleConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("tests.models", "TestsFlextDbtOracleModels"),
    "p": ("tests.protocols", "TestsFlextDbtOracleProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("tests.typings", "TestsFlextDbtOracleTypes"),
    "u": ("tests.utilities", "TestsFlextDbtOracleUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "TestsFlextDbtOracleConstants",
    "TestsFlextDbtOracleModels",
    "TestsFlextDbtOracleProtocols",
    "TestsFlextDbtOracleTypes",
    "TestsFlextDbtOracleUtilities",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
