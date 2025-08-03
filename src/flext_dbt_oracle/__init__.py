"""FLEXT DBT Oracle - Wrapper for flext-meltano consolidated implementation.

CONSOLIDATION: This project is now a library wrapper that imports the real
Singer/Meltano/DBT consolidated implementations from flext-meltano to eliminate
code duplication across the FLEXT ecosystem.

This follows the architectural principle:
- flext-* projects are LIBRARIES, not services
- tap/target/dbt/ext are Meltano plugins
- Real implementations are in flext-meltano

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano.dbt import (
    FlextMeltanoDbtManager,
    FlextMeltanoDbtProject,
    FlextMeltanoDbtRunner,
)

# Backward compatibility aliases
FlextDbtOracle = FlextMeltanoDbtManager
FlextDbtOracleProject = FlextMeltanoDbtProject
FlextDbtOracleRunner = FlextMeltanoDbtRunner
OracleDBT = FlextMeltanoDbtManager
DBTOracle = FlextMeltanoDbtManager

__version__ = "0.9.0-wrapper"

__all__ = [
    "DBTOracle",
    # Backward compatibility
    "FlextDbtOracle",
    "FlextDbtOracleProject",
    "FlextDbtOracleRunner",
    # Consolidated imports
    "FlextMeltanoDbtManager",
    "FlextMeltanoDbtProject",
    "FlextMeltanoDbtRunner",
    "OracleDBT",
    "__version__",
]
