"""Service helpers for workflow guidance and telemetry payloads."""

from __future__ import annotations

type JsonScalar = str | int | float | bool | None
type JsonValue = JsonScalar | dict[str, JsonValue] | list[JsonValue]
PERFORMANCE_RECOMMENDATION_THRESHOLD = 20


class FlextDbtOracleServices:
    """Utility service namespace for DBT Oracle workflows."""

    def generate_recommendations(self, table_count: int) -> dict[str, JsonValue]:
        """Generate lightweight recommendations from table volume."""
        recommendations: list[JsonValue] = []
        if table_count > PERFORMANCE_RECOMMENDATION_THRESHOLD:
            recommendations.append(
                "Process tables in batches and increase dbt threads gradually"
            )
        return {
            "table_count": table_count,
            "recommendations": recommendations,
        }

    def track_execution(self, workflow_name: str) -> dict[str, JsonValue]:
        """Build a minimal execution tracking payload."""
        return {
            "workflow": workflow_name,
            "status": "running",
        }


FlextDbtOracleWorkflowService = FlextDbtOracleServices
FlextDbtOracleMonitoringService = FlextDbtOracleServices

__all__ = [
    "FlextDbtOracleMonitoringService",
    "FlextDbtOracleServices",
    "FlextDbtOracleWorkflowService",
]
