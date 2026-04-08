# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "test_basic": "tests.unit.test_basic",
    "test_config": "tests.unit.test_config",
    "test_connections": "tests.unit.test_connections",
    "test_impl": "tests.unit.test_impl",
    "test_imports": "tests.unit.test_imports",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
