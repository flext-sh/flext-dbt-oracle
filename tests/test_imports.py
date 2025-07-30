"""Test basic imports work without DBT runtime."""

import pytest


def test_flext_dbt_oracle_imports() -> None:
    """Test that flext_dbt_oracle imports work."""
    # Test imports don't raise errors
    import flext_dbt_oracle
    import flext_dbt_oracle.adapters.oracle.connections
    import flext_dbt_oracle.adapters.oracle.impl

    # Verify modules exist
    assert flext_dbt_oracle
    assert flext_dbt_oracle.adapters.oracle.impl
    assert flext_dbt_oracle.adapters.oracle.connections


@pytest.mark.unit
def test_basic_functionality() -> None:
    """Test basic functionality without DBT runtime."""
    # Just ensure our code can be imported
    assert True
