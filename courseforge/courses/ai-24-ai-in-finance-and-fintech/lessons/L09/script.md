# L09 AI for Financial Analysis and Reporting | Presenter Script

Course: AI-24 · Video: 5 min · Words: 687

## Hook
It is the last day of the quarter-end close. You have a profit-and-loss sheet, a budget, and two hours to write the management commentary. An AI assistant can write a first draft in thirty seconds. Can you trust the numbers in it?

## Explain
Last time, we tested an assistant that talks to customers. Today we look inside the finance team. AI assistants are useful for tasks built around text and structure.

They can summarise long documents, such as board packs or audit reports. They can explain variances between actual results and budget in clear sentences. They can draft commentary for management reports in a set format. And they can check whether the commentary and the tables tell the same story.

But language models are built to produce fluent text, not to calculate. They can invent numbers that are not in the source. They can misread numbers, for example reading thousands as millions. They can calculate percentages wrongly. And they can give a convincing but wrong reason for a variance.

So the rule in this course is simple. Every figure in AI-drafted commentary is checked against the source before it leaves the team.

Where possible, calculate the variances yourself in the spreadsheet first, and give the AI the calculated table. Then its only job is to write the words, which is what it does best. Also, never paste confidential results or customer data into a public AI tool. And keep commentary factual. It must not turn into investment advice or a forecast presented as fact.

Think of an AI assistant as a fast, eager junior analyst. The junior can produce a well-written draft in minutes, and the draft is often useful. But no experienced manager sends a junior's work to the board without checking every number.

## Demonstrate
Arjun Mehta is a finance analyst at Kaveri Home Appliances, a synthetic company in India. He gives an AI assistant the quarterly profit-and-loss summary, in thousands of rupees, and asks for variance commentary against budget. Revenue was budgeted at twelve thousand, and came in at eleven thousand four hundred.

The AI's draft says revenue fell six percent below budget, gross margin improved thanks to lower costs, and operating profit was six hundred and eighteen below budget, mainly because of higher operating expenses.

Arjun checks each figure. Revenue fell six percent is wrong. Six hundred on twelve thousand is five percent. Gross margin improved is also wrong. It was forty percent in the budget and thirty-eight percent in the actual results, because costs fell less than revenue.

Six hundred and eighteen below budget is correct, but the reason is wrong. Lower gross profit explains four hundred and sixty-eight of it. Higher operating expenses explain only one hundred and fifty.

So Arjun rewrites the commentary. Revenue was five percent below budget. Gross margin fell from forty percent to thirty-eight percent, so gross profit was four hundred and sixty-eight below budget. Operating expenses were one hundred and fifty above budget. Together, operating profit was six hundred and eighteen, or thirty-four point three percent, below budget.

A common mistake is to check only the numbers you expect to be wrong, or only the first paragraph. Errors often hide in the reasons and comparisons, not only in the raw figures. Check every number, and every because.

## Recap
Let's recap. First, AI assistants are good at summarising, explaining variances and drafting commentary in a set format. Second, language models can invent, misread or miscalculate numbers, and give convincing but wrong reasons, so every figure and every reason must be checked against the source. Third, calculate variances in the spreadsheet first, use only synthetic or approved data, and keep commentary factual, with no investment advice.

## CTA
Now it is your turn. In the exercise below this video, you will give a free AI assistant the synthetic quarterly profit-and-loss sheet and ask for variance commentary. Then check every number against the sheet, and correct any errors. It takes about thirty minutes. In the next lesson, we look at explainability, and the question, why was I declined? See you there.

## Thumbnail
Headline: Check Every Number
Image: Navy background, a profit-and-loss table with one AI-drafted sentence underlined and a red correction mark beside '6%', headline in teal Inter Bold.

## Production Notes
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
- Kaveri Home Appliances and Arjun Mehta are synthetic and fictional. Figures are in thousands of rupees and must match content.md exactly (revenue 12,000 vs 11,400; gross margin 40.0% vs 38.0%; gross profit −468; operating expenses +150; operating profit −618, −34.3%).
- No forecasts or investment advice on screen or in captions; the commentary describes past results only.
- Scene 11 hero clip is about 7 seconds and the scene is about 20 seconds: hold the clip with a slow push-in, then cut to scene 12.
