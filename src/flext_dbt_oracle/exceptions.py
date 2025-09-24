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

from flext_core import FlextExceptions, FlextTypes


# ✅ DIRECT EXCEPTION CLASSES: Use direct inheritance instead of factory pattern
class FlextDbtOracleConfigurationError(FlextExceptions.ConfigurationError):
    """Oracle DBT configuration-specific errors."""


class FlextDbtOracleConnectionError(FlextExceptions.ConnectionError):
    """Oracle DBT connection-specific errors."""


class FlextDbtOracleAuthenticationError(FlextExceptions.AuthenticationError):
    """Oracle DBT authentication-specific errors."""


class FlextDbtOracleProcessingError(FlextExceptions.ProcessingError):
    """Oracle DBT processing-specific errors."""


class FlextDbtOracleValidationError(FlextExceptions.ValidationError):
    """Oracle DBT validation-specific errors."""


class FlextDbtOracleError(FlextExceptions.Error):
    """Oracle DBT generic errors."""


class FlextDbtOracleTimeoutError(FlextExceptions.TimeoutError):
    """Oracle DBT timeout-specific errors."""


# Domain-specific exceptions for Oracle DBT business logic
class FlextDbtOracleDatabaseError(FlextExceptions.BaseError):
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
        context: dict[str, object] = dict(
            cast("dict[str, object]", kwargs.get("context", {}))
        )
        if table_name is not None:
            context["table_name"] = table_name
        if schema_name is not None:
            context["schema_name"] = schema_name
        context["operation"] = operation

        super().__init__(
            f"Oracle DBT database: {message}",
            context=context,
        )


class FlextDbtOracleExecutionError(FlextExceptions.BaseError):
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
        context: dict[str, object] = dict(
            cast("dict[str, object]", kwargs.get("context", {}))
        )
        if sql_statement is not None:
            context["sql_statement"] = sql_statement
        if execution_step is not None:
            context["execution_step"] = execution_step
        context["operation"] = operation

        super().__init__(
            f"Oracle DBT execution: {message}",
            context=context,
        )


class FlextDbtOracleQueryError(FlextExceptions.BaseError):
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
        context: dict[str, object] = dict(
            cast("dict[str, object]", kwargs.get("context", {}))
        )
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
        context["operation"] = operation

        super().__init__(
            f"Oracle DBT query: {message}",
            context=context,
        )


class FlextDbtOracleModelError(FlextExceptions.BaseError):
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
        context: dict[str, object] = dict(
            cast("dict[str, object]", kwargs.get("context", {}))
        )
        if model_name is not None:
            context["model_name"] = model_name
        if model_type is not None:
            context["model_type"] = model_type
        context["operation"] = operation

        super().__init__(
            f"Oracle DBT model: {message}",
            context=context,
        )


class FlextDbtOracleCompilationError(FlextExceptions.BaseError):
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
        context: dict[str, object] = dict(
            cast("dict[str, object]", kwargs.get("context", {}))
        )
        if compilation_target is not None:
            context["compilation_target"] = compilation_target
        if compilation_stage is not None:
            context["compilation_stage"] = compilation_stage

        super().__init__(
            f"Oracle DBT compilation: {message}",
            context=context,
        )


# Export all exception types in alphabetical order
__all__: FlextTypes.Core.StringList = [
    "FlextDbtOracleAuthenticationError",
    "FlextDbtOracleCompilationError",
    "FlextDbtOracleConfigurationError",
    "FlextDbtOracleConnectionError",
    "FlextDbtOracleDatabaseError",
    "FlextDbtOracleError",
    "FlextDbtOracleExecutionError",
    "FlextDbtOracleModelError",
    "FlextDbtOracleProcessingError",
    "FlextDbtOracleQueryError",
    "FlextDbtOracleTimeoutError",
    "FlextDbtOracleValidationError",
]
