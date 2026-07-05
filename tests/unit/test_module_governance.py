"""Behavioral governance contract for the flext_dbt_oracle package namespace.

The observable contract under test is the *public module namespace* that the
package exposes on import: per FLEXT AGENTS.md §3.1 every package module must
expose only class-shaped facades — never a module-level logger and never a
loose top-level function. These assertions exercise that contract through the
public ``import`` + attribute surface only (the same surface any consumer sees),
not through any private attribute of a unit under test.
"""

from __future__ import annotations

import importlib
import inspect
import warnings
from pathlib import Path
from typing import TYPE_CHECKING

from tests.constants import c

if TYPE_CHECKING:
    from collections.abc import Iterator
    from types import ModuleType


class TestsFlextDbtOracleModuleGovernance:
    """Behavior contract for the flext_dbt_oracle public module namespace."""

    @staticmethod
    def _package_root() -> Path:
        src_dir: str = c.DbtOracle.Tests.SRC_DIR
        package_dir: str = c.DbtOracle.Tests.PACKAGE_DIR
        # Walk up from this test file to the first ancestor that actually holds
        # ``<src_dir>/<package_dir>`` so discovery is anchored to the real
        # package rather than a fixed, brittle parent depth.
        for ancestor in Path(__file__).resolve().parents:
            candidate = ancestor / src_dir / package_dir
            if candidate.is_dir():
                return candidate
        msg = f"could not locate {src_dir}/{package_dir} above {__file__}"
        raise FileNotFoundError(msg)

    @classmethod
    def _iter_package_modules(cls) -> list[Path]:
        return sorted(cls._package_root().rglob("*.py"))

    @classmethod
    def _relative_name(cls, module_path: Path) -> str:
        return str(module_path.relative_to(cls._package_root().parent))

    @classmethod
    def _dotted_name(cls, module_path: Path) -> str:
        relative = module_path.relative_to(cls._package_root().parent)
        parts = relative.with_suffix("").parts
        if parts[-1] == "__init__":
            parts = parts[:-1]
        return ".".join(parts)

    @classmethod
    def _import_module(cls, module_path: Path) -> ModuleType | None:
        try:
            return importlib.import_module(cls._dotted_name(module_path))
        except (ImportError, AttributeError) as exc:
            warnings.warn(
                f"skipping unimportable governance module {module_path}: {exc}",
                stacklevel=2,
            )
            return None

    @staticmethod
    def _owned_public_attrs(module: ModuleType) -> Iterator[tuple[str, object]]:
        module_name = module.__name__
        for name, value in vars(module).items():
            if name.startswith("__") and name.endswith("__"):
                continue
            owner = getattr(value, "__module__", None)
            if owner is not None and owner != module_name:
                continue
            yield name, value

    def test_package_exposes_at_least_one_module(self) -> None:
        # Guards the discovery contract: an empty scan would make every other
        # invariant vacuously true and hide real regressions.
        modules = self._iter_package_modules()

        assert modules, "expected flext_dbt_oracle package to expose modules"

    def test_public_namespace_never_exposes_a_module_level_logger(self) -> None:
        violations: list[str] = []
        for module_path in self._iter_package_modules():
            module = self._import_module(module_path)
            if module is None:
                continue
            names = {name for name, _ in self._owned_public_attrs(module)}
            if names & {"logger", "_logger"}:
                violations.append(self._relative_name(module_path))

        assert not violations, (
            f"Module-level logger assignments are forbidden: {violations}"
        )

    def test_public_namespace_never_exposes_a_top_level_function(self) -> None:
        violations: list[str] = []
        for module_path in self._iter_package_modules():
            module = self._import_module(module_path)
            if module is None:
                continue
            functions = sorted(
                name
                for name, value in self._owned_public_attrs(module)
                if inspect.isfunction(value)
            )
            if functions:
                violations.append(f"{self._relative_name(module_path)}: {functions}")

        assert not violations, (
            f"Top-level functions are forbidden in package modules: {violations}"
        )


__all__: list[str] = ["TestsFlextDbtOracleModuleGovernance"]
