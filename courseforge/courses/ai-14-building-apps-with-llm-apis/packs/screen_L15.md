# Screen Demo Pack: AI-14 L15 Capstone Step 2: Usage Logging and a Cost Dashboard

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-14-building-apps-with-llm-apis_L15_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Open usage.py in VS Code
2. Highlight the CREATE TABLE statement for calls
3. Highlight the success row with tokens, estimate_cost and stop_reason
4. Highlight the except anthropic.APIError branch that stores type(e).__name__
5. Highlight the finally block with the INSERT and commit

**Narration over this clip (for pacing)**

> It creates a calls table in SQLite. Then it wraps the API call. On success, it records the model, tokens, estimated cost and stop reason. On failure, it records the error type. The insert happens in a finally block, so every call is saved, whether it succeeds or fails.

## Clip 2: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L15_screen_2.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Open pages/dashboard.py
2. Highlight pandas.read_sql("SELECT * FROM calls", db)
3. Highlight the group-by-date and st.line_chart
4. Highlight the three st.metric boxes
5. Highlight the cost-per-feature table

**Narration over this clip (for pacing)**

> His dashboard is a second Streamlit page. It reads the table, groups it by date, and draws cost per day as a line chart. Three metric boxes show cost this month, average cost per request and error rate. A table shows cost per feature.

## Clip 3: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L15_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Highlight MONTHLY_BUDGET and the st.warning for spend above 80%
2. Set MONTHLY_BUDGET to a very small value and reload the page
3. Show the warning 'Spend is above 80% of the monthly budget'

**Narration over this clip (for pacing)**

> Then the alert. When the monthly total passes eighty percent of his budget constant, a warning appears at the top of the page. He tests it by setting a very small budget, reloads the page, and the warning is there. Then he sets the real budget back.

## Clip 4: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L15_screen_4.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Run streamlit run app.py and open the dashboard page
2. Show the metrics: 142 requests, 3 errors, 2.1% error rate (example numbers)
3. Point to the cost-per-feature table: weekly plan much higher than single recipe
4. Lower max_tokens for weekly plan and show the eval run still passing (example output)

**Narration over this clip (for pacing)**

> After a day of testing, you'll see something like this. A hundred and forty-two requests and three errors. He notices that the weekly plan feature uses about four times more output tokens than the single recipe feature. So he lowers its max tokens, after checking quality on his evaluation set.

## Production notes for this lesson

- [VERSION] Prices used for estimates, Streamlit functions (st.line_chart, st.metric, st.warning, multipage apps), file persistence on free hosting plans and the Console usage pages must be checked at recording time.
- The dashboard numbers (142 requests, 3 errors, 2.1% error rate, weekly plan using four times more output tokens) are illustrative: label them 'example' on screen. Cost values must come from placeholder prices, not real ones.
- Chidi Okafor and the Lagos grocery app are fictional; the usage log contains numbers only, no prompts or personal data.
