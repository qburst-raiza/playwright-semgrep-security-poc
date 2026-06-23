# Playwright Python Automation Framework

A test automation framework built with Playwright, Pytest, and the Page Object Model pattern.

## Tech Stack

- [Playwright for Python](https://playwright.dev/python/) — browser automation
- [Pytest](https://pytest.org/) — test runner
- [pytest-playwright](https://playwright.dev/python/docs/test-runners) — Playwright pytest plugin
- [pytest-html](https://pytest-html.readthedocs.io/) — HTML reporting
- [python-dotenv](https://github.com/theskumar/python-dotenv) — environment variable management

## Project Structure

```
playwright-mcp-poc/
├── tests/specs/          # Test specifications
├── pages/                # Page Object Model classes
├── helpers/              # Reusable utilities
├── data/                 # Test data (JSON)
├── .github/workflows/    # GitHub Actions CI
├── conftest.py           # Pytest fixtures
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Python dependencies
└── .env.example          # Environment variable template
```

## Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 3. Configure environment variables

```bash
cp .env.example .env
# Edit .env with your actual values
```

## Running Tests

```bash
# Run all tests (headless, default browser: chromium)
pytest

# Run in headed mode
pytest --headed

# Run against a specific browser
pytest --browser firefox
pytest --browser webkit

# Run a specific marker
pytest -m smoke
pytest -m login

# Run against a specific environment
pytest --env production

# Run in parallel
pytest -n auto
```

## Reporting

HTML reports are generated automatically in `reports/report.html` after each run.

## CI/CD

Tests run automatically on push/PR to `main` and `develop` branches via GitHub Actions across Chromium, Firefox, and WebKit. Test reports are uploaded as artifacts.

Required GitHub secrets:
- `STAGING_URL`
- `PROD_URL`
- `TEST_USERNAME`
- `TEST_PASSWORD`
