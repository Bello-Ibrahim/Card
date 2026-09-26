# Screen Demo Pack: AI-17 L11 What Makes Data Bad?

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L11_screen_1.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open Python, import duckdb and connect
2. Load the visits export into a table called visits
3. Run: SUMMARIZE visits;
4. Highlight the null percentage for patient_id and temp_c, and max temp_c = 73.0

**Narration over this clip (for pacing)**

> She opens Python, connects to DuckDB, and loads the visits export. Then she runs summarize. Two columns have missing values, the patient ID and the temperature. And the maximum temperature is seventy-three, which is impossible.

## Clip 2: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L11_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Type the targeted profile query from content.md (total_rows, missing_patient, missing_temp, duplicate_rows, temp_out_of_range)
2. Run it and show the result exactly: 11 | 1 | 1 | 3 | 1

**Narration over this clip (for pacing)**

> Next, a targeted profile in one query. It counts the total rows, the missing patient IDs, the missing temperatures, the extra rows beyond distinct visit IDs, and the temperatures outside a normal human range. On her eleven invented rows, it returns eleven, one, one, three and one.

## Clip 3: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L11_screen_3.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Type the malaria query from content.md: malaria_raw and malaria_real
2. Run it and show the result exactly: 6 | 3

**Narration over this clip (for pacing)**

> Three duplicate rows. So she compares the malaria count before and after removing duplicates. The raw count is six. The real count, by distinct visit, is three.

## Production notes for this lesson

- [VERIFY] The clinic duplicate-visit example is hypothetical and must stay presented as hypothetical: the voiceover says 'an invented example' and the stock and screen visuals must not show a real clinic, logo or patient. Figures come from invented sample data run in DuckDB 1.5.5.
- [VERIFY] Any public dataset suggested for the exercise: the voiceover names none; confirm licence, download location and that it holds no personal data before showing one.
- [VERSION] DuckDB's SUMMARIZE output columns and the FILTER clause must be checked against the current DuckDB release.
- Screen output must match content.md exactly: the profile query returns 11 | 1 | 1 | 3 | 1, the malaria query returns 6 | 3, and SUMMARIZE shows a maximum temp_c of 73.0.
- Dr. Samira Haddad and the clinics near Irbid, Jordan are fictional.
