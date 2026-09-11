# Connectors

A **connection** is a reusable, credentialed endpoint stored in MongoDB and
referenced by id. A **source** is one use of a connection inside a leg: a
path, a table, a query, a topic. Splitting them means credentials are managed
once, by people who are allowed to, and reconciliation authors never see them.

```yaml
# connection (managed under Connections in the UI)
connectionId: ledger_mssql
type: jdbc
config:
  databaseType: sqlserver
  host: sql.internal
  port: 1433
  database: LEDGER
  username: reconx_ro
  password: k8s:ledger-password        # a reference, never a value

# source (inside a reconciliation leg)
- id: ledger
  type: jdbc
  connectionRef: ledger_mssql
  dialect: mssql
  query: "SELECT ... FROM ${ledger_table} WHERE BusinessDate = '${business_date}'"
```

Fields listed as **secret** below are never returned by the API, never
logged, and never appear in events. See [SECURITY.md](SECURITY.md#1-secrets).

---

## S3

`type: s3` — AWS S3 or any S3-compatible endpoint.

| Field | Notes |
|---|---|
| `endpoint` | Omit for AWS; set for MinIO/Ceph/other |
| `region` | Default `us-east-1` |
| `bucket` | Default bucket; a source may override |
| `accessKey` / `secretKey` | **Secret references** |
| `sessionToken` | For STS credentials |
| `useInstanceProfile` | Prefer this on EKS (IRSA) — no keys at all |
| `assumeRoleArn` | Cross-account access |
| `pathStyleAccess` | Required by most non-AWS implementations |
| `sslEnabled` / `sslVerify` | TLS behaviour |
| `basePath` | Prefix prepended to every source path |
| `connectionTimeoutMs`, `socketTimeoutMs`, `maxConnections` | Client tuning |
| `extraProperties` | Any additional `fs.s3a.*` property |

Reads and writes go through Hadoop's `s3a://`. Source options: `path` (globs
allowed), `format`, `filePattern`, `recursive`, plus format options
(`header`, `delimiter`, `multiLine`, …).

**Operational notes.** Prefer IRSA/instance profiles to keys. Use
`recursive: false` with a dated prefix rather than a wide glob — listing a
large bucket is the slow part, not the read. Parquet and ORC push predicates
down; CSV does not.

---

## StorageGRID

`type: storagegrid` — NetApp StorageGRID via its S3 API. Inherits every S3
field, with the differences that matter made explicit:

| Field | Notes |
|---|---|
| `endpoint` | **Required**, e.g. `https://sg.example.com:8082` |
| `pathStyleAccess` | Defaults to `true` |
| `tenantAccountId` | StorageGRID tenant |
| `region` | Often a tenant-specific value rather than an AWS region |

**Operational notes.** Most StorageGRID problems are TLS (a private CA — add
it to the image trust store, do not disable verification) or virtual-host
addressing (keep path-style on).

---

## SFTP

`type: sftp`

| Field | Notes |
|---|---|
| `host`, `port`, `username` | |
| `password` | **Secret reference** |
| `privateKey` | **Secret reference** to a PEM key |
| `privateKeyPassphrase` | **Secret reference** |
| `knownHosts` | Path to a `known_hosts` file |
| `strictHostKeyChecking` | Default `true` — leave it on |
| `basePath` | Root for relative source paths |
| `timeoutSeconds`, `maxRetries`, `compression` | |

Files are staged to `RECONX_STAGING_DIR` and then read by Spark, so that
directory **must be shared** between the submitting process and the
executors (the chart provisions a `ReadWriteMany` PVC). Source options:
`path`, `filePattern` (glob), `format`, and gzip is decompressed
transparently.

**Operational notes.** Populate `knownHosts` when onboarding a host rather
than turning off host-key checking. Size the staging volume for the largest
day's files, and check that retention on the SFTP side does not delete a file
mid-run.

---

## JDBC

`type: jdbc` — PostgreSQL, MySQL/MariaDB, SQL Server, Oracle, DB2, SQLite, H2.

| Field | Notes |
|---|---|
| `databaseType` | `postgresql`, `mysql`, `sqlserver`, `oracle`, `db2`, … |
| `host`, `port`, `database`, `schema` | Used to build the URL |
| `jdbcUrl` | Overrides the built URL when you need vendor properties |
| `driver` | Auto-selected from `databaseType` if omitted |
| `username` | |
| `password` | **Secret reference** |
| `fetchSize`, `batchSize` | Read/write batching |
| `numPartitions`, `partitionColumn`, `lowerBound`, `upperBound` | Parallel reads |
| `sessionInitStatement` | e.g. `SET LOCK_TIMEOUT 5000` |
| `isolationLevel` | Default `READ_COMMITTED` |
| `ssl`, `connectTimeoutSeconds`, `queryTimeoutSeconds` | |
| `extraProperties` | Any additional JDBC property |

