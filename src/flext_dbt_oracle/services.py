"""Service helpers for workflow guidance and telemetry payloads."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_dbt_oracle import c, t


class FlextDbtOracleServices:
    """Utility service namespace for DBT Oracle workflows."""

    def generate_recommendations(
        self,
        table_count: int,
    ) -> Mapping[str, t.MetadataValue]:
        """Generate lightweight recommendations from table volume."""
        recommendations: Sequence[t.Scalar] = [
            "Process tables in batches and increase dbt threads gradually"
            for _ in [None]
            if table_count > c.DbtOracle.PERFORMANCE_RECOMMENDATION_THRESHOLD
        ]
        return {"table_count": table_count, "recommendations": recommendations}

    def track_execution(self, workflow_name: str) -> t.ConfigurationMapping:
        """Build a minimal execution tracking payload."""
        return {"workflow": workflow_name, "status": "running"}


__all__ = ["FlextDbtOracleServices"]
