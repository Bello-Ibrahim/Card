"""Distributed locking built on MongoDB.

The scheduler runs on every node.  Without coordination, N nodes would fire the
same reconciliation N times.  A lock is a document with a unique ``lockId`` and
a TTL index: acquiring is an atomic upsert that only succeeds when no live lock
exists, and a crashed holder's lock expires by itself.

Locks are *advisory for scheduling*; the authoritative duplicate-run guard is
the unique idempotency key on the runs collection (see
:class:`~reconx.config.repository.RunRepository`).  Two layers, so a lock
expiring mid-run can still never produce a duplicate.
"""

from __future__ import annotations

import os
import socket
import threading
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import timedelta
from typing import Any

from pymongo.database import Database
from pymongo.errors import DuplicateKeyError

from reconx.common.errors import LockAcquisitionError
from reconx.common.logging import get_logger
from reconx.common.timeutils import utcnow
from reconx.config.store import Collections

log = get_logger(__name__)

#: Collections whose unique index has already been ensured in this process.
_INDEXED: set[int] = set()


def ensure_lock_index(database: Database) -> None:
    """Guarantee the unique index the locking protocol depends on.

    Acquisition is safe *because* two concurrent upserts cannot both insert a
    document with the same ``lockId``.  The index is normally created by
    ``ensure_indexes`` at startup; this makes a lock correct even when it is
    used before that has run.
    """
    key = id(database)
    if key in _INDEXED:
        return
    collection = database[Collections.LOCKS]
    collection.create_index("lockId", unique=True, name="uq_lock_id")
    try:
        collection.create_index("expiresAt", expireAfterSeconds=0, name="ttl_lock")
    except Exception as exc:
        log.debug("lock.ttl_index_unavailable", error=str(exc)[:200])
    _INDEXED.add(key)


def node_id() -> str:
    """Stable identity for this process (pod name in Kubernetes)."""
    return os.getenv("RECONX_NODE_ID") or os.getenv("HOSTNAME") or socket.gethostname()


class DistributedLock:
    """A TTL-bounded, renewable lock."""

    def __init__(
        self,
        database: Database,
        lock_id: str,
        *,
        ttl_seconds: int = 120,
        owner: str | None = None,
    ) -> None:
        self.db = database
        self.lock_id = lock_id
        self.ttl_seconds = ttl_seconds
        self.owner = owner or node_id()
        self.token = uuid.uuid4().hex
        self._heartbeat: threading.Timer | None = None
        self._acquired = False

    @property
    def collection(self) -> Any:
        return self.db[Collections.LOCKS]

    def acquire(self) -> bool:
        """Atomically take the lock.  Returns False when someone else holds it."""
        ensure_lock_index(self.db)
        now = utcnow()
        expires = now + timedelta(seconds=self.ttl_seconds)
        try:
            # Only replaces a lock whose TTL has already passed: the filter makes
            # this a compare-and-set, and the unique index makes it atomic.
            result = self.collection.update_one(
                {"lockId": self.lock_id, "expiresAt": {"$lte": now}},
                {
                    "$set": {
                        "lockId": self.lock_id,
                        "owner": self.owner,
                        "token": self.token,
                        "acquiredAt": now,
                        "expiresAt": expires,
                        "renewals": 0,
                    }
                },
                upsert=True,
            )
            self._acquired = bool(result.upserted_id or result.modified_count)
        except DuplicateKeyError:
            self._acquired = False
        if self._acquired:
            log.debug("lock.acquired", lock_id=self.lock_id, owner=self.owner, ttl=self.ttl_seconds)
        else:
            holder = self.collection.find_one({"lockId": self.lock_id}, {"owner": True, "expiresAt": True})
            log.debug(
                "lock.contended",
                lock_id=self.lock_id,
                held_by=(holder or {}).get("owner"),
                expires_at=str((holder or {}).get("expiresAt")),
            )
        return self._acquired

    def renew(self) -> bool:
        """Extend the TTL.  Only the current token holder can renew."""
        result = self.collection.update_one(
            {"lockId": self.lock_id, "token": self.token},
            {
                "$set": {"expiresAt": utcnow() + timedelta(seconds=self.ttl_seconds)},
                "$inc": {"renewals": 1},
            },
        )
        renewed = result.modified_count > 0
        if not renewed:
            log.warning("lock.renew_failed", lock_id=self.lock_id, owner=self.owner)
        return renewed

    def release(self) -> None:
        self._stop_heartbeat()
        if not self._acquired:
            return
        self.collection.delete_one({"lockId": self.lock_id, "token": self.token})
        self._acquired = False
        log.debug("lock.released", lock_id=self.lock_id, owner=self.owner)

    def start_heartbeat(self, interval_seconds: float | None = None) -> None:
        """Renew in the background so long jobs keep their lock."""
        interval = interval_seconds or max(5.0, self.ttl_seconds / 3)

        def _beat() -> None:
            if not self._acquired:
                return
            self.renew()
            self._schedule(interval)

        self._schedule(interval, _beat)

    def _schedule(self, interval: float, function: Any = None) -> None:
        if function is None:
            return
        self._heartbeat = threading.Timer(interval, function)
        self._heartbeat.daemon = True
        self._heartbeat.start()

    def _stop_heartbeat(self) -> None:
        if self._heartbeat is not None:
            self._heartbeat.cancel()
            self._heartbeat = None

    def __enter__(self) -> DistributedLock:
        if not self.acquire():
            raise LockAcquisitionError(
                f"Lock '{self.lock_id}' is held by another node",
                details={"lockId": self.lock_id, "owner": self.owner},
            )
        return self

    def __exit__(self, *exc: Any) -> None:
        self.release()


@contextmanager
def try_lock(
    database: Database, lock_id: str, *, ttl_seconds: int = 120, owner: str | None = None
) -> Iterator[DistributedLock | None]:
    """Acquire if free, otherwise yield ``None`` - the caller simply skips."""
    lock = DistributedLock(database, lock_id, ttl_seconds=ttl_seconds, owner=owner)
    acquired = lock.acquire()
    try:
        yield lock if acquired else None
    finally:
        if acquired:
            lock.release()


def list_locks(database: Database) -> list[dict[str, Any]]:
    return list(database[Collections.LOCKS].find({}, {"_id": False}).sort("expiresAt", -1))


def force_release(database: Database, lock_id: str) -> bool:
    """Administrative override for a lock stuck behind a crashed node."""
    result = database[Collections.LOCKS].delete_one({"lockId": lock_id})
    if result.deleted_count:
        log.warning("lock.force_released", lock_id=lock_id)
    return bool(result.deleted_count)
