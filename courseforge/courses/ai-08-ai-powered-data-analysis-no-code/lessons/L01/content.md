# L01 What AI Can Do with Your Spreadsheets

Course: AI-08 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
You upload a spreadsheet, type "Which product sold best?", and ten seconds later you get a neat answer with a chart. It feels like magic. But how does the AI get that number, and how do you know it is right?

## Explanation
Some AI assistants, such as Claude and ChatGPT, can analyse files that you upload. The exact feature names, supported file types, size limits and the plans that include file analysis change often, so check the current tool before you rely on them. [VERSION]

When you upload a spreadsheet (for example a .csv or .xlsx file), a typical file-analysis tool does three things:

1. **It reads the data.** It looks at the column names and the first rows to understand what each column contains.
2. **It calculates.** Many tools write and run a small hidden program to sort, filter, add up or count the data. Some tools show this work if you ask; others do not show it by default. [VERSION]
3. **It describes the result in words.** It turns the numbers into sentences, and sometimes into a chart.

This makes AI useful for three kinds of work:

- **Fast summaries:** totals, averages and counts by group in seconds.
- **Formula ideas:** it can suggest Google Sheets formulas when you describe what you need in plain words.
- **Chart suggestions:** it can propose which chart fits your question.

It also fails in predictable ways:

- **Wrong column:** it adds up "Units" when you asked about revenue.
- **Rounding and missing rows:** it rounds early, or it skips rows with blank cells without telling you.
- **Confident but wrong conclusions:** it states a cause or a trend that the data does not support, in a very sure tone.
- **Privacy:** anything you upload leaves your computer. Never upload personal or confidential data unless your organisation has approved the tool for that data. You will learn how to prepare a safe file in L02.

**Analogy:** Think of the AI as a very fast junior analyst on their first week. They produce a summary in minutes, and it is often good. But they do not yet know your business, they sometimes pick the wrong column, and they never say "I am not sure". You would always review their work before sending it to your manager. Treat AI answers in the same way.

## Worked Example
Hiroshi runs a small shop in Osaka that sells handmade soap and candles, online and at a weekend market. He uploads this fictional sales sheet to an AI assistant:

| Month | Product | Channel | Units | Revenue |
|---|---|---|---|---|
| Jan | Soap bar | Online | 120 | 360 |
| Jan | Soap bar | Market | 80 | 240 |
| Jan | Candle | Online | 40 | 320 |
| Jan | Candle | Market | 25 | 200 |
| Feb | Soap bar | Online | 150 | 450 |
| Feb | Soap bar | Market | 70 | 210 |
| Feb | Candle | Online | 45 | 360 |
| Feb | Candle | Market | 30 | 240 |

He asks: "What was total revenue by channel?" The AI answers: Online 1,490 and Market 890, so online brought in about 63% of revenue.

Hiroshi checks one number in Google Sheets. He types `=SUMIF(C2:C9, "Online", E2:E9)` and gets 1,490. The answer matches.

Then he asks: "Which product is more popular?" The AI says: "Soap bars are much more popular, with 420 units against 140 candles." That is true for units. But by revenue the two products are close: soap bars 1,260 and candles 1,120. "Popular" was a vague word, and the AI chose units without saying so. Hiroshi learns to name the column he means.

## Common Mistake
Many beginners think that because the AI "runs code", its numbers must be correct. The calculation may be correct for the question the AI understood, but the AI may have understood a different question. It may use the wrong column, skip blank rows or read a number stored as text as zero. Always check at least one number by hand, and always ask which columns the AI used.

## Key Takeaways
1. AI file-analysis tools read your data, run hidden calculations and describe the results in words and charts.
2. They are fast at summaries, formula ideas and chart suggestions, but they can use the wrong column, skip rows and state confident but wrong conclusions.
3. Treat the AI like a fast junior analyst: check at least one number by hand, and never upload personal or confidential data to a tool your organisation has not approved.

## Hands-on Exercise
**Task:** Upload the sample sales dataset to an AI assistant, ask 3 questions, and check one answer by hand in Google Sheets.
**Tools:** Google Sheets (free); Claude or ChatGPT with file analysis (a free plan may have limits on uploads). [VERSION]
**Steps:**
1. Copy the table from the Worked Example into a new Google Sheet, with the headers in row 1. The data is fictional, so it is safe to upload.
2. Download it as a .csv file (File > Download > Comma-separated values). [VERSION]
3. Upload the file to Claude or ChatGPT and ask: "What was total revenue by month?", "Which channel sold more candles?" and "What share of revenue came from soap bars?"
4. For each answer, write down the number and the columns the AI says it used. If it does not say, ask it.
5. Choose one answer and check it with a formula in Google Sheets, for example `=SUMIF(A2:A9, "Feb", E2:E9)`.
6. Write one sentence: did the AI match your check? If not, what went wrong?
**What good looks like:** Correct answers are: January 1,120 and February 1,260; the Online channel sold more candles (85 against 55); soap bars brought in 1,260 of 2,380, about 53%. Your note shows one formula check and says clearly whether it matched.
**Time:** about 20 minutes

## Review Flags
- [VERSION] File-analysis features in Claude and ChatGPT (feature names, supported file types, size limits, whether the hidden calculation is shown, and which free or paid plans include uploads) must be checked against the live tools before scripting.
- [VERSION] The Google Sheets menu path File > Download > Comma-separated values must be checked against the current interface.
