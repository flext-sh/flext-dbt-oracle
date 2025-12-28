"""Constants for FLEXT DBT Oracle.

Extending flext-core with DBT Oracle-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum
from typing import Final, Literal

from flext_core import FlextConstants


class FlextDbtOracleConstants(FlextConstants):
    """Central container for DBT Oracle-specific constants.

    Follows the same pattern as FlextConstants from flext-core,
    organizing constants into logical categories with type safety.
    """

    class DbtOraclePerformance:
        """DBT Oracle-specific performance thresholds and limits.

        Note: Does not override parent Performance class to avoid inheritance conflicts.
        """

        # Object count thresholds
        LARGE_OBJECT_COUNT_THRESHOLD = 100
        VERY_LARGE_OBJECT_COUNT_THRESHOLD = 1000

        # Query performance
        SLOW_QUERY_THRESHOLD = 5.0  # seconds
        VERY_SLOW_QUERY_THRESHOLD = 30.0  # seconds

        # Batch sizes - using FlextConstants composition
        DEFAULT_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
        MAX_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.MAX_ITEMS

        # Connection pool
        MIN_POOL_SIZE = 1
        MAX_POOL_SIZE = 20
        DEFAULT_POOL_SIZE = 5

        # Oracle configuration thresholds (from utilities.py)
        DEFAULT_PORT: Final[int] = 1521
        DEFAULT_SERVICE: Final[str] = "XEPDB1"
        MAX_CONNECTIONS: Final[int] = 100
        CONNECTION_TIMEOUT: Final[int] = 30
        CONNECTION_TIME_THRESHOLD_MS: Final[int] = 1000
        MIN_AVAILABLE_CONNECTIONS: Final[int] = 10
        EXECUTION_TIME_THRESHOLD_HIGH_MS: Final[int] = 10000
        EXECUTION_TIME_THRESHOLD_MEDIUM_MS: Final[int] = 5000
        EXECUTION_TIME_THRESHOLD_LOW_MS: Final[int] = 1000
        HIGH_IO_OPERATIONS_THRESHOLD: Final[int] = 100000
        CPU_UTILIZATION_THRESHOLD: Final[float] = 0.1
        HIGH_BUFFER_GETS_THRESHOLD: Final[int] = 1000000
        LARGE_TABLE_SIZE_GB: Final[int] = 100
        HIGH_GROWTH_RATE_GB: Final[int] = 10
        GROWTH_RATE_THRESHOLD_GB: Final[int] = 5
        VERY_LARGE_TABLE_SIZE_GB: Final[int] = 1000

    class Oracle:
        """Oracle-specific constants."""

        # Identifier limits
        MAX_IDENTIFIER_LENGTH = 30  # Oracle 11g and below
        MAX_IDENTIFIER_LENGTH_12C = 128  # Oracle 12c and above

        # Object limits
        MAX_COLUMNS_PER_TABLE = 1000
        MAX_INDEXES_PER_TABLE = 32767

        # Data type sizes
        MAX_VARCHAR2_SIZE = 4000
        MAX_NUMBER_PRECISION = 38

        # Default port
        DEFAULT_PORT = 1521  # Standard Oracle port

        class Performance:
            """Oracle connection and performance thresholds.

            Migrated from utilities.py ClassVar constants to centralized Final constants.
            """

            # Oracle connection constants
            DEFAULT_PORT: Final[int] = 1521
            DEFAULT_SERVICE: Final[str] = "XEPDB1"
            MAX_CONNECTIONS: Final[int] = 100
            CONNECTION_TIMEOUT: Final[int] = 30

            # Oracle performance threshold constants
            CONNECTION_TIME_THRESHOLD_MS: Final[int] = 1000
            MIN_AVAILABLE_CONNECTIONS: Final[int] = 10
            EXECUTION_TIME_THRESHOLD_HIGH_MS: Final[int] = 10000
            EXECUTION_TIME_THRESHOLD_MEDIUM_MS: Final[int] = 5000
            EXECUTION_TIME_THRESHOLD_LOW_MS: Final[int] = 1000
            HIGH_IO_OPERATIONS_THRESHOLD: Final[int] = 100000
            CPU_UTILIZATION_THRESHOLD: Final[float] = 0.1
            HIGH_BUFFER_GETS_THRESHOLD: Final[int] = 1000000
            LARGE_TABLE_SIZE_GB: Final[int] = 100
            HIGH_GROWTH_RATE_GB: Final[int] = 10
            GROWTH_RATE_THRESHOLD_GB: Final[int] = 5
            VERY_LARGE_TABLE_SIZE_GB: Final[int] = 1000

    class DBT:
        """DBT-specific constants."""

        class ModelTypes(StrEnum):
            """DBT model types using StrEnum for type safety.

            DRY Pattern:
                StrEnum is the single source of truth. Use ModelTypes.TABLE.value
                or ModelTypes.TABLE directly - no base strings needed.
            """

            TABLE = "table"
            VIEW = "view"
            INCREMENTAL = "incremental"
            EPHEMERAL = "ephemeral"

        class Materialization(StrEnum):
            """DBT materialization strategies using StrEnum for type safety.

            DRY Pattern:
                StrEnum is the single source of truth. Use Materialization.TABLE.value
                or Materialization.TABLE directly - no base strings needed.
            """

            TABLE = "table"
            VIEW = "view"
            INCREMENTAL = "incremental"

        class TestSeverity(StrEnum):
            """DBT test severity levels using StrEnum for type safety.

            DRY Pattern:
                StrEnum is the single source of truth. Use TestSeverity.WARN.value
                or TestSeverity.WARN directly - no base strings needed.
            """

            WARN = "warn"
            ERROR = "error"

        # Freshness check intervals (in hours)
        FRESHNESS_WARN_AFTER = 24
        FRESHNESS_ERROR_AFTER = 48

    class DbtOracleValidation:
        """DBT Oracle-specific validation thresholds and limits.

        Note: Does not override parent Validation class to avoid inheritance conflicts.
        """

        # Row count thresholds for data quality
        MIN_ROW_COUNT_WARNING = 0
        MIN_ROW_COUNT_ERROR = 0

        # Null percentage thresholds
        MAX_NULL_PERCENTAGE_WARNING = 10.0
        MAX_NULL_PERCENTAGE_ERROR = 50.0

        # Schema validation
        MAX_SCHEMA_NAME_LENGTH = 30
        MAX_TABLE_NAME_LENGTH = 30
        MAX_COLUMN_NAME_LENGTH = 30

    class SchemaRecommendations:
        """Schema analysis thresholds."""

        # Schema count thresholds for organization recommendations
        MANY_SCHEMAS_THRESHOLD = 10

    class ModelOptimization:
        """Model and performance optimization thresholds."""

        # Object count thresholds
        MODERATE_OBJECT_COUNT = 50
        LARGE_DATASET_THRESHOLD = 50

        # Batch processing - using FlextConstants composition
        OBJECTS_PER_THREAD = 25
        MIN_THREADS = 4
        MAX_THREADS = 8
        LARGE_BATCH_SIZE = 5000
        DEFAULT_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE

    class Cache:
        """Cache configuration (use centralized constants)."""

        # TTL values in seconds
        METADATA_CACHE_TTL = 3600  # 1 hour
        QUERY_CACHE_TTL = 1800  # 30 minutes

        # Cache sizes
        MAX_CACHE_ENTRIES = 10000
        CACHE_CLEANUP_INTERVAL = 300  # 5 minutes

    class DbtOracleLogging:
        """DBT Oracle-specific logging configuration.

        Note: Does not override parent Logging class to avoid inheritance conflicts.
        """

        # Log levels as integers for comparison
        LOG_LEVEL_DEBUG = 10
        LOG_LEVEL_INFO = 20
        LOG_LEVEL_WARNING = 30
        LOG_LEVEL_ERROR = 40
        LOG_LEVEL_CRITICAL = 50

    # Type-safe literals - PEP 695 syntax for type checking
    # All Literal types reference StrEnum members where available - NO string duplication!
    type DbtLogLevelLiteral = Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ]
    """DBT log level literal - no corresponding StrEnum (acceptable pattern)."""

    type ModelTypeLiteral = Literal[
        DBT.ModelTypes.TABLE,
        DBT.ModelTypes.VIEW,
        DBT.ModelTypes.INCREMENTAL,
        DBT.ModelTypes.EPHEMERAL,
    ]
    """DBT model type literal - references DBT.ModelTypes StrEnum members."""

    type MaterializationLiteral = Literal[
        DBT.Materialization.TABLE,
        DBT.Materialization.VIEW,
        DBT.Materialization.INCREMENTAL,
    ]
    """DBT materialization literal - references DBT.Materialization StrEnum members."""

    type TestSeverityLiteral = Literal[
        DBT.TestSeverity.WARN,
        DBT.TestSeverity.ERROR,
    ]
    """DBT test severity literal - references DBT.TestSeverity StrEnum members."""


c = FlextDbtOracleConstants

__all__ = ["FlextDbtOracleConstants", "c"]
