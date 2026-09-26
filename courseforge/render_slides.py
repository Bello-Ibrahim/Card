"""Stage 4: render branded slides, text cards and thumbnails to 1920x1080 PNG.

Usage: python courseforge/render_slides.py COURSE_ID [LESSON_ID ...]

Reads each lesson's shotlist.json and writes lessons/{Lxx}/assets/slides/:
  s{NN}.png for every slide and text scene, thumbnail.png, and index.json
  (scene -> file, layout, needs_design). Slide bodies are descriptions written
  in Stage 3; common patterns are drawn automatically (numbered lists, "→" flows,
  "Left:/Right:" comparisons, code, quotes). A body the parser cannot lay out is
  still rendered as a clean text slide but flagged needs_design for a designer.

If lessons/{Lxx}/assets/slides/s{NN}.html exists, its body HTML (using the CSS
classes defined here) replaces the automatic layout for that scene.

The bottom-right corner (480x600) is kept clear for the keyed presenter.
Uses the pre-installed Chromium via Playwright (PLAYWRIGHT_BROWSERS_PATH).
"""

import html
import json
import re
import sys
from pathlib import Path

from check_curriculum import CATALOG, ROOT, slug_for

NAVY, TEAL, WHITE, MUTED = "#0B1F3A", "#00C2A8", "#FFFFFF", "#9FB3C8"
FONT = (ROOT / "brand" / "fonts" / "InterVariable.woff2").resolve()
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = f"""
@font-face {{ font-family: Inter; src: url('file://{FONT}') format('woff2'); font-weight: 100 900; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ width: 1920px; height: 1080px; background: {NAVY}; color: {WHITE};
       font-family: Inter, sans-serif; position: relative; overflow: hidden; }}
.brand {{ position: absolute; top: 48px; left: 96px; font-weight: 800; font-size: 30px; letter-spacing: -0.5px; }}
.brand b {{ color: {TEAL}; }}
.bar {{ position: absolute; top: 0; left: 0; width: 100%; height: 10px; background: {TEAL}; }}
.tag {{ position: absolute; bottom: 48px; left: 96px; font-size: 24px; color: {MUTED}; }}
.main {{ position: absolute; top: 150px; left: 96px; width: 1300px; bottom: 120px;
        display: flex; flex-direction: column; justify-content: center; gap: 36px; }}
h1 {{ font-size: 64px; font-weight: 800; line-height: 1.1; letter-spacing: -1px; }}
h1.big {{ font-size: 96px; }}
.sub {{ font-size: 34px; color: {MUTED}; line-height: 1.35; }}
ol, ul {{ list-style: none; display: flex; flex-direction: column; gap: 22px; }}
li {{ font-size: 34px; line-height: 1.3; padding-left: 64px; position: relative; }}
li .n {{ position: absolute; left: 0; top: -2px; width: 44px; height: 44px; border-radius: 50%;
        background: {TEAL}; color: {NAVY}; font-weight: 800; font-size: 24px;
        display: flex; align-items: center; justify-content: center; }}
li.dot::before {{ content: ''; position: absolute; left: 14px; top: 16px; width: 14px; height: 14px;
        border-radius: 50%; background: {TEAL}; }}
.flow {{ display: flex; flex-wrap: wrap; align-items: stretch; gap: 18px; }}
.box {{ flex: 1 1 0; min-width: 200px; background: rgba(255,255,255,0.06); border: 2px solid {TEAL};
       border-radius: 20px; padding: 26px; font-size: 28px; line-height: 1.3; display: flex; align-items: center; }}
.arrow {{ align-self: center; color: {TEAL}; font-size: 48px; font-weight: 800; }}
.cols {{ display: flex; gap: 32px; }}
.col {{ flex: 1; background: rgba(255,255,255,0.06); border-radius: 24px; padding: 36px; border-top: 8px solid {TEAL}; }}
.col h2 {{ font-size: 36px; font-weight: 800; margin-bottom: 18px; color: {TEAL}; }}
.col p {{ font-size: 28px; line-height: 1.4; }}
.col.b {{ border-top-color: {MUTED}; }}
.col.b h2 {{ color: {WHITE}; }}
pre {{ background: #06132A; border-left: 8px solid {TEAL}; border-radius: 16px; padding: 36px 40px;
      font-family: 'DejaVu Sans Mono', monospace; font-size: 26px; line-height: 1.5; white-space: pre-wrap; color: #E6F7F4; }}
.quote {{ font-size: 52px; font-weight: 700; line-height: 1.25; border-left: 10px solid {TEAL}; padding-left: 48px; }}
.card {{ position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; padding: 0 200px; text-align: center; }}
.card h1 {{ font-size: 88px; }}
.card h1 em {{ font-style: normal; color: {TEAL}; }}
.body {{ font-size: 32px; line-height: 1.45; color: {WHITE}; }}
"""

