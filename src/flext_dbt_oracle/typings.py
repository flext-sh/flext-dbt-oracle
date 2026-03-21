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

from flext_meltano import FlextMeltanoTypes

type ColumnSpec = dict[str, str]
type OraclePayload = dict[str, str | int | float | bool | None]
type OraclePayloadList = list[OraclePayload]


class FlextDbtOracleTypes(FlextMeltanoTypes):
    """DBT Oracle-specific type definitions extending t.

    Domain-specific type system for DBT Oracle data transformation operations.
    Contains ONLY complex DBT Oracle-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class DbtOracle:
        """DBT Oracle project complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ProjectConfiguration = dict[str, t.ContainerValue]
        "DBT project configuration type."
        type ModelConfiguration = dict[str, str | t.ContainerValue]
        "DBT model configuration type."
        type SourceConfiguration = dict[str, str | list[dict[str, t.ContainerValue]]]
        "DBT source configuration type."
        type ProfileConfiguration = dict[str, t.ContainerValue]
        "DBT profile configuration type."
        type MacroConfiguration = dict[str, str | t.ContainerValue]
        "DBT macro configuration type."
        type TestConfiguration = dict[str, str | bool | list[str]]
        "DBT test configuration type."

    class OracleConnection:
        """Oracle connection complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ConnectionConfig = dict[str, str | int | bool | t.ContainerValue]
        "Oracle connection configuration type."
        type DatabaseConnection = dict[str, str | t.ContainerValue]
        "Oracle database connection type."
        type PoolingConfig = dict[str, int | bool | t.ContainerValue]
        "Oracle pooling configuration type."
        type SecurityConfig = dict[str, bool | str | t.ContainerValue]
        "Oracle security configuration type."
        type SessionConfig = dict[str, str | int | t.ContainerValue]
        "Oracle session configuration type."
        type TimeoutConfig = dict[str, int | float]
        "Oracle timeout configuration type."

    class OracleData:
        """Oracle data complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type OracleTable = dict[str, str | list[str] | t.ContainerValue]
        "Oracle table type."
        type OracleSchema = dict[str, str | list[dict[str, t.ContainerValue]]]
        "Oracle schema type."
        type OracleColumn = dict[str, str | int | bool | t.ContainerValue]
        "Oracle column type."
        type OracleQuery = dict[str, str | list[str] | int | t.ContainerValue]
        "Oracle query type."
        type OracleIndex = dict[str, str | list[str] | t.ContainerValue]
        "Oracle index type."
        type OracleConstraint = dict[str, str | bool | list[str] | t.ContainerValue]
        "Oracle constraint type."

    class DbtTransformation:
        """DBT Oracle transformation complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type TransformationConfig = dict[str, t.ContainerValue]
        "DBT transformation configuration type."
        type SqlTransformation = dict[str, str | t.ContainerValue]
        "SQL transformation type."
        type DataValidation = dict[str, bool | str | list[str] | t.ContainerValue]
        "Data validation type."
        type MaterializationConfig = dict[str, str | t.ContainerValue]
        "Materialization configuration type."
        type OutputFormat = dict[str, str | t.ContainerValue]
        "Output format type."
        type ProcessingStep = dict[str, str | int | t.ContainerValue]
        "Processing step type."

    class DbtModel:
        """DBT Oracle model complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ModelDefinition = dict[str, str | t.ContainerValue]
        "DBT model definition type."
        type ModelExecution = dict[str, str | bool | int | t.ContainerValue]
        "DBT model execution type."
        type ModelDependency = dict[str, str | list[str] | t.ContainerValue]
        "DBT model dependency type."
        type ModelTest = dict[str, str | bool | t.ContainerValue]
        "DBT model test type."
        type ModelDocumentation = dict[str, str | t.ContainerValue]
        "DBT model documentation type."
        type ModelMaterialization = dict[str, str | t.ContainerValue]
        "DBT model materialization type."

    class DbtSource:
        """DBT Oracle source complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type SourceDefinition = dict[str, str | t.ContainerValue]
        "DBT source definition type."
        type SourceConnection = dict[str, t.ContainerValue]
        "DBT source connection type."
        type SourceTable = dict[str, str | list[dict[str, t.ContainerValue]]]
        "DBT source table type."
        type SourceFreshness = dict[str, str | int | t.ContainerValue]
        "DBT source freshness type."
        type SourceTest = dict[str, str | bool | list[str]]
        "DBT source test type."
        type SourceSchema = dict[str, str | t.ContainerValue]
        "DBT source schema type."

    class OracleAdapter:
        """Oracle adapter complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type AdapterConfiguration = dict[str, t.ContainerValue]
        "Oracle adapter configuration type."
        type ConnectionAdapter = dict[str, str | int | bool | t.ContainerValue]
        "Oracle connection adapter type."
        type QueryAdapter = dict[str, str | t.ContainerValue]
        "Oracle query adapter type."
        type SchemaAdapter = dict[str, str | list[str] | t.ContainerValue]
        "Oracle schema adapter type."
        type TransactionAdapter = dict[str, bool | str | t.ContainerValue]
        "Oracle transaction adapter type."
        type CursorAdapter = dict[str, str | int | t.ContainerValue]
        "Oracle cursor adapter type."

    class Project:
        """DBT Oracle-specific project types.

        Adds DBT Oracle transformation-specific project types.
        Follows domain separation principle:
        DBT Oracle domain owns Oracle data transformation-specific types.
        """

        type DbtOracleProjectType = object  # type: ignore[assignment]
        "DBT Oracle project type literal."
        type DbtOracleProjectConfig = dict[str, t.ContainerValue]
        "DBT Oracle project configuration type."
        type OracleTransformConfig = dict[str, str | int | bool | list[str]]
        "Oracle transformation configuration type."
        type OracleAnalyticsConfig = dict[str, bool | str | t.ContainerValue]
        "Oracle analytics configuration type."
        type DbtOraclePipelineConfig = dict[str, t.ContainerValue]
        "DBT Oracle pipeline configuration type."


t = FlextDbtOracleTypes
__all__ = [
    "ColumnSpec",
    "FlextDbtOracleTypes",
    "OraclePayload",
    "OraclePayloadList",
    "t",
]
