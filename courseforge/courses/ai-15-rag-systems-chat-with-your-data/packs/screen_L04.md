# Screen Demo Pack: AI-15 L04 Loading and Preparing a Document Collection

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L04_screen_1.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Show the drop_repeated_lines function in a notebook cell: Counter over the unique lines of each page, limit = min_share * len(pages), then remove repeated lines.
2. Highlight the default min_share=0.6.

**Narration over this clip (for pacing)**

> First, a simple and reliable cleaning rule. A line that appears on most pages of the same document is probably a header or footer. This small function counts each line across the pages, and removes any line that appears on at least sixty percent of them.

## Clip 2: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L04_screen_2.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Show the pages list: 'Annual Review' header, one sentence, 'Page 1' / 'Page 2' / 'Page 3'.
2. Run print(drop_repeated_lines(pages)) and show the exact output: ['Water access rose.\nPage 1', 'Schools reopened.\nPage 2', 'Budget was stable.\nPage 3'].
3. Show the page-number regular expression ^Page \d+$ removing the last line.

**Narration over this clip (for pacing)**

> We test it on three short pages. Each one starts with the same header, Annual Review, then one sentence, then a page number. When we run it, the header is gone from all three pages. The page numbers remain, because each one is different, so we remove them with a small pattern.

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L04_screen_3.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Show the folder data/raw/ with 25 PDF files.
2. Open the CSV file with columns for file name, source URL and licence.

**Narration over this clip (for pacing)**

> Now a full collection. Tanvir is a developer at a development research organisation in Dhaka, Bangladesh. His team wants to ask questions across twenty-five public World Bank reports about education and climate. He downloads the PDFs, and writes the source link and licence of each one into a spreadsheet file.

## Clip 4: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L04_screen_4.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Run the loop that reads each PDF page by page with pypdf.
2. Apply drop_repeated_lines and the page-number pattern to each document.
3. Build records with doc_id, title, page, date and url from the CSV.
4. Write data/records.jsonl and show its first lines.

**Narration over this clip (for pacing)**

> He loops over the files and extracts text page by page. He cleans each document with the function we just tested, removes page numbers, and builds one record per page, with the ID, title, page, date and link from the spreadsheet. Then he saves everything as JSON Lines, one record per line.

## Clip 5: scene 11

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L04_screen_5.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Print 3 random records and read them on screen.
2. Print a count of empty or very short pages per document.
3. Show the skipped list with two scanned reports and the reason 'scanned, no text'.

**Narration over this clip (for pacing)**

> Finally, he prints three random records and reads them. This check finds a problem. Two reports are scanned documents, and their text is empty. He does not index empty pages. He logs the two files in a skipped list, with the reason.

## Production notes for this lesson

- [VERIFY] Licence and terms of use of World Bank reports and any other example collection shown. The voiceover names World Bank reports as Tanvir's collection but makes no claim about their licence; confirm the terms before recording, or swap in another public collection.
- [VERSION] Parsing libraries (pypdf, BeautifulSoup) and their current APIs: check at recording time.
- The drop_repeated_lines output shown on screen must match content.md exactly: ['Water access rose.\nPage 1', 'Schools reopened.\nPage 2', 'Budget was stable.\nPage 3']. The voiceover says the header 'Annual Review' is removed and the page numbers remain.
- Tanvir and the Dhaka NGO are hypothetical. Do not show personal data in any record printed on screen.
