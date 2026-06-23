# Copilot Instructions -- Playwright Python Framework

## Purpose

Ensure all AI-generated Playwright Python automation code follows approved engineering and security standards. These rules are non-negotiable guardrails -- they apply to every file generated or modified in this project.

---

## Guardrails

### No Hardcoded Credentials
- Never embed usernames, passwords, tokens, API keys, or any secret values in source code or committed data files.
- Load all credentials exclusively from environment variables via `helpers/data_helpers.py` -> `get_env()` or pytest fixtures backed by `python-dotenv`.
- Reference `.env.example` as the template; the real `.env` file must never be committed.

```python
# WRONG
page.fill("#password", "secret_sauce")

# CORRECT
password = get_env("TEST_PASSWORD")
page.fill("#password", password)
```

### Use Environment Variables
- All environment-specific values (base URLs, credentials, feature flags) must come from `.env` via `os.getenv()` wrapped in `helpers/data_helpers.py`.
- Never call `os.getenv()` directly inside test files; use the `base_url` fixture or `get_env()` helper.
- CI/CD secrets are injected as GitHub Actions secrets -- never print or log secret values.

### No XPath Locators
- XPath locators are brittle, unreadable, and tightly coupled to DOM structure. Do not generate them.
- CSS selectors are acceptable only when no semantic locator is available.

```python
# WRONG
page.locator("//input[@id='username']")
page.locator("//div[contains(@class,'btn')]/span")

# CORRECT
page.get_by_label("Username")
page.get_by_role("button", name="Login")
```

### Use Playwright Semantic Locators
Apply locators in this strict priority order:

| Priority | Locator | When to use |
|----------|---------|-------------|
| 1 | `get_by_role()` | Buttons, links, headings, inputs with ARIA roles |
| 2 | `get_by_label()` | Form fields associated with a `<label>` |
| 3 | `get_by_placeholder()` | Inputs identified by placeholder text |
| 4 | `get_by_text()` | Non-interactive text content |
| 5 | `get_by_test_id()` | Elements with `data-testid` attributes |
| 6 | CSS selector | Only when none of the above apply |

### No `sleep()` or `wait_for_timeout()`
- `time.sleep()` and `page.wait_for_timeout()` are unconditional pauses that make tests slow and flaky. They are banned.
- Use Playwright's auto-waiting and explicit condition-based waits from `helpers/wait_helpers.py`.

```python
# WRONG
import time
time.sleep(3)
page.wait_for_timeout(2000)

# CORRECT
from helpers.wait_helpers import wait_for_selector, wait_for_network_idle
wait_for_selector(page, "[data-testid='dashboard']")
wait_for_network_idle(page)
```

### Use Page Object Model
- Every page or major UI component must have a corresponding class in `pages/`.
- Page classes encapsulate locators and interactions -- tests must not contain raw locator calls.
- Keep interaction methods (click, fill, navigate) separate from assertion methods (`expect_*`).

```python
# WRONG -- locator defined directly in test
def test_login(page):
    page.get_by_label("Username").fill("user")
    page.get_by_label("Password").fill("pass")
    page.get_by_role("button", name="Login").click()

# CORRECT -- delegate to Page Object
def test_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(get_env("TEST_USERNAME"), get_env("TEST_PASSWORD"))
    login_page.expect_login_successful()
```

### Follow Secure Coding Practices
- Do not log, print, or expose credentials, tokens, or PII at any point during test execution.
- Do not disable TLS/SSL verification (`verify=False`, `ignore_https_errors=True`) unless explicitly required and approved.
- Do not commit `.env`, secrets, or any file containing real credentials.
- Sanitise any dynamic input used in selectors to avoid selector-injection risks.
- Keep dependencies pinned in `requirements.txt` and updated regularly.

### Use Reusable Helpers
- Do not duplicate wait logic, assertion logic, or data-loading logic across test files.
- Import from the established helpers:

| Helper | Purpose |
|--------|---------|
| `helpers/wait_helpers.py` | All explicit waits |
| `helpers/assertion_helpers.py` | Reusable `expect()` wrappers |
| `helpers/data_helpers.py` | JSON test data and env var access |

- If a utility is needed in more than one test, it belongs in a helper -- not inline.

---

## Code Conventions

### Page Objects (`pages/`)
- One class per page or major component.
- Constructor receives `page: Page` and defines all locators as instance attributes.
- Navigation and interaction methods must not contain assertions.
- Add `expect_*` methods for state-specific assertions.

### Tests (`tests/specs/`)
- Group related tests in a class prefixed with `Test`.
- Each test must be independent and idempotent (no shared mutable state).
- Use `get_test_data()` for all test data -- never hardcode values.
- Apply pytest markers to classify tests: `@pytest.mark.smoke`, `@pytest.mark.regression`, `@pytest.mark.login`.

### Fixtures (`conftest.py`)
- Session-scoped fixtures for expensive setup (browser, base URL).
- Function-scoped `page` fixture for test isolation.
- All environment-specific config is injected via fixtures.

---

## Python Naming Conventions

| Artifact | Convention | Example |
|----------|------------|---------|
| Test files | `test_<feature>.py` | `test_login.py` |
| Page classes | `<Name>Page` | `LoginPage` |
| Test classes | `Test<Feature>` | `TestLogin` |
| Test methods | `test_<scenario>` | `test_valid_login` |
| Helper functions | `snake_case` | `wait_for_selector` |
| Fixtures | `snake_case` | `base_url` |
| Constants | `UPPER_SNAKE_CASE` | `DEFAULT_TIMEOUT` |
| Local variables | `snake_case` | `login_page` |

---

## Absolute Rules -- Never Do These

| Rule | Reason |
|------|--------|
| No `time.sleep()` or `wait_for_timeout()` | Causes flaky, slow tests |
| No XPath locators | Brittle and DOM-coupled |
| No hardcoded credentials | Security risk; secrets must not be in source |
| No `os.getenv()` inside test files | Bypass of fixture-managed config |
| No broad `except Exception` to hide failures | Masks real failures |
| No hardcoded base URLs | Breaks environment portability |
| No committing `.env` files | Exposes secrets in version control |
