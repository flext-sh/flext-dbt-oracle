"""Configuration for FLEXT DBT Oracle tests.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from flext_tests import tf, tk

from flext_dbt_oracle import t
from tests import u

if TYPE_CHECKING:
    from collections.abc import Generator


_ENV_BACKUP: t.MutableMappingKV[str, str | None] = {}


def pytest_sessionstart(session: pytest.Session) -> None:
    """Start Oracle container and configure session environment variables."""
    _ = session
    docker_control = tk.shared(
        "flext-oracle-db-test",
        workspace_root=Path(__file__).resolve().parents[2],
    )
    result = docker_control.execute()
    if result.failure:
        pytest.skip(
            f"Failed to start Oracle container: {result.error}",
            allow_module_level=True,
        )
    resolved_port = next(
        (
            int(host_port)
            for container_port, host_port in result.value.ports.items()
            if container_port.startswith("1521") and host_port.isdigit()
        ),
        1522,
    )
    env_vars = {
        "DBT_ORACLE_ORACLE_HOST": "localhost",
        "DBT_ORACLE_ORACLE_PORT": str(resolved_port),
        "DBT_ORACLE_ORACLE_USERNAME": "flext_test",
        "DBT_ORACLE_ORACLE_PASSWORD": "flext_test_password",
        "DBT_ORACLE_ORACLE_SERVICE_NAME": "FLEXTDB",
        "DBT_ORACLE_ORACLE_SCHEMA": "FLEXT_TEST",
    }
    for key, value in env_vars.items():
        _ENV_BACKUP[key] = os.environ.get(key)
        os.environ[key] = value


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    """Restore environment variables and stop the Oracle container."""
    _ = session
    _ = exitstatus
    for key, original in _ENV_BACKUP.items():
        if original is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = original

    docker_control = tk.shared(
        "flext-oracle-db-test",
        workspace_root=Path(__file__).resolve().parents[2],
    )
    _ = docker_control.down()


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
