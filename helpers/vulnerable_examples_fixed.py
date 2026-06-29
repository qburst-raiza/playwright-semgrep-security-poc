"""
REMEDIATED EXAMPLES — SECURE REPLACEMENT FOR vulnerable_examples.py
====================================================================
This file provides secure replacements for all vulnerability patterns found in
helpers/vulnerable_examples.py. Original functionality is preserved wherever
possible. Each remediation is documented inline.

Remediations applied:
    1.  Hardcoded API key        → os.getenv()
    2.  Hardcoded password       → os.getenv()
    3.  Hardcoded auth token     → os.getenv()
    4.  Weak cryptography (MD5)  → hashlib.scrypt() / hashlib.sha256()
    5.  Command injection        → subprocess argument list, shell=False, check=True
    6.  Unsafe serialisation     → json.dumps()
    7.  Unsafe deserialisation   → json.loads()
    8.  SQL injection            → parameterised queries

Compatible with:
    - Semgrep p/security-audit
    - Semgrep p/owasp-top-ten
    - Custom rules defined in ai-security.yml
"""

import hashlib
import json
import os
import sqlite3
import subprocess


# ── 1. HARDCODED API KEY ──────────────────────────────────────────────────────
# REMEDIATION: Load the API key from an environment variable at runtime.
# Never store secret values as literals in source code or commit them to VCS.
# Store the real value in a .env file (excluded from git via .gitignore) or in
# a secrets manager (e.g. AWS Secrets Manager, HashiCorp Vault).
# OWASP A02:2021 — Cryptographic Failures | CWE-798
API_KEY = os.getenv("API_KEY")


def get_api_key() -> str | None:
    # REMEDIATION: Return the value sourced from the environment.
    # Returns None if the variable is not set — callers should validate.
    return API_KEY


# ── 2. HARDCODED PASSWORD ─────────────────────────────────────────────────────
# REMEDIATION: Load the database password from an environment variable.
# Hardcoded credentials are permanently embedded in git history even after
# removal. Environment variables keep secrets out of the codebase entirely.
# OWASP A02:2021 — Cryptographic Failures | CWE-798
DB_PASSWORD = os.getenv("DB_PASSWORD")


def connect_database() -> dict:
    # REMEDIATION: Password is read from the environment, not embedded in code.
    return {"host": "localhost", "password": DB_PASSWORD}


# ── 3. HARDCODED TOKEN ────────────────────────────────────────────────────────
# REMEDIATION: Load the bearer token from an environment variable.
# Tokens grant API access to anyone who reads them; keeping them in env vars
# limits exposure to authorised runtime contexts only.
# OWASP A02:2021 — Cryptographic Failures | CWE-798
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

HEADERS = {
    # REMEDIATION: Reference the environment-sourced variable, not a literal.
    "Authorization": AUTH_TOKEN,
}


# ── 4. WEAK CRYPTOGRAPHY — PASSWORD HASHING ──────────────────────────────────
# REMEDIATION: Replace hashlib.md5() with hashlib.scrypt().
# scrypt is a memory-hard key-derivation function designed for password hashing.
# It is resistant to brute-force and GPU-accelerated attacks.
# A unique random salt is generated per invocation and prepended to the output
# so that identical passwords produce different hashes.
# OWASP A02:2021 — Cryptographic Failures | CWE-327
def hash_password_md5(password: str) -> str:
    # REMEDIATION: Use scrypt with a cryptographically random 16-byte salt.
    # Parameters (NIST / OWASP recommended minimums):
    #   n=16384 — CPU/memory cost factor (must be a power of 2)
    #   r=8     — block size
    #   p=1     — parallelisation factor
    salt = os.urandom(16)
    dk = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1)
    # Store as "salt_hex:derived_key_hex" so the salt can be recovered for verification.
    return salt.hex() + ":" + dk.hex()


