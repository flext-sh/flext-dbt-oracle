"""DBT Oracle domain constants — single source of truth for all constant values.

These constants were previously scattered in constants.py (ENFORCE-079).
Each constant family is namespaced under a dedicated inner class.
"""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_db_oracle import FlextDbOracleConstants
from flext_meltano import c


class FlextDbtOracleConstantsBase(c, FlextDbOracleConstants):
    """Base DBT Oracle constants inheriting from parent facades."""

    class DbtOracle:
        """DbtOracle domain namespace."""

        class Oracle:
            """Oracle connection defaults."""

            DEFAULT_HOST: Final[str] = FlextDbOracleConstants.LOCALHOST
            DEFAULT_PORT: Final[int] = 1521
            DEFAULT_SERVICE_NAME: Final[str] = "XEPDB1"
            DEFAULT_PROTOCOL: Final[str] = "tcp"

        class Dbt:
            """DBT runtime defaults and enums."""

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

        DEFAULT_MODEL_TYPE: Final[str] = "staging"
        DEFAULT_SOURCE_NAME: Final[str] = "oracle"
        DEFAULT_SCHEMA_NAME: Final[str] = "public"
        PERFORMANCE_RECOMMENDATION_THRESHOLD: Final[int] = 20
        NLS_LANG: Final[str] = "AMERICAN_AMERICA.AL32UTF8"
        NLS_DATE_FORMAT: Final[str] = "YYYY-MM-DD"


class FlextDbtOracleConstants(FlextDbtOracleConstantsBase):
    """Facade re-exporting all constant families."""

    class DbtOracle(FlextDbtOracleConstantsBase.DbtOracle):
        pass


c = FlextDbtOracleConstants

__all__: list[str] = ["FlextDbtOracleConstantsBase", "FlextDbtOracleConstants", "c"]
