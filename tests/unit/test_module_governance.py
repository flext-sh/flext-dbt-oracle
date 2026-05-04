"""Governance checks for DBT Oracle module structure."""

from __future__ import annotations

import importlib
import inspect
from collections.abc import Iterator
from pathlib import Path
from types import ModuleType

from tests import c


def _package_root() -> Path:
    project_root_parent_depth: int = c.DbtOracle.Tests.PROJECT_ROOT_PARENT_DEPTH
    src_dir: str = c.DbtOracle.Tests.SRC_DIR
    package_dir: str = c.DbtOracle.Tests.PACKAGE_DIR
    project_root: Path = Path(
        Path(__file__).resolve().parents[project_root_parent_depth],
    )
    package_root: Path = project_root / src_dir / package_dir
    return package_root


def _iter_package_modules() -> list[Path]:
    return sorted(_package_root().rglob("*.py"))


def _module_dotted_name(module_path: Path) -> str:
    package_root = _package_root()
    relative = module_path.relative_to(package_root.parent)
    parts = relative.with_suffix("").parts
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _import_package_module(module_path: Path) -> ModuleType | None:
    try:
        return importlib.import_module(_module_dotted_name(module_path))
    except (ImportError, AttributeError):
        return None


def _module_top_level_attrs(module: ModuleType) -> Iterator[tuple[str, object]]:
    module_name = module.__name__
    for name, value in vars(module).items():
        if name.startswith("__") and name.endswith("__"):
            continue
        owner = getattr(value, "__module__", None)
        if owner is not None and owner != module_name:
            continue
        yield name, value


class TestsFlextDbtOracleModuleGovernance:
    """Behavior contract for test_module_governance."""

    def test_package_modules_do_not_define_module_level_loggers(self) -> None:
        violations: list[str] = []
        for module_path in _iter_package_modules():
            module = _import_package_module(module_path)
            if module is None:
                continue
            for name, _ in _module_top_level_attrs(module):
                if name in {"logger", "_logger"}:
                    violations.append(
                        str(module_path.relative_to(_package_root().parent))
                    )
                    break
        assert not violations, (
            f"Module-level logger assignments are forbidden: {violations}"
        )

    def test_package_modules_do_not_define_top_level_functions(self) -> None:
        violations: list[str] = []
        for module_path in _iter_package_modules():
            module = _import_package_module(module_path)
            if module is None:
                continue
            unexpected_functions = sorted(
                name
                for name, value in _module_top_level_attrs(module)
                if inspect.isfunction(value)
            )
            if unexpected_functions:
                violations.append(
                    f"{module_path.relative_to(_package_root().parent)}: {unexpected_functions}",
                )
        assert not violations, (
            f"Top-level functions are forbidden in package modules: {violations}"
        )
