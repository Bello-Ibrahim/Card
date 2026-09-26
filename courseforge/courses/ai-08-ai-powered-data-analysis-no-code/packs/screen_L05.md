# Screen Demo Pack: AI-08 L05 AI-Written Formulas in Google Sheets

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L05_screen_1.mp4`
- **Target length:** about 14 seconds

**Steps**

1. In the AI chat, type: 'My Google Sheets data is in A1:G11, headers in row 1. Column C is Region, column G is Revenue. Write a formula for total revenue where Region is South.'
2. Show the AI reply: =SUMIFS(C2:C11, G2:G11, "South")
3. Switch to Google Sheets, click cell J2 and type the formula
4. Press Enter: J2 shows 0; zoom on the cell

**Narration over this clip (for pacing)**

> First, a total by region. She asks the AI for total revenue where region is South. It returns a SUMIFS formula. She types it into cell J2, and the result is zero.

## Clip 2: scene 10

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L05_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Highlight the three South rows (1002, 1006, 1008) in yellow
2. Show the hand sum as an overlay: 240 + 180 + 1,800 = 2,220
3. Click J2 and highlight the two ranges in the formula bar: C2:C11 is first, G2:G11 is second

**Narration over this clip (for pacing)**

> Zero cannot be right. She checks by hand. The South orders are two hundred and forty, one hundred and eighty, and one thousand eight hundred. That makes two thousand two hundred and twenty. The AI swapped the ranges. In SUMIFS, the range to add comes first.

## Clip 3: scene 11

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L05_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Edit J2 to =SUMIFS(G2:G11, C2:C11, "South") and press Enter: 2,220
2. In J3 enter the same formula with "North": 680
3. In J4 enter the same formula with "West": 550
4. Show a small hand-check column beside J2:J4 with green ticks

**Narration over this clip (for pacing)**

> She puts the revenue range first. Now the result is two thousand two hundred and twenty. She checks North the same way, which gives six hundred and eighty, and West, which gives five hundred and fifty.

## Clip 4: scene 12

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L05_screen_4.mp4`
- **Target length:** about 27 seconds

**Steps**

1. In the AI chat, ask for 'the revenue of a given Order ID'
2. Show the reply: =XLOOKUP(1008, A2:A11, G2:G11, "Not found")
3. Enter it in Google Sheets: 1,800; highlight row 1008
4. Change 1008 to 1002: 240; highlight row 1002
5. Change to 1010: 120; highlight row 1010
6. Change to 1099: Not found

**Narration over this clip (for pacing)**

> Second, a lookup. She asks for the revenue of a given order ID. The AI gives an XLOOKUP formula. For order ten oh eight, it returns one thousand eight hundred. She tests order ten oh two, which gives two hundred and forty, and order ten ten, which gives one hundred and twenty. An ID that does not exist returns not found, as expected.

## Clip 5: scene 13

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L05_screen_5.mp4`
- **Target length:** about 22 seconds

**Steps**

1. In the AI chat, ask for 'a Month column for grouping'
2. Show the reply =MONTH(B2); enter it in a spare cell: 1
3. Type in the chat: 'Will this mix January 2026 with January 2027?'
4. Show the improved reply: =TEXT(B2, "yyyy-mm")

**Narration over this clip (for pacing)**

> Third, a month column for grouping. The AI first suggests the MONTH function, which returns just the number one. So she asks, will this mix January twenty twenty-six with January twenty twenty-seven? It will. The AI suggests a better version with TEXT, which shows the year and the month.

## Clip 6: scene 14

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L05_screen_6.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Type 'Month' in H1
2. Enter =TEXT(B2, "yyyy-mm") in H2 and fill down to H11
3. Zoom on H2 (2026-01), H6 (2026-02) and H10 (2026-03), each next to its date in column B

**Narration over this clip (for pacing)**

> She types the header Month in H1, puts the formula in H2, and fills it down. She checks three rows. H2 shows twenty twenty-six, zero one. H6 shows twenty twenty-six, zero two. And H10 shows twenty twenty-six, zero three.

## Clip 7: scene 15

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_L05_screen_7.mp4`
- **Target length:** about 9 seconds

**Steps**

1. In the AI chat, type: 'Explain this formula step by step: =SUMIFS(G2:G11, C2:C11, "South")'
2. Scroll through the explanation
3. Switch to the sheet and highlight G2:G11, then C2:C11, then the word "South" as each part is explained

**Narration over this clip (for pacing)**

> Finally, she asks the AI to explain the SUMIFS formula step by step, and points to each range as she reads.

## Production notes for this lesson

- Screen demo lesson: record in Google Sheets and in Claude or ChatGPT (free tier) with the fictional clean orders sheet from content.md (A1:G11). Use the exact prompts and formulas from content.md: =SUMIFS(C2:C11, G2:G11, "South") → 0, corrected =SUMIFS(G2:G11, C2:C11, "South") → 2,220; =XLOOKUP(1008, A2:A11, G2:G11, "Not found") → 1,800; =MONTH(B2) → 1; =TEXT(B2, "yyyy-mm") in H2.
- If the live AI does not produce the swapped SUMIFS on its own, type the swapped formula shown in content.md for the demo; the narration says 'It returns a SUMIFS formula', which stays true.
- [VERSION] XLOOKUP availability in Google Sheets and the location of the locale setting (File > Settings) must be checked against the current interface.
- [VERSION] [REGION] [VERIFY] Argument separators and function names depend on locale settings. The narration only says that some locale settings use semicolons; it does not name which locales, and it does not say whether function names are translated. Confirm for the fr, pt and ar versions, and re-record the formula close-ups with semicolons where needed.
- Aigerim and the Almaty setting are fictional. Spoken numbers match content.md: South 240 + 180 + 1,800 = 2,220, North 680, West 550; lookup 1008 → 1,800, 1002 → 240, 1010 → 120; H2 2026-01, H6 2026-02, H10 2026-03.
