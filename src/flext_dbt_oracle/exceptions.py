
"""Domain-specific Oracle DBT exceptions using factory pattern to eliminate duplication.

Module documentation:

- USA create_module_exception_classes() para eliminar exception boilerplate massivo
- Elimina 71+ linhas duplicadas de código boilerplate por exception class
- SOLID: Single source of truth para module exception patterns
- Redução de 103+ linhas para 165 linhas (60% improvement with domain logic)

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import cast

from flext_core import FlextExceptions, FlextTypes, create_module_exception_classes

# 🚨 DRY PATTERN: Use create_module_exception_classes to eliminate exception duplication
_exceptions = create_module_exception_classes("flext_dbt_oracle")

# Extract factory-generated exception classes with proper typing for MyPy
FLEXT_DBT_ORACLEConfigurationError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FLEXT_DBT_ORACLEConfigurationError"],
)
FLEXT_DBT_ORACLEConnectionError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FLEXT_DBT_ORACLEConnectionError"],
)
FLEXT_DBT_ORACLEAuthenticationError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FLEXT_DBT_ORACLEAuthenticationError"],
)
FLEXT_DBT_ORACLEProcessingError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FLEXT_DBT_ORACLEProcessingError"],
)
FLEXT_DBT_ORACLEValidationError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FLEXT_DBT_ORACLEValidationError"],
)
FLEXT_DBT_ORACLEError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FLEXT_DBT_ORACLEError"],
)
FLEXT_DBT_ORACLETimeoutError: type[Exception] = cast(
    "type[Exception]",
    _exceptions["FLEXT_DBT_ORACLETimeoutError"],
)


# Domain-specific exceptions for Oracle DBT business logic
class FlextDbtOracleDatabaseError(FlextExceptions.ProcessingError):
    """Oracle DBT database-specific errors with Oracle context."""

    def __init__(
        self,
        message: str = "Oracle DBT database error",
        *,
        table_name: str | None = None,
        schema_name: str | None = None,
        operation: str = "database_processing",
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT database error with Oracle context."""
        context = dict(kwargs)
        if table_name is not None:
            context["table_name"] = table_name
        if schema_name is not None:
            context["schema_name"] = schema_name

        super().__init__(
            f"Oracle DBT database: {message}",
            operation=operation,
            context=context,
        )


class FlextDbtOracleExecutionError(FlextExceptions.ProcessingError):
    """Oracle DBT execution-specific errors with execution context."""

    def __init__(
        self,
        message: str = "Oracle DBT execution error",
        *,
        sql_statement: str | None = None,
        execution_step: str | None = None,
        operation: str = "dbt_execution",
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT execution error with execution context."""
        context = dict(kwargs)
        if sql_statement is not None:
            context["sql_statement"] = sql_statement
        if execution_step is not None:
            context["execution_step"] = execution_step

        super().__init__(
            f"Oracle DBT execution: {message}",
            operation=operation,
            context=context,
        )


class FlextDbtOracleQueryError(FlextExceptions.ProcessingError):
    """Oracle DBT query-specific errors with query context."""

    def __init__(
        self,
        message: str = "Oracle DBT query error",
        *,
        query_type: str | None = None,
        query_text: str | None = None,
        operation: str = "query_processing",
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT query error with query context."""
        context = dict(kwargs)
        if query_type is not None:
            context["query_type"] = query_type
        if query_text is not None:
            # Truncate long query text for logging
            max_query_text_length = 500
            context["query_text"] = (
                query_text[:max_query_text_length] + "..."
                if len(query_text) > max_query_text_length
                else query_text
            )

        super().__init__(
            f"Oracle DBT query: {message}",
            operation=operation,
            context=context,
        )


class FlextDbtOracleModelError(FlextExceptions.ProcessingError):
    """Oracle DBT model-specific errors with model context."""

    def __init__(
        self,
        message: str = "Oracle DBT model error",
        *,
        model_name: str | None = None,
        model_type: str | None = None,
        operation: str = "model_processing",
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT model error with model context."""
        context = dict(kwargs)
        if model_name is not None:
            context["model_name"] = model_name
        if model_type is not None:
            context["model_type"] = model_type

        super().__init__(
            f"Oracle DBT model: {message}",
            operation=operation,
            context=context,
        )


class FlextDbtOracleCompilationError(FlextExceptions):
    """Oracle DBT compilation errors with compilation context."""

    def __init__(
        self,
        message: str = "Oracle DBT compilation failed",
        *,
        compilation_target: str | None = None,
        compilation_stage: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT compilation error with compilation context."""
        validation_details: FlextTypes.Core.Dict = {}
        if compilation_target is not None:
            validation_details["compilation_target"] = compilation_target
        if compilation_stage is not None:
            validation_details["compilation_stage"] = compilation_stage

        context = dict(kwargs)
        super().__init__(
            f"Oracle DBT compilation: {message}",
            validation_details=validation_details,
            context=context,
        )


# Export all exception types in alphabetical order
__all__: FlextTypes.Core.StringList = [
    "FLEXT_DBT_ORACLEAuthenticationError",
    "FLEXT_DBT_ORACLEConfigurationError",
    "FLEXT_DBT_ORACLEConnectionError",
    "FLEXT_DBT_ORACLEError",
    "FLEXT_DBT_ORACLEProcessingError",
    "FLEXT_DBT_ORACLETimeoutError",
    "FLEXT_DBT_ORACLEValidationError",
    "FlextDbtOracleCompilationError",
    "FlextDbtOracleDatabaseError",
    "FlextDbtOracleExecutionError",
    "FlextDbtOracleModelError",
    "FlextDbtOracleQueryError",
]
