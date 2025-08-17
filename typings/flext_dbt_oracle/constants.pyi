from _typeshed import Incomplete
from flext_core.constants import FlextConstants

class FlextDbtOracleConstants(FlextConstants):
    class Performance:
        LARGE_OBJECT_COUNT_THRESHOLD: int
        VERY_LARGE_OBJECT_COUNT_THRESHOLD: int
        SLOW_QUERY_THRESHOLD: float
        VERY_SLOW_QUERY_THRESHOLD: float
        DEFAULT_BATCH_SIZE: int
        MAX_BATCH_SIZE: int
        MIN_POOL_SIZE: int
        MAX_POOL_SIZE: int
        DEFAULT_POOL_SIZE: int

    class Oracle:
        MAX_IDENTIFIER_LENGTH: int
        MAX_IDENTIFIER_LENGTH_12C: int
        MAX_COLUMNS_PER_TABLE: int
        MAX_INDEXES_PER_TABLE: int
        MAX_VARCHAR2_SIZE: int
        MAX_NUMBER_PRECISION: int
        DEFAULT_PORT: Incomplete

    class DBT:
        MODEL_TYPE_TABLE: str
        MODEL_TYPE_VIEW: str
        MODEL_TYPE_INCREMENTAL: str
        MODEL_TYPE_EPHEMERAL: str
        MATERIALIZATION_TABLE: str
        MATERIALIZATION_VIEW: str
        MATERIALIZATION_INCREMENTAL: str
        TEST_SEVERITY_WARN: str
        TEST_SEVERITY_ERROR: str
        FRESHNESS_WARN_AFTER: int
        FRESHNESS_ERROR_AFTER: int

    class Validation:
        MIN_ROW_COUNT_WARNING: int
        MIN_ROW_COUNT_ERROR: int
        MAX_NULL_PERCENTAGE_WARNING: float
        MAX_NULL_PERCENTAGE_ERROR: float
        MAX_SCHEMA_NAME_LENGTH: int
        MAX_TABLE_NAME_LENGTH: int
        MAX_COLUMN_NAME_LENGTH: int

    class SchemaRecommendations:
        MANY_SCHEMAS_THRESHOLD: int

    class ModelOptimization:
        MODERATE_OBJECT_COUNT: int
        LARGE_DATASET_THRESHOLD: int
        OBJECTS_PER_THREAD: int
        MIN_THREADS: int
        MAX_THREADS: int
        LARGE_BATCH_SIZE: int
        DEFAULT_BATCH_SIZE: int

    class Cache:
        METADATA_CACHE_TTL: int
        QUERY_CACHE_TTL: int
        MAX_CACHE_ENTRIES: int
        CACHE_CLEANUP_INTERVAL: int

    class Logging:
        LOG_LEVEL_DEBUG: int
        LOG_LEVEL_INFO: int
        LOG_LEVEL_WARNING: int
        LOG_LEVEL_ERROR: int
        LOG_LEVEL_CRITICAL: int
