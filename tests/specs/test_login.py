# Guardrail: Use Page Object Model.
# No raw Playwright locator calls appear in this file.
# All browser interactions are delegated to LoginPage.
#
# Guardrail: No hardcoded credentials.
# TEST_USERNAME and TEST_PASSWORD are loaded from the .env file at runtime
# via get_env() in helpers/data_helpers.py. This keeps secrets out of source
# control and allows CI/CD to inject them as GitHub Actions secrets.
import pytest
from pages.login_page import LoginPage
from helpers.data_helpers import get_env


@pytest.mark.login
@pytest.mark.smoke
class TestLogin:

    def test_should_login_successfully(self, page):
        """Verify that a valid user can log in to SauceDemo and reach the inventory page.

        Steps:
            1. Open SauceDemo (base_url resolves to https://www.saucedemo.com via .env).
            2. Read credentials from environment variables -- never from source code.
            3. Log in using LoginPage (Page Object Model).
            4. Assert the inventory list is visible, confirming a successful login.

        Guardrail: No sleep() or wait_for_timeout().
            Playwright's auto-waiting handles all navigation and element readiness.

        Guardrail: No XPath locators.
            All locator logic is inside LoginPage using semantic Playwright locators.

        Guardrail: Use environment variables.
            get_env() reads from .env via python-dotenv -- never os.getenv() directly
            in a test file.
        """
        # Guardrail: No hardcoded credentials.
        # TEST_USERNAME and TEST_PASSWORD must be set in .env (see .env.example).
        # In CI, they are injected as repository secrets via GitHub Actions.
        username = get_env("TEST_USERNAME")
        password = get_env("TEST_PASSWORD")

        login_page = LoginPage(page)

        # Navigate to SauceDemo -- base_url is set from STAGING_URL in .env.
        login_page.navigate()

        # Guardrail: Page Object Model -- login() encapsulates all field interactions.
        # Guardrail: No hardcoded credentials -- username and password come from env vars above.
        login_page.login(username, password)

        # Assert successful login by checking .inventory_list visibility.
        # .inventory_list is only rendered on /inventory.html after a valid login,
        # making it a definitive confirmation of authentication success.
        # Guardrail: No sleep() -- Playwright's built-in waiting is used inside is_login_successful().
        assert login_page.is_login_successful(), (
            "Login failed: .inventory_list is not visible after login attempt. "
            "Verify TEST_USERNAME and TEST_PASSWORD are correctly set in .env."
        )
