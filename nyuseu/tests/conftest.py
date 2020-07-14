import os
from pathlib import Path

import pytest
import environ


@pytest.fixture
def get_bozo() -> bool:
    """
    put the token of the Joplin WebClipper config page
    :return:
    """
    env_path = Path(__file__).parent.parent / ".env"
    env = environ.Env()
    env.read_env(env_path)
    bozo = os.getenv("BYPASS_BOZO")
    if not bozo:
        raise EnvironmentError("no BYPASS_BOZO set in .env file")
    return bozo
