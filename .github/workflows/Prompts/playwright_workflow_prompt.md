---
name: playwright_workflow_prompt.md
description: Use this prompt to generate a GitHub Actions workflow for Playwright Python automation projects, including automated test execution, dependency installation, browser setup, test reporting, and CI/CD integration on code pushes and pull requests.
---

Act as a DevOps Engineer.

Create a GitHub Actions workflow file:

.github/workflows/playwright.yml

Requirements:

Trigger on push
Trigger on pull_request
Use Ubuntu latest runner
Setup Python 3.13
Install dependencies from requirements.txt
Install Playwright browsers
Execute pytest tests
Generate HTML report
Upload report as workflow artifact
Fail workflow if tests fail

Generate production-ready YAML with comments explaining each step.