"""FLEXT DBT Oracle Types - Domain-specific DBT Oracle type definitions.

This module provides DBT Oracle-specific type definitions extending FlextCore.Types.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextCore.Types properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextCore

# =============================================================================
# DBT ORACLE-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT Oracle operations
# =============================================================================


# DBT Oracle domain TypeVars
class FlextDbtOracleTypes(FlextCore.Types):
    """DBT Oracle-specific type definitions extending FlextCore.Types.

    Domain-specific type system for DBT Oracle data transformation operations.
    Contains ONLY complex DBT Oracle-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # DBT PROJECT TYPES - DBT project configuration types for Oracle
    # =========================================================================

    class DbtProject:
        """DBT Oracle project complex types."""

        type ProjectConfiguration = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type ModelConfiguration = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type SourceConfiguration = dict[str, str | list[FlextCore.Types.Dict]]
        type ProfileConfiguration = dict[str, FlextCore.Types.ConfigValue]
        type MacroConfiguration = dict[str, str | FlextCore.Types.Dict]
        type TestConfiguration = dict[str, str | bool | FlextCore.Types.StringList]

    # =========================================================================
    # ORACLE CONNECTION TYPES - Oracle database connection configuration
    # =========================================================================

    class OracleConnection:
        """Oracle connection complex types."""

        type ConnectionConfig = dict[str, str | int | bool | FlextCore.Types.Dict]
        type DatabaseConnection = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type PoolingConfig = dict[str, int | bool | FlextCore.Types.Dict]
        type SecurityConfig = dict[
            str, bool | str | dict[str, FlextCore.Types.ConfigValue]
        ]
        type SessionConfig = dict[str, str | int | FlextCore.Types.Dict]
        type TimeoutConfig = dict[str, int | float]

    # =========================================================================
    # ORACLE DATA TYPES - Oracle table and schema types
    # =========================================================================

    class OracleData:
        """Oracle data complex types."""

        type OracleTable = dict[
            str, str | FlextCore.Types.StringList | dict[str, FlextCore.Types.JsonValue]
        ]
        type OracleSchema = dict[str, str | list[dict[str, FlextCore.Types.JsonValue]]]
        type OracleColumn = dict[str, str | int | bool | FlextCore.Types.Dict]
        type OracleQuery = dict[
            str, str | FlextCore.Types.StringList | int | FlextCore.Types.Dict
        ]
        type OracleIndex = dict[
            str, str | FlextCore.Types.StringList | dict[str, FlextCore.Types.JsonValue]
        ]
        type OracleConstraint = dict[
            str, str | bool | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]

    # =========================================================================
    # DBT TRANSFORMATION TYPES - Data transformation configuration for Oracle
    # =========================================================================

    class DbtTransformation:
        """DBT Oracle transformation complex types."""

        type TransformationConfig = dict[
            str, FlextCore.Types.JsonValue | FlextCore.Types.Dict
        ]
        type SqlTransformation = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type DataValidation = dict[
            str, bool | str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type MaterializationConfig = dict[
            str, str | dict[str, FlextCore.Types.JsonValue]
        ]
        type OutputFormat = dict[str, str | FlextCore.Types.Dict]
        type ProcessingStep = dict[
            str, str | int | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # DBT MODEL TYPES - DBT model definition and execution types for Oracle
    # =========================================================================

    class DbtModel:
        """DBT Oracle model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type ModelExecution = dict[str, str | bool | int | FlextCore.Types.Dict]
        type ModelDependency = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type ModelTest = dict[str, str | bool | dict[str, FlextCore.Types.JsonValue]]
        type ModelDocumentation = dict[str, str | FlextCore.Types.Dict]
        type ModelMaterialization = dict[
            str, str | dict[str, FlextCore.Types.ConfigValue]
        ]

    # =========================================================================
    # DBT SOURCE TYPES - DBT source configuration types for Oracle
    # =========================================================================

    class DbtSource:
        """DBT Oracle source complex types."""

        type SourceDefinition = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type SourceConnection = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type SourceTable = dict[str, str | list[dict[str, FlextCore.Types.JsonValue]]]
        type SourceFreshness = dict[str, str | int | FlextCore.Types.Dict]
        type SourceTest = dict[str, str | bool | FlextCore.Types.StringList]
        type SourceSchema = dict[str, str | dict[str, FlextCore.Types.JsonValue]]

    # =========================================================================
    # ORACLE ADAPTER TYPES - Oracle-specific adapter configuration
    # =========================================================================

    class OracleAdapter:
        """Oracle adapter complex types."""

        type AdapterConfiguration = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type ConnectionAdapter = dict[str, str | int | bool | FlextCore.Types.Dict]
        type QueryAdapter = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type SchemaAdapter = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type TransactionAdapter = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]
        type CursorAdapter = dict[str, str | int | FlextCore.Types.Dict]

    # =========================================================================
    # DBT ORACLE PROJECT TYPES - Domain-specific project types extending FlextCore.Types
    # =========================================================================

    class Project(FlextCore.Types.Project):
        """DBT Oracle-specific project types extending FlextCore.Types.Project.

        Adds DBT Oracle transformation-specific project types while inheriting
        generic types from FlextCore.Types. Follows domain separation principle:
        DBT Oracle domain owns Oracle data transformation-specific types.
        """

        # DBT Oracle-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextCore.Types.Project
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
        type DbtOracleProjectConfig = dict[str, FlextCore.Types.ConfigValue | object]
        type OracleTransformConfig = dict[
            str, str | int | bool | FlextCore.Types.StringList
        ]
        type OracleAnalyticsConfig = dict[str, bool | str | FlextCore.Types.Dict]
        type DbtOraclePipelineConfig = dict[str, FlextCore.Types.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - DBT Oracle TypeVars and types
# =============================================================================

__all__: FlextCore.Types.StringList = [
    "FlextDbtOracleTypes",
]
