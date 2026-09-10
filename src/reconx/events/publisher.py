"""Asynchronous Kafka event publishing.

Behaviour on Kafka failure is configurable per reconciliation
(``events.onFailure``):

``WARN_ONLY``  log, persist to the MongoDB outbox, and carry on (default)
``RETRY``      retry with exponential backoff, then fall back to the outbox
``FAIL_RUN``   propagate the error so the run is marked FAILED

Publishing is asynchronous: ``produce`` is non-blocking and the publisher
flushes at close.  Reconciliation results are never corrupted by a broker
outage - at worst the event lands in the outbox for replay.
"""

from __future__ import annotations

import json
import threading
from typing import TYPE_CHECKING, Any

from reconx.common.errors import EventPublishError
from reconx.common.logging import get_logger, scrub
from reconx.common.retry import RetryPolicy, call_with_retry
from reconx.common.timeutils import utcnow
from reconx.config.enums import EventFailureMode
from reconx.config.settings import Settings, get_settings
from reconx.events.schemas import ReconciliationEvent

if TYPE_CHECKING:  # pragma: no cover
    from pymongo.database import Database

log = get_logger(__name__)

OUTBOX_COLLECTION = "events_outbox"


class EventPublisher:
    """Publishes :class:`ReconciliationEvent` objects to Kafka."""

    def __init__(
        self,
        settings: Settings | None = None,
        *,
        topic_prefix: str | None = None,
        failure_mode: EventFailureMode = EventFailureMode.WARN_ONLY,
        outbox_db: Database | None = None,
        enabled: bool | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self.topic_prefix = topic_prefix or self.settings.kafka.topic_prefix
        self.failure_mode = failure_mode
        self.outbox_db = outbox_db
        self.enabled = self.settings.kafka.enabled if enabled is None else enabled
        self.extra_headers = extra_headers or {}
        self.retry_policy = RetryPolicy(max_attempts=4, initial_delay_seconds=1.0, max_delay_seconds=15.0)
        self._producer: Any = None
        self._lock = threading.Lock()
        self._delivery_failures: list[str] = []
        self._published = 0

    # ------------------------------------------------------------- producer
    def _get_producer(self) -> Any:
        if self._producer is not None:
            return self._producer
        with self._lock:
            if self._producer is not None:  # pragma: no cover - double-checked locking
                return self._producer
            try:
                from confluent_kafka import Producer
            except ImportError as exc:  # pragma: no cover - packaging guard
                raise EventPublishError("confluent-kafka is not installed") from exc
            kafka = self.settings.kafka
            config: dict[str, Any] = {
                "bootstrap.servers": kafka.bootstrap_servers,
                "client.id": kafka.client_id,
                "security.protocol": kafka.security_protocol,
                "acks": "all",
                "enable.idempotence": True,
                "retries": 5,
                "delivery.timeout.ms": kafka.delivery_timeout_ms,
                "linger.ms": 20,
                "compression.type": "snappy",
            }
            if kafka.sasl_mechanism:
                config.update(
                    {
                        "sasl.mechanism": kafka.sasl_mechanism,
                        "sasl.username": kafka.sasl_username or "",
                        "sasl.password": kafka.sasl_password or "",
                    }
                )
            if kafka.ssl_ca_location:
                config["ssl.ca.location"] = kafka.ssl_ca_location
            self._producer = Producer(config)
            log.info("events.producer_created", bootstrap=kafka.bootstrap_servers, prefix=self.topic_prefix)
            return self._producer

    def _on_delivery(self, error: Any, message: Any) -> None:
        if error is not None:
            self._delivery_failures.append(str(error))
            log.error("events.delivery_failed", error=str(error))
        else:
            self._published += 1
            log.debug("events.delivered", topic=message.topic(), partition=message.partition())

    # -------------------------------------------------------------- publish
    def publish(self, event: ReconciliationEvent) -> bool:
        """Publish one event.  Returns True when it was handed to the broker."""
        if not self.enabled:
            log.debug("events.disabled", event_type=event.event_type, recon_id=event.recon_id)
            return False

        topic = event.topic(self.topic_prefix)
        payload = scrub(event.dump())  # defence in depth: never leak secrets downstream
        body = json.dumps(payload, default=str).encode("utf-8")
        headers = [
            ("eventType", event.event_type.encode()),
            ("schemaVersion", event.schema_version.encode()),
            *[(k, str(v).encode()) for k, v in self.extra_headers.items()],
        ]

        def _produce() -> None:
            producer = self._get_producer()
            producer.produce(
                topic=topic,
                key=event.key().encode("utf-8"),
                value=body,
                headers=headers,
                on_delivery=self._on_delivery,
            )
            producer.poll(0)

        try:
            if self.failure_mode == EventFailureMode.RETRY:
                call_with_retry(_produce, policy=self.retry_policy, operation=f"kafka.publish.{topic}")
            else:
                _produce()
            log.info("events.published", topic=topic, event_type=event.event_type, run_id=event.run_id)
            return True
        except Exception as exc:
            return self._handle_failure(event, topic, payload, exc)

    def _handle_failure(
        self, event: ReconciliationEvent, topic: str, payload: dict[str, Any], exc: Exception
    ) -> bool:
        message = f"Failed to publish '{event.event_type}' to '{topic}': {exc}"
        self._write_outbox(topic, payload, str(exc))
        if self.failure_mode == EventFailureMode.FAIL_RUN:
            log.error("events.publish_failed_fatal", topic=topic, error=str(exc))
            raise EventPublishError(message, details={"topic": topic, "eventType": event.event_type})
        log.warning("events.publish_failed", topic=topic, error=str(exc), mode=self.failure_mode.value)
        return False

    def _write_outbox(self, topic: str, payload: dict[str, Any], error: str) -> None:
        """Persist undeliverable events so nothing is silently lost."""
        if self.outbox_db is None:
            return
        try:
            self.outbox_db[OUTBOX_COLLECTION].insert_one(
                {
                    "topic": topic,
                    "payload": payload,
                    "error": error[:2000],
                    "status": "PENDING",
                    "attempts": 0,
                    "createdAt": utcnow(),
                }
            )
            log.info("events.outbox_written", topic=topic)
        except Exception as outbox_exc:
            log.error("events.outbox_write_failed", error=str(outbox_exc))

    def replay_outbox(self, limit: int = 100) -> dict[str, int]:
        """Re-publish events that failed earlier (scheduler maintenance task)."""
        if self.outbox_db is None:
            return {"replayed": 0, "failed": 0}
        replayed = failed = 0
        cursor = (
            self.outbox_db[OUTBOX_COLLECTION]
            .find({"status": "PENDING"})
            .sort("createdAt", 1)
            .limit(limit)
        )
        for document in list(cursor):
            try:
                producer = self._get_producer()
                producer.produce(
                    topic=document["topic"],
                    value=json.dumps(document["payload"], default=str).encode("utf-8"),
                    on_delivery=self._on_delivery,
                )
                producer.poll(0)
                self.outbox_db[OUTBOX_COLLECTION].update_one(
                    {"_id": document["_id"]},
                    {"$set": {"status": "SENT", "sentAt": utcnow()}},
                )
                replayed += 1
            except Exception as exc:
                failed += 1
                self.outbox_db[OUTBOX_COLLECTION].update_one(
                    {"_id": document["_id"]},
                    {"$inc": {"attempts": 1}, "$set": {"error": str(exc)[:2000]}},
                )
        if replayed:
            self.flush()
        log.info("events.outbox_replayed", replayed=replayed, failed=failed)
        return {"replayed": replayed, "failed": failed}

    def flush(self, timeout_seconds: float = 15.0) -> int:
        """Block until queued events are delivered.  Returns messages still queued."""
        if self._producer is None:
            return 0
        remaining = self._producer.flush(timeout_seconds)
        if remaining:
            log.warning("events.flush_incomplete", remaining=remaining)
        if self._delivery_failures and self.failure_mode == EventFailureMode.FAIL_RUN:
            failures = list(self._delivery_failures)
            self._delivery_failures.clear()
            raise EventPublishError(
                f"{len(failures)} event(s) were not acknowledged by Kafka",
                details={"errors": failures[:5]},
            )
        return int(remaining or 0)

    def close(self) -> None:
        try:
            self.flush()
        finally:
            self._producer = None

    @property
    def stats(self) -> dict[str, Any]:
        return {
            "published": self._published,
            "deliveryFailures": len(self._delivery_failures),
            "enabled": self.enabled,
            "topicPrefix": self.topic_prefix,
        }


class NullEventPublisher(EventPublisher):
    """No-op publisher used in tests and when Kafka is intentionally disabled."""

    def __init__(self) -> None:
        super().__init__(enabled=False)
        self.events: list[ReconciliationEvent] = []

    def publish(self, event: ReconciliationEvent) -> bool:  # type: ignore[override]
        self.events.append(event)
        log.debug("events.captured", event_type=event.event_type)
        return True

    def flush(self, timeout_seconds: float = 15.0) -> int:  # type: ignore[override]
        return 0

    def close(self) -> None:  # type: ignore[override]
        return None
