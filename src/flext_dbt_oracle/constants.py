"""Constants used by the DBT Oracle package."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_db_oracle import FlextDbOracleConstants
from flext_meltano import FlextMeltanoConstants


class FlextDbtOracleConstants(FlextMeltanoConstants, FlextDbOracleConstants):
    """Domain constants for DBT Oracle workflows."""

    class DbtOracle:
        """DbtOracle domain namespace."""

        class Oracle:
            """Oracle connection defaults."""

            DEFAULT_HOST: Final[str] = FlextDbOracleConstants.LOCALHOST
            DEFAULT_PORT: Final[int] = 1521
            DEFAULT_SERVICE_NAME: Final[str] = "XEPDB1"
            DEFAULT_PROTOCOL: Final[str] = "tcp"
            DEFAULT_SCHEMA: Final[str] = "public"

        class Dbt:
            """DBT runtime defaults and enums."""

            DEFAULT_TARGET: Final[str] = "dev"
            DEFAULT_THREADS: Final[int] = 4
            DEFAULT_PROJECT_DIR: Final[str] = "."
            DEFAULT_PROFILES_DIR: Final[str] = "."
            DEFAULT_MATERIALIZATION: Final = "view"

            @unique
            class Materialization(StrEnum):
                """Valid DBT materialization values."""

                TABLE = "table"
                VIEW = "view"
                INCREMENTAL = "incremental"
                SNAPSHOT = "snapshot"

        DEFAULT_MODEL_TYPE: Final[str] = "staging"
        DEFAULT_SOURCE_NAME: Final[str] = "oracle"
        DEFAULT_SCHEMA_NAME: Final[str] = "public"
        PERFORMANCE_RECOMMENDATION_THRESHOLD: Final[int] = 20
        NLS_LANG: Final[str] = "AMERICAN_AMERICA.AL32UTF8"
        NLS_DATE_FORMAT: Final[str] = "YYYY-MM-DD"


c = FlextDbtOracleConstants

__all__: list[str] = ["FlextDbtOracleConstants", "c"]
