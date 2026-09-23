# L06 Asking Good Questions of Your Data | Presenter Script

Course: AI-08 · Video: 5 min · Words: 715

## Hook
Two people upload the same file to one AI tool. One gets a vague paragraph that could fit any business. The other gets a clear table with exact numbers and a note on how they were calculated. The difference is not the tool. It is the prompt.

## Explain
Last week, you prepared clean, safe data. This week, we analyse it, and that starts with the prompt.

In lesson three, you turned a business question into a measurable data question. Now you put that question into a prompt. A strong analysis prompt has four parts. First, describe the dataset. For example, this file has ten orders from January to March twenty twenty-six, one row per order. Second, name the columns. Revenue is in column G, in US dollars.

Third, state the question, with the measure, group, period and comparison. What was total revenue per region for January to March? Fourth, ask for the method. Show the table first. Then tell me how many rows and which columns you used, and how you calculated each number.

Asking for a table first, and conclusions second, is important. A table is easy to check against your own data. A paragraph of conclusions is easy to believe, and hard to check.

Asking for the method helps you spot problems early. If the AI says it used nine rows, and your sheet has ten, you know something is wrong before you read any conclusion. And keep one question per prompt when you start. Long prompts with five questions often skip or mix up one part.

And remember the safety rule from lesson two. Upload only anonymised or fictional data, or data your organisation has approved for the tool.

Asking AI about your data is like ordering at a busy counter. Something to eat, please, gets you whatever is easiest to serve. One vegetable soup, small, no bread, and the receipt, gets you exactly what you wanted, plus proof of what you paid for.

## Demonstrate
Sofia is an operations analyst for a courier company in Mexico City. She uploads a fictional, anonymised file of deliveries. The columns are delivery ID, date, zone, promised minutes and actual minutes.

Her first prompt is short. Are our deliveries late? The AI answers with a general paragraph. Some deliveries appear to be delayed, especially at busy times. It suggests that she monitor performance. There are no numbers she can use.

So she writes a second prompt. This file has one row per delivery for March twenty twenty-six. A delivery is late when actual minutes minus promised minutes is more than ten. For each zone, count the deliveries and the late deliveries, and give the percentage late.

Show the table first. Then tell me how many rows you used, and how you calculated each column. Conclusion in two sentences maximum.

This time, the AI gives a table with one row per zone, and the three numbers she asked for. It notes that it used all the rows in the file, and it shows the formula it used for late. The conclusion names the zone with the highest percentage late.

Sofia still checks. She counts the rows in her own sheet with a COUNTA formula, and she recalculates the percentage for one zone. Both match, so she can use the table in her weekly report.

A common mistake is to ask for insights or interesting patterns, and accept whatever comes back. The AI then chooses the measure, the group and the period for you, often without saying so. Ask your own measurable question, and ask for the table and the method before the conclusion.

## Recap
Let's recap. First, a strong analysis prompt describes the dataset, names the columns, states a measurable question, and asks for the method. Second, ask for a table first and conclusions second, because tables are easier to check than sentences. Third, check the row count and columns the AI reports against your own sheet, before you trust the conclusion.

## CTA
Now it is your turn. In the exercise below this video, you will upload the clean orders sheet and ask three questions, using the four-part prompt. For each answer, note whether the AI showed its method. It takes about twenty-five minutes. In the next lesson, we build summaries and pivot tables. See you there.

## Thumbnail
Headline: Same File, Better Prompt
Image: Navy background, two chat windows side by side: a grey vague paragraph on the left, a crisp teal table with a method note on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] File upload and analysis features in Claude and ChatGPT, including free plan limits, must be checked against the live tools before recording.
- Sofia, the Mexico City courier company and the deliveries file are fictional and anonymised. content.md gives no zone results, so the video shows a placeholder table with zone names only and no late percentages; do not invent figures on screen.
- Scene 11 and 12 slides show Sofia's second prompt word for word as in content.md. Scene 14 slide shows the check formula =COUNTA(A2:A5000) on screen, not read aloud.
- Stock footage of couriers must show no company names or logos.
