"""Kafka event envelopes.

Events are a public integration contract: downstream systems subscribe to them.
They are versioned (``schemaVersion``) and never carry secrets - the publisher
scrubs payloads before serialising.
"""

from __future__ import annotations

from typing import Any

from pydantic import Field

from reconx.common.ids import new_run_id
from reconx.common.timeutils import isoformat, utcnow
from reconx.config.models import ReconXModel

SCHEMA_VERSION = "1.0"


class EventType:
    STARTED = "RECONCILIATION_STARTED"
    STAGE_COMPLETED = "RECONCILIATION_STAGE_COMPLETED"
    LEG_COMPLETED = "RECONCILIATION_LEG_COMPLETED"
    COMPLETED = "RECONCILIATION_COMPLETED"
    FAILED = "RECONCILIATION_FAILED"
    EXCEPTION = "RECONCILIATION_EXCEPTION"
    DATA_UNAVAILABLE = "RECONCILIATION_DATA_UNAVAILABLE"
    ALERT = "RECONCILIATION_ALERT"
    CANCELLED = "RECONCILIATION_CANCELLED"


#: Event type -> topic suffix.  The full topic is ``<prefix>.<suffix>``.
TOPIC_SUFFIXES: dict[str, str] = {
    EventType.STARTED: "started",
    EventType.STAGE_COMPLETED: "stage.completed",
    EventType.LEG_COMPLETED: "stage.completed",
    EventType.COMPLETED: "completed",
    EventType.FAILED: "failed",
    EventType.EXCEPTION: "exception",
    EventType.DATA_UNAVAILABLE: "data-unavailable",
    EventType.ALERT: "alert",
    EventType.CANCELLED: "completed",
}


class ReconciliationEvent(ReconXModel):
    """The canonical event envelope."""

    event_id: str = Field(default_factory=new_run_id)
    event_type: str
    event_time: str = Field(default_factory=lambda: isoformat(utcnow()) or "")
    schema_version: str = SCHEMA_VERSION
    recon_id: str
    run_id: str | None = None
    version: int | None = None
    leg_id: str | None = None
    product: str | None = None
    customer: str | None = None
    environment: str | None = None
    business_date: str | None = None
    status: str | None = None
    node: str | None = None
    spark_application_id: str | None = None
    records_processed: int | None = None
    records_matched: int | None = None
    records_unmatched: int | None = None
    exceptions: int | None = None
    duplicates: int | None = None
    duration_ms: int | None = None
    match_percentage: float | None = None
    message: str | None = None
    details: dict[str, Any] = Field(default_factory=dict)

    def topic(self, prefix: str = "reconciliation") -> str:
        return f"{prefix}.{TOPIC_SUFFIXES.get(self.event_type, 'alert')}"

    def key(self) -> str:
        return f"{self.recon_id}:{self.run_id or self.event_id}"


def topics_for(prefix: str = "reconciliation") -> list[str]:
    return sorted({f"{prefix}.{suffix}" for suffix in TOPIC_SUFFIXES.values()})
