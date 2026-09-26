# Screen Demo Pack: AI-17 L05 DuckDB: Fast Analytics on Your Laptop

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L05_screen_1.mp4`
- **Target length:** about 6 seconds

**Steps**

1. In a terminal, run: pip install duckdb
2. Open a new file compare.py in the editor

**Narration over this clip (for pacing)**

> In a terminal, he installs DuckDB, and opens a new Python file called compare.

## Clip 2: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L05_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Type the first part of compare.py from content.md: import duckdb, os, time; con = duckdb.connect()
2. Type the COPY statement that selects meter_id, slot and kwh from range(2000000) TO 'readings.csv' (HEADER)
3. Type: COPY (SELECT * FROM 'readings.csv') TO 'readings.parquet' (FORMAT parquet)

**Narration over this clip (for pacing)**

> First, the script connects to DuckDB, and generates two million meter readings for five thousand meters. It writes them to a CSV file, then copies the same data into a Parquet file.

## Clip 3: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L05_screen_3.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Type the for loop over readings.csv and readings.parquet from content.md
2. Highlight the query: SELECT meter_id, avg(kwh) FROM the file GROUP BY meter_id
3. Highlight the print line with file size in MB and seconds

**Narration over this clip (for pacing)**

> Then, for each file, it runs the same query, the average reading per meter, and prints the file size in megabytes and the time the query took.

## Clip 4: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L05_screen_4.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run: python compare.py
2. Show the output exactly as in content.md: readings.csv 28.8 MB 0.121 s / readings.parquet 5.9 MB 0.009 s

**Narration over this clip (for pacing)**

> He runs the script. On our four-core test machine, the CSV file is twenty-eight point eight megabytes, and the query takes about a tenth of a second. The Parquet file is only five point nine megabytes, and the query takes nine thousandths of a second.

## Clip 5: scene 13

- **Filename:** `ai-17-data-engineering-for-ai_L05_screen_5.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Highlight the two size values side by side: 28.8 MB and 5.9 MB
2. Highlight the two times: 0.121 s and 0.009 s

**Narration over this clip (for pacing)**

> Same two million rows, about five times smaller, and more than ten times faster. Your exact numbers will differ with your hardware and DuckDB version. Hiroshi stores monthly exports as Parquet, and keeps PostgreSQL for the customer portal.

## Production notes for this lesson

- [VERSION] DuckDB's Python package interface (duckdb.connect, con.sql, COPY ... (FORMAT parquet)) and file-format support must be checked against the current release; the script was tested with DuckDB 1.5.5 and Python 3.
- [VERIFY] Any public CSV dataset suggested for the exercise: the voiceover names none; confirm licence and download location before showing one on screen.
- Screen output must match content.md exactly: readings.csv 28.8 MB 0.121 s and readings.parquet 5.9 MB 0.009 s. Sizes and timings are machine-specific; the voiceover says 'on our machine'. If a re-recording gives different timings, show the content.md output as a still or re-test and update content.md first.
- Hiroshi and the electricity retailer in Osaka are fictional; the data is generated, so no customer data appears on screen.
