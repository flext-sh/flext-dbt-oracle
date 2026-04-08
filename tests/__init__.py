# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants
    from tests.conftest import (
        MockConnectionManager,
        MockDbtOracleAdapter,
        MockDbtRunner,
        MockModelCompiler,
        MockRelationManager,
        MockSqlExecutor,
        pytest_configure,
        pytest_plugins,
        shared_oracle_container,
    )

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        FlextDbtOracleTestConstants,
        FlextDbtOracleTestConstants as c,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import FlextDbtOracleTestModels, FlextDbtOracleTestModels as m

    protocols = _tests_protocols
    import tests.test_module_governance as _tests_test_module_governance
    from tests.protocols import (
        FlextDbtOracleTestProtocols,
        FlextDbtOracleTestProtocols as p,
    )

    test_module_governance = _tests_test_module_governance
    import tests.typings as _tests_typings
    from tests.test_module_governance import PACKAGE_ROOT

    typings = _tests_typings
    import tests.utilities as _tests_utilities
    from tests.typings import FlextDbtOracleTestTypes, FlextDbtOracleTestTypes as t
    from tests.unit.test_config import FlextDbtOracleSettings

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.utilities import (
        FlextDbtOracleTestUtilities,
        FlextDbtOracleTestUtilities as u,
    )
_LAZY_IMPORTS = {
    "FlextDbtOracleSettings": ("tests.unit.test_config", "FlextDbtOracleSettings"),
    "FlextDbtOracleTestConstants": ("tests.constants", "FlextDbtOracleTestConstants"),
    "FlextDbtOracleTestModels": ("tests.models", "FlextDbtOracleTestModels"),
    "FlextDbtOracleTestProtocols": ("tests.protocols", "FlextDbtOracleTestProtocols"),
    "FlextDbtOracleTestTypes": ("tests.typings", "FlextDbtOracleTestTypes"),
    "FlextDbtOracleTestUtilities": ("tests.utilities", "FlextDbtOracleTestUtilities"),
    "MockConnectionManager": ("tests.conftest", "MockConnectionManager"),
    "MockDbtOracleAdapter": ("tests.conftest", "MockDbtOracleAdapter"),
    "MockDbtRunner": ("tests.conftest", "MockDbtRunner"),
    "MockModelCompiler": ("tests.conftest", "MockModelCompiler"),
    "MockRelationManager": ("tests.conftest", "MockRelationManager"),
    "MockSqlExecutor": ("tests.conftest", "MockSqlExecutor"),
    "PACKAGE_ROOT": ("tests.test_module_governance", "PACKAGE_ROOT"),
    "c": ("tests.constants", "FlextDbtOracleTestConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("tests.models", "FlextDbtOracleTestModels"),
    "models": "tests.models",
    "p": ("tests.protocols", "FlextDbtOracleTestProtocols"),
    "protocols": "tests.protocols",
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "pytest_plugins": ("tests.conftest", "pytest_plugins"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "shared_oracle_container": ("tests.conftest", "shared_oracle_container"),
    "t": ("tests.typings", "FlextDbtOracleTestTypes"),
    "test_module_governance": "tests.test_module_governance",
    "typings": "tests.typings",
    "u": ("tests.utilities", "FlextDbtOracleTestUtilities"),
    "utilities": "tests.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "PACKAGE_ROOT",
    "FlextDbtOracleSettings",
    "FlextDbtOracleTestConstants",
    "FlextDbtOracleTestModels",
    "FlextDbtOracleTestProtocols",
    "FlextDbtOracleTestTypes",
    "FlextDbtOracleTestUtilities",
    "MockConnectionManager",
    "MockDbtOracleAdapter",
    "MockDbtRunner",
    "MockModelCompiler",
    "MockRelationManager",
    "MockSqlExecutor",
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
    "pytest_configure",
    "pytest_plugins",
    "r",
    "s",
    "shared_oracle_container",
    "t",
    "test_module_governance",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
