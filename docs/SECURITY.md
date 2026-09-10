# Security

This document describes what the platform actually does, where the boundaries
are, and what you must do yourself before running it against production data.

---

## 1. Secrets

### Nothing is stored in plain text

A secret in a connection definition is either a **reference** or **Fernet
ciphertext**. The UI never stores what an operator typed:
`SecretResolver.encrypt_for_storage()` converts a typed password into
`enc:<token>` before it reaches MongoDB, and a reference is stored verbatim
because it contains no secret material.

| Reference | Resolved from | Typical use |
|---|---|---|
| `env:NAME` | Process environment | 12-factor, Kubernetes `env` from a Secret |
| `file:/path` | File contents | Docker secrets, mounted files |
| `k8s:NAME` | `<RECONX_SECURITY_SECRETS_FILE_DIR>/NAME` | Projected Secret volume (the default in the chart) |
| `enc:<token>` | Fernet, using `RECONX_SECURITY_ENCRYPTION_KEY` | Secrets entered in the UI |
| `vault:path#key` | HashiCorp Vault KV v2 | External secret manager |
| *literal* | Itself | **Development only** — logs a warning in any other environment |

`src/reconx/security/secrets.py` never logs a resolved value. Adding a backend
means subclassing `SecretProvider` and registering it; nothing else changes.

### Secrets never leave the process that needs them

* **API responses** — connections are returned with secret fields masked.
  A saved password is never displayed again; the UI shows `********` and a
  "replace" action.
* **Logs** — the structlog processor scrubs any key whose name looks
  sensitive, separator-insensitively, so `password`, `Password`,
  `secret_key`, `secretKey`, `sasl.password` and `awsSecretAccessKey` are all
  caught.
* **Kafka events** — the publisher scrubs payloads before serialising. Event
  envelopes carry ids, counts and status, never connection detail.
* **Spark** — credentials are set on the Hadoop configuration and JDBC
  properties of the running session, not passed on the command line and not
  written to the event log. JDBC URLs are logged with credentials stripped.
* **Error messages** — connector errors report the connection id and the
  failing operation, not the resolved credential.

### Generating keys

```bash
reconx-admin gen-key                 # Fernet key for RECONX_SECURITY_ENCRYPTION_KEY
openssl rand -hex 32                 # RECONX_SECURITY_JWT_SECRET
```

Losing the encryption key makes `enc:` secrets unrecoverable — they must be
re-entered. Back it up with the same care as a database credential.

---

## 2. Authentication

* Passwords are hashed with **bcrypt**. Because bcrypt silently truncates at
  72 bytes, passwords are pre-hashed with SHA-256 and base64-encoded first, so
  the full password contributes entropy regardless of length.
* Sign-in returns a **JWT** (`HS256` by default) carrying the username, roles
  and expiry. `RECONX_SECURITY_JWT_EXPIRY_MINUTES` defaults to 480.
* The bootstrap admin is created on first start. If
  `RECONX_SECURITY_BOOTSTRAP_ADMIN_PASSWORD` is unset, a random password is
  generated and **printed once** to the log — change it immediately.
* Token verification is centralised in `TokenService.verify()`; every
  protected route depends on it.
* `RECONX_SECURITY_AUTH_ENABLED=false` exists for local development only.
  Outside a local/dev/test environment the API logs an `api.insecure_configuration`
  error on every start naming it (alongside a default JWT secret, a missing
  encryption key and wildcard CORS), and `/api/system/info` reports the state
  so an operator can see it. It is not silently tolerated, but it is not
  refused either — alert on that log line.

### Integrating an enterprise IdP

`AuthenticationBackend` is an ABC with a single `authenticate()` method.
`MongoUserStore` is the shipped implementation; an LDAP, OIDC or SAML backend
replaces it without touching the routers, because every call site depends on
`Principal`, not on the store. Roles map from IdP groups at that boundary.

---

## 3. Authorisation (RBAC)

Five roles map to nineteen permissions. **Call sites check permissions, never
role names**, so a new role is a data change.

| Permission | ADMIN | OPERATOR | DEVELOPER | VIEWER | AUDITOR |
|---|:--:|:--:|:--:|:--:|:--:|
| `recon:view` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `recon:create` | ✅ | | ✅ | | |
| `recon:edit` | ✅ | | ✅ | | |
| `recon:activate` | ✅ | ✅ | | | |
| `recon:disable` | ✅ | ✅ | | | |
| `recon:delete` | ✅ | | | | |
| `recon:execute` | ✅ | ✅ | ✅ | | |
| `run:view` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `run:cancel` | ✅ | ✅ | | | |
| `connection:view` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `connection:manage` | ✅ | | ✅ | | |
| `connection:test` | ✅ | ✅ | ✅ | | |
| `schedule:view` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `schedule:manage` | ✅ | ✅ | ✅ | | |
| `report:view` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `exception:view` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `audit:view` | ✅ | | | | ✅ |
| `user:manage` | ✅ | | | | |
| `system:manage` | ✅ | | | | |

The separation that matters: a **DEVELOPER** can write a reconciliation but
cannot activate it; an **OPERATOR** can activate and run but cannot change the
logic. That is the four-eyes control for reconciliation configuration.

The UI hides what a principal cannot do, but the UI is not the boundary — the
API enforces it with a `requires(Permission)` dependency on every route.

---

## 4. SQL safety

Officers write SQL. That is a feature, and it is the largest attack surface in
the product, so it is fenced on several sides:

