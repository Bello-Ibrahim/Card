"""Connection definitions.

A connection captures *how* to reach a system.  Secret material is never stored
in the clear: every secret-bearing field holds a :class:`SecretRef` string such
as ``env:PG_PASSWORD``, ``file:/var/run/secrets/reconx/pg``, or
``enc:gAAAAA...`` (Fernet ciphertext produced by
:mod:`reconx.security.crypto`).  Resolution happens at execution time inside
:mod:`reconx.security.secrets`.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import ConfigDict, Field, model_validator

from reconx.config.enums import ConnectionType
from reconx.config.models import ReconXModel

SECRET_FIELDS = frozenset(
    {
        "password",
        "secret_key",
        "secretKey",
        "private_key",
        "privateKey",
        "passphrase",
        "sasl_password",
        "saslPassword",
        "ssl_key_password",
        "sslKeyPassword",
        "access_key",
        "accessKey",
        "session_token",
        "sessionToken",
    }
)


class BaseConnectionConfig(ReconXModel):
    model_config = ConfigDict(
        alias_generator=ReconXModel.model_config["alias_generator"],
        populate_by_name=True,
        extra="allow",
        str_strip_whitespace=True,
    )


class S3ConnectionConfig(BaseConnectionConfig):
    """AWS S3 or any S3-compatible endpoint (MinIO, Ceph, StorageGRID...)."""

    endpoint: str | None = Field(default=None, description="Custom endpoint URL; omit for AWS")
    region: str = "us-east-1"
    bucket: str | None = None
    access_key: str | None = Field(default=None, description="Secret reference")
    secret_key: str | None = Field(default=None, description="Secret reference")
    session_token: str | None = None
    use_instance_profile: bool = Field(
        default=False, description="Use IAM instance/IRSA credentials instead of keys"
    )
    assume_role_arn: str | None = None
    path_style_access: bool = False
    ssl_enabled: bool = True
    ssl_verify: bool = True
    base_path: str | None = None
    connection_timeout_ms: int = 30_000
    socket_timeout_ms: int = 60_000
    max_connections: int = 64
    extra_properties: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _validate(self) -> S3ConnectionConfig:
        if not self.use_instance_profile and not (self.access_key and self.secret_key):
            raise ValueError("S3 connection requires accessKey+secretKey or useInstanceProfile=true")
        return self


class StorageGridConnectionConfig(S3ConnectionConfig):
    """NetApp StorageGRID via its S3-compatible API.

    Defaults differ from AWS: an explicit endpoint is mandatory, path-style
    access is the norm and the region is a tenant-defined string.
    """

    endpoint: str = Field(description="StorageGRID S3 endpoint, e.g. https://sg.example.com:8082")
    path_style_access: bool = True
    region: str = "us-east-1"
    tenant_account_id: str | None = None


class SftpConnectionConfig(BaseConnectionConfig):
    host: str
    port: int = Field(default=22, ge=1, le=65535)
    username: str
    password: str | None = Field(default=None, description="Secret reference")
    private_key: str | None = Field(default=None, description="Secret reference to a PEM key")
    private_key_passphrase: str | None = None
    known_hosts: str | None = Field(default=None, description="Path to known_hosts file")
    strict_host_key_checking: bool = True
    base_path: str = "/"
    timeout_seconds: int = 30
    compression: bool = False
    max_retries: int = 3

    @model_validator(mode="after")
    def _validate(self) -> SftpConnectionConfig:
        if not self.password and not self.private_key:
            raise ValueError("SFTP connection requires 'password' or 'privateKey'")
        return self


class JdbcConnectionConfig(BaseConnectionConfig):
    """Vendor-neutral JDBC connection.

    Either provide a full ``jdbcUrl`` or the structured host/port/database
    fields; the URL is derived for the known vendors when it is omitted.
    """

    database_type: str = Field(default="postgresql", description="postgresql|mysql|oracle|sqlserver|db2|...")
    host: str | None = None
    port: int | None = Field(default=None, ge=1, le=65535)
    database: str | None = None
    db_schema: str | None = Field(default=None, alias="schema")
    username: str | None = None
    password: str | None = Field(default=None, description="Secret reference")
    jdbc_url: str | None = None
    driver: str | None = None
    fetch_size: int = 10_000
    batch_size: int = 10_000
    num_partitions: int | None = Field(default=None, ge=1, le=1024)
    partition_column: str | None = None
    lower_bound: str | None = None
    upper_bound: str | None = None
    session_init_statement: str | None = None
    isolation_level: str = "READ_COMMITTED"
    ssl: bool = False
    connect_timeout_seconds: int = 30
    query_timeout_seconds: int = 600
    extra_properties: dict[str, str] = Field(default_factory=dict)

    DEFAULT_PORTS: dict[str, int] = Field(default={}, exclude=True, repr=False)

    @model_validator(mode="after")
    def _validate(self) -> JdbcConnectionConfig:
        if not self.jdbc_url and not (self.host and self.database):
            raise ValueError("JDBC connection requires 'jdbcUrl' or 'host'+'database'")
        return self

    def resolved_driver(self) -> str:
        if self.driver:
            return self.driver
        return DEFAULT_DRIVERS.get(self.database_type.lower(), "")

    def resolved_url(self) -> str:
        if self.jdbc_url:
            return self.jdbc_url
        vendor = self.database_type.lower()
        port = self.port or DEFAULT_PORTS.get(vendor)
        if vendor in ("postgresql", "postgres"):
            url = f"jdbc:postgresql://{self.host}:{port}/{self.database}"
            return url + "?ssl=true&sslmode=require" if self.ssl else url
        if vendor in ("mysql", "mariadb"):
            return f"jdbc:{vendor}://{self.host}:{port}/{self.database}?useSSL={str(self.ssl).lower()}"
        if vendor == "sqlserver":
            return (
                f"jdbc:sqlserver://{self.host}:{port};databaseName={self.database};"
                f"encrypt={str(self.ssl).lower()};trustServerCertificate=true"
            )
        if vendor == "oracle":
            return f"jdbc:oracle:thin:@//{self.host}:{port}/{self.database}"
        if vendor == "db2":
            return f"jdbc:db2://{self.host}:{port}/{self.database}"
        if vendor == "sqlite":
            return f"jdbc:sqlite:{self.database}"
        raise ValueError(
            f"Cannot derive a JDBC URL for database type '{self.database_type}'. Provide 'jdbcUrl'."
        )


DEFAULT_PORTS: dict[str, int] = {
    "postgresql": 5432,
    "postgres": 5432,
    "mysql": 3306,
    "mariadb": 3306,
    "sqlserver": 1433,
    "oracle": 1521,
    "db2": 50000,
}

DEFAULT_DRIVERS: dict[str, str] = {
    "postgresql": "org.postgresql.Driver",
    "postgres": "org.postgresql.Driver",
    "mysql": "com.mysql.cj.jdbc.Driver",
    "mariadb": "org.mariadb.jdbc.Driver",
    "sqlserver": "com.microsoft.sqlserver.jdbc.SQLServerDriver",
    "oracle": "oracle.jdbc.OracleDriver",
    "db2": "com.ibm.db2.jcc.DB2Driver",
    "sqlite": "org.sqlite.JDBC",
    "h2": "org.h2.Driver",
}


class KafkaConnectionConfig(BaseConnectionConfig):
    bootstrap_servers: str
    security_protocol: Literal["PLAINTEXT", "SSL", "SASL_PLAINTEXT", "SASL_SSL"] = "PLAINTEXT"
    sasl_mechanism: Literal["PLAIN", "SCRAM-SHA-256", "SCRAM-SHA-512", "GSSAPI", "OAUTHBEARER"] | None = None
    sasl_username: str | None = None
    sasl_password: str | None = Field(default=None, description="Secret reference")
    ssl_ca_location: str | None = None
    ssl_certificate_location: str | None = None
    ssl_key_location: str | None = None
    ssl_key_password: str | None = None
    ssl_verify: bool = True
    consumer_group_prefix: str = "reconx"
    schema_registry_url: str | None = None
    extra_properties: dict[str, str] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _validate(self) -> KafkaConnectionConfig:
        if self.security_protocol.startswith("SASL") and not self.sasl_mechanism:
            raise ValueError("SASL security protocol requires 'saslMechanism'")
        return self


class FilesystemConnectionConfig(BaseConnectionConfig):
    base_path: str = "/"
    writable: bool = True
    create_missing_directories: bool = True


class SmtpConnectionConfig(BaseConnectionConfig):
    host: str
    port: int = 587
    username: str | None = None
    password: str | None = None
    use_tls: bool = True
    use_ssl: bool = False
    from_address: str = "reconx@example.com"
    from_name: str = "ReconX Platform"


CONFIG_BY_TYPE: dict[ConnectionType, type[BaseConnectionConfig]] = {
    ConnectionType.S3: S3ConnectionConfig,
    ConnectionType.STORAGEGRID: StorageGridConnectionConfig,
    ConnectionType.SFTP: SftpConnectionConfig,
    ConnectionType.JDBC: JdbcConnectionConfig,
    ConnectionType.KAFKA: KafkaConnectionConfig,
    ConnectionType.FILESYSTEM: FilesystemConnectionConfig,
    ConnectionType.SMTP: SmtpConnectionConfig,
}


class ConnectionDefinition(ReconXModel):
    """A named, environment-scoped connection to an external system."""

    model_config = ConfigDict(
        alias_generator=ReconXModel.model_config["alias_generator"],
        populate_by_name=True,
        extra="forbid",
        str_strip_whitespace=True,
    )

    connection_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9_.-]{1,127}$")
    name: str
    description: str | None = None
    type: ConnectionType
    environment: str = "default"
    enabled: bool = True
    tags: list[str] = Field(default_factory=list)
    config: dict[str, Any] = Field(default_factory=dict)
    created_by: str | None = None
    created_at: datetime | None = None
    updated_by: str | None = None
    updated_at: datetime | None = None
    last_tested_at: datetime | None = None
    last_test_result: str | None = None

    @model_validator(mode="after")
    def _validate_config(self) -> ConnectionDefinition:
        parse_connection_config(self.type, self.config)
        return self

    def typed_config(self) -> BaseConnectionConfig:
        return parse_connection_config(self.type, self.config)

    def masked(self) -> dict[str, Any]:
        """Representation safe to return over the API / render in the UI."""
        data = self.dump()
        data["config"] = mask_secrets(data.get("config", {}))
        return data


def parse_connection_config(conn_type: ConnectionType, raw: dict[str, Any]) -> BaseConnectionConfig:
    model = CONFIG_BY_TYPE.get(conn_type)
    if model is None:
        raise ValueError(f"Unsupported connection type '{conn_type}'")
    return model.model_validate(raw)


def mask_secrets(config: dict[str, Any]) -> dict[str, Any]:
    """Replace secret-bearing values with a non-reversible marker."""
    out: dict[str, Any] = {}
    for key, value in config.items():
        if key in SECRET_FIELDS and value:
            out[key] = "********"
        elif isinstance(value, dict):
            out[key] = mask_secrets(value)
        else:
            out[key] = value
    return out
