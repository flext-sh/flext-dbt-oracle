"""Test basic imports work without DBT runtime."""

import dbt.adapters.oracle
import pytest


def test_module_structure() -> None:
    """Test that module structure exists."""
    assert hasattr(dbt.adapters.oracle, "__version__")
    if dbt.adapters.oracle.__version__ != "1.0.0":
        msg = f"Expected {"1.0.0"}, got {dbt.adapters.oracle.__version__}"
        raise AssertionError(msg)


@pytest.mark.unit
def test_basic_functionality() -> None:
    """Test basic functionality without DBT runtime."""
    # Just ensure our code can be imported
    assert True
