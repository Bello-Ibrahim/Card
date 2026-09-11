"""Retry, templating, ids, timeutils, logging redaction and secrets."""

from __future__ import annotations

from datetime import UTC, date, datetime

import pytest

from reconx.common.errors import (
    ConfigurationError,
    ConnectionFailedError,
    ReconXError,
    SecretResolutionError,
)
from reconx.common.ids import deterministic_id, idempotency_key, new_run_id, slug
from reconx.common.logging import REDACTED, scrub
from reconx.common.retry import RetryPolicy, call_with_retry, is_retryable, retry
from reconx.common.templating import build_run_variables, render, render_deep
from reconx.common.timeutils import business_date, format_duration, isoformat, to_utc

pytestmark = pytest.mark.unit


class TestRetry:
    def test_retries_then_succeeds(self):
        attempts = {"count": 0}

        def flaky():
            attempts["count"] += 1
            if attempts["count"] < 3:
                raise ConnectionFailedError("transient")
            return "ok"

        result = call_with_retry(
            flaky, policy=RetryPolicy(max_attempts=5, initial_delay_seconds=0), sleep=lambda _: None
        )
        assert result == "ok"
        assert attempts["count"] == 3

    def test_non_retryable_error_fails_immediately(self):
        attempts = {"count": 0}

        def permanent():
            attempts["count"] += 1
            raise ConfigurationError("bad configuration")

        with pytest.raises(ConfigurationError):
            call_with_retry(
                permanent, policy=RetryPolicy(max_attempts=5, initial_delay_seconds=0), sleep=lambda _: None
            )
        assert attempts["count"] == 1

    def test_attempts_are_capped(self):
        attempts = {"count": 0}

        def always_fails():
            attempts["count"] += 1
            raise ConnectionFailedError("down")

        with pytest.raises(ConnectionFailedError):
            call_with_retry(
                always_fails,
                policy=RetryPolicy(max_attempts=3, initial_delay_seconds=0),
                sleep=lambda _: None,
            )
        assert attempts["count"] == 3

    def test_backoff_grows_and_is_capped(self):
        policy = RetryPolicy(initial_delay_seconds=1, multiplier=2, max_delay_seconds=5, jitter=False)
        delays = [policy.delay_for(attempt) for attempt in range(1, 6)]
        assert delays[0] == 0.0
        assert delays[1] == 1
        assert delays[2] == 2
        assert delays[4] == 5  # capped

    def test_decorator_form(self):
        calls = {"n": 0}

        @retry(RetryPolicy(max_attempts=2, initial_delay_seconds=0))
        def sometimes(value):
            calls["n"] += 1
            if calls["n"] == 1:
                raise OSError("socket")
            return value * 2

        assert sometimes(21) == 42

    def test_retryability_classification(self):
        assert is_retryable(ConnectionFailedError("x"))
        assert not is_retryable(ConfigurationError("x"))
        assert is_retryable(OSError("socket"))
        assert not is_retryable(ValueError("plain"))

    def test_policy_from_config(self):
        policy = RetryPolicy.from_config({"maxAttempts": 7, "initialDelaySeconds": 4})
        assert policy.max_attempts == 7
        assert policy.initial_delay_seconds == 4


class TestTemplating:
    def test_built_in_variables(self):
        variables = build_run_variables(biz_date=date(2026, 9, 10))
        assert variables["business_date"] == "2026-09-10"
        assert variables["business_date_compact"] == "20260910"
        assert variables["prev_business_date"] == "2026-09-09"
        assert variables["next_business_date"] == "2026-09-11"

    def test_render_into_a_sql_query_and_table_name(self):
        variables = build_run_variables(biz_date=date(2026, 9, 10), extra={"tbl": "[dbo].[Ledger]"})
        statement = render(
            "SELECT TOP (10) * FROM ${tbl} WHERE [BusinessDate] = '${business_date}'", variables
        )
        assert statement == (
            "SELECT TOP (10) * FROM [dbo].[Ledger] WHERE [BusinessDate] = '2026-09-10'"
        )

    def test_inline_default(self):
        assert render("${missing:fallback}", {}) == "fallback"

    def test_unresolved_variable_raises_in_strict_mode(self):
        with pytest.raises(ConfigurationError):
            render("${nope}", {"business_date": "2026-09-10"})

    def test_unresolved_variable_is_left_alone_when_not_strict(self):
        assert render("${nope}", {}, strict=False) == "${nope}"

    def test_render_deep_handles_nested_structures(self):
        payload = {"path": "s3://b/${business_date}/*.parquet", "items": [{"q": "d='${business_date}'"}]}
        rendered = render_deep(payload, {"business_date": "2026-09-10"})
        assert rendered["path"] == "s3://b/2026-09-10/*.parquet"
        assert rendered["items"][0]["q"] == "d='2026-09-10'"