1. **Read-only enforcement.** `assert_read_only()` strips comments and string
   literals, then rejects any statement that is not a `SELECT`/`WITH`, and any
   text containing a write, DDL, privilege, session or file/jar statement
   (`insert`, `update`, `delete`, `merge`, `drop`, `truncate`, `alter`,
   `grant`, `revoke`, `create table`, `copy`, `call`, `exec`, `attach`,
   `set `, `add jar`, …).
2. **Dangerous function deny-list.** Expressions and queries are checked for
   code-execution and file-access primitives across vendors: `java_method`,
   `reflect`, `xp_cmdshell`, `openrowset`, `pg_read_file`, `lo_import`,
   `utl_file`, `dbms_*`, `load_file`, `into outfile`, and more.
3. **Identifier and table-name validation.** `assert_table_name()` accepts
   real-world qualified names (`[dbo].[Trades]`, `"schema"."table"`,
   `` `db`.`tbl` ``) and nothing else — no expressions, no statement
   fragments.
4. **Variables are substituted, then validated.** `${var}` interpolation runs
   *before* the guard, so a value smuggled through a variable cannot escape
   it. Unresolved variables raise a named error rather than reaching the
   database.
5. **No Python execution.** Custom logic is Spark SQL expressions evaluated by
   Spark, and derived columns go through `assert_safe_expression()`. There is
   no `eval`, no `exec`, and no plugin path that executes user-supplied Python
   from the UI.

**The guard is defence in depth, not a substitute for least privilege.** Give
the reconciliation database user `SELECT` on precisely the objects it needs.
The platform's own metrics database user needs `INSERT`/`UPDATE` on the
metrics tables only.

---

## 5. Audit

Every configuration change and every exception transition writes an audit
entry with actor, action, entity, timestamp, correlation id and a field-level
diff — to MongoDB (`audit_log`) and to the metrics database (`audit_log`) so
it is queryable from the warehouse alongside the results it explains.

Audited actions include: definition create/update/activate/disable/archive/
rollback/clone, connection create/update/delete, run trigger/cancel/retry,
schedule pause/resume, exception status change and comment, user
create/update/delete, and lock force-release.

Audit records are append-only through the API — there is no route that edits
or deletes one. Exception comments are likewise immutable: a correction is a
new comment, and reopening is counted rather than erasing the closure.

`audit:view` is granted to ADMIN and AUDITOR only, so an auditor can read the
trail without holding any operational permission.

---

## 6. Transport and network

* Ingress terminates TLS; the chart's `ingress.tls` block wires the
  certificate secret and the websocket-friendly annotations Streamlit needs.
* MongoDB TLS is `MONGODB_TLS=true`; Kafka uses `KAFKA_SECURITY_PROTOCOL` with
  SASL/SSL and an optional CA path; JDBC TLS is a URL property
  (`sslmode=require`, `encrypt=true`, …) so it is per-connection.
* `deployment/kubernetes/09-networkpolicy.yaml` (and
  `networkPolicy.enabled` in the chart) applies a default-deny policy plus the
  specific flows the platform needs.
* The API sets security headers on every response
  (`X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`,
  `Referrer-Policy: no-referrer`, `Cache-Control: no-store`) plus an
  `X-Correlation-Id`. HSTS is left to the ingress, which is where TLS
  terminates. CORS is explicit —
  set `API_CORS_ORIGINS` to your UI origin in production rather than leaving
  the permissive local default.

---

## 7. Container and pod hardening

* Non-root user in every image, `runAsNonRoot: true` in every pod spec.
* No build toolchain in the runtime layer (multi-stage builds).
* Dropped capabilities and read-only root filesystem where the process allows;
  writable paths are explicit `emptyDir` mounts.
* Resource requests and limits on every container, PDBs on API and scheduler.
* Health, readiness and startup probes on every deployment.

---

## 8. Production hardening checklist

Before the first run against real data:

- [ ] `RECONX_SECURITY_JWT_SECRET` set to a generated value (not the default)
- [ ] `RECONX_SECURITY_ENCRYPTION_KEY` set, backed up, and rotated on a schedule
- [ ] `RECONX_SECURITY_BOOTSTRAP_ADMIN_PASSWORD` set, or the generated one changed at first login
- [ ] `RECONX_SECURITY_AUTH_ENABLED=true` and `RECONX_ENVIRONMENT=production`
- [ ] `secretsBackend: k8s` (or `vault`) — no literal secrets anywhere in configuration
- [ ] `API_CORS_ORIGINS` restricted to the UI origin
- [ ] TLS on ingress, MongoDB, Kafka and every JDBC connection
- [ ] Database users least-privileged: `SELECT` only for source connections
- [ ] `RESULT_AUTO_CREATE_SCHEMA=false`; migrations applied by a DBA
- [ ] MongoDB running as a replica set, with authentication enabled and backups verified
- [ ] NetworkPolicy enabled
- [ ] Role assignments reviewed — activation separated from authoring
- [ ] Audit log retention aligned to your regulatory requirement
- [ ] Log shipping configured; confirm no secret material appears in a sample
- [ ] `/metrics` scraped and alerts wired for failed runs and exception spikes
- [ ] `ADVISOR_LLM_ENABLED` left `false` unless sending run *metadata* to an
      external model is approved (see [ADVISOR.md](ADVISOR.md#privacy))

---

## 9. Reporting a vulnerability

Treat findings as you would for any internal platform: do not open a public
issue with a working exploit. The security-relevant modules are
`src/reconx/security/` (secrets, crypto, auth, RBAC, audit, SQL guard) and
`src/reconx/api/deps.py`.
