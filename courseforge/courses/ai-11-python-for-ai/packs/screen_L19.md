# Screen Demo Pack: AI-11 L19 Capstone Step 1: Choose, Load and Audit a Public Dataset

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L19_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Create a new Colab notebook named: Capstone - cereal yield
2. Add five text cells with the headings: 1 Question · 2 Source · 3 Load · 4 Audit · 5 Cleaning log
3. Under Source, type placeholders: Name · Web address · Download date · Licence

**Narration over this clip (for pacing)**

> He creates a new notebook and adds five text headings, in order. Question, Source, Load, Audit, and Cleaning log. The cleaning log stays empty until the next lesson. Under Source, he records the name, the web address, the download date and the licence.

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L19_screen_2.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Open the Colab file panel and upload the downloaded CSV
2. Under Load, type: df = pd.read_csv("file_name.csv")
3. Type: df.head() and df.info() in separate cells

**Narration over this clip (for pacing)**

> Then he uploads the downloaded file with the Colab file panel, loads it with read csv, and takes a first look with head and info.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L19_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Under Audit, add a code cell
2. Type: def audit(df):
3. Type (indented): """Print a short data-quality report for a DataFrame."""
4. Type (indented): print("Shape:", df.shape) / print("Duplicate rows:", df.duplicated().sum())
5. Type (indented): print("Missing values:") / print(df.isna().sum()[lambda s: s > 0])
6. Type (indented): print("Text columns:", df.select_dtypes(exclude="number").columns.tolist())

**Narration over this clip (for pacing)**

> Next, he writes a reusable audit function, so he can run the same checks again after cleaning. It prints the shape, the number of duplicate rows, the missing values in each column that has some, and the list of text columns.

## Clip 4: scene 11

- **Filename:** `ai-11-python-for-ai_L19_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run the L14 data cell
2. Type: audit(orders)
3. Press Shift + Enter
4. Output: Shape: (11, 8) / Duplicate rows: 1 / Missing values: order_date 1, payment 1 / Text columns: ['city', 'order_date', 'unit_price', 'payment', 'returned']

**Narration over this clip (for pacing)**

> To show that it works, we test it on the synthetic order data from lesson fourteen. Eleven rows, one duplicate, a missing date and payment, and five text columns. Exactly what we found by hand.

## Clip 5: scene 12

- **Filename:** `ai-11-python-for-ai_L19_screen_5.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Type: audit(df), then df.describe()
2. Type: df["category_column"].unique() for each category column
3. Plot a histogram of the main number column
4. In the Audit text cell, list each problem marked 'error' or 'needs a decision'

**Narration over this clip (for pacing)**

> On his real data, Yusuf runs the audit, then describe, unique on the category columns, and a quick histogram. He writes each problem in the Audit section, marked as an error or needing a decision.

## Production notes for this lesson

- [VERIFY] Licence terms of World Bank Open Data, Our World in Data, the UCI Machine Learning Repository and Kaggle datasets (Kaggle licences vary per dataset, and Kaggle needs a free account). The voiceover names the four sources only as places to browse and tells learners to check each licence on the dataset's own page; it makes no claim about any licence.
- [VERSION] Uploading files through the Colab file panel must be checked against the live interface before recording.
- Yusuf's question is hypothetical; no dataset or result is claimed. Screen scenes use a placeholder file name (file_name.csv) and do not show a real dataset's contents or findings. If the team wants to show a real file, pick one whose licence has been checked and add it to these notes.
- The audit function demo runs on the synthetic order data from L14. Printed output must match content.md: 'Shape: (11, 8) / Duplicate rows: 1 / Missing values: / order_date 1 / payment 1 / dtype: int64 / Text columns: ['city', 'order_date', 'unit_price', 'payment', 'returned']'.
- Stock footage of farms or fields must show no readable brand names or logos.
