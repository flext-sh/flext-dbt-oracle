"""Configuration for FLEXT DBT Oracle tests.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import os
import tempfile
from collections.abc import Generator
from pathlib import Path

import pytest
from flext_tests import tk


@pytest.fixture(scope="session")
def docker_control() -> tk:
    """Provide tk instance for container management."""
    return tk.shared(
        "flext-oracle-db-test",
        workspace_root=Path(__file__).resolve().parents[2],
    )


@pytest.fixture(scope="session")
def shared_oracle_container(docker_control: tk) -> Generator[str]:
    """Start and maintain flext-oracle-db-test container."""
    result = docker_control.execute()
    if result.failure:
        pytest.skip(f"Failed to start Oracle container: {result.error}")
    resolved_port = next(
        (
            int(host_port)
            for container_port, host_port in result.value.ports.items()
            if container_port.startswith("1521") and host_port.isdigit()
        ),
        1522,
    )
    os.environ.update({
        "DBT_ORACLE_ORACLE_HOST": "localhost",
        "DBT_ORACLE_ORACLE_PORT": str(resolved_port),
        "DBT_ORACLE_ORACLE_USERNAME": "flext_test",
        "DBT_ORACLE_ORACLE_PASSWORD": "flext_test_password",
        "DBT_ORACLE_ORACLE_SERVICE_NAME": "FLEXTDB",
        "DBT_ORACLE_ORACLE_SCHEMA": "FLEXT_TEST",
    })
    yield "flext-oracle-db-test"
    _ = docker_control.down()


@pytest.fixture(scope="session", autouse=True)
def oracle_shared_container_environment(shared_oracle_container: str) -> None:
    """Setup Oracle environment variables for shared container."""
    _ = shared_oracle_container


@pytest.fixture(autouse=True)
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    os.environ["FLEXT_ENV"] = "test"
    os.environ["FLEXT_LOG_LEVEL"] = "debug"
    temp_dir = tempfile.mkdtemp(prefix="dbt_profiles_")
    os.environ["DBT_PROFILES_DIR"] = temp_dir
    os.environ["DBT_TEST_USER_1"] = "dbt_test_user_1"
    os.environ["DBT_TEST_USER_2"] = "dbt_test_user_2"
    os.environ["DBT_TEST_USER_3"] = "dbt_test_user_3"
    yield
    _ = os.environ.pop("FLEXT_ENV", None)
    _ = os.environ.pop("FLEXT_LOG_LEVEL", None)
    _ = os.environ.pop("DBT_PROFILES_DIR", None)
    _ = os.environ.pop("DBT_TEST_USER_1", None)
    _ = os.environ.pop("DBT_TEST_USER_2", None)
    _ = os.environ.pop("DBT_TEST_USER_3", None)
