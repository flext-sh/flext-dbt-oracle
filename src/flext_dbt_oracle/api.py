"""DBT Oracle facade — unified entry point for DBT Oracle workflows.

Single responsibility: Delegate to FlextDbtOracleClient for actual
operations, to FlextDbtOracleModels for data validation, and to
FlextDbtOracleUtilities for SQL/model generation.
"""

from __future__ import annotations

from typing import ClassVar, override

from . import FlextDbtOracleSettings, c, m, p, r, s, t, u
from .services.client import FlextDbtOracleClient


class FlextDbtOracle(s[bool]):
    """Unified DBT Oracle facade — pure delegation pattern.

    Single responsibility: Delegate DBT Oracle operations to FlextDbtOracleClient.
    All configuration through FlextDbtOracleSettings model.
    All data validation through FlextDbtOracleModels.
    All SQL/model generation through FlextDbtOracleUtilities.
    100% GENERIC — no domain coupling.
    """

    model_config: ClassVar[m.ConfigDict] = m.ConfigDict(use_enum_values=True)

    _client: FlextDbtOracleClient | None = u.PrivateAttr(default_factory=lambda: None)

    def __init__(
        self, settings: FlextDbtOracleSettings | None = None
    ) -> None:
        """Bind the facade to explicit settings or the global singleton."""
        resolved = settings if settings is not None else FlextDbtOracleSettings.fetch_global()
        super().__init__(runtime_settings=resolved)

    @property
    @override
    def settings(self) -> FlextDbtOracleSettings:
        """The typed DBT Oracle settings bound to this facade."""
        current = super().settings
        return current

    @property
    def client(self) -> FlextDbtOracleClient:
        """Lazily instantiate the client bound to this facade's settings."""
        if self._client is None:
            self._client = FlextDbtOracleClient(self.settings)
        return self._client

    def discover(self) -> p.Result[t.StrSequence]:
        """Discover available Oracle tables for modeling."""
        return r[t.StrSequence].ok(self.client.discover_tables())

    def extract(
        self, table_name: str, filters: t.ConfigurationMapping | None = None
    ) -> p.Result[t.SequenceOf[t.ConfigurationMapping]]:
        """Extract sample data for a table."""
        return r[t.SequenceOf[t.ConfigurationMapping]].ok(
            self.client.extract_table_data(table_name, filters)
        )

    def run_pipeline(
        self,
        tables: t.StrSequence | None = None,
        filters: t.ConfigurationMapping | None = None,
    ) -> p.Result[t.JsonMapping]:
        """Run discover + extract pipeline."""
        return r[t.JsonMapping].ok(self.client.run_pipeline(tables, filters))

    def test_connection(self) -> p.Result[t.ConfigurationMapping]:
        """Test Oracle connectivity."""
        return r[t.ConfigurationMapping].ok(self.client.test_connection())

    def build_staging_models(
        self, source_tables: t.StrSequence
    ) -> p.Result[t.SequenceOf[m.DbtOracle.Model]]:
        """Generate deterministic staging model metadata."""
        return r[t.SequenceOf[m.DbtOracle.Model]].ok(
            u.DbtOracle.ModelBuilder.generate_staging_models(source_tables)
        )

    @property
    @override
    def runtime_settings(self) -> FlextDbtOracleSettings:
        """Override base property for covariant return."""
        return super().runtime_settings


__all__: list[str] = ["FlextDbtOracle"]
