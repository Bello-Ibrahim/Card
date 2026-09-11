"""Reconciliation job - the Spark application entry point.

Executes one run of one reconciliation definition:

1. load + validate the definition (MongoDB, or a file for offline runs)
2. build the run variables (``${business_date}`` and friends)
3. start Spark and publish ``reconciliation.started``
4. execute the leg DAG stage by stage, each leg producing a temp view that
   later legs can consume
5. write results and exceptions to the configured outputs
6. persist run/leg/field/source metrics to the JDBC metrics database
7. publish the completion event and send notifications

The module is runnable both in-process (``ReconciliationJob(...).run()``) and
via ``spark-submit`` (``python -m reconx.spark.job --recon-id ...``).
"""

from __future__ import annotations

import argparse
import json
import socket
import sys
import time
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any

from reconx.common.errors import (
    DataQualityError,
    NotFoundError,
    ReconXError,
)
from reconx.common.ids import new_run_id
from reconx.common.logging import bind_context, configure_logging, get_logger
from reconx.common.retry import RetryPolicy
from reconx.common.templating import build_run_variables
from reconx.common.timeutils import business_date as compute_business_date
from reconx.common.timeutils import isoformat, utcnow
from reconx.config.connections import ConnectionDefinition
from reconx.config.enums import (
    EventFailureMode,
    NotifyOn,
    OutputType,
    RunStatus,
    TriggerType,
)
from reconx.config.models import (
    LegSpec,
    OutputSpec,
    ReconciliationDefinition,
    declared_variable_defaults,
)
from reconx.config.settings import Settings, get_settings
from reconx.config.validation import validate_definition
from reconx.connectors.temp_view import leg_result_view
from reconx.events.publisher import EventPublisher, NullEventPublisher
from reconx.events.schemas import EventType, ReconciliationEvent
from reconx.metrics.repository import MetricsRepository
from reconx.notifications.base import NotificationContext, should_notify
from reconx.spark.io import (
    ConnectionProvider,
    ResultWriter,
    SourceReader,
    StaticConnectionProvider,
)
from reconx.spark.reconciliation.engine import LegResult, ReconciliationEngine
from reconx.spark.session import create_spark_session, spark_metrics, stop_spark_session

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, SparkSession

log = get_logger(__name__)

METRICS_CONNECTION_ID = "reconx-metrics-db"
#: Cap for the driver-side exception fallback (see _insert_exceptions_via_driver).
EXCEPTION_FALLBACK_LIMIT = 100_000


@dataclass
class RunOptions:
    run_id: str
    business_date: str
    trigger_type: TriggerType = TriggerType.MANUAL
    triggered_by: str = "system"
    parameters: dict[str, Any] = field(default_factory=dict)
    profile_sources: bool = False
    dry_run: bool = False
    node: str = field(default_factory=socket.gethostname)
    persist_metrics: bool = True
    send_notifications: bool = True
    attempt: int = 1


@dataclass
class RunSummary:
    run_id: str
    recon_id: str
    status: RunStatus
    metrics: dict[str, Any] = field(default_factory=dict)
    legs: list[dict[str, Any]] = field(default_factory=list)
    spark_application_id: str | None = None
    error: str | None = None
    started_at: datetime | None = None
    ended_at: datetime | None = None
    profiles: list[dict[str, Any]] = field(default_factory=list)
    data_quality: list[dict[str, Any]] = field(default_factory=list)

    @property
    def duration_ms(self) -> int | None:
        if self.started_at and self.ended_at:
            return int((self.ended_at - self.started_at).total_seconds() * 1000)
        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            "runId": self.run_id,
            "reconId": self.recon_id,
            "status": self.status.value,
            "metrics": self.metrics,
            "legs": self.legs,
            "sparkApplicationId": self.spark_application_id,
            "error": self.error,
            "startedAt": isoformat(self.started_at),
            "endedAt": isoformat(self.ended_at),
            "durationMs": self.duration_ms,
            "dataQuality": self.data_quality,
        }


