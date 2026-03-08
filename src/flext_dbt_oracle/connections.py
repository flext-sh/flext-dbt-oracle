"""Connection primitives shared by DBT Oracle modules."""

from __future__ import annotations

from flext_dbt_oracle.constants import c


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
        password=password,
        protocol=protocol,
    )


__all__ = ["OracleConnectionConfig", "build_oracle_connection_config"]
