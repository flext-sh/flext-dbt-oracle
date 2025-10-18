"""FLEXT DBT Oracle Types - Domain-specific DBT Oracle type definitions.

This module provides DBT Oracle-specific type definitions extending FlextTypes.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextTypes properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes

# =============================================================================
# DBT ORACLE-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT Oracle operations
# =============================================================================


# DBT Oracle domain TypeVars
class FlextDbtOracleTypes(FlextTypes):
    """DBT Oracle-specific type definitions extending FlextTypes.

    Domain-specific type system for DBT Oracle data transformation operations.
    Contains ONLY complex DBT Oracle-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types for Oracle
    # =========================================================================

    class DbtProject:
        """DBT Oracle project complex types."""

        type ProjectConfiguration = dict[str, object | dict[str, object]]
        type ModelConfiguration = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SourceConfiguration = dict[str, str | list[dict[str, object]]]
        type ProfileConfiguration = dict[str, object]
        type MacroConfiguration = dict[str, str | dict[str, object]]
        type TestConfiguration = dict[str, str | bool | list[str]]

    # =========================================================================
    # ORACLE CONNECTION TYPES - Oracle database connection configuration
    # =========================================================================

    class OracleConnection:
        """Oracle connection complex types."""

        type ConnectionConfig = dict[str, str | int | bool | dict[str, object]]
        type DatabaseConnection = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type PoolingConfig = dict[str, int | bool | dict[str, object]]
        type SecurityConfig = dict[str, bool | str | dict[str, object]]
        type SessionConfig = dict[str, str | int | dict[str, object]]
        type TimeoutConfig = dict[str, int | float]

    # =========================================================================
    # ORACLE DATA TYPES - Oracle table and schema types
    # =========================================================================

    class OracleData:
        """Oracle data complex types."""

        type OracleTable = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        type OracleSchema = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type OracleColumn = dict[str, str | int | bool | dict[str, object]]
        type OracleQuery = dict[str, str | list[str] | int | dict[str, object]]
        type OracleIndex = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        type OracleConstraint = dict[str, str | bool | list[str] | dict[str, object]]

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration for Oracle
    # =========================================================================

    class DbtTransformation:
        """DBT Oracle transformation complex types."""

        type TransformationConfig = dict[str, FlextTypes.JsonValue | dict[str, object]]
        type SqlTransformation = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type DataValidation = dict[str, bool | str | list[str] | dict[str, object]]
        type MaterializationConfig = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type OutputFormat = dict[str, str | dict[str, object]]
        type ProcessingStep = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types for Oracle
    # =========================================================================

    class DbtModel:
        """DBT Oracle model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ModelExecution = dict[str, str | bool | int | dict[str, object]]
        type ModelDependency = dict[str, str | list[str] | dict[str, object]]
        type ModelTest = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        type ModelDocumentation = dict[str, str | dict[str, object]]
        type ModelMaterialization = dict[str, str | dict[str, object]]

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types for Oracle
    # =========================================================================

    class DbtSource:
        """DBT Oracle source complex types."""

        type SourceDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SourceConnection = dict[str, object | dict[str, object]]
        type SourceTable = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type SourceFreshness = dict[str, str | int | dict[str, object]]
        type SourceTest = dict[str, str | bool | list[str]]
        type SourceSchema = dict[str, str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # ORACLE ADAPTER TYPES - Oracle-specific adapter configuration
    # =========================================================================

    class OracleAdapter:
        """Oracle adapter complex types."""

        type AdapterConfiguration = dict[str, object | dict[str, object]]
        type ConnectionAdapter = dict[str, str | int | bool | dict[str, object]]
        type QueryAdapter = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SchemaAdapter = dict[str, str | list[str] | dict[str, object]]
        type TransactionAdapter = dict[
            str, bool | str | dict[str, FlextTypes.JsonValue]
        ]
        type CursorAdapter = dict[str, str | int | dict[str, object]]

    # =========================================================================
    # DBT ORACLE PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes):
        """DBT Oracle-specific project types extending FlextTypes.

        Adds DBT Oracle transformation-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        DBT Oracle domain owns Oracle data transformation-specific types.
        """

        # DBT Oracle-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextTypes
            "library",
            "application",
            "service",
            # DBT Oracle-specific types
            "dbt-oracle",
            "oracle-transform",
            "oracle-analytics",
            "oracle-dbt-models",
            "dbt-oracle-project",
            "oracle-dimensional",
            "oracle-warehouse",
            "oracle-etl",
            "dbt-oracle-pipeline",
            "oracle-reporting",
            "oracle-dbt",
            "oracle-data-warehouse",
            "oracle-adapter",
            "oracle-connector",
            "oracle-integration",
            "oracle-bi",
        ]

        # DBT Oracle-specific project configurations
        type DbtOracleProjectConfig = dict[str, object]
        type OracleTransformConfig = dict[str, str | int | bool | list[str]]
        type OracleAnalyticsConfig = dict[str, bool | str | dict[str, object]]
        type DbtOraclePipelineConfig = dict[str, object]


# =============================================================================
# PUBLIC API EXPORTS - DBT Oracle TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextDbtOracleTypes",
]
