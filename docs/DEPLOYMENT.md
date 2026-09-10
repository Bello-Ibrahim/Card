# Deployment

ReconX ships three ways: **docker compose** (a complete local stack, for
development and demos), **raw Kubernetes manifests** (when you want to read
exactly what is applied), and a **Helm chart** (for real environments). All
three build from the same four images.

---

## 1. Images

| Image | Dockerfile | Runs |
|---|---|---|
| `reconx/api` | `deployment/docker/Dockerfile.api` | uvicorn + FastAPI control plane |
| `reconx/ui` | `deployment/docker/Dockerfile.ui` | Streamlit |
| `reconx/scheduler` | `deployment/docker/Dockerfile.scheduler` | The scheduler loop |
| `reconx/spark` | `deployment/docker/Dockerfile.spark` | Spark driver/executor image with `reconx` installed |

All four are multi-stage (a wheel is built in a builder stage and installed
into a slim runtime), run as a **non-root** user, declare a `HEALTHCHECK`, and
carry no build toolchain in the final layer.

```bash
make docker-build
REGISTRY=registry.example.com/ IMAGE_TAG=1.0.0 make docker-push
```

### JDBC drivers

Driver jars are **not** vendored — licences differ and versions are a local
decision. Fetch the ones you need into a directory that the images copy in:

```bash
./scripts/fetch-jdbc-drivers.sh deployment/docker/jars
```

The script pulls PostgreSQL, MySQL, MSSQL, DB2, SQLite and H2 from Maven
Central. Oracle's `ojdbc` must be downloaded manually and dropped into the
same directory. `deployment/docker/jars/README.md` lists the coordinates.

---

## 2. Local stack (docker compose)

```bash
./scripts/fetch-jdbc-drivers.sh deployment/docker/jars
docker compose up -d
```

Fourteen services: MongoDB (+ replica-set init), PostgreSQL, Kafka (KRaft) and
Kafka UI, MinIO (+ bucket init), an SFTP server, Mailpit, a Spark master and
worker, the API, **two scheduler replicas** and the UI.

| Service | URL | Credentials |
|---|---|---|
| Streamlit UI | http://localhost:8501 | `admin` / `reconx-admin` |
| API + OpenAPI | http://localhost:8000/docs | bearer token from `/api/auth/login` |
| Kafka UI | http://localhost:8080 | — |
| MinIO console | http://localhost:9001 | `reconx` / `reconx-secret` |
| Mailpit | http://localhost:8025 | — |
| Spark master | http://localhost:8090 | — |

Two scheduler replicas are deliberate: it is the cheapest demonstration that
distributed locking works. Watch both logs and you will see one node take the
lock and the other skip.

```bash
make docker-logs
make docker-clean      # stop and delete volumes
```

---

## 3. Kubernetes

### Raw manifests

```bash
kubectl apply -f deployment/kubernetes/
kubectl apply --dry-run=server -f deployment/kubernetes/    # validate first
```

| File | Contents |
|---|---|
| `00-namespace.yaml` | Namespace |
| `01-configmap.yaml` | Non-secret configuration (the `.env` keys) |
| `02-secret.yaml` | **Template only** — replace before applying |
| `03-rbac.yaml` | ServiceAccounts, Role/RoleBinding for Spark-on-K8s |
| `04-storage.yaml` | Staging PVC (`ReadWriteMany`) |
| `05-api.yaml` | Deployment, Service, HPA, PodDisruptionBudget |
| `06-ui.yaml` | Deployment, Service (session affinity) |
| `07-scheduler.yaml` | Deployment (2 replicas), PDB |
| `08-ingress.yaml` | Ingress with TLS and websocket-friendly annotations |
| `09-networkpolicy.yaml` | Default-deny plus the flows the platform needs |
| `10-maintenance-cronjob.yaml` | Retention/reclaim job |

Pods run with `runAsNonRoot`, a read-only root filesystem where possible,
dropped capabilities, topology-spread constraints across zones, and resource
requests/limits on every container.

### Helm (recommended)

```bash
helm upgrade --install reconx deployment/helm/reconx \
  --namespace reconx --create-namespace \
  -f my-values.yaml
```

A minimal production `my-values.yaml`:

```yaml
image:
  registry: registry.example.com/

config:
  environment: production

mongodb:
  enabled: false
  uri: "mongodb+srv://reconx@mongo.internal/?replicaSet=rs0"
  existingSecret: reconx-mongodb        # holds MONGODB_URI

resultDatabase:
  jdbcUrl: "jdbc:postgresql://pg.internal:5432/reconx_results"
  user: reconx
  autoCreateSchema: false               # DBAs apply the migration

kafka:
  bootstrapServers: "kafka-1:9093,kafka-2:9093"
  securityProtocol: SASL_SSL
  saslMechanism: SCRAM-SHA-512
  saslUsername: reconx

spark:
  submitMode: kubernetes
  master: "k8s://https://kubernetes.default.svc:443"
  executor: {cores: 4, memory: 8g, instances: 6}
  dynamicAllocation: {enabled: true, minExecutors: 2, maxExecutors: 40}
  shufflePartitions: 800

security:
  existingSecret: reconx-secrets        # JWT, encryption key, DB/SMTP/Kafka passwords
  secretsBackend: k8s

ingress:
  host: reconx.bank.internal
  tls: {enabled: true, secretName: reconx-tls}

storage:
  staging: {accessMode: ReadWriteMany, size: 200Gi, storageClassName: nfs}
```

