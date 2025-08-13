"""DBT Oracle exceptions using flext-core patterns.

Provides specialized exception classes for DBT Oracle operations
using flext-core exception factory patterns for consistent error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core.exceptions import create_module_exception_classes

# Create module-specific exception classes using flext-core factory
_exc = create_module_exception_classes("flext_dbt_oracle")

# Configuration and Setup Exceptions
FlextDbtOracleConfigError = _exc["FlextDbtOracleConfigurationError"]
FlextDbtOracleConnectionError = _exc["FlextDbtOracleConnectionError"]
FlextDbtOracleAuthenticationError = _exc["FlextDbtOracleAuthenticationError"]

# Data Processing Exceptions
FlextDbtOracleProcessingError = _exc["FlextDbtOracleProcessingError"]
FlextDbtOracleValidationError = _exc["FlextDbtOracleValidationError"]
FlextDbtOracleTransformationError = _exc["FlextDbtOracleProcessingError"]

# Database Operation Exceptions
FlextDbtOracleDatabaseError = _exc["FlextDbtOracleProcessingError"]
FlextDbtOracleQueryError = _exc["FlextDbtOracleProcessingError"]
FlextDbtOracleSchemaError = _exc["FlextDbtOracleValidationError"]

# DBT-specific Exceptions
FlextDbtOracleModelError = _exc["FlextDbtOracleProcessingError"]
FlextDbtOracleCompilationError = _exc["FlextDbtOracleProcessingError"]
FlextDbtOracleExecutionError = _exc["FlextDbtOracleProcessingError"]

# Oracle-specific Exceptions
FlextDbtOracleTypeError = _exc["FlextDbtOracleProcessingError"]
FlextDbtOraclePermissionError = _exc["FlextDbtOracleProcessingError"]
FlextDbtOracleResourceError = _exc["FlextDbtOracleProcessingError"]

# Performance and Timeout Exceptions
FlextDbtOracleTimeoutError = _exc["FlextDbtOracleTimeoutError"]
FlextDbtOraclePerformanceError = _exc["FlextDbtOracleProcessingError"]

# Export all exception types
__all__: list[str] = [
    "FlextDbtOracleAuthenticationError",
    "FlextDbtOracleCompilationError",
    # Configuration and Setup
    "FlextDbtOracleConfigError",
    "FlextDbtOracleConnectionError",
    # Database Operations
    "FlextDbtOracleDatabaseError",
    "FlextDbtOracleExecutionError",
    # DBT-specific
    "FlextDbtOracleModelError",
    "FlextDbtOraclePerformanceError",
    "FlextDbtOraclePermissionError",
    # Data Processing
    "FlextDbtOracleProcessingError",
    "FlextDbtOracleQueryError",
    "FlextDbtOracleResourceError",
    "FlextDbtOracleSchemaError",
    # Performance and Timeout
    "FlextDbtOracleTimeoutError",
    "FlextDbtOracleTransformationError",
    # Oracle-specific
    "FlextDbtOracleTypeError",
    "FlextDbtOracleValidationError",
]
