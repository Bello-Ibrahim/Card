# L04 Cleaning Messy Data with AI Help

Course: AI-08 · Module: M1 · Objectives: O3 · Video: 5 min

## Hook
You ask AI for sales by region, and it reports six regions. Your company has three. The maths was right, but the data was messy, and messy data gives wrong answers, however clever the tool.

## Explanation
Real spreadsheets are rarely clean. Five problems appear again and again:

- **Duplicates:** the same order entered twice, so totals are too high.
- **Blank cells:** a missing value, which some tools skip and others treat as zero.
- **Inconsistent spellings:** "South", "south", "Sth" and "South " (with a space at the end) are four different values to a computer.
- **Mixed date formats:** "08/01/2026" can mean 8 January or 1 August, depending on the country.
- **Numbers stored as text:** a value such as `'40` or "$30" looks like a number but is not added up in totals.

AI can help, but there is a right and a wrong way. The wrong way is to upload the file, say "clean this" and download whatever comes back. You cannot see what was changed, deleted or guessed.

The right way is to **describe the problem and ask for step-by-step fixes that you do yourself in Google Sheets.** For example: "In column C of my Google Sheet, regions are spelled in different ways, such as 'south', 'Sth' and 'North ' with a space. Give me a formula or a menu step to make them consistent." You stay in control, and every change is visible.

Useful tools in Google Sheets for cleaning:

- `=TRIM(C2)` removes extra spaces. `=PROPER(D2)` changes "desk LAMP" into "Desk Lamp".
- `=VALUE(E6)` turns a number stored as text into a real number.
- Data > Data cleanup > Remove duplicates, and Data cleanup > Trim whitespace. [VERSION]
- Find and replace (Edit > Find and replace) to change "Sth" into "South". [VERSION]

If your spreadsheet uses a locale with a comma as the decimal mark, formulas with more than one argument use semicolons instead of commas. L05 explains this. [REGION]

Keep a **cleaning log**: one line for each change, saying what you changed, how, and why.

**Analogy:** Cleaning data is like washing and sorting vegetables before you cook. If you skip it, the meal may look fine, but there is sand in the salad. And you wash them yourself, so you know what was thrown away.

## Worked Example
Mateus is the office manager of a small, fictional online office-supplies shop in Porto Alegre, Brazil. He exports this orders sheet (revenue is in US dollars):

| Order ID | Order Date | Region | Product | Units | Unit Price | Revenue |
|---|---|---|---|---|---|---|
| 1001 | 08/01/2026 | North | Notebook pack | 20 | 4 | 80 |
| 1002 | 2026-01-15 | south | Office chair | 2 | 120 | 240 |
| 1003 | 22 Jan 2026 | West | Desk Lamp | 5 | 30 | 150 |
| 1004 | 2026-02-03 | North␣ | office chair | 3 | 120 | |
| 1005 | 2026-02-11 | West | Notebook pack | '40 | 4 | 160 |
| 1006 | 2026-02-19 | Sth | Desk lamp | 6 | 30 | 180 |
| 1006 | 2026-02-19 | Sth | Desk lamp | 6 | 30 | 180 |
| 1007 | 2026-02-26 | North | Desk lamp | 4 | $30 | 120 |
| 1008 | 2026-03-04 | South | Office chair | 15 | 120 | '1,800 |
| 1009 | 2026-03-18 | West | Office Chair | 2 | 120 | 240 |
| 1010 | 25/03/2026 | North | Notebook pack | 30 | 4 | 120 |

(␣ shows a space at the end of the cell. A leading apostrophe shows a number stored as text.)

He asks an AI assistant to list the problems and suggest fixes, and he makes each change himself:

1. **Duplicate:** order 1006 appears twice. Removed one row with Remove duplicates.
2. **Blank cell:** revenue for 1004 is empty. He checks that Units × Unit Price gives 3 × 120 = 360 and enters 360.
3. **Spellings:** Region fixed with TRIM, then Find and replace ("south" and "Sth" to "South"). Product fixed with PROPER, then he changes "Desk Lamp" and "Office Chair" back to the company's style ("Desk lamp", "Office chair").
4. **Dates:** all changed to the format 2026-01-08. The AI warned that "08/01/2026" is ambiguous. Order IDs are in date order, and 1002 is 15 January, so 1001 must be 8 January.
5. **Text numbers:** `'40`, `$30` and `'1,800` converted to real numbers with VALUE and by retyping.

The clean sheet has 10 orders and total revenue of 3,450. Before cleaning, `=SUM` of the Revenue column gave only 1,470: the blank (360) and the text value (1,800) were left out, and the duplicate (180) was counted twice.

## Common Mistake
Many learners let the AI "clean" the file and never check what changed. The AI may delete real repeat orders as "duplicates" or fill blanks with guesses. Ask for steps, make each change yourself, and log it.

## Key Takeaways
1. The five common problems are duplicates, blank cells, inconsistent spellings, mixed date formats and numbers stored as text.
2. Describe the problem to AI and ask for step-by-step fixes that you apply yourself in Google Sheets, instead of letting it change the data invisibly.
3. Keep a cleaning log with every change, how you made it and why.

## Hands-on Exercise
**Task:** Clean the messy orders dataset from the Worked Example in Google Sheets with AI suggestions, fixing at least 5 types of problem and logging each change.
**Tools:** Google Sheets (free); Claude or ChatGPT (free tier). The data is fictional.
**Steps:**
1. Copy the messy table into a Google Sheet. Keep a copy of this tab called "Raw".
2. Ask an AI tool: "Here are the column names and 11 rows of my orders sheet. List every data problem and give me Google Sheets steps to fix each one. Do not return a cleaned table." Paste the rows as text.
3. Apply each fix yourself in a tab called "Clean".
4. Add a "Cleaning log" tab: problem, rows affected, fix, reason.
5. Check your work: `=COUNTA(A2:A20)` should give 10 orders and `=SUM(G2:G11)` should give 3450.
**What good looks like:** 10 rows remain, with three regions (North, South, West), three product names, one date format, real numbers only, and revenue 360 for order 1004. The log has at least 5 lines, one for each type of problem.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Google Sheets menu paths (Data > Data cleanup > Remove duplicates, Trim whitespace, and Edit > Find and replace) must be checked against the current interface.
- [REGION] Argument separators (comma or semicolon) depend on the spreadsheet locale; see the detailed note in L05.
