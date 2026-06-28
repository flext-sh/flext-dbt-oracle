# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import build_lazy_import_map, install_lazy_exports
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

if _t.TYPE_CHECKING:
    from flext_dbt_oracle.constants import (
        FlextDbtOracleConstants as FlextDbtOracleConstants,
        c as c,
    )
    from flext_dbt_oracle.models import (
        FlextDbtOracleModels as FlextDbtOracleModels,
        m as m,
    )
    from flext_dbt_oracle.protocols import (
        FlextDbtOracleProtocols as FlextDbtOracleProtocols,
        p as p,
    )
    from flext_dbt_oracle.settings import (
        FlextDbtOracleSettings as FlextDbtOracleSettings,
    )
    from flext_dbt_oracle.typings import (
        FlextDbtOracleTypes as FlextDbtOracleTypes,
        t as t,
    )
    from flext_dbt_oracle.utilities import (
        FlextDbtOracleUtilities as FlextDbtOracleUtilities,
        u as u,
    )
    from flext_meltano import d as d, e as e, h as h, r as r, s as s, x as x
_LAZY_IMPORTS = build_lazy_import_map(
    {
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


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)

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
