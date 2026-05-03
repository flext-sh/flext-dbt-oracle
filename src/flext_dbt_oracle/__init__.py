# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_dbt_oracle.__version__ import (
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_dbt_oracle.constants import FlextDbtOracleConstants, c
    from flext_dbt_oracle.models import FlextDbtOracleModels, m
    from flext_dbt_oracle.protocols import FlextDbtOracleProtocols, p
    from flext_dbt_oracle.settings import FlextDbtOracleSettings
    from flext_dbt_oracle.typings import FlextDbtOracleTypes, t
    from flext_dbt_oracle.utilities import FlextDbtOracleUtilities, u
    from flext_meltano import d, e, h, r, s, x
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".__version__": (
            "__author__",
            "__author_email__",
            "__description__",
            "__license__",
            "__title__",
            "__url__",
            "__version__",
            "__version_info__",
        ),
        ".constants": (
            "FlextDbtOracleConstants",
            "c",
        ),
        ".models": (
            "FlextDbtOracleModels",
            "m",
        ),
        ".protocols": (
            "FlextDbtOracleProtocols",
            "p",
        ),
        ".settings": ("FlextDbtOracleSettings",),
        ".typings": (
            "FlextDbtOracleTypes",
            "t",
        ),
        ".utilities": (
            "FlextDbtOracleUtilities",
            "u",
        ),
        "flext_meltano": (
            "d",
            "e",
            "h",
            "r",
            "s",
            "x",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "FlextDbtOracleConstants",
    "FlextDbtOracleModels",
    "FlextDbtOracleProtocols",
    "FlextDbtOracleSettings",
    "FlextDbtOracleTypes",
    "FlextDbtOracleUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
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
