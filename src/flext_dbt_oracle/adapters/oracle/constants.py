"""DBT Oracle Adapter Constants - Maximum flext-core integration with zero duplication.

This module provides DBT Oracle adapter specific constants using flext-core patterns.
All Oracle DB constants are inherited from flext-core to ensure consistency
and eliminate code duplication across Oracle projects.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import ClassVar, Final

# Import from flext-core as SINGLE SOURCE OF TRUTH
from flext_core.constants import FlextSemanticConstants


class FlextDbtOracleSemanticConstants(FlextSemanticConstants):
    """DBT Oracle adapter semantic constants extending FlextSemanticConstants.

    Modern Python 3.13 constants following semantic grouping patterns.
    Extends the FLEXT ecosystem constants with DBT Oracle adapter-specific values
    while maintaining full backward compatibility.
    """

    class Adapter:
        """DBT adapter metadata constants."""

        TYPE: Final = "oracle"
        DBT_VERSION_MIN: Final = "1.6.0"
        DBT_VERSION_MAX: Final = "1.8.x"
        DBT_VERSION_RECOMMENDED: Final = "1.8.0"

    class OracleDB:
        """Oracle database constants - CONSUME from flext-core."""

        # Basic connection - CONSUME from single source
        DEFAULT_PORT: Final = 1521
        DEFAULT_SERVICE_NAME: Final = "XE"
        DEFAULT_SCHEMA: Final = "SYSTEM"
        DEFAULT_ENCODING: Final = "utf-8"
        DEFAULT_PROTOCOL: Final = "tcp"
        DEFAULT_TIMEOUT: Final = 30

    class Performance:
        """Performance and optimization constants."""

        # Threading
        DEFAULT_THREADS: Final = 4
        MAX_THREADS: Final = 16
        MIN_THREADS: Final = 1

        # Connection pooling - CONSUME from flext-core
        DEFAULT_POOL_MIN_SIZE: Final = 5
        DEFAULT_POOL_MAX_SIZE: Final = 20
        MAX_POOL_SIZE: Final = 50
        MIN_POOL_SIZE: Final = 1

        # Batch processing - CONSUME from flext-core
        DEFAULT_BATCH_SIZE: Final = 1000
        MAX_BATCH_SIZE: Final = 10000
        MIN_BATCH_SIZE: Final = 1

        # Fetch settings
        DEFAULT_FETCH_SIZE: Final = 1000
        DEFAULT_ARRAY_SIZE: Final = 100
        MAX_FETCH_SIZE: Final = 10000

    class Materializations:
        """DBT materialization constants."""

        TABLE: Final = "table"
        VIEW: Final = "view"
        INCREMENTAL: Final = "incremental"
        SNAPSHOT: Final = "snapshot"
        EPHEMERAL: Final = "ephemeral"
        DEFAULT: Final = "table"
        VALID: ClassVar[set[str]] = {TABLE, VIEW, INCREMENTAL, SNAPSHOT, EPHEMERAL}

    class IncrementalStrategies:
        """DBT incremental strategy constants."""

        APPEND: Final = "append"
        MERGE: Final = "merge"
        DELETE_INSERT: Final = "delete+insert"
        DEFAULT: Final = MERGE
        VALID: ClassVar[set[str]] = {APPEND, MERGE, DELETE_INSERT}

    class SnapshotStrategies:
        """DBT snapshot strategy constants."""

        TIMESTAMP: Final = "timestamp"
        CHECK: Final = "check"
        DEFAULT: Final = TIMESTAMP
        VALID: ClassVar[set[str]] = {TIMESTAMP, CHECK}

    class DataTypes:
        """Oracle data type mapping constants."""

        # String types
        DEFAULT_STRING_TYPE: Final = "VARCHAR2(4000)"
        LONG_STRING_TYPE: Final = "CLOB"
        MAX_VARCHAR2_LENGTH: Final = 4000

        # Numeric types
        DEFAULT_INTEGER_TYPE: Final = "NUMBER(38,0)"
        DEFAULT_DECIMAL_TYPE: Final = "NUMBER(38,10)"
        DEFAULT_FLOAT_TYPE: Final = "BINARY_DOUBLE"
        BOOLEAN_TYPE: Final = "NUMBER(1,0)"

        # Date/Time types
        DEFAULT_DATE_TYPE: Final = "DATE"
        DEFAULT_DATETIME_TYPE: Final = "TIMESTAMP(6)"
        DEFAULT_TIMESTAMP_TYPE: Final = "TIMESTAMP(6)"

        # Complex types
        JSON_TYPE: Final = "CLOB"
        ARRAY_TYPE: Final = "CLOB"

    class Schema:
        """Schema and quoting constants."""

        DEFAULT_SCHEMA: Final = "dbt_user"
        DEFAULT_DATABASE: Final = None  # Oracle doesn't use database concept

        # Quoting
        QUOTE_CHARACTER: Final = '"'
        QUOTE_POLICY_WHEN_NEEDED: Final = "when_needed"
        QUOTE_POLICY_ALWAYS: Final = "always"
        QUOTE_POLICY_NEVER: Final = "never"
        DEFAULT_QUOTE_POLICY: Final = QUOTE_POLICY_WHEN_NEEDED

    class SSL:
        """SSL configuration constants - CONSUME from flext-core."""

        DISABLE: Final = "disable"
        ALLOW: Final = "allow"
        PREFER: Final = "prefer"
        REQUIRE: Final = "require"
        DEFAULT: Final = PREFER
        VALID: ClassVar[set[str]] = {DISABLE, ALLOW, PREFER, REQUIRE}

    class ErrorHandling:
        """Error handling and retry constants."""

        DEFAULT_RETRY_ATTEMPTS: Final = 3
        DEFAULT_RETRY_DELAY: Final = 1

        # Oracle-specific retryable errors
        RETRYABLE_ERRORS: ClassVar[set[str]] = {
            "ORA-00028",  # session killed
            "ORA-00060",  # deadlock detected
            "ORA-01012",  # not logged on
            "ORA-03113",  # end-of-file on communication channel
            "ORA-03114",  # not connected to ORACLE
            "ORA-12170",  # TNS timeout
        }

    class Logging:
        """Logging configuration constants - CONSUME from flext-core."""

        DEFAULT_LOG_LEVEL: Final = "INFO"
        VALID_LOG_LEVELS: ClassVar[set[str]] = {
            "DEBUG",
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL",
        }
        DEFAULT_SQL_LOGGING: Final = False
        DEFAULT_INCLUDE_TIMING: Final = True
        DEFAULT_INCLUDE_ROW_COUNTS: Final = True

    class Catalog:
        """Catalog and metadata constants."""

        SUPPORTS_TABLE_COMMENTS: Final = True
        SUPPORTS_COLUMN_COMMENTS: Final = True
        SUPPORTS_DATA_LINEAGE: Final = True
        SUPPORTS_CATALOG_INTEGRATION: Final = True

        # Oracle data dictionary views
        DBA_TABLES_VIEW: Final = "DBA_TABLES"
        ALL_TABLES_VIEW: Final = "ALL_TABLES"
        USER_TABLES_VIEW: Final = "USER_TABLES"
        DBA_TAB_COLUMNS_VIEW: Final = "DBA_TAB_COLUMNS"
        ALL_TAB_COLUMNS_VIEW: Final = "ALL_TAB_COLUMNS"
        USER_TAB_COLUMNS_VIEW: Final = "USER_TAB_COLUMNS"


# Backward compatibility aliases
FlextDbtOracleConstants = FlextDbtOracleSemanticConstants

# Legacy class aliases for backward compatibility (DEPRECATED - use semantic access)
OracleDBConstants = FlextDbtOracleSemanticConstants.OracleDB
OracleDefaults = FlextDbtOracleSemanticConstants.Performance
OracleLimits = FlextDbtOracleSemanticConstants.Performance
DBTOracleConstants = FlextDbtOracleSemanticConstants.Performance
DBTOracleAdapterConstants = FlextDbtOracleSemanticConstants
