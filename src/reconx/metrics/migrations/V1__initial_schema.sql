-- ReconX metrics database schema (PostgreSQL)
-- Generated from reconx.metrics.models - regenerate with `make db-ddl`.
-- Apply with: psql -f V1__initial_schema.sql

CREATE TABLE IF NOT EXISTS reconciliation_definition (
	recon_id VARCHAR(128) NOT NULL, 
	version INTEGER NOT NULL, 
	name VARCHAR(256) NOT NULL, 
	description TEXT, 
	product VARCHAR(128), 
	customer VARCHAR(128), 
	environment VARCHAR(64), 
	status VARCHAR(32) NOT NULL, 
	enabled BOOLEAN NOT NULL, 
	owner VARCHAR(128), 
	leg_count INTEGER, 
	schedule_type VARCHAR(32), 
	schedule_expression VARCHAR(256), 
	definition_json TEXT, 
	created_by VARCHAR(128), 
	created_at TIMESTAMP WITH TIME ZONE, 
	updated_by VARCHAR(128), 
	updated_at TIMESTAMP WITH TIME ZONE, 
	PRIMARY KEY (recon_id, version)
);

CREATE INDEX IF NOT EXISTS ix_definition_product ON reconciliation_definition (product, customer);

CREATE TABLE IF NOT EXISTS reconciliation_run (
	run_id VARCHAR(64) NOT NULL, 
	recon_id VARCHAR(128) NOT NULL, 
	recon_name VARCHAR(256), 
	version INTEGER NOT NULL, 
	product VARCHAR(128), 
	customer VARCHAR(128), 
	environment VARCHAR(64), 
	business_date VARCHAR(32), 
	status VARCHAR(32) NOT NULL, 
	trigger_type VARCHAR(32), 
	triggered_by VARCHAR(128), 
	node VARCHAR(128), 
	spark_application_id VARCHAR(128), 
	idempotency_key VARCHAR(256), 
	attempt INTEGER, 
	start_time TIMESTAMP WITH TIME ZONE, 
	end_time TIMESTAMP WITH TIME ZONE, 
	duration_ms BIGINT, 
	records_read BIGINT, 
	records_written BIGINT, 
	records_matched BIGINT, 
	records_unmatched BIGINT, 
	duplicates BIGINT, 
	exceptions BIGINT, 
	field_mismatches BIGINT, 
	match_percentage FLOAT, 
	read_time_ms BIGINT, 
	process_time_ms BIGINT, 
	write_time_ms BIGINT, 
	spark_time_ms BIGINT, 
	error_message TEXT, 
	created_at TIMESTAMP WITH TIME ZONE, 
	PRIMARY KEY (run_id)
);

CREATE INDEX IF NOT EXISTS ix_run_recon_start ON reconciliation_run (recon_id, start_time);
CREATE INDEX IF NOT EXISTS ix_run_business_date ON reconciliation_run (business_date);
CREATE INDEX IF NOT EXISTS ix_run_status ON reconciliation_run (status, start_time);

CREATE TABLE IF NOT EXISTS reconciliation_leg_run (
	id BIGSERIAL NOT NULL, 
	run_id VARCHAR(64) NOT NULL, 
	recon_id VARCHAR(128) NOT NULL, 
	leg_id VARCHAR(128) NOT NULL, 
	leg_name VARCHAR(256), 
	status VARCHAR(32) NOT NULL, 
	stage INTEGER, 
	start_time TIMESTAMP WITH TIME ZONE, 
	end_time TIMESTAMP WITH TIME ZONE, 
	duration_ms BIGINT, 
	left_source VARCHAR(128), 
	right_source VARCHAR(128), 
	recon_key VARCHAR(512), 
	match_logic VARCHAR(1024), 
	left_records BIGINT, 
	right_records BIGINT, 
	matched BIGINT, 
	mismatched BIGINT, 
	left_only BIGINT, 
	right_only BIGINT, 
	duplicates_left BIGINT, 
	duplicates_right BIGINT, 
	duplicate_keys BIGINT, 
	field_mismatches BIGINT, 
	exceptions BIGINT, 
	match_percentage FLOAT, 
	read_time_ms BIGINT, 
	process_time_ms BIGINT, 
	write_time_ms BIGINT, 
	error_message TEXT, 
	PRIMARY KEY (id)
);

CREATE UNIQUE INDEX IF NOT EXISTS ix_leg_run ON reconciliation_leg_run (run_id, leg_id);

