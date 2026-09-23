"""Check Stage 2 output (lesson content, module quizzes, capstone rubric).

Usage: python courseforge/check_content.py [course_id ...]
With no arguments, checks every course that has a lessons/ folder.
Formats: courseforge/STAGE2_FORMAT.md
"""

import json
import re
import sys

from check_curriculum import CATALOG, ROOT, slug_for

SECTIONS = ["Hook", "Explanation", "Worked Example", "Common Mistake",
            "Key Takeaways", "Hands-on Exercise", "Review Flags"]
EXERCISE_FIELDS = ["**Task:**", "**Tools:**", "**Steps:**", "**What good looks like:**", "**Time:**"]
TAG = re.compile(r"\[(VERIFY|VERSION|REGION)\]")


def sections(text):
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def check_lesson(path, lesson):
    lid = lesson["lesson_id"]
    if not path.exists():
        return [f"{lid}: missing content.md"]
    text = path.read_text()
    errs = []
    if not text.startswith(f"# {lid} "):
        errs.append(f"{lid}: title line must start with '# {lid} '")
    sec = sections(text)
    if list(sec) != SECTIONS:
        return errs + [f"{lid}: sections must be exactly {SECTIONS}, got {list(sec)}"]
    words = len(re.findall(r"\w+", text))
    if not 450 <= words <= 1100:
        errs.append(f"{lid}: {words} words (need 450-1100)")
    if "**Analogy:**" not in sec["Explanation"]:
        errs.append(f"{lid}: Explanation needs an **Analogy:** paragraph")
    takeaways = re.findall(r"^\d+\. ", sec["Key Takeaways"], flags=re.M)
    if len(takeaways) != 3:
        errs.append(f"{lid}: {len(takeaways)} key takeaways (need 3)")
    missing = [f for f in EXERCISE_FIELDS if f not in sec["Hands-on Exercise"]]
    if missing:
        errs.append(f"{lid}: exercise missing {missing}")
    body_tags = set(TAG.findall(text.split("## Review Flags")[0]))
    flag_tags = set(TAG.findall(sec["Review Flags"]))
    if body_tags - flag_tags:
        errs.append(f"{lid}: tags {sorted(body_tags - flag_tags)} used in body but not listed in Review Flags")
    if not sec["Review Flags"].strip():
        errs.append(f"{lid}: Review Flags empty (write '- None.')")
    return errs


def check_quiz(path, module, objective_ids):
    mid = module["module_id"]
    if not path.exists():
        return [f"{mid}: missing quiz.json"]
    try:
        q = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        return [f"{mid}: invalid JSON {e}"]
    errs = []
    qs = q.get("questions", [])
    if q.get("module_id") != mid:
        errs.append(f"{mid}: module_id mismatch")
    if len(qs) != 5:
        errs.append(f"{mid}: {len(qs)} questions (need 5)")
    lesson_ids = {lesson["lesson_id"] for lesson in module["lessons"]}
    for item in qs:
        qid = f"{mid}/{item.get('id')}"
        opts = item.get("options", [])
        if len(opts) != 4 or len(set(opts)) != 4:
            errs.append(f"{qid}: need 4 distinct options")
        if item.get("answer_index") not in range(4):
            errs.append(f"{qid}: answer_index must be 0-3")
        if not item.get("question") or not item.get("explanation"):
            errs.append(f"{qid}: question and explanation required")
        if item.get("lesson_id") not in lesson_ids:
            errs.append(f"{qid}: lesson_id not in module")
        if item.get("objective") not in objective_ids:
            errs.append(f"{qid}: unknown objective")
    answers = [item.get("answer_index") for item in qs]
    if qs and max(answers.count(a) for a in set(answers)) > 2:
        errs.append(f"{mid}: correct answers bunched in one position {answers}")
    if untested := lesson_ids - {item.get("lesson_id") for item in qs}:
        errs.append(f"{mid}: lessons not tested {sorted(untested)}")
    return errs


def check_rubric(path, c):
    if not path.exists():
        return ["missing capstone_rubric.md"]
    text = path.read_text()
    errs = []
    sec = sections(text)
    for h in ["Task", "Deliverables", "Criteria", "Submission Checklist"]:
        if h not in sec:
            errs.append(f"rubric missing section {h}")
    rows = [r for r in re.findall(r"^\|(.+)\|\s*$", sec.get("Criteria", ""), flags=re.M)
            if not re.match(r"\s*-", r) and "Criterion" not in r]
    if not 4 <= len(rows) <= 6:
        errs.append(f"rubric has {len(rows)} criteria (need 4-6)")
    points = []
    for r in rows:
        cells = [x.strip() for x in r.split("|")]
        if len(cells) != 7 or not cells[-1].isdigit():
            errs.append(f"rubric row needs 7 cells ending in points: {cells[0][:40]}")
        else:
            points.append(int(cells[-1]))
    if points and sum(points) != 100:
        errs.append(f"rubric points total {sum(points)} (need 100)")
    if "Total: 100" not in text:
        errs.append("rubric needs 'Total: 100'")
    assessed = set(c["capstone"].get("assesses", []))
    cited = set(re.findall(r"\bO\d+\b", sec.get("Criteria", "")))
    if assessed - cited:
        errs.append(f"rubric does not cite capstone objectives {sorted(assessed - cited)}")
    return errs


def check(brief):
    d = ROOT / "courses" / slug_for(brief)
    c = json.loads((d / "curriculum.json").read_text())
    objective_ids = {o["id"] for o in c["objectives"]}
    errs = []
    for m in c["modules"]:
        for lesson in m["lessons"]:
            errs += check_lesson(d / "lessons" / lesson["lesson_id"] / "content.md", lesson)
        errs += check_quiz(d / "modules" / m["module_id"] / "quiz.json", m, objective_ids)
    errs += check_rubric(d / "capstone_rubric.md", c)
    return errs


def main(wanted):
    failed = 0
    for brief in json.loads(CATALOG.read_text()):
        d = ROOT / "courses" / slug_for(brief)
        if wanted and brief["course_id"] not in wanted:
            continue
        if not wanted and not (d / "lessons").exists():
            continue
        errs = check(brief)
        if errs:
            failed += 1
            print(f"FAIL {brief['course_id']} ({len(errs)} issues)")
            for e in errs:
                print(f"   - {e}")
        else:
            print(f"ok   {brief['course_id']}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
