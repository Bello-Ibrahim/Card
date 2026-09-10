#!/usr/bin/env python3
"""Static validation for the ReconX Helm chart.

`helm lint` and `helm template` are the authoritative checks and are what CI
should run.  This script catches the two mistakes that survive review most
often, without needing the helm binary:

1. a template referencing a value that does not exist in ``values.yaml``
   (``.Values.api.autoscaling.minReplcas``) - helm renders it as empty rather
   than failing, so the bug reaches the cluster;
2. unbalanced ``{{- if }}`` / ``{{- end }}`` blocks, or an ``include`` of a
   helper that was never defined.

Exit code 0 means the chart passed these checks.

    python scripts/validate_helm_chart.py [chart-directory]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

VALUE_REFERENCE = re.compile(r"\.Values\.([A-Za-z0-9_.]+)")
INCLUDE_REFERENCE = re.compile(r'include\s+"([^"]+)"')
DEFINE_HELPER = re.compile(r'define\s+"([^"]+)"')
BLOCK_OPEN = re.compile(r"\{\{-?\s*(if|range|with|define|block)\b")
BLOCK_END = re.compile(r"\{\{-?\s*end\s*-?\}\}")

#: Values supplied by the user at install time rather than defaulted in values.yaml.
OPTIONAL_PATHS = {
    "security.bootstrapAdminPassword",
    "image.registry",
}


def flatten(data: Any, prefix: str = "") -> set[str]:
    """Every dotted path present in values.yaml, including intermediate nodes."""
    paths: set[str] = set()
    if isinstance(data, dict):
        for key, value in data.items():
            path = f"{prefix}{key}"
            paths.add(path)
            paths |= flatten(value, f"{path}.")
    return paths


def check_chart(chart_dir: Path) -> list[str]:
    problems: list[str] = []

    chart_file = chart_dir / "Chart.yaml"
    values_file = chart_dir / "values.yaml"
    templates_dir = chart_dir / "templates"

    for required in (chart_file, values_file, templates_dir):
        if not required.exists():
            problems.append(f"missing {required.relative_to(chart_dir.parent)}")
    if problems:
        return problems

    chart = yaml.safe_load(chart_file.read_text())
    for field in ("apiVersion", "name", "version", "appVersion"):
        if not chart.get(field):
            problems.append(f"Chart.yaml: '{field}' is required")

    values = yaml.safe_load(values_file.read_text()) or {}
    known_paths = flatten(values)

    helpers: set[str] = set()
    for template in sorted(templates_dir.glob("*.tpl")):
        helpers |= set(DEFINE_HELPER.findall(template.read_text()))

    for template in sorted(templates_dir.iterdir()):
        if template.suffix not in (".yaml", ".tpl", ".txt"):
            continue
        content = template.read_text()
        name = template.name

        # 1. value references
        for reference in sorted(set(VALUE_REFERENCE.findall(content))):
            path = reference.rstrip(".")
            if path in OPTIONAL_PATHS or path in known_paths:
                continue
            # Allow indexing into a map whose keys are user supplied.
            if any(path.startswith(f"{known}.") for known in known_paths if _is_free_form(values, known)):
                continue
            problems.append(f"{name}: .Values.{path} is not defined in values.yaml")

        # 2. helper references
        for reference in sorted(set(INCLUDE_REFERENCE.findall(content))):
            if reference.startswith("reconx.") and reference not in helpers:
                problems.append(f"{name}: include \"{reference}\" has no matching define")

        # 3. block balance
        opens = len(BLOCK_OPEN.findall(content))
        ends = len(BLOCK_END.findall(content))
        if opens != ends:
            problems.append(f"{name}: {opens} block opener(s) but {ends} 'end' statement(s)")

    return problems


def _is_free_form(values: Any, path: str) -> bool:
    """True when a values node is a user-populated map (arbitrary keys below it)."""
    node: Any = values
    for part in path.split("."):
        if not isinstance(node, dict) or part not in node:
            return False
        node = node[part]
    return isinstance(node, dict) and not node


def main() -> int:
    chart_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "deployment/helm/reconx")
    problems = check_chart(chart_dir)
    template_count = len(list((chart_dir / "templates").glob("*"))) if (chart_dir / "templates").exists() else 0
    print(f"Validating {chart_dir} ({template_count} template file(s))")
    if problems:
        for problem in problems:
            print(f"  ERROR: {problem}")
        print(f"\n{len(problems)} problem(s) found")
        return 1
    print("  OK: value references, helper includes and block balance all check out")
    print("\nRun `helm lint` and `helm template` for the authoritative check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
