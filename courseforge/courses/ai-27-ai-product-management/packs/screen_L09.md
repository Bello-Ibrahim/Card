# Screen Demo Pack: AI-27 L09 Building a Test Set and Running Evaluations

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-27-ai-product-management_L09_screen_1.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Open a new Google Sheets file
2. Type headers in columns A to F: ID, Type, Input, Expected behaviour, Output, Human score
3. Add column G: Judge score

**Narration over this clip (for pacing)**

> Let's run one. Maria Santos is a PM at a hypothetical home goods shop in the Philippines. Her feature answers questions about returns, using the shop's return policy. In Google Sheets, she creates columns for ID, type, input, expected behaviour, output, human score and judge score.

## Clip 2: scene 8

- **Filename:** `ai-27-ai-product-management_L09_screen_2.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Fill 20 rows with invented cases: 8 Common, 5 Edge, 4 Language, 3 Refuse
2. Paste each input into Claude together with the return policy
3. Paste Claude's answer into column E (Output)
4. Score column F (Human score) with the 0, 1, 2 rubric

**Narration over this clip (for pacing)**

> She fills twenty rows with invented cases: eight common, five edge, four language, and three should refuse. All cases are invented, with no real customer data. She pastes each input into Claude with the policy, and copies the answer into the output column. Then she scores each answer with the rubric.

## Clip 3: scene 9

- **Filename:** `ai-27-ai-product-management_L09_screen_3.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open a new Claude chat and paste the rubric
2. Send one case at a time: "Score this answer 0, 1 or 2 using the rubric. Give the score and one reason."
3. Record each score in column G (Judge score)

**Narration over this clip (for pacing)**

> Next, she opens a new Claude chat, gives it the rubric, and sends one case at a time, asking for a score of zero, one or two with one reason. She records each score in the judge column.

## Clip 4: scene 10

- **Filename:** `ai-27-ai-product-management_L09_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Add pass rate formula: =COUNTIF(F2:F21,2)/20
2. Add pass rate by type: =COUNTIFS(B2:B21,"Edge",F2:F21,2)/COUNTIF(B2:B21,"Edge") and repeat for each type
3. Add agreement formula: =SUMPRODUCT(--(F2:F21=G2:G21))/20
4. Highlight results: 60% overall, Common 75%, Edge 40%, Language 50%, Refuse 67%

**Narration over this clip (for pacing)**

> Now she adds formulas for the pass rate, the pass rate for each type, and the agreement between her and the judge. Her human pass rate is twelve of twenty, or sixty percent. By type, common cases pass at seventy five percent, but edge cases only at forty percent.

## Clip 5: scene 11

- **Filename:** `ai-27-ai-product-management_L09_screen_5.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Show the judge pass rate cell: 14 of 20, 70%
2. Show the agreement cell: 15 of 20, 75%

**Narration over this clip (for pacing)**

> The judge gives fourteen passes, which is seventy percent. It agrees with Maria on fifteen of twenty cases, which is seventy five percent. It scores higher than Maria on four cases, and lower on one.

## Clip 6: scene 12

- **Filename:** `ai-27-ai-product-management_L09_screen_6.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Filter rows where column F and column G differ
2. Read each of the 5 disagreement rows
3. Highlight row 16: Cebuano return question, Human 0, Judge 2

**Narration over this clip (for pacing)**

> She filters the rows where the two scores differ, and reads each one. The biggest miss is case sixteen. The answer in Cebuano was wrong, but the judge gave it a two. So the judge is too generous, and weak on less common languages. Every judge score in those languages needs human review.

## Production notes for this lesson

- [VERSION] Claude free-plan limits and data-use terms, and the Google Sheets COUNTIF, COUNTIFS and SUMPRODUCT formulas, must be checked before recording the screen demo.
- Screen demo: record in Google Sheets and Claude with a prepared sheet holding Maria's 20 invented cases from content.md (types, inputs, human and judge scores exactly as in the table). Use a short invented return policy as context. No real customer data.
- The metrics must be spoken and shown exactly: human pass rate 12 of 20, 60 percent; judge 14 passes, 70 percent; agreement 15 of 20, 75 percent; judge higher on 4 cases and lower on 1; biggest miss case 16 (Cebuano). These were checked against the sample table in content.md.
- LLM-as-judge is taught as a technique with limits and human spot checks, never as a replacement for human rating (curriculum flag).
- Maria Santos and the online home-goods shop in the Philippines are hypothetical. Tagalog, Taglish and Cebuano inputs on screen should be checked by a speaker before recording.
