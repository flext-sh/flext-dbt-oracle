"""Settings model used by DBT Oracle runtime components."""

from __future__ import annotations

from pydantic import BaseModel, Field


class FlextDbtOracleSettings(BaseModel):
    """Configuration for DBT Oracle operations."""

    oracle_host: str = Field(default="localhost", description="Oracle database host")
    oracle_username: str = Field(description="Oracle database username")
    oracle_password: str = Field(description="Oracle database password")
    oracle_port: int = Field(default=1521, description="Oracle database port")
    oracle_service_name: str = Field(
        default="ORCL", description="Oracle service name or SID"
    )

    def get_database_identifier(self) -> str:
        """Return service name or SID identifier."""
        return self.oracle_service_name


__all__ = ["FlextDbtOracleSettings"]
