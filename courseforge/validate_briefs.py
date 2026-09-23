"""Validate CourseForge briefs and estimate variable Claude spend.

Usage: python courseforge/validate_briefs.py courseforge/briefs/certifai_catalog.json
Accepts a single brief object or a list of briefs. Exits 1 if any brief is invalid.
"""

import json
import sys
from pathlib import Path

import jsonschema

SCHEMA = json.loads((Path(__file__).parent / "course_brief.schema.json").read_text())

# Claude Sonnet 5 via the Batch API (50% off $2 / $10 per million tokens).
IN_PER_TOKEN = 1.00 / 1_000_000
OUT_PER_TOKEN = 5.00 / 1_000_000

# Rough token budgets; the agent recalculates from real counts before each stage.
CURRICULUM = (3_000, 5_000)  # per course
LESSON = (8_000, 8_000)  # content + script + shot list + slide HTML, per lesson
QUIZ = (4_000, 3_000)  # per module (~4 lessons)
SRT_TRANSLATION = (3_000, 4_000)  # per lesson per non-English language
RETRY_HEADROOM = 1.5
DEFAULT_LESSONS = 12  # used when a brief has no target_lessons

RTL_LANGUAGES = {"ar", "fa", "he", "ur"}


def cost(tokens, times=1):
    return times * (tokens[0] * IN_PER_TOKEN + tokens[1] * OUT_PER_TOKEN)


def estimate(brief):
    lessons = brief.get("target_lessons", DEFAULT_LESSONS)
    modules = max(1, round(lessons / 4))
    langs = len([lang for lang in brief["languages"] if lang != "en"])
    base = (
        cost(CURRICULUM)
        + cost(LESSON, lessons)
        + cost(QUIZ, modules)
        + cost(SRT_TRANSLATION, lessons * langs)
    )
    return base * RETRY_HEADROOM


def warnings(brief):
    out = []
    p = brief["presenter"]
    if not p.get("avatar_id") or not p.get("voice_id"):
        out.append("presenter avatar_id/voice_id empty: Stage 4 HeyGen pack is blocked until set")
    if RTL_LANGUAGES & set(brief["languages"]):
        out.append("RTL language: captions need an Arabic-capable font (Inter has no Arabic glyphs)")
    if not brief["brand"].get("logo_url"):
        out.append("no logo_url: intro/outro use a text wordmark")
    return out


def main(path):
    data = json.loads(Path(path).read_text())
    briefs = data if isinstance(data, list) else [data]
    ids = [b.get("course_id") for b in briefs]
    dupes = {i for i in ids if i and ids.count(i) > 1}
    failed = 0
    total_cost = total_lessons = 0
    for brief in briefs:
        label = brief.get("course_id") or brief.get("course_title", "?")
        errors = sorted(jsonschema.Draft202012Validator(SCHEMA).iter_errors(brief), key=str)
        if label in dupes:
            errors.append(f"duplicate course_id {label}")
        if errors:
            failed += 1
            print(f"FAIL {label}")
            for e in errors:
                print(f"   - {getattr(e, 'message', e)}")
            continue
        est = estimate(brief)
        total_cost += est
        total_lessons += brief.get("target_lessons", DEFAULT_LESSONS)
        flag = "OVER 80%" if est > 0.8 * brief["budget_limit_usd"] else "ok"
        print(f"ok   {label}  lessons={brief.get('target_lessons', DEFAULT_LESSONS):>2}  "
              f"est=${est:.2f} / budget ${brief['budget_limit_usd']}  [{flag}]")
    common = {}
    for brief in briefs:
        for w in warnings(brief):
            common.setdefault(w, []).append(brief.get("course_id", "?"))
    print(f"\n{len(briefs) - failed}/{len(briefs)} valid, {total_lessons} lessons, "
          f"estimated variable Claude spend ${total_cost:.2f}")
    for w, who in common.items():
        scope = "all courses" if len(who) == len(briefs) else ", ".join(who)
        print(f"WARN ({scope}): {w}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "courseforge/examples/course_brief.example.json"))
