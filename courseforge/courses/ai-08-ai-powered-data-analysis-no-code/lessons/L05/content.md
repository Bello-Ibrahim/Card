# L05 AI-Written Formulas in Google Sheets

Course: AI-08 · Module: M1 · Objectives: O3, O6 · Video: 5 min (screen demo)

## Hook
You want "total revenue for the South region" but do not remember the formula. AI can write it in seconds. But a formula that looks right can still give the wrong number.

## Explanation
Describe what you need in plain words, and an AI assistant can write the formula. A good request has four parts:

1. **Where the data is:** "My data is in A1:G11, with headers in row 1."
2. **What each column contains:** "Column C is Region, column G is Revenue."
3. **What you want:** "Total revenue where Region is South."
4. **Which tool:** "Google Sheets", because formulas differ between spreadsheet tools.

Useful functions for this course:

- **SUMIFS** adds numbers that meet conditions.
- **XLOOKUP** finds a value in one column and returns the matching value from another. [VERSION]
- **IF** returns one result if a condition is true and another if it is false.
- **Date functions**, such as TEXT and MONTH, extract parts of a date.

**Always test a new formula** on a few rows that you can check by hand. If the formula and your hand check agree on 3 rows, you can trust it much more.

If you do not understand a formula, ask the AI to explain it step by step. Do not use a formula you cannot explain.

**Comma or semicolon?** In Google Sheets, the spreadsheet locale (File > Settings) sets the argument separator. Many locales that use a comma as the decimal mark, such as French or Portuguese settings, use semicolons: `=SUMIFS(G2:G11; C2:C11; "South")`. If an AI formula shows a parse error, check the separators. Function names can also be translated in some spreadsheet tools and language settings. [VERSION] [REGION] [VERIFY]

**Analogy:** An AI-written formula is like a recipe from a friend who has never seen your kitchen. It is usually close, but you still taste the dish before serving it.

## Worked Example
Aigerim, a finance assistant in Almaty, Kazakhstan, practises with the clean fictional orders sheet from L04 (columns A to G, revenue in US dollars):

| Order ID | Order Date | Region | Product | Units | Unit Price | Revenue |
|---|---|---|---|---|---|---|
| 1001 | 2026-01-08 | North | Notebook pack | 20 | 4 | 80 |
| 1002 | 2026-01-15 | South | Office chair | 2 | 120 | 240 |
| 1003 | 2026-01-22 | West | Desk lamp | 5 | 30 | 150 |
| 1004 | 2026-02-03 | North | Office chair | 3 | 120 | 360 |
| 1005 | 2026-02-11 | West | Notebook pack | 40 | 4 | 160 |
| 1006 | 2026-02-19 | South | Desk lamp | 6 | 30 | 180 |
| 1007 | 2026-02-26 | North | Desk lamp | 4 | 30 | 120 |
| 1008 | 2026-03-04 | South | Office chair | 15 | 120 | 1800 |
| 1009 | 2026-03-18 | West | Office chair | 2 | 120 | 240 |
| 1010 | 2026-03-25 | North | Notebook pack | 30 | 4 | 120 |

Presenter steps on screen:

1. **Total by region.** In the AI chat, ask for "total revenue where Region is South". The AI returns `=SUMIFS(C2:C11, G2:G11, "South")`. Type it in cell J2: the result is 0. Hand check: South orders are 240 + 180 + 1,800 = 2,220. The AI swapped the ranges. In SUMIFS, the range to add comes first. Correct it to `=SUMIFS(G2:G11, C2:C11, "South")`: the result is 2,220. Check "North" (680) and "West" (550) the same way.
2. **Lookup.** Ask for "the revenue of a given Order ID". The AI returns `=XLOOKUP(1008, A2:A11, G2:G11, "Not found")`. Result: 1,800. Test with 1002 (240) and 1010 (120), reading each row. Test 1099: "Not found", as expected.
3. **Date calculation.** Ask for "a Month column for grouping". The AI first suggests `=MONTH(B2)`, which returns 1. Ask: "Will this mix January 2026 with January 2027?" It will, so ask for a better version: `=TEXT(B2, "yyyy-mm")`. Put it in H2 with the header "Month" in H1, and fill down. Check 3 rows: H2 shows 2026-01, H6 shows 2026-02, H10 shows 2026-03.
4. **Explain.** Ask the AI to explain the SUMIFS formula step by step, and point to each range on screen.

## Common Mistake
Many learners accept a formula because it returns a number without an error. A wrong formula often returns a real-looking number, or 0, with no warning. Only a hand check shows it is correct.

## Key Takeaways
1. Describe where the data is, what each column holds, what you want and which tool you use, and the AI can write a useful formula.
2. Test every AI-written formula on at least 3 rows that you check by hand, and correct it if the results differ.
3. Ask the AI to explain any formula you do not understand, and watch for comma or semicolon separators in your locale.

## Hands-on Exercise
**Task:** Ask Claude or ChatGPT for 3 formulas for the orders dataset: a total by region, a lookup and a date calculation. Test each on 3 rows by hand and correct any that are wrong.
**Tools:** Google Sheets (free); Claude or ChatGPT (free tier). The data is fictional.
**Steps:**
1. Open your clean orders sheet from L04, or copy the table above into A1:G11.
2. Ask the AI for a formula for total revenue by region. Enter it for all three regions.
3. Ask for a lookup formula that returns the Product for any Order ID.
4. Ask for a Month column formula in column H, and fill it down.
5. Test each formula on 3 rows or cases by hand. Write the formula result and your hand result side by side.
6. If any result is wrong, tell the AI what you expected and ask for a correction. Record the fix.
**What good looks like:** Region totals of North 680, South 2,220 and West 550 (together 3,450), with the Revenue range first in SUMIFS. A lookup such as `=XLOOKUP(1005, A2:A11, D2:D11)` returns "Notebook pack". The Month column shows year and month, such as 2026-02. A small table records 9 hand checks and any corrections.
**Time:** about 30 minutes

## Review Flags
- [VERSION] XLOOKUP availability in Google Sheets and the location of the locale setting (File > Settings) must be checked against the current interface.
- [VERSION] [REGION] Argument separators and function names depend on locale settings (comma or semicolon); check how formulas appear for the fr, pt and ar versions of the course.
- [VERIFY] Confirm which Google Sheets locales use semicolon separators (including Arabic-language locales) and whether Google Sheets translates function names in any locale.