class ReconciliationJob:
    """Executes a reconciliation definition end to end."""

    def __init__(
        self,
        definition: ReconciliationDefinition,
        connections: ConnectionProvider,
        options: RunOptions,
        *,
        settings: Settings | None = None,
        spark: SparkSession | None = None,
        metrics: MetricsRepository | None = None,
        events: EventPublisher | None = None,
        run_repository: Any | None = None,
        mongo_db: Any | None = None,
    ) -> None:
        self.definition = definition
        self.connections = connections
        self.options = options
        self.settings = settings or get_settings()
        self.spark = spark
        self._owns_spark = spark is None
        self.metrics = metrics
        self.events = events or NullEventPublisher()
        self.run_repository = run_repository
        self.mongo_db = mongo_db
        # Declared variable defaults first, then per-run parameters, then the
        # built-ins (${business_date} and friends) - so a run can override a
        # default without the definition having to repeat it.
        self.variables = build_run_variables(
            recon_id=definition.recon_id,
            run_id=options.run_id,
            biz_date=_parse_date(options.business_date),
            timezone_name=definition.schedule.timezone,
            extra={**declared_variable_defaults(definition), **(options.parameters or {})},
        )
        self.summary = RunSummary(run_id=options.run_id, recon_id=definition.recon_id, status=RunStatus.QUEUED)
        self._leg_results: dict[str, LegResult] = {}
        self._source_metrics: list[dict[str, Any]] = []
        self.retry_policy = RetryPolicy(
            max_attempts=max(1, definition.schedule.retries.max_attempts),
            initial_delay_seconds=definition.schedule.retries.initial_delay_seconds,
            max_delay_seconds=definition.schedule.retries.max_delay_seconds,
            multiplier=definition.schedule.retries.multiplier,
        )

    # ------------------------------------------------------------------ run
    def run(self) -> RunSummary:
        bind_context(
            recon_id=self.definition.recon_id,
            run_id=self.options.run_id,
            business_date=self.options.business_date,
            node=self.options.node,
        )
        self.summary.started_at = utcnow()
        self.summary.status = RunStatus.STARTING

        report = validate_definition(self.definition)
        if not report.valid:
            message = "; ".join(f"{i.path}: {i.message}" for i in report.errors)
            self.summary.status = RunStatus.FAILED
            self.summary.error = f"Configuration is invalid: {message}"
            self.summary.ended_at = utcnow()
            log.error("job.invalid_definition", errors=len(report.errors))
            self._finalise()
            return self.summary

        if self.options.dry_run:
            self.summary.status = RunStatus.SUCCESS
            self.summary.ended_at = utcnow()
            log.info("job.dry_run_ok", stages=len(report.execution_order))
            return self.summary

        try:
            self._ensure_metrics_schema()
            self._start_spark()
            self._record_run_start()
            self._update_run_status(RunStatus.RUNNING)
            self._publish(EventType.STARTED, status=RunStatus.RUNNING.value)
            self._execute_legs(report.execution_order)
            self.summary.status = self._determine_status()
        except DataQualityError as exc:
            self.summary.status = RunStatus.FAILED
            self.summary.error = exc.message
            log.error("job.data_quality_failed", error=exc.message, details=exc.details)
        except ReconXError as exc:
            self.summary.status = RunStatus.FAILED
            self.summary.error = f"{exc.code}: {exc.message}"
            log.error("job.failed", code=exc.code, error=exc.message, details=exc.details)
        except Exception as exc:
            self.summary.status = RunStatus.FAILED
            self.summary.error = f"{type(exc).__name__}: {exc}"
            log.exception("job.unexpected_failure", error=str(exc))
        finally:
            self.summary.ended_at = utcnow()
            self._finalise()
        return self.summary

    # -------------------------------------------------------------- metrics
    def _ensure_metrics_schema(self) -> None:
        """Create missing metrics tables when auto-create is enabled (dev/CI)."""
        if self.metrics is None or not self.options.persist_metrics:
            return
        if not self.settings.result_db.auto_create_schema:
            return
        try:
            self.metrics.create_schema()
        except Exception as exc:
            log.error("job.metrics_schema_failed", error=str(exc))

    def _record_run_start(self) -> None:
        if self.metrics is None or not self.options.persist_metrics:
            return
        try:
            self.metrics.upsert_definition(self.definition.dump())
            self.metrics.record_run_start(
                {
                    "runId": self.options.run_id,
                    "reconId": self.definition.recon_id,
                    "reconName": self.definition.name,
                    "version": self.definition.version,
                    "product": self.definition.product,
                    "customer": self.definition.customer,
                    "environment": self.definition.environment or self.settings.environment,
                    "businessDate": self.options.business_date,
                    "status": RunStatus.RUNNING.value,
                    "triggerType": self.options.trigger_type.value,
                    "triggeredBy": self.options.triggered_by,
                    "node": self.options.node,
                    "sparkApplicationId": self.summary.spark_application_id,
                    "attempt": self.options.attempt,
                    "startTime": self.summary.started_at,
                }
            )
        except Exception as exc:
            log.error("job.run_start_persist_failed", error=str(exc))

    # ---------------------------------------------------------------- spark
    def _start_spark(self) -> None:
        if self.spark is None:
            app_name = f"reconx-{self.definition.recon_id}-{self.options.run_id[:8]}"
            self.spark = create_spark_session(
                app_name, settings=self.settings, overrides=self.definition.spark
            )
        info = spark_metrics(self.spark)
        self.summary.spark_application_id = info.get("sparkApplicationId")
        bind_context(spark_application_id=self.summary.spark_application_id)
        log.info("job.spark_ready", **{k: v for k, v in info.items() if k != "webUrl"})

    # ----------------------------------------------------------------- legs
    def _execute_legs(self, stages: list[list[str]]) -> None:
        legs_by_id = {leg.id: leg for leg in self.definition.enabled_legs}
        for stage_index, stage in enumerate(stages):
            for leg_id in stage:
                leg = legs_by_id.get(leg_id)
                if leg is None:
                    continue
                self._execute_leg(leg, stage_index)
            if self.definition.events.emit_stage_events:
                self._publish(
                    EventType.STAGE_COMPLETED,
                    status=RunStatus.RUNNING.value,
                    details={"stage": stage_index, "legs": stage},
                )

    def _execute_leg(self, leg: LegSpec, stage_index: int) -> None:
        started = utcnow()
        bind_context(leg_id=leg.id)
        log.info("leg.started", leg_id=leg.id, stage=stage_index)
        leg_record: dict[str, Any] = {
            "run_id": self.options.run_id,
            "recon_id": self.definition.recon_id,
            "leg_id": leg.id,
            "leg_name": leg.name or leg.id,
            "status": RunStatus.RUNNING.value,
            "stage": stage_index,
            "start_time": started,
            "left_source": leg.left_source,
            "right_source": leg.right_source,
        }
        try:
            reader = self._reader()
            frames: dict[str, DataFrame] = {}
            read_ms = 0
            for source in leg.sources:
                result = reader.read(source, leg_id=leg.id)
                frames[source.id] = result.dataframe
                read_ms += result.read_time_ms
                self._source_metrics.append(
                    {
                        "runId": self.options.run_id,
                        "reconId": self.definition.recon_id,
                        "legId": leg.id,
                        "sourceId": source.id,
                        "sourceType": source.type.value,
                        "connectionRef": source.connection_ref,
                        "recordsRead": result.row_count,
                        "columnCount": len(result.schema_fields),
                        "readTimeMs": result.read_time_ms,
                        "dataQualityPassed": result.data_quality.passed if result.data_quality else None,
                        "dataQualityDetails": result.data_quality.to_dict() if result.data_quality else None,
                        "schema": result.schema_fields,
                    }
                )
                if result.data_quality:
                    self.summary.data_quality.append(result.data_quality.to_dict())

            left = frames[leg.left_source or leg.sources[0].id]
            right = frames[leg.right_source or leg.sources[-1].id]

            if leg.pre_transformations:
                transformer = reader.transformer
                left = transformer.apply_all(
                    left, leg.pre_transformations, context=f"leg.{leg.id}.pre", sources=frames
                )

            if self.options.profile_sources:
                self._profile(leg, left, right)

            process_started = time.time()
            engine = ReconciliationEngine(self.spark)  # type: ignore[arg-type]
            result = engine.reconcile(leg, left, right)
            result_df = result.result

            if leg.post_transformations:
                result_df = reader.transformer.apply_all(
                    result_df, leg.post_transformations, context=f"leg.{leg.id}.post", sources=frames
                )
                result = LegResult(
                    leg_id=result.leg_id,
                    result=result_df,
                    exceptions=result.exceptions,
                    metrics=result.metrics,
                    field_metrics=result.field_metrics,
                    rule_metrics=result.rule_metrics,
                    aggregate_results=result.aggregate_results,
                    key_description=result.key_description,
                    match_logic_description=result.match_logic_description,
                )

            # Register the result so later legs can consume it as a source.
            view_name = leg.register_result_view or leg_result_view(leg.id)
            result_df.createOrReplaceTempView(view_name)
            for output in leg.outputs:
                if output.type == OutputType.TEMP_VIEW and output.view:
                    result_df.createOrReplaceTempView(output.view)

            result.metrics.read_time_ms = read_ms
            result.metrics.process_time_ms = int((time.time() - process_started) * 1000)

            write_ms = self._write_outputs(leg, result)
            result.metrics.write_time_ms = write_ms

            self._leg_results[leg.id] = result
            leg_record.update(
                {
                    "status": RunStatus.SUCCESS.value,
                    "end_time": utcnow(),
                    "duration_ms": int((utcnow() - started).total_seconds() * 1000),
                    "recon_key": result.key_description[:512],
                    "match_logic": result.match_logic_description[:1024],
                    "left_records": result.metrics.left_records,
                    "right_records": result.metrics.right_records,
                    "matched": result.metrics.matched,
                    "mismatched": result.metrics.mismatched,
                    "left_only": result.metrics.left_only,
                    "right_only": result.metrics.right_only,
                    "duplicates_left": result.metrics.duplicates_left,
                    "duplicates_right": result.metrics.duplicates_right,
                    "duplicate_keys": result.metrics.duplicate_keys,
                    "field_mismatches": result.metrics.field_mismatches,
                    "exceptions": result.metrics.exceptions,
                    "match_percentage": result.metrics.match_percentage,
                    "read_time_ms": result.metrics.read_time_ms,
                    "process_time_ms": result.metrics.process_time_ms,
                    "write_time_ms": result.metrics.write_time_ms,
                }
            )
            log.info(
                "leg.completed",
                leg_id=leg.id,
                matched=result.metrics.matched,
                exceptions=result.metrics.exceptions,
                duration_ms=leg_record["duration_ms"],
            )
            if self.definition.events.emit_stage_events:
                self._publish(
                    EventType.LEG_COMPLETED,
                    status=RunStatus.RUNNING.value,
                    leg_id=leg.id,
                    records_processed=result.metrics.total_records,
                    records_matched=result.metrics.matched,
                    records_unmatched=result.metrics.unmatched,
                    exceptions=result.metrics.exceptions,
                    details={"matchPercentage": result.metrics.match_percentage},
                )
        except Exception as exc:
            leg_record.update(
                {
                    "status": RunStatus.FAILED.value,
                    "end_time": utcnow(),
                    "error_message": f"{type(exc).__name__}: {exc}"[:4000],
                }
            )
            log.error("leg.failed", leg_id=leg.id, error=str(exc))
            self._record_leg(leg_record)
            if not leg.continue_on_failure:
                raise
            return
        finally:
            bind_context(leg_id=None)
        self._record_leg(leg_record)
        self.summary.legs.append(
            {
                **result.metrics.to_dict(),
                "legName": leg.name or leg.id,
                "stage": stage_index,
                "reconKey": result.key_description,
                "matchLogic": result.match_logic_description,
                "ruleMetrics": result.rule_metrics,
                "aggregates": result.aggregate_results,
                "unmatched": result.metrics.unmatched,
            }
        )

    # -------------------------------------------------------------- outputs
    def _write_outputs(self, leg: LegSpec, result: LegResult) -> int:
        writer = ResultWriter(
            self.connections,
            variables=self.variables,
            staging_dir=self.settings.staging_dir,
            retry_policy=self.retry_policy,
            run_id=self.options.run_id,
            recon_id=self.definition.recon_id,
        )
        total_ms = 0
        for output in leg.outputs:
            if output.type == OutputType.TEMP_VIEW:
                continue  # already registered
            outcome = writer.write(result.result, output, leg_id=leg.id)
            total_ms += int(outcome.get("writeTimeMs", 0) or 0)

        if leg.exception_output and leg.exception_output.enabled:
            outcome = writer.write(result.exceptions, leg.exception_output, leg_id=leg.id)
            total_ms += int(outcome.get("writeTimeMs", 0) or 0)
        elif self.options.persist_metrics and self.metrics is not None:
            total_ms += self._write_exceptions_to_metrics_db(leg, result)
        return total_ms

    def _write_exceptions_to_metrics_db(self, leg: LegSpec, result: LegResult) -> int:
        """Persist exceptions to the metrics DB with a distributed JDBC write."""
        from pyspark.sql import functions as F

        started = time.time()
        try:
            # created_at is left to the database's server default: JDBC drivers
            # encode timestamps differently (SQLite stores epoch millis), and the
            # database clock is the authoritative one anyway.
            exceptions = (
                result.exceptions.withColumn("run_id", F.lit(self.options.run_id))
                .withColumn("recon_id", F.lit(self.definition.recon_id))
                .withColumn("business_date", F.lit(self.options.business_date))
                .withColumn("status", F.lit("OPEN"))
            )
            exceptions = exceptions.withColumn(
                "key_components", F.to_json(F.col("key_components"))
            ).withColumn("context_columns", F.to_json(F.col("context_columns")))
            columns = [
                "run_id",
                "recon_id",
                "leg_id",
                "business_date",
                "reconciliation_key",
                "exception_type",
                "source",
                "field",
                "rule",
                "expected_value",
                "actual_value",
                "key_components",
                "context_columns",
                "left_occurrences",
                "right_occurrences",
                "status",
            ]
            output = OutputSpec(
                id=f"{leg.id}_exceptions",
                type=OutputType.JDBC,
                connection_ref=METRICS_CONNECTION_ID,
                table="reconciliation_exceptions",
                mode="append",
                columns=columns,
            )
            writer = ResultWriter(
                self.connections,
                variables=self.variables,
                run_id=self.options.run_id,
                recon_id=self.definition.recon_id,
                retry_policy=self.retry_policy,
            )
            writer.write(exceptions.select(*columns), output, leg_id=leg.id, add_run_columns=False)
        except Exception as exc:
            log.warning(
                "job.exception_jdbc_write_failed",
                leg_id=leg.id,
                error=str(exc).replace("\n", " | ")[:400],
                fallback="driver-side batch insert",
                hint="Add the JDBC driver jar to the Spark classpath for distributed exception writes",
            )
            self._insert_exceptions_via_driver(leg, result)
        return int((time.time() - started) * 1000)

    def _insert_exceptions_via_driver(self, leg: LegSpec, result: LegResult) -> None:
        """Bounded fallback when Spark cannot reach the metrics DB over JDBC.

        Streams rows with ``toLocalIterator`` (one partition at a time, never a
        full ``collect``) and stops at ``EXCEPTION_FALLBACK_LIMIT`` so the driver
        stays bounded regardless of dataset size.
        """
        if self.metrics is None:
            return
        try:
            batch: list[dict[str, Any]] = []
            written = 0
            truncated = False
            for row in result.exceptions.toLocalIterator():
                data = row.asDict(recursive=True)
                batch.append(
                    {
                        "run_id": self.options.run_id,
                        "recon_id": self.definition.recon_id,
                        "leg_id": data.get("leg_id", leg.id),
                        "business_date": self.options.business_date,
                        "reconciliation_key": data.get("reconciliation_key"),
                        "exception_type": data.get("exception_type"),
                        "source": data.get("source"),
                        "field": data.get("field"),
                        "rule": data.get("rule"),
                        "expected_value": data.get("expected_value"),
                        "actual_value": data.get("actual_value"),
                        "key_components": data.get("key_components"),
                        "context_columns": data.get("context_columns"),
                        "left_occurrences": data.get("left_occurrences"),
                        "right_occurrences": data.get("right_occurrences"),
                    }
                )
                if len(batch) >= 1000:
                    written += self.metrics.record_exceptions(batch)
                    batch = []
                if written >= EXCEPTION_FALLBACK_LIMIT:
                    truncated = True
                    break
            if batch:
                written += self.metrics.record_exceptions(batch)
            log.info(
                "job.exceptions_persisted_via_driver",
                leg_id=leg.id,
                written=written,
                truncated=truncated,
            )
            if truncated:
                log.warning(
                    "job.exceptions_truncated",
                    leg_id=leg.id,
                    limit=EXCEPTION_FALLBACK_LIMIT,
                    hint="Configure an exceptionOutput (S3/Parquet/JDBC) for full exception capture",
                )
        except Exception as exc:
            log.error("job.exception_persist_failed", leg_id=leg.id, error=str(exc))

    # -------------------------------------------------------------- profile
    def _profile(self, leg: LegSpec, left: DataFrame, right: DataFrame) -> None:
        from reconx.spark.profiler import profile_summary

        try:
            summary = profile_summary(
                left,
                right,
                left_id=leg.left_source or "left",
                right_id=leg.right_source or "right",
            )
            summary.update(
                {
                    "reconId": self.definition.recon_id,
                    "runId": self.options.run_id,
                    "legId": leg.id,
                    "createdAt": utcnow(),
                }
            )
            self.summary.profiles.append(summary)
            if self.mongo_db is not None:
                from reconx.config.store import Collections

                self.mongo_db[Collections.COLUMN_PROFILES].replace_one(
                    {"runId": self.options.run_id, "legId": leg.id},
                    summary,
                    upsert=True,
                )
            log.info("job.profiled", leg_id=leg.id, key_candidates=len(summary.get("keyCandidates", [])))
        except Exception as exc:
            log.warning("job.profiling_failed", leg_id=leg.id, error=str(exc))

    # --------------------------------------------------------------- status
    def _determine_status(self) -> RunStatus:
        if not self._leg_results:
            return RunStatus.FAILED
        exceptions = sum(r.metrics.exceptions for r in self._leg_results.values())
        for leg in self.definition.enabled_legs:
            result = self._leg_results.get(leg.id)
            if result is None:
                continue
            options = leg.matching
            compared = result.metrics.matched + result.metrics.unmatched
            if options.exception_threshold is not None and result.metrics.exceptions > options.exception_threshold:
                return RunStatus.PARTIAL_SUCCESS
            if options.exception_threshold_percent is not None and compared:
                percentage = result.metrics.exceptions / compared * 100
                if percentage > options.exception_threshold_percent:
                    return RunStatus.PARTIAL_SUCCESS
        if len(self._leg_results) < len(self.definition.enabled_legs):
            # A leg was skipped or tolerated a failure (continueOnFailure).
            return RunStatus.PARTIAL_SUCCESS
        log.debug("job.status_success", exceptions=exceptions)
        return RunStatus.SUCCESS

    def _aggregate_metrics(self) -> dict[str, Any]:
        read = sum(r.metrics.total_records for r in self._leg_results.values())
        matched = sum(r.metrics.matched for r in self._leg_results.values())
        unmatched = sum(r.metrics.unmatched for r in self._leg_results.values())
        return {
            "recordsRead": read,
            "recordsMatched": matched,
            "recordsUnmatched": unmatched,
            "duplicates": sum(
                r.metrics.duplicates_left + r.metrics.duplicates_right for r in self._leg_results.values()
            ),
            "exceptions": sum(r.metrics.exceptions for r in self._leg_results.values()),
            "fieldMismatches": sum(r.metrics.field_mismatches for r in self._leg_results.values()),
            "matchPercentage": round(matched / (matched + unmatched) * 100, 4)
            if (matched + unmatched)
            else None,
            "readTimeMs": sum(r.metrics.read_time_ms for r in self._leg_results.values()),
            "processTimeMs": sum(r.metrics.process_time_ms for r in self._leg_results.values()),
            "writeTimeMs": sum(r.metrics.write_time_ms for r in self._leg_results.values()),
            "legCount": len(self._leg_results),
        }

    # ------------------------------------------------------------- finalise
    def _finalise(self) -> None:
        self.summary.metrics = self._aggregate_metrics()
        self._update_run_status(self.summary.status, error=self.summary.error)
        self._persist_metrics()
        self._publish_completion()
        self._notify()
        if self._owns_spark:
            stop_spark_session(self.spark)
        try:
            self.events.close()
        except Exception as exc:
            log.warning("job.event_flush_failed", error=str(exc))
        log.info(
            "job.finished",
            status=self.summary.status.value,
            duration_ms=self.summary.duration_ms,
            **{k: v for k, v in self.summary.metrics.items() if isinstance(v, (int, float))},
        )

    def _persist_metrics(self) -> None:
        if not self.options.persist_metrics or self.metrics is None:
            return
        try:
            self.metrics.record_run_completion(
                self.options.run_id,
                status=self.summary.status.value,
                metrics=self.summary.metrics,
                error=self.summary.error,
                spark_application_id=self.summary.spark_application_id,
                end_time=self.summary.ended_at,
            )
            if self._source_metrics:
                self.metrics.record_source_metrics(self._source_metrics)
            field_rows: list[dict[str, Any]] = []
            metric_rows: list[dict[str, Any]] = []
            for leg_id, result in self._leg_results.items():
                rule_names = {r["ruleId"]: r["ruleName"] for r in result.rule_metrics}
                for row in result.field_metrics:
                    field_rows.append(
                        {
                            **row,
                            "runId": self.options.run_id,
                            "reconId": self.definition.recon_id,
                            "ruleName": rule_names.get(row.get("ruleId")),
                        }
                    )
                for name, value in result.metrics.to_dict().items():
                    if isinstance(value, (int, float)) and value is not None:
                        metric_rows.append(
                            {
                                "run_id": self.options.run_id,
                                "recon_id": self.definition.recon_id,
                                "leg_id": leg_id,
                                "metric_name": name,
                                "metric_value": value,
                                "metric_type": "COUNTER",
                                "business_date": self.options.business_date,
                            }
                        )
                for aggregate in result.aggregate_results:
                    metric_rows.append(
                        {
                            "run_id": self.options.run_id,
                            "recon_id": self.definition.recon_id,
                            "leg_id": leg_id,
                            "metric_name": f"aggregate.{aggregate['name']}",
                            "metric_value": aggregate.get("difference"),
                            "metric_text": json.dumps(aggregate, default=str)[:1024],
                            "metric_type": "AGGREGATE",
                            "business_date": self.options.business_date,
                        }
                    )
            if field_rows:
                self.metrics.record_field_metrics(field_rows)
            if metric_rows:
                self.metrics.record_metrics(metric_rows)
        except Exception as exc:
            log.error("job.metrics_persist_failed", error=str(exc))

    def _record_leg(self, record: dict[str, Any]) -> None:
        if self.metrics is not None and self.options.persist_metrics:
            try:
                self.metrics.record_leg_run(record)
            except Exception as exc:
                log.error("job.leg_persist_failed", leg_id=record.get("leg_id"), error=str(exc))
        if self.run_repository is not None:
            try:
                self.run_repository.upsert_leg(
                    self.options.run_id,
                    {
                        "legId": record["leg_id"],
                        "status": record["status"],
                        "stage": record.get("stage"),
                        "matched": record.get("matched"),
                        "mismatched": record.get("mismatched"),
                        "leftOnly": record.get("left_only"),
                        "rightOnly": record.get("right_only"),
                        "exceptions": record.get("exceptions"),
                        "matchPercentage": record.get("match_percentage"),
                        "durationMs": record.get("duration_ms"),
                        "errorMessage": record.get("error_message"),
                        "reconKey": record.get("recon_key"),
                        "matchLogic": record.get("match_logic"),
                    },
                )
            except Exception as exc:
                log.warning("job.leg_state_update_failed", error=str(exc))

    def _update_run_status(self, status: RunStatus, *, error: str | None = None) -> None:
        if self.run_repository is None:
            return
        try:
            self.run_repository.update_status(
                self.options.run_id,
                status,
                error=error,
                spark_application_id=self.summary.spark_application_id,
                metrics=self.summary.metrics or None,
            )
        except Exception as exc:
            log.warning("job.run_state_update_failed", status=status.value, error=str(exc))

    def _publish(self, event_type: str, **kwargs: Any) -> None:
        if not self.definition.events.enabled:
            return
        event = ReconciliationEvent(
            event_type=event_type,
            recon_id=self.definition.recon_id,
            run_id=self.options.run_id,
            version=self.definition.version,
            product=self.definition.product,
            customer=self.definition.customer,
            environment=self.definition.environment,
            business_date=self.options.business_date,
            node=self.options.node,
            spark_application_id=self.summary.spark_application_id,
            **kwargs,
        )
        try:
            self.events.publish(event)
        except Exception as exc:
            if self.definition.events.on_failure == EventFailureMode.FAIL_RUN:
                raise
            log.warning("job.event_publish_failed", event_type=event_type, error=str(exc))

    def _publish_completion(self) -> None:
        metrics = self.summary.metrics
        event_type = (
            EventType.COMPLETED
            if self.summary.status in (RunStatus.SUCCESS, RunStatus.PARTIAL_SUCCESS)
            else EventType.FAILED
        )
        self._publish(
            event_type,
            status=self.summary.status.value,
            records_processed=metrics.get("recordsRead"),
            records_matched=metrics.get("recordsMatched"),
            records_unmatched=metrics.get("recordsUnmatched"),
            exceptions=metrics.get("exceptions"),
            duplicates=metrics.get("duplicates"),
            duration_ms=self.summary.duration_ms,
            match_percentage=metrics.get("matchPercentage"),
            message=self.summary.error,
            details={"legs": [leg.get("legId") for leg in self.summary.legs]}
            if self.definition.events.include_metrics
            else {},
        )

    def _notify(self) -> None:
        if not self.options.send_notifications:
            return
        email_config = self.definition.notifications.email
        exceptions = int(self.summary.metrics.get("exceptions", 0) or 0)
        breached = bool(
            email_config.exception_threshold is not None
            and exceptions > email_config.exception_threshold
        )
        reason = should_notify(
            self.summary.status.value, email_config.on, exception_threshold_breached=breached
        )
        if reason is None:
            return
        try:
            from reconx.notifications.email import EmailNotifier

            sample: list[dict[str, Any]] = []
            if email_config.include_exception_sample and self.metrics is not None:
                try:
                    sample = self.metrics.list_exceptions(
                        run_id=self.options.run_id, limit=email_config.exception_sample_size
                    )
                except Exception as exc:
                    log.debug("job.exception_sample_unavailable", error=str(exc))
            context = NotificationContext(
                recon_id=self.definition.recon_id,
                recon_name=self.definition.name,
                run_id=self.options.run_id,
                status=self.summary.status.value,
                business_date=self.options.business_date,
                trigger=self.options.trigger_type.value,
                started_at=isoformat(self.summary.started_at),
                ended_at=isoformat(self.summary.ended_at),
                duration_ms=self.summary.duration_ms,
                metrics=self.summary.metrics,
                legs=self.summary.legs,
                exceptions_sample=sample,
                error_message=self.summary.error,
                product=self.definition.product,
                customer=self.definition.customer,
                environment=self.definition.environment or self.settings.environment,
                spark_application_id=self.summary.spark_application_id,
                ui_url=f"{self.settings.api.base_url}/runs/{self.options.run_id}",
                notify_reason=reason if isinstance(reason, NotifyOn) else NotifyOn.SUCCESS,
            )
            EmailNotifier(self.settings).send(context, email_config)
        except Exception as exc:
            log.error("job.notification_failed", error=str(exc))

    def _reader(self) -> SourceReader:
        return SourceReader(
            self.spark,  # type: ignore[arg-type]
            self.connections,
            variables=self.variables,
            staging_dir=self.settings.staging_dir,
            retry_policy=self.retry_policy,
            run_id=self.options.run_id,
            recon_id=self.definition.recon_id,
        )


