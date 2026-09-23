"""Check Stage 1 curricula against their briefs.

Usage: python courseforge/check_curriculum.py [course_id ...]
With no arguments, checks every course in the catalog that has a curriculum.json.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CATALOG = ROOT / "briefs" / "certifai_catalog.json"
BLOOM = ["Remember", "Understand", "Apply", "Analyse", "Evaluate", "Create"]


def slug_for(brief):
    title = re.sub(r"[^a-z0-9]+", "-", brief["course_title"].lower()).strip("-")
    return f"{brief['course_id'].lower()}-{title}"


def check(brief):
    path = ROOT / "courses" / slug_for(brief) / "curriculum.json"
    if not path.exists():
        return None, [f"missing {path.relative_to(ROOT)}"]
    errs = []
    try:
        c = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        return path, [f"invalid JSON: {e}"]
    for key in ["course_id", "slug", "course_title", "level", "status", "overview", "time_plan",
                "objectives", "modules", "capstone", "coverage_check", "screen_demo_lessons", "flags"]:
        if key not in c:
            errs.append(f"missing key {key}")
    if errs:
        return path, errs
    if c["course_id"] != brief["course_id"] or c["slug"] != slug_for(brief):
        errs.append("course_id/slug mismatch")
    if c["course_title"] != brief["course_title"] or c["level"] != brief["level"]:
        errs.append("course_title/level differ from brief")
    objs = c["objectives"]
    if not 5 <= len(objs) <= 7:
        errs.append(f"{len(objs)} objectives (need 5-7)")
    if any(o.get("bloom") not in BLOOM for o in objs):
        errs.append(f"bloom level must be one of {BLOOM}")
    obj_ids = {o["id"] for o in objs}
    lessons = [lesson for m in c["modules"] for lesson in m["lessons"]]
    if len(lessons) != brief["target_lessons"]:
        errs.append(f"{len(lessons)} lessons, brief wants {brief['target_lessons']}")
    ids = [lesson["lesson_id"] for lesson in lessons]
    if ids != [f"L{i:02d}" for i in range(1, len(ids) + 1)]:
        errs.append("lesson_ids must run L01, L02, ... in order")
    cov = {}
    for lesson in lessons:
        for key in ["title", "objectives", "summary", "exercise"]:
            if not lesson.get(key):
                errs.append(f"{lesson.get('lesson_id')} missing {key}")
        for o in lesson.get("objectives", []):
            if o not in obj_ids:
                errs.append(f"{lesson['lesson_id']} references unknown objective {o}")
            cov.setdefault(o, []).append(lesson["lesson_id"])
    if uncovered := obj_ids - set(cov):
        errs.append(f"objectives not covered by any lesson: {sorted(uncovered)}")
    if cov != c["coverage_check"]:
        errs.append("coverage_check does not match lesson objectives")
    if bad := set(c["screen_demo_lessons"]) - set(ids):
        errs.append(f"screen_demo_lessons not in curriculum: {sorted(bad)}")
    if bad := set(c["capstone"].get("built_in", [])) - set(ids):
        errs.append(f"capstone built_in lessons not in curriculum: {sorted(bad)}")
    return path, errs


def main(wanted):
    briefs = json.loads(CATALOG.read_text())
    if wanted:
        briefs = [b for b in briefs if b["course_id"] in wanted]
    failed = 0
    for brief in briefs:
        path, errs = check(brief)
        if path is None and not wanted:
            continue
        if errs:
            failed += 1
            print(f"FAIL {brief['course_id']}: " + "; ".join(errs))
        else:
            print(f"ok   {brief['course_id']}  {brief['target_lessons']} lessons")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
