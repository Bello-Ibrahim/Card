# Screen Demo Pack: AI-11 L12 Selecting and Filtering Rows and Columns

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L12_screen_1.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Run the L11 sample cell so df exists
2. Add a new code cell
3. Type: latest = df[df["year"] == df["year"].max()]

**Narration over this clip (for pacing)**

> First, we keep only the latest year. Instead of typing two thousand and seven, we ask for the maximum year, so the code still works when newer data is added.

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L12_screen_2.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Type: mask = latest["continent"].isin(["Africa", "Americas"]) & (latest["lifeExp"] > 60)
2. Type: result = latest.loc[mask, ["country", "continent", "lifeExp"]]
3. Type: print(result) and print(len(result))

**Narration over this clip (for pacing)**

> Next, the mask. The continent must be in our list of two, and life expectancy must be above sixty. Then loc keeps the matching rows, and only three columns. We print the result and count its rows.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L12_screen_3.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Press Shift + Enter
2. Output: Ghana Africa 60.1 (index 5) / Peru Americas 71.6 (index 8) / Chile Americas 78.5 (index 11) / 3
3. Point at the index labels 5, 8, 11

**Narration over this clip (for pacing)**

> Run it. Ghana, Peru and Chile, and a count of three. The numbers on the left show which rows of the original table were kept. Kenya is not there, because its value, fifty-nine point six, is below sixty. Counting the rows is a quick check that the filter did what you meant.

## Clip 4: scene 11

- **Filename:** `ai-11-python-for-ai_L12_screen_4.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Add a new code cell
2. Type: asia07 = df[(df["continent"] == "Asia") & (df["year"] == 2007)]
3. Type: print(asia07.sort_values("pop", ascending=False)[["country", "pop"]])
4. Press Shift + Enter
5. Output: Vietnam 85000000 (index 14) / Nepal 28000000 (index 17)

**Narration over this clip (for pacing)**

> One more. Asian countries in two thousand and seven, with the largest population first. We combine two conditions, each in its own brackets. Then we sort by population in descending order, and show two columns. Vietnam comes first, with eighty-five million people, then Nepal. Two rows, which is what we expected from the sample.

## Production notes for this lesson

- [VERIFY] Gapminder data source, access method and licence (carried from L11). The practice sample values are invented; label the table on screen as 'Invented practice data'.
- [VERSION] Outputs and error messages were produced with Python 3.11 and pandas 3.0.6. The voiceover mentions the 'truth value is ambiguous' error only in general terms; the second error (missing brackets) may be worded differently in other pandas versions and is not shown on screen.
- Printed outputs on screen must match content.md: the Ghana / Peru / Chile table with index labels 5, 8, 11, then '3'; the Vietnam 85000000 / Nepal 28000000 table with index 14 and 17.
- Before the demo, run the L11 sample cell on screen (or show it already run) so df exists.
- Mateus (Maputo) is fictional.