# --------------------------------------------------------------------------- #
# Wiring helpers
# --------------------------------------------------------------------------- #
def metrics_connection(settings: Settings | None = None) -> ConnectionDefinition:
    """Expose the platform metrics DB as a regular JDBC connection."""
    settings = settings or get_settings()
    result_db = settings.result_db
    return ConnectionDefinition(
        connectionId=METRICS_CONNECTION_ID,
        name="ReconX metrics database",
        type="jdbc",
        config={
            "jdbcUrl": result_db.jdbc_url,
            "driver": result_db.jdbc_driver,
            "username": result_db.jdbc_user,
            "password": result_db.jdbc_password,
            "databaseType": _vendor_of(result_db.jdbc_url),
            "schema": result_db.schema_name if result_db.schema_name != "public" else None,
        },
    )


def _vendor_of(jdbc_url: str) -> str:
    if jdbc_url.startswith("jdbc:"):
        return jdbc_url[5:].split(":", 1)[0]
    return "postgresql"


class RepositoryConnectionProvider:
    """Connection provider backed by MongoDB, plus the internal metrics DB."""

    def __init__(self, repository: Any, settings: Settings | None = None) -> None:
        self.repository = repository
        self.settings = settings or get_settings()
        self._metrics = metrics_connection(self.settings)

    def get(self, connection_id: str) -> ConnectionDefinition:
        if connection_id == METRICS_CONNECTION_ID:
            return self._metrics
        return self.repository.get(connection_id)


