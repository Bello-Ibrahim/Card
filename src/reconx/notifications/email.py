"""SMTP e-mail notifications with an HTML template.

Supports plain SMTP, STARTTLS and implicit SSL, optional authentication, and a
plain-text alternative so the message renders in any client.
"""

from __future__ import annotations

import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path
from typing import Any

from reconx.common.errors import NotificationError
from reconx.common.logging import get_logger
from reconx.common.retry import RetryPolicy, call_with_retry
from reconx.common.timeutils import format_duration
from reconx.config.models import EmailNotification
from reconx.config.settings import Settings, get_settings
from reconx.notifications.base import (
    NotificationContext,
    NotificationResult,
    Notifier,
    register_notifier,
)

log = get_logger(__name__)

TEMPLATE_DIR = Path(__file__).parent / "templates"

STATUS_COLOURS = {
    "SUCCESS": "#1a7f37",
    "PARTIAL_SUCCESS": "#9a6700",
    "FAILED": "#cf222e",
    "CANCELLED": "#6e7781",
    "SKIPPED": "#6e7781",
    "WAITING_FOR_DATA": "#0969da",
}


@register_notifier
class EmailNotifier(Notifier):
    channel = "email"

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self.retry_policy = RetryPolicy(max_attempts=3, initial_delay_seconds=5.0)

    # ------------------------------------------------------------- rendering
    def render_subject(self, context: NotificationContext, config: EmailNotification) -> str:
        prefix = config.subject_prefix or "[RECON]"
        status = context.status.replace("_", " ")
        date_part = f" - {context.business_date}" if context.business_date else ""
        return f"{prefix.rstrip(']')} {status}] {context.recon_name}{date_part}"

    def render_html(self, context: NotificationContext, config: EmailNotification) -> str:
        from jinja2 import Environment, FileSystemLoader, select_autoescape

        environment = Environment(
            loader=FileSystemLoader(str(TEMPLATE_DIR)),
            autoescape=select_autoescape(["html"]),
        )
        environment.filters["duration"] = format_duration
        environment.filters["thousands"] = lambda v: f"{int(v):,}" if v is not None else "-"
        template = environment.get_template("run_notification.html")
        return template.render(
            ctx=context,
            data=context.to_dict(),
            colour=STATUS_COLOURS.get(context.status, "#0969da"),
            config=config,
            show_exceptions=config.include_exception_sample and context.exceptions_sample,
        )

    def render_text(self, context: NotificationContext) -> str:
        metrics = context.metrics or {}
        lines = [
            f"{context.recon_name} ({context.recon_id})",
            f"Status: {context.status}",
            f"Run ID: {context.run_id}",
            f"Business date: {context.business_date or '-'}",
            f"Duration: {format_duration(context.duration_ms)}",
            "",
            f"Records:    {int(metrics.get('recordsRead', 0)):,}",
            f"Matched:    {int(metrics.get('recordsMatched', 0)):,}",
            f"Unmatched:  {int(metrics.get('recordsUnmatched', 0)):,}",
            f"Duplicates: {int(metrics.get('duplicates', 0)):,}",
            f"Exceptions: {int(metrics.get('exceptions', 0)):,}",
        ]
        if metrics.get("matchPercentage") is not None:
            lines.append(f"Match rate: {metrics['matchPercentage']}%")
        if context.error_message:
            lines += ["", f"Error: {context.error_message}"]
        if context.ui_url:
            lines += ["", f"Run details: {context.ui_url}"]
        return "\n".join(lines)

    # --------------------------------------------------------------- sending
    def send(self, context: NotificationContext, config: EmailNotification) -> NotificationResult:
        if not config.enabled:
            return NotificationResult(False, self.channel, "Email notifications are disabled")
        recipients = [r for r in config.recipients if r]
        if not recipients:
            return NotificationResult(False, self.channel, "No recipients configured")
        if not self.settings.smtp.enabled:
            log.warning("email.disabled_globally", recon_id=context.recon_id)
            return NotificationResult(False, self.channel, "SMTP is disabled by platform configuration")

        message = EmailMessage()
        message["Subject"] = self.render_subject(context, config)
        message["From"] = f"{self.settings.smtp.from_name} <{self.settings.smtp.from_address}>"
        message["To"] = ", ".join(recipients)
        if config.cc:
            message["Cc"] = ", ".join(config.cc)
        message["X-ReconX-Run-Id"] = context.run_id
        message["X-ReconX-Recon-Id"] = context.recon_id
        message.set_content(self.render_text(context))
        message.add_alternative(self.render_html(context, config), subtype="html")

        all_recipients = [*recipients, *config.cc]

        def _send() -> None:
            self._transmit(message, all_recipients)

        try:
            call_with_retry(_send, policy=self.retry_policy, operation="email.send")
        except Exception as exc:
            log.error("email.send_failed", error=str(exc), recon_id=context.recon_id)
            raise NotificationError(f"Could not send notification email: {exc}") from exc

        log.info(
            "email.sent",
            recon_id=context.recon_id,
            run_id=context.run_id,
            recipients=len(all_recipients),
            status=context.status,
        )
        return NotificationResult(True, self.channel, "Notification sent", recipients=all_recipients)

    def _transmit(self, message: EmailMessage, recipients: list[str]) -> None:
        smtp_settings = self.settings.smtp
        context = ssl.create_default_context()
        if smtp_settings.use_ssl:
            with smtplib.SMTP_SSL(
                smtp_settings.host, smtp_settings.port, timeout=smtp_settings.timeout_seconds, context=context
            ) as server:
                self._authenticate(server)
                server.send_message(message, to_addrs=recipients)
            return
        with smtplib.SMTP(
            smtp_settings.host, smtp_settings.port, timeout=smtp_settings.timeout_seconds
        ) as server:
            server.ehlo()
            if smtp_settings.use_tls:
                server.starttls(context=context)
                server.ehlo()
            self._authenticate(server)
            server.send_message(message, to_addrs=recipients)

    def _authenticate(self, server: Any) -> None:
        if self.settings.smtp.username and self.settings.smtp.password:
            server.login(self.settings.smtp.username, self.settings.smtp.password)

    def test(self, config: Any = None) -> NotificationResult:
        """Verify the SMTP endpoint is reachable and credentials are accepted."""
        smtp_settings = self.settings.smtp
        try:
            if smtp_settings.use_ssl:
                with smtplib.SMTP_SSL(
                    smtp_settings.host, smtp_settings.port, timeout=smtp_settings.timeout_seconds
                ) as server:
                    self._authenticate(server)
                    server.noop()
            else:
                with smtplib.SMTP(
                    smtp_settings.host, smtp_settings.port, timeout=smtp_settings.timeout_seconds
                ) as server:
                    server.ehlo()
                    if smtp_settings.use_tls:
                        server.starttls(context=ssl.create_default_context())
                        server.ehlo()
                    self._authenticate(server)
                    server.noop()
            return NotificationResult(
                True, self.channel, f"SMTP {smtp_settings.host}:{smtp_settings.port} is reachable"
            )
        except Exception as exc:
            return NotificationResult(False, self.channel, f"SMTP test failed: {type(exc).__name__}: {exc}")
