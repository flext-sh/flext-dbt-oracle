"""FLEXT DBT Oracle Types - Domain-specific DBT Oracle type definitions."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_db_oracle import FlextDbOracleTypes
from flext_meltano import FlextMeltanoTypes


class FlextDbtOracleTypes(FlextMeltanoTypes, FlextDbOracleTypes):
    """DBT Oracle-specific type definitions extending t."""

    class DbtOracle:
        """DbtOracle domain namespace for all type definitions."""

        type ColumnSpec = FlextMeltanoTypes.StrMapping
        "Column specification type."
        type OraclePayload = Mapping[str, FlextMeltanoTypes.Primitives | None]
        "Oracle payload type."
        type OraclePayloadList = Sequence[OraclePayload]
        "List of Oracle payloads."

        type ProjectConfiguration = Mapping[str, FlextMeltanoTypes.ContainerValue]
        "DBT project configuration type."
        type ModelConfiguration = Mapping[str, str | FlextMeltanoTypes.ContainerValue]
        "DBT model configuration type."
        type SourceConfiguration = Mapping[
            str,
            str | Sequence[FlextMeltanoTypes.ContainerValueMapping],
        ]
        "DBT source configuration type."
        type ProfileConfiguration = Mapping[str, FlextMeltanoTypes.ContainerValue]
        "DBT profile configuration type."
        type MacroConfiguration = Mapping[str, str | FlextMeltanoTypes.ContainerValue]
        "DBT macro configuration type."
        type TestConfiguration = Mapping[str, str | bool | Sequence[str]]
        "DBT test configuration type."

        class OracleConnection:
            """Oracle connection complex types."""

            type ConnectionConfig = Mapping[
                str,
                FlextMeltanoTypes.Scalar | FlextMeltanoTypes.ContainerValue,
            ]
            type DatabaseConnection = Mapping[
                str, str | FlextMeltanoTypes.ContainerValue
            ]
            type PoolingConfig = Mapping[
                str, int | bool | FlextMeltanoTypes.ContainerValue
            ]
            type SecurityConfig = Mapping[
                str,
                bool | str | FlextMeltanoTypes.ContainerValue,
            ]
            type SessionConfig = Mapping[
                str, str | int | FlextMeltanoTypes.ContainerValue
            ]
            type TimeoutConfig = Mapping[str, int | float]

        class OracleData:
            """Oracle data complex types."""

            type OracleTable = Mapping[
                str,
                str | Sequence[str] | FlextMeltanoTypes.ContainerValue,
            ]
            type OracleSchema = Mapping[
                str,
                str | Sequence[FlextMeltanoTypes.ContainerValueMapping],
            ]
            type OracleColumn = Mapping[
                str,
                FlextMeltanoTypes.Scalar | FlextMeltanoTypes.ContainerValue,
            ]
            type OracleQuery = Mapping[
                str,
                str | Sequence[str] | int | FlextMeltanoTypes.ContainerValue,
            ]
            type OracleIndex = Mapping[
                str,
                str | Sequence[str] | FlextMeltanoTypes.ContainerValue,
            ]
            type OracleConstraint = Mapping[
                str,
                str | bool | Sequence[str] | FlextMeltanoTypes.ContainerValue,
            ]

        class DbtTransformation:
            """DBT Oracle transformation complex types."""

            type TransformationConfig = Mapping[str, FlextMeltanoTypes.ContainerValue]
            type SqlTransformation = Mapping[
                str, str | FlextMeltanoTypes.ContainerValue
            ]
            type DataValidation = Mapping[
                str,
                bool | str | Sequence[str] | FlextMeltanoTypes.ContainerValue,
            ]
            type MaterializationConfig = Mapping[
                str,
                str | FlextMeltanoTypes.ContainerValue,
            ]
            type OutputFormat = Mapping[str, str | FlextMeltanoTypes.ContainerValue]
            type ProcessingStep = Mapping[
                str, str | int | FlextMeltanoTypes.ContainerValue
            ]

        class DbtModel:
            """DBT Oracle model complex types."""

            type ModelDefinition = Mapping[str, str | FlextMeltanoTypes.ContainerValue]
            type ModelExecution = Mapping[
                str,
                str | bool | int | FlextMeltanoTypes.ContainerValue,
            ]
            type ModelDependency = Mapping[
                str,
                str | Sequence[str] | FlextMeltanoTypes.ContainerValue,
            ]
            type ModelTest = Mapping[str, str | bool | FlextMeltanoTypes.ContainerValue]
            type ModelDocumentation = Mapping[
                str, str | FlextMeltanoTypes.ContainerValue
            ]
            type ModelMaterialization = Mapping[
                str, str | FlextMeltanoTypes.ContainerValue
            ]

        class DbtSource:
            """DBT Oracle source complex types."""

            type SourceDefinition = Mapping[str, str | FlextMeltanoTypes.ContainerValue]
            type SourceConnection = Mapping[str, FlextMeltanoTypes.ContainerValue]
            type SourceTable = Mapping[
                str,
                str | Sequence[FlextMeltanoTypes.ContainerValueMapping],
            ]
            type SourceFreshness = Mapping[
                str,
                str | int | FlextMeltanoTypes.ContainerValue,
            ]
            type SourceTest = Mapping[str, str | bool | Sequence[str]]
            type SourceSchema = Mapping[str, str | FlextMeltanoTypes.ContainerValue]

        class OracleAdapter:
            """Oracle adapter complex types."""

            type AdapterConfiguration = Mapping[str, FlextMeltanoTypes.ContainerValue]
            type ConnectionAdapter = Mapping[
                str,
                FlextMeltanoTypes.Scalar | FlextMeltanoTypes.ContainerValue,
            ]
            type QueryAdapter = Mapping[str, str | FlextMeltanoTypes.ContainerValue]
            type SchemaAdapter = Mapping[
                str,
                str | Sequence[str] | FlextMeltanoTypes.ContainerValue,
            ]
            type TransactionAdapter = Mapping[
                str,
                bool | str | FlextMeltanoTypes.ContainerValue,
            ]
            type CursorAdapter = Mapping[
                str, str | int | FlextMeltanoTypes.ContainerValue
            ]

        class Project:
            """DBT Oracle-specific project types."""

            type DbtOracleProjectType = FlextMeltanoTypes.NormalizedValue
            type DbtOracleProjectConfig = Mapping[str, FlextMeltanoTypes.ContainerValue]
            type OracleTransformConfig = Mapping[
                str,
                FlextMeltanoTypes.Scalar | Sequence[str],
            ]
            type OracleAnalyticsConfig = Mapping[
                str,
                bool | str | FlextMeltanoTypes.ContainerValue,
            ]
            type DbtOraclePipelineConfig = Mapping[
                str, FlextMeltanoTypes.ContainerValue
            ]


t = FlextDbtOracleTypes
__all__ = [
    "FlextDbtOracleTypes",
    "t",
]
