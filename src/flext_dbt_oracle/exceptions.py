"""Oracle DBT exception hierarchy using flext-core patterns.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT

Domain-specific exceptions for Oracle DBT operations inheriting from flext-core.
"""

from __future__ import annotations

from flext_core.exceptions import (
    FlextAuthenticationError,
    FlextConfigurationError,
    FlextConnectionError,
    FlextError,
    FlextProcessingError,
    FlextTimeoutError,
    FlextValidationError,
)


class FlextDbtOracleError(FlextError):
    """Base exception for Oracle DBT operations."""

    def __init__(
        self,
        message: str = "Oracle DBT error",
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT error with context."""
        context = kwargs.copy()
        if model_name is not None:
            context["model_name"] = model_name

        super().__init__(message, error_code="ORACLE_DBT_ERROR", context=context)


class FlextDbtOracleConnectionError(FlextConnectionError):
    """Oracle DBT connection errors."""

    def __init__(
        self,
        message: str = "Oracle DBT connection failed",
        database_name: str | None = None,
        host: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT connection error with context."""
        context = kwargs.copy()
        if database_name is not None:
            context["database_name"] = database_name
        if host is not None:
            context["host"] = host

        super().__init__(f"Oracle DBT connection: {message}", **context)


class FlextDbtOracleAuthenticationError(FlextAuthenticationError):
    """Oracle DBT authentication errors."""

    def __init__(
        self,
        message: str = "Oracle DBT authentication failed",
        username: str | None = None,
        database_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT authentication error with context."""
        context = kwargs.copy()
        if username is not None:
            context["username"] = username
        if database_name is not None:
            context["database_name"] = database_name

        super().__init__(f"Oracle DBT auth: {message}", **context)


class FlextDbtOracleValidationError(FlextValidationError):
    """Oracle DBT validation errors."""

    def __init__(
        self,
        message: str = "Oracle DBT validation failed",
        field: str | None = None,
        value: object = None,
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT validation error with context."""
        validation_details: dict[str, object] = {}
        if field is not None:
            validation_details["field"] = field
        if value is not None:
            validation_details["value"] = str(value)[:100]  # Truncate long values

        context = kwargs.copy()
        if model_name is not None:
            context["model_name"] = model_name

        super().__init__(
            f"Oracle DBT validation: {message}",
            validation_details=validation_details,
            context=context,
        )


class FlextDbtOracleConfigurationError(FlextConfigurationError):
    """Oracle DBT configuration errors."""

    def __init__(
        self,
        message: str = "Oracle DBT configuration error",
        config_key: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT configuration error with context."""
        context = kwargs.copy()
        if config_key is not None:
            context["config_key"] = config_key

        super().__init__(f"Oracle DBT config: {message}", **context)


class FlextDbtOracleProcessingError(FlextProcessingError):
    """Oracle DBT processing errors."""

    def __init__(
        self,
        message: str = "Oracle DBT processing failed",
        model_name: str | None = None,
        stage: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT processing error with context."""
        context = kwargs.copy()
        if model_name is not None:
            context["model_name"] = model_name
        if stage is not None:
            context["stage"] = stage

        super().__init__(f"Oracle DBT processing: {message}", **context)


class FlextDbtOracleTimeoutError(FlextTimeoutError):
    """Oracle DBT timeout errors."""

    def __init__(
        self,
        message: str = "Oracle DBT operation timed out",
        operation: str | None = None,
        timeout_seconds: float | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT timeout error with context."""
        context = kwargs.copy()
        if operation is not None:
            context["operation"] = operation
        if timeout_seconds is not None:
            context["timeout_seconds"] = timeout_seconds

        super().__init__(f"Oracle DBT timeout: {message}", **context)


class FlextDbtOracleModelError(FlextDbtOracleError):
    """Oracle DBT model-specific errors."""

    def __init__(
        self,
        message: str = "Oracle DBT model error",
        model_name: str | None = None,
        model_type: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT model error with context."""
        context = kwargs.copy()
        if model_type is not None:
            context["model_type"] = model_type

        super().__init__(
            f"Oracle DBT model: {message}",
            model_name=model_name,
            **context,
        )


class FlextDbtOracleAdapterError(FlextDbtOracleError):
    """Oracle DBT adapter errors."""

    def __init__(
        self,
        message: str = "Oracle DBT adapter error",
        adapter_method: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT adapter error with context."""
        context = kwargs.copy()
        if adapter_method is not None:
            context["adapter_method"] = adapter_method

        super().__init__(f"Oracle DBT adapter: {message}", context=context)


class FlextDbtOracleTestError(FlextDbtOracleError):
    """Oracle DBT test errors."""

    def __init__(
        self,
        message: str = "Oracle DBT test failed",
        test_name: str | None = None,
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle DBT test error with context."""
        context = kwargs.copy()
        if test_name is not None:
            context["test_name"] = test_name

        super().__init__(
            f"Oracle DBT test: {message}",
            model_name=model_name,
            **context,
        )


__all__ = [
    "FlextDbtOracleAdapterError",
    "FlextDbtOracleAuthenticationError",
    "FlextDbtOracleConfigurationError",
    "FlextDbtOracleConnectionError",
    "FlextDbtOracleError",
    "FlextDbtOracleModelError",
    "FlextDbtOracleProcessingError",
    "FlextDbtOracleTestError",
    "FlextDbtOracleTimeoutError",
    "FlextDbtOracleValidationError",
]
