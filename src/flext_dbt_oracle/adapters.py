"""Oracle Table adapter layer implementing Interface Segregation and Dependency Inversion.

This module creates clean interfaces between flext-dbt-oracle business logic and
the actual FlextDbOracleModels.Table implementation, following SOLID principles.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from flext_core import r, t
from flext_db_oracle.models import FlextDbOracleModels


class FlextDbtOracleAdapters:
    """Unified Oracle table adapter service with interface, adapter, and factory capabilities.

    Consolidates Oracle table adapter functionality including interface definitions,
    adapter pattern implementation, and factory methods following FLEXT unified class pattern.
    """

    class TableInterface(Protocol):
        """Interface defining what flext-dbt-oracle needs from Oracle tables.

        This follows Interface Segregation Principle - only methods we actually need.
        """

        @property
        def name(self: object) -> str:
            """Table name."""

        @property
        def schema_name(self: object) -> str:
            """Schema/owner name."""

        @property
        def columns(self: object) -> list[dict[str, str]]:
            """List of column information as dictionaries."""

        @property
        def metadata(self: object) -> dict[str, t.GeneralValueType]:
            """Table metadata information."""

    @dataclass
    class TableAdapter:
        """Adapter that converts FlextDbOracleModels.Table to our business interface.

        Follows Adapter Pattern (Open/Closed Principle) - extends functionality
        without modifying existing classes.
        """

        _table: FlextDbOracleModels.Table
        _extra_metadata: dict[str, t.GeneralValueType]

        @classmethod
        def create_from_table(
            cls,
            table: FlextDbOracleModels.Table,
            metadata: dict[str, t.GeneralValueType] | None = None,
        ) -> r[FlextDbtOracleAdapters.TableAdapter]:
            """Create adapter from actual Table object with optional metadata.

            Args:
            table: The actual FlextDbOracleModels.Table instance
            metadata: Optional additional metadata

            Returns:
            r containing the adapter

            """
            if not table:
                return r[FlextDbtOracleAdapters.TableAdapter].fail(
                    "Table cannot be None",
                )

            if not table.name:
                return r[FlextDbtOracleAdapters.TableAdapter].fail(
                    "Table name cannot be empty",
                )

            return r[FlextDbtOracleAdapters.TableAdapter].ok(
                cls(
                    _table=table,
                    _extra_metadata=metadata or {},
                ),
            )

        @classmethod
        def create_from_metadata(
            cls,
            name: str,
            schema_name: str,
            columns: list[dict[str, str]] | None = None,
            metadata: dict[str, t.GeneralValueType] | None = None,
        ) -> r[FlextDbtOracleAdapters.TableAdapter]:
            """Create adapter from raw metadata (for cases where we build from scratch).

            Args:
            name: Table name
            schema_name: Schema/owner name
            columns: Column information
            metadata: Additional metadata

            Returns:
            r containing the adapter

            """
            if not name:
                return r[FlextDbtOracleAdapters.TableAdapter].fail(
                    "Table name cannot be empty",
                )

            if not schema_name:
                return r[FlextDbtOracleAdapters.TableAdapter].fail(
                    "Schema name cannot be empty",
                )

            # Create a basic Table object (using actual constructor signature)
            try:
                # Convert column information if provided
                table_columns: list[t.GeneralValueType] = (
                    list(columns) if columns else []
                )

                table = FlextDbOracleModels.Table(
                    name=name,
                    owner=schema_name,  # Use 'owner' not 'schema_name'
                    columns=table_columns,  # Use provided columns
                )
            except Exception as e:
                return r[FlextDbtOracleAdapters.TableAdapter].fail(
                    f"Failed to create Table: {e}",
                )

            return r[FlextDbtOracleAdapters.TableAdapter].ok(
                cls(
                    _table=table,
                    _extra_metadata=metadata or {},
                ),
            )

        @property
        def name(self: object) -> str:
            """Table name from the adapted table."""
            return self._table.name

        @property
        def schema_name(self: object) -> str:
            """Schema name (mapped from 'owner' attribute)."""
            return self._table.owner

        @property
        def columns(self: object) -> list[dict[str, str]]:
            """Column information converted to dictionaries."""
            # Convert Column objects to dictionaries for business logic compatibility
            return [
                {
                    "name": col.name if hasattr(col, "name") else str(col),
                    "data_type": getattr(col, "data_type", "UNKNOWN"),
                    "nullable": str(getattr(col, "nullable", True)),
                }
                for col in self._table.columns
            ]

        @property
        def metadata(self: object) -> dict[str, t.GeneralValueType]:
            """Combined metadata from table and extra metadata."""
            base_metadata = {
                "name": self.name,
                "owner": self.schema_name,
                "column_count": len(self._table.columns),
            }
            # Merge with extra metadata
            return {**base_metadata, **self._extra_metadata}

        def get_underlying_table(self: object) -> FlextDbOracleModels.Table:
            """Get the underlying Table object for operations that need it."""
            return self._table

    class TableFactory:
        """Factory for creating table adapters with different strategies.

        Follows Factory Pattern and Single Responsibility Principle.
        """

        @staticmethod
        def from_api_response(
            table_name: str,
            api_response: dict[str, t.GeneralValueType],
            schema_name: str | None = None,
        ) -> r[FlextDbtOracleAdapters.TableAdapter]:
            """Create table adapter from Oracle API response.

            Args:
            table_name: Name of the table
            api_response: Dictionary response from Oracle API
            schema_name: Optional schema name (inferred if not provided)

            Returns:
            r containing the table adapter

            """
            if not table_name:
                return r[FlextDbtOracleAdapters.TableAdapter].fail(
                    "Table name required",
                )

            if not isinstance(api_response, dict):
                return r[FlextDbtOracleAdapters.TableAdapter].fail(
                    "API response must be a dictionary",
                )

            # Extract schema name from response if not provided
            effective_schema_name = schema_name or api_response.get(
                "owner",
                str(api_response.get("schema_name", "USER")),
            )

            # Extract column information if available
            columns = []
            if "columns" in api_response and isinstance(api_response["columns"], list):
                columns = [
                    {
                        "name": col.get("name", "UNKNOWN"),
                        "data_type": col.get("data_type", "UNKNOWN"),
                        "nullable": str(col.get("nullable", True)),
                    }
                    for col in api_response["columns"]
                    if isinstance(col, dict)
                ]

            return FlextDbtOracleAdapters.TableAdapter.create_from_metadata(
                name=table_name,
                schema_name=effective_schema_name,
                columns=columns,
                metadata=dict(api_response),
            )

        @staticmethod
        def from_table_list(
            table_names: list[str],
            schema_name: str = "USER",
        ) -> r[list[FlextDbtOracleAdapters.TableAdapter]]:
            """Create table adapters from a list of table names.

            Args:
            table_names: List of table names
            schema_name: Schema name for all tables

            Returns:
            r containing list of table adapters

            """
            if not table_names:
                return r[list[FlextDbtOracleAdapters.TableAdapter]].ok([])

            adapters: list[FlextDbtOracleAdapters.TableAdapter] = []
            for table_name in table_names:
                if isinstance(table_name, str) and table_name.strip():
                    adapter_result = (
                        FlextDbtOracleAdapters.TableAdapter.create_from_metadata(
                            name=table_name.strip(),
                            schema_name=schema_name,
                            columns=[],
                            metadata={},
                        )
                    )
                    if adapter_result.is_success:
                        adapters.append(adapter_result.value)
                    else:
                        return r[list[FlextDbtOracleAdapters.TableAdapter]].fail(
                            f"Failed to create adapter for table {table_name}: {adapter_result.error}",
                        )

            return r[list[FlextDbtOracleAdapters.TableAdapter]].ok(adapters)


# Type classes with real inheritance for backward compatibility
class OracleTableAdapter(FlextDbtOracleAdapters.TableAdapter):
    """OracleTableAdapter - real inheritance from FlextDbtOracleAdapters.TableAdapter."""


class OracleTableFactory(FlextDbtOracleAdapters.TableFactory):
    """OracleTableFactory - real inheritance from FlextDbtOracleAdapters.TableFactory."""


__all__: list[str] = [
    "FlextDbtOracleAdapters",
    "OracleTableAdapter",
    "OracleTableFactory",
]
