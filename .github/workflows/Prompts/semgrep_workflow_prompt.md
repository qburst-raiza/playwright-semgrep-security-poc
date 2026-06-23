name: semgrep_workflow_prompt.md

description: Generate GitHub Actions workflow for Semgrep security scanning in Playwright Python automation projects.

Act as a Senior DevSecOps Engineer and Semgrep Security Specialist.

Before generating any code:

* Read the repository structure.
* Read copilot_instructions.md.
* Read ai-security.yml.
* Follow all security guardrails defined in the project.

PROJECT CONTEXT

Repository:
playwright-semgrep-security-poc

Technology Stack:

* Python 3.13
* Playwright Python
* Pytest
* Semgrep
* GitHub Actions

OBJECTIVE

Create a GitHub Actions workflow that automatically performs security scanning whenever code is pushed or a Pull Request is created.

Create:

.github/workflows/semgrep.yml

WORKFLOW REQUIREMENTS

Trigger:

* push
* pull_request

Runner:

* ubuntu-latest

Python Version:

* 3.13

STEP 1 – Checkout Repository

Use:

actions/checkout@v4

STEP 2 – Setup Python

Use:

actions/setup-python@v5

Configure:

python-version: "3.13"

STEP 3 – Install Dependencies

Install:

pip install semgrep

STEP 4 – Create Security Report Directory

Create:

reports/security

STEP 5 – Run Security Audit Rules

Execute:

semgrep --config=p/security-audit . --json --output reports/security/security-audit.json

STEP 6 – Run OWASP Top Ten Rules

Execute:

semgrep --config=p/owasp-top-ten . --json --output reports/security/owasp-top-ten.json

STEP 7 – Run Custom Organization Rules

Execute:

semgrep --config ai-security.yml . --json --output reports/security/custom-rules.json

STEP 8 – Upload Security Reports

Use:

actions/upload-artifact@v4

Artifact Name:

semgrep-security-reports

Upload:

reports/security/

Retention:

14 days

STEP 9 – Pipeline Behavior

Requirements:

* Workflow must fail if Semgrep detects blocking vulnerabilities.
* Display findings in workflow logs.
* Produce downloadable artifacts.
* Follow GitHub Actions best practices.

DOCUMENTATION

Add detailed comments explaining:

* Why each step exists.
* What security validation is being performed.
* How the workflow integrates into CI/CD.

SECURITY REQUIREMENTS

Ensure workflow can detect:

* Hardcoded API Keys
* Hardcoded Passwords
* Hardcoded Tokens
* Weak Cryptography (MD5)
* shell=True usage
* Unsafe Pickle Serialization
* Unsafe Pickle Deserialization
* SQL Injection Patterns
* OWASP Top 10 Vulnerabilities

EXPECTED RESULT

Every push or pull request should automatically trigger:

1. Playwright functional validation (existing workflow)
2. Semgrep security validation (new workflow)

The repository should provide continuous functional and security testing through GitHub Actions.

STRICT RULES

* Do not modify existing Playwright workflow.
* Create a separate semgrep.yml workflow.
* Use repository root as scan target.
* Upload reports even if scans fail.
* Generate production-ready GitHub Actions YAML.
