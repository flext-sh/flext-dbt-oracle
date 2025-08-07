"""Oracle DBT exception hierarchy following flext-core patterns.

This module implements Oracle DBT-specific exceptions using proper static
inheritance from flext-core abstractions, following the architectural principle
of using generic functionality from abstract libraries correctly.
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


# Define Oracle DBT-specific exception hierarchy using static inheritance
class FlextDbtOracleError(FlextError):
    """Base Oracle DBT error following flext-core patterns."""

    def __init__(self, message: str = "Oracle DBT error", **kwargs: object) -> None:
        """Initialize Oracle DBT error with context."""
        super().__init__(
            message,
            error_code="FLEXT_DBT_ORACLE_ERROR",
            context=kwargs,
        )


class FlextDbtOracleValidationError(FlextValidationError):
    """Oracle DBT validation errors following flext-core patterns."""

    def __init__(self, message: str = "Oracle DBT validation error", **kwargs: object) -> None:
        """Initialize Oracle DBT validation error."""
        super().__init__(
            message,
            error_code="FLEXT_DBT_ORACLE_VALIDATION_ERROR",
            context=kwargs,
        )


class FlextDbtOracleConfigurationError(FlextConfigurationError):
    """Oracle DBT configuration errors following flext-core patterns."""

    def __init__(self, message: str = "Oracle DBT configuration error", **kwargs: object) -> None:
        """Initialize Oracle DBT configuration error."""
        super().__init__(
            message,
            **kwargs,
        )


class FlextDbtOracleConnectionError(FlextConnectionError):
    """Oracle DBT connection errors following flext-core patterns."""

    def __init__(self, message: str = "Oracle DBT connection error", **kwargs: object) -> None:
        """Initialize Oracle DBT connection error."""
        super().__init__(
            message,
            **kwargs,
        )


class FlextDbtOracleAuthenticationError(FlextAuthenticationError):
    """Oracle DBT authentication errors following flext-core patterns."""

    def __init__(self, message: str = "Oracle DBT authentication error", **kwargs: object) -> None:
        """Initialize Oracle DBT authentication error."""
        super().__init__(
            message,
            **kwargs,
        )


class FlextDbtOracleProcessingError(FlextProcessingError):
    """Oracle DBT processing errors following flext-core patterns."""

    def __init__(self, message: str = "Oracle DBT processing error", **kwargs: object) -> None:
        """Initialize Oracle DBT processing error."""
        super().__init__(
            message,
            **kwargs,
        )


class FlextDbtOracleTimeoutError(FlextTimeoutError):
    """Oracle DBT timeout errors following flext-core patterns."""

    def __init__(self, message: str = "Oracle DBT timeout error", **kwargs: object) -> None:
        """Initialize Oracle DBT timeout error."""
        super().__init__(
            message,
            **kwargs,
        )


# Create additional Oracle DBT-specific exceptions using static inheritance
class FlextDbtOracleModelError(FlextDbtOracleError):
    """Oracle DBT model-specific errors."""

    def __init__(self, message: str = "Oracle DBT model error", **kwargs: object) -> None:
        """Initialize Oracle DBT model error."""
        super().__init__(
            message,
            **kwargs,
        )


class FlextDbtOracleAdapterError(FlextDbtOracleError):
    """Oracle DBT adapter errors."""

    def __init__(self, message: str = "Oracle DBT adapter error", **kwargs: object) -> None:
        """Initialize Oracle DBT adapter error."""
        super().__init__(
            message,
            **kwargs,
        )


class FlextDbtOracleTestError(FlextDbtOracleError):
    """Oracle DBT test errors."""

    def __init__(self, message: str = "Oracle DBT test error", **kwargs: object) -> None:
        """Initialize Oracle DBT test error."""
        super().__init__(
            message,
            **kwargs,
        )


__all__: list[str] = [
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
