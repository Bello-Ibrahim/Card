# Screen Demo Pack: AI-11 L17 Shaping Features: Text, Categories and Dates

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-11-python-for-ai_L17_screen_1.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run the L14 and L16 cells so clean exists
2. Add a new code cell
3. Type: df = clean.copy()
4. Type: df["city"] = df["city"].str.strip().str.lower().str.replace("ha noi", "hanoi")
5. Type: print(df["city"].value_counts())
6. Press Shift + Enter
7. Output: lagos 3 / lima 3 / hanoi 2

**Narration over this clip (for pacing)**

> First, the city column. We strip the spaces, make it lowercase, and replace the spelling with a space in Hanoi. Value counts shows Lagos three, Lima three, and Hanoi two. Six spellings became three cities.

## Clip 2: scene 10

- **Filename:** `ai-11-python-for-ai_L17_screen_2.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Add a new code cell
2. Type: df["month"] = df["order_date"].dt.month
3. Type: df["weekday"] = df["order_date"].dt.dayofweek
4. Type: print(df[["order_date", "month", "weekday"]].head(3))
5. Press Shift + Enter
6. Output: 2026-03-02 3 0 / 2026-03-02 3 0 / 2026-03-03 3 1

**Narration over this clip (for pacing)**

> Next, the date parts. We add a month column and a weekday column. The second of March, twenty twenty-six, is a Monday, so its weekday is zero.

## Clip 3: scene 11

- **Filename:** `ai-11-python-for-ai_L17_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Add a new code cell
2. Type: counts = df["payment"].value_counts()
3. Type: rare = counts[counts < 2].index
4. Type: df["payment"] = df["payment"].replace(list(rare), "other")
5. Type: encoded = pd.get_dummies(df, columns=["city", "payment"], dtype=int)
6. Type: print(encoded.filter(like="city_").head(3))

**Narration over this clip (for pacing)**

> Then Hamza counts the payment methods, and finds those with fewer than two rows. After cleaning, mobile appeared only once, so it becomes other. Finally, get dummies encodes city and payment, with dtype equals int.

## Clip 4: scene 12

- **Filename:** `ai-11-python-for-ai_L17_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Press Shift + Enter
2. Output: city_hanoi city_lagos city_lima / 0 1 0 / 0 1 0 / 1 0 0
3. Scroll to show payment_card, payment_cash and payment_other in encoded.columns

**Narration over this clip (for pacing)**

> Run it. Filter shows only the new city columns. Each row has a single one, in the column for its city. The table also has three new payment columns, for card, cash and other.

## Production notes for this lesson

- [VERSION] pd.get_dummies default output type is True/False (bool) in pandas 2.0 and later, and 0/1 integers (uint8) in earlier versions. The lesson uses dtype=int so results match; the voiceover says only that the default depends on the version. Outputs were produced with Python 3.11 and pandas 3.0.6, and tested with pandas 2.2.3.
- The order data is synthetic, created for this course. Hamza (Rabat) is fictional.
- Printed outputs on screen must match content.md: value_counts 'lagos 3 / lima 3 / hanoi 2'; the order_date / month / weekday head(3) table (2026-03-02 3 0; 2026-03-02 3 0; 2026-03-03 3 1); and the city_hanoi / city_lagos / city_lima 0/1 table.
- Before the demo, run the L14 and L16 cells on screen (or show them already run) so clean exists.
