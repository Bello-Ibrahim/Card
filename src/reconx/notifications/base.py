"""Notifier plugin interface.

Adding a channel (Slack, Teams, PagerDuty, ServiceNow) means implementing
:class:`Notifier` and registering it - no changes to the engine or scheduler.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from reconx.common.logging import get_logger
from reconx.config.enums import NotifyOn

log = get_logger(__name__)


@dataclass
class NotificationContext:
    """Everything a channel needs to render a message."""

    recon_id: str
    recon_name: str
    run_id: str
    status: str
    business_date: str | None = None
    trigger: str | None = None
    started_at: str | None = None
    ended_at: str | None = None
    duration_ms: int | None = None
    metrics: dict[str, Any] = field(default_factory=dict)
    legs: list[dict[str, Any]] = field(default_factory=list)
    exceptions_sample: list[dict[str, Any]] = field(default_factory=list)
    error_message: str | None = None
    product: str | None = None
    customer: str | None = None
    environment: str | None = None
    spark_application_id: str | None = None
    ui_url: str | None = None
    notify_reason: NotifyOn = NotifyOn.SUCCESS

    def to_dict(self) -> dict[str, Any]:
        return {
            "reconId": self.recon_id,
            "reconName": self.recon_name,
            "runId": self.run_id,
            "status": self.status,
            "businessDate": self.business_date,
            "trigger": self.trigger,
            "startedAt": self.started_at,
            "endedAt": self.ended_at,
            "durationMs": self.duration_ms,
            "metrics": self.metrics,
            "legs": self.legs,
            "exceptionsSample": self.exceptions_sample,
            "errorMessage": self.error_message,
            "product": self.product,
            "customer": self.customer,
            "environment": self.environment,
            "sparkApplicationId": self.spark_application_id,
            "uiUrl": self.ui_url,
            "notifyReason": self.notify_reason.value,
        }


@dataclass
class NotificationResult:
    success: bool
    channel: str
    message: str
    recipients: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "success": self.success,
            "channel": self.channel,
            "message": self.message,
            "recipients": self.recipients,
        }


class Notifier(ABC):
    channel: str = "abstract"

    @abstractmethod
    def send(self, context: NotificationContext, config: Any) -> NotificationResult: ...

    @abstractmethod
    def test(self, config: Any) -> NotificationResult: ...


_REGISTRY: dict[str, Notifier] = {}


def register_notifier(cls: type[Notifier]) -> type[Notifier]:
    _REGISTRY[cls.channel] = cls()
    log.debug("notifier.registered", channel=cls.channel)
    return cls


def get_notifier(channel: str) -> Notifier:
    if channel not in _REGISTRY:
        raise KeyError(f"No notifier registered for channel '{channel}' (have: {sorted(_REGISTRY)})")
    return _REGISTRY[channel]


def available_notifiers() -> list[str]:
    return sorted(_REGISTRY)


def should_notify(status: str, configured: list[NotifyOn], *, exception_threshold_breached: bool = False) -> NotifyOn | None:
    """Decide whether a completed run warrants a notification."""
    mapping = {
        "SUCCESS": NotifyOn.SUCCESS,
        "PARTIAL_SUCCESS": NotifyOn.PARTIAL_SUCCESS,
        "FAILED": NotifyOn.FAILURE,
        "CANCELLED": NotifyOn.CANCELLED,
        "SKIPPED": NotifyOn.DATA_UNAVAILABLE,
        "WAITING_FOR_DATA": NotifyOn.DATA_UNAVAILABLE,
    }
    if exception_threshold_breached and NotifyOn.EXCEPTION_THRESHOLD in configured:
        return NotifyOn.EXCEPTION_THRESHOLD
    reason = mapping.get(status)
    if reason and reason in configured:
        return reason
    return None
