"""Oracle DBT Adapter Implementation using FLEXT DB Oracle.

Modern DBT adapter implementation leveraging
flext-infrastructure.databases.flext-db-oracle services
for enterprise-grade Oracle Database integration.
"""

from __future__ import annotations

from typing import Any

# MIGRATED: DBT components now consolidated in flext-meltano
from flext_meltano import BaseConnectionManager, BaseRelation, SQLAdapter

from flext_dbt_oracle.adapters.oracle.connections import OracleConnectionManager


class OracleAdapter(SQLAdapter):
    """Oracle Database adapter for DBT using flext-infrastructure.databases.flext-db-oracle foundation.

    Oracle Database adapter for DBT using
    flext-infrastructure.databases.flext-db-oracle foundation.
    Provides enterprise-grade Oracle Database integration with:
    - Modern connection management via flext-infrastructure.databases.flext-db-oracle
    - Advanced error handling and resilience
    - Enterprise performance optimizations
    - Zero code duplication across FLEXT ecosystem
    """

    ConnectionManager: type[BaseConnectionManager] = OracleConnectionManager  # type: ignore[assignment]

    @classmethod
    def date_function(cls) -> str:
        """Return the Oracle date function."""
        return "SYSDATE"

    @classmethod
    def is_cancelable(cls) -> bool:
        """Oracle connections can be canceled."""
        return True

    # Use parent class quote implementation

    def get_columns_in_relation(self, relation: Any) -> list[Any]:
        """Get columns for a given relation using flext-infrastructure.databases.flext-db-oracle services.

        Get columns for a given relation using
        flext-infrastructure.databases.flext-db-oracle services.
        """
        # Query Oracle's data dictionary - schema/table validated by dbt framework
        # Using parameterized query for security
        sql = """
        SELECT column_name, data_type, nullable, data_default, column_id
        FROM all_tab_columns
        WHERE owner = :schema_name
        AND table_name = :table_name
        ORDER BY column_id
        """
        bindings = {"schema_name": relation.schema, "table_name": relation.identifier}
        _, table = self.execute(sql, bindings, fetch=True)
        return [
            {
                "name": row[0],
                "data_type": row[1],
                "nullable": row[2] == "Y",
                "default": row[3],
                "position": row[4],
            }
            for row in table
        ]

    def list_relations_without_caching(
        self,
        schema_relation: BaseRelation,
    ) -> list[BaseRelation]:
        """List relations in schema without caching using flext-infrastructure.databases.flext-db-oracle services.

        List relations in schema without caching using
        flext-infrastructure.databases.flext-db-oracle services.
        """
        # Query Oracle data dictionary - schema validated by dbt framework
        # Using parameterized query for security
        sql = """
        SELECT table_name, 'table' as relation_type
        FROM all_tables
        WHERE owner = :schema_name
        UNION ALL
        SELECT view_name, 'view' as relation_type
        FROM all_views
        WHERE owner = :schema_name
        """
        bindings = {"schema_name": schema_relation.schema}
        _, table = self.execute(sql, bindings, fetch=True)
        relations = []
        for row in table:
            relation = self.Relation.create(
                database=schema_relation.database,
                schema=schema_relation.schema,
                identifier=row[0],
                type=row[1],
            )
            relations.append(relation)
        return relations

    def check_schema_exists(self, database: str, schema: str) -> bool:
        """Check if schema exists in Oracle using flext-infrastructure.databases.flext-db-oracle services.

        Check if schema exists in Oracle using
        flext-infrastructure.databases.flext-db-oracle services.
        """
        # Query Oracle data dictionary - schema validated and uppercased
        # Using parameterized query for security
        sql = """
        SELECT COUNT(*)
        FROM all_users
        WHERE username = :schema_name
        """
        bindings = {"schema_name": schema.upper()}
        _, table = self.execute(sql, bindings, fetch=True)
        return len(table) > 0 and table[0][0] > 0
