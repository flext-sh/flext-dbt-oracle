# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_oracle/_protocols/dbt
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

from flext_dbt_oracle import t

if TYPE_CHECKING:
    from flext_dbt_oracle._constants import FlextDbtOracleConstantsEnums


class FlextDbtOracleProtocolsDbt:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class Model(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def name(self) -> str:
            """DBT model name."""
            ...

        @property
        def dbt_model_type(self) -> str:
            """DBT model classification."""
            ...

        @property
        def schema_name(self) -> str:
            """Target schema name."""
            ...

        @property
        def table_name(self) -> str:
            """Target table name."""
            ...

        @property
        def materialization(self) -> FlextDbtOracleConstantsEnums.Dbt.Materialization:
            """DBT materialization strategy."""
            ...

        @property
        def sql_content(self) -> str:
            """Model SQL body."""
            ...

        @property
        def description(self) -> str:
            """Human-readable model description."""
            ...

        @property
        def source_name(self) -> str:
            """Source system name."""
            ...

        @property
        def columns(self) -> Sequence[Mapping[str, str]]:
            """Normalized column metadata for the DBT model."""
            ...

        @property
        def dependencies(self) -> Sequence[str]:
            """Upstream DBT model dependencies."""
            ...

    @runtime_checkable
    class DbtConnectionProfile(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def type(self) -> str:
            """Dbt adapter type."""
            ...

        @property
        def host(self) -> str:
            """Oracle database host."""
            ...

        @property
        def port(self) -> t.PortNumber:
            """Oracle database port."""
            ...

        @property
        def user(self) -> str:
            """Oracle database username."""
            ...

        @property
        def password(self) -> str:
            """Oracle database password."""
            ...

        @property
        def service_name(self) -> str:
            """Oracle service name."""
            ...

        @property
        def schema_name(self) -> str:
            """Target dbt schema."""
            ...

        @property
        def project(self) -> str:
            """Dbt project name."""
            ...

    @runtime_checkable
    class OracleTableAdapter(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def schema_name(self) -> str:
            """Oracle schema name."""
            ...

        @property
        def table_name(self) -> str:
            """Oracle table name."""
            ...

        @property
        def relation(self) -> str:
            """Fully qualified relation name."""
            ...

        @property
        def relation_name(self) -> str:
            """Fully qualified relation name under its stable public name."""
            ...


__all__: list[str] = [
    "FlextDbtOracleProtocolsDbt",
]
