"""DBT Oracle protocols for FLEXT ecosystem."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_db_oracle import FlextDbOracleProtocols
from flext_dbt_oracle import t
from flext_meltano import FlextMeltanoProtocols


class FlextDbtOracleProtocols(FlextMeltanoProtocols, FlextDbOracleProtocols):
    """DBT Oracle protocols extending Oracle and Meltano protocols."""

    class DbtOracle:
        """DBT Oracle domain protocols."""

        @runtime_checkable
        class Dbt(FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload], Protocol):
            """Protocol for DBT operations with Oracle data."""

            def compile_dbt_models(
                self,
                models: t.ScalarList | None = None,
                config: t.DbtOracle.OraclePayload | None = None,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Compile DBT models for Oracle data processing."""
                ...

            def get_dbt_manifest(
                self,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Get DBT manifest with Oracle model definitions."""
                ...

            def run_dbt_models(
                self,
                models: t.ScalarList | None = None,
                config: t.DbtOracle.OraclePayload | None = None,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Run DBT models with Oracle data sources."""
                ...

            def test_dbt_models(
                self,
                models: t.ScalarList | None = None,
                config: t.DbtOracle.OraclePayload | None = None,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Test DBT models with Oracle data validation."""
                ...

            def validate_dbt_project(
                self,
                project_path: str,
            ) -> FlextMeltanoProtocols.Result[bool]:
                """Validate DBT project configuration for Oracle integration."""
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
                """Extract data from Oracle database for DBT processing."""
                ...

            def sync_oracle_to_warehouse(
                self,
                oracle_data: t.DbtOracle.OraclePayloadList,
                warehouse_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Sync Oracle data to data warehouse for DBT processing."""
                ...

            def transform_oracle_to_dbt_format(
                self,
                oracle_data: t.DbtOracle.OraclePayloadList,
                transformation_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Transform Oracle data to DBT-compatible format."""
                ...

            def validate_oracle_data_quality(
                self,
                data: t.DbtOracle.OraclePayloadList,
                quality_rules: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Validate Oracle data quality for DBT processing."""
                ...

        @runtime_checkable
        class Modeling(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload],
            Protocol,
        ):
            """Protocol for Oracle data modeling operations."""

            def create_performance_models(
                self,
                oracle_performance_data: t.DbtOracle.OraclePayloadList,
                modeling_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Create performance models from Oracle performance data."""
                ...

            def create_schema_dimension(
                self,
                oracle_schemas: t.DbtOracle.OraclePayloadList,
                dimension_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Create schema dimension model from Oracle schema data."""
                ...

            def create_table_dimension(
                self,
                oracle_tables: t.DbtOracle.OraclePayloadList,
                dimension_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Create table dimension model from Oracle table data."""
                ...

            def generate_fact_tables(
                self,
                dimensions: t.DbtOracle.OraclePayloadList,
                fact_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Generate fact tables from Oracle dimensions."""
                ...

        @runtime_checkable
        class Transformation(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload],
            Protocol,
        ):
            """Protocol for Oracle data transformation operations."""

            def apply_business_rules(
                self,
                data: t.DbtOracle.OraclePayloadList,
                business_rules: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Apply business rules to Oracle data transformations."""
                ...

            def apply_oracle_specific_transformations(
                self,
                oracle_data: t.DbtOracle.OraclePayloadList,
                transformation_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Apply Oracle-specific data transformations."""
                ...

            def normalize_oracle_data_types(
                self,
                oracle_data: t.DbtOracle.OraclePayloadList,
                normalization_rules: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Normalize Oracle data types for consistent DBT processing."""
                ...

            def optimize_oracle_queries(
                self,
                query_config: t.DbtOracle.OraclePayload,
                optimization_rules: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Optimize Oracle queries for DBT processing."""
                ...

        @runtime_checkable
        class Macro(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload],
            Protocol,
        ):
            """Protocol for DBT macro operations with Oracle data."""

            def create_oracle_snapshot_macro(
                self,
                snapshot_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[str]:
                """Create DBT snapshot macro for Oracle data versioning."""
                ...

            def create_oracle_test_macro(
                self,
                test_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[str]:
                """Create DBT test macro for Oracle data validation."""
                ...

            def generate_oracle_source_macro(
                self,
                source_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[str]:
                """Generate DBT macro for Oracle data sources."""
                ...

            def generate_oracle_transformation_macro(
                self,
                transformation_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[str]:
                """Generate DBT transformation macro for Oracle data."""
                ...

        @runtime_checkable
        class Quality(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload],
            Protocol,
        ):
            """Protocol for Oracle data quality operations."""

            def check_data_completeness(
                self,
                data: t.DbtOracle.OraclePayloadList,
                completeness_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Check Oracle data completeness for DBT processing."""
                ...

            def detect_data_anomalies(
                self,
                data: t.DbtOracle.OraclePayloadList,
                anomaly_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayloadList]:
                """Detect anomalies in Oracle data for quality assurance."""
                ...

            def generate_quality_report(
                self,
                quality_results: t.DbtOracle.OraclePayloadList,
                report_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Generate data quality report for Oracle DBT processing."""
                ...

            def validate_oracle_schema_compliance(
                self,
                oracle_data: t.DbtOracle.OraclePayloadList,
                schema_rules: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Validate Oracle data against schema compliance rules."""
                ...

        @runtime_checkable
        class Performance(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload],
            Protocol,
        ):
            """Protocol for DBT Oracle performance optimization."""

            def monitor_dbt_performance(
                self,
                run_results: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Monitor DBT performance with Oracle data processing."""
                ...

            def optimize_dbt_models(
                self,
                model_config: t.DbtOracle.OraclePayload,
                performance_metrics: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Optimize DBT models for Oracle data processing performance."""
                ...

            def optimize_oracle_query_performance(
                self,
                query_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Optimize Oracle queries for DBT data processing."""
                ...

            def tune_oracle_connections(
                self,
                connection_config: t.DbtOracle.OraclePayload,
                tuning_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Tune Oracle connections for improved DBT performance."""
                ...

        @runtime_checkable
        class Monitoring(
            FlextDbOracleProtocols.Service[t.DbtOracle.OraclePayload],
            Protocol,
        ):
            """Protocol for DBT Oracle monitoring operations."""

            def create_monitoring_dashboard(
                self,
                dashboard_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Create monitoring dashboard for DBT Oracle operations."""
                ...

            def get_health_status(
                self,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Get DBT Oracle integration health status."""
                ...

            def monitor_oracle_data_freshness(
                self,
                freshness_config: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[t.DbtOracle.OraclePayload]:
                """Monitor Oracle data freshness for DBT processing."""
                ...

            def track_dbt_run_metrics(
                self,
                run_id: str,
                metrics: t.DbtOracle.OraclePayload,
            ) -> FlextMeltanoProtocols.Result[bool]:
                """Track DBT run metrics for Oracle data processing."""
                ...


__all__ = ["FlextDbtOracleProtocols", "p"]

p = FlextDbtOracleProtocols
