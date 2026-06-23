"""
INTENTIONALLY VULNERABLE EXAMPLES — FOR SEMGREP EVALUATION ONLY
================================================================
This file contains deliberately insecure code patterns used solely to verify
that Semgrep (or another SAST tool) correctly detects the following rule categories:

    - python.lang.security.hardcoded-api-key
    - python.lang.security.hardcoded-password
    - python.lang.security.hardcoded-token
    - python.lang.security.insecure-hash-algorithms
    - python.lang.security.subprocess-shell-true
    - python.lang.security.insecure-pickle

DO NOT use any of the code in this file in production or any real application.
DO NOT store real secrets here — all values below are synthetic placeholders.
"""

import hashlib
import pickle
import subprocess
import sqlite3


# ── 1. HARDCODED API KEY ──────────────────────────────────────────────────────
# VULN: API key embedded directly in source code.
# Semgrep rule: generic.secrets.security.detected-generic-api-key
# Risk: Key is exposed in version control and to anyone with read access to the repo.
API_KEY = "AIzaSyD-INTENTIONALLY_FAKE_KEY_FOR_SEMGREP_TEST_1234567890abcdef"  # noqa: S105


def get_api_key():
    # VULN: Returning hardcoded secret from a function — Semgrep flags this pattern.
    return API_KEY


# ── 2. HARDCODED PASSWORD ─────────────────────────────────────────────────────
# VULN: Password literal assigned to a variable named 'password'.
# Semgrep rule: python.lang.security.audit.hardcoded-password-string
# Risk: Anyone with source access obtains the credential in plaintext.
DB_PASSWORD = "S3cr3tP@ssw0rd_SEMGREP_TEST"  # noqa: S105


def connect_database():
    # VULN: Hardcoded password passed directly to a connection call.
    return {"host": "localhost", "password": DB_PASSWORD}


# ── 3. HARDCODED TOKEN ────────────────────────────────────────────────────────
# VULN: Bearer token literal in source.
# Semgrep rule: generic.secrets.security.detected-generic-secret
# Risk: Token grants API access to anyone who reads this file.
AUTH_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.SEMGREP_TEST_FAKE_TOKEN.signature"  # noqa: S105

HEADERS = {
    "Authorization": AUTH_TOKEN,  # VULN: Hardcoded bearer token in headers dict.
}


# ── 4. MD5 HASHING ────────────────────────────────────────────────────────────
# VULN: MD5 is cryptographically broken and must not be used for password hashing
#       or integrity verification of security-sensitive data.
# Semgrep rule: python.lang.security.audit.md5-used
# Risk: Collision attacks and rainbow tables render MD5 trivially reversible.
def hash_password_md5(password: str) -> str:
    # VULN: Using MD5 to hash a password — should use bcrypt, argon2, or scrypt.
    return hashlib.md5(password.encode()).hexdigest()  # noqa: S324


def compute_md5_checksum(data: bytes) -> str:
    # VULN: MD5 used for integrity check — SHA-256 or SHA-3 should be used instead.
    return hashlib.md5(data).hexdigest()  # noqa: S324


# ── 5. SUBPROCESS WITH shell=True ────────────────────────────────────────────
# VULN: shell=True passes the command string to the OS shell, enabling
#       command injection if any part of the string is derived from user input.
# Semgrep rule: python.lang.security.audit.subprocess-shell-true
# Risk: An attacker can inject shell metacharacters (;, |, &&, `) to execute
#       arbitrary commands on the host OS.
def run_command(user_input: str) -> str:
    # VULN: user_input is interpolated into a shell command — command injection risk.
    result = subprocess.run(  # noqa: S602
        f"echo {user_input}",
        shell=True,           # VULN: shell=True enables injection
        capture_output=True,
        text=True,
    )
    return result.stdout


def ping_host(hostname: str) -> None:
    # VULN: shell=True with a formatted string — classic injection vector.
    subprocess.call(f"ping -c 1 {hostname}", shell=True)  # noqa: S602, S603


# ── 6. PICKLE SERIALIZATION ───────────────────────────────────────────────────
# VULN: pickle.dumps() serialises arbitrary Python objects.
#       If the serialised output is stored or transmitted and later deserialised
#       from an untrusted source, it allows remote code execution.
# Semgrep rule: python.lang.security.audit.pickle
# Risk: Pickle data can encode __reduce__ methods that execute arbitrary code
#       when unpickled.
def serialize_object(obj: object) -> bytes:
    # VULN: Serialising to pickle format — use JSON or msgpack for safe serialisation.
    return pickle.dumps(obj)  # noqa: S301


# ── 7. PICKLE DESERIALIZATION ─────────────────────────────────────────────────
# VULN: pickle.loads() on data from any external or untrusted source allows
#       remote code execution. This is one of the most critical Python security flaws.
# Semgrep rule: python.lang.security.audit.pickle
# Risk: A crafted pickle payload can call os.system(), subprocess, or exec() during
#       deserialization, giving an attacker full code execution.
def deserialize_object(data: bytes) -> object:
    # VULN: Never unpickle data received from a network socket, file, or user input.
    return pickle.loads(data)  # noqa: S301


# ── 8. SQL QUERY CONCATENATION ───────────────────────────────────────────────
# VULN: Building SQL queries by string concatenation with user-supplied values
#       enables SQL injection attacks.
# Semgrep rule: python.lang.security.audit.formatted-sql-query
# Risk: An attacker can inject SQL syntax to bypass authentication, exfiltrate data,
#       modify records, or drop tables (e.g., username = "' OR '1'='1").
def get_user_by_username(username: str) -> list:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # VULN: username is concatenated directly — use parameterised queries instead:
    #       cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    query = "SELECT * FROM users WHERE username = '" + username + "'"  # noqa: S608
    cursor.execute(query)  # VULN: SQL injection
    return cursor.fetchall()


def delete_user(user_id: str) -> None:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # VULN: f-string interpolation in SQL — use parameterised queries.
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")  # noqa: S608
    conn.commit()
    
# Demo change
# Trigger CI/CD pipeline