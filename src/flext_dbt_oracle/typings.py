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

        type ProjectConfiguration = dict[str, object | dict[str, object]]
        "DBT project configuration type."
        type ModelConfiguration = dict[str, str | dict[str, object]]
        "DBT model configuration type."
        type SourceConfiguration = dict[str, str | list[dict[str, object]]]
        "DBT source configuration type."
        type ProfileConfiguration = dict[str, object]
        "DBT profile configuration type."
        type MacroConfiguration = dict[str, str | dict[str, object]]
        "DBT macro configuration type."
        type TestConfiguration = dict[str, str | bool | list[str]]
        "DBT test configuration type."

    class OracleConnection:
        """Oracle connection complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ConnectionConfig = dict[str, str | int | bool | dict[str, object]]
        "Oracle connection configuration type."
        type DatabaseConnection = dict[str, str | dict[str, object]]
        "Oracle database connection type."
        type PoolingConfig = dict[str, int | bool | dict[str, object]]
        "Oracle pooling configuration type."
        type SecurityConfig = dict[str, bool | str | dict[str, object]]
        "Oracle security configuration type."
        type SessionConfig = dict[str, str | int | dict[str, object]]
        "Oracle session configuration type."
        type TimeoutConfig = dict[str, int | float]
        "Oracle timeout configuration type."

    class OracleData:
        """Oracle data complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type OracleTable = dict[str, str | list[str] | dict[str, object]]
        "Oracle table type."
        type OracleSchema = dict[str, str | list[dict[str, object]]]
        "Oracle schema type."
        type OracleColumn = dict[str, str | int | bool | dict[str, object]]
        "Oracle column type."
        type OracleQuery = dict[str, str | list[str] | int | dict[str, object]]
        "Oracle query type."
        type OracleIndex = dict[str, str | list[str] | dict[str, object]]
        "Oracle index type."
        type OracleConstraint = dict[str, str | bool | list[str] | dict[str, object]]
        "Oracle constraint type."

    class DbtTransformation:
        """DBT Oracle transformation complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type TransformationConfig = dict[str, object | dict[str, object]]
        "DBT transformation configuration type."
        type SqlTransformation = dict[str, str | dict[str, object]]
        "SQL transformation type."
        type DataValidation = dict[str, bool | str | list[str] | dict[str, object]]
        "Data validation type."
        type MaterializationConfig = dict[str, str | dict[str, object]]
        "Materialization configuration type."
        type OutputFormat = dict[str, str | dict[str, object]]
        "Output format type."
        type ProcessingStep = dict[str, str | int | dict[str, object]]
        "Processing step type."

    class DbtModel:
        """DBT Oracle model complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type ModelDefinition = dict[str, str | dict[str, object]]
        "DBT model definition type."
        type ModelExecution = dict[str, str | bool | int | dict[str, object]]
        "DBT model execution type."
        type ModelDependency = dict[str, str | list[str] | dict[str, object]]
        "DBT model dependency type."
        type ModelTest = dict[str, str | bool | dict[str, object]]
        "DBT model test type."
        type ModelDocumentation = dict[str, str | dict[str, object]]
        "DBT model documentation type."
        type ModelMaterialization = dict[str, str | dict[str, object]]
        "DBT model materialization type."

    class DbtSource:
        """DBT Oracle source complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type SourceDefinition = dict[str, str | dict[str, object]]
        "DBT source definition type."
        type SourceConnection = dict[str, object | dict[str, object]]
        "DBT source connection type."
        type SourceTable = dict[str, str | list[dict[str, object]]]
        "DBT source table type."
        type SourceFreshness = dict[str, str | int | dict[str, object]]
        "DBT source freshness type."
        type SourceTest = dict[str, str | bool | list[str]]
        "DBT source test type."
        type SourceSchema = dict[str, str | dict[str, object]]
        "DBT source schema type."

    class OracleAdapter:
        """Oracle adapter complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        type AdapterConfiguration = dict[str, object | dict[str, object]]
        "Oracle adapter configuration type."
        type ConnectionAdapter = dict[str, str | int | bool | dict[str, object]]
        "Oracle connection adapter type."
        type QueryAdapter = dict[str, str | dict[str, object]]
        "Oracle query adapter type."
        type SchemaAdapter = dict[str, str | list[str] | dict[str, object]]
        "Oracle schema adapter type."
        type TransactionAdapter = dict[str, bool | str | dict[str, object]]
        "Oracle transaction adapter type."
        type CursorAdapter = dict[str, str | int | dict[str, object]]
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
        type DbtOracleProjectConfig = dict[str, object]
        "DBT Oracle project configuration type."
        type OracleTransformConfig = dict[str, str | int | bool | list[str]]
        "Oracle transformation configuration type."
        type OracleAnalyticsConfig = dict[str, bool | str | dict[str, object]]
        "Oracle analytics configuration type."
        type DbtOraclePipelineConfig = dict[str, object]
        "DBT Oracle pipeline configuration type."


t = FlextDbtOracleTypes
__all__ = ["FlextDbtOracleTypes", "t"]


type ColumnSpec = dict[str, str]

type OraclePayload = t.Dict

type OraclePayloadList = list[t.Dict]
