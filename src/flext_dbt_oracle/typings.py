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

from flext_core import FlextTypes
from flext_db_oracle import FlextDbOracleTypes
from flext_meltano import FlextMeltanoTypes


class FlextDbtOracleTypes(FlextMeltanoTypes, FlextDbOracleTypes):
    """DBT Oracle-specific type definitions extending t.

    Domain-specific type system for DBT Oracle data transformation operations.
    Contains ONLY complex DBT Oracle-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class DbtOracle:
        """DBT Oracle project complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ProjectConfiguration = dict[
            str, FlextTypes.JsonValue | dict[str, FlextTypes.JsonValue]
        ]
        "DBT project configuration type."
        type ModelConfiguration = dict[str, str | dict[str, FlextTypes.JsonValue]]
        "DBT model configuration type."
        type SourceConfiguration = dict[
            str, str | list[dict[str, FlextTypes.JsonValue]]
        ]
        "DBT source configuration type."
        type ProfileConfiguration = dict[str, FlextTypes.JsonValue]
        "DBT profile configuration type."
        type MacroConfiguration = dict[str, str | dict[str, FlextTypes.JsonValue]]
        "DBT macro configuration type."
        type TestConfiguration = dict[str, str | bool | list[str]]
        "DBT test configuration type."

    class OracleConnection:
        """Oracle connection complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ConnectionConfig = dict[
            str, str | int | bool | dict[str, FlextTypes.ContainerValue]
        ]
        "Oracle connection configuration type."
        type DatabaseConnection = dict[str, str | dict[str, FlextTypes.JsonValue]]
        "Oracle database connection type."
        type PoolingConfig = dict[
            str, int | bool | dict[str, FlextTypes.ContainerValue]
        ]
        "Oracle pooling configuration type."
        type SecurityConfig = dict[
            str, bool | str | dict[str, FlextTypes.ContainerValue]
        ]
        "Oracle security configuration type."
        type SessionConfig = dict[str, str | int | dict[str, FlextTypes.ContainerValue]]
        "Oracle session configuration type."
        type TimeoutConfig = dict[str, int | float]
        "Oracle timeout configuration type."

    class OracleData:
        """Oracle data complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type OracleTable = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        "Oracle table type."
        type OracleSchema = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        "Oracle schema type."
        type OracleColumn = dict[
            str, str | int | bool | dict[str, FlextTypes.ContainerValue]
        ]
        "Oracle column type."
        type OracleQuery = dict[
            str, str | list[str] | int | dict[str, FlextTypes.ContainerValue]
        ]
        "Oracle query type."
        type OracleIndex = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        "Oracle index type."
        type OracleConstraint = dict[
            str, str | bool | list[str] | dict[str, FlextTypes.ContainerValue]
        ]
        "Oracle constraint type."

    class DbtTransformation:
        """DBT Oracle transformation complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type TransformationConfig = dict[
            str, FlextTypes.JsonValue | dict[str, FlextTypes.ContainerValue]
        ]
        "DBT transformation configuration type."
        type SqlTransformation = dict[str, str | dict[str, FlextTypes.JsonValue]]
        "SQL transformation type."
        type DataValidation = dict[
            str, bool | str | list[str] | dict[str, FlextTypes.ContainerValue]
        ]
        "Data validation type."
        type MaterializationConfig = dict[str, str | dict[str, FlextTypes.JsonValue]]
        "Materialization configuration type."
        type OutputFormat = dict[str, str | dict[str, FlextTypes.ContainerValue]]
        "Output format type."
        type ProcessingStep = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        "Processing step type."

    class DbtModel:
        """DBT Oracle model complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ModelDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        "DBT model definition type."
        type ModelExecution = dict[
            str, str | bool | int | dict[str, FlextTypes.ContainerValue]
        ]
        "DBT model execution type."
        type ModelDependency = dict[
            str, str | list[str] | dict[str, FlextTypes.ContainerValue]
        ]
        "DBT model dependency type."
        type ModelTest = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        "DBT model test type."
        type ModelDocumentation = dict[str, str | dict[str, FlextTypes.ContainerValue]]
        "DBT model documentation type."
        type ModelMaterialization = dict[
            str, str | dict[str, FlextTypes.ContainerValue]
        ]
        "DBT model materialization type."

    class DbtSource:
        """DBT Oracle source complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type SourceDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        "DBT source definition type."
        type SourceConnection = dict[
            str, FlextTypes.ContainerValue | dict[str, FlextTypes.ContainerValue]
        ]
        "DBT source connection type."
        type SourceTable = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        "DBT source table type."
        type SourceFreshness = dict[
            str, str | int | dict[str, FlextTypes.ContainerValue]
        ]
        "DBT source freshness type."
        type SourceTest = dict[str, str | bool | list[str]]
        "DBT source test type."
        type SourceSchema = dict[str, str | dict[str, FlextTypes.JsonValue]]
        "DBT source schema type."

    class OracleAdapter:
        """Oracle adapter complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type AdapterConfiguration = dict[
            str, FlextTypes.ContainerValue | dict[str, FlextTypes.ContainerValue]
        ]
        "Oracle adapter configuration type."
        type ConnectionAdapter = dict[
            str, str | int | bool | dict[str, FlextTypes.ContainerValue]
        ]
        "Oracle connection adapter type."
        type QueryAdapter = dict[str, str | dict[str, FlextTypes.JsonValue]]
        "Oracle query adapter type."
        type SchemaAdapter = dict[
            str, str | list[str] | dict[str, FlextTypes.ContainerValue]
        ]
        "Oracle schema adapter type."
        type TransactionAdapter = dict[
            str, bool | str | dict[str, FlextTypes.JsonValue]
        ]
        "Oracle transaction adapter type."
        type CursorAdapter = dict[str, str | int | dict[str, FlextTypes.ContainerValue]]
        "Oracle cursor adapter type."

    class Project(FlextDbOracleTypes.Project):
        """DBT Oracle-specific project types.

        Adds DBT Oracle transformation-specific project types.
        Follows domain separation principle:
        DBT Oracle domain owns Oracle data transformation-specific types.
        """

        type DbtOracleProjectType = Literal[
            "library",
            "application",
            "service",
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
        "DBT Oracle project type literal."
        type DbtOracleProjectConfig = dict[str, FlextTypes.ContainerValue]
        "DBT Oracle project configuration type."
        type OracleTransformConfig = dict[str, str | int | bool | list[str]]
        "Oracle transformation configuration type."
        type OracleAnalyticsConfig = dict[
            str, bool | str | dict[str, FlextTypes.ContainerValue]
        ]
        "Oracle analytics configuration type."
        type DbtOraclePipelineConfig = dict[str, FlextTypes.ContainerValue]
        "DBT Oracle pipeline configuration type."


t = FlextDbtOracleTypes
__all__ = ["FlextDbtOracleTypes", "t"]
