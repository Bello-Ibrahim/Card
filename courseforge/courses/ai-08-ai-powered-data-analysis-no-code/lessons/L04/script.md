# L04 Cleaning Messy Data with AI Help | Presenter Script

Course: AI-08 · Video: 5 min · Words: 740

## Hook
You ask AI for sales by region, and it reports six regions. Your company has three. The maths was right, but the data was messy. And messy data gives wrong answers, however clever the tool.

## Explain
Last time, we turned vague worries into clear data questions. Before we answer them, we need clean data.

Five problems appear again and again. Duplicates, where the same order is entered twice, so totals are too high. Blank cells, which some tools skip and others treat as zero. And inconsistent spellings. South, lower-case south, S T H, and South with a space at the end are four different values to a computer.

Then there are mixed date formats. Zero eight, zero one, twenty twenty-six can mean the eighth of January or the first of August, depending on the country. And numbers stored as text. They look like numbers, but they are not added up in totals.

AI can help, but there is a right way and a wrong way. The wrong way is to upload the file, say clean this, and download whatever comes back. You cannot see what was changed, deleted or guessed. The right way is to describe the problem, and ask for step-by-step fixes that you make yourself in Google Sheets.

Google Sheets has useful tools for this. TRIM removes extra spaces. PROPER fixes capital letters. VALUE turns a number stored as text into a real number. There are also menu tools to remove duplicates, and find and replace to change one spelling into another.

And keep a cleaning log. One line for each change, saying what you changed, how, and why.

Cleaning data is like washing and sorting vegetables before you cook. If you skip it, the meal may look fine, but there is sand in the salad. And you wash them yourself, so you know what was thrown away.

## Demonstrate
Mateus is the office manager of a fictional online office-supplies shop in Porto Alegre, Brazil. He exports his orders sheet. It has eleven rows, and revenue is in US dollars.

Look closely, and the problems appear. Order ten oh six is there twice. One revenue cell is empty. Regions are spelled in different ways. Dates come in three formats. And some numbers have an apostrophe or a dollar sign, so they are stored as text.

He asks an AI assistant to list the problems and suggest fixes, and makes each change himself. First, he removes the duplicate row. Second, the blank revenue for order ten oh four. He checks that three units times one hundred and twenty gives three hundred and sixty, and enters it.

Third, spellings. He fixes the regions with TRIM, then find and replace, so south and S T H become South. He tidies the product names in the same way.

Fourth, dates. The AI warns that zero eight, zero one is ambiguous. The order IDs are in date order, and order ten oh two is the fifteenth of January. So order ten oh one must be the eighth of January. He changes every date to one format, year, month, day.

Fifth, text numbers. He converts them into real numbers with VALUE, or by retyping them.

Before cleaning, the sum of the revenue column gave only one thousand four hundred and seventy. The blank and the one thousand eight hundred stored as text were left out, and the duplicate was counted twice. The clean sheet has ten orders, and total revenue of three thousand four hundred and fifty.

A common mistake is to let the AI clean the file, and never check what changed. It may delete real repeat orders as duplicates, or fill blanks with guesses. Ask for steps, make each change yourself, and log it.

## Recap
Let's recap. First, the five common problems are duplicates, blank cells, inconsistent spellings, mixed date formats, and numbers stored as text. Second, describe the problem to AI, and ask for step-by-step fixes that you apply yourself, instead of letting it change the data invisibly. Third, keep a cleaning log with every change, how you made it, and why.

## CTA
Now it is your turn. In the exercise below this video, you will clean Mateus's messy orders sheet in Google Sheets with AI suggestions. Fix at least five types of problem, and log each change. It takes about thirty minutes. In the next lesson, we look at AI-written formulas in Google Sheets. See you there.

## Thumbnail
Headline: Clean Before You Analyse
Image: Navy background, a messy spreadsheet on the left with red-highlighted cells, a clean one on the right with teal ticks, headline in teal Inter Bold.

## Production Notes
- [VERSION] Google Sheets menu paths (Data > Data cleanup > Remove duplicates, Trim whitespace, and Edit > Find and replace) must be checked against the current interface. The narration names the tools, not the menu paths.
- [REGION] Argument separators (comma or semicolon) depend on the spreadsheet locale; the video does not cover this (L05 does). Formulas on slides use commas.
- Mateus, the Porto Alegre shop and all orders are fictional; revenue is in US dollars. Spoken numbers match content.md: 11 rows before, 10 orders after, blank for order 1004 = 3 × 120 = 360, SUM before cleaning 1,470, clean total 3,450 (360 and 1,800 left out, 180 counted twice).
- Scene 10 slide shows the full messy table exactly as in content.md, with a visible marker for the trailing space in 'North ' and the apostrophes in '40 and '1,800.
- 'Sth' is spoken as 'S T H'; order IDs are spoken as 'ten oh four' and so on.
