# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_basic": ("test_basic",),
        ".test_config": ("test_config",),
        ".test_connections": ("test_connections",),
        ".test_impl": ("test_impl",),
        ".test_imports": ("test_imports",),
        ".test_module_governance": ("test_module_governance",),
        "flext_dbt_oracle": (
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
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
