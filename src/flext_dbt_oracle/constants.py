"""Constants for FLEXT DBT Oracle module.

This module defines centralized constants following the FlextConstants pattern
from flext-core, extending it with DBT Oracle-specific constants.
"""

from __future__ import annotations

from flext_core import FlextConstants


class FlextDbtOracleConstants(FlextConstants):
    """Central container for DBT Oracle-specific constants.

    Follows the same pattern as FlextConstants from flext-core,
    organizing constants into logical categories with type safety.
    """

    class Performance:
        """Performance thresholds and limits."""

        # Object count thresholds
        LARGE_OBJECT_COUNT_THRESHOLD = 100
        VERY_LARGE_OBJECT_COUNT_THRESHOLD = 1000

        # Query performance
        SLOW_QUERY_THRESHOLD = 5.0  # seconds
        VERY_SLOW_QUERY_THRESHOLD = 30.0  # seconds

        # Batch sizes (use centralized constants)
        DEFAULT_BATCH_SIZE = FlextConstants.DBT.DEFAULT_BATCH_SIZE
        MAX_BATCH_SIZE = FlextConstants.DBT.MAX_BATCH_SIZE

        # Connection pool
        MIN_POOL_SIZE = 1
        MAX_POOL_SIZE = 20
        DEFAULT_POOL_SIZE = 5

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
        DEFAULT_PORT = FlextConstants.Infrastructure.DEFAULT_ORACLE_PORT

    class DBT:
        """DBT-specific constants."""

        # Model types
        MODEL_TYPE_TABLE = "table"
        MODEL_TYPE_VIEW = "view"
        MODEL_TYPE_INCREMENTAL = "incremental"
        MODEL_TYPE_EPHEMERAL = "ephemeral"

        # Materialization strategies
        MATERIALIZATION_TABLE = "table"
        MATERIALIZATION_VIEW = "view"
        MATERIALIZATION_INCREMENTAL = "incremental"

        # Test severity levels
        TEST_SEVERITY_WARN = "warn"
        TEST_SEVERITY_ERROR = "error"

        # Freshness check intervals (in hours)
        FRESHNESS_WARN_AFTER = 24
        FRESHNESS_ERROR_AFTER = 48

    class Validation:
        """Validation thresholds and limits."""

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

        # Batch processing (use centralized constants)
        OBJECTS_PER_THREAD = 25
        MIN_THREADS = 4
        MAX_THREADS = 8
        LARGE_BATCH_SIZE = FlextConstants.DBT.LARGE_BATCH_SIZE
        DEFAULT_BATCH_SIZE = FlextConstants.DBT.DEFAULT_BATCH_SIZE

    class Cache:
        """Cache configuration (use centralized constants)."""

        # TTL values in seconds
        METADATA_CACHE_TTL = FlextConstants.Cache.METADATA_CACHE_TTL
        QUERY_CACHE_TTL = FlextConstants.Cache.QUERY_CACHE_TTL

        # Cache sizes
        MAX_CACHE_ENTRIES = FlextConstants.Cache.MAX_CACHE_ENTRIES
        CACHE_CLEANUP_INTERVAL = FlextConstants.Cache.CACHE_CLEANUP_INTERVAL

    class Logging:
        """Logging configuration."""

        # Log levels as integers for comparison
        LOG_LEVEL_DEBUG = 10
        LOG_LEVEL_INFO = 20
        LOG_LEVEL_WARNING = 30
        LOG_LEVEL_ERROR = 40
        LOG_LEVEL_CRITICAL = 50
