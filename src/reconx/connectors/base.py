"""Connector abstraction and registry."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import TYPE_CHECKING, Any

from reconx.common.errors import ConfigurationError, ConnectorError
from reconx.common.logging import get_logger
from reconx.common.retry import RetryPolicy
from reconx.config.connections import ConnectionDefinition
from reconx.config.enums import SourceType
from reconx.config.models import OutputSpec, SourceSpec

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, SparkSession

log = get_logger(__name__)


@dataclass
class ConnectionTestResult:
    """Outcome of a ``Test Connection`` action."""

    success: bool
    message: str
    latency_ms: int | None = None
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "success": self.success,
            "message": self.message,
            "latencyMs": self.latency_ms,
            "details": self.details,
        }


@dataclass
class FileInfo:
    """A file/object discovered by a connector (used by availability conditions)."""

    path: str
    size_bytes: int = 0
    modified_at: datetime | None = None
    is_directory: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "sizeBytes": self.size_bytes,
            "modifiedAt": self.modified_at.isoformat() if self.modified_at else None,
            "isDirectory": self.is_directory,
        }


@dataclass
class SourceContext:
    """Everything a connector needs to read a dataset."""

    source: SourceSpec
    connection: ConnectionDefinition | None = None
    resolved_config: dict[str, Any] = field(default_factory=dict)
    variables: dict[str, Any] = field(default_factory=dict)
    run_id: str | None = None
    recon_id: str | None = None
    leg_id: str | None = None
    staging_dir: str = "/tmp/reconx-staging"  # noqa: S108 - overridden by settings
    retry_policy: RetryPolicy = field(default_factory=RetryPolicy)

    @property
    def path(self) -> str | None:
        return self.source.path

    def option(self, name: str, default: Any = None) -> Any:
        return self.source.options.get(name, default)

    def conn(self, name: str, default: Any = None) -> Any:
        return self.resolved_config.get(name, default)


@dataclass
class OutputContext:
    """Everything a connector needs to write a dataset."""

    output: OutputSpec
    connection: ConnectionDefinition | None = None
    resolved_config: dict[str, Any] = field(default_factory=dict)
    variables: dict[str, Any] = field(default_factory=dict)
    run_id: str | None = None
    recon_id: str | None = None
    leg_id: str | None = None
    staging_dir: str = "/tmp/reconx-staging"  # noqa: S108
    retry_policy: RetryPolicy = field(default_factory=RetryPolicy)

    def option(self, name: str, default: Any = None) -> Any:
        return self.output.options.get(name, default)

    def conn(self, name: str, default: Any = None) -> Any:
        return self.resolved_config.get(name, default)


class DataSourceConnector(ABC):
    """Contract every connector implements.

    ``config`` is a :class:`SourceContext` (read) or :class:`OutputContext`
    (write) carrying the source/output specification, the *resolved* connection
    configuration (secrets already dereferenced) and the run variables.
    """

    #: Source types handled by this connector.
    source_types: tuple[SourceType, ...] = ()
    #: Human readable name shown in the UI.
    display_name: str = ""
    #: Whether the connector can enumerate files (needed by availability conditions).
    supports_listing: bool = False

    @abstractmethod
    def read(self, config: SourceContext, spark: SparkSession) -> DataFrame:
        """Return a Spark DataFrame for the configured dataset."""

    @abstractmethod
    def write(self, dataframe: DataFrame, config: OutputContext) -> dict[str, Any]:
        """Persist ``dataframe``; returns writer metadata (rows written, target...)."""

    @abstractmethod
    def test_connection(self, config: dict[str, Any]) -> ConnectionTestResult:
        """Verify reachability/credentials using a *resolved* connection config."""

    @abstractmethod
    def validate(self, config: dict[str, Any]) -> list[str]:
        """Static validation of a connection config; returns a list of problems."""

    # -- optional capabilities ------------------------------------------------
    def list_files(self, config: dict[str, Any], path: str, pattern: str | None = None) -> list[FileInfo]:
        raise ConnectorError(f"{self.__class__.__name__} does not support file listing")

    def prepare_spark(self, spark: SparkSession, config: dict[str, Any]) -> None:
        """Hook to apply per-connection Hadoop/Spark configuration before reading."""
        return None

    # -- helpers --------------------------------------------------------------
    @staticmethod
    def _require(config: dict[str, Any], *keys: str) -> list[str]:
        return [f"'{key}' is required" for key in keys if not config.get(key)]


_REGISTRY: dict[SourceType, DataSourceConnector] = {}


def register_connector(cls: type[DataSourceConnector]) -> type[DataSourceConnector]:
    """Class decorator registering a connector for its declared source types."""
    instance = cls()
    if not cls.source_types:
        raise ConfigurationError(f"Connector {cls.__name__} declares no source_types")
    for source_type in cls.source_types:
        _REGISTRY[source_type] = instance
    log.debug("connector.registered", connector=cls.__name__, types=[str(t) for t in cls.source_types])
    return cls


def get_connector(source_type: SourceType | str) -> DataSourceConnector:
    key = SourceType(source_type) if not isinstance(source_type, SourceType) else source_type
    connector = _REGISTRY.get(key)
    if connector is None:
        raise ConfigurationError(
            f"No connector registered for source type '{key}'",
            details={"available": [str(t) for t in _REGISTRY]},
        )
    return connector


def available_connectors() -> dict[str, str]:
    return {str(source_type): conn.display_name for source_type, conn in sorted(_REGISTRY.items(), key=str)}
