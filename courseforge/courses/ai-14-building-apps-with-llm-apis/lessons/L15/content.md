# L15 Capstone Step 2: Usage Logging and a Cost Dashboard

Course: AI-14 · Module: M4 · Objectives: O6, O7 · Video: 5 min (screen demo)

## Hook
Your app works, and people are starting to use it. How much did it cost yesterday? Which feature is the most expensive? How many requests failed? If you cannot answer in ten seconds, you are not ready for production.

## Explanation
Step 2 adds two things: a **log** of every API call, and a **dashboard page** that turns the log into numbers you can act on.

**What to log for every call:**

- time (in UTC), feature name and model
- input tokens, output tokens and any cache tokens
- latency in milliseconds (and time to first token for streamed calls)
- estimated cost, using your price constants from L04 [VERSION]
- stop reason, and the error class if the call failed

Do not log prompts or outputs that contain personal data. For cost monitoring, you need numbers, not content.

**Where to store it.** **SQLite** is a file-based database that comes with Python, so it needs no server. A CSV file also works for a small app. On free hosting plans, local files may be lost when the app restarts, so treat the log as short-term, or use a small hosted database later. [VERSION]

**What to show on the dashboard:**

- cost per day, as a chart
- average cost per request, overall and per feature
- request count and error rate (failed calls ÷ all calls)
- an **alert** when this month's spend passes a share of your budget, for example 80%

The dashboard shows your own estimate. The Console's usage and billing pages show the real charges, so compare the two now and then. [VERSION]

**Analogy:** A cost dashboard is like the fuel gauge and trip computer in a car. You could drive without them and check your bank statement at the end of the month, but by then the fuel is already used. The gauge tells you while you can still change how you drive.

## Worked Example
Chidi Okafor builds a meal planner for a grocery app in Lagos, Nigeria. He wraps every API call in one function that logs to SQLite:

```python
import sqlite3, time
from datetime import datetime, timezone

db = sqlite3.connect("usage.db", check_same_thread=False)
db.execute("""CREATE TABLE IF NOT EXISTS calls (ts TEXT, feature TEXT,
    model TEXT, tokens_in INT, tokens_out INT, latency_ms INT,
    cost REAL, stop_reason TEXT, error TEXT)""")

def logged_call(feature, **params):
    start = time.perf_counter()
    row = (feature, params["model"], 0, 0, 0.0, None, "UnknownError")
    try:
        r = client.messages.create(**params)
        row = (feature, r.model, r.usage.input_tokens, r.usage.output_tokens,
               estimate_cost(r.usage), r.stop_reason, None)
        return r
    except anthropic.APIError as e:
        row = (feature, params["model"], 0, 0, 0.0, None, type(e).__name__)
        raise
    finally:
        ms = int((time.perf_counter() - start) * 1000)
        ts = datetime.now(timezone.utc).isoformat()
        db.execute("INSERT INTO calls VALUES (?,?,?,?,?,?,?,?,?)",
                   (ts, *row[:4], ms, *row[4:]))
        db.commit()
```

His dashboard is a second Streamlit page, `pages/dashboard.py`. On screen he:

1. Reads the table with `pandas.read_sql("SELECT * FROM calls", db)`.
2. Groups by date and shows cost per day with `st.line_chart`. [VERSION]
3. Shows three `st.metric` boxes: cost this month, average cost per request and error rate. [VERSION]
4. Shows `st.warning("Spend is above 80% of the monthly budget")` when the monthly total passes 80% of his `MONTHLY_BUDGET` constant.
5. Adds a table of cost per feature.

Example output after a day of testing: 142 requests, 3 errors (2.1%), average cost per request shown to four decimal places. He sees that the "weekly plan" feature uses four times more output tokens than "single recipe", and lowers its max_tokens after checking quality on his eval set.

## Common Mistake
Many developers log only successful calls, because the logging line comes after the API call. Failed calls then disappear, and the error rate always looks like zero. Log in a `finally` block, so every call is recorded, whether it succeeds or fails. Also log streamed calls from the final message, not from the text pieces.

## Key Takeaways
1. Log every call, including failures: time, feature, model, tokens, latency, estimated cost, stop reason and error.
2. A dashboard should show cost per day, cost per request, error rate and an alert near your budget limit.
3. Your dashboard is an estimate; compare it with the Console's real usage pages, and never log personal data.

## Hands-on Exercise
**Task:** Capstone step 2: add usage logging and a cost dashboard page to your app.
**Tools:** Python with `sqlite3` (built in), `pandas` and `streamlit`; your capstone app from L14; your price constants from L04. [VERSION]
**Steps:**
1. Create a `calls` table in SQLite (or a CSV file) with all the fields listed in the Explanation.
2. Route every API call in your app through one logging function, including streamed calls and tool loops.
3. Make at least 20 test calls, including 2 that fail on purpose (for example, a max_tokens value that is too small).
4. Create a dashboard page with cost per day, average cost per request, error rate and cost per feature.
5. Add a monthly budget constant and an alert at 80% of it. Test the alert by setting a very small budget.
6. Compare your estimated total with the Console usage page, and note any difference. [VERSION]
**What good looks like:** Every call appears in the log, including failures; the dashboard shows the four measures correctly; the alert appears when you lower the budget; and no prompts or personal data are stored.
**Time:** about 75 minutes

## Review Flags
- [VERSION] Prices used for estimates, Streamlit functions (`st.line_chart`, `st.metric`, `st.warning`, multipage apps), file persistence on free hosting plans and the Console usage pages must be checked at recording time.
- The numbers in the worked example are illustrative.
