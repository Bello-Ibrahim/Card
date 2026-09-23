# L01 What AI Can Do with Your Spreadsheets | Presenter Script

Course: AI-08 · Video: 5 min · Words: 739

## Hook
You upload a spreadsheet and type, which product sold best? Ten seconds later, you get a neat answer with a chart. It feels like magic. But how does the AI get that number? And how do you know it is right?

## Explain
Hi, and welcome to AI-Powered Data Analysis, No Code. In this first lesson, we look at what AI can do with your spreadsheets, and where it goes wrong.

Some AI assistants, such as Claude and ChatGPT, can analyse files that you upload. When you upload a spreadsheet, a typical tool does three things. First, it reads the data. It looks at the column names and the first rows to understand what each column contains.

Second, it calculates. Many tools write and run a small hidden program to sort, filter, add up or count the data. Third, it describes the result in words, and sometimes in a chart.

This makes AI useful for three kinds of work. Fast summaries, like totals, averages and counts by group, in seconds. Formula ideas, when you describe what you need in plain words. And chart suggestions that fit your question.

But it also fails in predictable ways. It can use the wrong column, for example adding up units when you asked about revenue. It can round too early, or skip rows with blank cells without telling you. And it can state a cause or a trend that the data does not support, in a very sure tone.

Anything you upload leaves your computer. So never upload personal or confidential data unless your organisation has approved the tool for that data. You will learn how to prepare a safe file in the next lesson.

Think of it this way. Imagine a very fast junior analyst in their first week. They produce a summary in minutes, and it is often good. But they do not yet know your business, they sometimes pick the wrong column, and they never say, I am not sure.

You would always review their work before you send it to your manager. Treat AI answers in the same way.

## Demonstrate
Hiroshi runs a small shop in Osaka that sells handmade soap and candles, online and at a weekend market. He uploads a fictional sales sheet to an AI assistant.

The sheet has eight rows. Two months, January and February. Two products, soap bars and candles. Two channels, online and market. And for each row, the units sold and the revenue.

He asks, what was total revenue by channel? The AI answers. Online, one thousand four hundred and ninety. Market, eight hundred and ninety. So online brought in about sixty-three percent of revenue.

Hiroshi checks one number in Google Sheets. He uses a formula that adds up the revenue column, but only for rows where the channel is online. The result is one thousand four hundred and ninety. The answer matches.

Then he asks, which product is more popular? The AI says soap bars are much more popular, with four hundred and twenty units against one hundred and forty candles. That is true for units.

But look at revenue. Soap bars brought in one thousand two hundred and sixty, and candles one thousand one hundred and twenty. The two products are close. Popular was a vague word, and the AI chose units without saying so. Hiroshi learns to name the column he means.

A common mistake is to think that because the AI runs code, its numbers must be correct. But the AI may have understood a different question. So always check at least one number by hand, and always ask which columns the AI used.

## Recap
Let's recap. First, AI file-analysis tools read your data, run hidden calculations, and describe the results in words and charts. Second, they are fast at summaries, formula ideas and chart suggestions, but they can use the wrong column, skip rows, and sound sure when they are wrong.

Third, treat the AI like a fast junior analyst. Check at least one number by hand, and never upload personal or confidential data to a tool your organisation has not approved.

## CTA
Now it is your turn. In the exercise below this video, you will upload the same sample sales sheet to Claude or ChatGPT, ask three questions, and check one answer by hand in Google Sheets. It takes about twenty minutes. In the next lesson, we look at safe data handling before you upload. See you there.

## Thumbnail
Headline: Can You Trust AI's Numbers?
Image: Navy background, a spreadsheet grid on the left with one cell circled in teal, a chat bubble with a number on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] File-analysis features in Claude and ChatGPT (feature names, supported file types, size limits, whether the hidden calculation is shown, and which free or paid plans include uploads) must be checked against the live tools before recording. The script avoids naming limits or plans for this reason.
- [VERSION] The exercise uses Google Sheets File > Download > Comma-separated values; check the menu path in the current interface (not spoken in the video).
- Hiroshi, his Osaka shop and all figures are fictional. Every spoken number matches content.md: Online 1,490, Market 890, about 63%; soap bars 420 units / 1,260 revenue, candles 140 units / 1,120 revenue.
- Scene 10 slide shows the full eight-row sample table from content.md exactly as written; scene 12 shows the formula =SUMIF(C2:C9, "Online", E2:E9) on screen, not read aloud.
- Stock footage for Hiroshi's shop must show no real shop names or logos.