Validate before installing:

```bash
make helm-lint          # helm lint + scripts/validate_helm_chart.py
make helm-template      # render locally and read the output
```

`scripts/validate_helm_chart.py` is a static checker for the chart (values
referenced by templates exist, templates parse, required keys are present).
It exists so the chart can be validated in environments where the `helm`
binary is unavailable; it is not a replacement for `helm lint` where you have
it.

---

## 4. Secrets

**Never put a secret in `values.yaml` or a ConfigMap in production.** Create
the Secret out of band and point the chart at it:

```bash
kubectl -n reconx create secret generic reconx-secrets \
  --from-literal=RECONX_SECURITY_JWT_SECRET="$(openssl rand -hex 32)" \
  --from-literal=RECONX_SECURITY_ENCRYPTION_KEY="$(reconx-admin gen-key)" \
  --from-literal=RESULT_JDBC_PASSWORD="..." \
  --from-literal=SMTP_PASSWORD="..." \
  --from-literal=KAFKA_SASL_PASSWORD="..."
```

```yaml
security:
  existingSecret: reconx-secrets
  secretsBackend: k8s
```

With `secretsBackend: k8s`, connection-level secrets are referenced from
reconciliation configuration as `k8s:<key>` and read from the projected
volume at `/var/run/secrets/reconx`. Other schemes (`env:`, `file:`, `enc:`,
`vault:`) work the same way — see [SECURITY.md](SECURITY.md#1-secrets).

Rotating the encryption key re-encrypts stored connection secrets; rotating
the JWT secret invalidates issued tokens (users sign in again). Neither
requires a redeploy of the Spark image.

---

## 5. Spark

Three submit modes, set by `SPARK_SUBMIT_MODE`:

| Mode | Use when |
|---|---|
| `inprocess` | Local development, the demo, unit/e2e tests |
| `spark-submit` | An existing standalone or YARN cluster |
| `kubernetes` | Spark-on-Kubernetes — the driver is a pod, executors are pods |

For `kubernetes`, the chart creates the `reconx-spark` ServiceAccount and the
Role/RoleBinding the driver needs to create executor pods, and passes
`SPARK_IMAGE` through. Set executor sizing and dynamic allocation in values;
a single reconciliation can override them (`spark:` block in the definition)
when one feed is much larger than the rest.

The staging PVC must be `ReadWriteMany`: SFTP downloads and Excel conversion
stage files that executors then read.

---

## 6. Databases

### MongoDB

A **replica set is required** — the platform uses transactions for
version-and-pointer writes. Indexes (including the unique idempotency index
and the lock TTL index) are created by:

```bash
reconx-admin init-db          # or: POST /api/system/initialise
```

Back up with `mongodump` or your managed provider's snapshots. The
configuration store is the system of record for *what* reconciliations exist;
losing it loses definitions and audit history.

### Metrics database

```bash
psql -f src/reconx/metrics/migrations/V1__initial_schema.sql
```

Set `RESULT_AUTO_CREATE_SCHEMA=false` in production so the application never
issues DDL. Regenerate the migration after model changes with `make db-ddl`.

Size the exception table for your volume: it is the only table that grows with
break count rather than run count. Retention is enforced by the maintenance
CronJob using each definition's `retention` block.

---

## 7. Kafka

Topics are `<prefix>.started`, `.stage.completed`, `.completed`, `.failed`,
`.exception`, `.data-unavailable`, `.alert`. Create them ahead of time if
auto-creation is disabled:

```bash
for t in started stage.completed completed failed exception data-unavailable alert; do
  kafka-topics.sh --create --topic reconciliation.$t --partitions 6 --replication-factor 3 ...
done
```

If the broker is unreachable, the publisher writes to a MongoDB outbox and the
behaviour is decided by the definition's `events.onFailure`
(`WARN_ONLY`, `RETRY`, `FAIL_RUN`). Outbox drainage is part of the maintenance
job.

---

## 8. Upgrades

The control plane is stateless, so a rolling update is safe. The order that
matters is schema-first:

1. Apply any new metrics-database migration.
2. `helm upgrade` — API and UI roll first, then schedulers.
3. Because schedulers coordinate through MongoDB locks and the unique
   idempotency key, a mixed-version scheduler fleet during the roll cannot
   double-fire a reconciliation.

Definitions are versioned and forward-compatible: an older definition document
validates against a newer model because every added field has a default.

Roll back with `helm rollback`; configuration is untouched by a code rollback.

---

## 9. Disaster recovery

See [OPERATIONS.md](OPERATIONS.md#8-disaster-recovery) for RPO/RTO targets, the
restore runbook and the failure-mode table.
