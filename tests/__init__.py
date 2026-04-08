# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        TestsFlextDbtOracleConstants,
        TestsFlextDbtOracleConstants as c,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import TestsFlextDbtOracleModels, TestsFlextDbtOracleModels as m

    protocols = _tests_protocols
    import tests.test_module_governance as _tests_test_module_governance
    from tests.protocols import (
        TestsFlextDbtOracleProtocols,
        TestsFlextDbtOracleProtocols as p,
    )

    test_module_governance = _tests_test_module_governance
    import tests.typings as _tests_typings

    typings = _tests_typings
    import tests.unit as _tests_unit
    from tests.typings import TestsFlextDbtOracleTypes, TestsFlextDbtOracleTypes as t

    unit = _tests_unit
    import tests.utilities as _tests_utilities

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.utilities import (
        TestsFlextDbtOracleUtilities,
        TestsFlextDbtOracleUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("tests.unit",),
    {
        "TestsFlextDbtOracleConstants": (
            "tests.constants",
            "TestsFlextDbtOracleConstants",
        ),
        "TestsFlextDbtOracleModels": ("tests.models", "TestsFlextDbtOracleModels"),
        "TestsFlextDbtOracleProtocols": (
            "tests.protocols",
            "TestsFlextDbtOracleProtocols",
        ),
        "TestsFlextDbtOracleTypes": ("tests.typings", "TestsFlextDbtOracleTypes"),
        "TestsFlextDbtOracleUtilities": (
            "tests.utilities",
            "TestsFlextDbtOracleUtilities",
        ),
        "c": ("tests.constants", "TestsFlextDbtOracleConstants"),
        "conftest": "tests.conftest",
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("tests.models", "TestsFlextDbtOracleModels"),
        "models": "tests.models",
        "p": ("tests.protocols", "TestsFlextDbtOracleProtocols"),
        "protocols": "tests.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "t": ("tests.typings", "TestsFlextDbtOracleTypes"),
        "test_module_governance": "tests.test_module_governance",
        "typings": "tests.typings",
        "u": ("tests.utilities", "TestsFlextDbtOracleUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("logger", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

__all__ = [
    "TestsFlextDbtOracleConstants",
    "TestsFlextDbtOracleModels",
    "TestsFlextDbtOracleProtocols",
    "TestsFlextDbtOracleTypes",
    "TestsFlextDbtOracleUtilities",
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "t",
    "test_module_governance",
    "typings",
    "u",
    "unit",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
