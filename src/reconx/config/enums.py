"""Enumerations shared by configuration models, engine and UI."""

from __future__ import annotations

from enum import Enum


class StrEnum(str, Enum):
    def __str__(self) -> str:  # pragma: no cover - trivial
        return str(self.value)


class ConnectionType(StrEnum):
    S3 = "s3"
    STORAGEGRID = "storagegrid"
    SFTP = "sftp"
    JDBC = "jdbc"
    FILESYSTEM = "filesystem"
    KAFKA = "kafka"
    SMTP = "smtp"


class SourceType(StrEnum):
    S3 = "s3"
    STORAGEGRID = "storagegrid"
    SFTP = "sftp"
    JDBC = "jdbc"
    FILESYSTEM = "filesystem"
    KAFKA = "kafka"
    EXCEL = "excel"
    TEMP_VIEW = "temp_view"
    LEG_OUTPUT = "leg_output"
    INLINE = "inline"


class FileFormat(StrEnum):
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"
    EXCEL = "excel"
    ORC = "orc"
    AVRO = "avro"
    TEXT = "text"
    DELIMITED = "delimited"


class DefinitionStatus(StrEnum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    ARCHIVED = "ARCHIVED"


class RunStatus(StrEnum):
    QUEUED = "QUEUED"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    SKIPPED = "SKIPPED"
    WAITING_FOR_DATA = "WAITING_FOR_DATA"

    @property
    def is_terminal(self) -> bool:
        return self in _TERMINAL_STATUSES

    @property
    def is_active(self) -> bool:
        return self in _ACTIVE_STATUSES


_TERMINAL_STATUSES = frozenset(
    {
        RunStatus.SUCCESS,
        RunStatus.PARTIAL_SUCCESS,
        RunStatus.FAILED,
        RunStatus.CANCELLED,
        RunStatus.SKIPPED,
    }
)
_ACTIVE_STATUSES = frozenset(
    {RunStatus.QUEUED, RunStatus.STARTING, RunStatus.RUNNING, RunStatus.WAITING_FOR_DATA}
)


class TriggerType(StrEnum):
    SCHEDULED = "SCHEDULED"
    MANUAL = "MANUAL"
    API = "API"
    EVENT = "EVENT"
    DEPENDENCY = "DEPENDENCY"
    RETRY = "RETRY"
    BACKFILL = "BACKFILL"


class ScheduleType(StrEnum):
    CRON = "cron"
    INTERVAL = "interval"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    ONCE = "once"
    EVENT = "event"
    MANUAL = "manual"


class ConditionOperator(StrEnum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"


class ConditionType(StrEnum):
    ALWAYS = "always"
    FILE_EXISTS = "file_exists"
    S3_FILE_EXISTS = "s3_file_exists"
    SFTP_FILE_EXISTS = "sftp_file_exists"
    FILE_COUNT = "file_count"
    FILE_SIZE = "file_size"
    JDBC_QUERY = "jdbc_query"
    CUSTOM_SQL = "custom_sql"
    KAFKA_AVAILABLE = "kafka_available"
    PREVIOUS_RUN_SUCCESSFUL = "previous_run_successful"
    RECONCILIATION_SUCCEEDED = "reconciliation_succeeded"


class LogicalOperator(StrEnum):
    """Boolean operator used to combine matching rules / comparisons."""

    AND = "AND"
    OR = "OR"


class ComparisonRule(StrEnum):
    EXACT = "exact"
    CASE_INSENSITIVE = "case_insensitive"
    TRIMMED = "trimmed"
    NUMERIC_EXACT = "numeric_exact"
    NUMERIC_TOLERANCE = "numeric_tolerance"
    PERCENTAGE_TOLERANCE = "percentage_tolerance"
    DATE_TOLERANCE = "date_tolerance"
    DATE_ONLY = "date_only"
    EXPRESSION = "expression"
    CONTAINS = "contains"
    ALWAYS_MATCH = "always_match"


class AggregateFunction(StrEnum):
    COUNT = "COUNT"
    COUNT_DISTINCT = "COUNT_DISTINCT"
    SUM = "SUM"
    MIN = "MIN"
    MAX = "MAX"
    AVG = "AVG"


class MatchCategory(StrEnum):
    MATCHED = "MATCHED"
    MISMATCH = "MISMATCH"
    LEFT_ONLY = "LEFT_ONLY"
    RIGHT_ONLY = "RIGHT_ONLY"
    DUPLICATE_LEFT = "DUPLICATE_LEFT"
    DUPLICATE_RIGHT = "DUPLICATE_RIGHT"
    DUPLICATE_BOTH = "DUPLICATE_BOTH"
    MISSING = "MISSING"


DUPLICATE_CATEGORIES = frozenset(
    {MatchCategory.DUPLICATE_LEFT, MatchCategory.DUPLICATE_RIGHT, MatchCategory.DUPLICATE_BOTH}
)
EXCEPTION_CATEGORIES = frozenset(
    {
        MatchCategory.MISMATCH,
        MatchCategory.LEFT_ONLY,
        MatchCategory.RIGHT_ONLY,
        MatchCategory.DUPLICATE_LEFT,
        MatchCategory.DUPLICATE_RIGHT,
        MatchCategory.DUPLICATE_BOTH,
        MatchCategory.MISSING,
    }
)


class TransformType(StrEnum):
    SELECT = "select"
    DROP = "drop"
    RENAME = "rename"
    CAST = "cast"
    FILTER = "filter"
    DERIVE = "derive"
    SQL = "sql"
    TEMP_VIEW = "temp_view"
    DEDUPLICATE = "deduplicate"
    DISTINCT = "distinct"
    AGGREGATE = "aggregate"
    JOIN = "join"
    UNION = "union"
    FILL_NULL = "fill_null"
    DROP_NULL = "drop_null"
    NORMALIZE = "normalize"
    DATE_FORMAT = "date_format"
    STRING_OP = "string_op"
    LIMIT = "limit"
    ORDER_BY = "order_by"
    REPARTITION = "repartition"


class DataQualityCheckType(StrEnum):
    SCHEMA = "schema"
    NOT_NULL = "not_null"
    UNIQUE = "unique"
    ROW_COUNT = "row_count"
    COLUMN_EXISTS = "column_exists"
    DATA_TYPE = "data_type"
    DATE_VALID = "date_valid"
    RANGE = "range"
    REGEX = "regex"
    CUSTOM_SQL = "custom_sql"


class DataQualityAction(StrEnum):
    STOP = "STOP"
    CONTINUE_WITH_WARNING = "CONTINUE_WITH_WARNING"


class SchemaMode(StrEnum):
    INFER = "infer"
    EXPLICIT = "explicit"
    VALIDATE = "validate"
    EVOLVE = "evolve"


class WriteMode(StrEnum):
    APPEND = "append"
    OVERWRITE = "overwrite"
    ERROR_IF_EXISTS = "errorifexists"
    IGNORE = "ignore"


class OutputType(StrEnum):
    JDBC = "jdbc"
    S3 = "s3"
    STORAGEGRID = "storagegrid"
    FILESYSTEM = "filesystem"
    KAFKA = "kafka"
    TEMP_VIEW = "temp_view"
    SFTP = "sftp"
    NONE = "none"


class EventFailureMode(StrEnum):
    FAIL_RUN = "FAIL_RUN"
    WARN_ONLY = "WARN_ONLY"
    RETRY = "RETRY"


class NotifyOn(StrEnum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    DATA_UNAVAILABLE = "DATA_UNAVAILABLE"
    EXCEPTION_THRESHOLD = "EXCEPTION_THRESHOLD"
    CANCELLED = "CANCELLED"


class AdviceCategory(StrEnum):
    """Categories emitted by the reconciliation advisor."""

    KEY_SELECTION = "KEY_SELECTION"
    MATCHING_RULE = "MATCHING_RULE"
    NORMALIZATION = "NORMALIZATION"
    TOLERANCE = "TOLERANCE"
    DATA_QUALITY = "DATA_QUALITY"
    DUPLICATES = "DUPLICATES"
    COVERAGE = "COVERAGE"
    PERFORMANCE = "PERFORMANCE"
    OPERATIONS = "OPERATIONS"


class AdviceSeverity(StrEnum):
    INFO = "INFO"
    SUGGESTION = "SUGGESTION"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


class Role(StrEnum):
    ADMIN = "ADMIN"
    OPERATOR = "OPERATOR"
    DEVELOPER = "DEVELOPER"
    VIEWER = "VIEWER"
    AUDITOR = "AUDITOR"


class Permission(StrEnum):
    RECON_VIEW = "recon:view"
    RECON_CREATE = "recon:create"
    RECON_EDIT = "recon:edit"
    RECON_ACTIVATE = "recon:activate"
    RECON_DISABLE = "recon:disable"
    RECON_DELETE = "recon:delete"
    RECON_EXECUTE = "recon:execute"
    RUN_VIEW = "run:view"
    RUN_CANCEL = "run:cancel"
    CONNECTION_VIEW = "connection:view"
    CONNECTION_MANAGE = "connection:manage"
    CONNECTION_TEST = "connection:test"
    SCHEDULE_VIEW = "schedule:view"
    SCHEDULE_MANAGE = "schedule:manage"
    REPORT_VIEW = "report:view"
    EXCEPTION_VIEW = "exception:view"
    AUDIT_VIEW = "audit:view"
    USER_MANAGE = "user:manage"
    SYSTEM_MANAGE = "system:manage"
