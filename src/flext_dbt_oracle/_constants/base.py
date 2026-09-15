"""Base constants for DBT Oracle — project metadata and DBT constants."""

from __future__ import annotations

from typing import Final


class FlextDbtOracleConstantsBase:
    """Base DBT Oracle constants: metadata and DBT constants."""

    class DbtOracle:
        """DBT Oracle constants namespace."""

        class Dbt:
            """DBT constants and enum values."""

            PROJECT_NAME: Final[str] = "dbt-oracle"


__all__: list[str] = ["FlextDbtOracleConstantsBase"]
