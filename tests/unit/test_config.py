"""Advanced tests for Oracle configuration using FLEXT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_dbt_oracle.settings import FlextDbtOracleSettings
from tests.unit._config_parts.connection import FlextDbtOracleConfigConnectionPart
from tests.unit._config_parts.construction import FlextDbtOracleConfigConstructionPart
from tests.unit._config_parts.validation import FlextDbtOracleConfigValidationPart


class TestsFlextDbtOracleConfig(
    FlextDbtOracleConfigConstructionPart,
    FlextDbtOracleConfigValidationPart,
    FlextDbtOracleConfigConnectionPart,
):
    """Test DBT Oracle configuration functionality."""

    def setup_method(self) -> None:
        """Reset singleton before each test to avoid cross-test pollution."""
        FlextDbtOracleSettings.reset_for_testing()
