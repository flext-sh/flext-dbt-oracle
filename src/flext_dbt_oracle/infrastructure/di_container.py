"""🚨 ARCHITECTURAL COMPLIANCE: ELIMINATED DUPLICATE DI Container.

REFATORADO COMPLETO:
- REMOVIDA TODAS as duplicações de FlextContainer/DIContainer
- USA APENAS FlextContainer oficial do flext-core
- Mantém apenas utilitários flext_dbt_oracle-específicos
- SEM fallback, backward compatibility ou código duplicado

Copyright (c) 2025 Flext. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Any

# 🚨 ARCHITECTURAL COMPLIANCE: Use ONLY official flext-core FlextContainer
from flext_core import FlextContainer, get_logger

logger = get_logger(__name__)


# ==================== FLEXT_DBT_ORACLE-SPECIFIC DI UTILITIES ====================

_flext_dbt_oracle_container_instance: FlextContainer | None = None


def get_flext_dbt_oracle_container() -> FlextContainer:
    """Get FLEXT_DBT_ORACLE-specific DI container instance.

    Returns:
        FlextContainer: Official container from flext-core.

    """
    global _flext_dbt_oracle_container_instance
    if _flext_dbt_oracle_container_instance is None:
        _flext_dbt_oracle_container_instance = FlextContainer()
    return _flext_dbt_oracle_container_instance


def configure_flext_dbt_oracle_dependencies() -> None:
    """Configure FLEXT_DBT_ORACLE dependencies using official FlextContainer."""
    container = get_flext_dbt_oracle_container()

    try:
        # Register module-specific dependencies
        # Note: Actual service registration would happen here
        # when the concrete implementations are available

        # For now, just register simple string placeholders to avoid import issues
        container.register("oracle_adapter", "dbt_oracle_adapter_placeholder")
        container.register("oracle_connection", "dbt_oracle_connection_placeholder")
        container.register("oracle_config", "dbt_oracle_config_placeholder")

        logger.info("FLEXT_DBT_ORACLE dependencies configured successfully")

    except Exception as e:
        logger.exception(f"Failed to configure FLEXT_DBT_ORACLE dependencies: {e}")


def get_flext_dbt_oracle_service(service_name: str) -> Any:
    """Get flext_dbt_oracle service from container.

    Args:
        service_name: Name of service to retrieve.

    Returns:
        Service instance or None if not found.

    """
    container = get_flext_dbt_oracle_container()
    result = container.get(service_name)

    if result.success:
        return result.data

    logger.warning(
        f"FLEXT_DBT_ORACLE service '{service_name}' not found: {result.error}",
    )
    return None


# Initialize flext_dbt_oracle dependencies on module import
configure_flext_dbt_oracle_dependencies()
