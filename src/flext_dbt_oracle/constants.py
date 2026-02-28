"""Constants used by the DBT Oracle package."""

from __future__ import annotations

from enum import StrEnum
from typing import Final

from flext_db_oracle.constants import FlextDbOracleConstants
from flext_meltano import FlextMeltanoConstants


class FlextDbtOracleConstants(FlextMeltanoConstants, FlextDbOracleConstants):
    """Domain constants for DBT Oracle workflows."""

    class Core:
        """Package metadata constants."""

        NAME: Final[str] = "flext-dbt-oracle"
        VERSION: Final[str] = "0.10.0-dev"

    class Oracle:
        """Oracle connection defaults."""

        DEFAULT_HOST: Final[str] = "localhost"
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
        DEFAULT_MATERIALIZATION: Final[str] = "view"

        class Materialization(StrEnum):
            """Valid DBT materialization values."""

            TABLE = "table"
            VIEW = "view"
            INCREMENTAL = "incremental"
            SNAPSHOT = "snapshot"

    class DbtOracle:
        """DBT Oracle domain-specific defaults."""

        DEFAULT_MODEL_TYPE: Final[str] = "staging"
        DEFAULT_SOURCE_NAME: Final[str] = "oracle"
        DEFAULT_SCHEMA_NAME: Final[str] = "public"
        PERFORMANCE_RECOMMENDATION_THRESHOLD: Final[int] = 20
        NLS_LANG: Final[str] = "AMERICAN_AMERICA.AL32UTF8"
        NLS_DATE_FORMAT: Final[str] = "YYYY-MM-DD"


c = FlextDbtOracleConstants

__all__ = ["FlextDbtOracleConstants", "c"]
