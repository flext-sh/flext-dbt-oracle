# AUTO-GENERATED FILE — Regenerate with: make gen
"""Config Parts package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_oracle.tests.unit._config_parts.connection import (
        FlextDbtOracleConfigConnectionPart as FlextDbtOracleConfigConnectionPart,
    )
    from flext_dbt_oracle.tests.unit._config_parts.construction import (
        FlextDbtOracleConfigConstructionPart as FlextDbtOracleConfigConstructionPart,
    )
    from flext_dbt_oracle.tests.unit._config_parts.validation import (
        FlextDbtOracleConfigValidationPart as FlextDbtOracleConfigValidationPart,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".connection": ("FlextDbtOracleConfigConnectionPart",),
        ".construction": ("FlextDbtOracleConfigConstructionPart",),
        ".validation": ("FlextDbtOracleConfigValidationPart",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
