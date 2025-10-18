"""DBT Oracle protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextResult


class FlextDbtOracleProtocols:
    """DBT Oracle protocols with explicit re-exports from FlextProtocols foundation.

    This class provides protocol definitions for DBT operations with Oracle database integration,
    data transformation, modeling, and enterprise Oracle analytics patterns.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in DbtOracle namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    # ============================================================================
    # DBT ORACLE-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class DbtOracle:
        """DBT Oracle domain protocols for Oracle database transformation and analytics."""

        @runtime_checkable
        class DbtProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT operations with Oracle data."""

            def run_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, object] | None = None,
            ) -> FlextResult[dict[str, object]]:
                """Run DBT models with Oracle data sources.

                Args:
                    models: Specific models to run, or None for all models
                    config: DBT configuration parameters

                Returns:
                    FlextResult[dict[str, object]]: DBT run results or error

                """

            def test_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, object] | None = None,
            ) -> FlextResult[dict[str, object]]:
                """Test DBT models with Oracle data validation.

                Args:
                    models: Specific models to test, or None for all models
                    config: DBT test configuration

                Returns:
                    FlextResult[dict[str, object]]: DBT test results or error

                """

            def compile_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, object] | None = None,
            ) -> FlextResult[dict[str, object]]:
                """Compile DBT models for Oracle data processing.

                Args:
                    models: Specific models to compile, or None for all models
                    config: DBT compilation configuration

                Returns:
                    FlextResult[dict[str, object]]: DBT compilation results or error

                """

            def get_dbt_manifest(self) -> FlextResult[dict[str, object]]:
                """Get DBT manifest with Oracle model definitions.

                Returns:
                    FlextResult[dict[str, object]]: DBT manifest or error

                """

            def validate_dbt_project(self, project_path: str) -> FlextResult[bool]:
                """Validate DBT project configuration for Oracle integration.

                Args:
                    project_path: Path to DBT project directory

                Returns:
                    FlextResult[bool]: Validation status or error

                """

        @runtime_checkable
        class OracleIntegrationProtocol(FlextProtocols.Service, Protocol):
            """Protocol for Oracle database integration operations."""

            def extract_oracle_data(
                self,
                oracle_config: dict[str, object],
                extraction_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Extract data from Oracle database for DBT processing.

                Args:
                    oracle_config: Oracle connection configuration
                    extraction_config: Data extraction parameters

                Returns:
                    FlextResult[list[dict[str, object]]]: Extracted Oracle data or error

                """

            def transform_oracle_to_dbt_format(
                self,
                oracle_data: list[dict[str, object]],
                transformation_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Transform Oracle data to DBT-compatible format.

                Args:
                    oracle_data: Raw Oracle data
                    transformation_config: Transformation parameters

                Returns:
                    FlextResult[list[dict[str, object]]]: Transformed data or error

                """

            def validate_oracle_data_quality(
                self,
                data: list[dict[str, object]],
                quality_rules: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Validate Oracle data quality for DBT processing.

                Args:
                    data: Oracle data to validate
                    quality_rules: Data quality validation rules

                Returns:
                    FlextResult[dict[str, object]]: Quality validation results or error

                """

            def sync_oracle_to_warehouse(
                self,
                oracle_data: list[dict[str, object]],
                warehouse_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Sync Oracle data to data warehouse for DBT processing.

                Args:
                    oracle_data: Oracle data to sync
                    warehouse_config: Data warehouse configuration

                Returns:
                    FlextResult[dict[str, object]]: Sync operation results or error

                """

        @runtime_checkable
        class ModelingProtocol(FlextProtocols.Service, Protocol):
            """Protocol for Oracle data modeling operations."""

            def create_table_dimension(
                self,
                oracle_tables: list[dict[str, object]],
                dimension_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Create table dimension model from Oracle table data.

                Args:
                    oracle_tables: Oracle table data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextResult[dict[str, object]]: Table dimension model or error

                """

            def create_schema_dimension(
                self,
                oracle_schemas: list[dict[str, object]],
                dimension_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Create schema dimension model from Oracle schema data.

                Args:
                    oracle_schemas: Oracle schema data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextResult[dict[str, object]]: Schema dimension model or error

                """

            def create_performance_models(
                self,
                oracle_performance_data: list[dict[str, object]],
                modeling_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Create performance models from Oracle performance data.

                Args:
                    oracle_performance_data: Oracle performance metrics
                    modeling_config: Performance modeling configuration

                Returns:
                    FlextResult[dict[str, object]]: Performance models or error

                """

            def generate_fact_tables(
                self,
                dimensions: list[dict[str, object]],
                fact_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Generate fact tables from Oracle dimensions.

                Args:
                    dimensions: Oracle dimension models
                    fact_config: Fact table configuration

                Returns:
                    FlextResult[list[dict[str, object]]]: Generated fact tables or error

                """

        @runtime_checkable
        class TransformationProtocol(FlextProtocols.Service, Protocol):
            """Protocol for Oracle data transformation operations."""

            def normalize_oracle_data_types(
                self,
                oracle_data: list[dict[str, object]],
                normalization_rules: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Normalize Oracle data types for consistent DBT processing.

                Args:
                    oracle_data: Raw Oracle data
                    normalization_rules: Data type normalization rules

                Returns:
                    FlextResult[list[dict[str, object]]]: Normalized Oracle data or error

                """

            def apply_oracle_specific_transformations(
                self,
                oracle_data: list[dict[str, object]],
                transformation_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Apply Oracle-specific data transformations.

                Args:
                    oracle_data: Oracle data to transform
                    transformation_config: Oracle transformation configuration

                Returns:
                    FlextResult[list[dict[str, object]]]: Transformed data or error

                """

            def apply_business_rules(
                self,
                data: list[dict[str, object]],
                business_rules: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Apply business rules to Oracle data transformations.

                Args:
                    data: Oracle data to transform
                    business_rules: Business transformation rules

                Returns:
                    FlextResult[list[dict[str, object]]]: Transformed data or error

                """

            def optimize_oracle_queries(
                self,
                query_config: dict[str, object],
                optimization_rules: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Optimize Oracle queries for DBT processing.

                Args:
                    query_config: Oracle query configuration
                    optimization_rules: Query optimization rules

                Returns:
                    FlextResult[dict[str, object]]: Optimized query configuration or error

                """

        @runtime_checkable
        class MacroProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT macro operations with Oracle data."""

            def generate_oracle_source_macro(
                self, source_config: dict[str, object]
            ) -> FlextResult[str]:
                """Generate DBT macro for Oracle data sources.

                Args:
                    source_config: Oracle source configuration

                Returns:
                    FlextResult[str]: Generated DBT macro or error

                """

            def create_oracle_test_macro(
                self, test_config: dict[str, object]
            ) -> FlextResult[str]:
                """Create DBT test macro for Oracle data validation.

                Args:
                    test_config: Oracle test configuration

                Returns:
                    FlextResult[str]: Generated test macro or error

                """

            def generate_oracle_transformation_macro(
                self, transformation_config: dict[str, object]
            ) -> FlextResult[str]:
                """Generate DBT transformation macro for Oracle data.

                Args:
                    transformation_config: Oracle transformation configuration

                Returns:
                    FlextResult[str]: Generated transformation macro or error

                """

            def create_oracle_snapshot_macro(
                self, snapshot_config: dict[str, object]
            ) -> FlextResult[str]:
                """Create DBT snapshot macro for Oracle data versioning.

                Args:
                    snapshot_config: Oracle snapshot configuration

                Returns:
                    FlextResult[str]: Generated snapshot macro or error

                """

        @runtime_checkable
        class QualityProtocol(FlextProtocols.Service, Protocol):
            """Protocol for Oracle data quality operations."""

            def validate_oracle_schema_compliance(
                self,
                oracle_data: list[dict[str, object]],
                schema_rules: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Validate Oracle data against schema compliance rules.

                Args:
                    oracle_data: Oracle data to validate
                    schema_rules: Schema compliance rules

                Returns:
                    FlextResult[dict[str, object]]: Schema validation results or error

                """

            def check_data_completeness(
                self,
                data: list[dict[str, object]],
                completeness_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Check Oracle data completeness for DBT processing.

                Args:
                    data: Oracle data to check
                    completeness_config: Completeness validation configuration

                Returns:
                    FlextResult[dict[str, object]]: Completeness check results or error

                """

            def detect_data_anomalies(
                self,
                data: list[dict[str, object]],
                anomaly_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Detect anomalies in Oracle data for quality assurance.

                Args:
                    data: Oracle data to analyze
                    anomaly_config: Anomaly detection configuration

                Returns:
                    FlextResult[list[dict[str, object]]]: Detected anomalies or error

                """

            def generate_quality_report(
                self,
                quality_results: list[dict[str, object]],
                report_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Generate data quality report for Oracle DBT processing.

                Args:
                    quality_results: Quality validation results
                    report_config: Report generation configuration

                Returns:
                    FlextResult[dict[str, object]]: Quality report or error

                """

        @runtime_checkable
        class PerformanceProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT Oracle performance optimization operations."""

            def optimize_dbt_models(
                self,
                model_config: dict[str, object],
                performance_metrics: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Optimize DBT models for Oracle data processing performance.

                Args:
                    model_config: DBT model configuration
                    performance_metrics: Current performance metrics

                Returns:
                    FlextResult[dict[str, object]]: Optimization recommendations or error

                """

            def tune_oracle_connections(
                self,
                connection_config: dict[str, object],
                tuning_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Tune Oracle connections for improved DBT performance.

                Args:
                    connection_config: Oracle connection configuration
                    tuning_config: Connection tuning parameters

                Returns:
                    FlextResult[dict[str, object]]: Tuned connection configuration or error

                """

            def monitor_dbt_performance(
                self, run_results: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Monitor DBT performance with Oracle data processing.

                Args:
                    run_results: DBT run results

                Returns:
                    FlextResult[dict[str, object]]: Performance metrics or error

                """

            def optimize_oracle_queries(
                self, query_config: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Optimize Oracle queries for DBT data processing.

                Args:
                    query_config: Oracle query configuration

                Returns:
                    FlextResult[dict[str, object]]: Query optimization results or error

                """

        @runtime_checkable
        class MonitoringProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT Oracle monitoring operations."""

            def track_dbt_run_metrics(
                self, run_id: str, metrics: dict[str, object]
            ) -> FlextResult[bool]:
                """Track DBT run metrics for Oracle data processing.

                Args:
                    run_id: DBT run identifier
                    metrics: Run metrics data

                Returns:
                    FlextResult[bool]: Metric tracking success status

                """

            def monitor_oracle_data_freshness(
                self, freshness_config: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Monitor Oracle data freshness for DBT processing.

                Args:
                    freshness_config: Data freshness monitoring configuration

                Returns:
                    FlextResult[dict[str, object]]: Data freshness status or error

                """

            def get_health_status(self) -> FlextResult[dict[str, object]]:
                """Get DBT Oracle integration health status.

                Returns:
                    FlextResult[dict[str, object]]: Health status or error

                """

            def create_monitoring_dashboard(
                self, dashboard_config: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Create monitoring dashboard for DBT Oracle operations.

                Args:
                    dashboard_config: Dashboard configuration

                Returns:
                    FlextResult[dict[str, object]]: Dashboard creation result or error

                """

    # ============================================================================
    # BACKWARD COMPATIBILITY ALIASES (100% COMPATIBILITY)
    # ============================================================================

    # DBT operations
    DbtProtocol = DbtOracle.DbtProtocol

    # Oracle integration
    OracleIntegrationProtocol = DbtOracle.OracleIntegrationProtocol

    # Data modeling
    ModelingProtocol = DbtOracle.ModelingProtocol

    # Transformations
    TransformationProtocol = DbtOracle.TransformationProtocol

    # DBT macros
    MacroProtocol = DbtOracle.MacroProtocol

    # Data quality
    QualityProtocol = DbtOracle.QualityProtocol

    # Performance optimization
    PerformanceProtocol = DbtOracle.PerformanceProtocol

    # Monitoring
    MonitoringProtocol = DbtOracle.MonitoringProtocol

    # Convenience aliases for downstream usage
    DbtOracleProtocol = DbtOracle.DbtProtocol
    DbtOracleIntegrationProtocol = DbtOracle.OracleIntegrationProtocol
    DbtOracleModelingProtocol = DbtOracle.ModelingProtocol
    DbtOracleTransformationProtocol = DbtOracle.TransformationProtocol
    DbtOracleMacroProtocol = DbtOracle.MacroProtocol
    DbtOracleQualityProtocol = DbtOracle.QualityProtocol
    DbtOraclePerformanceProtocol = DbtOracle.PerformanceProtocol
    DbtOracleMonitoringProtocol = DbtOracle.MonitoringProtocol


__all__ = [
    "FlextDbtOracleProtocols",
]
