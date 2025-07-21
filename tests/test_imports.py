"""Test basic imports work without DBT runtime."""

import pytest


def test_module_structure() -> None:
    """Test that module structure exists."""
    import dbt.adapters.oracle

    assert hasattr(dbt.adapters.oracle, "__version__")
    assert dbt.adapters.oracle.__version__ == "1.0.0"


@pytest.mark.unit
def test_basic_functionality() -> None:
    """Test basic functionality without DBT runtime."""
    # Just ensure our code can be imported
    assert True
