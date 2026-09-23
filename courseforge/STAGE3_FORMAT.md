# Stage 3 formats

`check_script.py` enforces these formats. Stage 3 turns each lesson's `content.md` into a spoken script (`script.md`) and a timed shot list (`shotlist.json`), both saved in `lessons/{lesson_id}/`.

## script.md

The narration is the text pasted into HeyGen, so it must read well when spoken.

```markdown
# L01 What Is AI, Really? | Presenter Script

Course: AI-01 · Video: 5 min · Words: 702

## Hook
One continuous narration, 20 seconds or less (about 45 words at most).

## Explain
...

## Demonstrate
...

## Recap
...

## CTA
...

## Thumbnail
Headline: Rules or Learning?
Image: one line describing the branded thumbnail slide.

## Production Notes
- Anything the presenter, editor or reviewer must know, with [VERIFY]/[VERSION]/[REGION] tags carried from content.md. Write "- None." if there is nothing.
```

Narration rules:
- The five narration sections (Hook to CTA) contain only spoken words: no markdown, lists, links, code, tags or stage directions.
- Word count is `lesson_length_min × 140`, ±10% (630–770 words for a 5-minute lesson).
- Write for the ear: short sentences, B2-level international English, no idioms. Say numbers the way they are spoken. Don't read code aloud; describe what it does and let the screen show it.
- No unverified facts. If content.md flags a claim, the script either leaves it out or keeps the claim with its tag in Production Notes for review.
- Use one example thread from content.md. Don't try to cover everything; the lesson page carries the full text.
- The CTA points learners to the lesson's hands-on exercise (and, near the end of the course, the capstone), and ends by naming the next lesson.
- Don't mention CertifAI's prices, other companies' brands (except the tools in the brief or DECISIONS.md) or anything that dates quickly.

## shotlist.json

```json
{
  "course_id": "AI-01",
  "lesson_id": "L01",
  "duration_s": 300.0,
  "thumbnail": {"headline": "Rules or Learning?", "slide": {"layout": "thumbnail", "title": "Rules or Learning?", "body": "..."}},
  "scenes": [
    {
      "scene": 1,
      "start": 0.0,
      "end": 18.0,
      "visual_type": "presenter_full",
      "voiceover": "exact narration words for this scene",
      "on_screen_text": "optional short caption, 8 words or fewer"
    }
  ]
}
```

- `visual_type` is one of `presenter_full`, `slide`, `stock`, `hero_broll`, `screen`, `text`.
- **presenter_full**: the presenter fills the frame. Scene 1 (the hook) and the last scene (the CTA) must use it.
- **slide**: needs `"slide": {"layout": "title|bullets|diagram|comparison|quote|code", "title": "...", "body": "..."}`. The body describes the content (bullets, diagram elements, code) for slide_render. It is not HTML.
- **stock**: needs `"stock_query"` (3–8 plain words, no brands).
- **hero_broll**: needs `"broll_prompt"` (Subject + Action + Setting + Camera movement + Lighting + Style + Duration 5–8s; diverse international people and settings; no text, logos or real public figures) and `"broll_tool": "FLOW"|"KLING"`. At most 2 per lesson. Use it only when slides or stock footage can't cover the scene.
- **screen**: needs `"screen_steps"` (a list of on-screen actions). Allowed only when the lesson is in the curriculum's `screen_demo_lessons`.
- **text**: a full-screen text card. Needs `on_screen_text`.
- The presenter's audio runs through every scene. For all types except `presenter_full`, the presenter appears keyed in a corner.
- Scenes are numbered from 1, run back to back from 0.0 to `duration_s` with no gaps, and each lasts 3–30 seconds.
- Each scene's length is its voiceover word count × 60 / 140, ±2.0 seconds (or ±25% for long scenes).
- Joined together, the scene voiceovers must equal the script narration word for word, ignoring punctuation and case.
- `duration_s` equals total narration words × 60 / 140, ±10 seconds.
- The thumbnail headline is 5 words or fewer.
