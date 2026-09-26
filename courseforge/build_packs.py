"""Stage 4: build the manual production packs and per-lesson asset tracking for a course.

Usage: python courseforge/build_packs.py COURSE_ID [--start YYYY-MM-DD]

Writes courses/{slug}/packs/:
  README.md            what to produce, where to upload it, and the filename rules
  heygen_{Mx}.md       HeyGen Batch Pack per module (paste-ready scripts, exact settings)
  broll_{date}.md      hero B-roll prompts, at most 8 clips per day
  screen_{Lxx}.md      OBS Screen Demo Pack per demo lesson
  stock_queries.csv    stock searches for the stock_search step (Pexels/Pixabay)
and lessons/{Lxx}/assets.json (every scene's asset, file and status).
Run render_slides.py first so slide and thumbnail PNGs exist.
"""

import csv
import datetime as dt
import json
import math
import sys

from check_curriculum import CATALOG, ROOT, slug_for

MAX_BROLL_PER_DAY = 8
GREEN = "#00FF00"


def heygen_settings(brief):
    p = brief["presenter"]
    voice = (f"`{p['voice_id']}`" + (" (the same ID as the avatar: if HeyGen does not list it as a voice, use "
             f"{p.get('avatar_name', 'the avatar')}'s paired English voice and record its ID in DECISIONS.md)"
             if p['voice_id'] == p.get('avatar_id') else "") if p.get("voice_id") else
             f"{p.get('avatar_name', 'the avatar')}'s paired English voice. Use the same voice for every lesson, "
             "and record its voice ID in DECISIONS.md and the catalogue after the first render")
    return "\n".join([
        "| Setting | Value |", "|---|---|",
        f"| Avatar | **{p.get('avatar_name', '')}** (standard avatar), ID `{p['avatar_id']}` |",
        f"| Voice | {voice} |",
        f"| Background | Solid colour **{GREEN}** (pure green, no gradient, no image) |",
        "| Resolution | 1080p (1920×1080) |", "| Aspect ratio | 16:9 |",
        "| Avatar framing | Centred, head and shoulders, same size in every lesson |",
        "| Captions/subtitles | **Off** (captions are added in Stage 6) |",
        "| Music | Off |",
        "| Speed | Normal (1.0×) |",
    ])


def pron_notes(script_md):
    notes = script_md.split("## Production Notes", 1)[-1]
    return [n.strip("- ").strip() for n in notes.splitlines()
            if any(k in n.lower() for k in ("pronounc", "pronunciation", "say "))]