class TestIdentifiers:
    def test_idempotency_key_is_deterministic(self):
        first = idempotency_key("recon", 2, {"business_date": "2026-09-10"})
        second = idempotency_key("recon", 2, {"business_date": "2026-09-10"})
        assert first == second

    def test_idempotency_key_varies_with_dimensions(self):
        assert idempotency_key("recon", 1, {"business_date": "2026-09-10"}) != idempotency_key(
            "recon", 1, {"business_date": "2026-09-11"}
        )

    def test_idempotency_key_varies_with_version(self):
        assert idempotency_key("recon", 1, {}) != idempotency_key("recon", 2, {})

    def test_run_ids_are_unique(self):
        assert len({new_run_id() for _ in range(200)}) == 200

    def test_slug_and_deterministic_id(self):
        assert slug("Payments Daily!") == "payments-daily"
        assert deterministic_id("a", 1) == deterministic_id("a", 1)


class TestRedaction:
    def test_secret_keys_are_redacted(self):
        payload = {
            "username": "svc",
            "password": "hunter2",
            "config": {"secretKey": "abc", "accessKey": "AKIA", "endpoint": "https://s3"},
            "list": [{"saslPassword": "p"}],
        }
        scrubbed = scrub(payload)
        assert scrubbed["username"] == "svc"
        assert scrubbed["password"] == REDACTED
        assert scrubbed["config"]["secretKey"] == REDACTED
        assert scrubbed["config"]["endpoint"] == "https://s3"
        assert scrubbed["list"][0]["saslPassword"] == REDACTED


class TestTimeUtils:
    def test_business_date_offset(self):
        reference = datetime(2026, 9, 10, 3, 0, tzinfo=UTC)
        assert business_date(reference, offset_days=-1) == date(2026, 9, 9)

    def test_timezone_shifts_the_calendar_date(self):
        reference = datetime(2026, 9, 10, 2, 0, tzinfo=UTC)
        assert business_date(reference, tz="America/New_York") == date(2026, 9, 9)

    @pytest.mark.parametrize(
        "millis,expected",
        [(None, "-"), (5000, "5s"), (65000, "1m 5s"), (3_725_000, "1h 2m 5s")],
    )
    def test_duration_formatting(self, millis, expected):
        assert format_duration(millis) == expected

    def test_isoformat_is_utc_z(self):
        assert isoformat(datetime(2026, 9, 10, 12, 0, tzinfo=UTC)) == "2026-09-10T12:00:00Z"

    def test_naive_datetimes_are_treated_as_utc(self):
        assert to_utc(datetime(2026, 9, 10, 12, 0)).tzinfo is UTC


class TestSecrets:
    def test_encrypt_and_resolve_round_trip(self):
        from reconx.security.secrets import SecretResolver

        resolver = SecretResolver()
        reference = resolver.encrypt_for_storage("super-secret")
        assert reference.startswith("enc:")
        assert resolver.resolve(reference) == "super-secret"

    def test_environment_reference(self, monkeypatch):
        from reconx.security.secrets import SecretResolver

        monkeypatch.setenv("RECONX_TEST_SECRET", "from-env")
        assert SecretResolver().resolve("env:RECONX_TEST_SECRET") == "from-env"

    def test_missing_environment_variable_raises(self):
        from reconx.security.secrets import SecretResolver

        with pytest.raises(SecretResolutionError):
            SecretResolver().resolve("env:DEFINITELY_NOT_SET_12345")

    def test_file_reference(self, tmp_path):
        from reconx.security.secrets import SecretResolver

        secret_file = tmp_path / "pw"
        secret_file.write_text("file-secret\n")
        assert SecretResolver().resolve(f"file:{secret_file}") == "file-secret"

    def test_existing_reference_is_not_double_encrypted(self):
        from reconx.security.secrets import SecretResolver

        resolver = SecretResolver()
        assert resolver.encrypt_for_storage("env:MY_VAR") == "env:MY_VAR"

    def test_resolve_mapping_only_touches_secret_fields(self):
        from reconx.config.connections import SECRET_FIELDS
        from reconx.security.secrets import SecretResolver

        resolver = SecretResolver()
        config = {"host": "db", "password": resolver.encrypt_for_storage("pw")}
        resolved = resolver.resolve_mapping(config, SECRET_FIELDS)
        assert resolved["host"] == "db"
        assert resolved["password"] == "pw"


class TestErrors:
    def test_error_serialisation(self):
        error = ReconXError("boom", details={"a": 1})
        assert error.to_dict() == {
            "code": "RECONX_ERROR",
            "message": "boom",
            "retryable": False,
            "details": {"a": 1},
        }

    def test_retryable_flag_is_declared_per_type(self):
        assert ConnectionFailedError("x").retryable is True
        assert ConfigurationError("x").retryable is False
