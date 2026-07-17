"""DBT Oracle protocols for FLEXT ecosystem.

Most inner ``DbtOracle.*`` Protocol classes that previously lived here
(``Dbt``, ``OracleIntegration``, ``Modeling``, ``Transformation``, ``Macro``,
``Quality``, ``Performance``, ``Monitoring``) had zero workspace consumers and
were removed per AGENTS.md §3.5 (no dead code) + STRICT YAGNI. The
``DbtOracle.Model`` protocol is defined here because it is the typed return
contract of ``u.DbtOracle.ModelBuilder.generate_staging_models`` (consumed by
``FlextDbtOracleServiceBase.generate_staging_models``); typing comes from the
protocol, never the concrete ``m`` model (FLEXT law Rule 19). The rest of the
facade behavior is inherited via the ``FlextDbOracleProtocols`` +
``FlextMeltanoProtocols`` MRO chain.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_db_oracle import FlextDbOracleProtocols
from flext_dbt_oracle.constants import FlextDbtOracleConstants as c
from flext_dbt_oracle.typings import FlextDbtOracleTypes as t
from flext_meltano import p


class FlextDbtOracleProtocols(p, FlextDbOracleProtocols):
    """DBT Oracle protocols facade — composes Oracle and Meltano protocols."""

    class DbtOracle:
        """DBT Oracle domain protocol namespace."""

        @runtime_checkable
        class Model(Protocol):
            """Structural contract for a generated DBT staging-model payload."""

            @property
            def name(self) -> str:
                """The DBT model name."""
                ...

            @property
            def dbt_model_type(self) -> str:
                """The DBT model classification."""
                ...

            @property
            def schema_name(self) -> str:
                """The target schema name."""
                ...

            @property
            def table_name(self) -> str:
                """The target table name."""
                ...

            @property
            def materialization(self) -> c.DbtOracle.Dbt.Materialization:
                """The DBT materialization strategy."""
                ...

            @property
            def sql_content(self) -> str:
                """The rendered model SQL body."""
                ...

            @property
            def description(self) -> str:
                """The human-readable model description."""
                ...

            @property
            def source_name(self) -> str:
                """The source system name."""
                ...

            @property
            def columns(self) -> t.SequenceOf[t.StrMapping]:
                """The normalized column metadata."""
                ...

            @property
            def dependencies(self) -> t.StrSequence:
                """The upstream DBT model dependencies."""
                ...


__all__: list[str] = ["FlextDbtOracleProtocols", "p"]

p = FlextDbtOracleProtocols
