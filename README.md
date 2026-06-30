# Playwright + GitHub Copilot + Semgrep Security PoC
![PoC](https://img.shields.io/badge/Project-Proof%20of%20Concept-blue)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-brightgreen)
![GitHub Copilot](https://img.shields.io/badge/GitHub-Copilot-black)
![Semgrep](https://img.shields.io/badge/Semgrep-SAST-red)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF)
![Status](https://img.shields.io/badge/Status-Completed-success)

## Overview

This repository contains a **Proof of Concept (PoC)** demonstrating how **GitHub Copilot**, **Playwright (Python)**, **Semgrep**, and **GitHub Actions** can be integrated to build secure AI-assisted test automation with automated Static Application Security Testing (SAST).

The PoC evaluates the effectiveness of **Semgrep** in detecting security vulnerabilities in AI-generated Python automation code and demonstrates how security validation can be integrated into a modern DevSecOps CI/CD pipeline.

---

# Objectives

This Proof of Concept demonstrates how to:

- Generate a Playwright Python automation framework using GitHub Copilot.
- Implement secure AI coding guardrails for Playwright automation.
- Develop a scalable automation framework using the Page Object Model (POM).
- Execute automated UI tests using Playwright and Pytest.
- Integrate automated security scanning using Semgrep.
- Evaluate Security Audit, OWASP Top 10, and Custom Semgrep rules.
- Detect intentionally introduced security vulnerabilities.
- Validate remediation of identified vulnerabilities.
- Demonstrate secure DevSecOps practices within GitHub Actions.
- Showcase prompt-driven AI-assisted automation development.

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| GitHub Copilot | AI-assisted code generation |
| Model Context Protocol (MCP) | Prompt-driven AI-assisted development |
| Python 3.13 | Programming Language |
| Playwright | Browser Automation Framework |
| Pytest | Test Execution Framework |
| Page Object Model (POM) | Automation Design Pattern |
| python-dotenv | Environment Variable Management |
| GitHub Actions | CI/CD Automation |
| Semgrep | Static Application Security Testing (SAST) |
| Security Audit Rules | General Security Vulnerability Detection |
| OWASP Top 10 Rules | OWASP Security Validation |
| Custom Semgrep Rules | Organization-specific Security Validation |

---

# Repository Structure

```text
playwright-semgrep-security-poc/
│
├── .github/
│   └── workflows/
│       ├── playwright.yml
│       ├── semgrep.yml
│       └── Prompts/
│           ├── playwright_workflow_prompt.md
│           ├── remediation_prompt_semgrep.md
│           └── semgrep_workflow_prompt.md
│
├── data/
│
├── helpers/
│   ├── assertion_helpers.py
│   ├── data_helpers.py
│   ├── wait_helpers.py
│   ├── vulnerable_examples.py
│   └── vulnerable_examples_fixed.py
│
├── pages/
│
├── reports/
│
├── tests/
│   └── specs/
│
├── ai-security.yml
├── conftest.py
├── copilot_instructions.md
├── pytest.ini
├── requirements.txt
├── secure_playwright_test_generation.md
├── README.md
└── .env.example
```

---

# Framework Features

- AI-assisted Playwright framework generation using GitHub Copilot.
- Prompt-driven automation development using MCP concepts.
- Page Object Model (POM) architecture.
- Reusable helper utilities and Pytest fixtures.
- Secure coding guardrails for AI-generated code.
- Environment variable management using `.env`.
- Cross-browser Playwright execution.
- HTML reporting.
- GitHub Actions CI/CD integration.
- Automated Semgrep Static Application Security Testing (SAST).
- Security Audit, OWASP Top 10, and Custom Semgrep rule evaluation.
- Automated validation of vulnerable and remediated code samples.

---

# Project Workflow

```text
                    GitHub Copilot
                           │
                           ▼
          Generate Playwright Automation Framework
                           │
                           ▼
              Playwright Functional Tests
                           │
                           ▼
                 GitHub Actions CI/CD
                           │
          ┌────────────────┴─────────────────┐
          │                                  │
          ▼                                  ▼
 Playwright Test Execution           Semgrep Security Scan
                                             │
                    ┌────────────────────────┼────────────────────────┐
                    │                        │                        │
                    ▼                        ▼                        ▼
            Security Audit          OWASP Top 10 Rules        Custom Rules
                    │                        │                        │
                    └────────────────────────┼────────────────────────┘
                                             │
                                             ▼
                            Security Reports & Validation
```

---

# Prerequisites

- Python 3.13 or later
- Git
- Visual Studio Code
- GitHub Account
- GitHub Copilot
- Playwright
- Semgrep

---

# Getting Started

## Clone Repository

```bash
git clone <repository-url>

cd playwright-semgrep-security-poc
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt

playwright install
```

---

## Configure Environment Variables

Copy the sample environment file.

Windows

```bash
copy .env.example .env
```

Linux/macOS

```bash
cp .env.example .env
```

Update the following variables.

```text
TEST_USERNAME=

TEST_PASSWORD=

STAGING_URL=

PROD_URL=
```

---

# Running Playwright Tests

Run all tests

```bash
pytest
```

Run in headed mode

```bash
pytest --headed
```

Run using Chromium

```bash
pytest --browser chromium
```

Run using Firefox

```bash
pytest --browser firefox
```

Run using WebKit

```bash
pytest --browser webkit
```

Run smoke tests

```bash
pytest -m smoke
```

Run login tests

```bash
pytest -m login
```

---

# Running Semgrep Locally

## Security Audit Rules

```bash
semgrep --config=p/security-audit .
```

---

## OWASP Top 10 Rules

```bash
semgrep --config=p/owasp-top-ten .
```

---

## Custom Security Rules

```bash
semgrep --config ai-security.yml .
```

---

# GitHub Actions Workflows

## Playwright Workflow

Automatically performs the following steps:

- Checkout repository
- Setup Python environment
- Install dependencies
- Install Playwright browsers
- Execute Playwright tests
- Generate HTML reports
- Upload test artifacts

Triggers

- Push
- Pull Request

---

## Semgrep Workflow

Automatically performs the following steps:

- Checkout repository
- Setup Python
- Install Semgrep
- Execute Security Audit scan
- Execute OWASP Top 10 scan
- Execute Custom Rule scan
- Generate security reports
- Upload workflow artifacts

Triggers

- Push
- Pull Request

---

# GitHub Copilot Prompt Files

The repository contains reusable prompts used during the implementation of this Proof of Concept.

| Prompt | Description |
|---------|-------------|
| secure_playwright_test_generation.md | Master GitHub Copilot prompt used to generate the Playwright automation framework from scratch. |
| .github/workflows/Prompts/playwright_workflow_prompt.md | Prompt used to generate the Playwright GitHub Actions workflow. |
| .github/workflows/Prompts/semgrep_workflow_prompt.md | Prompt used to generate the Semgrep GitHub Actions workflow. |
| .github/workflows/Prompts/remediation_prompt_semgrep.md | Prompt used to generate secure remediated code samples. |
| copilot_instructions.md | AI coding guardrails followed during AI-assisted code generation. |

---

# Security Validation

The repository intentionally contains vulnerable code to validate Semgrep security scanning.

## Vulnerable Sample

```text
helpers/vulnerable_examples.py
```

Contains intentionally vulnerable implementations demonstrating:

- Hardcoded credentials
- SQL Injection
- Command Injection
- Weak Cryptography (MD5)
- Unsafe Deserialization using Pickle

These vulnerabilities are expected to be detected by:

- Security Audit Rules
- OWASP Top 10 Rules
- Custom Semgrep Rules

---

## Remediated Sample

```text
helpers/vulnerable_examples_fixed.py
```

Demonstrates secure implementations using:

- Environment Variables
- Parameterized SQL Queries
- Secure subprocess execution
- JSON serialization
- Strong password hashing using `hashlib.scrypt`

The remediated implementation is used to validate successful security remediation.

---

# Reports

## Playwright Reports

Generated locally under:

```text
reports/
```

GitHub Actions uploads the reports as workflow artifacts.

---

## Semgrep Reports

Generated during the GitHub Actions security workflow.

Reports include:

- Security Audit
- OWASP Top 10
- Custom Rule Results

Artifacts are automatically uploaded for every workflow execution.

---

# Required GitHub Secrets

Configure the following GitHub repository secrets.

```text
TEST_USERNAME

TEST_PASSWORD

STAGING_URL

PROD_URL
```

---

# Key Outcomes

This Proof of Concept successfully demonstrates:

- AI-assisted Playwright framework generation using GitHub Copilot.
- Prompt-driven automation development using MCP concepts.
- Secure coding guardrails for AI-generated automation code.
- Automated browser testing using Playwright.
- Integration of Semgrep SAST into GitHub Actions.
- Automated execution of Security Audit, OWASP Top 10, and Custom Rule scans.
- Detection of intentionally introduced security vulnerabilities.
- Validation of remediated secure implementations.
- End-to-end DevSecOps workflow for AI-assisted automation projects.

---

# Future Enhancements

- Integrate Semgrep AppSec Platform.
- Enable Pull Request security annotations.
- Add Software Composition Analysis (SCA).
- Integrate CodeQL and Trivy.
- Expand Playwright test coverage.
- Implement security quality gates.
- Add automated SARIF publishing.
- Integrate security dashboards.

---

# License

This repository is intended for **research, learning, and Proof of Concept purposes**.

The vulnerable sample code included in this repository is intentionally insecure and is provided solely to demonstrate automated security scanning, vulnerability detection, remediation, and validation techniques.

Do **not** use the vulnerable sample code in production applications.