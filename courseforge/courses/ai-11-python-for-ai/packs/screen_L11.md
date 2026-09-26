# Screen Demo Pack: AI-11 L11 Meet pandas: Series and DataFrames

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L11_screen_1.mp4`
- **Target length:** about 29 seconds

**Steps**

1. Add a new code cell
2. Paste the sample cell from content.md: import io, import pandas as pd, the sample text (country,continent,year,lifeExp,pop,gdpPercap and 18 rows), then df = pd.read_csv(io.StringIO(sample))
3. Press Shift + Enter; no output appears

**Narration over this clip (for pacing)**

> We paste one cell into Colab. It imports pandas and holds the practice sample as text in CSV format. A small helper from the io module lets read csv treat that text as if it were a file, and the result is a DataFrame called df. With a real file, you would simply give read csv the file name. We use this same sample until lesson fifteen.

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L11_screen_2.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Add a new code cell
2. Type: print(df.shape)
3. Type: print(df.columns.tolist())
4. Type: print(df["year"].unique())
5. Press Shift + Enter
6. Output: (18, 6) / ['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap'] / [1997 2002 2007]

**Narration over this clip (for pacing)**

> Now a first look. Shape tells us there are eighteen rows and six columns. Next we list the column names. And then the unique years. There are three, nineteen ninety-seven, two thousand and two, and two thousand and seven.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L11_screen_3.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Add a new code cell
2. Type: df.describe().round(1)
3. Press Shift + Enter
4. Point at the min and max rows: lifeExp 54.8 to 78.5; pop 15,000,000 to 85,000,000

**Narration over this clip (for pacing)**

> Next, describe, rounded to one decimal place. Look at the minimum and maximum rows. Life expectancy runs from fifty-four point eight to seventy-eight point five. Population runs from fifteen million to eighty-five million. That is a much wider range. Notice that country and continent are missing from this summary. We will see why in a moment.

## Clip 4: scene 11

- **Filename:** `ai-11-python-for-ai_L11_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Add a new code cell
2. Type: df.info()
3. Press Shift + Enter
4. Point at the non-null counts (18 in every column) and the dtype column

**Narration over this clip (for pacing)**

> Finally, info. Every column has eighteen values that are not missing, so nothing is missing. It also shows each column's data type. The text columns may show a different type name, depending on your pandas version.

## Production notes for this lesson

- [VERIFY] Gapminder data source, access method (CSV URL or the plotly library copy) and licence must be confirmed before recording and before learners publish results. The voiceover says only that learners must check the source and licence.
- [VERSION] px.data.gapminder() availability in the Colab runtime; dtype names in info() (str in pandas 3, object in older versions). content.md outputs were produced with Python 3.11 and pandas 3.0.6.
- The practice sample values are invented and must stay labelled on screen as 'Invented practice data, not real statistics' whenever the table is visible.
- Printed outputs on screen must match content.md: '(18, 6)', "['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap']", '[1997 2002 2007]'; describe() min/max: lifeExp 54.8 to 78.5, pop 15,000,000 to 85,000,000.
- Screen step for the sample cell: paste the full sample cell from content.md rather than typing it; zoom so the reader can see it is a CSV block.
- Aroha (Wellington) is fictional.
