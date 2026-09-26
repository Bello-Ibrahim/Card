# Screen Demo Pack: AI-11 L14 Finding Data Quality Problems

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L14_screen_1.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Add a new code cell
2. Paste the data cell from content.md: import io, import pandas as pd, the raw text (order_id,city,order_date,quantity,unit_price,payment,returned,refund and 11 rows), then orders = pd.read_csv(io.StringIO(raw))
3. Press Shift + Enter

**Narration over this clip (for pacing)**

> We paste one cell that holds eleven orders as CSV text, and read it into a DataFrame called orders. We use this same file for the next three lessons.

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L14_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Add a new code cell
2. Type: print(orders.isna().sum()[lambda s: s > 0])
3. Type: print(orders.duplicated().sum())
4. Type: print(orders["city"].unique().tolist())
5. Press Shift + Enter
6. Output: order_date 1 / payment 1 / dtype: int64 / 1 / ['Lagos', 'lagos ', 'Hanoi', 'Lima', 'LIMA', 'Ha Noi']

**Narration over this clip (for pacing)**

> Now three checks. First, missing values. A short extra step keeps only the columns that have at least one. One order date and one payment method are missing. Second, duplicates. There is one copied row. Third, the city spellings. Six different spellings, for only three cities.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L14_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Add a new code cell
2. Type: print(orders.dtypes) and point at unit_price and order_date shown as text
3. Type: bad_price = pd.to_numeric(orders["unit_price"], errors="coerce").isna()
4. Type: print(orders.loc[bad_price, ["order_id", "unit_price"]])
5. Press Shift + Enter
6. Output: 1005 unknown (index 4)

**Narration over this clip (for pacing)**

> Dtypes shows that the price and the date are both stored as text. To find the bad price, we try to convert the column to numbers. Any value that fails becomes missing, and we show those rows. It is order ten oh five, with the price unknown.

## Clip 4: scene 11

- **Filename:** `ai-11-python-for-ai_L14_screen_4.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Type: print(orders["quantity"].describe()[["min", "50%", "max"]])
2. Press Shift + Enter
3. Output: min -2.0 / 50% 2.0 / max 500.0

**Narration over this clip (for pacing)**

> Finally, the quantity. The minimum is minus two, which is impossible. The median is two. And the maximum is five hundred. That is possible, but very unusual.

## Production notes for this lesson

- The order data is synthetic, created for this course; label it on screen as 'Synthetic data, made up for this course'. Prices are in US dollars. Oluwaseun and the marketplace are fictional.
- [VERSION] Text column dtype names (str in pandas 3, object in earlier versions) and printed output formats differ between pandas versions. content.md outputs were produced with Python 3.11 and pandas 3.0.6. The voiceover says 'text' and does not name the dtype.
- Curriculum [VERIFY] flag for Gapminder does not apply: this lesson uses only the synthetic order data.
- Printed outputs on screen must match content.md: 'order_date 1 / payment 1 / dtype: int64', '1', "['Lagos', 'lagos ', 'Hanoi', 'Lima', 'LIMA', 'Ha Noi']", the order 1005 'unknown' row, and 'min -2.0 / 50% 2.0 / max 500.0'.
- Stock footage of market or delivery scenes must show no readable shop names or logos.
