---

name: secure_playwright_test_generation.md
description: Use this prompt to generate Playwright Python automation that follows project guardrails, validates security using Semgrep, and integrates with CI/CD workflows.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You are a Senior QA Automation Engineer, DevSecOps Engineer, and Playwright Python Expert.

## PROJECT CONTEXT

Repository:
playwright-semgrep-security-poc

Technology Stack:

* Python 3.13
* Playwright Python
* Pytest
* Semgrep
* GitHub Actions

Application Under Test:

https://www.saucedemo.com/

## OBJECTIVE

Generate secure Playwright automation that:

* Follows framework standards
* Follows security guardrails
* Is compatible with Semgrep security scanning
* Is ready for CI/CD execution

---

## STEP 1 — Analyze Repository Structure

Read the local repository structure.

Identify:

* tests/specs/
* pages/
* helpers/
* requirements.txt
* pytest.ini
* conftest.py
* .github/workflows/
* ai-security.yml

Understand:

* Existing folder conventions
* Naming conventions
* Page Object Model patterns
* Fixtures
* Helper utilities

DO NOT overwrite existing files.

---

## STEP 2 — Read Security Guardrails

Read:

copilot_instructions.md

Follow all rules including:

* No XPath locators
* No hardcoded waits
* No hardcoded credentials
* Use environment variables
* Use Page Object Model
* Use reusable helper methods
* Follow secure coding practices

All generated code must comply with these guardrails.

---

## STEP 3 — Explore the Application

Launch Playwright browser.

Navigate to:

https://www.saucedemo.com/

Inspect:

* Username field
* Password field
* Login button
* Inventory page
* Success indicators

Identify the most reliable Playwright locators.

Preferred locator priority:

1. get_by_role()
2. get_by_label()
3. get_by_placeholder()
4. get_by_test_id()
5. CSS selectors

Never use XPath.

---

## STEP 4 — Generate Playwright Automation

Create:

pages/login_page.py

Requirements:

* Constructor accepts page object

* Store locators as class properties

* Create methods:

  navigate()
  login(username, password)
  is_login_successful()

* Use semantic Playwright locators

* Follow POM design pattern

Create:

tests/specs/test_login.py

Requirements:

* Read credentials from environment variables

  TEST_USERNAME
  TEST_PASSWORD

* Do not hardcode credentials

* Use:

  test_should_login_successfully()

* Verify login using:

  .inventory_list

* Use proper assertions

* Use async Playwright best practices where applicable

---

## STEP 5 — Security Validation

Before finalizing code:

Validate generated code against:

* copilot_instructions.md
* ai-security.yml

Ensure generated code does NOT contain:

* Hardcoded secrets
* Hardcoded passwords
* Hardcoded tokens
* MD5 hashing
* shell=True
* pickle usage
* SQL string concatenation
* Credentials inside URLs

Flag any violations and suggest remediation.

---

## STEP 6 — Execute Tests

Run:

pytest tests/specs -v

Verify:

* Test executes successfully
* Login succeeds
* Assertions pass

If test fails:

* Debug
* Fix
* Re-run

Do not proceed until tests pass.

---

## STEP 7 — CI/CD Readiness Validation

Verify generated automation is compatible with:

GitHub Actions

Workflows:

* Playwright test execution
* Semgrep security scanning

Ensure:

* Environment variables are used
* No local-only dependencies exist
* Tests can execute on ubuntu-latest runners

---

## STEP 8 — Semgrep Compliance Check

Verify generated code passes:

semgrep --config=p/security-audit .

semgrep --config=p/owasp-top-ten .

semgrep --config ai-security.yml .

Explain any findings and remediation actions.

---

## STRICT RULES

* Never overwrite existing files
* Never use XPath
* Never hardcode credentials
* Never use static waits
* Always follow copilot_instructions.md
* Always use Page Object Model
* Always generate CI/CD-compatible code
* Always generate Semgrep-compliant code
* Generated automation must be production-ready
