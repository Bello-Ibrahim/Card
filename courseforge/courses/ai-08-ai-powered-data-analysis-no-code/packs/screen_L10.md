# Screen Demo Pack: AI-08 L10 A Simple Dashboard in Looker Studio

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L10_screen_1.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Open Looker Studio and choose Create > Report
2. In Add data to report, choose the Google Sheets connector
3. Select the orders spreadsheet and its worksheet
4. Keep 'Use first row as headers' ticked; click Add

**Narration over this clip (for pacing)**

> He opens Looker Studio and creates a new report. He chooses the Google Sheets connector, selects the spreadsheet and the worksheet, keeps the first row as headers, and adds it.

## Clip 2: scene 10

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L10_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open the data source fields; confirm Order Date is Date type and Revenue is Number (change if needed)
2. Add a scorecard with Revenue (SUM): 3,450
3. Add a second scorecard with Record Count: 10

**Narration over this clip (for pacing)**

> He checks the fields. Order date must be a date, and revenue must be a number. Then he adds two scorecards. Revenue shows three thousand four hundred and fifty, and the record count shows ten orders.

## Clip 3: scene 11

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L10_screen_3.mp4`
- **Target length:** about 27 seconds

**Steps**

1. In Claude or ChatGPT type: 'Write a Looker Studio calculated field for average revenue per order, from fields Revenue and Order ID.'
2. Show the reply: SUM(Revenue) / COUNT(Order ID)
3. In Looker Studio, add a calculated field with this formula
4. Add a third scorecard with the new field: 345
5. Overlay the hand check: 3,450 ÷ 10 = 345 ✓

**Narration over this clip (for pacing)**

> Next, he asks the AI for a Looker Studio calculated field for average revenue per order. It suggests the sum of revenue divided by the count of order IDs. He adds it as a third scorecard, which shows three hundred and forty-five. He checks by hand. Three thousand four hundred and fifty divided by ten is three hundred and forty-five.

## Clip 4: scene 12

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L10_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Add a time series chart
2. Set the dimension to Order Date, granularity Month
3. Set the metric to Revenue
4. Hover each point: 470, 820, 2,160

**Narration over this clip (for pacing)**

> Now the charts. First, a time series chart, with order date set to month, and revenue as the metric. It shows four hundred and seventy, eight hundred and twenty, and two thousand one hundred and sixty.

## Clip 5: scene 13

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L10_screen_5.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Add a bar chart
2. Dimension: Region; metric: Revenue; sort descending
3. Hover each bar: South 2,220, North 680, West 550

**Narration over this clip (for pacing)**

> Then a bar chart with region and revenue, sorted from largest. South is two thousand two hundred and twenty, North six hundred and eighty, and West five hundred and fifty.

## Clip 6: scene 14

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L10_screen_6.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Add a date range control and drag it to the top right
2. Switch to View mode
3. Set the range to 1–28 February 2026
4. Zoom on the Revenue scorecard: 820

**Narration over this clip (for pacing)**

> He adds a date range control in the top right, and tests it. He chooses February twenty twenty-six only, and total revenue changes to eight hundred and twenty.

## Clip 7: scene 15

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L10_screen_7.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Add a text box at the top: 'Orders dashboard, January to March 2026'
2. Click Share
3. Enter the placeholder address owner@example.com
4. Set the role to Viewer and send

**Narration over this clip (for pacing)**

> Finally, he types the title, orders dashboard, January to March twenty twenty-six. He clicks share, adds the owner's email address, and chooses viewer.

## Production notes for this lesson

- Screen demo lesson: record in Looker Studio with a free Google account, connected to the fictional clean orders sheet from content.md (headers in row 1, no merged cells, real dates in Order Date).
- [VERSION] Looker Studio interface, connectors and sharing settings must be checked against the live tool before recording: Create > Report, the Google Sheets connector options ('Use first row as headers'), field types, scorecard and chart names, Record Count, calculated field syntax (SUM(Revenue) / COUNT(Order ID)), the date range control, and the Share and Viewer options.
- [VERIFY] How data source credentials (owner's or viewer's) affect what viewers can see, and the current default. The narration says only 'check the data source settings before you share'; it does not state the credential behaviour as fact.
- Omar and the Amman setting are fictional. Spoken numbers match content.md: scorecards 3,450 and 10; calculated field 345 (3,450 ÷ 10); months 470, 820, 2,160; regions South 2,220, North 680, West 550; February filter 820.
- Scene 15: use a placeholder email address such as owner@example.com, never a real one.
