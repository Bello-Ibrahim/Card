# Screen Demo Pack: AI-11 L18 Building an ML-Ready Table

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L18_screen_1.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Run the L14, L16 and L17 cells so encoded exists
2. Add a new code cell
3. Type: print(encoded[["returned", "refund"]].head(3))
4. Press Shift + Enter
5. Output: no 0.0 / yes 12.0 / no 0.0
6. Highlight the yes / 12.0 row

**Narration over this clip (for pacing)**

> First, she looks at the returned and refund columns side by side. See the pattern? The refund is above zero only when the order was returned. That is leakage.

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L18_screen_2.mp4`
- **Target length:** about 26 seconds

**Steps**

1. Add a new code cell
2. Type: ml = encoded.copy()
3. Type: ml["returned"] = (ml["returned"] == "yes").astype(int)
4. Type: ml = ml.drop(columns=["order_id", "refund", "order_date"])
5. Type: print(ml.shape) and print(ml.columns.tolist())

**Narration over this clip (for pacing)**

> Next, she makes a copy called ml. The target, returned, becomes one for yes and zero for no. The comparison with yes gives True or False, and as type int turns that into one or zero. Then she drops three columns. The order number, which is an identifier. The refund, which leaks. And the order date, which is already converted.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L18_screen_3.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Press Shift + Enter
2. Output: (8, 11)
3. Output: ['quantity', 'unit_price', 'returned', 'month', 'weekday', 'city_hanoi', 'city_lagos', 'city_lima', 'payment_card', 'payment_cash', 'payment_other']

**Narration over this clip (for pacing)**

> Run it. Eight rows and eleven columns. The target, plus quantity, price, month, weekday, three city columns and three payment columns.

## Clip 4: scene 11

- **Filename:** `ai-11-python-for-ai_L18_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Add a new code cell
2. Type: print(ml.select_dtypes("number").shape[1] == ml.shape[1])
3. Type: ml.to_csv("orders_ml_ready.csv", index=False)
4. Press Shift + Enter
5. Output: True
6. Open the Colab file panel and show orders_ml_ready.csv

**Narration over this clip (for pacing)**

> She checks that every column is numeric. The answer is True. Then she saves the table as a CSV file. Index equals False stops pandas from writing the row labels as an extra column.

## Production notes for this lesson

- [VERSION] The Colab file panel and its download option must be checked against the live interface before recording.
- Judgement call (curriculum): the course ends at an ML-ready table; train/test splits, scaling and modelling are left to AI-12. The voiceover names the next course only as 'the next course, Machine Learning with scikit-learn'.
- The order data is synthetic, created for this course. Anjali (Pune) is fictional.
- Printed outputs on screen must match content.md: the returned / refund head(3) table (no 0.0 / yes 12.0 / no 0.0), '(8, 11)', the 11-column list, and 'True'.
- Before the demo, run the L14, L16 and L17 cells on screen (or show them already run) so encoded exists.
