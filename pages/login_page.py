# Guardrail: Use Page Object Model.
# All locators and interactions are encapsulated here.
# Tests must never contain raw Playwright locator calls.
from playwright.sync_api import Page, expect


class LoginPage:
    # Guardrail: No hardcoded base URL.
    # URL is relative; the base_url is injected by the pytest-playwright fixture
    # which reads STAGING_URL from the .env file via conftest.py.
    # SauceDemo's login form lives at the root path.
    URL = "/"

    def __init__(self, page: Page) -> None:
        self.page = page

        # Guardrail: No XPath locators.
        # Locator strategy: get_by_placeholder() is chosen because SauceDemo's
        # username and password <input> elements have no associated <label> elements,
        # making get_by_label() unavailable. Placeholder text is the next semantic
        # option in the priority order (role > label > placeholder > text > testid > CSS).
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")

        # Guardrail: No XPath locators.
        # Locator strategy: get_by_role() is the highest-priority semantic locator.
        # The submit button carries role="button" and accessible name "Login".
        self.login_button = page.get_by_role("button", name="Login")

        # CSS selector used here because .inventory_list is a structural container
        # with no ARIA role or accessible name to target semantically.
        # CSS is acceptable as a last resort per the locator priority rules.
        # This element is only rendered on /inventory.html after a successful login,
        # making it a reliable post-login assertion target.
        self.inventory_list = page.locator(".inventory_list")

        # [data-test="error"] is SauceDemo's error container attribute.
        # CSS attribute selector is used; no semantic alternative exists here.
        self.error_message = page.locator("[data-test='error']")

    def navigate(self) -> None:
        """Navigate to the SauceDemo login page.

        Guardrail: No hardcoded URL -- goto() uses the relative path combined with
        the base_url set in browser context args from the .env STAGING_URL value.
        """
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        """Fill in credentials and submit the login form.

        Guardrail: No hardcoded credentials.
        username and password are passed as parameters and must originate from
        environment variables at the call site (via get_env() in test files).

        Guardrail: No sleep() or wait_for_timeout().
        Playwright auto-waits for elements to be actionable before fill() and click().
        """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def is_login_successful(self) -> bool:
        """Return True if the inventory list is visible after login.

        Guardrail: No sleep() or wait_for_timeout().
        Playwright's is_visible() uses the element's current visibility state;
        Playwright's auto-waiting in login() ensures navigation has settled.

        .inventory_list is only present on /inventory.html, confirming a successful
        login redirect. This is the verification element specified in requirements.
        """
        return self.inventory_list.is_visible()

    def expect_login_successful(self) -> None:
        """Assert that the inventory list is visible using a Playwright assertion."""
        expect(self.inventory_list).to_be_visible()

    def expect_error_message(self, message: str) -> None:
        """Assert that an error banner with the given text is visible."""
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(message)
