"""Schedule computation, distributed locking and condition evaluation."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from types import SimpleNamespace

import pytest

from reconx.common.errors import LockAcquisitionError
from reconx.common.timeutils import utcnow
from reconx.config.models import ConditionSpec, ScheduleSpec
from reconx.scheduler.conditions import ConditionEvaluator, ConditionResult, _compare
from reconx.scheduler.locks import DistributedLock, force_release, list_locks, try_lock
from reconx.scheduler.triggers import describe, is_due, next_fire_time, upcoming_fire_times

pytestmark = pytest.mark.unit


class TestTriggers:
    def test_cron_respects_the_timezone(self):
        schedule = ScheduleSpec.model_validate(
            {"type": "cron", "expression": "0 2 * * *", "timezone": "Europe/London"}
        )
        after = datetime(2026, 9, 10, 12, 0, tzinfo=UTC)
        fire = next_fire_time(schedule, after=after)
        assert fire.hour == 1  # 02:00 BST == 01:00 UTC

    def test_daily_schedule(self):
        schedule = ScheduleSpec.model_validate({"type": "daily", "time": "23:30"})
        fire = next_fire_time(schedule, after=datetime(2026, 9, 10, 12, 0, tzinfo=UTC))
        assert (fire.hour, fire.minute) == (23, 30)

    def test_weekly_schedule_picks_the_next_configured_day(self):
        schedule = ScheduleSpec.model_validate(
            {"type": "weekly", "time": "06:00", "daysOfWeek": [0, 4]}
        )
        fire = next_fire_time(schedule, after=datetime(2026, 9, 10, 12, 0, tzinfo=UTC))
        assert fire.weekday() in (0, 4)

    def test_monthly_day_31_clamps_to_the_last_day(self):
        schedule = ScheduleSpec.model_validate({"type": "monthly", "time": "23:00", "dayOfMonth": 31})
        fire = next_fire_time(schedule, after=datetime(2026, 9, 10, 12, 0, tzinfo=UTC))
        assert fire.day == 30 and fire.month == 9

    def test_interval_schedule_skips_missed_windows(self):
        schedule = ScheduleSpec.model_validate({"type": "interval", "intervalSeconds": 3600})
        now = utcnow()
        fire = next_fire_time(schedule, after=now, last_run=now - timedelta(hours=5))
        assert fire > now

    def test_manual_and_paused_schedules_never_fire(self):
        assert next_fire_time(ScheduleSpec.model_validate({"type": "manual"})) is None
        paused = ScheduleSpec.model_validate({"type": "daily", "time": "02:00", "paused": True})
        assert next_fire_time(paused) is None

    def test_once_schedule_does_not_refire(self):
        run_at = utcnow() + timedelta(hours=1)
        schedule = ScheduleSpec.model_validate({"type": "once", "runAt": run_at.isoformat()})
        assert next_fire_time(schedule) is not None
        assert next_fire_time(schedule, last_run=run_at + timedelta(minutes=1)) is None

    def test_end_date_stops_the_schedule(self):
        schedule = ScheduleSpec.model_validate(
            {"type": "daily", "time": "02:00", "endDate": (utcnow() - timedelta(days=1)).isoformat()}
        )
        assert next_fire_time(schedule) is None

    def test_due_within_grace_but_not_after(self):
        schedule = ScheduleSpec.model_validate(
            {"type": "cron", "expression": "0 2 * * *", "misfireGraceSeconds": 600}
        )
        assert is_due(schedule, next_run_at=utcnow() - timedelta(seconds=60))
        assert not is_due(schedule, next_run_at=utcnow() - timedelta(hours=3))
        assert not is_due(schedule, next_run_at=utcnow() + timedelta(minutes=5))

    def test_catch_up_ignores_the_grace_window(self):
        schedule = ScheduleSpec.model_validate(
            {"type": "cron", "expression": "0 2 * * *", "misfireGraceSeconds": 60, "catchUp": True}
        )
        assert is_due(schedule, next_run_at=utcnow() - timedelta(hours=5))

    def test_descriptions_are_human_readable(self):
        assert "Cron" in describe(ScheduleSpec.model_validate({"type": "cron", "expression": "0 2 * * *"}))
        assert describe(ScheduleSpec.model_validate({"type": "interval", "intervalSeconds": 7200})) == "Every 2h"

    def test_upcoming_returns_distinct_increasing_times(self):
        schedule = ScheduleSpec.model_validate({"type": "cron", "expression": "0 2 * * *"})
        times = upcoming_fire_times(schedule, 4)
        assert len(times) == 4
        assert times == sorted(times)


class TestLocks:
    def test_only_one_holder_at_a_time(self, mongo_db):
        first = DistributedLock(mongo_db, "recon:a", ttl_seconds=60, owner="node-1")
        second = DistributedLock(mongo_db, "recon:a", ttl_seconds=60, owner="node-2")
        assert first.acquire() is True
        assert second.acquire() is False
        first.release()
        assert second.acquire() is True
        second.release()

    def test_expired_lock_can_be_taken_over(self, mongo_db):
        holder = DistributedLock(mongo_db, "recon:b", ttl_seconds=60, owner="dead-node")
        assert holder.acquire()
        mongo_db["locks"].update_one(
            {"lockId": "recon:b"}, {"$set": {"expiresAt": utcnow() - timedelta(seconds=1)}}
        )
        successor = DistributedLock(mongo_db, "recon:b", ttl_seconds=60, owner="live-node")
        assert successor.acquire() is True
        successor.release()

    def test_renew_extends_only_for_the_token_holder(self, mongo_db):
        lock = DistributedLock(mongo_db, "recon:c", ttl_seconds=60, owner="node-1")
        assert lock.acquire()
        assert lock.renew() is True
        other = DistributedLock(mongo_db, "recon:c", ttl_seconds=60, owner="node-2")
        assert other.renew() is False
        lock.release()

    def test_context_manager_raises_when_contended(self, mongo_db):
        holder = DistributedLock(mongo_db, "recon:d", ttl_seconds=60, owner="node-1")
        holder.acquire()
        with pytest.raises(LockAcquisitionError), DistributedLock(
            mongo_db, "recon:d", ttl_seconds=60, owner="node-2"
        ):
            pass
        holder.release()

    def test_try_lock_yields_none_when_contended(self, mongo_db):
        holder = DistributedLock(mongo_db, "recon:e", ttl_seconds=60, owner="node-1")
        holder.acquire()
        with try_lock(mongo_db, "recon:e", owner="node-2") as lock:
            assert lock is None
        holder.release()
        with try_lock(mongo_db, "recon:e", owner="node-2") as lock:
            assert lock is not None

    def test_listing_and_force_release(self, mongo_db):
        lock = DistributedLock(mongo_db, "recon:f", ttl_seconds=60)
        lock.acquire()
        assert any(item["lockId"] == "recon:f" for item in list_locks(mongo_db))
        assert force_release(mongo_db, "recon:f") is True
        assert force_release(mongo_db, "recon:f") is False


class _StubConnections:
    def __init__(self, connection):
        self.connection = connection

    def get(self, connection_id):
        return self.connection


class TestConditions:
    def test_file_exists_is_satisfied(self, tmp_path, connection_definitions):
        data_file = tmp_path / "feed.csv"
        data_file.write_text("a,b\n1,2\n")
        evaluator = ConditionEvaluator(_StubConnections(connection_definitions["local_files"]))
        result = evaluator.evaluate(
            ConditionSpec.model_validate(
                {"type": "file_exists", "path": str(tmp_path), "filePattern": "*.csv"}
            )
        )
        assert result.satisfied
        assert result.details["qualifying"] == 1

    def test_file_exists_is_unsatisfied_when_absent(self, tmp_path, connection_definitions):
        evaluator = ConditionEvaluator(_StubConnections(connection_definitions["local_files"]))
        result = evaluator.evaluate(
            ConditionSpec.model_validate(
                {"type": "file_exists", "path": str(tmp_path), "filePattern": "*.parquet"}
            )
        )
        assert not result.satisfied
        assert "Waiting for" in result.summary()

    def test_empty_file_fails_the_size_requirement(self, tmp_path, connection_definitions):
        (tmp_path / "empty.csv").write_text("")
        evaluator = ConditionEvaluator(_StubConnections(connection_definitions["local_files"]))
        result = evaluator.evaluate(
            ConditionSpec.model_validate(
                {"type": "file_exists", "path": str(tmp_path), "filePattern": "*.csv", "minSizeBytes": 1}
            )
        )
        assert not result.satisfied

    def test_variables_are_rendered_into_the_path(self, tmp_path, connection_definitions):
        directory = tmp_path / "2026-09-10"
        directory.mkdir()
        (directory / "feed.csv").write_text("x\n")
        evaluator = ConditionEvaluator(
            _StubConnections(connection_definitions["local_files"]),
            variables={"business_date": "2026-09-10"},
        )
        result = evaluator.evaluate(
            ConditionSpec.model_validate(
                {"type": "file_exists", "path": f"{tmp_path}/${{business_date}}", "filePattern": "*.csv"}
            )
        )
        assert result.satisfied

    def test_and_requires_every_child(self, tmp_path, connection_definitions):
        (tmp_path / "present.csv").write_text("x\n")
        evaluator = ConditionEvaluator(_StubConnections(connection_definitions["local_files"]))
        result = evaluator.evaluate(
            ConditionSpec.model_validate(
                {
                    "operator": "AND",
                    "conditions": [
                        {"type": "file_exists", "path": str(tmp_path), "filePattern": "present.csv"},
                        {"type": "file_exists", "path": str(tmp_path), "filePattern": "absent.csv"},
                    ],
                }
            )
        )
        assert not result.satisfied
        assert len(result.unsatisfied_leaves()) == 1

    def test_or_needs_only_one_child(self, tmp_path, connection_definitions):
        (tmp_path / "present.csv").write_text("x\n")
        evaluator = ConditionEvaluator(_StubConnections(connection_definitions["local_files"]))
        result = evaluator.evaluate(
            ConditionSpec.model_validate(
                {
                    "operator": "OR",
                    "conditions": [
                        {"type": "file_exists", "path": str(tmp_path), "filePattern": "absent.csv"},
                        {"type": "file_exists", "path": str(tmp_path), "filePattern": "present.csv"},
                    ],
                }
            )
        )
        assert result.satisfied

    def test_not_inverts(self, tmp_path, connection_definitions):
        evaluator = ConditionEvaluator(_StubConnections(connection_definitions["local_files"]))
        result = evaluator.evaluate(
            ConditionSpec.model_validate(
                {
                    "operator": "NOT",
                    "conditions": [
                        {"type": "file_exists", "path": str(tmp_path), "filePattern": "absent.csv"}
                    ],
                }
            )
        )
        assert result.satisfied

    def test_nested_boolean_tree(self, tmp_path, connection_definitions):
        (tmp_path / "a.csv").write_text("x\n")
        evaluator = ConditionEvaluator(_StubConnections(connection_definitions["local_files"]))
        result = evaluator.evaluate(
            ConditionSpec.model_validate(
                {
                    "operator": "AND",
                    "conditions": [
                        {"type": "file_exists", "path": str(tmp_path), "filePattern": "a.csv"},
                        {
                            "operator": "OR",
                            "conditions": [
                                {"type": "file_exists", "path": str(tmp_path), "filePattern": "b.csv"},
                                {"type": "always"},
                            ],
                        },
                    ],
                }
            )
        )
        assert result.satisfied

    def test_previous_run_condition(self, connection_definitions):
        runs = SimpleNamespace(
            list=lambda **kwargs: [{"status": "SUCCESS", "runId": "r1", "endTime": utcnow()}]
        )
        evaluator = ConditionEvaluator(
            _StubConnections(connection_definitions["local_files"]), run_repository=runs
        )
        result = evaluator.evaluate(
            ConditionSpec.model_validate({"type": "previous_run_successful"}), recon_id="upstream"
        )
        assert result.satisfied

    def test_previous_run_condition_without_success(self, connection_definitions):
        runs = SimpleNamespace(list=lambda **kwargs: [{"status": "FAILED", "runId": "r1"}])
        evaluator = ConditionEvaluator(
            _StubConnections(connection_definitions["local_files"]), run_repository=runs
        )
        result = evaluator.evaluate(
            ConditionSpec.model_validate({"type": "previous_run_successful"}), recon_id="upstream"
        )
        assert not result.satisfied

    def test_unreachable_source_is_reported_not_raised(self, connection_definitions):
        evaluator = ConditionEvaluator(_StubConnections(connection_definitions["local_files"]))
        result = evaluator.evaluate(
            ConditionSpec.model_validate({"type": "file_exists", "path": "/nonexistent/deep/path"})
        )
        assert not result.satisfied

    @pytest.mark.parametrize(
        "value,comparator,threshold,expected",
        [
            (5, "gt", 0, True),
            (0, "gt", 0, False),
            (5, "gte", 5, True),
            (3, "lt", 5, True),
            (5, "eq", 5, True),
            (5, "ne", 5, False),
        ],
    )
    def test_scalar_comparison(self, value, comparator, threshold, expected):
        condition = ConditionSpec.model_validate(
            {
                "type": "jdbc_query",
                "connectionRef": "db",
                "query": "SELECT 1",
                "comparator": comparator,
                "threshold": threshold,
            }
        )
        satisfied, _ = _compare(value, condition)
        assert satisfied is expected

    def test_condition_result_serialisation(self):
        result = ConditionResult(True, "all good", "AND", children=[ConditionResult(True, "leaf", "always")])
        payload = result.to_dict()
        assert payload["satisfied"] is True
        assert payload["children"][0]["description"] == "leaf"