WORDMARK = '<div class="bar"></div><div class="brand">Certif<b>AI</b></div>'


def esc(t):
    return html.escape(t.strip())


def tidy(t):
    """Clean a description fragment for display: drop drawing words, capitalise, no trailing full stop."""
    t = re.sub(r"\s+(box|icon|arrow)$", "", t.strip(" .;"), flags=re.I)
    return t[:1].upper() + t[1:] if t else t


def split_tag(body):
    m = re.search(r"\s*(?:Tag|Caption|Small tag):\s*(.+)$", body)
    return (body[:m.start()], m.group(1)) if m else (body, "")


def items_numbered(body):
    parts = re.split(r"(?:^|\s)(\d{1,2})\.\s+", body)
    if len(parts) >= 5:
        return [p.strip(" ;") for p in parts[2::2] if p.strip()]
    return None


def items_simple(body):
    for sep in (" · ", "; "):
        if body.count(sep) >= 1:
            return [p.strip(" .") for p in body.split(sep) if p.strip()]
    return None


def slide_html(slide, course_tag):
    layout, title, body = slide.get("layout"), slide.get("title", ""), slide.get("body", "")
    body, tag = split_tag(body)
    tag = tag or course_tag
    needs = False
    inner = f"<h1>{esc(title)}</h1>" if title else ""
    if layout == "title":
        chips = items_simple(body) or [body]
        inner = f'<h1 class="big">{esc(title)}</h1><div class="sub">{" · ".join(esc(c) for c in chips)}</div>'
    elif layout == "bullets":
        nums = items_numbered(body)
        if nums:
            inner += "<ol>" + "".join(f'<li><span class="n">{i}</span>{esc(t)}</li>' for i, t in enumerate(nums, 1)) + "</ol>"
        else:
            m = re.match(r"([^:]{3,80}):\s*(.+)$", body)
            lead, rest = (m.group(1), m.group(2)) if m else ("", body)
            items = items_simple(rest)
            if items and len(items) >= 2:
                inner += (f'<div class="sub">{esc(lead)}</div>' if lead else "")
                inner += "<ul>" + "".join(f'<li class="dot">{esc(t)}</li>' for t in items[:7]) + "</ul>"
            else:
                inner += f'<div class="body">{esc(body)}</div>'
                needs = True
    elif layout == "diagram":
        if "→" in body:
            steps = [re.sub(r"^(arrow|then)\s*", "", s.strip(), flags=re.I) for s in body.split("→")]
            steps = [s for s in steps if s and s.lower() not in ("arrow",)]
            parts = []
            for i, s in enumerate(steps[:6]):
                if i:
                    parts.append('<div class="arrow">→</div>')
                parts.append(f'<div class="box">{esc(tidy(s))}</div>')
            inner += f'<div class="flow">{"".join(parts)}</div>'
            needs = len(steps) > 6
        else:
            inner += f'<div class="body">{esc(body)}</div>'
            needs = True
    elif layout == "comparison":
        m = re.match(r"\s*Left[^:]*:\s*(.+?)[.;]?\s+Right[^:]*:\s*(.+)$", body, re.S)
        if m:
            lt, rt = m.group(1), m.group(2)
            lh = re.match(r"\s*Left,?\s*([^:]*):", body)
            rh = re.search(r"Right,?\s*([^:]*):", body)
            inner += (f'<div class="cols"><div class="col"><h2>{esc(lh.group(1) or "Before")}</h2><p>{esc(lt)}</p></div>'
                      f'<div class="col b"><h2>{esc(rh.group(1) or "After")}</h2><p>{esc(rt)}</p></div></div>')
        elif "→" in body or " vs " in body.lower():
            a, _, b = re.split(r"(→| vs | VS | Vs )", body, maxsplit=1)
            inner += (f'<div class="cols"><div class="col"><p>{esc(tidy(a))}</p></div>'
                      f'<div class="arrow">→</div><div class="col b"><p>{esc(tidy(b))}</p></div></div>')
            needs = True
        else:
            items = items_simple(body)
            if items and len(items) == 2:
                inner += (f'<div class="cols"><div class="col"><p>{esc(items[0])}</p></div>'
                          f'<div class="col b"><p>{esc(items[1])}</p></div></div>')
            else:
                inner += f'<div class="body">{esc(body)}</div>'
                needs = True
    elif layout == "code":
        inner += f"<pre>{html.escape(body.strip())}</pre>"
    elif layout == "quote":
        inner = (f"<h1>{esc(title)}</h1>" if title else "") + f'<div class="quote">{esc(body)}</div>'
    else:
        inner += f'<div class="body">{esc(body)}</div>'
        needs = True
    page = f'{WORDMARK}<div class="main">{inner}</div><div class="tag">{esc(tag)}</div>'
    return page, needs