# ── 4b. WEAK CRYPTOGRAPHY — INTEGRITY CHECKSUM ───────────────────────────────
# REMEDIATION: Replace hashlib.md5() with hashlib.sha256() for checksums.
# MD5 is collision-prone and must not be used for security-sensitive integrity
# checks. SHA-256 provides 128-bit collision resistance.
# OWASP A02:2021 — Cryptographic Failures | CWE-327
def compute_md5_checksum(data: bytes) -> str:
    # REMEDIATION: Use SHA-256 for data integrity verification.
    return hashlib.sha256(data).hexdigest()


# ── 5. COMMAND INJECTION ──────────────────────────────────────────────────────
# REMEDIATION: Remove shell=True and pass command as an argument list.
# With shell=False (the default), the OS executes the binary directly without
# invoking a shell interpreter, so shell metacharacters (;, |, &&, `) in
# user_input cannot be used to inject additional commands.
# check=True raises CalledProcessError on non-zero exit codes instead of
# silently swallowing failures.
# OWASP A03:2021 — Injection | CWE-78
def run_command(user_input: str) -> str:
    # REMEDIATION: Pass arguments as a list; shell=False is the secure default.
    result = subprocess.run(
        ["echo", user_input],   # Each argument is a separate list element.
        shell=False,            # REMEDIATION: Never use shell=True with user input.
        capture_output=True,
        text=True,
        check=True,             # Raise on non-zero exit code for explicit error handling.
    )
    return result.stdout


def ping_host(hostname: str) -> None:
    # REMEDIATION: Pass ping and its arguments as a list; no shell interpolation.
    subprocess.run(
        ["ping", "-c", "1", hostname],  # hostname is passed as a discrete argument.
        shell=False,                    # REMEDIATION: Eliminates shell injection vector.
        check=True,
    )


# ── 6. UNSAFE SERIALISATION ───────────────────────────────────────────────────
# REMEDIATION: Replace pickle.dumps() with json.dumps().
# JSON serialisation cannot embed executable code; pickle can encode arbitrary
# Python objects including __reduce__ hooks that execute code on deserialisation.
# Only objects with JSON-compatible types (dict, list, str, int, float, bool,
# None) can be serialised with json — this restriction is intentional and safe.
# OWASP A08:2021 — Software and Data Integrity Failures | CWE-502
def serialize_object(obj: object) -> str:
    # REMEDIATION: Use json.dumps() — returns a str instead of bytes.
    # Raises TypeError for non-serialisable types, preventing silent data loss.
    return json.dumps(obj)


# ── 7. UNSAFE DESERIALISATION ─────────────────────────────────────────────────
# REMEDIATION: Replace pickle.loads() with json.loads().
# json.loads() can only reconstruct primitive Python types from a JSON string;
# it cannot execute arbitrary code embedded in the payload.
# OWASP A08:2021 — Software and Data Integrity Failures | CWE-502
def deserialize_object(data: str) -> object:
    # REMEDIATION: Use json.loads() — safe for untrusted input.
    # Note: the parameter type changed from bytes to str to match json.loads().
    return json.loads(data)


# ── 8a. SQL INJECTION — STRING CONCATENATION ─────────────────────────────────
# REMEDIATION: Replace string concatenation with a parameterised query.
# The DB-API 2.0 placeholder (?) causes the database driver to transmit the
# parameter value separately from the SQL statement, making injection impossible
# regardless of what characters username contains.
# OWASP A03:2021 — Injection | CWE-89
def get_user_by_username(username: str) -> list:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # REMEDIATION: Use a parameterised query with a tuple of bind values.
    # The driver handles quoting/escaping; user input never becomes part of SQL text.
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchall()


# ── 8b. SQL INJECTION — F-STRING INTERPOLATION ───────────────────────────────
# REMEDIATION: Replace f-string interpolation with a parameterised query.
# F-string formatting and % formatting are both vulnerable to injection because
# they produce a final SQL string before the DB driver ever sees it.
# OWASP A03:2021 — Injection | CWE-89
def delete_user(user_id: str) -> None:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # REMEDIATION: Pass user_id as a bind parameter, not embedded in the SQL string.
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
