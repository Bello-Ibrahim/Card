"""Configuration validation: DAG shape, references, SQL safety and semantics.

Validation is deliberately *reported* rather than raised one error at a time -
the UI shows the operator every problem at once.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any

from reconx.common.errors import CyclicDependencyError
from reconx.config.enums import (
    ComparisonRule,
    ConditionType,
    OutputType,
    ScheduleType,
    SourceType,
    TransformType,
)
from reconx.config.models import (
    ConditionSpec,
    LegSpec,
    ReconciliationDefinition,
    _walk_conditions,
)
from reconx.security.sql_guard import (
    assert_read_only,
    assert_safe_expression,
    assert_table_name,
)


@dataclass
class ValidationIssue:
    severity: str  # ERROR | WARNING | INFO
    path: str
    message: str
    hint: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {"severity": self.severity, "path": self.path, "message": self.message, "hint": self.hint}


@dataclass
class ValidationReport:
    issues: list[ValidationIssue] = field(default_factory=list)
    execution_order: list[list[str]] = field(default_factory=list)

    def error(self, path: str, message: str, hint: str | None = None) -> None:
        self.issues.append(ValidationIssue("ERROR", path, message, hint))

    def warn(self, path: str, message: str, hint: str | None = None) -> None:
        self.issues.append(ValidationIssue("WARNING", path, message, hint))

    def info(self, path: str, message: str, hint: str | None = None) -> None:
        self.issues.append(ValidationIssue("INFO", path, message, hint))

    @property
    def errors(self) -> list[ValidationIssue]:
        return [i for i in self.issues if i.severity == "ERROR"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [i for i in self.issues if i.severity == "WARNING"]

    @property
    def valid(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict[str, Any]:
        return {
            "valid": self.valid,
            "errorCount": len(self.errors),
            "warningCount": len(self.warnings),
            "issues": [i.to_dict() for i in self.issues],
            "executionOrder": self.execution_order,
        }


# --------------------------------------------------------------------------- #
# DAG helpers
# --------------------------------------------------------------------------- #
def build_dependency_graph(legs: list[LegSpec]) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {leg.id: set() for leg in legs}
    for leg in legs:
        for dep in leg.depends_on:
            if dep in graph:
                graph[leg.id].add(dep)
    return graph


#: DFS colouring used by cycle detection.
_WHITE, _GREY, _BLACK = 0, 1, 2


def detect_cycles(graph: dict[str, set[str]]) -> list[list[str]]:
    """Return every dependency cycle (DFS with colouring)."""
    colour: dict[str, int] = defaultdict(int)  # 0 = unvisited, 1 = on the stack, 2 = done
    stack: list[str] = []
    cycles: list[list[str]] = []

    def visit(node: str) -> None:
        colour[node] = _GREY
        stack.append(node)
        for dep in sorted(graph.get(node, ())):
            if colour[dep] == _WHITE:
                visit(dep)
            elif colour[dep] == _GREY:
                start = stack.index(dep)
                cycle = [*stack[start:], dep]
                if cycle not in cycles:
                    cycles.append(cycle)
        stack.pop()
        colour[node] = _BLACK

    for node in sorted(graph):
        if colour[node] == _WHITE:
            visit(node)
    return cycles


def topological_stages(graph: dict[str, set[str]]) -> list[list[str]]:
    """Group legs into stages; legs in the same stage can run in parallel."""
    cycles = detect_cycles(graph)
    if cycles:
        raise CyclicDependencyError(
            "Reconciliation legs form a dependency cycle: "
            + "; ".join(" -> ".join(c) for c in cycles),
            details={"cycles": cycles},
        )
    remaining = {node: set(deps) for node, deps in graph.items()}
    stages: list[list[str]] = []
    while remaining:
        ready = sorted(node for node, deps in remaining.items() if not deps)
        if not ready:  # pragma: no cover - guarded by detect_cycles
            raise CyclicDependencyError("Unresolvable leg dependencies", details={"remaining": list(remaining)})
        stages.append(ready)
        for node in ready:
            remaining.pop(node)
        for deps in remaining.values():
            deps.difference_update(ready)
    return stages


# --------------------------------------------------------------------------- #
# Validation
# --------------------------------------------------------------------------- #
def validate_definition(
    definition: ReconciliationDefinition,
    *,
    available_connections: dict[str, str] | None = None,
    known_recon_ids: set[str] | None = None,
) -> ValidationReport:
    """Full static validation.

    ``available_connections`` maps connection id -> type.  ``None`` means "the
    caller does not know which connections exist" and connection references are
    left unchecked; an empty dict means "no connections exist", which *is* an
    error for a definition that references one.
    """
    report = ValidationReport()

    if not definition.legs:
        report.error("legs", "A reconciliation must define at least one leg")
        return report

    _validate_dag(definition, report)
    _validate_legs(definition, report, available_connections)
    _validate_conditions(definition.conditions, report, available_connections, known_recon_ids or set())
    _validate_schedule(definition, report)
    _validate_notifications(definition, report)
    return report


def _validate_dag(definition: ReconciliationDefinition, report: ValidationReport) -> None:
    legs = definition.enabled_legs
    graph = build_dependency_graph(legs)
    leg_ids = set(graph)
    for leg in legs:
        for dep in leg.depends_on:
            if dep not in leg_ids:
                report.error(
                    f"legs.{leg.id}.dependsOn",
                    f"Leg '{leg.id}' depends on '{dep}' which does not exist or is disabled",
                )
    try:
        report.execution_order = topological_stages(
            {k: {d for d in v if d in leg_ids} for k, v in graph.items()}
        )
    except CyclicDependencyError as exc:
        for cycle in exc.details.get("cycles", []):
            report.error("legs", "Cyclic leg dependency: " + " -> ".join(cycle),
                         hint="A leg cannot (transitively) consume its own output")
    if len(report.execution_order) > 1:
        report.info("legs", f"Execution plan: {len(report.execution_order)} stage(s)")


def _validate_legs(
    definition: ReconciliationDefinition, report: ValidationReport, connections: dict[str, str] | None
) -> None:
    leg_ids = {leg.id for leg in definition.legs}
    produced_views: set[str] = set()

    for leg in definition.legs:
        path = f"legs.{leg.id}"
        for source in leg.sources:
            spath = f"{path}.sources.{source.id}"
            if source.connection_ref and connections is not None:
                conn_type = connections.get(source.connection_ref)
                if conn_type is None:
                    report.error(spath, f"Connection '{source.connection_ref}' does not exist")
                elif not _connection_matches(source.type, conn_type):
                    report.error(
                        spath,
                        f"Source type '{source.type.value}' cannot use a '{conn_type}' connection",
                    )
            if source.type == SourceType.LEG_OUTPUT:
                if source.leg_ref not in leg_ids:
                    report.error(spath, f"legRef '{source.leg_ref}' is not a known leg")
                elif source.leg_ref == leg.id:
                    report.error(spath, "A leg cannot consume its own output")
            if source.type == SourceType.TEMP_VIEW and source.view and source.view not in produced_views:
                report.warn(
                    spath,
                    f"Temp view '{source.view}' is not produced by an earlier leg in this definition",
                    hint="Make sure a preceding transformation or leg registers this view",
                )
            if source.register_temp_view:
                produced_views.add(source.register_temp_view)
            if source.query:
                _safe_sql(report, f"{spath}.query", source.query)
            if source.table:
                _safe_identifier(report, f"{spath}.table", source.table)
            if source.filter:
                _safe_expression(report, f"{spath}.filter", source.filter)
            for i, transform in enumerate(source.transformations):
                _validate_transformation(report, f"{spath}.transformations[{i}]", transform, produced_views)
            for dq in source.data_quality:
                if dq.sql:
                    _safe_expression(report, f"{spath}.dataQuality.{dq.type.value}", dq.sql)

        for i, transform in enumerate(leg.pre_transformations):
            _validate_transformation(report, f"{path}.preTransformations[{i}]", transform, produced_views)
        for i, transform in enumerate(leg.post_transformations):
            _validate_transformation(report, f"{path}.postTransformations[{i}]", transform, produced_views)

        if len(leg.sources) > 1 and not leg.keys:
            report.error(f"{path}.keys", "A two-sided leg requires at least one key mapping")
        for key in leg.keys:
            if key.normalization and key.normalization.expression:
                _safe_expression(report, f"{path}.keys.{key.key_alias}", key.normalization.expression)

        logic = leg.effective_match_logic()
        if logic is None:
            report.warn(
                f"{path}.comparisons",
                "No field comparisons configured - the leg only reports presence (LEFT_ONLY / RIGHT_ONLY)",
                hint="Add a matching logic to detect value differences (MISMATCH)",
            )
        else:
            seen_rule_ids: set[str] = set()
            for rule in logic.all_rules():
                if rule.id in seen_rule_ids:
                    report.error(f"{path}.matchLogic", f"Duplicate matching-rule id '{rule.id}'")
                seen_rule_ids.add(rule.id)
                for comparison in rule.comparisons:
                    cpath = f"{path}.matchLogic.{rule.id}.{comparison.field_name}"
                    if comparison.rule == ComparisonRule.EXPRESSION:
                        if not comparison.expression:
                            report.error(cpath, "Comparison rule 'expression' requires an 'expression'")
                        else:
                            _safe_expression(report, cpath, comparison.expression)
                    if comparison.rule in (
                        ComparisonRule.NUMERIC_TOLERANCE,
                        ComparisonRule.PERCENTAGE_TOLERANCE,
                        ComparisonRule.DATE_TOLERANCE,
                    ) and comparison.tolerance is None:
                        report.error(cpath, f"Comparison rule '{comparison.rule.value}' requires 'tolerance'")
            report.info(f"{path}.matchLogic", f"Matching logic: {logic.describe()}")

        for output in [*leg.outputs, leg.exception_output]:
            if output is None or not output.enabled:
                continue
            opath = f"{path}.outputs.{output.id or output.type.value}"
            if output.connection_ref and connections is not None:
                conn_type = connections.get(output.connection_ref)
                if conn_type is None:
                    report.error(opath, f"Connection '{output.connection_ref}' does not exist")
            if output.type == OutputType.JDBC and output.table:
                _safe_identifier(report, f"{opath}.table", output.table)
            if output.type == OutputType.TEMP_VIEW and output.view:
                produced_views.add(output.view)

        if not leg.outputs and not leg.exception_output:
            report.warn(
                f"{path}.outputs",
                "Leg has no outputs configured - results will only exist in the metrics database",
                hint="Add a JDBC/S3 output to persist matched/unmatched detail",
            )
        if leg.register_result_view:
            produced_views.add(leg.register_result_view)


def _connection_matches(source_type: SourceType, connection_type: str) -> bool:
    mapping = {
        SourceType.S3: {"s3", "storagegrid"},
        SourceType.STORAGEGRID: {"storagegrid", "s3"},
        SourceType.SFTP: {"sftp"},
        SourceType.JDBC: {"jdbc"},
        SourceType.KAFKA: {"kafka"},
        SourceType.FILESYSTEM: {"filesystem"},
        SourceType.EXCEL: {"filesystem", "s3", "storagegrid", "sftp"},
    }
    allowed = mapping.get(source_type)
    return allowed is None or connection_type in allowed


def _validate_transformation(
    report: ValidationReport, path: str, transform: Any, produced_views: set[str]
) -> None:
    if transform.type in (TransformType.SQL, TransformType.TEMP_VIEW) and transform.sql:
        _safe_sql(report, f"{path}.sql", transform.sql)
        if transform.type == TransformType.TEMP_VIEW and transform.view_name:
            produced_views.add(transform.view_name)
    if transform.type == TransformType.FILTER and (transform.condition or transform.expression):
        _safe_expression(report, f"{path}.condition", transform.condition or transform.expression or "")
    if transform.type == TransformType.DERIVE:
        for column, expression in transform.fields.items():
            _safe_expression(report, f"{path}.fields.{column}", expression)
    if transform.type == TransformType.AGGREGATE:
        for column, expression in transform.aggregations.items():
            _safe_expression(report, f"{path}.aggregations.{column}", expression)
    if transform.normalization and transform.normalization.expression:
        _safe_expression(report, f"{path}.normalization.expression", transform.normalization.expression)


def _validate_conditions(
    condition: ConditionSpec | None,
    report: ValidationReport,
    connections: dict[str, str] | None,
    known_recon_ids: set[str],
) -> None:
    if condition is None:
        return
    depth = _condition_depth(condition)
    if depth > 6:
        report.warn("conditions", f"Condition tree is {depth} levels deep - consider simplifying")
    for leaf in _walk_conditions(condition):
        cpath = f"conditions.{leaf.type.value if leaf.type else '?'}"
        if leaf.connection_ref and connections is not None and leaf.connection_ref not in connections:
            report.error(cpath, f"Condition references unknown connection '{leaf.connection_ref}'")
        if leaf.type in (ConditionType.JDBC_QUERY, ConditionType.CUSTOM_SQL) and leaf.query:
            _safe_sql(report, f"{cpath}.query", leaf.query)
        if (
            leaf.type == ConditionType.RECONCILIATION_SUCCEEDED
            and known_recon_ids
            and leaf.recon_id not in known_recon_ids
        ):
            report.error(cpath, f"Condition references unknown reconciliation '{leaf.recon_id}'")


def _condition_depth(condition: ConditionSpec, depth: int = 1) -> int:
    if not condition.is_composite:
        return depth
    return max((_condition_depth(c, depth + 1) for c in condition.conditions), default=depth)


def _validate_schedule(definition: ReconciliationDefinition, report: ValidationReport) -> None:
    schedule = definition.schedule
    if schedule.type == ScheduleType.MANUAL and definition.conditions:
        report.info(
            "schedule",
            "Conditions are configured but the schedule is manual - conditions are evaluated on manual runs too",
        )
    if schedule.type != ScheduleType.MANUAL and not schedule.enabled:
        report.warn("schedule", "Schedule is configured but disabled - the reconciliation will not run")
    if schedule.max_concurrent_runs > 1:
        report.warn(
            "schedule.maxConcurrentRuns",
            "Allowing concurrent runs weakens idempotency guarantees",
            hint="Keep 1 unless runs are partitioned by business date",
        )
    if schedule.timeout_minutes < 5:
        report.warn("schedule.timeoutMinutes", "Timeout below 5 minutes may cancel healthy Spark jobs")


def _validate_notifications(definition: ReconciliationDefinition, report: ValidationReport) -> None:
    email = definition.notifications.email
    if email.enabled and not email.recipients:
        report.warn("notifications.email", "Email notifications are enabled but no recipients are configured")


def _safe_sql(report: ValidationReport, path: str, sql: str) -> None:
    try:
        assert_read_only(sql, context=path)
    except Exception as exc:
        report.error(path, str(exc), hint="Only read-only SELECT/WITH statements are permitted")


def _safe_expression(report: ValidationReport, path: str, expression: str) -> None:
    try:
        assert_safe_expression(expression, context=path)
    except Exception as exc:
        report.error(path, str(exc))


def _safe_identifier(report: ValidationReport, path: str, name: str) -> None:
    try:
        assert_table_name(name, context=path)
    except Exception as exc:
        report.error(path, str(exc))
