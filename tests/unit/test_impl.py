"""Tests for Oracle adapter helpers and table factory.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_dbt_oracle.adapters import OracleTableAdapter, OracleTableFactory


class TestOracleTableAdapter:
    """Test OracleTableAdapter."""

    def test_get_relation_name(self) -> None:
        adapter = OracleTableAdapter(schema_name="HR", table_name="EMPLOYEES")
        assert adapter.get_relation_name() == "HR.EMPLOYEES"

    def test_to_metadata(self) -> None:
        adapter = OracleTableAdapter(schema_name="HR", table_name="EMPLOYEES")
        meta = adapter.to_metadata()
        assert meta["schema"] == "HR"
        assert meta["table"] == "EMPLOYEES"
        assert meta["relation"] == "HR.EMPLOYEES"

    def test_dataclass_slots(self) -> None:
        adapter = OracleTableAdapter(schema_name="SYS", table_name="DUAL")
        assert adapter.schema_name == "SYS"
        assert adapter.table_name == "DUAL"


class TestOracleTableFactory:
    """Test OracleTableFactory."""

    def test_create_basic(self) -> None:
        adapter = OracleTableFactory.create("HR", "EMPLOYEES")
        assert isinstance(adapter, OracleTableAdapter)
        assert adapter.schema_name == "HR"
        assert adapter.table_name == "EMPLOYEES"

    def test_create_trims_whitespace(self) -> None:
        adapter = OracleTableFactory.create("  HR  ", "  EMPLOYEES  ")
        assert adapter.schema_name == "HR"
        assert adapter.table_name == "EMPLOYEES"

    def test_create_empty_schema_defaults_to_public(self) -> None:
        adapter = OracleTableFactory.create("", "EMPLOYEES")
        assert adapter.schema_name == "public"

    def test_create_whitespace_schema_defaults_to_public(self) -> None:
        adapter = OracleTableFactory.create("   ", "EMPLOYEES")
        assert adapter.schema_name == "public"
