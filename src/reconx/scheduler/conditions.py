"""Data-availability condition evaluation.

A reconciliation can declare "run at 02:00, **but only if** the data is
there".  Conditions form a boolean tree (AND / OR / NOT, nested arbitrarily)
whose leaves probe the outside world: files on S3/SFTP/disk, row counts in a
database, messages on a Kafka topic, or the outcome of another reconciliation.

Evaluation is *explainable*: every leaf returns the evidence it saw, so the UI
can show an officer exactly which condition is holding a run back.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import timedelta
from typing import Any

from reconx.common.errors import ConfigurationError, ConnectionFailedError
from reconx.common.logging import get_logger
from reconx.common.retry import RetryPolicy, call_with_retry
from reconx.common.templating import render_deep
from reconx.common.timeutils import utcnow
from reconx.config.connections import SECRET_FIELDS
from reconx.config.enums import ConditionOperator, ConditionType, RunStatus, SourceType
from reconx.config.models import ConditionSpec
from reconx.connectors import get_connector
from reconx.security.secrets import SecretResolver, get_secret_resolver

log = get_logger(__name__)


@dataclass
class ConditionResult:
    """The outcome of one condition (leaf or composite)."""

    satisfied: bool
    description: str
    condition_type: str
    details: dict[str, Any] = field(default_factory=dict)
    children: list[ConditionResult] = field(default_factory=list)
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "satisfied": self.satisfied,
            "description": self.description,
            "type": self.condition_type,
            "details": self.details,
            "error": self.error,
            "children": [c.to_dict() for c in self.children],
        }

    def summary(self) -> str:
        """One-line explanation suitable for a run record or a UI badge."""
        if self.satisfied:
            return f"All conditions satisfied: {self.description}"
        unmet = self.unsatisfied_leaves()
        if not unmet:
            return f"Condition not satisfied: {self.description}"
        return "Waiting for: " + "; ".join(leaf.description for leaf in unmet[:4])

    def unsatisfied_leaves(self) -> list[ConditionResult]:
        if not self.children:
            return [] if self.satisfied else [self]
        out: list[ConditionResult] = []
        for child in self.children:
            out.extend(child.unsatisfied_leaves())
        return out


class ConditionEvaluator:
    """Evaluates a condition tree against live systems."""

    def __init__(
        self,
        connections: Any,
        *,
        run_repository: Any | None = None,
        secret_resolver: SecretResolver | None = None,
        variables: dict[str, Any] | None = None,
        retry_policy: RetryPolicy | None = None,
    ) -> None:
        self.connections = connections
        self.run_repository = run_repository
        self.secrets = secret_resolver or get_secret_resolver()
        self.variables = variables or {}
        self.retry_policy = retry_policy or RetryPolicy(max_attempts=2, initial_delay_seconds=2.0)

    # ------------------------------------------------------------- dispatch
    def evaluate(self, condition: ConditionSpec | None, *, recon_id: str | None = None) -> ConditionResult:
        if condition is None:
            return ConditionResult(True, "no conditions configured", "always")
        if condition.is_composite:
            return self._evaluate_composite(condition, recon_id=recon_id)
        return self._evaluate_leaf(condition, recon_id=recon_id)

    def _evaluate_composite(self, condition: ConditionSpec, *, recon_id: str | None) -> ConditionResult:
        operator = condition.operator or ConditionOperator.AND
        children = [self.evaluate(child, recon_id=recon_id) for child in condition.conditions]

        if operator == ConditionOperator.AND:
            satisfied = all(child.satisfied for child in children)
        elif operator == ConditionOperator.OR:
            satisfied = any(child.satisfied for child in children)
        else:  # NOT
            satisfied = not children[0].satisfied

        description = (
            f"NOT ({children[0].description})"
            if operator == ConditionOperator.NOT
            else f" {operator.value} ".join(f"({c.description})" for c in children)
        )
        return ConditionResult(
            satisfied=satisfied,
            description=condition.description or description,
            condition_type=operator.value,
            children=children,
        )

    def _evaluate_leaf(self, condition: ConditionSpec, *, recon_id: str | None) -> ConditionResult:
        rendered = ConditionSpec.model_validate(
            render_deep(condition.model_dump(by_alias=True), self.variables, strict=False)
        )
        kind = rendered.type or ConditionType.ALWAYS
        handlers = {
            ConditionType.ALWAYS: self._always,
            ConditionType.FILE_EXISTS: self._file_exists,
            ConditionType.S3_FILE_EXISTS: self._file_exists,
            ConditionType.SFTP_FILE_EXISTS: self._file_exists,
            ConditionType.FILE_COUNT: self._file_count,
            ConditionType.FILE_SIZE: self._file_size,
            ConditionType.JDBC_QUERY: self._jdbc_query,
            ConditionType.CUSTOM_SQL: self._jdbc_query,
            ConditionType.KAFKA_AVAILABLE: self._kafka_available,
            ConditionType.PREVIOUS_RUN_SUCCESSFUL: self._previous_run,
            ConditionType.RECONCILIATION_SUCCEEDED: self._previous_run,
        }
        handler = handlers.get(kind)
        if handler is None:  # pragma: no cover - enum is exhaustive
            raise ConfigurationError(f"Unsupported condition type '{kind}'")
        try:
            result = handler(rendered, recon_id)
        except ConnectionFailedError as exc:
            result = ConditionResult(
                False,
                f"{kind.value}: source unreachable ({exc.message})",
                kind.value,
                error=exc.message,
            )
        except Exception as exc:
            log.error("condition.evaluation_failed", type=kind.value, error=str(exc)[:300])
            result = ConditionResult(
                False, f"{kind.value}: evaluation failed ({exc})", kind.value, error=str(exc)[:500]
            )
        if rendered.negate:
            result.satisfied = not result.satisfied
            result.description = f"NOT ({result.description})"
        log.info(
            "condition.evaluated",
            type=kind.value,
            satisfied=result.satisfied,
            description=result.description[:160],
        )
        return result

    # ---------------------------------------------------------------- leaves
    def _always(self, condition: ConditionSpec, recon_id: str | None) -> ConditionResult:
        return ConditionResult(True, "always true", ConditionType.ALWAYS.value)

    def _resolved_connection(self, connection_ref: str | None) -> tuple[Any, dict[str, Any]]:
        if not connection_ref:
            raise ConfigurationError("Condition requires a connectionRef")
        connection = self.connections.get(connection_ref)
        config = self.secrets.resolve_mapping(connection.config, SECRET_FIELDS)
        return connection, render_deep(config, self.variables, strict=False)

    def _list_files(self, condition: ConditionSpec) -> tuple[list[Any], dict[str, Any]]:
        if condition.connection_ref:
            connection, config = self._resolved_connection(condition.connection_ref)
            source_type = SourceType(str(connection.type))
        else:
            config = {"basePath": "/"}
            source_type = SourceType.FILESYSTEM
        connector = get_connector(source_type)
        path = condition.path or ""
        files = call_with_retry(
            lambda: connector.list_files(config, path, condition.file_pattern),
            policy=self.retry_policy,
            operation=f"condition.list.{source_type.value}",
        )
        files = [f for f in files if not f.is_directory]
        return files, {"path": path, "pattern": condition.file_pattern, "connector": source_type.value}

    def _file_exists(self, condition: ConditionSpec, recon_id: str | None) -> ConditionResult:
        files, context = self._list_files(condition)
        qualifying = [f for f in files if f.size_bytes >= max(0, condition.min_size_bytes)]
        satisfied = len(qualifying) >= max(1, condition.min_count)
        description = (
            f"{len(qualifying)} file(s) at {context['path']}"
            + (f" matching '{condition.file_pattern}'" if condition.file_pattern else "")
            + f" (need {max(1, condition.min_count)})"
        )
        return ConditionResult(
            satisfied,
            description,
            (condition.type or ConditionType.FILE_EXISTS).value,
            details={
                **context,
                "matched": len(files),
                "qualifying": len(qualifying),
                "totalBytes": sum(f.size_bytes for f in files),
                "sample": [f.to_dict() for f in files[:5]],
            },
        )

    def _file_count(self, condition: ConditionSpec, recon_id: str | None) -> ConditionResult:
        files, context = self._list_files(condition)
        count = len(files)
        satisfied = count >= condition.min_count and (
            condition.max_count is None or count <= condition.max_count
        )
        bounds = f"min {condition.min_count}" + (
            f", max {condition.max_count}" if condition.max_count is not None else ""
        )
        return ConditionResult(
            satisfied,
            f"{count} file(s) at {context['path']} ({bounds})",
            ConditionType.FILE_COUNT.value,
            details={**context, "count": count, "sample": [f.to_dict() for f in files[:5]]},
        )

    def _file_size(self, condition: ConditionSpec, recon_id: str | None) -> ConditionResult:
        files, context = self._list_files(condition)
        total = sum(f.size_bytes for f in files)
        largest = max((f.size_bytes for f in files), default=0)
        satisfied = bool(files) and largest >= condition.min_size_bytes
        return ConditionResult(
            satisfied,
            f"largest file at {context['path']} is {largest:,} bytes "
            f"(need >= {condition.min_size_bytes:,})",
            ConditionType.FILE_SIZE.value,
            details={**context, "totalBytes": total, "largestBytes": largest, "fileCount": len(files)},
        )

    def _jdbc_query(self, condition: ConditionSpec, recon_id: str | None) -> ConditionResult:
        from reconx.connectors.jdbc import JdbcConnector

        _, config = self._resolved_connection(condition.connection_ref)
        value = call_with_retry(
            lambda: JdbcConnector().execute_scalar(config, condition.query or ""),
            policy=self.retry_policy,
            operation="condition.jdbc_query",
        )
        satisfied, explanation = _compare(value, condition)
        return ConditionResult(
            satisfied,
            f"query returned {value!r}; {explanation}",
            (condition.type or ConditionType.JDBC_QUERY).value,
            details={"value": _jsonable(value), "comparator": condition.comparator, "threshold": condition.threshold},
        )

    def _kafka_available(self, condition: ConditionSpec, recon_id: str | None) -> ConditionResult:
        from reconx.connectors.kafka import KafkaConnector

        _, config = self._resolved_connection(condition.connection_ref)
        since_ms = None
        if condition.lookback_hours:
            since_ms = int((utcnow() - timedelta(hours=condition.lookback_hours)).timestamp() * 1000)
        info = call_with_retry(
            lambda: KafkaConnector().message_count(config, condition.topic or "", since_ms=since_ms),
            policy=self.retry_policy,
            operation="condition.kafka",
        )
        available = int(info.get("totalMessages", 0))
        satisfied = available >= condition.min_messages
        window = f" in the last {condition.lookback_hours}h" if condition.lookback_hours else ""
        return ConditionResult(
            satisfied,
            f"{available:,} message(s) on '{condition.topic}'{window} (need {condition.min_messages})",
            ConditionType.KAFKA_AVAILABLE.value,
            details=info,
        )

    def _previous_run(self, condition: ConditionSpec, recon_id: str | None) -> ConditionResult:
        target = condition.recon_id or recon_id
        if not target:
            raise ConfigurationError("previous_run condition needs a reconciliation id")
        if self.run_repository is None:
            raise ConfigurationError("previous_run condition requires the run repository")
        cutoff = utcnow() - timedelta(hours=condition.lookback_hours)
        runs = self.run_repository.list(recon_id=target, since=cutoff, limit=20)
        successful = [
            run
            for run in runs
            if run.get("status") in (RunStatus.SUCCESS.value, RunStatus.PARTIAL_SUCCESS.value)
        ]
        satisfied = bool(successful)
        latest = successful[0] if successful else (runs[0] if runs else None)
        return ConditionResult(
            satisfied,
            (
                f"'{target}' succeeded at {latest.get('endTime') or latest.get('createdAt')}"
                if satisfied and latest
                else f"'{target}' has no successful run in the last {condition.lookback_hours}h"
            ),
            (condition.type or ConditionType.PREVIOUS_RUN_SUCCESSFUL).value,
            details={
                "reconId": target,
                "lookbackHours": condition.lookback_hours,
                "runsChecked": len(runs),
                "lastStatus": (latest or {}).get("status"),
                "lastRunId": (latest or {}).get("runId"),
            },
        )


def _compare(value: Any, condition: ConditionSpec) -> tuple[bool, str]:
    """Compare a scalar query result against the configured expectation."""
    if condition.expected is not None:
        satisfied = str(value) == str(condition.expected)
        return satisfied, f"expected {condition.expected!r}"
    numeric: float | None
    try:
        numeric = float(value) if value is not None else None
    except (TypeError, ValueError):
        numeric = None
    if numeric is None:
        satisfied = bool(value)
        return satisfied, "non-numeric result treated as a boolean"
    threshold = float(condition.threshold)
    comparisons = {
        "gt": (numeric > threshold, ">"),
        "gte": (numeric >= threshold, ">="),
        "lt": (numeric < threshold, "<"),
        "lte": (numeric <= threshold, "<="),
        "eq": (numeric == threshold, "=="),
        "ne": (numeric != threshold, "!="),
    }
    satisfied, symbol = comparisons.get(condition.comparator, (numeric > threshold, ">"))
    return satisfied, f"needs {symbol} {threshold:g}"


def _jsonable(value: Any) -> Any:
    from datetime import date, datetime
    from decimal import Decimal

    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return float(value)
    return value
