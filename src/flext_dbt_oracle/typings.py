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

from flext import FlextTypes

# =============================================================================
# DBT ORACLE-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT Oracle operations
# =============================================================================


# DBT Oracle domain TypeVars
class FlextDbtOracleTypes(FlextTypes):
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

        type ProjectConfiguration = dict[str, object | dict[str, object]]
        """DBT project configuration type."""
        type ModelConfiguration = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT model configuration type."""
        type SourceConfiguration = dict[str, str | list[dict[str, object]]]
        """DBT source configuration type."""
        type ProfileConfiguration = dict[str, object]
        """DBT profile configuration type."""
        type MacroConfiguration = dict[str, str | dict[str, object]]
        """DBT macro configuration type."""
        type TestConfiguration = dict[str, str | bool | list[str]]
        """DBT test configuration type."""

    # =========================================================================
    # ORACLE CONNECTION TYPES - Oracle database connection configuration
    # =========================================================================

    class OracleConnection:
        """Oracle connection complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ConnectionConfig = dict[str, str | int | bool | dict[str, object]]
        """Oracle connection configuration type."""
        type DatabaseConnection = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """Oracle database connection type."""
        type PoolingConfig = dict[str, int | bool | dict[str, object]]
        """Oracle pooling configuration type."""
        type SecurityConfig = dict[str, bool | str | dict[str, object]]
        """Oracle security configuration type."""
        type SessionConfig = dict[str, str | int | dict[str, object]]
        """Oracle session configuration type."""
        type TimeoutConfig = dict[str, int | float]
        """Oracle timeout configuration type."""

    # =========================================================================
    # ORACLE DATA TYPES - Oracle table and schema types
    # =========================================================================

    class OracleData:
        """Oracle data complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type OracleTable = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        """Oracle table type."""
        type OracleSchema = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        """Oracle schema type."""
        type OracleColumn = dict[str, str | int | bool | dict[str, object]]
        """Oracle column type."""
        type OracleQuery = dict[str, str | list[str] | int | dict[str, object]]
        """Oracle query type."""
        type OracleIndex = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        """Oracle index type."""
        type OracleConstraint = dict[str, str | bool | list[str] | dict[str, object]]
        """Oracle constraint type."""

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration for Oracle
    # =========================================================================

    class DbtTransformation:
        """DBT Oracle transformation complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type TransformationConfig = dict[str, FlextTypes.JsonValue | dict[str, object]]
        """DBT transformation configuration type."""
        type SqlTransformation = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """SQL transformation type."""
        type DataValidation = dict[str, bool | str | list[str] | dict[str, object]]
        """Data validation type."""
        type MaterializationConfig = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """Materialization configuration type."""
        type OutputFormat = dict[str, str | dict[str, object]]
        """Output format type."""
        type ProcessingStep = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        """Processing step type."""

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types for Oracle
    # =========================================================================

    class DbtModel:
        """DBT Oracle model complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ModelDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT model definition type."""
        type ModelExecution = dict[str, str | bool | int | dict[str, object]]
        """DBT model execution type."""
        type ModelDependency = dict[str, str | list[str] | dict[str, object]]
        """DBT model dependency type."""
        type ModelTest = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        """DBT model test type."""
        type ModelDocumentation = dict[str, str | dict[str, object]]
        """DBT model documentation type."""
        type ModelMaterialization = dict[str, str | dict[str, object]]
        """DBT model materialization type."""

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types for Oracle
    # =========================================================================

    class DbtSource:
        """DBT Oracle source complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type SourceDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT source definition type."""
        type SourceConnection = dict[str, object | dict[str, object]]
        """DBT source connection type."""
        type SourceTable = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        """DBT source table type."""
        type SourceFreshness = dict[str, str | int | dict[str, object]]
        """DBT source freshness type."""
        type SourceTest = dict[str, str | bool | list[str]]
        """DBT source test type."""
        type SourceSchema = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT source schema type."""

    # =========================================================================
    # ORACLE ADAPTER TYPES - Oracle-specific adapter configuration
    # =========================================================================

    class OracleAdapter:
        """Oracle adapter complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type AdapterConfiguration = dict[str, object | dict[str, object]]
        """Oracle adapter configuration type."""
        type ConnectionAdapter = dict[str, str | int | bool | dict[str, object]]
        """Oracle connection adapter type."""
        type QueryAdapter = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """Oracle query adapter type."""
        type SchemaAdapter = dict[str, str | list[str] | dict[str, object]]
        """Oracle schema adapter type."""
        type TransactionAdapter = dict[
            str, bool | str | dict[str, FlextTypes.JsonValue],
        ]
        """Oracle transaction adapter type."""
        type CursorAdapter = dict[str, str | int | dict[str, object]]
        """Oracle cursor adapter type."""

    # =========================================================================
    # DBT ORACLE PROJECT TYPES - Domain-specific project types extending t
    # =========================================================================

    class Project:
        """DBT Oracle-specific project types.

        Adds DBT Oracle transformation-specific project types.
        Follows domain separation principle:
        DBT Oracle domain owns Oracle data transformation-specific types.
        """

        # DBT Oracle-specific project types - PEP 695 syntax
        type ProjectType = Literal[
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
        type DbtOracleProjectConfig = dict[str, object]
        """DBT Oracle project configuration type."""
        type OracleTransformConfig = dict[str, str | int | bool | list[str]]
        """Oracle transformation configuration type."""
        type OracleAnalyticsConfig = dict[str, bool | str | dict[str, object]]
        """Oracle analytics configuration type."""
        type DbtOraclePipelineConfig = dict[str, object]
        """DBT Oracle pipeline configuration type."""

    class DbtOracle:
        """DBT Oracle types namespace for cross-project access.

        Provides organized access to all DBT Oracle types for other FLEXT projects.
        Usage: Other projects can reference `t.DbtOracle.OracleData.*`, `t.DbtOracle.Project.*`, etc.
        This enables consistent namespace patterns for cross-project type access.

        Examples:
            from flext_dbt_oracle.typings import t
            config: t.DbtOracle.Project.DbtOracleProjectConfig = ...
            table: t.DbtOracle.OracleData.OracleTable = ...

        Note: Namespace composition via inheritance - no aliases needed.
        Access parent namespaces directly through inheritance.

        """


# Alias for simplified usage
t = FlextDbtOracleTypes

# Namespace composition via class inheritance
# DbtOracle namespace provides access to nested classes through inheritance
# Access patterns:
# - t.DbtOracle.* for DBT Oracle-specific types
# - t.Project.* for project types
# - t.Core.* for core types (inherited from parent)

__all__ = [
    "FlextDbtOracleTypes",
    "t",
]
