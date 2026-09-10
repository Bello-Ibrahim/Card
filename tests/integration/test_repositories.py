"""Repository behaviour: versioning, idempotency, connections and audit."""

from __future__ import annotations

import pytest

from reconx.common.errors import ConflictError, DuplicateRunError, NotFoundError
from reconx.config.connections import ConnectionDefinition
from reconx.config.enums import DefinitionStatus, RunStatus, TriggerType
from reconx.config.models import ReconciliationDefinition
from reconx.config.repository import (
    ConnectionRepository,
    ReconciliationRepository,
    RunRepository,
)
from reconx.config.store import Collections
from reconx.security.audit import AuditLogger, diff_documents

pytestmark = pytest.mark.integration


@pytest.fixture
def repository(mongo_db):
    return ReconciliationRepository(mongo_db, AuditLogger(mongo_db))


@pytest.fixture
def definition(sample_definition):
    return ReconciliationDefinition.model_validate(sample_definition)


class TestVersioning:
    def test_create_stores_version_one(self, repository, definition):
        created = repository.create(definition, actor="alice")
        assert created.version == 1
        assert created.status == DefinitionStatus.DRAFT
        assert created.created_by == "alice"

    def test_duplicate_create_is_rejected(self, repository, definition):
        repository.create(definition, actor="alice")
        with pytest.raises(ConflictError):
            repository.create(definition, actor="alice")

    def test_saving_appends_a_version_without_destroying_the_old_one(self, repository, definition):
        repository.create(definition, actor="alice")
        updated = definition.model_copy(update={"description": "second version"})
        saved = repository.save_new_version(updated, actor="bob", comment="tweak")
        assert saved.version == 2
        history = repository.list_versions(definition.recon_id)
        assert [v["version"] for v in history] == [2, 1]
        assert repository.get(definition.recon_id, version=1).description != "second version"

    def test_editing_an_active_definition_does_not_change_what_runs(self, repository, definition):
        repository.create(definition, actor="alice")
        repository.activate_version(definition.recon_id, actor="alice")
        updated = definition.model_copy(update={"description": "draft change"})
        repository.save_new_version(updated, actor="bob")
        head = repository.get(definition.recon_id)
        assert head.version == 1
        assert head.status == DefinitionStatus.ACTIVE
        assert head.description != "draft change"

    def test_explicit_activation_promotes_the_new_version(self, repository, definition):
        repository.create(definition, actor="alice")
        repository.activate_version(definition.recon_id, actor="alice")
        updated = definition.model_copy(update={"description": "v2"})
        repository.save_new_version(updated, actor="bob", activate=True)
        head = repository.get(definition.recon_id)
        assert head.version == 2 and head.status == DefinitionStatus.ACTIVE

    def test_optimistic_concurrency_check(self, repository, definition):
        repository.create(definition, actor="alice")
        with pytest.raises(ConflictError):
            repository.save_new_version(definition, actor="bob", expected_version=99)

    def test_rollback_republishes_as_a_new_version(self, repository, definition):
        repository.create(definition, actor="alice")
        repository.save_new_version(
            definition.model_copy(update={"description": "v2"}), actor="bob"
        )
        restored = repository.rollback(definition.recon_id, 1, actor="carol")
        assert restored.version == 3
        assert restored.description == definition.description
        assert len(repository.list_versions(definition.recon_id)) == 3

    def test_rollback_to_the_current_version_is_rejected(self, repository, definition):
        repository.create(definition, actor="alice")
        with pytest.raises(ConflictError):
            repository.rollback(definition.recon_id, 1, actor="alice")

    def test_archived_definitions_cannot_be_modified(self, repository, definition):
        repository.create(definition, actor="alice")
        repository.archive(definition.recon_id, actor="alice")
        with pytest.raises(ConflictError):
            repository.save_new_version(definition, actor="alice")

    def test_clone_creates_an_independent_draft(self, repository, definition):
        repository.create(definition, actor="alice")
        repository.activate_version(definition.recon_id, actor="alice")
        clone = repository.clone(definition.recon_id, "payments_copy", actor="bob")
        assert clone.recon_id == "payments_copy"
        assert clone.status == DefinitionStatus.DRAFT
        assert clone.version == 1

    def test_missing_definition_raises(self, repository):
        with pytest.raises(NotFoundError):
            repository.get("does_not_exist")

    def test_list_active_only_returns_enabled_active(self, repository, definition):
        repository.create(definition, actor="alice")
        assert repository.list_active() == []
        repository.activate_version(definition.recon_id, actor="alice")
        assert [d.recon_id for d in repository.list_active()] == [definition.recon_id]

    def test_filters_and_facets(self, repository, definition):
        repository.create(definition, actor="alice")
        assert repository.list(product="PAYMENTS")
        assert repository.list(search="Payments")
        assert repository.distinct("product") == ["PAYMENTS"]


