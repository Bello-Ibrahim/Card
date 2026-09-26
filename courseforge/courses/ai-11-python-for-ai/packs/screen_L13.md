# Screen Demo Pack: AI-11 L13 Sorting, Grouping and Summarising

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L13_screen_1.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Run the L11 sample cell so df exists
2. Add a new code cell
3. Type: summary = df.groupby(["continent", "year"])["gdpPercap"].median()
4. Type: print(summary.unstack())

**Narration over this clip (for pacing)**

> We group by two columns, continent and year, take the income column, and calculate the median. Then unstack turns the years into columns, so the table is easy to read across. Grouping by two columns gives one value for each pair of continent and year.

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L13_screen_2.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Press Shift + Enter
2. Output: table with columns 1997, 2002, 2007: Africa 1230.0 / 1235.0 / 1405.0; Americas 7980.0 / 8345.0 / 10290.0; Asia 1200.0 / 1410.0 / 1765.0
3. Point along the Americas row, then down the 2007 column

**Narration over this clip (for pacing)**

> Run it. We get one row per continent, and one column per year. In this sample, the Americas have much higher values than the other two groups. And all three groups increase from two thousand and two to two thousand and seven.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L13_screen_3.mp4`
- **Target length:** about 27 seconds

**Steps**

1. Add a new code cell
2. Type: print(df.sort_values("gdpPercap", ascending=False).head(3)[["country", "year", "gdpPercap"]])
3. Press Shift + Enter
4. Output: Chile 2007 13170 / Chile 2002 10780 / Chile 1997 10120

**Narration over this clip (for pacing)**

> But with only two countries per continent, these are practice numbers only. Real conclusions need the full dataset. So which rows drive the high Americas values? A quick sort, largest first, showing the top three rows. All three are Chile. So one country pulls the Americas group up. This is a good habit. When a summary surprises you, look at the rows behind it.

## Production notes for this lesson

- [VERIFY] Gapminder data source, access method and licence (carried from L11). The practice sample values are invented; label the table on screen as 'Invented practice data'.
- [VERSION] Printed output formats (for example the 'Name: count' line under value_counts()) differ between pandas versions. Outputs were produced with Python 3.11 and pandas 3.0.6.
- Printed outputs on screen must match content.md: the unstacked median table (Africa 1230.0 / 1235.0 / 1405.0; Americas 7980.0 / 8345.0 / 10290.0; Asia 1200.0 / 1410.0 / 1765.0) and the Chile 2007 13170 / 2002 10780 / 1997 10120 sort.
- Soo-ah (Seoul) is fictional. Stock footage of receipts must show no readable shop names or logos.
