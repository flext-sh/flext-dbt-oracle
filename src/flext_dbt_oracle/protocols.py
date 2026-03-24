"""DBT Oracle protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_db_oracle.protocols import FlextDbOracleProtocols
from flext_meltano import FlextMeltanoProtocols

from flext_dbt_oracle import t


class FlextDbtOracleProtocols(FlextMeltanoProtocols, FlextDbOracleProtocols):
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
    connection: p.Database.Connection

    # Meltano protocols (inherited)
    dbt: p.Meltano.Dbt

    # DBT Oracle-specific protocols
    dbt_protocol: p.DbtOracle.Dbt
    """

    class DbtOracle:
        """DBT Oracle domain protocols for Oracle database transformation and analytics."""

        @runtime_checkable
        class Dbt(FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload], Protocol):
            """Protocol for DBT operations with Oracle data."""

            def compile_dbt_models(
                self,
                models: t.ScalarList | None = None,
                config: t.DbtOracle.OraclePayload | None = None,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Compile DBT models for Oracle data processing.

                Args:
                models: Specific models to compile, or None for all models
                config: DBT compilation configuration

                Returns:
                r[t.DbtOracle.OraclePayload]: DBT compilation results or error

                """
                ...

            def get_dbt_manifest(
                self,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Get DBT manifest with Oracle model definitions.

                Returns:
                r[t.DbtOracle.OraclePayload]: DBT manifest or error

                """
                ...

            def run_dbt_models(
                self,
                models: t.ScalarList | None = None,
                config: t.DbtOracle.OraclePayload | None = None,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Run DBT models with Oracle data sources.

                Args:
                models: Specific models to run, or None for all models
                config: DBT configuration parameters

                Returns:
                r[t.DbtOracle.OraclePayload]: DBT run results or error

                """
                ...

            def test_dbt_models(
                self,
                models: t.ScalarList | None = None,
                config: t.DbtOracle.OraclePayload | None = None,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Test DBT models with Oracle data validation.

                Args:
                models: Specific models to test, or None for all models
                config: DBT test configuration

                Returns:
                r[t.DbtOracle.OraclePayload]: DBT test results or error

                """
                ...

            def validate_dbt_project(
                self,
                project_path: str,
            ) -> FlextMeltanoProtocols.Result[bool]:
                """Validate DBT project configuration for Oracle integration.

                Args:
                project_path: Path to DBT project directory

                Returns:
                r[bool]: Validation status or error

                """
                ...

        @runtime_checkable
        class OracleIntegration(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload],
            Protocol,
        ):
            """Protocol for Oracle database integration operations."""

            def extract_oracle_data(
                self,
                oracle_config: t.DbtOracle.OraclePayload,
                extraction_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Extract data from Oracle database for DBT processing.

                Args:
                oracle_config: Oracle connection configuration
                extraction_config: Data extraction parameters

                Returns:
                r[t.DbtOracle.OraclePayloadList]: Extracted Oracle data or error

                """
                ...

            def sync_oracle_to_warehouse(
                self,
                oracle_data: t.DbtOracle.OraclePayloadList,
                warehouse_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Sync Oracle data to data warehouse for DBT processing.

                Args:
                oracle_data: Oracle data to sync
                warehouse_config: Data warehouse configuration

                Returns:
                r[t.DbtOracle.OraclePayload]: Sync operation results or error

                """
                ...

            def transform_oracle_to_dbt_format(
                self,
                oracle_data: t.DbtOracle.OraclePayloadList,
                transformation_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Transform Oracle data to DBT-compatible format.

                Args:
                oracle_data: Raw Oracle data
                transformation_config: Transformation parameters

                Returns:
                r[t.DbtOracle.OraclePayloadList]: Transformed data or error

                """
                ...

            def validate_oracle_data_quality(
                self,
                data: t.DbtOracle.OraclePayloadList,
                quality_rules: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Validate Oracle data quality for DBT processing.

                Args:
                data: Oracle data to validate
                quality_rules: Data quality validation rules

                Returns:
                r[t.DbtOracle.OraclePayload]: Quality validation results or error

                """
                ...

        @runtime_checkable
        class Modeling(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload], Protocol,
        ):
            """Protocol for Oracle data modeling operations."""

            def create_performance_models(
                self,
                oracle_performance_data: t.DbtOracle.OraclePayloadList,
                modeling_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Create performance models from Oracle performance data.

                Args:
                oracle_performance_data: Oracle performance metrics
                modeling_config: Performance modeling configuration

                Returns:
                r[t.DbtOracle.OraclePayload]: Performance models or error

                """
                ...

            def create_schema_dimension(
                self,
                oracle_schemas: t.DbtOracle.OraclePayloadList,
                dimension_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Create schema dimension model from Oracle schema data.

                Args:
                oracle_schemas: Oracle schema data
                dimension_config: Dimension modeling configuration

                Returns:
                r[t.DbtOracle.OraclePayload]: Schema dimension model or error

                """
                ...

            def create_table_dimension(
                self,
                oracle_tables: t.DbtOracle.OraclePayloadList,
                dimension_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Create table dimension model from Oracle table data.

                Args:
                oracle_tables: Oracle table data
                dimension_config: Dimension modeling configuration

                Returns:
                r[t.DbtOracle.OraclePayload]: Table dimension model or error

                """
                ...

            def generate_fact_tables(
                self,
                dimensions: t.DbtOracle.OraclePayloadList,
                fact_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Generate fact tables from Oracle dimensions.

                Args:
                dimensions: Oracle dimension models
                fact_config: Fact table configuration

                Returns:
                r[t.DbtOracle.OraclePayloadList]: Generated fact tables or error

                """
                ...

        @runtime_checkable
        class Transformation(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload], Protocol,
        ):
            """Protocol for Oracle data transformation operations."""

            def apply_business_rules(
                self,
                data: t.DbtOracle.OraclePayloadList,
                business_rules: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Apply business rules to Oracle data transformations.

                Args:
                data: Oracle data to transform
                business_rules: Business transformation rules

                Returns:
                r[t.DbtOracle.OraclePayloadList]: Transformed data or error

                """
                ...

            def apply_oracle_specific_transformations(
                self,
                oracle_data: t.DbtOracle.OraclePayloadList,
                transformation_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Apply Oracle-specific data transformations.

                Args:
                oracle_data: Oracle data to transform
                transformation_config: Oracle transformation configuration

                Returns:
                r[t.DbtOracle.OraclePayloadList]: Transformed data or error

                """
                ...

            def normalize_oracle_data_types(
                self,
                oracle_data: t.DbtOracle.OraclePayloadList,
                normalization_rules: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Normalize Oracle data types for consistent DBT processing.

                Args:
                oracle_data: Raw Oracle data
                normalization_rules: Data type normalization rules

                Returns:
                r[t.DbtOracle.OraclePayloadList]: Normalized Oracle data or error

                """
                ...

            def optimize_oracle_queries(
                self,
                query_config: t.DbtOracle.OraclePayload,
                optimization_rules: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Optimize Oracle queries for DBT processing.

                Args:
                query_config: Oracle query configuration
                optimization_rules: Query optimization rules

                Returns:
                r[t.DbtOracle.OraclePayload]: Optimized query configuration or error

                """
                ...

        @runtime_checkable
        class Macro(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload], Protocol,
        ):
            """Protocol for DBT macro operations with Oracle data."""

            def create_oracle_snapshot_macro(
                self,
                snapshot_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[str]:
                """Create DBT snapshot macro for Oracle data versioning.

                Args:
                snapshot_config: Oracle snapshot configuration

                Returns:
                r[str]: Generated snapshot macro or error

                """
                ...

            def create_oracle_test_macro(
                self,
                test_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[str]:
                """Create DBT test macro for Oracle data validation.

                Args:
                test_config: Oracle test configuration

                Returns:
                r[str]: Generated test macro or error

                """
                ...

            def generate_oracle_source_macro(
                self,
                source_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[str]:
                """Generate DBT macro for Oracle data sources.

                Args:
                source_config: Oracle source configuration

                Returns:
                r[str]: Generated DBT macro or error

                """
                ...

            def generate_oracle_transformation_macro(
                self,
                transformation_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[str]:
                """Generate DBT transformation macro for Oracle data.

                Args:
                transformation_config: Oracle transformation configuration

                Returns:
                r[str]: Generated transformation macro or error

                """
                ...

        @runtime_checkable
        class Quality(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload], Protocol,
        ):
            """Protocol for Oracle data quality operations."""

            def check_data_completeness(
                self,
                data: t.DbtOracle.OraclePayloadList,
                completeness_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Check Oracle data completeness for DBT processing.

                Args:
                data: Oracle data to check
                completeness_config: Completeness validation configuration

                Returns:
                r[t.DbtOracle.OraclePayload]: Completeness check results or error

                """
                ...

            def detect_data_anomalies(
                self,
                data: t.DbtOracle.OraclePayloadList,
                anomaly_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Detect anomalies in Oracle data for quality assurance.

                Args:
                data: Oracle data to analyze
                anomaly_config: Anomaly detection configuration

                Returns:
                r[t.DbtOracle.OraclePayloadList]: Detected anomalies or error

                """
                ...

            def generate_quality_report(
                self,
                quality_results: t.DbtOracle.OraclePayloadList,
                report_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Generate data quality report for Oracle DBT processing.

                Args:
                quality_results: Quality validation results
                report_config: Report generation configuration

                Returns:
                r[t.DbtOracle.OraclePayload]: Quality report or error

                """
                ...

            def validate_oracle_schema_compliance(
                self,
                oracle_data: t.DbtOracle.OraclePayloadList,
                schema_rules: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Validate Oracle data against schema compliance rules.

                Args:
                oracle_data: Oracle data to validate
                schema_rules: Schema compliance rules

                Returns:
                r[t.DbtOracle.OraclePayload]: Schema validation results or error

                """
                ...

        @runtime_checkable
        class Performance(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload], Protocol,
        ):
            """Protocol for DBT Oracle performance optimization operations."""

            def monitor_dbt_performance(
                self,
                run_results: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Monitor DBT performance with Oracle data processing.

                Args:
                run_results: DBT run results

                Returns:
                r[t.DbtOracle.OraclePayload]: Performance metrics or error

                """
                ...

            def optimize_dbt_models(
                self,
                model_config: t.DbtOracle.OraclePayload,
                performance_metrics: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Optimize DBT models for Oracle data processing performance.

                Args:
                model_config: DBT model configuration
                performance_metrics: Current performance metrics

                Returns:
                r[t.DbtOracle.OraclePayload]: Optimization recommendations or error

                """
                ...

            def optimize_oracle_query_performance(
                self,
                query_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Optimize Oracle queries for DBT data processing.

                Args:
                query_config: Oracle query configuration

                Returns:
                r[t.DbtOracle.OraclePayload]: Query optimization results or error

                """
                ...

            def tune_oracle_connections(
                self,
                connection_config: t.DbtOracle.OraclePayload,
                tuning_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Tune Oracle connections for improved DBT performance.

                Args:
                connection_config: Oracle connection configuration
                tuning_config: Connection tuning parameters

                Returns:
                r[t.DbtOracle.OraclePayload]: Tuned connection configuration or error

                """
                ...

        @runtime_checkable
        class Monitoring(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload], Protocol,
        ):
            """Protocol for DBT Oracle monitoring operations."""

            def create_monitoring_dashboard(
                self,
                dashboard_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Create monitoring dashboard for DBT Oracle operations.

                Args:
                dashboard_config: Dashboard configuration

                Returns:
                r[t.DbtOracle.OraclePayload]: Dashboard creation result or error

                """
                ...

            def get_health_status(
                self,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Get DBT Oracle integration health status.

                Returns:
                r[t.DbtOracle.OraclePayload]: Health status or error

                """
                ...

            def monitor_oracle_data_freshness(
                self,
                freshness_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Monitor Oracle data freshness for DBT processing.

                Args:
                freshness_config: Data freshness monitoring configuration

                Returns:
                r[t.DbtOracle.OraclePayload]: Data freshness status or error

                """
                ...

            def track_dbt_run_metrics(
                self,
                run_id: str,
                metrics: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[bool]:
                """Track DBT run metrics for Oracle data processing.

                Args:
                run_id: DBT run identifier
                metrics: Run metrics data

                Returns:
                r[bool]: Metric tracking success status

                """
                ...


__all__ = ["FlextDbtOracleProtocols", "p"]

p = FlextDbtOracleProtocols