A source supplies either `table` or `query`, plus `dialect` so the UI knows
how to quote identifiers in previews. **The query is sent verbatim** — write
T-SQL for SQL Server, PL/SQL-flavoured SQL for Oracle. `${variables}` are
substituted in both the query and the table name before the statement is
validated as read-only.

```yaml
- id: ledger
  type: jdbc
  connectionRef: ledger_mssql
  dialect: mssql
  query: |
    SELECT l.[CustomerId] AS customer_id, l.[Amount] AS amount
    FROM ${ledger_table} AS l WITH (NOLOCK)
    WHERE l.[BusinessDate] = '${business_date}'
```

**Operational notes.** Set `partitionColumn` + bounds + `numPartitions` for
anything large — without them Spark reads through a single connection. Push
filters into the query rather than reading the table and filtering in Spark.
Grant the reconciliation user `SELECT` only. Driver jars are not vendored:
run `./scripts/fetch-jdbc-drivers.sh` (Oracle's `ojdbc` must be downloaded by
hand).

**Query preview.** The designer's *Preview query* button streams the cursor
and stops at the row limit, so previewing a query against a huge table is
safe.

---

## Filesystem

`type: filesystem` — local or mounted (NFS, CIFS) paths.

| Field | Notes |
|---|---|
| `basePath` | Root; source paths are resolved under it |
| `writable` | Refuse writes when false |
| `createMissingDirectories` | For outputs |

Formats: CSV, JSON, Parquet, ORC, Avro, text, delimited. Every Spark
executor must see the same path — this is for shared mounts, not for a
directory that exists on one node.

---

## Kafka

`type: kafka` — batch reads by offset range (not streaming).

| Field | Notes |
|---|---|
| `bootstrapServers` | |
| `securityProtocol` | `PLAINTEXT`, `SSL`, `SASL_PLAINTEXT`, `SASL_SSL` |
| `saslMechanism` | `PLAIN`, `SCRAM-SHA-256/512`, `GSSAPI`, `OAUTHBEARER` |
| `saslUsername` | |
| `saslPassword` | **Secret reference** |
| `sslCaLocation`, `sslCertificateLocation`, `sslKeyLocation`, `sslKeyPassword` | mTLS |
| `consumerGroupPrefix` | |
| `schemaRegistryUrl` | For Avro payloads |
| `extraProperties` | Any additional client property |

Source options: `topic`, `startingOffsets`, `endingOffsets`, and a payload
`format` (`json`, `csv`, `avro`). A reconciliation is a bounded computation,
so the source reads a *range* — for "everything since yesterday", set the
offsets by timestamp.

---

## Excel

`type: excel` (a source type; the file itself comes from a filesystem, S3 or
SFTP connection).

| Option | Notes |
|---|---|
| `sheet` | Name or index |
| `headerRow` | Zero-based |
| `skipRows` | |
| `maxRows` | **Explicit cap** — Excel is read on the driver |
| `dataAddress` | Cell range, e.g. `A3:H5000` |

Read with `openpyxl` in read-only mode and converted to a DataFrame. Excel
files are inherently driver-side and single-threaded: the row cap is there to
stop someone pointing a 2M-row workbook at the driver. For anything large,
convert to CSV/Parquet upstream.

---

## Temp view and leg output

`type: temp_view` (`view: name`) and `type: leg_output`
(`legRef`, optionally `legOutputRef`).

This is how multi-leg DAGs pass data: a leg registers its result as a Spark
temporary view (`registerResultView`), and a downstream leg consumes it
directly — no serialisation, no object-storage round trip. A
`transformations` step of type `temp_view` can register an intermediate too,
which is what lets a source be reused by several legs after one expensive
read.

`type: inline` also exists — rows written directly in the definition. It is
for reference data and tests, not for volume.

---

## Adding a connector

```python
from reconx.connectors.base import (
    ConnectionTestResult, DataSourceConnector, OutputContext, SourceContext,
    register_connector,
)

@register_connector
class MyConnector(DataSourceConnector):
    source_types = (SourceType.MYTYPE,)
    display_name = "My System"
    supports_listing = True

    def read(self, config: SourceContext, spark) -> "DataFrame": ...
    def write(self, dataframe, config: OutputContext) -> dict: ...
    def test_connection(self, config: dict) -> ConnectionTestResult: ...
    def validate(self, config: dict) -> list[str]: ...

    # optional
    def list_files(self, config, path, pattern=None): ...
    def prepare_spark(self, spark, config) -> None: ...
```

`SourceContext`/`OutputContext` carry the source specification, the
**already-resolved** connection configuration and the run variables — a
connector never resolves secrets itself and never sees a reference.

Add the type to `ConnectionType`/`SourceType`, add a config model in
`config/connections.py` (listing any secret field in `SECRET_FIELDS` so it is
masked and scrubbed), and import the module so the decorator runs. The
reconciliation engine is not touched: it asks the registry for a connector and
calls `read`. The UI picks the new type up from
`GET /api/connections/types`.
