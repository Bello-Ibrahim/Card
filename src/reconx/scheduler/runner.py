"""Spark job orchestration.

Submits a reconciliation run to Spark and tracks it.  Three modes, chosen with
``SPARK_SUBMIT_MODE``:

``inprocess``     run the job in a child Python process using ``local[*]``
                  (development, small reconciliations, CI)
``spark-submit``  ``spark-submit --master spark://...`` against a standalone or
                  YARN cluster
``kubernetes``    ``spark-submit --master k8s://...`` in cluster mode, so the
                  driver runs as its own pod and survives the scheduler
                  restarting

In every mode the *authoritative* run state lives in MongoDB and the metrics
database - the local handle is a convenience for cancellation and log capture,
never a source of truth.  That is what lets any node pick up after a crash.
"""

from __future__ import annotations

import os
import shlex
import subprocess
import sys
import threading
from dataclasses import dataclass, field
from datetime import timedelta
from pathlib import Path
from typing import Any

from reconx.common.errors import JobSubmissionError
from reconx.common.logging import get_logger
from reconx.common.timeutils import utcnow
from reconx.config.enums import RunStatus
from reconx.config.models import ReconciliationDefinition
from reconx.config.settings import Settings, get_settings
from reconx.scheduler.locks import node_id
from reconx.spark.job import RunOptions
from reconx.spark.session import build_spark_conf

log = get_logger(__name__)


@dataclass
class SubmissionHandle:
    """A submitted run this node is tracking."""

    run_id: str
    recon_id: str
    mode: str
    process: subprocess.Popen[bytes] | None = None
    submitted_at: Any = field(default_factory=utcnow)
    command: list[str] = field(default_factory=list)
    log_path: str | None = None

    @property
    def pid(self) -> int | None:
        return self.process.pid if self.process else None

    def is_running(self) -> bool:
        return self.process is not None and self.process.poll() is None

    def exit_code(self) -> int | None:
        return self.process.poll() if self.process else None

    def to_dict(self) -> dict[str, Any]:
        return {
            "runId": self.run_id,
            "reconId": self.recon_id,
            "mode": self.mode,
            "pid": self.pid,
            "running": self.is_running(),
            "exitCode": self.exit_code(),
            "submittedAt": self.submitted_at.isoformat(),
            "logPath": self.log_path,
        }


class SparkJobOrchestrator:
    """Builds and launches the Spark application for a run."""

    def __init__(self, settings: Settings | None = None, *, log_dir: str | None = None) -> None:
        self.settings = settings or get_settings()
        self.log_dir = Path(log_dir or os.getenv("RECONX_JOB_LOG_DIR", "/tmp/reconx-logs"))  # noqa: S108
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self._handles: dict[str, SubmissionHandle] = {}
        self._lock = threading.Lock()

    # ------------------------------------------------------------- commands
    def build_command(self, definition: ReconciliationDefinition, options: RunOptions) -> list[str]:
        mode = self.settings.spark.submit_mode
        job_args = [
            "--recon-id",
            definition.recon_id,
            "--version",
            str(definition.version),
            "--run-id",
            options.run_id,
            "--business-date",
            options.business_date,
            "--trigger",
            options.trigger_type.value,
            "--triggered-by",
            options.triggered_by,
        ]
        for key, value in (options.parameters or {}).items():
            job_args += ["--param", f"{key}={value}"]
        if options.profile_sources:
            job_args.append("--profile")

        if mode == "inprocess":
            python = self.settings.spark.python_executable or sys.executable
            return [python, "-m", "reconx.spark.job", *job_args]

        spark_submit = self._spark_submit_binary()
        conf = build_spark_conf(self.settings, definition.spark, app_name=f"reconx-{definition.recon_id}")
        command = [spark_submit, "--master", self.settings.spark.master]

        if mode == "kubernetes":
            command += ["--deploy-mode", "cluster"]
            conf.setdefault("spark.kubernetes.namespace", self.settings.spark.namespace)
            conf.setdefault("spark.kubernetes.container.image", self.settings.spark.image)
            conf.setdefault(
                "spark.kubernetes.authenticate.driver.serviceAccountName",
                self.settings.spark.service_account,
            )
            # Environment the driver pod needs to reach Mongo/Kafka/JDBC.
            for variable in (
                "MONGODB_URI",
                "MONGODB_DATABASE",
                "KAFKA_BOOTSTRAP_SERVERS",
                "RESULT_JDBC_URL",
                "RESULT_JDBC_USER",
                "RESULT_JDBC_PASSWORD",
                "RECONX_SECURITY_ENCRYPTION_KEY",
                "RECONX_ENVIRONMENT",
                "LOG_LEVEL",
            ):
                value = os.getenv(variable)
                if value is not None:
                    conf[f"spark.kubernetes.driverEnv.{variable}"] = value
                    conf[f"spark.executorEnv.{variable}"] = value
        else:
            command += ["--deploy-mode", os.getenv("SPARK_DEPLOY_MODE", "client")]

        for key, value in sorted(conf.items()):
            command += ["--conf", f"{key}={value}"]
        if self.settings.spark.extra_jars:
            command += ["--jars", self.settings.spark.extra_jars]
        if self.settings.spark.extra_packages:
            command += ["--packages", self.settings.spark.extra_packages]

        entrypoint = os.getenv("RECONX_JOB_ENTRYPOINT", "")
        if not entrypoint:
            entrypoint = str(Path(__file__).resolve().parents[1] / "spark" / "job.py")
        command += [entrypoint, *job_args]
        return command

    def _spark_submit_binary(self) -> str:
        home = self.settings.spark.home or os.getenv("SPARK_HOME")
        if home:
            candidate = Path(home) / "bin" / "spark-submit"
            if candidate.exists():
                return str(candidate)
        from shutil import which

        found = which("spark-submit")
        if not found:
            raise JobSubmissionError(
                "spark-submit is not on PATH and SPARK_HOME is not set",
                details={"hint": "Set SPARK_HOME, or use SPARK_SUBMIT_MODE=inprocess for local runs"},
            )
        return found

    # --------------------------------------------------------------- submit
    def submit(self, definition: ReconciliationDefinition, options: RunOptions) -> SubmissionHandle:
        command = self.build_command(definition, options)
        log_path = self.log_dir / f"{options.run_id}.log"
        environment = {
            **os.environ,
            "RECONX_SERVICE": "spark-job",
            "RECONX_NODE_ID": node_id(),
            "PYTHONUNBUFFERED": "1",
        }
        log.info(
            "orchestrator.submitting",
            recon_id=definition.recon_id,
            run_id=options.run_id,
            mode=self.settings.spark.submit_mode,
            command=" ".join(shlex.quote(part) for part in command[:8]) + " ...",
        )
        try:
            handle_file = log_path.open("wb")
            process = subprocess.Popen(  # noqa: S603 - command is built from validated settings
                command,
                stdout=handle_file,
                stderr=subprocess.STDOUT,
                env=environment,
                cwd=os.getenv("RECONX_JOB_CWD") or None,
                start_new_session=True,
            )
        except (OSError, ValueError) as exc:
            raise JobSubmissionError(
                f"Could not start the Spark job: {exc}",
                details={"runId": options.run_id, "mode": self.settings.spark.submit_mode},
            ) from exc

        handle = SubmissionHandle(
            run_id=options.run_id,
            recon_id=definition.recon_id,
            mode=self.settings.spark.submit_mode,
            process=process,
            command=command,
            log_path=str(log_path),
        )
        with self._lock:
            self._handles[options.run_id] = handle
        log.info("orchestrator.submitted", run_id=options.run_id, pid=process.pid, log=str(log_path))
        return handle

    # ---------------------------------------------------------------- track
    def handle(self, run_id: str) -> SubmissionHandle | None:
        with self._lock:
            return self._handles.get(run_id)

    def running_count(self) -> int:
        with self._lock:
            return sum(1 for handle in self._handles.values() if handle.is_running())

    def reap(self) -> list[SubmissionHandle]:
        """Return (and forget) handles whose process has exited."""
        finished: list[SubmissionHandle] = []
        with self._lock:
            for run_id, handle in list(self._handles.items()):
                if not handle.is_running():
                    finished.append(handle)
                    self._handles.pop(run_id, None)
        for handle in finished:
            log.info(
                "orchestrator.job_finished",
                run_id=handle.run_id,
                exit_code=handle.exit_code(),
                log=handle.log_path,
            )
        return finished

    def cancel(self, run_id: str, *, timeout_seconds: int = 30) -> bool:
        handle = self.handle(run_id)
        if handle is None or not handle.is_running():
            return False
        process = handle.process
        assert process is not None
        log.warning("orchestrator.cancelling", run_id=run_id, pid=process.pid)
        process.terminate()
        try:
            process.wait(timeout=timeout_seconds)
        except subprocess.TimeoutExpired:
            log.error("orchestrator.force_killing", run_id=run_id, pid=process.pid)
            process.kill()
        with self._lock:
            self._handles.pop(run_id, None)
        return True

    def tail_log(self, run_id: str, lines: int = 200) -> str:
        handle = self.handle(run_id)
        path = Path(handle.log_path) if handle and handle.log_path else self.log_dir / f"{run_id}.log"
        if not path.exists():
            return ""
        with path.open("r", encoding="utf-8", errors="replace") as stream:
            return "".join(stream.readlines()[-lines:])

    def shutdown(self, *, wait_seconds: int = 5) -> None:
        with self._lock:
            handles = list(self._handles.values())
        for handle in handles:
            if handle.is_running() and handle.process is not None:
                log.info("orchestrator.detaching", run_id=handle.run_id, pid=handle.pid)
        self._handles.clear()


def reclaim_orphaned_runs(run_repository: Any, *, timeout_minutes: int = 720, node: str | None = None) -> int:
    """Fail runs left RUNNING by a node that died.

    Executed on scheduler startup and periodically.  Because runs carry a
    unique idempotency key, a reclaimed run can be safely retried without
    creating a duplicate.
    """
    cutoff = utcnow() - timedelta(minutes=timeout_minutes)
    stale = [
        run
        for run in run_repository.list(
            status=[RunStatus.RUNNING.value, RunStatus.STARTING.value], limit=500
        )
        if (run.get("startTime") or run.get("createdAt")) and (run.get("startTime") or run["createdAt"]) < cutoff
    ]
    for run in stale:
        run_repository.update_status(
            run["runId"],
            RunStatus.FAILED,
            error=(
                f"Run abandoned - no progress since {run.get('startTime') or run.get('createdAt')}. "
                f"The executing node ({run.get('node')}) is presumed lost."
            ),
        )
        log.warning("orchestrator.orphan_reclaimed", run_id=run["runId"], node=run.get("node"))
    return len(stale)