class TestConnections:
    def test_secrets_are_encrypted_at_rest(self, mongo_db):
        repository = ConnectionRepository(mongo_db)
        connection = ConnectionDefinition.model_validate(
            {
                "connectionId": "pg_main",
                "name": "PG",
                "type": "jdbc",
                "config": {
                    "databaseType": "postgresql",
                    "host": "db",
                    "database": "reconx",
                    "username": "u",
                    "password": "plaintext-secret",
                },
            }
        )
        repository.create(connection, actor="alice")
        stored = mongo_db[Collections.CONNECTIONS].find_one({"connectionId": "pg_main"})
        assert stored["config"]["password"] != "plaintext-secret"
        assert stored["config"]["password"].startswith("enc:")

    def test_masked_view_never_exposes_a_secret(self, mongo_db):
        repository = ConnectionRepository(mongo_db)
        repository.create(
            ConnectionDefinition.model_validate(
                {
                    "connectionId": "c1",
                    "name": "C",
                    "type": "jdbc",
                    "config": {"host": "h", "database": "d", "username": "u", "password": "s3cret"},
                }
            ),
            actor="alice",
        )
        masked = repository.get("c1").masked()
        assert masked["config"]["password"] == "********"

    def test_masked_password_on_update_keeps_the_stored_value(self, mongo_db):
        repository = ConnectionRepository(mongo_db)
        repository.create(
            ConnectionDefinition.model_validate(
                {
                    "connectionId": "c2",
                    "name": "C",
                    "type": "jdbc",
                    "config": {"host": "h", "database": "d", "username": "u", "password": "original"},
                }
            ),
            actor="alice",
        )
        stored_before = mongo_db[Collections.CONNECTIONS].find_one({"connectionId": "c2"})["config"]["password"]
        repository.update(
            ConnectionDefinition.model_validate(
                {
                    "connectionId": "c2",
                    "name": "C renamed",
                    "type": "jdbc",
                    "config": {"host": "h", "database": "d", "username": "u", "password": "********"},
                }
            ),
            actor="bob",
        )
        stored_after = mongo_db[Collections.CONNECTIONS].find_one({"connectionId": "c2"})["config"]["password"]
        assert stored_after == stored_before

    def test_connection_in_use_cannot_be_deleted(self, mongo_db, sample_definition):
        connections = ConnectionRepository(mongo_db)
        connections.create(
            ConnectionDefinition.model_validate(
                {
                    "connectionId": "local_files",
                    "name": "Files",
                    "type": "filesystem",
                    "config": {"basePath": "/"},
                }
            ),
            actor="alice",
        )
        ReconciliationRepository(mongo_db).create(
            ReconciliationDefinition.model_validate(sample_definition), actor="alice"
        )
        with pytest.raises(ConflictError):
            connections.delete("local_files", actor="alice")


