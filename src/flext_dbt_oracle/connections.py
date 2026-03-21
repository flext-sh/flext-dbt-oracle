"""Connection primitives shared by DBT Oracle modules."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field, SecretStr, field_validator

from flext_dbt_oracle.constants import FlextDbtOracleConstants as c
from flext_dbt_oracle.typings import FlextDbtOracleTypes as t


class OracleConnectionConfig(BaseModel):
    """Configuration for Oracle database connections."""

    host: Annotated[
        str, Field(default=c.Oracle.DEFAULT_HOST, description="Oracle database host")
    ]
    port: Annotated[
        t.PortNumber,
        Field(default=c.Oracle.DEFAULT_PORT, description="Oracle database port"),
    ]
    username: Annotated[str, Field(default="", description="Oracle database username")]
    password: Annotated[
        str | SecretStr,
        Field(default=SecretStr(""), description="Oracle database password"),
    ]
    service_name: Annotated[
        str,
        Field(default=c.Oracle.DEFAULT_SERVICE_NAME, description="Oracle service name"),
    ]
    sid: Annotated[str | None, Field(default=None, description="Oracle SID (optional)")]
    protocol: Annotated[
        str,
        Field(
            default=c.Oracle.DEFAULT_PROTOCOL, description="Oracle connection protocol"
        ),
    ]

    @field_validator("password", mode="before")
    @classmethod
    def validate_password(cls, v: str | SecretStr) -> SecretStr:
        """Convert string passwords to SecretStr."""
        if isinstance(v, str):
            return SecretStr(v)
        return v

    def get_database_identifier(self) -> str:
        """Return the database identifier (SID if set, otherwise service_name)."""
        if self.sid:
            return self.sid
        return self.service_name

    def get_dsn(self) -> str:
        """Return the connection string in DSN format.

        Format:
        - With service_name: "tcp://username:***@host:port/service_name"
        - With sid: "tcp://username:***@host:port:sid"
        """
        if self.sid:
            return f"{self.protocol}://{self.username}:***@{self.host}:{self.port}:{self.sid}"
        return f"{self.protocol}://{self.username}:***@{self.host}:{self.port}/{self.service_name}"


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
