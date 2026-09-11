"""The distributed scheduler.

Every node runs the same loop:

1. refresh ``schedule_state`` for the active definitions
2. find schedules whose ``nextRunAt`` has passed
3. take a short-lived distributed lock per reconciliation - only one node wins
4. evaluate the data-availability conditions
5. create the run (unique idempotency key = second line of defence) and submit
   the Spark job
6. advance ``nextRunAt`` and record what happened

Runs whose conditions are not yet met are held in ``WAITING_FOR_DATA`` and
re-checked until ``waitForDataMinutes`` elapses, at which point they are
``SKIPPED`` (not failed - missing data is an operational state, not an error).
"""

from __future__ import annotations

import contextlib
import signal
import threading
import time
from datetime import timedelta
from typing import Any

from pymongo.database import Database

from reconx.common.errors import DuplicateRunError, ReconXError
from reconx.common.ids import new_run_id
from reconx.common.logging import bind_context, clear_context, configure_logging, get_logger
from reconx.common.templating import build_run_variables
from reconx.common.timeutils import business_date as compute_business_date
from reconx.common.timeutils import to_utc, utcnow
from reconx.config.enums import RunStatus, TriggerType
from reconx.config.models import ReconciliationDefinition, declared_variable_defaults
from reconx.config.repository import (
    ConnectionRepository,
    ReconciliationRepository,
    RunRepository,
)
from reconx.config.settings import Settings, get_settings
from reconx.config.store import Collections, get_database
from reconx.metrics.repository import MetricsRepository
from reconx.scheduler.conditions import ConditionEvaluator, ConditionResult
from reconx.scheduler.locks import DistributedLock, node_id
from reconx.scheduler.runner import SparkJobOrchestrator, reclaim_orphaned_runs
from reconx.scheduler.triggers import describe, is_due, next_fire_time
from reconx.spark.job import RepositoryConnectionProvider, RunOptions

log = get_logger(__name__)


