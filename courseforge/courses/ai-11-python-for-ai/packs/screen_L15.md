# Screen Demo Pack: AI-11 L15 Exploring Data with Charts

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L15_screen_1.mp4`
- **Target length:** about 29 seconds

**Steps**

1. Run the L11 sample cell so df exists
2. Add a new code cell
3. Type: import matplotlib.pyplot as plt
4. Type: ax = df["lifeExp"].plot(kind="hist", bins=6, title="Life expectancy (practice sample)")
5. Type: ax.set_xlabel("Life expectancy (years)") and plt.show()
6. Press Shift + Enter; the histogram appears
7. Point at the two groups of bars

**Narration over this clip (for pacing)**

> First, a histogram of life expectancy. The bins setting asks for six bars, and we add a title and a label on the horizontal axis. It shows two groups. Several values between about fifty-five and sixty-four, several between about sixty-eight and seventy-nine, and few in between. With a different number of bars, the picture can change, so it is worth trying two or three.

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L15_screen_2.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Add a new code cell
2. Type: latest = df[df["year"] == 2007]
3. Type: ax = latest.plot(kind="bar", x="country", y="gdpPercap", legend=False, title="GDP per person, 2007 (practice sample)")
4. Type: ax.set_ylabel("GDP per person (US$)") and plt.show()
5. Press Shift + Enter; the bar chart appears

**Narration over this clip (for pacing)**

> Next, a bar chart. We keep only two thousand and seven, and plot income per person by country, with a title and a label on the vertical axis, in US dollars. Chile stands far above the other five countries.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L15_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Add a new code cell
2. Type: ax = df.plot(kind="scatter", x="gdpPercap", y="lifeExp", logx=True, title="Richer countries, longer lives?")
3. Type: ax.set_xlabel("GDP per person (log scale)") and ax.set_ylabel("Life expectancy (years)")
4. Type: plt.show()
5. Press Shift + Enter; the scatter plot appears
6. Circle the three Vietnam points high on the left

**Narration over this clip (for pacing)**

> Finally, a scatter plot of income against life expectancy, with a log scale for income. The dots generally rise from left to right. But three points sit high on the left. Vietnam has life expectancy above seventy with low income per person.

## Clip 4: scene 11

- **Filename:** `ai-11-python-for-ai_L15_screen_4.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Add a text cell under the scatter plot
2. Type: Question: why is Vietnam high on the left? Practice data only, not a conclusion.

**Narration over this clip (for pacing)**

> Rafael notes this as a question for further reading, not a conclusion. He also reminds the teachers that these are invented practice numbers. Real statements need the full dataset.

## Production notes for this lesson

- [VERSION] pandas plotting options (kind, bins, logx, legend, title) and matplotlib behaviour differ between versions; check in the current Colab runtime. content.md code was tested with pandas 3.0.6 and matplotlib 3.11.2.
- [VERIFY] Gapminder data source, access method and licence (carried from L11). The practice sample values are invented; every chart title in the demo includes 'practice sample' or the screen shows the label 'Invented practice data'.
- Charts on screen must be the ones produced by the content.md code: a 6-bin life expectancy histogram with two groups (about 55 to 64 and about 68 to 79); a 2007 GDP-per-person bar chart with Chile far above the rest; a log-scale scatter with three Vietnam points high on the left.
- Rafael (Lisbon) is fictional.
