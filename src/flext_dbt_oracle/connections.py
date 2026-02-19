"""Connection primitives shared by DBT Oracle modules."""

from __future__ import annotations

from pydantic import BaseModel, Field


class OracleConnectionConfig(BaseModel):
    """Structured Oracle connection parameters."""

    host: str = "localhost"
    port: int = Field(default=1521, ge=1)
    service_name: str = "XEPDB1"
    sid: str | None = None
    username: str = ""
    password: str = ""
    protocol: str = "tcp"

    def get_database_identifier(self) -> str:
        """Return SID when present, otherwise service name."""
        return self.sid or self.service_name

    def get_dsn(self) -> str:
        """Build a masked DSN string from runtime fields."""
        identifier = self.get_database_identifier()
        separator = ":" if self.sid else "/"
        return f"{self.protocol}://{self.username}:***@{self.host}:{self.port}{separator}{identifier}"


def build_oracle_connection_config(
    host: str,
    username: str,
    password: str,
    service_name: str = "XEPDB1",
    *,
    sid: str | None = None,
    port: int = 1521,
    protocol: str = "tcp",
) -> OracleConnectionConfig:
    """Create validated Oracle connection config object."""
    return OracleConnectionConfig(
        host=host,
        port=port,
        service_name=service_name,
        sid=sid,
        username=username,
        password=password,
        protocol=protocol,
    )


__all__ = ["OracleConnectionConfig", "build_oracle_connection_config"]
