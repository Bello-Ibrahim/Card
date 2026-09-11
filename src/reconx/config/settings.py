"""Environment-driven platform settings (12-factor).

Every service (API, scheduler, Spark job, UI) reads the same settings object so
that a single ConfigMap/Secret drives the whole deployment.
"""

from __future__ import annotations

import functools
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="MONGODB_", extra="ignore")

    uri: str = Field(default="mongodb://localhost:27017/?replicaSet=&directConnection=true")
    database: str = Field(default="reconx")
    tls: bool = False
    server_selection_timeout_ms: int = 10_000
    max_pool_size: int = 50


class KafkaSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="KAFKA_", extra="ignore")

    bootstrap_servers: str = Field(default="localhost:9092")
    security_protocol: str = "PLAINTEXT"
    sasl_mechanism: str | None = None
    sasl_username: str | None = None
    sasl_password: str | None = None
    ssl_ca_location: str | None = None
    client_id: str = "reconx"
    topic_prefix: str = "reconciliation"
    enabled: bool = True
    delivery_timeout_ms: int = 30_000


class ResultDbSettings(BaseSettings):
    """JDBC metrics/results database.

    ``jdbc_url`` is what Spark uses; ``sqlalchemy_url`` is what the control
    plane uses.  If only one is provided the other is derived when possible.
    """

    model_config = SettingsConfigDict(env_prefix="RESULT_", extra="ignore")

    jdbc_url: str = Field(default="jdbc:postgresql://localhost:5432/reconx_results")
    jdbc_driver: str = Field(default="org.postgresql.Driver")
    jdbc_user: str = Field(default="reconx")
    jdbc_password: str = Field(default="reconx")
    sqlalchemy_url: str | None = None
    schema_name: str = "public"
    pool_size: int = 5
    auto_create_schema: bool = Field(
        default=True,
        description="Create missing metrics tables on startup. Disable in production where DBAs apply migrations.",
    )

    def resolved_sqlalchemy_url(self) -> str:
        if self.sqlalchemy_url:
            return self.sqlalchemy_url
        return jdbc_to_sqlalchemy(self.jdbc_url, self.jdbc_user, self.jdbc_password)


def jdbc_to_sqlalchemy(jdbc_url: str, user: str | None, password: str | None) -> str:
    """Translate a JDBC URL into a SQLAlchemy URL.

    Used by the control plane (connection tests, availability conditions, query
    previews, metrics access) - Spark keeps using the JDBC URL directly.  The
    vendor-specific URL shapes are handled explicitly because they differ far
    more than ``vendor://host/db``.
    """
    from urllib.parse import quote_plus

    if not jdbc_url:
        return jdbc_url
    if not jdbc_url.startswith("jdbc:"):
        return jdbc_url
    body = jdbc_url[len("jdbc:") :]
    vendor = body.split(":", 1)[0].lower()

    def credentials() -> str:
        if not user:
            return ""
        return quote_plus(user) + (f":{quote_plus(password)}" if password else "") + "@"

    # sqlite:  jdbc:sqlite:/path/to.db
    if vendor == "sqlite":
        path = body.split(":", 1)[1] if ":" in body else ""
        # An absolute path needs four slashes (sqlite:////abs/path.db); a relative
        # one needs three - concatenating preserves whichever the user gave.
        return f"sqlite:///{path}" if path else "sqlite://"

    # SQL Server:  jdbc:sqlserver://host:1433;databaseName=db;encrypt=true
    if vendor == "sqlserver":
        remainder = body.split("://", 1)[1] if "://" in body else ""
        host_part, _, properties = remainder.partition(";")
        settings_map = {
            key.strip().lower(): value
            for key, _, value in (item.partition("=") for item in properties.split(";") if item)
        }
        database = settings_map.get("databasename", "")
        driver = quote_plus(settings_map.get("driver", "ODBC Driver 18 for SQL Server"))
        query = f"?driver={driver}&TrustServerCertificate=yes"
        return f"mssql+pyodbc://{credentials()}{host_part}/{database}{query}"

    # Oracle:  jdbc:oracle:thin:@//host:1521/service  or  @host:1521:SID
    if vendor == "oracle":
        target = body.split("@", 1)[1] if "@" in body else ""
        target = target.lstrip("/")
        if target.count(":") == 2 and "/" not in target:  # host:port:SID
            host, port, sid = target.split(":")
            return f"oracle+oracledb://{credentials()}{host}:{port}/?service_name={sid}"
        return f"oracle+oracledb://{credentials()}{target}"

    driver_map = {
        "postgresql": "postgresql+psycopg",
        "postgres": "postgresql+psycopg",
        "mysql": "mysql+pymysql",
        "mariadb": "mysql+pymysql",
        "db2": "ibm_db_sa",
        "h2": "h2",
    }
    dialect = driver_map.get(vendor, vendor)
    remainder = body.split("://", 1)[1] if "://" in body else ""
    if not remainder:
        return jdbc_url
    return f"{dialect}://{credentials()}{remainder}"


