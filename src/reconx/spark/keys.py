"""Reconciliation key construction.

A reconciliation key is a *normalised* concatenation of one or more columns.
Normalisation is what makes real-world data reconcile: ``'  001 '`` on one
side and ``'1'`` on the other are the same customer once trim + leading-zero
handling is applied.

The generated key columns are added under the reserved ``__reconx`` prefix so
they can never collide with business columns.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from reconx.common.errors import ReconciliationError
from reconx.common.logging import get_logger
from reconx.config.models import KeyMapping, MatchingOptions, Normalization
from reconx.spark.transforms import normalise_column

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame
    from pyspark.sql.column import Column

log = get_logger(__name__)

KEY_COLUMN = "__reconx_key"
KEY_PART_PREFIX = "__reconx_key_"
#: Sentinel used so a NULL key component never collides with an empty string.
NULL_TOKEN = "<NULL>"  # noqa: S105 - a NULL sentinel, not a credential


def default_normalization(options: MatchingOptions) -> Normalization:
    """Leg-level defaults applied when a key component defines none of its own."""
    return Normalization(
        trim=options.trim_keys,
        case="upper" if options.case_insensitive_keys else "none",
        null_as="" if options.null_equals_null else None,
    )


def key_part_column(
    dataframe: DataFrame,
    column_name: str,
    normalization: Normalization | None,
    *,
    side: str,
) -> Column:
    from pyspark.sql import functions as F

    if column_name not in dataframe.columns:
        raise ReconciliationError(
            f"{side} side has no key column '{column_name}'",
            details={"available": dataframe.columns, "side": side},
        )
    normalised = normalise_column(F.col(column_name), normalization)
    # NULLs must stay distinguishable from empty strings unless the
    # configuration explicitly maps them together via ``null_as``.
    if normalization is None or normalization.null_as is None:
        return F.coalesce(normalised.cast("string"), F.lit(NULL_TOKEN))
    return normalised.cast("string")


def add_reconciliation_key(
    dataframe: DataFrame,
    keys: list[KeyMapping],
    *,
    side: str,
    options: MatchingOptions,
    keep_parts: bool = True,
) -> DataFrame:
    """Add ``__reconx_key`` (and per-component columns) to one side of a leg."""
    from pyspark.sql import functions as F

    if not keys:
        raise ReconciliationError("At least one key mapping is required to build a reconciliation key")

    defaults = default_normalization(options)
    result = dataframe
    part_columns: list[str] = []
    for index, mapping in enumerate(keys):
        source_column = mapping.left if side == "left" else mapping.right
        alias = f"{KEY_PART_PREFIX}{index}"
        normalization = mapping.normalization or defaults
        result = result.withColumn(
            alias, key_part_column(result, source_column or "", normalization, side=side)
        )
        part_columns.append(alias)

    separator = options.key_separator or "|"
    result = result.withColumn(KEY_COLUMN, F.concat_ws(separator, *[F.col(c) for c in part_columns]))
    if not keep_parts:
        result = result.drop(*part_columns)
    log.debug("keys.generated", side=side, components=len(keys), separator=separator)
    return result


def key_component_aliases(keys: list[KeyMapping]) -> dict[str, str]:
    """Map generated part columns to their business alias for reporting."""
    return {f"{KEY_PART_PREFIX}{index}": mapping.key_alias for index, mapping in enumerate(keys)}


def describe_key(keys: list[KeyMapping], options: MatchingOptions) -> str:
    """Readable description shown in the UI, e.g. ``TRIM(UPPER(customer_id)) | transaction_id``."""
    parts: list[str] = []
    defaults = default_normalization(options)
    for mapping in keys:
        rules = mapping.normalization or defaults
        expression = mapping.left or "?"
        if rules.trim:
            expression = f"TRIM({expression})"
        if rules.case == "upper":
            expression = f"UPPER({expression})"
        elif rules.case == "lower":
            expression = f"LOWER({expression})"
        if rules.strip_leading_zeros:
            expression = f"STRIP_ZEROS({expression})"
        if rules.pad_left:
            expression = f"LPAD({expression},{rules.pad_left},'{rules.pad_character}')"
        if rules.date_format:
            expression = f"DATE_FORMAT({expression},'{rules.date_format}')"
        if rules.numeric_scale is not None:
            expression = f"ROUND({expression},{rules.numeric_scale})"
        parts.append(expression)
    return f" {options.key_separator or '|'} ".join(parts)
