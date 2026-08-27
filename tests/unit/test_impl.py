"""Behavioral tests for the Oracle table adapter value object.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

# mypy: warn-unused-ignores=False
# Why: pyrefly flags mutation of frozen Pydantic fields, which mypy does not.

from __future__ import annotations

import pytest
from pydantic import ValidationError

from flext_tests import tm
from tests import m

OracleTableAdapter = m.DbtOracle.OracleTableAdapter

__all__: list[str] = ["TestsFlextDbtOracleImpl"]


class TestsFlextDbtOracleImpl:
    """Public-contract behavior of OracleTableAdapter."""

    @pytest.mark.parametrize(
        ("schema_name", "table_name", "expected_relation"),
        [
            ("HR", "EMPLOYEES", "HR.EMPLOYEES"),
            ("SYS", "DUAL", "SYS.DUAL"),
            ("scott", "emp", "scott.emp"),
            ("S", "T", "S.T"),
        ],
    )
    def test_relation_name_is_qualified_schema_dot_table(
        self, schema_name: str, table_name: str, expected_relation: str
    ) -> None:
        """relation_name qualifies the table with its schema."""
        adapter = OracleTableAdapter(schema_name=schema_name, table_name=table_name)

        tm.that(adapter.relation_name, eq=expected_relation)

    def test_public_fields_expose_supplied_values(self) -> None:
        """The constructor arguments are readable as public fields."""
        adapter = OracleTableAdapter(schema_name="HR", table_name="EMPLOYEES")

        tm.that(adapter.schema_name, eq="HR")
        tm.that(adapter.table_name, eq="EMPLOYEES")

    def test_model_dump_by_alias_returns_full_public_contract(self) -> None:
        """model_dump(by_alias=True) surfaces schema, table and computed relation."""
        adapter = OracleTableAdapter(schema_name="HR", table_name="EMPLOYEES")

        tm.that(
            adapter.model_dump(by_alias=True),
            eq={"schema": "HR", "table": "EMPLOYEES", "relation": "HR.EMPLOYEES"},
        )

    def test_dumped_relation_matches_relation_name(self) -> None:
        """model_dump(by_alias=True)['relation'] is consistent with relation_name."""
        adapter = OracleTableAdapter(schema_name="FIN", table_name="LEDGER")

        tm.that(adapter.model_dump(by_alias=True)["relation"], eq=adapter.relation_name)

    def test_model_dump_includes_computed_relation_name(self) -> None:
        """The serialized model carries the computed relation_name."""
        adapter = OracleTableAdapter(schema_name="HR", table_name="JOBS")

        tm.that(
            adapter.model_dump(),
            eq={"schema_name": "HR", "table_name": "JOBS", "relation_name": "HR.JOBS"},
        )

    def test_value_equality_by_public_state(self) -> None:
        """Two adapters with identical fields compare equal."""
        left = OracleTableAdapter(schema_name="HR", table_name="EMP")
        right = OracleTableAdapter(schema_name="HR", table_name="EMP")

        tm.that(left, eq=right)

    def test_distinct_state_is_not_equal(self) -> None:
        """Adapters differing in any field are not equal."""
        base = OracleTableAdapter(schema_name="HR", table_name="EMP")

        tm.that(base, ne=OracleTableAdapter(schema_name="HR", table_name="DEPT"))
        tm.that(base, ne=OracleTableAdapter(schema_name="SYS", table_name="EMP"))

    def test_adapter_is_immutable(self) -> None:
        """Adapter is a frozen value object; mutation is rejected."""
        adapter = OracleTableAdapter(schema_name="HR", table_name="EMP")

        tm.rejects_assignment(adapter, "schema_name", "SYS", expected=ValidationError)

    @pytest.mark.parametrize(
        "kwargs", [{"schema_name": "HR"}, {"table_name": "EMP"}, {}]
    )
    def test_missing_required_field_raises_validation_error(
        self, kwargs: dict[str, str]
    ) -> None:
        """Both schema_name and table_name are mandatory."""
        with pytest.raises(ValidationError):
            OracleTableAdapter(**kwargs)
