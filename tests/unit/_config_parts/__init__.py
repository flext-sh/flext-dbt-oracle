"""Configuration test parts for flext-dbt-oracle."""

from __future__ import annotations

from tests.unit._config_parts.connection import (
    FlextDbtOracleConfigConnectionPart,
)
from tests.unit._config_parts.construction import (
    FlextDbtOracleConfigConstructionPart,
)
from tests.unit._config_parts.validation import (
    FlextDbtOracleConfigValidationPart,
)

__all__: list[str] = [
    "FlextDbtOracleConfigConnectionPart",
    "FlextDbtOracleConfigConstructionPart",
    "FlextDbtOracleConfigValidationPart",
]