class SchedulerService:
    """The scheduler loop.  Safe to run on every node."""

    def __init__(
        self,
        database: Database | None = None,
        settings: Settings | None = None,
        *,
        orchestrator: SparkJobOrchestrator | None = None,
        metrics: MetricsRepository | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self.db = database if database is not None else get_database(self.settings)
        self.node = self.settings.scheduler.node_id or node_id()
        self.recon_repository = ReconciliationRepository(self.db)
        self.connection_repository = ConnectionRepository(self.db)
        self.run_repository = RunRepository(self.db)
        self.metrics = metrics or MetricsRepository(settings=self.settings)
        self.orchestrator = orchestrator or SparkJobOrchestrator(self.settings)
        self.connections = RepositoryConnectionProvider(self.connection_repository, self.settings)
        self._stop = threading.Event()
        self._ticks = 0

    # ------------------------------------------------------------------ run
    def start(self) -> None:
        """Run until interrupted."""
        configure_logging(self.settings.log_level, json_output=self.settings.log_format == "json")
        log.info(
            "scheduler.starting",
            node=self.node,
            poll_interval=self.settings.scheduler.poll_interval_seconds,
            max_concurrent=self.settings.scheduler.max_concurrent_runs,
        )
        self._install_signal_handlers()
        try:
            reclaimed = reclaim_orphaned_runs(
                self.run_repository,
                timeout_minutes=self.settings.scheduler.orphan_run_timeout_minutes,
                node=self.node,
            )
            if reclaimed:
                log.warning("scheduler.orphans_reclaimed", count=reclaimed)
        except Exception as exc:
            log.error("scheduler.orphan_reclaim_failed", error=str(exc)[:300])

        while not self._stop.is_set():
            started = time.time()
            try:
                self.tick()
            except Exception as exc:
                log.exception("scheduler.tick_failed", error=str(exc)[:400])
            elapsed = time.time() - started
            self._stop.wait(max(1.0, self.settings.scheduler.poll_interval_seconds - elapsed))
        log.info("scheduler.stopped", node=self.node, ticks=self._ticks)

    def stop(self) -> None:
        self._stop.set()

    def _install_signal_handlers(self) -> None:
        def _handler(signum: int, _frame: Any) -> None:
            log.info("scheduler.signal_received", signal=signum)
            self.stop()

        for sig in (signal.SIGINT, signal.SIGTERM):
            # Signals can only be installed on the main thread.
            with contextlib.suppress(ValueError):
                signal.signal(sig, _handler)

    # ----------------------------------------------------------------- tick
    def tick(self) -> dict[str, Any]:
        """One scheduling pass.  Returns a summary (used by tests and /metrics)."""
        self._ticks += 1
        self.orchestrator.reap()
        summary = {"evaluated": 0, "fired": 0, "waiting": 0, "skipped": 0, "locked": 0}

        definitions = self.recon_repository.list_active()
        for definition in definitions:
            self.refresh_schedule_state(definition)

        for definition in definitions:
            summary["evaluated"] += 1
            try:
                outcome = self.maybe_fire(definition)
            except Exception as exc:
                log.error("scheduler.definition_failed", recon_id=definition.recon_id, error=str(exc)[:300])
                continue
            if outcome in summary:
                summary[outcome] += 1

        self.process_waiting_runs()
        log.debug("scheduler.tick", node=self.node, **summary)
        return summary

    def refresh_schedule_state(self, definition: ReconciliationDefinition) -> dict[str, Any]:
        """Keep ``schedule_state`` in step with the definition's schedule."""
        state = self.db[Collections.SCHEDULE_STATE].find_one({"reconId": definition.recon_id})
        schedule = definition.schedule
        update: dict[str, Any] = {
            "reconId": definition.recon_id,
            "reconName": definition.name,
            "type": schedule.type.value,
            "description": describe(schedule),
            "enabled": schedule.enabled and definition.enabled,
            "paused": schedule.paused,
            "timezone": schedule.timezone,
            "version": definition.version,
            "updatedAt": utcnow(),
        }
        if state is None or state.get("nextRunAt") is None or state.get("version") != definition.version:
            update["nextRunAt"] = next_fire_time(
                schedule, last_run=to_utc(state["lastRunAt"]) if state and state.get("lastRunAt") else None
            )
        self.db[Collections.SCHEDULE_STATE].update_one(
            {"reconId": definition.recon_id}, {"$set": update}, upsert=True
        )
        return {**(state or {}), **update}

    def maybe_fire(self, definition: ReconciliationDefinition) -> str:
        """Fire the reconciliation if it is due, conditions permitting."""
        state = self.db[Collections.SCHEDULE_STATE].find_one({"reconId": definition.recon_id}) or {}
        schedule = definition.schedule
        next_run_at = state.get("nextRunAt")
        if not is_due(schedule, next_run_at=to_utc(next_run_at) if next_run_at else None):
            return "not_due"

        if self.orchestrator.running_count() >= self.settings.scheduler.max_concurrent_runs:
            log.warning("scheduler.node_at_capacity", node=self.node, recon_id=definition.recon_id)
            return "locked"

        active = self.run_repository.count_active(definition.recon_id)
        if active >= schedule.max_concurrent_runs:
            log.info(
                "scheduler.concurrency_limit",
                recon_id=definition.recon_id,
                active=active,
                limit=schedule.max_concurrent_runs,
            )
            self._advance(definition, state)
            return "skipped"

        lock = DistributedLock(
            self.db,
            f"schedule:{definition.recon_id}",
            ttl_seconds=self.settings.scheduler.lock_ttl_seconds,
            owner=self.node,
        )
        if not lock.acquire():
            return "locked"
        try:
            return self._fire(definition, state)
        finally:
            lock.release()

    def _fire(self, definition: ReconciliationDefinition, state: dict[str, Any]) -> str:
        business_date = compute_business_date(
            tz=definition.schedule.timezone, offset_days=definition.schedule.business_date_offset_days
        ).isoformat()
        bind_context(recon_id=definition.recon_id, business_date=business_date, node=self.node)
        scheduled_time = state.get("nextRunAt")

        variables = build_run_variables(
            recon_id=definition.recon_id,
            biz_date=compute_business_date(
                tz=definition.schedule.timezone,
                offset_days=definition.schedule.business_date_offset_days,
            ),
            timezone_name=definition.schedule.timezone,
            extra=declared_variable_defaults(definition),
        )
        condition_result = self._evaluate_conditions(definition, variables)

        if not condition_result.satisfied:
            run = self._create_run(
                definition,
                business_date,
                status=RunStatus.WAITING_FOR_DATA,
                trigger=TriggerType.SCHEDULED,
                condition_result=condition_result,
            )
            self._record_scheduler_execution(
                definition,
                status="WAITING_FOR_DATA",
                scheduled_time=scheduled_time,
                business_date=business_date,
                run_id=(run or {}).get("runId"),
                condition_result=condition_result,
            )
            self._advance(definition, state)
            clear_context()
            return "waiting"

        run = self._create_run(
            definition, business_date, status=RunStatus.QUEUED, trigger=TriggerType.SCHEDULED
        )
        if run is None:
            self._advance(definition, state)
            clear_context()
            return "skipped"

        self._submit(definition, run, variables=variables)
        self._record_scheduler_execution(
            definition,
            status="FIRED",
            scheduled_time=scheduled_time,
            business_date=business_date,
            run_id=run["runId"],
            condition_result=condition_result,
        )
        self._advance(definition, state, last_run=utcnow())
        clear_context()
        return "fired"

    # ------------------------------------------------------------ helpers
    def _evaluate_conditions(
        self, definition: ReconciliationDefinition, variables: dict[str, Any]
    ) -> ConditionResult:
        evaluator = ConditionEvaluator(
            self.connections,
            run_repository=self.run_repository,
            variables=variables,
        )
        return evaluator.evaluate(definition.conditions, recon_id=definition.recon_id)

    def _create_run(
        self,
        definition: ReconciliationDefinition,
        business_date: str,
        *,
        status: RunStatus,
        trigger: TriggerType,
        triggered_by: str | None = None,
        condition_result: ConditionResult | None = None,
        parameters: dict[str, Any] | None = None,
    ) -> dict[str, Any] | None:
        try:
            run = self.run_repository.create(
                run_id=new_run_id(),
                definition=definition,
                trigger_type=trigger,
                triggered_by=triggered_by or f"scheduler@{self.node}",
                business_date=business_date,
                parameters=parameters or declared_variable_defaults(definition),
                node=self.node,
                status=status,
            )
        except DuplicateRunError as exc:
            # Another node won the race, or this business date already ran.
            log.info(
                "scheduler.duplicate_run_skipped",
                recon_id=definition.recon_id,
                business_date=business_date,
                existing_run_id=exc.details.get("existingRunId"),
            )
            return None
        if condition_result is not None:
            self.db[Collections.RUNS].update_one(
                {"runId": run["runId"]},
                {
                    "$set": {
                        "conditionResult": condition_result.to_dict(),
                        "conditionSummary": condition_result.summary(),
                        "waitingSince": utcnow(),
                    }
                },
            )
        try:
            self.metrics.record_run_start({**run, "status": status.value})
        except Exception as exc:
            log.warning("scheduler.metrics_run_start_failed", error=str(exc)[:200])
        return run

    def _submit(
        self,
        definition: ReconciliationDefinition,
        run: dict[str, Any],
        *,
        variables: dict[str, Any] | None = None,
    ) -> None:
        options = RunOptions(
            run_id=run["runId"],
            business_date=run["businessDate"],
            trigger_type=TriggerType(run.get("triggerType", TriggerType.SCHEDULED.value)),
            triggered_by=run.get("triggeredBy", self.node),
            parameters=run.get("parameters") or {},
            node=self.node,
            attempt=int(run.get("attempt", 1)),
        )
        try:
            handle = self.orchestrator.submit(definition, options)
            self.run_repository.update_status(
                run["runId"],
                RunStatus.STARTING,
                extra={"node": self.node, "submittedAt": utcnow(), "pid": handle.pid},
            )
        except ReconXError as exc:
            log.error("scheduler.submit_failed", run_id=run["runId"], error=exc.message)
            self.run_repository.update_status(run["runId"], RunStatus.FAILED, error=exc.message)
            self.metrics.record_run_completion(run["runId"], status=RunStatus.FAILED.value, error=exc.message)

    def _advance(
        self,
        definition: ReconciliationDefinition,
        state: dict[str, Any],
        *,
        last_run: Any = None,
    ) -> None:
        next_run = next_fire_time(
            definition.schedule,
            after=utcnow(),
            last_run=last_run or (to_utc(state["lastRunAt"]) if state.get("lastRunAt") else None),
        )
        update: dict[str, Any] = {"nextRunAt": next_run, "updatedAt": utcnow()}
        if last_run:
            update["lastRunAt"] = last_run
        self.db[Collections.SCHEDULE_STATE].update_one(
            {"reconId": definition.recon_id}, {"$set": update}, upsert=True
        )
        log.info(
            "scheduler.next_run_scheduled",
            recon_id=definition.recon_id,
            next_run_at=next_run.isoformat() if next_run else None,
        )

    def _record_scheduler_execution(
        self,
        definition: ReconciliationDefinition,
        *,
        status: str,
        scheduled_time: Any,
        business_date: str,
        run_id: str | None,
        condition_result: ConditionResult | None,
    ) -> None:
        try:
            self.metrics.record_scheduler_execution(
                {
                    "reconId": definition.recon_id,
                    "node": self.node,
                    "scheduledTime": scheduled_time,
                    "firedAt": utcnow(),
                    "status": status,
                    "runId": run_id,
                    "businessDate": business_date,
                    "conditionsMet": condition_result.satisfied if condition_result else None,
                    "conditionDetail": condition_result.to_dict() if condition_result else None,
                    "message": condition_result.summary() if condition_result else None,
                }
            )
        except Exception as exc:
            log.warning("scheduler.execution_record_failed", error=str(exc)[:200])

    # --------------------------------------------------- waiting-for-data
    def process_waiting_runs(self) -> dict[str, int]:
        """Re-check conditions for runs parked in WAITING_FOR_DATA."""
        summary = {"released": 0, "skipped": 0, "still_waiting": 0}
        waiting = self.run_repository.list(status=RunStatus.WAITING_FOR_DATA.value, limit=200)
        for run in waiting:
            lock = DistributedLock(
                self.db,
                f"waiting:{run['runId']}",
                ttl_seconds=self.settings.scheduler.lock_ttl_seconds,
                owner=self.node,
            )
            if not lock.acquire():
                continue
            try:
                definition = self.recon_repository.find_optional(run["reconId"])
                if definition is None:
                    self.run_repository.update_status(
                        run["runId"], RunStatus.CANCELLED, error="Definition no longer exists"
                    )
                    continue
                waiting_since = run.get("waitingSince") or run.get("createdAt") or utcnow()
                deadline = to_utc(waiting_since) + timedelta(
                    minutes=definition.schedule.wait_for_data_minutes
                )
                variables = build_run_variables(
                    recon_id=definition.recon_id,
                    biz_date=None,
                    timezone_name=definition.schedule.timezone,
                    extra={**declared_variable_defaults(definition), **(run.get("parameters") or {})},
                )
                result = self._evaluate_conditions(definition, variables)
                if result.satisfied:
                    self.run_repository.update_status(
                        run["runId"],
                        RunStatus.QUEUED,
                        extra={"conditionSummary": result.summary(), "conditionResult": result.to_dict()},
                    )
                    self._submit(definition, {**run, "status": RunStatus.QUEUED.value}, variables=variables)
                    summary["released"] += 1
                    log.info("scheduler.data_arrived", run_id=run["runId"], recon_id=run["reconId"])
                elif utcnow() > deadline:
                    message = f"Data did not arrive within {definition.schedule.wait_for_data_minutes} minutes. {result.summary()}"
                    self.run_repository.update_status(
                        run["runId"], RunStatus.SKIPPED, error=message,
                        extra={"conditionResult": result.to_dict()},
                    )
                    self.metrics.record_run_completion(
                        run["runId"], status=RunStatus.SKIPPED.value, error=message
                    )
                    self._notify_data_unavailable(definition, run, result)
                    summary["skipped"] += 1
                    log.warning("scheduler.data_wait_timeout", run_id=run["runId"], recon_id=run["reconId"])
                else:
                    self.db[Collections.RUNS].update_one(
                        {"runId": run["runId"]},
                        {
                            "$set": {
                                "conditionSummary": result.summary(),
                                "conditionResult": result.to_dict(),
                                "lastConditionCheckAt": utcnow(),
                            }
                        },
                    )
                    summary["still_waiting"] += 1
            except Exception as exc:
                log.error("scheduler.waiting_run_failed", run_id=run.get("runId"), error=str(exc)[:300])
            finally:
                lock.release()
        return summary

    def _notify_data_unavailable(
        self, definition: ReconciliationDefinition, run: dict[str, Any], result: ConditionResult
    ) -> None:
        from reconx.config.enums import NotifyOn
        from reconx.notifications.base import NotificationContext, should_notify

        email = definition.notifications.email
        if should_notify(RunStatus.SKIPPED.value, email.on) is None:
            return
        try:
            from reconx.notifications.email import EmailNotifier

            EmailNotifier(self.settings).send(
                NotificationContext(
                    recon_id=definition.recon_id,
                    recon_name=definition.name,
                    run_id=run["runId"],
                    status=RunStatus.SKIPPED.value,
                    business_date=run.get("businessDate"),
                    trigger=run.get("triggerType"),
                    error_message=result.summary(),
                    product=definition.product,
                    customer=definition.customer,
                    environment=definition.environment or self.settings.environment,
                    ui_url=f"{self.settings.api.base_url}/runs/{run['runId']}",
                    notify_reason=NotifyOn.DATA_UNAVAILABLE,
                ),
                email,
            )
        except Exception as exc:
            log.error("scheduler.data_unavailable_notification_failed", error=str(exc)[:200])

    # ---------------------------------------------------------- manual API
    def trigger_now(
        self,
        recon_id: str,
        *,
        triggered_by: str,
        business_date: str | None = None,
        parameters: dict[str, Any] | None = None,
        skip_conditions: bool = False,
        profile_sources: bool = False,
        version: int | None = None,
    ) -> dict[str, Any]:
        """Start a run immediately (used by the API's "Run now")."""
        definition = self.recon_repository.get(recon_id, version=version)
        resolved_date = business_date or compute_business_date(
            tz=definition.schedule.timezone, offset_days=definition.schedule.business_date_offset_days
        ).isoformat()
        merged_parameters = {**declared_variable_defaults(definition), **(parameters or {})}
        variables = build_run_variables(
            recon_id=recon_id,
            timezone_name=definition.schedule.timezone,
            extra=merged_parameters,
        )

        condition_result: ConditionResult | None = None
        if not skip_conditions and definition.conditions is not None:
            condition_result = self._evaluate_conditions(definition, variables)

        status = (
            RunStatus.WAITING_FOR_DATA
            if condition_result is not None and not condition_result.satisfied
            else RunStatus.QUEUED
        )
        run = self._create_run(
            definition,
            resolved_date,
            status=status,
            trigger=TriggerType.MANUAL,
            triggered_by=triggered_by,
            condition_result=condition_result,
            parameters=merged_parameters,
        )
        if run is None:
            raise DuplicateRunError(
                f"A run of '{recon_id}' for business date {resolved_date} already exists",
                details={"reconId": recon_id, "businessDate": resolved_date},
            )
        if status == RunStatus.QUEUED:
            options_parameters = dict(merged_parameters)
            run["parameters"] = options_parameters
            if profile_sources:
                run["profileSources"] = True
            self._submit_manual(definition, run, profile_sources=profile_sources)
        return {
            **run,
            "conditionSummary": condition_result.summary() if condition_result else None,
            "conditionsSatisfied": condition_result.satisfied if condition_result else True,
        }

    def _submit_manual(
        self, definition: ReconciliationDefinition, run: dict[str, Any], *, profile_sources: bool
    ) -> None:
        options = RunOptions(
            run_id=run["runId"],
            business_date=run["businessDate"],
            trigger_type=TriggerType.MANUAL,
            triggered_by=run.get("triggeredBy", "api"),
            parameters=run.get("parameters") or {},
            profile_sources=profile_sources,
            node=self.node,
        )
        try:
            handle = self.orchestrator.submit(definition, options)
            self.run_repository.update_status(
                run["runId"],
                RunStatus.STARTING,
                extra={"node": self.node, "submittedAt": utcnow(), "pid": handle.pid},
            )
        except ReconXError as exc:
            self.run_repository.update_status(run["runId"], RunStatus.FAILED, error=exc.message)
            raise

    def cancel_run(self, run_id: str, *, actor: str) -> dict[str, Any]:
        run = self.run_repository.get(run_id)
        if RunStatus(run["status"]).is_terminal:
            return {"cancelled": False, "reason": f"Run is already {run['status']}"}
        cancelled_locally = self.orchestrator.cancel(run_id)
        self.run_repository.update_status(
            run_id, RunStatus.CANCELLED, error=f"Cancelled by {actor}"
        )
        try:
            self.metrics.record_run_completion(
                run_id, status=RunStatus.CANCELLED.value, error=f"Cancelled by {actor}"
            )
        except Exception as exc:
            log.warning("scheduler.cancel_metrics_failed", error=str(exc)[:200])
        log.info("scheduler.run_cancelled", run_id=run_id, actor=actor, local=cancelled_locally)
        return {"cancelled": True, "runId": run_id, "processTerminated": cancelled_locally}

    def status(self) -> dict[str, Any]:
        return {
            "node": self.node,
            "ticks": self._ticks,
            "runningJobs": self.orchestrator.running_count(),
            "maxConcurrent": self.settings.scheduler.max_concurrent_runs,
            "pollIntervalSeconds": self.settings.scheduler.poll_interval_seconds,
            "schedules": self.db[Collections.SCHEDULE_STATE].count_documents({"enabled": True}),
        }


def run() -> None:
    """Console-script entry point (``reconx-scheduler``)."""
    settings = get_settings()
    configure_logging(settings.log_level, json_output=settings.log_format == "json")
    if not settings.scheduler.enabled:
        log.warning("scheduler.disabled_by_configuration")
        return
    from reconx.config.store import ensure_indexes

    database = get_database(settings)
    ensure_indexes(database, settings)
    service = SchedulerService(database, settings)
    try:
        service.metrics.create_schema()
    except Exception as exc:
        log.error("scheduler.metrics_schema_failed", error=str(exc)[:300])
    service.start()


if __name__ == "__main__":  # pragma: no cover
    run()
