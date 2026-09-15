"""Environment fixtures for local DBT Oracle configuration and model tests.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from flext_tests import tf

from tests import u

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    with (
        tf().temporary_directory() as temp_dir,
        u.Tests.env_vars_context({
            "FLEXT_ENV": "test",
            "FLEXT_LOG_LEVEL": "debug",
            "DBT_PROFILES_DIR": temp_dir,
            "DBT_TEST_USER_1": "dbt_test_user_1",
            "DBT_TEST_USER_2": "dbt_test_user_2",
            "DBT_TEST_USER_3": "dbt_test_user_3",
        }),
    ):
        yield
