"""Connection primitives shared by DBT Oracle modules."""

from __future__ import annotations

from pydantic import BaseModel, Field, SecretStr

from flext_dbt_oracle.constants import c


class OracleConnectionConfig(BaseModel):
    """Configuration for Oracle database connections."""

    host: str = Field(description="Oracle database host")
    port: int = Field(description="Oracle database port")
    username: str = Field(description="Oracle database username")
    password: SecretStr = Field(description="Oracle database password")
    service_name: str = Field(description="Oracle service name")
    sid: str | None = Field(default=None, description="Oracle SID (optional)")
    protocol: str = Field(description="Oracle connection protocol")


def build_oracle_connection_config(
    host: str,
    username: str,
    password: str,
    service_name: str = c.Oracle.DEFAULT_SERVICE_NAME,
    *,
    sid: str | None = None,
    port: int = c.Oracle.DEFAULT_PORT,
    protocol: str = c.Oracle.DEFAULT_PROTOCOL,
) -> OracleConnectionConfig:
    """Create validated Oracle connection config object."""
    return OracleConnectionConfig(
        host=host,
        port=port,
        service_name=service_name,
        sid=sid,
        username=username,
        password=SecretStr(password),
        protocol=protocol,
    )


__all__ = ["OracleConnectionConfig", "build_oracle_connection_config"]