CREATE TABLE IF NOT EXISTS reconciliation_metrics (
	id BIGSERIAL NOT NULL, 
	run_id VARCHAR(64) NOT NULL, 
	recon_id VARCHAR(128) NOT NULL, 
	leg_id VARCHAR(128), 
	metric_name VARCHAR(128) NOT NULL, 
	metric_value NUMERIC(38, 6), 
	metric_text VARCHAR(1024), 
	metric_type VARCHAR(32), 
	business_date VARCHAR(32), 
	recorded_at TIMESTAMP WITH TIME ZONE, 
	PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS ix_metrics_recon ON reconciliation_metrics (recon_id, recorded_at);
CREATE INDEX IF NOT EXISTS ix_metrics_run ON reconciliation_metrics (run_id, metric_name);

CREATE TABLE IF NOT EXISTS reconciliation_exceptions (
	id BIGSERIAL NOT NULL, 
	run_id VARCHAR(64) NOT NULL, 
	recon_id VARCHAR(128) NOT NULL, 
	leg_id VARCHAR(128) NOT NULL, 
	business_date VARCHAR(32), 
	reconciliation_key VARCHAR(1024), 
	exception_type VARCHAR(64) NOT NULL, 
	source VARCHAR(128), 
	field VARCHAR(256), 
	rule VARCHAR(256), 
	expected_value VARCHAR(2048), 
	actual_value VARCHAR(2048), 
	key_components TEXT, 
	context_columns TEXT, 
	left_occurrences INTEGER, 
	right_occurrences INTEGER, 
	status VARCHAR(32), 
	assigned_to VARCHAR(128), 
	resolution_code VARCHAR(64), 
	resolution_note TEXT, 
	resolved_by VARCHAR(128), 
	resolved_at TIMESTAMP WITH TIME ZONE, 
	reopened_count INTEGER, 
	comment_count INTEGER, 
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
	updated_at TIMESTAMP WITH TIME ZONE, 
	PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS ix_exceptions_recon_date ON reconciliation_exceptions (recon_id, business_date);
CREATE INDEX IF NOT EXISTS ix_exceptions_status ON reconciliation_exceptions (status, recon_id);
CREATE INDEX IF NOT EXISTS ix_exceptions_run ON reconciliation_exceptions (run_id, exception_type);
CREATE INDEX IF NOT EXISTS ix_exceptions_key ON reconciliation_exceptions (recon_id, reconciliation_key);

CREATE TABLE IF NOT EXISTS reconciliation_exception_comment (
	id BIGSERIAL NOT NULL, 
	exception_id BIGINT NOT NULL, 
	run_id VARCHAR(64), 
	recon_id VARCHAR(128), 
	author VARCHAR(128) NOT NULL, 
	comment TEXT NOT NULL, 
	status_before VARCHAR(32), 
	status_after VARCHAR(32), 
	created_at TIMESTAMP WITH TIME ZONE NOT NULL, 
	PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS ix_exception_comment ON reconciliation_exception_comment (exception_id, created_at);

CREATE TABLE IF NOT EXISTS reconciliation_source_metrics (
	id BIGSERIAL NOT NULL, 
	run_id VARCHAR(64) NOT NULL, 
	recon_id VARCHAR(128) NOT NULL, 
	leg_id VARCHAR(128) NOT NULL, 
	source_id VARCHAR(128) NOT NULL, 
	source_type VARCHAR(64), 
	connection_ref VARCHAR(128), 
	records_read BIGINT, 
	column_count INTEGER, 
	read_time_ms BIGINT, 
	data_quality_passed BOOLEAN, 
	data_quality_details TEXT, 
	schema_json TEXT, 
	created_at TIMESTAMP WITH TIME ZONE, 
	PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS ix_source_metrics_run ON reconciliation_source_metrics (run_id, leg_id, source_id);

CREATE TABLE IF NOT EXISTS reconciliation_field_metrics (
	id BIGSERIAL NOT NULL, 
	run_id VARCHAR(64) NOT NULL, 
	recon_id VARCHAR(128) NOT NULL, 
	leg_id VARCHAR(128) NOT NULL, 
	rule_id VARCHAR(128), 
	rule_name VARCHAR(256), 
	field_name VARCHAR(256), 
	compared_count BIGINT, 
	mismatch_count BIGINT, 
	mismatch_percentage FLOAT, 
	created_at TIMESTAMP WITH TIME ZONE, 
	PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS ix_field_metrics_run ON reconciliation_field_metrics (run_id, leg_id);

CREATE TABLE IF NOT EXISTS audit_log (
	id BIGSERIAL NOT NULL, 
	event_time TIMESTAMP WITH TIME ZONE NOT NULL, 
	action VARCHAR(64) NOT NULL, 
	entity_type VARCHAR(64) NOT NULL, 
	entity_id VARCHAR(256) NOT NULL, 
	actor VARCHAR(128) NOT NULL, 
	success BOOLEAN, 
	old_version INTEGER, 
	new_version INTEGER, 
	changes TEXT, 
	details TEXT, 
	source_ip VARCHAR(64), 
	PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS ix_audit_time ON audit_log (event_time);
CREATE INDEX IF NOT EXISTS ix_audit_entity ON audit_log (entity_type, entity_id);

CREATE TABLE IF NOT EXISTS scheduler_execution (
	id BIGSERIAL NOT NULL, 
	recon_id VARCHAR(128) NOT NULL, 
	node VARCHAR(128) NOT NULL, 
	scheduled_time TIMESTAMP WITH TIME ZONE, 
	fired_at TIMESTAMP WITH TIME ZONE NOT NULL, 
	status VARCHAR(32) NOT NULL, 
	run_id VARCHAR(64), 
	business_date VARCHAR(32), 
	conditions_met BOOLEAN, 
	condition_detail TEXT, 
	message TEXT, 
	PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS ix_scheduler_recon ON scheduler_execution (recon_id, fired_at);
