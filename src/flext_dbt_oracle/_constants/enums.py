"""DBT Oracle constant enumerations and values."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_db_oracle import FlextDbOracleConstants


class FlextDbtOracleConstantsEnums:
    """DBT Oracle enumerations and values composed into the constants facade."""

    class Oracle:
        """Oracle connection defaults."""

        DEFAULT_HOST: Final[str] = FlextDbOracleConstants.LOCALHOST
        DEFAULT_PORT: Final[int] = 1521
        DEFAULT_SERVICE_NAME: Final[str] = "XEPDB1"
        DEFAULT_PROTOCOL: Final[str] = "tcp"

    class Dbt:
        """DBT runtime defaults, metadata, and enums."""

        PROJECT_NAME: Final[str] = "dbt-oracle"

        @unique
        class Materialization(StrEnum):
            """Valid DBT materialization values."""

            TABLE = "table"
            VIEW = "view"
            INCREMENTAL = "incremental"
            SNAPSHOT = "snapshot"

        DEFAULT_TARGET: Final[str] = "dev"
        DEFAULT_PROFILES_DIR: Final[str] = "."
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
    PERFORMANCE_RECOMMENDATION_THRESHOLD: Final[int] = 20
    NLS_LANG: Final[str] = "AMERICAN_AMERICA.AL32UTF8"
    NLS_DATE_FORMAT: Final[str] = "YYYY-MM-DD"


__all__: list[str] = ["FlextDbtOracleConstantsEnums"]
