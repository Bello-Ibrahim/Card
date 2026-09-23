"""Check Stage 3 output (script.md and shotlist.json per lesson).

Usage: python courseforge/check_script.py COURSE_ID [LESSON_ID ...]
       python courseforge/check_script.py --all
Formats: courseforge/STAGE3_FORMAT.md
"""

import json
import re
import sys

from check_content import sections
from check_curriculum import CATALOG, ROOT, slug_for

NARRATION = ["Hook", "Explain", "Demonstrate", "Recap", "CTA"]
SECTIONS = NARRATION + ["Thumbnail", "Production Notes"]
TYPES = {"presenter_full", "slide", "stock", "hero_broll", "screen", "text"}
LAYOUTS = {"title", "bullets", "diagram", "comparison", "quote", "code"}
WPM = 140


def words(text):
    return re.findall(r"[\w']+", text.lower())


def check_lesson(d, brief, lesson, demos):
    lid = lesson["lesson_id"]
    ldir = d / "lessons" / lid
    sp, jp = ldir / "script.md", ldir / "shotlist.json"
    if not sp.exists() or not jp.exists():
        return [f"{lid}: missing script.md or shotlist.json"]
    errs = []
    text = sp.read_text()
    if not text.startswith(f"# {lid} "):
        errs.append(f"{lid}: title must start with '# {lid} '")
    sec = sections(text)
    if list(sec) != SECTIONS:
        return errs + [f"{lid}: sections must be {SECTIONS}, got {list(sec)}"]
    narration = " ".join(sec[s].strip() for s in NARRATION)
    for s in NARRATION:
        body = sec[s]
        if re.search(r"^\s*([-*]|\d+\.)\s|`|\[(VERIFY|VERSION|REGION)\]|\*\*|\(|\)|https?://", body, re.M):
            errs.append(f"{lid}: {s} must be plain spoken text (no lists, code, tags, bold, brackets or links)")
    n = len(words(narration))
    target = brief.get("lesson_length_min", 5) * WPM
    if not 0.9 * target <= n <= 1.1 * target:
        errs.append(f"{lid}: narration {n} words (need {int(0.9 * target)}-{int(1.1 * target)})")
    hook_n = len(words(sec["Hook"]))
    if hook_n > 47:
        errs.append(f"{lid}: hook {hook_n} words (max about 47 for 20s)")
    head = re.search(r"Headline:\s*(.+)", sec["Thumbnail"])
    if not head or len(words(head.group(1))) > 5:
        errs.append(f"{lid}: Thumbnail needs 'Headline:' of 5 words or fewer")
    if not sec["Production Notes"].strip():
        errs.append(f"{lid}: Production Notes empty (write '- None.')")

    try:
        sl = json.loads(jp.read_text())
    except json.JSONDecodeError as e:
        return errs + [f"{lid}: shotlist invalid JSON {e}"]
    if sl.get("lesson_id") != lid or sl.get("course_id") != brief["course_id"]:
        errs.append(f"{lid}: shotlist ids mismatch")
    th = sl.get("thumbnail", {})
    if not th.get("headline") or len(words(th["headline"])) > 5 or "slide" not in th:
        errs.append(f"{lid}: thumbnail needs headline of 5 words or fewer and a slide")
    scenes = sl.get("scenes", [])
    if not scenes:
        return errs + [f"{lid}: no scenes"]
    t = 0.0
    hero = 0
    for i, s in enumerate(scenes, 1):
        tag = f"{lid}/scene {s.get('scene')}"
        if s.get("scene") != i:
            errs.append(f"{tag}: scenes must be numbered 1..n in order")
        vt = s.get("visual_type")
        if vt not in TYPES:
            errs.append(f"{tag}: bad visual_type {vt}")
        start, end = s.get("start"), s.get("end")
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            errs.append(f"{tag}: start/end must be numbers")
            continue
        if abs(start - t) > 0.05:
            errs.append(f"{tag}: starts at {start}, expected {t:.1f} (no gaps or overlaps)")
        dur = end - start
        if not 3 <= dur <= 30:
            errs.append(f"{tag}: duration {dur:.1f}s (need 3-30s)")
        vn = len(words(s.get("voiceover", "")))
        expected = vn * 60 / WPM
        if vn == 0:
            errs.append(f"{tag}: empty voiceover")
        elif abs(dur - expected) > max(2.0, 0.25 * expected):
            errs.append(f"{tag}: {dur:.1f}s for {vn} words (expected about {expected:.1f}s)")
        t = end
        ost = s.get("on_screen_text", "")
        if ost and len(words(ost)) > 8:
            errs.append(f"{tag}: on_screen_text over 8 words")
        if vt == "slide":
            sd = s.get("slide", {})
            if sd.get("layout") not in LAYOUTS or not sd.get("title") or not sd.get("body"):
                errs.append(f"{tag}: slide needs layout in {sorted(LAYOUTS)}, title and body")
        if vt == "stock" and not 3 <= len(words(s.get("stock_query", ""))) <= 8:
            errs.append(f"{tag}: stock needs stock_query of 3-8 words")
        if vt == "hero_broll":
            hero += 1
            p = s.get("broll_prompt", "")
            if s.get("broll_tool") not in ("FLOW", "KLING") or len(words(p)) < 15:
                errs.append(f"{tag}: hero_broll needs broll_tool FLOW|KLING and a full broll_prompt")
            if re.search(r"\blogos?\b(?![^.]*\bno\b)|\bbrand name", p, re.I) and "no " not in p.lower():
                errs.append(f"{tag}: broll_prompt must not ask for logos or brands")
        if vt == "screen":
            if lid not in demos:
                errs.append(f"{tag}: screen scene but {lid} is not in screen_demo_lessons")
            if not s.get("screen_steps"):
                errs.append(f"{tag}: screen needs screen_steps")
        if vt == "text" and not ost:
            errs.append(f"{tag}: text scene needs on_screen_text")
    if hero > 2:
        errs.append(f"{lid}: {hero} hero_broll scenes (max 2)")
    if scenes[0].get("visual_type") != "presenter_full" or scenes[-1].get("visual_type") != "presenter_full":
        errs.append(f"{lid}: first (hook) and last (CTA) scenes must be presenter_full")
    total = n * 60 / WPM
    if abs(sl.get("duration_s", 0) - t) > 0.05:
        errs.append(f"{lid}: duration_s {sl.get('duration_s')} != last scene end {t}")
    if abs(t - total) > 10:
        errs.append(f"{lid}: timeline {t:.0f}s vs narration {total:.0f}s (±10s)")
    vo = words(" ".join(s.get("voiceover", "") for s in scenes))
    if vo != words(narration):
        nw = words(narration)
        k = next((i for i, (a, b) in enumerate(zip(vo, nw)) if a != b), min(len(vo), len(nw)))
        errs.append(f"{lid}: scene voiceovers differ from script narration at word {k}: "
                    f"'{' '.join(vo[k:k + 6])}' vs '{' '.join(nw[k:k + 6])}'")
    return errs


def check_course(brief, wanted=None):
    d = ROOT / "courses" / slug_for(brief)
    c = json.loads((d / "curriculum.json").read_text())
    demos = set(c["screen_demo_lessons"])
    errs = []
    for m in c["modules"]:
        for lesson in m["lessons"]:
            if wanted and lesson["lesson_id"] not in wanted:
                continue
            errs += check_lesson(d, brief, lesson, demos)
    return errs


def main(args):
    briefs = {b["course_id"]: b for b in json.loads(CATALOG.read_text())}
    if args and args[0] == "--all":
        targets = [(b, None) for b in briefs.values()
                   if any((ROOT / "courses" / slug_for(b) / "lessons").glob("*/script.md"))]
    else:
        targets = [(briefs[args[0]], set(args[1:]) or None)]
    failed = 0
    for brief, wanted in targets:
        errs = check_course(brief, wanted)
        if errs:
            failed += 1
            print(f"FAIL {brief['course_id']} ({len(errs)} issues)")
            for e in errs:
                print(f"   - {e}")
        else:
            print(f"ok   {brief['course_id']}" + (f" {' '.join(sorted(wanted))}" if wanted else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
