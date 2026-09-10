"""Reserved column names used by the reconciliation engine.

Everything the engine adds is prefixed with ``__reconx`` (or the side prefixes)
so it can never collide with a business column, and the public result columns
are renamed to friendly names right before the outputs are written.
"""

from __future__ import annotations

LEFT_PREFIX = "l__"
RIGHT_PREFIX = "r__"

MATCH_COLUMN = "__reconx_match"
CATEGORY_COLUMN = "__reconx_category"
LEFT_PRESENT_COLUMN = "__reconx_left_present"
RIGHT_PRESENT_COLUMN = "__reconx_right_present"
LEFT_DUP_COLUMN = "__reconx_left_dup_count"
RIGHT_DUP_COLUMN = "__reconx_right_dup_count"
RULE_COLUMN_PREFIX = "__reconx_rule_"
FIELD_COLUMN_PREFIX = "__reconx_field_"
MISMATCHED_FIELDS_COLUMN = "__reconx_mismatched_fields"
MATCHED_RULES_COLUMN = "__reconx_matched_rules"
FAILED_RULES_COLUMN = "__reconx_failed_rules"

#: Friendly names used in persisted results.
PUBLIC_RENAMES: dict[str, str] = {
    "__reconx_key": "recon_key",
    CATEGORY_COLUMN: "match_category",
    MISMATCHED_FIELDS_COLUMN: "mismatched_fields",
    MATCHED_RULES_COLUMN: "matched_rules",
    FAILED_RULES_COLUMN: "failed_rules",
    LEFT_DUP_COLUMN: "left_duplicate_count",
    RIGHT_DUP_COLUMN: "right_duplicate_count",
}

INTERNAL_PREFIXES = ("__reconx",)


def is_internal(column: str) -> bool:
    return column.startswith(INTERNAL_PREFIXES)