def sqlalchemy_to_jdbc(url: str) -> str:
    """Translate a SQLAlchemy URL into the JDBC URL Spark needs.

    The inverse of :func:`jdbc_to_sqlalchemy`.  Useful when the control plane is
    configured with a SQLAlchemy URL and the Spark job has to reach the same
    database, and in tests where both halves must agree on one database.
    """
    from urllib.parse import urlparse

    if url.startswith("jdbc:"):
        return url
    parsed = urlparse(url)
    dialect = parsed.scheme.split("+", 1)[0]
    vendor = {"postgresql": "postgresql", "mysql": "mysql", "mssql": "sqlserver", "oracle": "oracle"}.get(
        dialect, dialect
    )
    if vendor == "sqlite":
        return f"jdbc:sqlite:{url.split('sqlite://', 1)[1].lstrip('/') if '///' not in url else url.split('///', 1)[1]}"
    host = parsed.hostname or ""
    port = f":{parsed.port}" if parsed.port else ""
    database = (parsed.path or "").lstrip("/")
    if vendor == "sqlserver":
        return f"jdbc:sqlserver://{host}{port};databaseName={database}"
    if vendor == "oracle":
        return f"jdbc:oracle:thin:@//{host}{port}/{database}"
    return f"jdbc:{vendor}://{host}{port}/{database}"


class SparkSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SPARK_", extra="ignore")

    master: str = Field(default="local[*]")
    namespace: str = "reconx"
    submit_mode: Literal["inprocess", "spark-submit", "kubernetes"] = "inprocess"
    home: str | None = None
    image: str = "reconx/spark:1.0.0"
    service_account: str = "reconx-spark"
    driver_cores: int = 1
    driver_memory: str = "2g"
    executor_cores: int = 2
    executor_memory: str = "4g"
    executor_instances: int = 2
    dynamic_allocation: bool = False
    dynamic_allocation_min_executors: int = 1
    dynamic_allocation_max_executors: int = 10
    shuffle_partitions: int = 200
    adaptive_enabled: bool = True
    broadcast_threshold_mb: int = 10
    event_log_dir: str | None = None
    extra_jars: str | None = None
    extra_packages: str | None = None
    local_dir: str | None = None
    warehouse_dir: str | None = None
    job_timeout_seconds: int = 7200
    python_executable: str | None = None


class SmtpSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SMTP_", extra="ignore")

    host: str = "localhost"
    port: int = 1025
    username: str | None = None
    password: str | None = None
    use_tls: bool = False
    use_ssl: bool = False
    from_address: str = "reconx@example.com"
    from_name: str = "ReconX Platform"
    timeout_seconds: int = 30
    enabled: bool = True


class SecuritySettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="RECONX_SECURITY_", extra="ignore")

    jwt_secret: str = Field(default="change-me-in-production")
    jwt_algorithm: str = "HS256"
    jwt_expiry_minutes: int = 480
    encryption_key: str | None = Field(
        default=None, description="Fernet key (base64, 32 bytes) for secret encryption at rest"
    )
    secrets_backend: Literal["env", "file", "encrypted", "auto"] = "auto"
    secrets_file_dir: str = "/var/run/secrets/reconx"
    bootstrap_admin_username: str = "admin"
    bootstrap_admin_password: str | None = None
    auth_enabled: bool = True
    allow_anonymous_read: bool = False

    @field_validator("jwt_secret")
    @classmethod
    def _warn_default(cls, v: str) -> str:
        return v


class SchedulerSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SCHEDULER_", extra="ignore")

    enabled: bool = True
    poll_interval_seconds: int = 30
    lock_ttl_seconds: int = 120
    node_id: str | None = None
    max_concurrent_runs: int = 10
    data_wait_timeout_minutes: int = 240
    condition_recheck_seconds: int = 300
    orphan_run_timeout_minutes: int = 720


class ApiSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="API_", extra="ignore")

    host: str = "0.0.0.0"  # noqa: S104 - containers bind all interfaces
    port: int = 8000
    root_path: str = ""
    cors_origins: str = "*"
    workers: int = 1
    base_url: str = "http://localhost:8000"
    request_timeout_seconds: int = 120


class Settings(BaseSettings):
    """Root settings aggregate."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    environment: str = Field(default="local", alias="RECONX_ENVIRONMENT")
    service: str = Field(default="reconx", alias="RECONX_SERVICE")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    log_format: Literal["json", "console"] = Field(default="json", alias="LOG_FORMAT")
    staging_dir: str = Field(default="/tmp/reconx-staging", alias="RECONX_STAGING_DIR")  # noqa: S108

    mongo: MongoSettings = Field(default_factory=MongoSettings)
    kafka: KafkaSettings = Field(default_factory=KafkaSettings)
    result_db: ResultDbSettings = Field(default_factory=ResultDbSettings)
    spark: SparkSettings = Field(default_factory=SparkSettings)
    smtp: SmtpSettings = Field(default_factory=SmtpSettings)
    security: SecuritySettings = Field(default_factory=SecuritySettings)
    scheduler: SchedulerSettings = Field(default_factory=SchedulerSettings)
    api: ApiSettings = Field(default_factory=ApiSettings)


@functools.lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


def reset_settings_cache() -> None:
    get_settings.cache_clear()