def load_definition_file(path: str) -> ReconciliationDefinition:
    """Load a definition from YAML/JSON (offline runs, CI, tests)."""
    import yaml

    raw = Path(path).read_text(encoding="utf-8")
    data = yaml.safe_load(raw)
    if isinstance(data, dict) and "reconciliation" in data:
        data = data["reconciliation"]
    if isinstance(data, dict) and "id" in data and "reconId" not in data:
        data["reconId"] = data.pop("id")
    return ReconciliationDefinition.model_validate(data)


def load_connections_file(path: str) -> dict[str, ConnectionDefinition]:
    import yaml

    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    entries = data.get("connections", data) if isinstance(data, dict) else data
    connections: dict[str, ConnectionDefinition] = {}
    if isinstance(entries, dict):
        entries = [{"connectionId": key, **value} for key, value in entries.items()]
    for entry in entries or []:
        if "id" in entry and "connectionId" not in entry:
            entry["connectionId"] = entry.pop("id")
        connection = ConnectionDefinition.model_validate(entry)
        connections[connection.connection_id] = connection
    return connections


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="reconx-job", description="Execute a ReconX reconciliation with Apache Spark"
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--recon-id", help="Reconciliation id to load from MongoDB")
    source.add_argument("--definition-file", help="YAML/JSON definition file (offline mode)")
    parser.add_argument("--version", type=int, help="Definition version (defaults to the active one)")
    parser.add_argument("--connections-file", help="YAML file of connections (offline mode)")
    parser.add_argument("--run-id", help="Run id (generated when omitted)")
    parser.add_argument("--business-date", help="Business date (YYYY-MM-DD); defaults to today")
    parser.add_argument("--trigger", default=TriggerType.MANUAL.value, help="Trigger type")
    parser.add_argument("--triggered-by", default="cli", help="Actor that started the run")
    parser.add_argument("--param", action="append", default=[], help="Extra variable, key=value")
    parser.add_argument("--profile", action="store_true", help="Profile sources for the advisor")
    parser.add_argument("--dry-run", action="store_true", help="Validate only, do not execute")
    parser.add_argument("--no-metrics", action="store_true", help="Skip metrics persistence")
    parser.add_argument("--no-notifications", action="store_true", help="Skip notifications")
    parser.add_argument("--master", help="Override the Spark master URL")
    parser.add_argument("--output-json", help="Write the run summary as JSON to this path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    settings = get_settings()
    configure_logging(settings.log_level, json_output=settings.log_format == "json")

    parameters: dict[str, Any] = {}
    for item in args.param:
        key, _, value = item.partition("=")
        parameters[key.strip()] = value.strip()

    options = RunOptions(
        run_id=args.run_id or new_run_id(),
        business_date=args.business_date or compute_business_date().isoformat(),
        trigger_type=TriggerType(args.trigger),
        triggered_by=args.triggered_by,
        parameters=parameters,
        profile_sources=args.profile,
        dry_run=args.dry_run,
        persist_metrics=not args.no_metrics,
        send_notifications=not args.no_notifications,
    )

    metrics: MetricsRepository | None = None
    events: EventPublisher | None = None
    run_repository = None
    mongo_db = None

    if args.definition_file:
        definition = load_definition_file(args.definition_file)
        connections_map = (
            load_connections_file(args.connections_file) if args.connections_file else {}
        )
        connections_map.setdefault(METRICS_CONNECTION_ID, metrics_connection(settings))
        connections: ConnectionProvider = StaticConnectionProvider(connections_map)
    else:
        from reconx.config.repository import ConnectionRepository, ReconciliationRepository, RunRepository
        from reconx.config.store import get_database

        mongo_db = get_database(settings)
        repository = ReconciliationRepository(mongo_db)
        try:
            definition = repository.get(args.recon_id, version=args.version)
        except NotFoundError as exc:
            log.error("job.definition_not_found", recon_id=args.recon_id, error=str(exc))
            return 2
        connections = RepositoryConnectionProvider(ConnectionRepository(mongo_db), settings)
        run_repository = RunRepository(mongo_db)

    if options.persist_metrics:
        metrics = MetricsRepository(settings=settings)
    if settings.kafka.enabled:
        events = EventPublisher(
            settings,
            topic_prefix=definition.events.topic_prefix or settings.kafka.topic_prefix,
            failure_mode=definition.events.on_failure,
            outbox_db=mongo_db,
            extra_headers=definition.events.extra_headers,
        )

    if args.master:
        settings.spark.master = args.master

    job = ReconciliationJob(
        definition,
        connections,
        options,
        settings=settings,
        metrics=metrics,
        events=events,
        run_repository=run_repository,
        mongo_db=mongo_db,
    )
    summary = job.run()

    if args.output_json:
        Path(args.output_json).write_text(json.dumps(summary.to_dict(), indent=2, default=str))
    print(json.dumps(summary.to_dict(), indent=2, default=str))
    return 0 if summary.status in (RunStatus.SUCCESS, RunStatus.PARTIAL_SUCCESS) else 1


def _parse_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
