from flext_core.exceptions import FlextProcessingError, FlextValidationError

__all__ = [
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

FLEXT_DBT_ORACLEConfigurationError: type[Exception]
FLEXT_DBT_ORACLEConnectionError: type[Exception]
FLEXT_DBT_ORACLEAuthenticationError: type[Exception]
FLEXT_DBT_ORACLEProcessingError: type[Exception]
FLEXT_DBT_ORACLEValidationError: type[Exception]
FLEXT_DBT_ORACLEError: type[Exception]
FLEXT_DBT_ORACLETimeoutError: type[Exception]

class FlextDbtOracleDatabaseError(FlextProcessingError):
    def __init__(
        self,
        message: str = "Oracle DBT database error",
        *,
        table_name: str | None = None,
        schema_name: str | None = None,
        operation: str = "database_processing",
        **kwargs: object,
    ) -> None: ...

class FlextDbtOracleExecutionError(FlextProcessingError):
    def __init__(
        self,
        message: str = "Oracle DBT execution error",
        *,
        sql_statement: str | None = None,
        execution_step: str | None = None,
        operation: str = "dbt_execution",
        **kwargs: object,
    ) -> None: ...

class FlextDbtOracleQueryError(FlextProcessingError):
    def __init__(
        self,
        message: str = "Oracle DBT query error",
        *,
        query_type: str | None = None,
        query_text: str | None = None,
        operation: str = "query_processing",
        **kwargs: object,
    ) -> None: ...

class FlextDbtOracleModelError(FlextProcessingError):
    def __init__(
        self,
        message: str = "Oracle DBT model error",
        *,
        model_name: str | None = None,
        model_type: str | None = None,
        operation: str = "model_processing",
        **kwargs: object,
    ) -> None: ...

class FlextDbtOracleCompilationError(FlextValidationError):
    def __init__(
        self,
        message: str = "Oracle DBT compilation failed",
        *,
        compilation_target: str | None = None,
        compilation_stage: str | None = None,
        **kwargs: object,
    ) -> None: ...
