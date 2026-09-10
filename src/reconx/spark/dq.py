"""Data quality checks executed before reconciliation.

Checks run as Spark aggregations (one pass per source) and either stop the run
or let it continue with a warning, as configured per check.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from reconx.common.errors import DataQualityError
from reconx.common.logging import get_logger
from reconx.config.enums import DataQualityAction, DataQualityCheckType
from reconx.config.models import DataQualityCheck, SchemaSpec
from reconx.security.sql_guard import assert_safe_expression
from reconx.spark.schema import compare_schemas, normalise_type

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame

log = get_logger(__name__)


@dataclass
class DataQualityResult:
    check_id: str
    check_type: str
    passed: bool
    message: str
    action: str = DataQualityAction.STOP.value
    failed_records: int = 0
    total_records: int = 0
    details: dict[str, Any] = field(default_factory=dict)

    @property
    def blocking(self) -> bool:
        return not self.passed and self.action == DataQualityAction.STOP.value

    def to_dict(self) -> dict[str, Any]:
        return {
            "checkId": self.check_id,
            "checkType": self.check_type,
            "passed": self.passed,
            "message": self.message,
            "action": self.action,
            "failedRecords": self.failed_records,
            "totalRecords": self.total_records,
            "details": self.details,
        }


@dataclass
class DataQualityReport:
    source_id: str
    results: list[DataQualityResult] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(r.passed for r in self.results)

    @property
    def blocking_failures(self) -> list[DataQualityResult]:
        return [r for r in self.results if r.blocking]

    @property
    def warnings(self) -> list[DataQualityResult]:
        return [r for r in self.results if not r.passed and not r.blocking]

    def raise_if_blocking(self) -> None:
        blocking = self.blocking_failures
        if blocking:
            raise DataQualityError(
                f"Data quality failed for source '{self.source_id}': "
                + "; ".join(r.message for r in blocking),
                details={"sourceId": self.source_id, "failures": [r.to_dict() for r in blocking]},
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            "sourceId": self.source_id,
            "passed": self.passed,
            "results": [r.to_dict() for r in self.results],
        }


class DataQualityRunner:
    """Executes the configured checks against a source DataFrame."""

    def run(
        self,
        dataframe: DataFrame,
        checks: list[DataQualityCheck],
        *,
        source_id: str,
        schema_spec: SchemaSpec | None = None,
    ) -> DataQualityReport:
        report = DataQualityReport(source_id=source_id)
        if not checks:
            return report

        from pyspark.sql import functions as F

        # Row count is needed by nearly every ratio-based check; compute once.
        total = dataframe.count()

        aggregations: list[Any] = []
        aliases: list[tuple[str, DataQualityCheck, str]] = []
        deferred: list[DataQualityCheck] = []

        for index, check in enumerate(checks):
            check_id = check.id or f"{check.type.value}_{index}"
            if check.type == DataQualityCheckType.NOT_NULL:
                for column in check.columns:
                    alias = f"nn_{index}_{column}"
                    if column not in dataframe.columns:
                        continue
                    aggregations.append(
                        F.sum(F.when(F.col(column).isNull(), F.lit(1)).otherwise(F.lit(0))).alias(alias)
                    )
                    aliases.append((alias, check, column))
            elif check.type == DataQualityCheckType.RANGE:
                for column in check.columns:
                    if column not in dataframe.columns:
                        continue
                    alias = f"rng_{index}_{column}"
                    condition = F.lit(False)
                    if check.min_value is not None:
                        condition = condition | (F.col(column).cast("double") < F.lit(check.min_value))
                    if check.max_value is not None:
                        condition = condition | (F.col(column).cast("double") > F.lit(check.max_value))
                    aggregations.append(
                        F.sum(F.when(condition, F.lit(1)).otherwise(F.lit(0))).alias(alias)
                    )
                    aliases.append((alias, check, column))
            elif check.type == DataQualityCheckType.REGEX:
                for column in check.columns:
                    if column not in dataframe.columns:
                        continue
                    alias = f"rgx_{index}_{column}"
                    aggregations.append(
                        F.sum(
                            F.when(
                                F.col(column).isNotNull()
                                & ~F.col(column).cast("string").rlike(check.pattern or ".*"),
                                F.lit(1),
                            ).otherwise(F.lit(0))
                        ).alias(alias)
                    )
                    aliases.append((alias, check, column))
            elif check.type == DataQualityCheckType.DATE_VALID:
                for column in check.columns:
                    if column not in dataframe.columns:
                        continue
                    alias = f"dt_{index}_{column}"
                    parsed = (
                        F.to_timestamp(F.col(column).cast("string"), check.date_format)
                        if check.date_format
                        else F.col(column).cast("timestamp")
                    )
                    aggregations.append(
                        F.sum(
                            F.when(F.col(column).isNotNull() & parsed.isNull(), F.lit(1)).otherwise(F.lit(0))
                        ).alias(alias)
                    )
                    aliases.append((alias, check, column))
            elif check.type == DataQualityCheckType.CUSTOM_SQL:
                assert_safe_expression(check.sql or "", context=f"dq.{check_id}")
                alias = f"sql_{index}"
                aggregations.append(
                    F.sum(F.when(~F.expr(check.sql or "true"), F.lit(1)).otherwise(F.lit(0))).alias(alias)
                )
                aliases.append((alias, check, "*"))
            else:
                deferred.append(check)

        row: dict[str, Any] = {}
        if aggregations:
            row = dataframe.agg(*aggregations).collect()[0].asDict()

        grouped: dict[int, list[tuple[str, int]]] = {}
        for alias, check, column in aliases:
            grouped.setdefault(id(check), []).append((column, int(row.get(alias) or 0)))

        for index, check in enumerate(checks):
            check_id = check.id or f"{check.type.value}_{index}"
            if id(check) in grouped:
                failures = grouped[id(check)]
                failed = sum(count for _, count in failures)
                offending = {column: count for column, count in failures if count}
                passed = _within_threshold(failed, total, check.threshold)
                report.results.append(
                    DataQualityResult(
                        check_id=check_id,
                        check_type=check.type.value,
                        passed=passed,
                        action=check.on_failure.value,
                        failed_records=failed,
                        total_records=total,
                        message=(
                            f"{check.type.value}: {failed:,} of {total:,} record(s) failed"
                            + (f" ({offending})" if offending else "")
                            if failed
                            else f"{check.type.value}: passed on {total:,} record(s)"
                        ),
                        details={"columns": offending},
                    )
                )
                continue
            if check in deferred:
                report.results.append(self._run_deferred(dataframe, check, check_id, total, schema_spec))

        for result in report.results:
            log.info(
                "dq.check",
                source=source_id,
                check=result.check_id,
                passed=result.passed,
                failed_records=result.failed_records,
            )
        return report

    def _run_deferred(
        self,
        dataframe: DataFrame,
        check: DataQualityCheck,
        check_id: str,
        total: int,
        schema_spec: SchemaSpec | None,
    ) -> DataQualityResult:

        kind = check.type
        if kind == DataQualityCheckType.ROW_COUNT:
            below = check.min_rows is not None and total < check.min_rows
            above = check.max_rows is not None and total > check.max_rows
            passed = not (below or above)
            bounds = f"min={check.min_rows}, max={check.max_rows}"
            return DataQualityResult(
                check_id=check_id,
                check_type=kind.value,
                passed=passed,
                action=check.on_failure.value,
                total_records=total,
                message=(
                    f"row_count: {total:,} record(s) "
                    + ("within" if passed else "outside")
                    + f" configured bounds ({bounds})"
                ),
                details={"minRows": check.min_rows, "maxRows": check.max_rows},
            )

        if kind == DataQualityCheckType.COLUMN_EXISTS:
            missing = [c for c in check.columns if c not in dataframe.columns]
            return DataQualityResult(
                check_id=check_id,
                check_type=kind.value,
                passed=not missing,
                action=check.on_failure.value,
                total_records=total,
                message=(
                    f"column_exists: missing {missing}" if missing else "column_exists: all columns present"
                ),
                details={"missing": missing, "available": dataframe.columns},
            )

        if kind == DataQualityCheckType.UNIQUE:
            distinct = dataframe.select(*check.columns).distinct().count()
            duplicates = total - distinct
            passed = _within_threshold(duplicates, total, check.threshold)
            return DataQualityResult(
                check_id=check_id,
                check_type=kind.value,
                passed=passed,
                action=check.on_failure.value,
                failed_records=duplicates,
                total_records=total,
                message=(
                    f"unique: {duplicates:,} duplicate record(s) on {check.columns}"
                    if duplicates
                    else f"unique: no duplicates on {check.columns}"
                ),
                details={"columns": check.columns, "distinct": distinct},
            )

        if kind == DataQualityCheckType.DATA_TYPE:
            actual = {f.name: f.dataType.simpleString() for f in dataframe.schema.fields}
            expected = normalise_type(check.expected_type or "string")
            mismatches = {
                column: actual.get(column)
                for column in check.columns
                if column in actual and actual[column] != expected
            }
            return DataQualityResult(
                check_id=check_id,
                check_type=kind.value,
                passed=not mismatches,
                action=check.on_failure.value,
                total_records=total,
                message=(
                    f"data_type: {mismatches} do not match expected '{expected}'"
                    if mismatches
                    else f"data_type: all columns are '{expected}'"
                ),
                details={"mismatches": mismatches},
            )

        if kind == DataQualityCheckType.SCHEMA:
            if schema_spec is None or not schema_spec.fields:
                return DataQualityResult(
                    check_id=check_id,
                    check_type=kind.value,
                    passed=True,
                    action=check.on_failure.value,
                    total_records=total,
                    message="schema: no declared schema to validate against - skipped",
                )
            comparison = compare_schemas(schema_spec, dataframe)
            return DataQualityResult(
                check_id=check_id,
                check_type=kind.value,
                passed=bool(comparison["compatible"]),
                action=check.on_failure.value,
                total_records=total,
                message=(
                    "schema: matches the declared schema"
                    if comparison["compatible"]
                    else f"schema: missing={comparison['missing']} typeMismatches={comparison['typeMismatches']}"
                ),
                details=comparison,
            )

        return DataQualityResult(  # pragma: no cover - enum exhaustive
            check_id=check_id,
            check_type=kind.value,
            passed=True,
            action=check.on_failure.value,
            total_records=total,
            message=f"{kind.value}: not implemented - skipped",
        )


def _within_threshold(failed: int, total: int, threshold: float | None) -> bool:
    if failed == 0:
        return True
    if threshold is None:
        return False
    if threshold <= 1:  # ratio
        return (failed / total if total else 0) <= threshold
    return failed <= threshold
