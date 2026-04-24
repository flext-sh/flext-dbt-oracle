"""Governance checks for DBT Oracle module structure."""

from __future__ import annotations

import ast
from pathlib import Path

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


def _read_module_tree(module_path: Path) -> ast.Module:
    return ast.parse(module_path.read_text(encoding="utf-8"), filename=str(module_path))


def test_package_modules_do_not_define_module_level_loggers() -> None:
    violations: list[str] = []
    for module_path in _iter_package_modules():
        module_tree = _read_module_tree(module_path)
        for node in module_tree.body:
            if not isinstance(node, ast.Assign):
                continue
            if any(
                isinstance(target, ast.Name) and target.id == "logger"
                for target in node.targets
            ):
                violations.append(str(module_path.relative_to(_package_root().parent)))
    assert not violations, (
        f"Module-level logger assignments are forbidden: {violations}"
    )


def test_package_modules_do_not_define_top_level_functions() -> None:
    violations: list[str] = []
    for module_path in _iter_package_modules():
        module_tree = _read_module_tree(module_path)
        unexpected_functions = sorted(
            node.name for node in module_tree.body if isinstance(node, ast.FunctionDef)
        )
        if unexpected_functions:
            violations.append(
                f"{module_path.relative_to(_package_root().parent)}: {unexpected_functions}",
            )
    assert not violations, (
        f"Top-level functions are forbidden in package modules: {violations}"
    )
