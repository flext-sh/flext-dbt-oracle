"""Connection primitives shared by DBT Oracle modules."""

from __future__ import annotations

from flext_dbt_oracle import FlextDbtOracleModels, c, t


class FlextDbtOracleConnections:
    """Facade for Oracle connection settings construction."""

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
        """Create validated Oracle connection settings t.JsonValue."""
        return FlextDbtOracleModels.DbtOracle.OracleConnectionConfig(
            host=host,
            port=port,
            service_name=service_name,
            sid=sid,
            username=username,
            password=t.SecretStr(password),
            protocol=protocol,
        )


__all__: list[str] = ["FlextDbtOracleConnections"]
