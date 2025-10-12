"""DBT Oracle protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextCore


class FlextDbtOracleProtocols:
    """DBT Oracle protocols with explicit re-exports from FlextCore.Protocols foundation.

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

    Foundation = FlextCore.Protocols.Foundation
    Domain = FlextCore.Protocols.Domain
    Application = FlextCore.Protocols.Application
    Infrastructure = FlextCore.Protocols.Infrastructure
    Extensions = FlextCore.Protocols.Extensions
    Commands = FlextCore.Protocols.Commands

    # ============================================================================
    # DBT ORACLE-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class DbtOracle:
        """DBT Oracle domain protocols for Oracle database transformation and analytics."""

        @runtime_checkable
        class DbtProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT operations with Oracle data."""

            def run_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Run DBT models with Oracle data sources.

                Args:
                    models: Specific models to run, or None for all models
                    config: DBT configuration parameters

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT run results or error

                """

            def test_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Test DBT models with Oracle data validation.

                Args:
                    models: Specific models to test, or None for all models
                    config: DBT test configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT test results or error

                """

            def compile_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Compile DBT models for Oracle data processing.

                Args:
                    models: Specific models to compile, or None for all models
                    config: DBT compilation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT compilation results or error

                """

            def get_dbt_manifest(self) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Get DBT manifest with Oracle model definitions.

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT manifest or error

                """

            def validate_dbt_project(self, project_path: str) -> FlextCore.Result[bool]:
                """Validate DBT project configuration for Oracle integration.

                Args:
                    project_path: Path to DBT project directory

                Returns:
                    FlextCore.Result[bool]: Validation status or error

                """

        @runtime_checkable
        class OracleIntegrationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Oracle database integration operations."""

            def extract_oracle_data(
                self,
                oracle_config: FlextCore.Types.Dict,
                extraction_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Extract data from Oracle database for DBT processing.

                Args:
                    oracle_config: Oracle connection configuration
                    extraction_config: Data extraction parameters

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Extracted Oracle data or error

                """

            def transform_oracle_to_dbt_format(
                self,
                oracle_data: list[FlextCore.Types.Dict],
                transformation_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Transform Oracle data to DBT-compatible format.

                Args:
                    oracle_data: Raw Oracle data
                    transformation_config: Transformation parameters

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Transformed data or error

                """

            def validate_oracle_data_quality(
                self,
                data: list[FlextCore.Types.Dict],
                quality_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Validate Oracle data quality for DBT processing.

                Args:
                    data: Oracle data to validate
                    quality_rules: Data quality validation rules

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Quality validation results or error

                """

            def sync_oracle_to_warehouse(
                self,
                oracle_data: list[FlextCore.Types.Dict],
                warehouse_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Sync Oracle data to data warehouse for DBT processing.

                Args:
                    oracle_data: Oracle data to sync
                    warehouse_config: Data warehouse configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Sync operation results or error

                """

        @runtime_checkable
        class ModelingProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Oracle data modeling operations."""

            def create_table_dimension(
                self,
                oracle_tables: list[FlextCore.Types.Dict],
                dimension_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create table dimension model from Oracle table data.

                Args:
                    oracle_tables: Oracle table data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Table dimension model or error

                """

            def create_schema_dimension(
                self,
                oracle_schemas: list[FlextCore.Types.Dict],
                dimension_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create schema dimension model from Oracle schema data.

                Args:
                    oracle_schemas: Oracle schema data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Schema dimension model or error

                """

            def create_performance_models(
                self,
                oracle_performance_data: list[FlextCore.Types.Dict],
                modeling_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create performance models from Oracle performance data.

                Args:
                    oracle_performance_data: Oracle performance metrics
                    modeling_config: Performance modeling configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Performance models or error

                """

            def generate_fact_tables(
                self,
                dimensions: list[FlextCore.Types.Dict],
                fact_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Generate fact tables from Oracle dimensions.

                Args:
                    dimensions: Oracle dimension models
                    fact_config: Fact table configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Generated fact tables or error

                """

        @runtime_checkable
        class TransformationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Oracle data transformation operations."""

            def normalize_oracle_data_types(
                self,
                oracle_data: list[FlextCore.Types.Dict],
                normalization_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Normalize Oracle data types for consistent DBT processing.

                Args:
                    oracle_data: Raw Oracle data
                    normalization_rules: Data type normalization rules

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Normalized Oracle data or error

                """

            def apply_oracle_specific_transformations(
                self,
                oracle_data: list[FlextCore.Types.Dict],
                transformation_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Apply Oracle-specific data transformations.

                Args:
                    oracle_data: Oracle data to transform
                    transformation_config: Oracle transformation configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Transformed data or error

                """

            def apply_business_rules(
                self,
                data: list[FlextCore.Types.Dict],
                business_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Apply business rules to Oracle data transformations.

                Args:
                    data: Oracle data to transform
                    business_rules: Business transformation rules

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Transformed data or error

                """

            def optimize_oracle_queries(
                self,
                query_config: FlextCore.Types.Dict,
                optimization_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Optimize Oracle queries for DBT processing.

                Args:
                    query_config: Oracle query configuration
                    optimization_rules: Query optimization rules

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Optimized query configuration or error

                """

        @runtime_checkable
        class MacroProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT macro operations with Oracle data."""

            def generate_oracle_source_macro(
                self, source_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Generate DBT macro for Oracle data sources.

                Args:
                    source_config: Oracle source configuration

                Returns:
                    FlextCore.Result[str]: Generated DBT macro or error

                """

            def create_oracle_test_macro(
                self, test_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Create DBT test macro for Oracle data validation.

                Args:
                    test_config: Oracle test configuration

                Returns:
                    FlextCore.Result[str]: Generated test macro or error

                """

            def generate_oracle_transformation_macro(
                self, transformation_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Generate DBT transformation macro for Oracle data.

                Args:
                    transformation_config: Oracle transformation configuration

                Returns:
                    FlextCore.Result[str]: Generated transformation macro or error

                """

            def create_oracle_snapshot_macro(
                self, snapshot_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Create DBT snapshot macro for Oracle data versioning.

                Args:
                    snapshot_config: Oracle snapshot configuration

                Returns:
                    FlextCore.Result[str]: Generated snapshot macro or error

                """

        @runtime_checkable
        class QualityProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Oracle data quality operations."""

            def validate_oracle_schema_compliance(
                self,
                oracle_data: list[FlextCore.Types.Dict],
                schema_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Validate Oracle data against schema compliance rules.

                Args:
                    oracle_data: Oracle data to validate
                    schema_rules: Schema compliance rules

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Schema validation results or error

                """

            def check_data_completeness(
                self,
                data: list[FlextCore.Types.Dict],
                completeness_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Check Oracle data completeness for DBT processing.

                Args:
                    data: Oracle data to check
                    completeness_config: Completeness validation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Completeness check results or error

                """

            def detect_data_anomalies(
                self,
                data: list[FlextCore.Types.Dict],
                anomaly_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Detect anomalies in Oracle data for quality assurance.

                Args:
                    data: Oracle data to analyze
                    anomaly_config: Anomaly detection configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Detected anomalies or error

                """

            def generate_quality_report(
                self,
                quality_results: list[FlextCore.Types.Dict],
                report_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Generate data quality report for Oracle DBT processing.

                Args:
                    quality_results: Quality validation results
                    report_config: Report generation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Quality report or error

                """

        @runtime_checkable
        class PerformanceProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT Oracle performance optimization operations."""

            def optimize_dbt_models(
                self,
                model_config: FlextCore.Types.Dict,
                performance_metrics: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Optimize DBT models for Oracle data processing performance.

                Args:
                    model_config: DBT model configuration
                    performance_metrics: Current performance metrics

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Optimization recommendations or error

                """

            def tune_oracle_connections(
                self,
                connection_config: FlextCore.Types.Dict,
                tuning_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Tune Oracle connections for improved DBT performance.

                Args:
                    connection_config: Oracle connection configuration
                    tuning_config: Connection tuning parameters

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Tuned connection configuration or error

                """

            def monitor_dbt_performance(
                self, run_results: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Monitor DBT performance with Oracle data processing.

                Args:
                    run_results: DBT run results

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Performance metrics or error

                """

            def optimize_oracle_queries(
                self, query_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Optimize Oracle queries for DBT data processing.

                Args:
                    query_config: Oracle query configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Query optimization results or error

                """

        @runtime_checkable
        class MonitoringProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT Oracle monitoring operations."""

            def track_dbt_run_metrics(
                self, run_id: str, metrics: FlextCore.Types.Dict
            ) -> FlextCore.Result[bool]:
                """Track DBT run metrics for Oracle data processing.

                Args:
                    run_id: DBT run identifier
                    metrics: Run metrics data

                Returns:
                    FlextCore.Result[bool]: Metric tracking success status

                """

            def monitor_oracle_data_freshness(
                self, freshness_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Monitor Oracle data freshness for DBT processing.

                Args:
                    freshness_config: Data freshness monitoring configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Data freshness status or error

                """

            def get_health_status(self) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Get DBT Oracle integration health status.

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Health status or error

                """

            def create_monitoring_dashboard(
                self, dashboard_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create monitoring dashboard for DBT Oracle operations.

                Args:
                    dashboard_config: Dashboard configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Dashboard creation result or error

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