class TestRuns:
    def test_idempotency_key_prevents_duplicate_runs(self, mongo_db, definition):
        from reconx.config.store import ensure_indexes

        ensure_indexes(mongo_db)
        runs = RunRepository(mongo_db)
        runs.create(
            run_id="run-1",
            definition=definition,
            trigger_type=TriggerType.SCHEDULED,
            triggered_by="scheduler",
            business_date="2026-09-10",
        )
        with pytest.raises(DuplicateRunError):
            runs.create(
                run_id="run-2",
                definition=definition,
                trigger_type=TriggerType.SCHEDULED,
                triggered_by="scheduler-on-another-node",
                business_date="2026-09-10",
            )

    def test_different_business_dates_are_distinct_runs(self, mongo_db, definition):
        from reconx.config.store import ensure_indexes

        ensure_indexes(mongo_db)
        runs = RunRepository(mongo_db)
        runs.create(
            run_id="run-1",
            definition=definition,
            trigger_type=TriggerType.SCHEDULED,
            triggered_by="s",
            business_date="2026-09-10",
        )
        second = runs.create(
            run_id="run-2",
            definition=definition,
            trigger_type=TriggerType.SCHEDULED,
            triggered_by="s",
            business_date="2026-09-11",
        )
        assert second["runId"] == "run-2"

    def test_status_transitions_record_timing(self, mongo_db, definition):
        runs = RunRepository(mongo_db)
        runs.create(
            run_id="run-3",
            definition=definition,
            trigger_type=TriggerType.MANUAL,
            triggered_by="alice",
            business_date="2026-09-10",
        )
        runs.update_status("run-3", RunStatus.RUNNING)
        completed = runs.update_status("run-3", RunStatus.SUCCESS, metrics={"recordsRead": 10})
        assert completed["status"] == "SUCCESS"
        assert completed["durationMs"] is not None
        assert completed["metrics"]["recordsRead"] == 10

    def test_active_run_counting(self, mongo_db, definition):
        runs = RunRepository(mongo_db)
        runs.create(
            run_id="run-4",
            definition=definition,
            trigger_type=TriggerType.MANUAL,
            triggered_by="alice",
            business_date="2026-09-10",
        )
        assert runs.count_active(definition.recon_id) == 1
        runs.update_status("run-4", RunStatus.SUCCESS)
        assert runs.count_active(definition.recon_id) == 0

    def test_claim_queued_is_exclusive(self, mongo_db, definition):
        runs = RunRepository(mongo_db)
        runs.create(
            run_id="run-5",
            definition=definition,
            trigger_type=TriggerType.SCHEDULED,
            triggered_by="s",
            business_date="2026-09-10",
        )
        first = runs.claim_queued("node-a", limit=5)
        second = runs.claim_queued("node-b", limit=5)
        assert len(first) == 1
        assert second == []

    def test_statistics(self, mongo_db, definition):
        runs = RunRepository(mongo_db)
        for index, status in enumerate([RunStatus.SUCCESS, RunStatus.FAILED]):
            runs.create(
                run_id=f"stat-{index}",
                definition=definition,
                trigger_type=TriggerType.MANUAL,
                triggered_by="alice",
                business_date=f"2026-09-{10 + index}",
            )
            runs.update_status(f"stat-{index}", status, metrics={"recordsRead": 100, "recordsMatched": 90})
        statistics = runs.statistics()
        assert statistics["total"] == 2
        assert statistics["byStatus"]["SUCCESS"] == 1


class TestAudit:
    def test_changes_are_recorded_with_a_diff(self, mongo_db, definition):
        audit = AuditLogger(mongo_db)
        repository = ReconciliationRepository(mongo_db, audit)
        repository.create(definition, actor="alice")
        repository.save_new_version(
            definition.model_copy(update={"description": "changed"}), actor="bob", comment="why"
        )
        entries = audit.query(entity_type="reconciliation", entity_id=definition.recon_id)
        actions = [entry["action"] for entry in entries]
        assert "CREATE" in actions and "UPDATE" in actions
        update_entry = next(entry for entry in entries if entry["action"] == "UPDATE")
        assert update_entry["oldVersion"] == 1 and update_entry["newVersion"] == 2

    def test_diff_ignores_volatile_fields(self):
        changes = diff_documents(
            {"name": "a", "updatedAt": "t1", "version": 1}, {"name": "b", "updatedAt": "t2", "version": 2}
        )
        assert set(changes) == {"name"}

    def test_secrets_are_scrubbed_from_audit_details(self, mongo_db):
        audit = AuditLogger(mongo_db)
        audit.record(
            action="TEST",
            entity_type="connection",
            entity_id="c1",
            actor="alice",
            details={"password": "hunter2", "host": "db"},
        )
        entry = audit.query(entity_type="connection")[0]
        assert entry["details"]["password"] == "***REDACTED***"
        assert entry["details"]["host"] == "db"
