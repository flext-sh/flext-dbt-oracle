"""Connection primitives shared by DBT Oracle modules."""

from __future__ import annotations

from pydantic import SecretStr

from flext_dbt_oracle import FlextDbtOracleModels, c


class FlextDbtOracleConnections:
    """Facade for Oracle connection config construction."""

    @staticmethod
    def build_oracle_connection_config(
        host: str,
        username: str,
        password: str,
        service_name: str = c.DbtOracle.Oracle.DEFAULT_SERVICE_NAME,
        *,
        sid: str | None = None,
        port: int = c.DbtOracle.Oracle.DEFAULT_PORT,
        protocol: str = c.DbtOracle.Oracle.DEFAULT_PROTOCOL,
    ) -> FlextDbtOracleModels.DbtOracle.OracleConnectionConfig:
        """Create validated Oracle connection config t.NormalizedValue."""
        return FlextDbtOracleModels.DbtOracle.OracleConnectionConfig(
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
    service_name: str = c.DbtOracle.Oracle.DEFAULT_SERVICE_NAME,
    *,
    sid: str | None = None,
    port: int = c.DbtOracle.Oracle.DEFAULT_PORT,
    protocol: str = c.DbtOracle.Oracle.DEFAULT_PROTOCOL,
) -> FlextDbtOracleModels.DbtOracle.OracleConnectionConfig:
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
