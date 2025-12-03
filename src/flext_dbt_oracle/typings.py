"""FLEXT DBT Oracle Types - Domain-specific DBT Oracle type definitions.

This module provides DBT Oracle-specific type definitions extending t.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends t properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import t

# =============================================================================
# DBT ORACLE-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT Oracle operations
# =============================================================================


# DBT Oracle domain TypeVars
class FlextDbtOracleTypes(t):
    """DBT Oracle-specific type definitions extending t.

    Domain-specific type system for DBT Oracle data transformation operations.
    Contains ONLY complex DBT Oracle-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types for Oracle
    # =========================================================================

    class DbtProject:
        """DBT Oracle project complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        ProjectConfiguration: type = dict[str, object | dict[str, object]]
        """DBT project configuration type."""
        ModelConfiguration: type = dict[str, str | dict[str, t.JsonValue]]
        """DBT model configuration type."""
        SourceConfiguration: type = dict[str, str | list[dict[str, object]]]
        """DBT source configuration type."""
        ProfileConfiguration: type = dict[str, object]
        """DBT profile configuration type."""
        MacroConfiguration: type = dict[str, str | dict[str, object]]
        """DBT macro configuration type."""
        TestConfiguration: type = dict[str, str | bool | list[str]]
        """DBT test configuration type."""

    # =========================================================================
    # ORACLE CONNECTION TYPES - Oracle database connection configuration
    # =========================================================================

    class OracleConnection:
        """Oracle connection complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        ConnectionConfig: type = dict[str, str | int | bool | dict[str, object]]
        """Oracle connection configuration type."""
        DatabaseConnection: type = dict[str, str | dict[str, t.JsonValue]]
        """Oracle database connection type."""
        PoolingConfig: type = dict[str, int | bool | dict[str, object]]
        """Oracle pooling configuration type."""
        SecurityConfig: type = dict[str, bool | str | dict[str, object]]
        """Oracle security configuration type."""
        SessionConfig: type = dict[str, str | int | dict[str, object]]
        """Oracle session configuration type."""
        TimeoutConfig: type = dict[str, int | float]
        """Oracle timeout configuration type."""

    # =========================================================================
    # ORACLE DATA TYPES - Oracle table and schema types
    # =========================================================================

    class OracleData:
        """Oracle data complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        OracleTable: type = dict[str, str | list[str] | dict[str, t.JsonValue]]
        """Oracle table type."""
        OracleSchema: type = dict[str, str | list[dict[str, t.JsonValue]]]
        """Oracle schema type."""
        OracleColumn: type = dict[str, str | int | bool | dict[str, object]]
        """Oracle column type."""
        OracleQuery: type = dict[str, str | list[str] | int | dict[str, object]]
        """Oracle query type."""
        OracleIndex: type = dict[str, str | list[str] | dict[str, t.JsonValue]]
        """Oracle index type."""
        OracleConstraint: type = dict[str, str | bool | list[str] | dict[str, object]]
        """Oracle constraint type."""

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration for Oracle
    # =========================================================================

    class DbtTransformation:
        """DBT Oracle transformation complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        TransformationConfig: type = dict[str, t.JsonValue | dict[str, object]]
        """DBT transformation configuration type."""
        SqlTransformation: type = dict[str, str | dict[str, t.JsonValue]]
        """SQL transformation type."""
        DataValidation: type = dict[str, bool | str | list[str] | dict[str, object]]
        """Data validation type."""
        MaterializationConfig: type = dict[str, str | dict[str, t.JsonValue]]
        """Materialization configuration type."""
        OutputFormat: type = dict[str, str | dict[str, object]]
        """Output format type."""
        ProcessingStep: type = dict[str, str | int | dict[str, t.JsonValue]]
        """Processing step type."""

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types for Oracle
    # =========================================================================

    class DbtModel:
        """DBT Oracle model complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        ModelDefinition: type = dict[str, str | dict[str, t.JsonValue]]
        """DBT model definition type."""
        ModelExecution: type = dict[str, str | bool | int | dict[str, object]]
        """DBT model execution type."""
        ModelDependency: type = dict[str, str | list[str] | dict[str, object]]
        """DBT model dependency type."""
        ModelTest: type = dict[str, str | bool | dict[str, t.JsonValue]]
        """DBT model test type."""
        ModelDocumentation: type = dict[str, str | dict[str, object]]
        """DBT model documentation type."""
        ModelMaterialization: type = dict[str, str | dict[str, object]]
        """DBT model materialization type."""

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types for Oracle
    # =========================================================================

    class DbtSource:
        """DBT Oracle source complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        SourceDefinition: type = dict[str, str | dict[str, t.JsonValue]]
        """DBT source definition type."""
        SourceConnection: type = dict[str, object | dict[str, object]]
        """DBT source connection type."""
        SourceTable: type = dict[str, str | list[dict[str, t.JsonValue]]]
        """DBT source table type."""
        SourceFreshness: type = dict[str, str | int | dict[str, object]]
        """DBT source freshness type."""
        SourceTest: type = dict[str, str | bool | list[str]]
        """DBT source test type."""
        SourceSchema: type = dict[str, str | dict[str, t.JsonValue]]
        """DBT source schema type."""

    # =========================================================================
    # ORACLE ADAPTER TYPES - Oracle-specific adapter configuration
    # =========================================================================

    class OracleAdapter:
        """Oracle adapter complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        AdapterConfiguration: type = dict[str, object | dict[str, object]]
        """Oracle adapter configuration type."""
        ConnectionAdapter: type = dict[str, str | int | bool | dict[str, object]]
        """Oracle connection adapter type."""
        QueryAdapter: type = dict[str, str | dict[str, t.JsonValue]]
        """Oracle query adapter type."""
        SchemaAdapter: type = dict[str, str | list[str] | dict[str, object]]
        """Oracle schema adapter type."""
        TransactionAdapter: type = dict[str, bool | str | dict[str, t.JsonValue]]
        """Oracle transaction adapter type."""
        CursorAdapter: type = dict[str, str | int | dict[str, object]]
        """Oracle cursor adapter type."""

    # =========================================================================
    # DBT ORACLE PROJECT TYPES - Domain-specific project types extending t
    # =========================================================================

    class Project(t):
        """DBT Oracle-specific project types extending t.

        Adds DBT Oracle transformation-specific project types while inheriting
        generic types from t. Follows domain separation principle:
        DBT Oracle domain owns Oracle data transformation-specific types.
        """

        # DBT Oracle-specific project types extending the generic ones
        # Python 3.13+ best practice: Use TypeAlias for better type checking
        ProjectType: type = Literal[
            # Generic types inherited from t
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
        """DBT Oracle project type literal."""

        # DBT Oracle-specific project configurations
        DbtOracleProjectConfig: type = dict[str, object]
        """DBT Oracle project configuration type."""
        OracleTransformConfig: type = dict[str, str | int | bool | list[str]]
        """Oracle transformation configuration type."""
        OracleAnalyticsConfig: type = dict[str, bool | str | dict[str, object]]
        """Oracle analytics configuration type."""
        DbtOraclePipelineConfig: type = dict[str, object]
        """DBT Oracle pipeline configuration type."""


# =============================================================================
# PUBLIC API EXPORTS - DBT Oracle TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextDbtOracleTypes",
]
