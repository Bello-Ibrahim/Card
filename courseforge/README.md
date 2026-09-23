# CourseForge (budget mode)

An agent specification that turns a course brief into lesson videos. The
orchestrator is n8n and the "brain" is Claude via the Batch API. The steps a
cheap stack can't automate go to a human as ready-to-paste packs.

| File | Purpose |
|---|---|
| `system_prompt.md` | The full agent prompt, with the budget-mode overrides merged in |
| `tools.json` | Tool definitions in Claude API format (`name` / `description` / `input_schema`) for the n8n agent node |
| `course_brief.schema.json` | JSON Schema for validating a brief before a run |
| `examples/course_brief.example.json` | Example brief |

## Changes from the original draft

The budget-mode block contradicted parts of the full-stack prompt. I resolved
those conflicts in `system_prompt.md`:

- **Stage 4** called `heygen_create_video`, `veo_generate_clip`,
  `kling_generate_clip`, `image_generate` and `check_job_status`, and budget mode
  has none of them. These are now manual packs (HeyGen, B-roll, Screen Demo)
  plus `slide_render` and `stock_search`. Polling is replaced by `storage_list`
  checks on `/incoming/`.
- **The thumbnail** is now a branded slide rendered with `slide_render`, so no
  paid image generation is needed.
- **Stage 5 retries** are split in two. Automated assets are regenerated.
  Manual assets get a revised prompt in the next pack. The "NEEDS_HUMAN" rule
  after 2 retries is unchanged.
- **Stage 7** is captions only: translated SRT sidecar files, no dubbing.
  Burned-in translated versions are optional.
- **The presenter** is one continuous HeyGen video per lesson on #00FF00. It is
  the master audio track, so shot-list timings follow the narration.
- **Two tools were added**, because the rules can't be followed without them:
  - `media_probe` (ffprobe): the ±1.5s duration check needs real measurements.
  - `storage_list`: the no-fabrication rule needs proof that an upload exists.
- **Music** comes from a pre-loaded royalty-free folder (`/assets/music/`),
  because budget mode has no music tool.
- **Cost control** counts only variable API spend against `budget_limit_usd`.
  Fixed subscriptions are reported separately.

## Cost stack

| Job | Tool | Cost | Runs |
|---|---|---|---|
| Content, scripts, prompts, quizzes, slides | Claude API, `claude-sonnet-5`, Batch API | $2.00 / $10.00 per M input/output tokens; the Batch API halves this to **$1.00 / $5.00** | Automated |
| Orchestrator | n8n, self-hosted | Free locally, ~$5–7/month on a VPS | Automated |
| Presenter | HeyGen Creator, standard avatars | $29/month [VERIFY] | Manual (HeyGen Batch Pack) |
| Slides and motion graphics | HTML → PNG → FFmpeg zoom/pan | Free | Automated |
| Stock B-roll | Pexels / Pixabay APIs | Free | Automated |
| Hero B-roll (≤2 per lesson) | Google Flow (Veo), Kling free credits | Free [VERIFY daily limits] | Manual (B-roll Pack) |
| Screen demos | OBS Studio | Free | Manual |
| Captions | Whisper (local) | Free | Automated |
| Caption translation | Claude (batch) | A few dollars | Automated |
| Music | YouTube Audio Library / Pixabay Music | Free | Pre-loaded by a human |
| Assembly | FFmpeg | Free | Automated |

I confirmed the Claude pricing (Sonnet 5 at $2/$10 per million tokens, 50% off
on the Batch API) against Anthropic's current model table. The HeyGen and
Flow/Kling figures come from the original brief and third-party reviews, so
check them on the vendors' pricing pages. The claim that standard-avatar video
is unlimited and uses no credits is disputed by reviewers. Test standard-avatar
quality and your real monthly output in the first month before committing.

**Rough Claude cost per lesson:** about 10k input and 8k output tokens across
content, script, shot list and slide HTML comes to about $0.05 per lesson at
batch rates. Translating captions adds about $0.01 per language per lesson. A
20-lesson course in 4 languages should cost well under $5 in variable spend.
These are estimates. The agent recalculates them before each stage from real
token counts.

## Running a course

1. Validate the brief:
   `python -c "import json,jsonschema; jsonschema.validate(json.load(open('brief.json')), json.load(open('courseforge/course_brief.schema.json')))"`
2. In n8n, create an AI Agent node. Set its system prompt to
   `system_prompt.md` and its tools to `tools.json`. Give it the brief as the
   first user message.
3. Map each tool to a workflow: Anthropic Batches API, a headless-Chromium
   screenshot, the Pexels/Pixabay HTTP APIs, `whisper` CLI, `ffmpeg`/`ffprobe`,
   file storage, and a Slack/email node for `notify_human`.
4. Approve the curriculum (Stage 1) and the first lesson's script (Stage 3).
   Then work through the packs and upload the files to `/incoming/` using the
   exact filenames given.
