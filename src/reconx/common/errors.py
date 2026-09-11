"""Exception hierarchy for ReconX.

Every error carries an explicit ``retryable`` flag so the retry helper in
:mod:`reconx.common.retry` never spins forever on a permanent failure
(bad credentials, invalid configuration, schema mismatch...).
"""

from __future__ import annotations

from typing import Any


class ReconXError(Exception):
    """Base class for all platform errors."""

    retryable: bool = False
    code: str = "RECONX_ERROR"

    def __init__(self, message: str, *, details: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "message": self.message,
            "retryable": self.retryable,
            "details": self.details,
        }


class ConfigurationError(ReconXError):
    """Invalid / inconsistent configuration supplied by a user."""

    code = "CONFIGURATION_ERROR"


class ValidationError(ConfigurationError):
    code = "VALIDATION_ERROR"


class CyclicDependencyError(ValidationError):
    code = "CYCLIC_DEPENDENCY"


class NotFoundError(ReconXError):
    code = "NOT_FOUND"


class ConflictError(ReconXError):
    code = "CONFLICT"


class AuthenticationError(ReconXError):
    code = "AUTHENTICATION_ERROR"


class AuthorizationError(ReconXError):
    code = "AUTHORIZATION_ERROR"


class SecretResolutionError(ReconXError):
    code = "SECRET_RESOLUTION_ERROR"


class ConnectorError(ReconXError):
    """Base class for connector failures."""

    code = "CONNECTOR_ERROR"


class ConnectionFailedError(ConnectorError):
    code = "CONNECTION_FAILED"
    retryable = True


class UnsupportedFormatError(ConnectorError):
    code = "UNSUPPORTED_FORMAT"


class SchemaMismatchError(ReconXError):
    code = "SCHEMA_MISMATCH"


class DataQualityError(ReconXError):
    code = "DATA_QUALITY_FAILED"


class DataUnavailableError(ReconXError):
    code = "DATA_UNAVAILABLE"


class TransformationError(ReconXError):
    code = "TRANSFORMATION_ERROR"


class ReconciliationError(ReconXError):
    code = "RECONCILIATION_ERROR"


class EventPublishError(ReconXError):
    code = "EVENT_PUBLISH_ERROR"
    retryable = True


class NotificationError(ReconXError):
    code = "NOTIFICATION_ERROR"
    retryable = True


class MetricsPersistenceError(ReconXError):
    code = "METRICS_PERSISTENCE_ERROR"
    retryable = True


class LockAcquisitionError(ReconXError):
    code = "LOCK_NOT_ACQUIRED"


class DuplicateRunError(ConflictError):
    code = "DUPLICATE_RUN"


class JobSubmissionError(ReconXError):
    code = "JOB_SUBMISSION_ERROR"
    retryable = True


class TimeoutExceededError(ReconXError):
    code = "TIMEOUT_EXCEEDED"


RETRYABLE_CODES = frozenset(
    e.code
    for e in (
        ConnectionFailedError,
        EventPublishError,
        NotificationError,
        MetricsPersistenceError,
        JobSubmissionError,
    )
)
