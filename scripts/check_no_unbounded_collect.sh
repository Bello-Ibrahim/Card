#!/usr/bin/env bash
# Reconciliation data must never be materialised on the driver.
#
# A `.collect()` is allowed only when the same line shows the bound - it is an
# aggregate (`agg(...)`), it is limited (`limit(...)`), or it carries an
# explicit `# bounded: <why>` marker. `toPandas()` is never allowed on a
# reconciliation DataFrame: it is always a full materialisation.
set -euo pipefail

target="${1:-src/reconx/spark}"
status=0

if offenders=$(grep -rnE '\.collect\(\)' "$target" --include='*.py' \
                | grep -vE '(agg\(|limit\(|# bounded)'); then
  echo "Unbounded collect() found - aggregate in Spark, limit the result, or"
  echo "annotate the bound with '# bounded: <why>':"
  echo "$offenders"
  status=1
fi

if offenders=$(grep -rnE '\.toPandas\(\)' "$target" --include='*.py' \
                | grep -vE '# bounded'); then
  echo "toPandas() materialises the whole DataFrame on the driver:"
  echo "$offenders"
  status=1
fi

exit "$status"
