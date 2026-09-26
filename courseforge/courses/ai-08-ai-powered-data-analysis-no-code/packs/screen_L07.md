# Screen Demo Pack: AI-08 L07 Summaries and Pivot Tables

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L07_screen_1.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Click cell C3 in the orders data
2. Open Insert > Pivot table
3. Select New sheet
4. Click Create; the empty pivot table and editor appear

**Narration over this clip (for pacing)**

> He clicks any cell in the data, and chooses insert, pivot table. He selects a new sheet, and clicks create.

## Clip 2: scene 10

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L07_screen_2.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Next to Rows, click Add and choose Region
2. Next to Values, click Add and choose Revenue
3. Zoom on 'Summarise by: SUM'
4. Highlight the result: North 680, South 2,220, West 550, Grand total 3,450

**Narration over this clip (for pacing)**

> In the editor, he adds region to rows. Then he adds revenue to values, and checks that it is summarised by sum. The result is North six hundred and eighty, South two thousand two hundred and twenty, and West five hundred and fifty. The grand total is three thousand four hundred and fifty.

## Clip 3: scene 11

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L07_screen_3.mp4`
- **Target length:** about 26 seconds

**Steps**

1. Add Revenue to Values a second time; change Summarise by to COUNTA
2. Add Revenue to Values a third time; change Summarise by to AVERAGE
3. Highlight row by row: North 4 / 170, South 3 / 740, West 3 / 183.33

**Narration over this clip (for pacing)**

> Next, he adds revenue to values two more times, once as a count of orders, and once as an average. North has four orders, with an average of one hundred and seventy. South has three orders, with an average of seven hundred and forty. West has three orders, with an average of one hundred and eighty-three point three three.

## Clip 4: scene 12

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L07_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Return to the data, Insert > Pivot table > New sheet > Create
2. Rows: Add > Month
3. Values: Add > Revenue (SUM)
4. Highlight 2026-01 470, 2026-02 820, 2026-03 2,160

**Narration over this clip (for pacing)**

> Then he builds a second pivot table, with month in rows and the sum of revenue. January is four hundred and seventy, February eight hundred and twenty, and March two thousand one hundred and sixty.

## Clip 5: scene 13

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L07_screen_5.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Download the sheet as .csv
2. In Claude or ChatGPT, upload the file
3. Type: 'Show total, count and average Revenue per Region in a table, and tell me how many rows you used.'

**Narration over this clip (for pacing)**

> He uploads the same sheet to the AI tool. He asks for total, count and average revenue per region in a table, and the number of rows it used.

## Clip 6: scene 14

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L07_screen_6.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Show the AI table: South total 420, 2 orders
2. Split screen with the pivot table: South 2,220, 3 orders; circle both South rows in red
3. Type in the chat: 'Which rows did you use for South?'

**Narration over this clip (for pacing)**

> The AI's table shows South with a total of four hundred and twenty, and only two orders. The pivot table shows two thousand two hundred and twenty, and three orders. So he asks the AI which rows it used.

## Clip 7: scene 15

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L07_screen_7.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Show the AI reply naming order 1008 as skipped
2. Open the exported file and zoom on "1,800" in quotation marks for order 1008
3. Fix the value to 1800, re-export and re-upload
4. Show the new AI table: South 2,220, 3 orders, with green ticks beside the pivot table

**Narration over this clip (for pacing)**

> It had read the revenue of order ten oh eight as text, because his exported file still had one thousand eight hundred in quotation marks. So it left that row out. He fixes the source file, and the numbers match.

## Production notes for this lesson

- Screen demo lesson: record in Google Sheets and in Claude or ChatGPT with the fictional clean orders sheet from content.md, including the Month column (H) from L05.
- [VERSION] Google Sheets pivot table steps (Insert > Pivot table, New sheet, the Rows and Values Add buttons, and the 'Summarise by' options including COUNTA) must be checked against the current interface before recording.
- [VERSION] File-analysis features in Claude and ChatGPT must be checked against the live tools before recording.
- To reproduce the AI mismatch in scene 13, export a copy of the file in which order 1008's revenue is stored as the text "1,800" in quotation marks, as content.md describes. If the live AI reads it correctly anyway, show the mismatch from a prepared screenshot and label it 'example'.
- Tomasz and the Kraków setting are fictional. Spoken numbers match content.md: North 680 / 4 orders / average 170; South 2,220 / 3 / 740; West 550 / 3 / 183.33; total 3,450; months 470, 820, 2,160; AI table South 420 with 2 orders.
