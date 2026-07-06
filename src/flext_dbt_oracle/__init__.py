# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Oracle package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports
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
from flext_dbt_oracle._exports import FLEXT_DBT_ORACLE_LAZY_IMPORTS

if TYPE_CHECKING:
    from flext_db_oracle import d as d, e as e, h as h, r as r, x as x
    from flext_dbt_oracle.base import (
        FlextDbtOracleServiceBase as FlextDbtOracleServiceBase,
        s as s,
    )
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


_LAZY_IMPORTS = FLEXT_DBT_ORACLE_LAZY_IMPORTS


_EAGER_EXPORTS = (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)


_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextDbtOracleConstants",
    "FlextDbtOracleModels",
    "FlextDbtOracleProtocols",
    "FlextDbtOracleServiceBase",
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
)

__all__: tuple[str, ...] = (
    "FlextDbtOracleConstants",
    "FlextDbtOracleModels",
    "FlextDbtOracleProtocols",
    "FlextDbtOracleServiceBase",
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
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=_PUBLIC_EXPORTS,
)