def card_html(text, course_tag):
    t = esc(text)
    words = t.split()
    if len(words) > 2:  # highlight the last phrase in teal
        cut = max(1, len(words) // 2)
        t = " ".join(words[:cut]) + " <em>" + " ".join(words[cut:]) + "</em>"
    return f'{WORDMARK}<div class="card"><h1>{t}</h1></div><div class="tag">{esc(course_tag)}</div>'


def thumb_html(headline, course_title, lesson_label):
    return (f'{WORDMARK}<div class="main" style="width:1500px"><div class="sub" style="color:{TEAL};font-weight:700">'
            f'{esc(course_title)}</div><h1 class="big" style="font-size:132px">{esc(headline)}</h1>'
            f'<div class="sub">{esc(lesson_label)}</div></div>')


def render_course(brief, wanted=None):
    from playwright.sync_api import sync_playwright

    d = ROOT / "courses" / slug_for(brief)
    c = json.loads((d / "curriculum.json").read_text())
    lessons = [lesson for m in c["modules"] for lesson in m["lessons"]]
    total = len(lessons)
    stats = {"rendered": 0, "needs_design": 0}
    tmp = ROOT / "brand" / "_render.html"
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        def shot(body_html, out):
            tmp.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head>"
                           f"<body>{body_html}</body></html>")
            page.goto(tmp.resolve().as_uri())
            page.evaluate("document.fonts.ready")
            page.screenshot(path=str(out))
            stats["rendered"] += 1

        for n, lesson in enumerate(lessons, 1):
            lid = lesson["lesson_id"]
            if wanted and lid not in wanted:
                continue
            sl = json.loads((d / "lessons" / lid / "shotlist.json").read_text())
            out = d / "lessons" / lid / "assets" / "slides"
            out.mkdir(parents=True, exist_ok=True)
            tag = f"{brief['course_title']} · Lesson {n} of {total}"
            index = {}
            for s in sl["scenes"]:
                f = out / f"s{s['scene']:02d}.png"
                custom = out / f"s{s['scene']:02d}.html"
                if s["visual_type"] == "slide" and custom.exists():
                    # a designed override (body HTML using the CSS classes above) replaces the automatic layout
                    shot(f'{WORDMARK}{custom.read_text()}<div class="tag">{esc(tag)}</div>', f)
                    index[s["scene"]] = {"file": f.name, "layout": s["slide"]["layout"], "needs_design": False,
                                         "custom": custom.name}
                elif s["visual_type"] == "slide":
                    body, needs = slide_html(s["slide"], tag)
                    shot(body, f)
                    stats["needs_design"] += needs
                    index[s["scene"]] = {"file": f.name, "layout": s["slide"]["layout"], "needs_design": needs}
                elif s["visual_type"] == "text":
                    shot(card_html(s["on_screen_text"], tag), f)
                    index[s["scene"]] = {"file": f.name, "layout": "text_card", "needs_design": False}
            shot(thumb_html(sl["thumbnail"]["headline"], brief["course_title"], f"Lesson {n} · {lesson['title']}"),
                 out / "thumbnail.png")
            index["thumbnail"] = {"file": "thumbnail.png", "layout": "thumbnail", "needs_design": False}
            (out / "index.json").write_text(json.dumps(index, indent=2) + "\n")
        browser.close()
    tmp.unlink(missing_ok=True)
    return stats


def main(args):
    briefs = {b["course_id"]: b for b in json.loads(CATALOG.read_text())}
    stats = render_course(briefs[args[0]], set(args[1:]) or None)
    print(f"{args[0]}: {stats['rendered']} images rendered, {stats['needs_design']} slides flagged needs_design")


if __name__ == "__main__":
    main(sys.argv[1:])
