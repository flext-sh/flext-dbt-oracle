"""DBT Oracle constant enumerations and values."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final


class FlextDbtOracleConstantsEnums:
    """DBT Oracle enumerations and values composed into the constants facade."""

    class Dbt:
        """DBT runtime defaults, metadata, and enums."""

        @unique
        class Materialization(StrEnum):
            """Valid DBT materialization values."""

            TABLE = "table"
            VIEW = "view"
            INCREMENTAL = "incremental"
            SNAPSHOT = "snapshot"

        DEFAULT_MATERIALIZATION: Final[Materialization] = Materialization.VIEW

        # dbt Jinja template, not executable SQL: `source()` is resolved by dbt at
        # compile time against the project's declared sources, so the value never
        # reaches a database driver as a literal.
        STAGING_SELECT_TEMPLATE: Final[str] = (
            "select * from {{{{ source('oracle', '{table}') }}}}"
        )

    DEFAULT_MODEL_TYPE: Final[str] = "staging"
    DEFAULT_SOURCE_NAME: Final[str] = "oracle"
    DEFAULT_SCHEMA_NAME: Final[str] = "public"


__all__: list[str] = ["FlextDbtOracleConstantsEnums"]
