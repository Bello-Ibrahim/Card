"""Build script.md and shotlist.json for a lesson from its stage3_plan.json.

Usage: python courseforge/build_stage3.py COURSE_ID LESSON_ID [LESSON_ID ...]

The plan is the single source: each narration section (Hook, Explain, Demonstrate,
Recap, CTA) is a list of scenes, each with its "voiceover" and visual fields
(see STAGE3_FORMAT.md). Timings come from word counts at 140 words per minute,
so the script, the shot list and the timeline always agree.

stage3_plan.json:
{
  "title": "What Is AI, Really?",
  "thumbnail": {"headline": "...", "image": "...", "slide": {"layout": "title", "title": "...", "body": "..."}},
  "production_notes": ["..."],
  "sections": {"Hook": [scene, ...], "Explain": [...], "Demonstrate": [...], "Recap": [...], "CTA": [...]}
}
"""

import json
import sys

from check_curriculum import CATALOG, ROOT, slug_for
from check_script import NARRATION, WPM, words


def build(brief, lid):
    d = ROOT / "courses" / slug_for(brief) / "lessons" / lid
    plan = json.loads((d / "stage3_plan.json").read_text())
    t = 0.0
    scenes, parts = [], {}
    for sec in NARRATION:
        paras = []
        for s in plan["sections"][sec]:
            vo = " ".join(s["voiceover"].split())
            dur = round(len(words(vo)) * 60 / WPM, 1)
            scene = {"scene": len(scenes) + 1, "start": round(t, 1), "end": round(t + dur, 1), "section": sec}
            scene.update({k: v for k, v in s.items() if k != "voiceover"})
            scene["voiceover"] = vo
            scenes.append(scene)
            t = round(t + dur, 1)
            paras.append(vo)
        parts[sec] = "\n\n".join(paras)
    n = sum(len(words(p)) for p in parts.values())
    th = plan["thumbnail"]
    notes = plan.get("production_notes") or ["None."]
    md = [f"# {lid} {plan['title']} | Presenter Script", "",
          f"Course: {brief['course_id']} · Video: {brief.get('lesson_length_min', 5)} min · Words: {n}", ""]
    for sec in NARRATION:
        md += [f"## {sec}", parts[sec], ""]
    md += ["## Thumbnail", f"Headline: {th['headline']}", f"Image: {th['image']}", "",
           "## Production Notes"] + [f"- {x}" for x in notes] + [""]
    (d / "script.md").write_text("\n".join(md))
    shot = {"course_id": brief["course_id"], "lesson_id": lid, "duration_s": t,
            "thumbnail": {"headline": th["headline"], "slide": th["slide"]}, "scenes": scenes}
    (d / "shotlist.json").write_text(json.dumps(shot, indent=2, ensure_ascii=False) + "\n")
    return n, t, len(scenes)


def main(args):
    briefs = {b["course_id"]: b for b in json.loads(CATALOG.read_text())}
    brief = briefs[args[0]]
    for lid in args[1:]:
        n, t, k = build(brief, lid)
        print(f"{brief['course_id']} {lid}: {n} words, {t:.0f}s, {k} scenes")


if __name__ == "__main__":
    main(sys.argv[1:])
