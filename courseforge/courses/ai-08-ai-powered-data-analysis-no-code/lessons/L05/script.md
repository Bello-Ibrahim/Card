# L05 AI-Written Formulas in Google Sheets | Presenter Script

Course: AI-08 · Video: 5 min · Words: 739

## Hook
You want total revenue for the South region, but you do not remember the formula. AI can write it in seconds. But a formula that looks right can still give the wrong number.

## Explain
Last time, we cleaned Mateus's orders sheet. Now we ask AI to write formulas for it, and we test every one.

Describe what you need in plain words, and an AI assistant can write the formula. A good request has four parts. Where the data is. What each column contains. What you want. And which tool, because formulas differ between spreadsheet tools.

Four functions are useful here. SUMIFS adds numbers that meet conditions. XLOOKUP finds a value in one column and returns the matching value from another. IF gives one result when a condition is true, and another when it is false. And date functions, such as TEXT and MONTH, take out parts of a date.

Always test a new formula on a few rows you can check by hand. If the formula and your hand check agree on three rows, you can trust it much more. And if you do not understand a formula, ask the AI to explain it.

One more thing. In some locale settings, Google Sheets uses semicolons instead of commas between the parts of a formula. If an AI formula shows a parse error, check the separators.

Think of an AI-written formula as a recipe from a friend who has never seen your kitchen. It is usually close, but you still taste the dish before you serve it.

## Demonstrate
Let's watch. Aigerim is a finance assistant in Almaty, Kazakhstan. She uses the clean, fictional orders sheet from the last lesson, with ten orders and revenue in US dollars.

First, a total by region. She asks the AI for total revenue where region is South. It returns a SUMIFS formula. She types it into cell J2, and the result is zero.

Zero cannot be right. She checks by hand. The South orders are two hundred and forty, one hundred and eighty, and one thousand eight hundred. That makes two thousand two hundred and twenty. The AI swapped the ranges. In SUMIFS, the range to add comes first.

She puts the revenue range first. Now the result is two thousand two hundred and twenty. She checks North the same way, which gives six hundred and eighty, and West, which gives five hundred and fifty.

Second, a lookup. She asks for the revenue of a given order ID. The AI gives an XLOOKUP formula. For order ten oh eight, it returns one thousand eight hundred. She tests order ten oh two, which gives two hundred and forty, and order ten ten, which gives one hundred and twenty. An ID that does not exist returns not found, as expected.

Third, a month column for grouping. The AI first suggests the MONTH function, which returns just the number one. So she asks, will this mix January twenty twenty-six with January twenty twenty-seven? It will. The AI suggests a better version with TEXT, which shows the year and the month.

She types the header Month in H1, puts the formula in H2, and fills it down. She checks three rows. H2 shows twenty twenty-six, zero one. H6 shows twenty twenty-six, zero two. And H10 shows twenty twenty-six, zero three.

Finally, she asks the AI to explain the SUMIFS formula step by step, and points to each range as she reads.

A common mistake is to accept a formula because it returns a number without an error. A wrong formula often returns a real-looking number, or zero, with no warning. Only a hand check shows it is correct.

## Recap
Let's recap. First, describe the data, the columns, what you want and the tool, and AI can write a useful formula. Second, test every AI formula on at least three rows by hand, and correct it if the results differ. Third, ask the AI to explain any formula you do not understand, and watch the separators for your locale.

## CTA
Now it is your turn. In the exercise below this video, you will ask Claude or ChatGPT for three formulas: a total by region, a lookup, and a date calculation. Test each one on three rows by hand, and correct any that are wrong. It takes about thirty minutes. Next time, we start week two with asking good questions of your data. See you there.

## Thumbnail
Headline: Test Every AI Formula
Image: Navy background, a Google Sheets-style formula bar showing a SUMIFS formula with a red 0 result crossed out and a teal 2,220 with a tick, headline in teal Inter Bold.

## Production Notes
- Screen demo lesson: record in Google Sheets and in Claude or ChatGPT (free tier) with the fictional clean orders sheet from content.md (A1:G11). Use the exact prompts and formulas from content.md: =SUMIFS(C2:C11, G2:G11, "South") → 0, corrected =SUMIFS(G2:G11, C2:C11, "South") → 2,220; =XLOOKUP(1008, A2:A11, G2:G11, "Not found") → 1,800; =MONTH(B2) → 1; =TEXT(B2, "yyyy-mm") in H2.
- If the live AI does not produce the swapped SUMIFS on its own, type the swapped formula shown in content.md for the demo; the narration says 'It returns a SUMIFS formula', which stays true.
- [VERSION] XLOOKUP availability in Google Sheets and the location of the locale setting (File > Settings) must be checked against the current interface.
- [VERSION] [REGION] [VERIFY] Argument separators and function names depend on locale settings. The narration only says that some locale settings use semicolons; it does not name which locales, and it does not say whether function names are translated. Confirm for the fr, pt and ar versions, and re-record the formula close-ups with semicolons where needed.
- Aigerim and the Almaty setting are fictional. Spoken numbers match content.md: South 240 + 180 + 1,800 = 2,220, North 680, West 550; lookup 1008 → 1,800, 1002 → 240, 1010 → 120; H2 2026-01, H6 2026-02, H10 2026-03.
