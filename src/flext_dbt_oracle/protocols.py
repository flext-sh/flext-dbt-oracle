"""DBT Oracle protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_core.typings import t
from flext_db_oracle.protocols import FlextDbOracleProtocols as p_db_oracle
from flext_meltano.protocols import FlextMeltanoProtocols as p_meltano


class FlextDbtOracleProtocols(p_meltano, p_db_oracle):
    """DBT Oracle protocols extending Oracle and Meltano protocols.

    Extends both FlextDbOracleProtocols and FlextMeltanoProtocols via multiple inheritance
    to inherit all Oracle protocols, Meltano protocols, and foundation protocols.

    Architecture:
    - EXTENDS: FlextDbOracleProtocols (inherits .Database.* protocols)
    - EXTENDS: FlextMeltanoProtocols (inherits .Meltano.* protocols)
    - ADDS: DBT Oracle-specific protocols in Dbt.Oracle namespace
    - PROVIDES: Root-level alias `p` for convenient access

    Usage:
    from flext_dbt_oracle.protocols import p

    # Foundation protocols (inherited)
    result: p.Result[str]
    service: p.Service[str]

    # Oracle protocols (inherited)
    connection: p.Database.ConnectionProtocol

    # Meltano protocols (inherited)
    dbt: p.Meltano.DbtProtocol

    # DBT Oracle-specific protocols
    dbt_protocol: p.DbtOracle.DbtProtocol
    """

    class DbtOracle:
        """DBT Oracle domain protocols for Oracle database transformation and analytics."""

        @runtime_checkable
        class DbtProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for DBT operations with Oracle data."""

            def run_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, t.GeneralValueType] | None = None,
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Run DBT models with Oracle data sources.

                Args:
                models: Specific models to run, or None for all models
                config: DBT configuration parameters

                Returns:
                r[dict[str, t.GeneralValueType]]: DBT run results or error

                """
                ...

            def test_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, t.GeneralValueType] | None = None,
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Test DBT models with Oracle data validation.

                Args:
                models: Specific models to test, or None for all models
                config: DBT test configuration

                Returns:
                r[dict[str, t.GeneralValueType]]: DBT test results or error

                """
                ...

            def compile_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, t.GeneralValueType] | None = None,
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Compile DBT models for Oracle data processing.

                Args:
                models: Specific models to compile, or None for all models
                config: DBT compilation configuration

                Returns:
                r[dict[str, t.GeneralValueType]]: DBT compilation results or error

                """
                ...

            def get_dbt_manifest(
                self,
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Get DBT manifest with Oracle model definitions.

                Returns:
                r[dict[str, t.GeneralValueType]]: DBT manifest or error

                """
                ...

            def validate_dbt_project(self, project_path: str) -> p_meltano.Result[bool]:
                """Validate DBT project configuration for Oracle integration.

                Args:
                project_path: Path to DBT project directory

                Returns:
                r[bool]: Validation status or error

                """
                ...

        @runtime_checkable
        class OracleIntegrationProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for Oracle database integration operations."""

            def extract_oracle_data(
                self,
                oracle_config: dict[str, t.GeneralValueType],
                extraction_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[list[dict[str, t.GeneralValueType]]]:
                """Extract data from Oracle database for DBT processing.

                Args:
                oracle_config: Oracle connection configuration
                extraction_config: Data extraction parameters

                Returns:
                r[list[dict[str, t.GeneralValueType]]]: Extracted Oracle data or error

                """
                ...

            def transform_oracle_to_dbt_format(
                self,
                oracle_data: list[dict[str, t.GeneralValueType]],
                transformation_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[list[dict[str, t.GeneralValueType]]]:
                """Transform Oracle data to DBT-compatible format.

                Args:
                oracle_data: Raw Oracle data
                transformation_config: Transformation parameters

                Returns:
                r[list[dict[str, t.GeneralValueType]]]: Transformed data or error

                """
                ...

            def validate_oracle_data_quality(
                self,
                data: list[dict[str, t.GeneralValueType]],
                quality_rules: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Validate Oracle data quality for DBT processing.

                Args:
                data: Oracle data to validate
                quality_rules: Data quality validation rules

                Returns:
                r[dict[str, t.GeneralValueType]]: Quality validation results or error

                """
                ...

            def sync_oracle_to_warehouse(
                self,
                oracle_data: list[dict[str, t.GeneralValueType]],
                warehouse_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Sync Oracle data to data warehouse for DBT processing.

                Args:
                oracle_data: Oracle data to sync
                warehouse_config: Data warehouse configuration

                Returns:
                r[dict[str, t.GeneralValueType]]: Sync operation results or error

                """
                ...

        @runtime_checkable
        class ModelingProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for Oracle data modeling operations."""

            def create_table_dimension(
                self,
                oracle_tables: list[dict[str, t.GeneralValueType]],
                dimension_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Create table dimension model from Oracle table data.

                Args:
                oracle_tables: Oracle table data
                dimension_config: Dimension modeling configuration

                Returns:
                r[dict[str, t.GeneralValueType]]: Table dimension model or error

                """
                ...

            def create_schema_dimension(
                self,
                oracle_schemas: list[dict[str, t.GeneralValueType]],
                dimension_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Create schema dimension model from Oracle schema data.

                Args:
                oracle_schemas: Oracle schema data
                dimension_config: Dimension modeling configuration

                Returns:
                r[dict[str, t.GeneralValueType]]: Schema dimension model or error

                """
                ...

            def create_performance_models(
                self,
                oracle_performance_data: list[dict[str, t.GeneralValueType]],
                modeling_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Create performance models from Oracle performance data.

                Args:
                oracle_performance_data: Oracle performance metrics
                modeling_config: Performance modeling configuration

                Returns:
                r[dict[str, t.GeneralValueType]]: Performance models or error

                """
                ...

            def generate_fact_tables(
                self,
                dimensions: list[dict[str, t.GeneralValueType]],
                fact_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[list[dict[str, t.GeneralValueType]]]:
                """Generate fact tables from Oracle dimensions.

                Args:
                dimensions: Oracle dimension models
                fact_config: Fact table configuration

                Returns:
                r[list[dict[str, t.GeneralValueType]]]: Generated fact tables or error

                """
                ...

        @runtime_checkable
        class TransformationProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for Oracle data transformation operations."""

            def normalize_oracle_data_types(
                self,
                oracle_data: list[dict[str, t.GeneralValueType]],
                normalization_rules: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[list[dict[str, t.GeneralValueType]]]:
                """Normalize Oracle data types for consistent DBT processing.

                Args:
                oracle_data: Raw Oracle data
                normalization_rules: Data type normalization rules

                Returns:
                r[list[dict[str, t.GeneralValueType]]]: Normalized Oracle data or error

                """
                ...

            def apply_oracle_specific_transformations(
                self,
                oracle_data: list[dict[str, t.GeneralValueType]],
                transformation_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[list[dict[str, t.GeneralValueType]]]:
                """Apply Oracle-specific data transformations.

                Args:
                oracle_data: Oracle data to transform
                transformation_config: Oracle transformation configuration

                Returns:
                r[list[dict[str, t.GeneralValueType]]]: Transformed data or error

                """
                ...

            def apply_business_rules(
                self,
                data: list[dict[str, t.GeneralValueType]],
                business_rules: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[list[dict[str, t.GeneralValueType]]]:
                """Apply business rules to Oracle data transformations.

                Args:
                data: Oracle data to transform
                business_rules: Business transformation rules

                Returns:
                r[list[dict[str, t.GeneralValueType]]]: Transformed data or error

                """
                ...

            def optimize_oracle_queries(
                self,
                query_config: dict[str, t.GeneralValueType],
                optimization_rules: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Optimize Oracle queries for DBT processing.

                Args:
                query_config: Oracle query configuration
                optimization_rules: Query optimization rules

                Returns:
                r[dict[str, t.GeneralValueType]]: Optimized query configuration or error

                """
                ...

        @runtime_checkable
        class MacroProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for DBT macro operations with Oracle data."""

            def generate_oracle_source_macro(
                self,
                source_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[str]:
                """Generate DBT macro for Oracle data sources.

                Args:
                source_config: Oracle source configuration

                Returns:
                r[str]: Generated DBT macro or error

                """
                ...

            def create_oracle_test_macro(
                self,
                test_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[str]:
                """Create DBT test macro for Oracle data validation.

                Args:
                test_config: Oracle test configuration

                Returns:
                r[str]: Generated test macro or error

                """
                ...

            def generate_oracle_transformation_macro(
                self,
                transformation_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[str]:
                """Generate DBT transformation macro for Oracle data.

                Args:
                transformation_config: Oracle transformation configuration

                Returns:
                r[str]: Generated transformation macro or error

                """
                ...

            def create_oracle_snapshot_macro(
                self,
                snapshot_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[str]:
                """Create DBT snapshot macro for Oracle data versioning.

                Args:
                snapshot_config: Oracle snapshot configuration

                Returns:
                r[str]: Generated snapshot macro or error

                """
                ...

        @runtime_checkable
        class QualityProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for Oracle data quality operations."""

            def validate_oracle_schema_compliance(
                self,
                oracle_data: list[dict[str, t.GeneralValueType]],
                schema_rules: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Validate Oracle data against schema compliance rules.

                Args:
                oracle_data: Oracle data to validate
                schema_rules: Schema compliance rules

                Returns:
                r[dict[str, t.GeneralValueType]]: Schema validation results or error

                """
                ...

            def check_data_completeness(
                self,
                data: list[dict[str, t.GeneralValueType]],
                completeness_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Check Oracle data completeness for DBT processing.

                Args:
                data: Oracle data to check
                completeness_config: Completeness validation configuration

                Returns:
                r[dict[str, t.GeneralValueType]]: Completeness check results or error

                """
                ...

            def detect_data_anomalies(
                self,
                data: list[dict[str, t.GeneralValueType]],
                anomaly_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[list[dict[str, t.GeneralValueType]]]:
                """Detect anomalies in Oracle data for quality assurance.

                Args:
                data: Oracle data to analyze
                anomaly_config: Anomaly detection configuration

                Returns:
                r[list[dict[str, t.GeneralValueType]]]: Detected anomalies or error

                """
                ...

            def generate_quality_report(
                self,
                quality_results: list[dict[str, t.GeneralValueType]],
                report_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Generate data quality report for Oracle DBT processing.

                Args:
                quality_results: Quality validation results
                report_config: Report generation configuration

                Returns:
                r[dict[str, t.GeneralValueType]]: Quality report or error

                """
                ...

        @runtime_checkable
        class PerformanceProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for DBT Oracle performance optimization operations."""

            def optimize_dbt_models(
                self,
                model_config: dict[str, t.GeneralValueType],
                performance_metrics: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Optimize DBT models for Oracle data processing performance.

                Args:
                model_config: DBT model configuration
                performance_metrics: Current performance metrics

                Returns:
                r[dict[str, t.GeneralValueType]]: Optimization recommendations or error

                """
                ...

            def tune_oracle_connections(
                self,
                connection_config: dict[str, t.GeneralValueType],
                tuning_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Tune Oracle connections for improved DBT performance.

                Args:
                connection_config: Oracle connection configuration
                tuning_config: Connection tuning parameters

                Returns:
                r[dict[str, t.GeneralValueType]]: Tuned connection configuration or error

                """
                ...

            def monitor_dbt_performance(
                self,
                run_results: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Monitor DBT performance with Oracle data processing.

                Args:
                run_results: DBT run results

                Returns:
                r[dict[str, t.GeneralValueType]]: Performance metrics or error

                """
                ...

            def optimize_oracle_query_performance(
                self,
                query_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Optimize Oracle queries for DBT data processing.

                Args:
                query_config: Oracle query configuration

                Returns:
                r[dict[str, t.GeneralValueType]]: Query optimization results or error

                """
                ...

        @runtime_checkable
        class MonitoringProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for DBT Oracle monitoring operations."""

            def track_dbt_run_metrics(
                self,
                run_id: str,
                metrics: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[bool]:
                """Track DBT run metrics for Oracle data processing.

                Args:
                run_id: DBT run identifier
                metrics: Run metrics data

                Returns:
                r[bool]: Metric tracking success status

                """
                ...

            def monitor_oracle_data_freshness(
                self,
                freshness_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Monitor Oracle data freshness for DBT processing.

                Args:
                freshness_config: Data freshness monitoring configuration

                Returns:
                r[dict[str, t.GeneralValueType]]: Data freshness status or error

                """
                ...

            def get_health_status(
                self,
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Get DBT Oracle integration health status.

                Returns:
                r[dict[str, t.GeneralValueType]]: Health status or error

                """
                ...

            def create_monitoring_dashboard(
                self,
                dashboard_config: dict[str, t.GeneralValueType],
            ) -> p_meltano.Result[dict[str, t.GeneralValueType]]:
                """Create monitoring dashboard for DBT Oracle operations.

                Args:
                dashboard_config: Dashboard configuration

                Returns:
                r[dict[str, t.GeneralValueType]]: Dashboard creation result or error

                """
                ...


# Runtime alias for simplified usage
p = FlextDbtOracleProtocols

__all__ = [
    "FlextDbtOracleProtocols",
    "p",
]
