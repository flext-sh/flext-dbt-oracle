"""DBT Oracle CLI — command interface for DBT Oracle workflows.

Thin delegation to FlextDbtOracle facade methods.
"""

from __future__ import annotations

from typing import override

from flext_cli import c, p, r, t, u

from . import FlextDbtOracleSettings, FlextDbtOracle, c as pkg_c, settings
from .api import FlextDbtOracle as FlextDbtOracleFacade


class FlextDbtOracleCli(FlextDbtOracleFacade):
    """CLI facade for DBT Oracle operations."""

    @classmethod
    @override
    def _cli_entry_points(cls) -> t.MappingKV[str, t.Callable[..., p.Result[t.JsonValue]]]:
        """Map CLI verbs to facade methods returning p.Result."""
        return {
            "discover": lambda **_: cls._wrap(lambda api: api.discover()),
            "extract": lambda table_name, filters=None: cls._wrap(
                lambda api: api.extract(table_name, filters)
            ),
            "run-pipeline": lambda tables=None, filters=None: cls._wrap(
                lambda api: api.run_pipeline(tables, filters)
            ),
            "test-connection": lambda **_: cls._wrap(
                lambda api: api.test_connection()
            ),
            "build-staging": lambda tables: cls._wrap(
                lambda api: api.build_staging_models(tables)
            ),
        }

    @staticmethod
    def _wrap(fn) -> p.Result[t.JsonValue]:
        """Execute facade method and return p.Result."""
        api = FlextDbtOracleFacade()
        return fn(api)


def cli() -> None:
    """CLI entry point."""
    FlextDbtOracleCli.execute()


__all__: list[str] = ["FlextDbtOracleCli", "cli"]
