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

        type ProjectConfiguration = dict[str, FlextTypes.ConfigValue | FlextTypes.Dict]
        type ModelConfiguration = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SourceConfiguration = dict[str, str | list[FlextTypes.Dict]]
        type ProfileConfiguration = dict[str, FlextTypes.ConfigValue]
        type MacroConfiguration = dict[str, str | FlextTypes.Dict]
        type TestConfiguration = dict[str, str | bool | FlextTypes.StringList]

    # =========================================================================
    # ORACLE CONNECTION TYPES - Oracle database connection configuration
    # =========================================================================

    class OracleConnection:
        """Oracle connection complex types."""

        type ConnectionConfig = dict[str, str | int | bool | FlextTypes.Dict]
        type DatabaseConnection = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type PoolingConfig = dict[str, int | bool | FlextTypes.Dict]
        type SecurityConfig = dict[str, bool | str | dict[str, FlextTypes.ConfigValue]]
        type SessionConfig = dict[str, str | int | FlextTypes.Dict]
        type TimeoutConfig = dict[str, int | float]

    # =========================================================================
    # ORACLE DATA TYPES - Oracle table and schema types
    # =========================================================================

    class OracleData:
        """Oracle data complex types."""

        type OracleTable = dict[
            str, str | FlextTypes.StringList | dict[str, FlextTypes.JsonValue]
        ]
        type OracleSchema = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type OracleColumn = dict[str, str | int | bool | FlextTypes.Dict]
        type OracleQuery = dict[
            str, str | FlextTypes.StringList | int | FlextTypes.Dict
        ]
        type OracleIndex = dict[
            str, str | FlextTypes.StringList | dict[str, FlextTypes.JsonValue]
        ]
        type OracleConstraint = dict[
            str, str | bool | FlextTypes.StringList | FlextTypes.Dict
        ]

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration for Oracle
    # =========================================================================

    class DbtTransformation:
        """DBT Oracle transformation complex types."""

        type TransformationConfig = dict[str, FlextTypes.JsonValue | FlextTypes.Dict]
        type SqlTransformation = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type DataValidation = dict[
            str, bool | str | FlextTypes.StringList | FlextTypes.Dict
        ]
        type MaterializationConfig = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type OutputFormat = dict[str, str | FlextTypes.Dict]
        type ProcessingStep = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types for Oracle
    # =========================================================================

    class DbtModel:
        """DBT Oracle model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ModelExecution = dict[str, str | bool | int | FlextTypes.Dict]
        type ModelDependency = dict[str, str | FlextTypes.StringList | FlextTypes.Dict]
        type ModelTest = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        type ModelDocumentation = dict[str, str | FlextTypes.Dict]
        type ModelMaterialization = dict[str, str | dict[str, FlextTypes.ConfigValue]]

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types for Oracle
    # =========================================================================

    class DbtSource:
        """DBT Oracle source complex types."""

        type SourceDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SourceConnection = dict[str, FlextTypes.ConfigValue | FlextTypes.Dict]
        type SourceTable = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type SourceFreshness = dict[str, str | int | FlextTypes.Dict]
        type SourceTest = dict[str, str | bool | FlextTypes.StringList]
        type SourceSchema = dict[str, str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # ORACLE ADAPTER TYPES - Oracle-specific adapter configuration
    # =========================================================================

    class OracleAdapter:
        """Oracle adapter complex types."""

        type AdapterConfiguration = dict[str, FlextTypes.ConfigValue | FlextTypes.Dict]
        type ConnectionAdapter = dict[str, str | int | bool | FlextTypes.Dict]
        type QueryAdapter = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SchemaAdapter = dict[str, str | FlextTypes.StringList | FlextTypes.Dict]
        type TransactionAdapter = dict[
            str, bool | str | dict[str, FlextTypes.JsonValue]
        ]
        type CursorAdapter = dict[str, str | int | FlextTypes.Dict]

    # =========================================================================
    # DBT ORACLE PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes.Project):
        """DBT Oracle-specific project types extending FlextTypes.Project.

        Adds DBT Oracle transformation-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        DBT Oracle domain owns Oracle data transformation-specific types.
        """

        # DBT Oracle-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextTypes.Project
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
        type DbtOracleProjectConfig = dict[str, FlextTypes.ConfigValue | object]
        type OracleTransformConfig = dict[str, str | int | bool | FlextTypes.StringList]
        type OracleAnalyticsConfig = dict[str, bool | str | FlextTypes.Dict]
        type DbtOraclePipelineConfig = dict[str, FlextTypes.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - DBT Oracle TypeVars and types
# =============================================================================

__all__: FlextTypes.StringList = [
    "FlextDbtOracleTypes",
]
