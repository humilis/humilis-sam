"""Fixtures for the integration tests suite."""

import os
from collections import namedtuple

import pytest

from humilis.environment import Environment


@pytest.fixture(scope="session",
                params=["tests/integration/humilis-sam-classic.yaml",
                        "tests/integration/humilis-sam-swagger.yaml"])
def settings(request):
    """Global test settings."""
    Settings = namedtuple('Settings', 'stage update destroy environment_path')
    return Settings(
        stage=os.environ.get("STAGE", "DEV"),
        update=os.environ.get("UPDATE", "yes"),
        destroy=os.environ.get("DESTROY", "yes"),
        environment_path=request.param)


@pytest.yield_fixture(scope="session")
def environment(settings):
    """The test environment: this fixtures creates it and takes care of
    removing it after tests have run."""
    env = Environment(settings.environment_path, stage=settings.stage)
    if settings.update == "yes":
        env.create(update=True)
    else:
        env.create()
    yield env
    if settings.destroy == "yes":
        env.delete()
