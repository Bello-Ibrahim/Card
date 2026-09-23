# L15 Capstone Step 2: Usage Logging and a Cost Dashboard | Presenter Script

Course: AI-14 · Video: 5 min · Words: 692

## Hook
Your app works, and people are starting to use it. How much did it cost yesterday? Which feature is the most expensive? How many requests failed? If you cannot answer in ten seconds, you are not ready for production.

## Explain
In capstone step one, you built your core feature. Step two adds two things. A log of every API call, and a dashboard page that turns the log into numbers you can act on.

For every call, log the time, the feature name and the model. Log the input, output and cache tokens, and the latency. Add the estimated cost, using your price constants from lesson four. And log the stop reason, and the error type if the call failed. Do not log prompts or outputs with personal data. For cost monitoring, you need numbers, not content.

SQLite is a file-based database that comes with Python, so it needs no server. A CSV file also works. On free hosting plans, local files may be lost when the app restarts, so treat the log as short-term, or move to a small hosted database later.

The dashboard shows cost per day as a chart, the average cost per request, overall and per feature, the request count and the error rate. And it shows an alert when this month's spend passes a share of your budget, for example eighty percent. Remember, this is your own estimate. The Console's usage pages show the real charges, so compare the two now and then.

A cost dashboard is like the fuel gauge in a car. You could wait for your bank statement at the end of the month, but by then the fuel is gone. The gauge tells you while you can still change how you drive.

## Demonstrate
Chidi Okafor builds a meal planner for a grocery app in Lagos, Nigeria. It has two features, a weekly plan and a single recipe. Every API call in his app, including streamed calls and tool loops, goes through one logging function.

It creates a calls table in SQLite. Then it wraps the API call. On success, it records the model, tokens, estimated cost and stop reason. On failure, it records the error type. The insert happens in a finally block, so every call is saved, whether it succeeds or fails.

His dashboard is a second Streamlit page. It reads the table, groups it by date, and draws cost per day as a line chart. Three metric boxes show cost this month, average cost per request and error rate. A table shows cost per feature.

Then the alert. When the monthly total passes eighty percent of his budget constant, a warning appears at the top of the page. He tests it by setting a very small budget, reloads the page, and the warning is there. Then he sets the real budget back.

After a day of testing, you'll see something like this. A hundred and forty-two requests and three errors. He notices that the weekly plan feature uses about four times more output tokens than the single recipe feature. So he lowers its max tokens, after checking quality on his evaluation set.

A common mistake is to log only successful calls, because the log line comes after the API call. Then the error rate always looks like zero. Log in a finally block, and log streamed calls from the final message. And remember to compare your total with the real usage in the Console.

## Recap
Let's recap. First, log every call, including failures, with the time, feature, model, tokens, latency, estimated cost, stop reason and error. Second, your dashboard shows cost per day, cost per request, error rate and an alert near your budget limit. Third, the dashboard is an estimate, so compare it with the Console's real usage pages, and never log personal data.

## CTA
Now it is your turn. This is capstone step two. Add usage logging and a cost dashboard page to your app, make at least twenty test calls, including two that fail on purpose, and test your budget alert. In the next lesson, Capstone Step Three: Test, Deploy and Present, you will ship it. See you there.

## Thumbnail
Headline: Know What It Costs
Image: Navy background, a dashboard with a cost-per-day line chart, three metric tiles and an amber budget alert, headline in teal Inter Bold.

## Production Notes
- [VERSION] Prices used for estimates, Streamlit functions (st.line_chart, st.metric, st.warning, multipage apps), file persistence on free hosting plans and the Console usage pages must be checked at recording time.
- The dashboard numbers (142 requests, 3 errors, 2.1% error rate, weekly plan using four times more output tokens) are illustrative: label them 'example' on screen. Cost values must come from placeholder prices, not real ones.
- Chidi Okafor and the Lagos grocery app are fictional; the usage log contains numbers only, no prompts or personal data.
