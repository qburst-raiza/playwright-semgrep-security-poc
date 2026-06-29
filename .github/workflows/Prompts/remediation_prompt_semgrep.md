---
name: remediation_prompt_semgrep.md
description: Generate a secure remediated version of intentionally vulnerable Python code by replacing insecure coding patterns with security best practices and ensuring Semgrep compliance.
---

Act as a Senior Application Security Engineer and Python Developer.

Before generating any code:

Read helpers/vulnerable_examples.py.
Preserve the original functionality wherever possible.
Create a new file. Do not modify the original vulnerable file.

Create:

helpers/vulnerable_examples_fixed.py
Apply the following remediations:
Hardcoded API Keys
Replace with os.getenv().
Hardcoded Passwords
Replace with environment variables.
Hardcoded Authentication Tokens
Replace with environment variables.
Weak Cryptography
Replace hashlib.md5() with hashlib.scrypt().
Command Injection
Replace subprocess.run(..., shell=True) with secure subprocess execution using argument lists and check=True.
Unsafe Serialization
Replace pickle.dumps() with json.dumps().
Unsafe Deserialization
Replace pickle.loads() with json.loads().
SQL Injection
Replace SQL string concatenation and formatted queries with parameterized queries.
Additional Requirements
Add comments explaining each remediation.
Follow Python coding standards.
Do not introduce new security vulnerabilities.
Ensure the generated code is compatible with:
Semgrep Security Audit Rules (p/security-audit)
OWASP Top 10 Rules (p/owasp-top-ten)
Custom rules defined in ai-security.yml
Ensure the code is suitable for CI/CD environments and secure coding best practices.
Expected Output

Generate only:

helpers/vulnerable_examples_fixed.py

The generated file should significantly reduce or eliminate the security findings reported by Semgrep while preserving the original intent of the sample code.