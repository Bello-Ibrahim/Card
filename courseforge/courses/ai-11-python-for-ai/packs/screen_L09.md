# Screen Demo Pack: AI-11 L09 Modules, Libraries and Installing Packages

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L09_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Add a new code cell
2. Type: import math / import random / from datetime import date
3. Type: print(math.sqrt(81), math.ceil(4.2))

**Narration over this clip (for pacing)**

> We import math and random, and the date tool from datetime. First, a quick test of math. The square root of eighty-one is nine, and math ceil rounds four point two up to five. Rounding up is useful for questions like, how many boxes do I need?

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L09_screen_2.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Type: fair = date(2026, 12, 5)
2. Type: today = date(2026, 9, 23)
3. Type: print((fair - today).days, "days to go")
4. Press Shift + Enter
5. Output: 9.0 5 / 73 days to go

**Narration over this clip (for pacing)**

> Next, two dates. The fair is on the fifth of December, twenty twenty-six. For today, we use a fixed date, so the output is the same every time. We subtract one date from the other and ask for the days. Run it, and there are seventy-three days to go.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L09_screen_3.mp4`
- **Target length:** about 26 seconds

**Steps**

1. Add a new code cell
2. Type: random.seed(42)
3. Type: names = ["Tariq", "Ingrid", "Chen", "Adaeze"]
4. Type: print(random.choice(names))
5. Press Shift + Enter
6. Output: Tariq

**Narration over this clip (for pacing)**

> Now the prize draw. We make a list of four volunteer names, and random choice picks one. But first we set a seed. The seed makes the random result repeatable, so everyone who runs this gets the same name. That matters in data work, because others must be able to reproduce your results. For a real draw, remove the seed.

## Clip 4: scene 11

- **Filename:** `ai-11-python-for-ai_L09_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Add a new code cell
2. Type: import pandas as pd
3. Type: print(pd.__version__)
4. Type: # %pip install some-package-name
5. Press Shift + Enter; a version number appears (depends on the runtime)

**Narration over this clip (for pacing)**

> Finally, we import pandas with the short nickname p d, which almost all pandas code uses, and print its version. It is already installed. The install command stays as a comment, so we don't run it.

## Production notes for this lesson

- [VERSION] Check the Colab install command (%pip vs !pip), the libraries pre-installed in Colab, the pandas version printed, and how long installed packages last in a Colab session against the live tool before recording.
- Verified with Python 3.11 on 2026-09-23: random.seed(42) then random.choice picks Tariq.
- The pandas version number on screen depends on the Colab runtime; the voiceover does not say it.
- Judgement call (curriculum): NumPy is named only; its maths use is covered in AI-05.
- Printed outputs on screen must match content.md: '9.0 5' and '73 days to go'. Valentina, the Bogotá book fair, the date and the names are made up.
