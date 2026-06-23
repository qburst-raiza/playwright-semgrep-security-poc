import os
import pytest
from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging", help="Target environment")


@pytest.fixture(scope="session")
def base_url(pytestconfig) -> str:
    env = pytestconfig.getoption("--env")
    urls = {
        "staging": os.getenv("STAGING_URL", "https://staging.example.com"),
        "production": os.getenv("PROD_URL", "https://example.com"),
    }
    return urls.get(env, urls["staging"])


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, base_url):
    """
    Configure Playwright browser context.

    Guardrails:
    - Base URL comes from environment variables.
    - Video recording can be enabled through RECORD_VIDEO.
    - No hardcoded secrets.
    """

    return {
        **browser_context_args,
        "base_url": base_url,
        "viewport": {
            "width": 1280,
            "height": 720,
        },
        "record_video_dir": (
            "reports/videos/"
            if os.getenv("RECORD_VIDEO", "false").lower() == "true"
            else None
        ),
    }


