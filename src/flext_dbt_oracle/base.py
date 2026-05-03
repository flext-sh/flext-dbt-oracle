"""Shared service foundation for flext-dbt-oracle components.

Inherits from FlextMeltanoDbtServiceBase which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-oracle domain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations
