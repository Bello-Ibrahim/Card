"""``reconx-admin`` - operational command line.

Covers the tasks an operator needs outside the UI: generating an encryption
key, initialising storage, importing/exporting definitions, running a
reconciliation, and the maintenance job (retention + event replay).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from reconx import __version__
from reconx.common.logging import configure_logging, get_logger
from reconx.config.settings import get_settings

log = get_logger(__name__)


def _database() -> Any:
    from reconx.config.store import get_database

    return get_database()


# --------------------------------------------------------------------------- #
# Commands
# --------------------------------------------------------------------------- #
def cmd_gen_key(args: argparse.Namespace) -> int:
    """Generate a Fernet key for encrypting connection secrets at rest."""
    from reconx.security.crypto import generate_key

    key = generate_key()
    print(key)
    print(
        "\nSet this as RECONX_SECURITY_ENCRYPTION_KEY (Kubernetes Secret / vault).",
        file=sys.stderr,
    )
    print(
        "Keep it safe: without it, stored connection secrets cannot be decrypted.",
        file=sys.stderr,
    )
    return 0


def cmd_init(args: argparse.Namespace) -> int:
    """Create MongoDB indexes and the metrics tables."""
    from reconx.config.store import ensure_indexes
    from reconx.metrics.repository import MetricsRepository

    indexes = ensure_indexes(_database())
    print(f"MongoDB: {len(indexes)} index(es) ensured")
    tables = MetricsRepository().create_schema()
    print(f"Metrics database: {len(tables)} table(s) ensured")
    for table in tables:
        print(f"  - {table}")
    return 0


def cmd_create_user(args: argparse.Namespace) -> int:
    from reconx.security.auth import MongoUserStore

    store = MongoUserStore(_database())
    store.ensure_indexes()
    user = store.create_user(
        args.username, args.password, args.roles, email=args.email, created_by="cli"
    )
    print(json.dumps(user, indent=2, default=str))
    return 0


def cmd_import(args: argparse.Namespace) -> int:
    """Import a reconciliation definition from YAML/JSON."""
    from reconx.config.repository import ReconciliationRepository
    from reconx.config.validation import validate_definition
    from reconx.spark.job import load_definition_file

    definition = load_definition_file(args.file)
    report = validate_definition(definition)
    for issue in report.issues:
        print(f"  {issue.severity}: {issue.path} - {issue.message}")
    if not report.valid:
        print(f"\n{len(report.errors)} error(s); nothing was imported.")
        return 1

    repository = ReconciliationRepository(_database())
    existing = repository.find_optional(definition.recon_id)
    if existing is None:
        saved = repository.create(definition, actor=args.actor)
    else:
        saved = repository.save_new_version(
            definition, actor=args.actor, comment=args.comment, activate=args.activate
        )
    if args.activate and saved.status.value != "ACTIVE":
        saved = repository.activate_version(saved.recon_id, actor=args.actor)
    print(f"Imported '{saved.recon_id}' as version {saved.version} ({saved.status.value})")
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    import yaml

    from reconx.config.repository import ReconciliationRepository

    repository = ReconciliationRepository(_database())
    definition = repository.get(args.recon_id, version=args.version)
    payload = {"reconciliation": definition.dump()}
    text = (
        json.dumps(payload, indent=2, default=str)
        if args.format == "json"
        else yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
    )
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(text)
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    """Run a reconciliation now (delegates to the Spark job entry point)."""
    from reconx.spark.job import main as job_main

    job_args = ["--recon-id", args.recon_id]
    if args.business_date:
        job_args += ["--business-date", args.business_date]
    if args.version:
        job_args += ["--version", str(args.version)]
    if args.profile:
        job_args.append("--profile")
    for parameter in args.param or []:
        job_args += ["--param", parameter]
    return job_main(job_args)


def cmd_validate(args: argparse.Namespace) -> int:
    from reconx.config.validation import validate_definition
    from reconx.spark.job import load_definition_file

    definition = load_definition_file(args.file)
    report = validate_definition(definition)
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.valid else 1


def cmd_maintenance(args: argparse.Namespace) -> int:
    """Retention enforcement and Kafka outbox replay (run from a CronJob)."""
    settings = get_settings()
    exit_code = 0

    if args.purge:
        from reconx.config.repository import ReconciliationRepository
        from reconx.metrics.repository import MetricsRepository

        metrics = MetricsRepository()
        repository = ReconciliationRepository(_database())
        for document in repository.list(limit=1000):
            retention = document.get("retention") or {}
            deleted = metrics.purge_old_data(
                runs_days=int(retention.get("runsDays", 365)),
                exceptions_days=int(retention.get("exceptionsDays", 90)),
                recon_id=document["reconId"],
            )
            if any(deleted.values()):
                print(f"{document['reconId']}: purged {deleted}")

    if args.replay_events and settings.kafka.enabled:
        from reconx.events.publisher import EventPublisher

        publisher = EventPublisher(settings, outbox_db=_database())
        result = publisher.replay_outbox(limit=args.replay_limit)
        publisher.close()
        print(f"Outbox replay: {result}")
        if result.get("failed"):
            exit_code = 1

    if args.reclaim_orphans:
        from reconx.config.repository import RunRepository
        from reconx.scheduler.runner import reclaim_orphaned_runs

        reclaimed = reclaim_orphaned_runs(
            RunRepository(_database()), timeout_minutes=settings.scheduler.orphan_run_timeout_minutes
        )
        print(f"Reclaimed {reclaimed} orphaned run(s)")

    return exit_code


def cmd_check(args: argparse.Namespace) -> int:
    """Verify every platform dependency is reachable."""
    settings = get_settings()
    results: dict[str, Any] = {}
    ok = True

    try:
        from reconx.config.store import ping

        results["mongodb"] = ping(settings)
    except Exception as exc:
        results["mongodb"] = {"ok": False, "error": str(exc)[:300]}
        ok = False

    try:
        from reconx.metrics.repository import MetricsRepository

        results["metricsDatabase"] = MetricsRepository().ping()
    except Exception as exc:
        results["metricsDatabase"] = {"ok": False, "error": str(exc)[:300]}
        ok = False

    if settings.kafka.enabled:
        try:
            from confluent_kafka.admin import AdminClient

            metadata = AdminClient(
                {"bootstrap.servers": settings.kafka.bootstrap_servers}
            ).list_topics(timeout=8)
            results["kafka"] = {"ok": True, "brokers": len(metadata.brokers)}
        except Exception as exc:
            results["kafka"] = {"ok": False, "error": str(exc)[:300]}
    else:
        results["kafka"] = {"ok": True, "disabled": True}

    if settings.smtp.enabled:
        from reconx.notifications.email import EmailNotifier

        outcome = EmailNotifier(settings).test()
        results["smtp"] = {"ok": outcome.success, "message": outcome.message}

    print(json.dumps(results, indent=2, default=str))
    return 0 if ok else 1


# --------------------------------------------------------------------------- #
# Parser
# --------------------------------------------------------------------------- #
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="reconx-admin", description="ReconX administration")
    parser.add_argument("--version", action="version", version=f"reconx {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("gen-key", help="Generate a secret-encryption key").set_defaults(
        func=cmd_gen_key
    )
    subparsers.add_parser("init-db", help="Create MongoDB indexes and metrics tables").set_defaults(
        func=cmd_init
    )
    subparsers.add_parser("check", help="Verify every dependency is reachable").set_defaults(func=cmd_check)

    user = subparsers.add_parser("create-user", help="Create a platform user")
    user.add_argument("username")
    user.add_argument("password")
    user.add_argument("--roles", nargs="+", default=["VIEWER"])
    user.add_argument("--email")
    user.set_defaults(func=cmd_create_user)

    import_parser = subparsers.add_parser("import", help="Import a definition from YAML/JSON")
    import_parser.add_argument("file")
    import_parser.add_argument("--actor", default="cli")
    import_parser.add_argument("--comment")
    import_parser.add_argument("--activate", action="store_true")
    import_parser.set_defaults(func=cmd_import)

    export_parser = subparsers.add_parser("export", help="Export a definition")
    export_parser.add_argument("recon_id")
    export_parser.add_argument("--version", type=int)
    export_parser.add_argument("--output")
    export_parser.add_argument("--format", choices=["yaml", "json"], default="yaml")
    export_parser.set_defaults(func=cmd_export)

    validate_parser = subparsers.add_parser("validate", help="Validate a definition file")
    validate_parser.add_argument("file")
    validate_parser.set_defaults(func=cmd_validate)

    run_parser = subparsers.add_parser("run", help="Run a reconciliation now")
    run_parser.add_argument("recon_id")
    run_parser.add_argument("--business-date")
    run_parser.add_argument("--version", type=int)
    run_parser.add_argument("--profile", action="store_true", help="Profile sources for the advisor")
    run_parser.add_argument("--param", action="append", help="Variable, key=value")
    run_parser.set_defaults(func=cmd_run)

    maintenance = subparsers.add_parser("maintenance", help="Retention and event replay")
    maintenance.add_argument("--purge", action="store_true", help="Apply retention policies")
    maintenance.add_argument("--replay-events", action="store_true", help="Replay the Kafka outbox")
    maintenance.add_argument("--replay-limit", type=int, default=500)
    maintenance.add_argument("--reclaim-orphans", action="store_true", help="Fail abandoned runs")
    maintenance.set_defaults(func=cmd_maintenance)

    return parser


def main(argv: list[str] | None = None) -> int:
    settings = get_settings()
    configure_logging(settings.log_level, json_output=settings.log_format == "json")
    args = build_parser().parse_args(argv)
    try:
        return int(args.func(args))
    except Exception as exc:
        log.error("cli.command_failed", command=args.command, error=str(exc)[:500])
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
