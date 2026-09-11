"""Guard rails for user-supplied SQL and Spark SQL expressions.

The platform deliberately lets power users write Spark SQL - it is the sane way
to express transformations.  What it must never allow is arbitrary code
execution or data destruction from a web form.  Everything below is a
deny-list-plus-shape check applied *before* the statement reaches Spark/JDBC.
"""

from __future__ import annotations

import re

from reconx.common.errors import ValidationError

#: Vendor-specific read-only constructs that must keep working:
#: ``SELECT TOP (100) ...`` and table hints such as ``WITH (NOLOCK)`` (SQL Server),
#: ``FETCH FIRST n ROWS ONLY`` (Oracle/DB2), ``LIMIT n`` (PostgreSQL/MySQL).
#: None of them are affected by the deny-list below - they are plain SELECT syntax.

#: Statements that are never acceptable from configuration.
FORBIDDEN_STATEMENTS = (
    "insert",
    "update",
    "delete",
    "merge",
    "drop",
    "truncate",
    "alter",
    "grant",
    "revoke",
    "create table",
    "create database",
    "create schema",
    "create function",
    "create or replace function",
    "load data",
    "copy",
    "call",
    "execute",
    "exec",
    "attach",
    "detach",
    "set ",
    "reset ",
    "add jar",
    "add file",
    "list jar",
    "refresh function",
)

#: Expression-level constructs that would allow code execution or file access.
FORBIDDEN_FUNCTIONS = (
    "java_method",
    "reflect",
    "reflectjava",
    "xpath",
    "input_file_block_start",
    "sha2wrapper",
    "system",
    "pg_read_file",
    "pg_ls_dir",
    "lo_import",
    "lo_export",
    "dbms_",
    "utl_file",
    "utl_http",
    "xp_cmdshell",
    "sp_configure",
    "openrowset",
    "opendatasource",
    "load_file",
    "into outfile",
    "into dumpfile",
)

_COMMENT_RE = re.compile(r"(--[^\n]*|/\*.*?\*/)", re.DOTALL)
_STRING_RE = re.compile(r"'([^']|'')*'")


def _normalise(sql: str) -> str:
    """Lower-cased SQL with comments and string literals removed."""
    without_comments = _COMMENT_RE.sub(" ", sql)
    without_strings = _STRING_RE.sub("''", without_comments)
    return re.sub(r"\s+", " ", without_strings).strip().lower()


def assert_read_only(sql: str, *, context: str = "sql") -> str:
    """Reject anything that is not a single read-only statement."""
    if not sql or not sql.strip():
        raise ValidationError(f"{context}: SQL statement is empty")
    normalised = _normalise(sql)

    statements = [s for s in normalised.split(";") if s.strip()]
    if len(statements) > 1:
        raise ValidationError(
            f"{context}: multiple SQL statements are not allowed (found {len(statements)})"
        )

    if not (normalised.startswith("select") or normalised.startswith("with") or normalised.startswith("(")):
        raise ValidationError(f"{context}: only SELECT/WITH statements are allowed")

    for forbidden in FORBIDDEN_STATEMENTS:
        if re.search(rf"(^|[\s(]){re.escape(forbidden.strip())}(\s|$|\()", normalised):
            raise ValidationError(f"{context}: statement '{forbidden.strip()}' is not permitted")

    assert_no_dangerous_functions(normalised, context=context)
    return sql


def assert_no_dangerous_functions(sql: str, *, context: str = "expression") -> None:
    lowered = _normalise(sql) if not sql.islower() else sql
    for forbidden in FORBIDDEN_FUNCTIONS:
        if forbidden in lowered:
            raise ValidationError(f"{context}: use of '{forbidden}' is not permitted")


def assert_safe_expression(expression: str, *, context: str = "expression") -> str:
    """Validate a scalar/boolean Spark SQL expression (not a full statement)."""
    if not expression or not expression.strip():
        raise ValidationError(f"{context}: expression is empty")
    normalised = _normalise(expression)
    if ";" in normalised:
        raise ValidationError(f"{context}: ';' is not allowed inside an expression")
    for forbidden in ("insert ", "update ", "delete ", "drop ", "alter ", "create ", "grant ", "truncate "):
        if normalised.startswith(forbidden) or f" {forbidden}" in f" {normalised}":
            raise ValidationError(f"{context}: DDL/DML is not allowed inside an expression")
    assert_no_dangerous_functions(normalised, context=context)
    return expression


_IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{0,127}$")

#: One name part: bare, [bracketed] (SQL Server), "quoted" (ANSI) or `backticked` (MySQL).
_PART = r"""(?:[A-Za-z_][A-Za-z0-9_$#]{0,127}|\[[^\]\[]{1,128}\]|"[^"]{1,128}"|`[^`]{1,128}`)"""
_QUALIFIED_RE = re.compile(rf"^{_PART}(\.{_PART}){{0,3}}$")


def assert_identifier(name: str, *, context: str = "identifier") -> str:
    if not _IDENTIFIER_RE.match(name or ""):
        raise ValidationError(
            f"{context}: '{name}' is not a valid identifier (letters, digits and underscore only)"
        )
    return name


def assert_table_name(name: str, *, context: str = "table") -> str:
    r"""Validate an (optionally qualified) table name.

    Accepts the quoting styles of the supported vendors so a SQL Server user can
    write ``[dbo].[Transactions]`` and a MySQL user ``\`schema\`.\`table\```,
    while still rejecting anything that could smuggle in a second statement.
    """
    candidate = (name or "").strip()
    if not _QUALIFIED_RE.match(candidate):
        raise ValidationError(
            f"{context}: '{name}' is not a valid (optionally qualified) table name. "
            "Use db.schema.table, [db].[schema].[table], \"schema\".\"table\" or `schema`.`table`."
        )
    if any(ch in candidate for ch in (";", "--", "/*")):
        raise ValidationError(f"{context}: '{name}' contains illegal characters")
    return candidate


def quote_literal(value: str) -> str:
    """Single-quote a SQL string literal safely (for generated conditions)."""
    return "'" + str(value).replace("'", "''") + "'"
