"""Connection primitives shared by DBT Oracle modules."""

from __future__ import annotations

from pydantic import SecretStr

from flext_dbt_oracle.constants import c
from flext_dbt_oracle.models import FlextDbtOracleModels


class FlextDbtOracleConnections:
    """Facade for Oracle connection config construction."""

    @staticmethod
    def build_oracle_connection_config(
        host: str,
        username: str,
        password: str,
        service_name: str = c.Oracle.DEFAULT_SERVICE_NAME,
        *,
        sid: str | None = None,
        port: int = c.Oracle.DEFAULT_PORT,
        protocol: str = c.Oracle.DEFAULT_PROTOCOL,
    ) -> FlextDbtOracleModels.OracleConnectionConfig:
        """Create validated Oracle connection config t.NormalizedValue."""
        return FlextDbtOracleModels.OracleConnectionConfig(
            host=host,
            port=port,
            service_name=service_name,
            sid=sid,
            username=username,
            password=SecretStr(password),
            protocol=protocol,
        )


def build_oracle_connection_config(
    host: str,
    username: str,
    password: str,
    service_name: str = c.Oracle.DEFAULT_SERVICE_NAME,
    *,
    sid: str | None = None,
    port: int = c.Oracle.DEFAULT_PORT,
    protocol: str = c.Oracle.DEFAULT_PROTOCOL,
) -> FlextDbtOracleModels.OracleConnectionConfig:
    """Module-level shim — delegates to FlextDbtOracleConnections.build_oracle_connection_config."""
    return FlextDbtOracleConnections.build_oracle_connection_config(
        host=host,
        username=username,
        password=password,
        service_name=service_name,
        sid=sid,
        port=port,
        protocol=protocol,
    )


__all__ = [
    "FlextDbtOracleConnections",
    "build_oracle_connection_config",
]
