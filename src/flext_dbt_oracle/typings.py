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

from collections.abc import Mapping, Sequence

from flext_meltano import FlextMeltanoTypes

type ColumnSpec = Mapping[str, str]
type OraclePayload = Mapping[str, str | int | float | bool | None]
type OraclePayloadList = Sequence[OraclePayload]


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

        type ProjectConfiguration = Mapping[str, t.ContainerValue]
        "DBT project configuration type."
        type ModelConfiguration = Mapping[str, str | t.ContainerValue]
        "DBT model configuration type."
        type SourceConfiguration = Mapping[
            str, str | Sequence[Mapping[str, t.ContainerValue]]
        ]
        "DBT source configuration type."
        type ProfileConfiguration = Mapping[str, t.ContainerValue]
        "DBT profile configuration type."
        type MacroConfiguration = Mapping[str, str | t.ContainerValue]
        "DBT macro configuration type."
        type TestConfiguration = Mapping[str, str | bool | Sequence[str]]
        "DBT test configuration type."

    class OracleConnection:
        """Oracle connection complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ConnectionConfig = Mapping[str, str | int | bool | t.ContainerValue]
        "Oracle connection configuration type."
        type DatabaseConnection = Mapping[str, str | t.ContainerValue]
        "Oracle database connection type."
        type PoolingConfig = Mapping[str, int | bool | t.ContainerValue]
        "Oracle pooling configuration type."
        type SecurityConfig = Mapping[str, bool | str | t.ContainerValue]
        "Oracle security configuration type."
        type SessionConfig = Mapping[str, str | int | t.ContainerValue]
        "Oracle session configuration type."
        type TimeoutConfig = Mapping[str, int | float]
        "Oracle timeout configuration type."

    class OracleData:
        """Oracle data complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type OracleTable = Mapping[str, str | Sequence[str] | t.ContainerValue]
        "Oracle table type."
        type OracleSchema = Mapping[str, str | Sequence[Mapping[str, t.ContainerValue]]]
        "Oracle schema type."
        type OracleColumn = Mapping[str, str | int | bool | t.ContainerValue]
        "Oracle column type."
        type OracleQuery = Mapping[str, str | Sequence[str] | int | t.ContainerValue]
        "Oracle query type."
        type OracleIndex = Mapping[str, str | Sequence[str] | t.ContainerValue]
        "Oracle index type."
        type OracleConstraint = Mapping[
            str, str | bool | Sequence[str] | t.ContainerValue
        ]
        "Oracle constraint type."

    class DbtTransformation:
        """DBT Oracle transformation complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type TransformationConfig = Mapping[str, t.ContainerValue]
        "DBT transformation configuration type."
        type SqlTransformation = Mapping[str, str | t.ContainerValue]
        "SQL transformation type."
        type DataValidation = Mapping[
            str, bool | str | Sequence[str] | t.ContainerValue
        ]
        "Data validation type."
        type MaterializationConfig = Mapping[str, str | t.ContainerValue]
        "Materialization configuration type."
        type OutputFormat = Mapping[str, str | t.ContainerValue]
        "Output format type."
        type ProcessingStep = Mapping[str, str | int | t.ContainerValue]
        "Processing step type."

    class DbtModel:
        """DBT Oracle model complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ModelDefinition = Mapping[str, str | t.ContainerValue]
        "DBT model definition type."
        type ModelExecution = Mapping[str, str | bool | int | t.ContainerValue]
        "DBT model execution type."
        type ModelDependency = Mapping[str, str | Sequence[str] | t.ContainerValue]
        "DBT model dependency type."
        type ModelTest = Mapping[str, str | bool | t.ContainerValue]
        "DBT model test type."
        type ModelDocumentation = Mapping[str, str | t.ContainerValue]
        "DBT model documentation type."
        type ModelMaterialization = Mapping[str, str | t.ContainerValue]
        "DBT model materialization type."

    class DbtSource:
        """DBT Oracle source complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type SourceDefinition = Mapping[str, str | t.ContainerValue]
        "DBT source definition type."
        type SourceConnection = Mapping[str, t.ContainerValue]
        "DBT source connection type."
        type SourceTable = Mapping[str, str | Sequence[Mapping[str, t.ContainerValue]]]
        "DBT source table type."
        type SourceFreshness = Mapping[str, str | int | t.ContainerValue]
        "DBT source freshness type."
        type SourceTest = Mapping[str, str | bool | Sequence[str]]
        "DBT source test type."
        type SourceSchema = Mapping[str, str | t.ContainerValue]
        "DBT source schema type."

    class OracleAdapter:
        """Oracle adapter complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type AdapterConfiguration = Mapping[str, t.ContainerValue]
        "Oracle adapter configuration type."
        type ConnectionAdapter = Mapping[str, str | int | bool | t.ContainerValue]
        "Oracle connection adapter type."
        type QueryAdapter = Mapping[str, str | t.ContainerValue]
        "Oracle query adapter type."
        type SchemaAdapter = Mapping[str, str | Sequence[str] | t.ContainerValue]
        "Oracle schema adapter type."
        type TransactionAdapter = Mapping[str, bool | str | t.ContainerValue]
        "Oracle transaction adapter type."
        type CursorAdapter = Mapping[str, str | int | t.ContainerValue]
        "Oracle cursor adapter type."

    class Project:
        """DBT Oracle-specific project types.

        Adds DBT Oracle transformation-specific project types.
        Follows domain separation principle:
        DBT Oracle domain owns Oracle data transformation-specific types.
        """

        type DbtOracleProjectType = t.NormalizedValue
        "DBT Oracle project type literal."
        type DbtOracleProjectConfig = Mapping[str, t.ContainerValue]
        "DBT Oracle project configuration type."
        type OracleTransformConfig = Mapping[str, str | int | bool | Sequence[str]]
        "Oracle transformation configuration type."
        type OracleAnalyticsConfig = Mapping[str, bool | str | t.ContainerValue]
        "Oracle analytics configuration type."
        type DbtOraclePipelineConfig = Mapping[str, t.ContainerValue]
        "DBT Oracle pipeline configuration type."


t = FlextDbtOracleTypes
__all__ = [
    "ColumnSpec",
    "FlextDbtOracleTypes",
    "OraclePayload",
    "OraclePayloadList",
    "t",
]
