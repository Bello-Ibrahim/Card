# Screen Demo Pack: AI-11 L16 Cleaning Data: Missing Values, Duplicates and Types

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L16_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run the L14 data cell so orders exists
2. Add a new code cell
3. Type: clean = orders.drop_duplicates()
4. Type: clean = clean[clean["quantity"] > 0]
5. Type: clean = clean.dropna(subset=["order_date"]).copy()

**Narration over this clip (for pacing)**

> We make a new table called clean. First, we drop the duplicate. Then we keep only rows with a quantity above zero. Then we drop the row with no order date, and make a copy, so later changes don't affect the original.

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L16_screen_2.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Type: clean["unit_price"] = pd.to_numeric(clean["unit_price"], errors="coerce")
2. Type: clean["unit_price"] = clean["unit_price"].fillna(clean["unit_price"].median())
3. Type: clean["order_date"] = pd.to_datetime(clean["order_date"])
4. Type: print(clean.shape, clean.isna().sum().sum())

**Narration over this clip (for pacing)**

> Next, the price. We convert it to numbers, so unknown becomes missing, and fill it with the median price. Then we convert the dates to real dates. Finally, we print the shape and the total count of missing values.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L16_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Press Shift + Enter
2. Output: (8, 8) 0

**Narration over this clip (for pacing)**

> Run it. Eight rows and eight columns, and zero missing values. The table went from eleven rows to eight. The price is now a number column, and the order date is a date column.

## Clip 4: scene 11

- **Filename:** `ai-11-python-for-ai_L16_screen_4.mp4`
- **Target length:** about 27 seconds

**Steps**

1. Add a text cell
2. Type the cleaning log table from content.md: Problem · Action · Rows · Justification
3. Rows: duplicate 1003 dropped; quantity -2 (1004) dropped; missing date (1007) dropped; price 'unknown' (1005) filled with median 4.50; dates converted with to_datetime; quantity 500 (1006) kept and flagged

**Narration over this clip (for pacing)**

> Now Linh writes her cleaning log in a text cell. The duplicate was counted twice by mistake. Minus two is impossible. A missing date cannot be guessed. The unknown price is filled with the median, because prices vary widely. Dates become real dates for the next lesson. And the five hundred unit order is kept and flagged, while she waits for the Lima shop.

## Clip 5: scene 12

- **Filename:** `ai-11-python-for-ai_L16_screen_5.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Add a line under the log: Risk: dropping 1007 removes one of only two returned orders

**Narration over this clip (for pacing)**

> She also notes one cost. Order ten oh seven was one of only two returned orders. So dropping it removes half of the returns. She adds this to the log as a risk.

## Production notes for this lesson

- [VERSION] The date dtype shows as datetime64[us] in pandas 3 and datetime64[ns] in pandas 2. The voiceover says 'a date column' only. The code was tested without warnings in pandas 3.0.6 and 2.2.3 with Python 3.11.
- The order data is synthetic, created for this course; keep the on-screen label 'Synthetic data, made up for this course'. Linh is fictional.
- Printed output on screen must match content.md: '(8, 8) 0'. The cleaning log in the text cell must match the content.md table, including the median fill value 4.50.
- Before the demo, run the L14 data cell on screen (or show it already run) so orders exists.