def build(brief, start):
    slug = slug_for(brief)
    d = ROOT / "courses" / slug
    c = json.loads((d / "curriculum.json").read_text())
    packs = d / "packs"
    packs.mkdir(exist_ok=True)
    demos = set(c["screen_demo_lessons"])
    stock_rows, broll, uploads = [], [], []
    written = []
    for m in c["modules"]:
        mid = m["module_id"]
        md = [f"# HeyGen Batch Pack: {brief['course_id']} {mid} ({m['title']})", "",
              f"Course: {brief['course_title']}. Make one HeyGen video per lesson below, using these settings "
              "for every video.", "", heygen_settings(brief), "",
              "How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line "
              "is a natural pause. Do not add or change words, because the edit is timed to this exact narration.", "",
              "Save each finished video with the exact filename shown, and upload it to `/incoming/`.", ""]
        for lesson in m["lessons"]:
            lid = lesson["lesson_id"]
            ldir = d / "lessons" / lid
            sl = json.loads((ldir / "shotlist.json").read_text())
            script = (ldir / "script.md").read_text()
            fname = f"{slug}_{mid}_{lid}_presenter.mp4"
            uploads.append(fname)
            words = sum(len(s["voiceover"].split()) for s in sl["scenes"])
            narration = "\n\n".join(s["voiceover"] for s in sl["scenes"])
            md += [f"## {lid} {lesson['title']}", "",
                   f"- **Filename:** `{fname}`",
                   f"- **Expected length:** about {sl['duration_s'] / 60:.1f} minutes ({words} words). "
                   "The quality gate accepts ±10%."]
            pn = pron_notes(script)
            if pn:
                md.append("- **Pronunciation:** " + " ".join(pn))
            md += ["", "```text", narration, "```", ""]
            # per-lesson asset tracking
            idx_path = ldir / "assets" / "slides" / "index.json"
            idx = json.loads(idx_path.read_text()) if idx_path.exists() else {}
            assets, n_broll, n_screen = [], 0, 0
            for s in sl["scenes"]:
                a = {"scene": s["scene"], "start": s["start"], "end": s["end"], "visual_type": s["visual_type"]}
                vt = s["visual_type"]
                if vt in ("slide", "text"):
                    info = idx.get(str(s["scene"]), {})
                    a.update({"file": f"assets/slides/{info['file']}" if info else None,
                              "status": "RENDERED" if info else "PENDING_RENDER",
                              "needs_design": info.get("needs_design", False)})
                elif vt == "presenter_full":
                    a.update({"file": f"/incoming/{fname}", "status": "PENDING_UPLOAD", "source": "presenter"})
                elif vt == "stock":
                    target = f"{slug}_{lid}_stock_{s['scene']:02d}.mp4"
                    stock_rows.append({"lesson_id": lid, "scene": s["scene"], "query": s["stock_query"],
                                       "orientation": "landscape",
                                       "min_duration_s": math.ceil(s["end"] - s["start"]),
                                       "filename": target})
                    a.update({"file": f"/incoming/{target}", "status": "PENDING_STOCK", "query": s["stock_query"]})
                elif vt == "hero_broll":
                    n_broll += 1
                    target = f"{slug}_{lid}_broll_{n_broll}.mp4"
                    broll.append({"lesson_id": lid, "scene": s["scene"], "tool": s["broll_tool"],
                                  "prompt": s["broll_prompt"], "scene_len": s["end"] - s["start"],
                                  "filename": target})
                    uploads.append(target)
                    a.update({"file": f"/incoming/{target}", "status": "PENDING_UPLOAD"})
                elif vt == "screen":
                    n_screen += 1
                    target = f"{slug}_{lid}_screen_{n_screen}.mp4"
                    uploads.append(target)
                    a.update({"file": f"/incoming/{target}", "status": "PENDING_UPLOAD",
                              "steps": s.get("screen_steps", [])})
                assets.append(a)
            (ldir / "assets.json").write_text(json.dumps({
                "course_id": brief["course_id"], "lesson_id": lid,
                "presenter_track": {"file": f"/incoming/{fname}", "status": "PENDING_UPLOAD",
                                    "expected_s": sl["duration_s"]},
                "thumbnail": {"file": "assets/slides/thumbnail.png",
                              "status": "RENDERED" if "thumbnail" in idx else "PENDING_RENDER"},
                "music": {"file": None, "status": "PENDING_SELECTION",
                          "note": "Choose one track from /assets/music/ (royalty-free) and record its licence."},
                "scenes": assets}, indent=2, ensure_ascii=False) + "\n")
            # screen demo pack
            if lid in demos and n_screen:
                scr = [f"# Screen Demo Pack: {brief['course_id']} {lid} {lesson['title']}", "",
                       "Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: "
                       "the presenter's HeyGen audio is laid over it in the edit.",
                       "Before recording: close notifications, hide bookmarks and personal accounts, use sample "
                       "data only, and zoom the browser or editor so text is readable on a phone.",
                       "Pace each clip to the narration shown. It can run a little long, because the editor trims "
                       "it. Upload each clip to `/incoming/` with the exact filename.", ""]
                k = 0
                for s in sl["scenes"]:
                    if s["visual_type"] != "screen":
                        continue
                    k += 1
                    scr += [f"## Clip {k}: scene {s['scene']}", "",
                            f"- **Filename:** `{slug}_{lid}_screen_{k}.mp4`",
                            f"- **Target length:** about {s['end'] - s['start']:.0f} seconds", "",
                            "**Steps**", ""] + [f"{i}. {st}" for i, st in enumerate(s.get("screen_steps", []), 1)] + [
                            "", "**Narration over this clip (for pacing)**", "", f"> {s['voiceover']}", ""]
                notes = script.split("## Production Notes", 1)[-1].strip()
                scr += ["## Production notes for this lesson", "", notes, ""]
                (packs / f"screen_{lid}.md").write_text("\n".join(scr))
                written.append(f"screen_{lid}.md")
        (packs / f"heygen_{mid}.md").write_text("\n".join(md))
        written.append(f"heygen_{mid}.md")
    # b-roll packs, at most 8 per day
    for i in range(0, len(broll), MAX_BROLL_PER_DAY):
        day = start + dt.timedelta(days=i // MAX_BROLL_PER_DAY)
        chunk = broll[i:i + MAX_BROLL_PER_DAY]
        md = [f"# B-roll Pack: {brief['course_id']}, {day.isoformat()}", "",
              f"{len(chunk)} clips (at most {MAX_BROLL_PER_DAY} a day, to stay inside free daily credits). "
              "16:9, 1080p where offered, 5–8 seconds each. No text, logos or real public figures in any clip. "
              "Upload to `/incoming/` with the exact filename.", ""]
        for j, b in enumerate(chunk, i + 1):
            md += [f"## {j}. [{b['tool']}] {b['lesson_id']} scene {b['scene']}", "",
                   f"- **Filename:** `{b['filename']}`",
                   f"- **Scene length:** {b['scene_len']:.0f} s (if the clip is shorter, the editor holds it "
                   "with a slow push-in)", "", "```text", b["prompt"], "```", ""]
        name = f"broll_{day.isoformat()}.md"
        (packs / name).write_text("\n".join(md))
        written.append(name)
    with (packs / "stock_queries.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["lesson_id", "scene", "query", "orientation", "min_duration_s", "filename"])
        w.writeheader()
        w.writerows(stock_rows)
    written.append("stock_queries.csv")
    readme = [f"# Stage 4 packs: {brief['course_id']} {brief['course_title']}", "",
              "| Pack | What a person does |", "|---|---|",
              "| `heygen_M*.md` | Render one presenter video per lesson in HeyGen with the settings shown |",
              "| `broll_*.md` | Generate the hero clips in Google Flow or Kling, at most 8 a day |",
              "| `screen_L*.md` | Record the screen demos in OBS |",
              "| `stock_queries.csv` | Run the stock_search step (Pexels/Pixabay API), or download manually |",
              "", f"Slides, text cards and thumbnails are already rendered in `lessons/*/assets/slides/`. "
              "Slides marked `needs_design` in `assets.json` are working placeholders: a designer can replace one "
              "by adding `sNN.html` next to it and re-running `render_slides.py`.", "",
              f"## Files expected in /incoming/ ({len(uploads)} plus {len(stock_rows)} stock clips)", ""] + \
             [f"- [ ] `{u}`" for u in uploads] + [""]
    (packs / "README.md").write_text("\n".join(readme))
    return {"packs": written, "uploads": len(uploads), "stock": len(stock_rows), "broll": len(broll)}


def main(args):
    briefs = {b["course_id"]: b for b in json.loads(CATALOG.read_text())}
    start = dt.date.today()
    if "--start" in args:
        start = dt.date.fromisoformat(args[args.index("--start") + 1])
    r = build(briefs[args[0]], start)
    print(f"{args[0]}: {len(r['packs'])} pack files, {r['uploads']} uploads expected, "
          f"{r['stock']} stock clips, {r['broll']} hero clips")


if __name__ == "__main__":
    main(sys.argv[1:])
