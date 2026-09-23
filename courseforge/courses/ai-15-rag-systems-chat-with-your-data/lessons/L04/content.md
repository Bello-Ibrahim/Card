# L04 Loading and Preparing a Document Collection

Course: AI-15 · Module: M1 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Your first pipeline used one clean text file. Real collections are not clean. PDFs repeat the same header on every page, web pages include menus and cookie notices, and nobody remembers which file came from where. If this noise goes into your index, it comes back out in your answers.

## Explanation
Loading has one goal: turn every source file into a **record** with clean text and useful metadata. A simple record looks like this:

```python
{"doc_id": "wb-2023-017", "title": "...", "page": 12,
 "date": "2023-06", "url": "https://...", "doc_type": "report",
 "language": "en", "text": "..."}
```

Keep one record per page for PDFs, so each citation can point to a page. For HTML and Markdown, one record per document or per section is enough.

**Parsing by format.** Each format needs its own tool. These are common free Python options; check their current APIs. [VERSION]

- **PDF:** a library such as `pypdf` extracts text page by page. Scanned PDFs contain images, not text, and need OCR, which is out of scope here. Tables often come out as broken lines; note which documents rely on tables.
- **HTML:** `BeautifulSoup` can remove `nav`, `header`, `footer` and `script` elements before you take the text.
- **Markdown:** read it as text and keep the headings, because they are useful for chunking in L05.

**Cleaning.** Remove repeated headers and footers, page numbers, and extra blank lines. A simple and reliable rule: a line that appears on most pages of the same document is probably a header or footer.

```python
from collections import Counter

def drop_repeated_lines(pages, min_share=0.6):
    counts = Counter(line.strip() for p in pages
                     for line in set(p.splitlines()) if line.strip())
    limit = min_share * len(pages)
    repeated = {line for line, n in counts.items() if n >= limit}
    return ["\n".join(l for l in p.splitlines() if l.strip() not in repeated)
            for p in pages]

pages = ["Annual Review\nWater access rose.\nPage 1",
         "Annual Review\nSchools reopened.\nPage 2",
         "Annual Review\nBudget was stable.\nPage 3"]
print(drop_repeated_lines(pages))
```

Output:

```
['Water access rose.\nPage 1', 'Schools reopened.\nPage 2', 'Budget was stable.\nPage 3']
```

The header is gone. The page numbers remain because each one is different; remove them with a small regular expression such as `^Page \d+$`.

**Metadata** does two jobs. It lets the answer cite "title, page 12" with a link, and it lets retrieval filter by year, document type or language (L06). Collect it at load time; it is hard to recover later.

**Licence.** Before you index a collection, check its licence and terms of use. Some public reports allow reuse with attribution; others do not allow commercial use. Record the licence in your project notes. [VERIFY]

**Analogy:** Loading documents is like a kitchen preparing ingredients before cooking. You wash the vegetables, remove the parts you cannot eat, and label each container with its contents and date. If you skip this step, every dish that follows has the same problem.

## Worked Example
Tanvir is a developer at a hypothetical development-research NGO in Dhaka, Bangladesh. His team wants to ask questions across 25 public World Bank reports about education and climate. [VERIFY] licence and terms of use for World Bank reports.

On screen, follow his steps:

1. He downloads the 25 PDFs into a folder `data/raw/` and writes the source URL and licence of each into a CSV file.
2. He loops over the files with `pypdf`, extracting text page by page. [VERSION]
3. He runs `drop_repeated_lines` on each document's pages, then removes page numbers with a regular expression.
4. He builds one record per page with `doc_id`, `title`, `page`, `date` and `url` from the CSV.
5. He saves all records as JSON Lines (one JSON object per line) in `data/records.jsonl`.
6. He prints 3 random records and reads them.

The check in step 6 finds a problem: two reports are scanned documents, and their text is empty. He logs them in a "skipped" list instead of indexing empty pages.

## Common Mistake
Many developers index raw text straight from the parser and never look at it. Then answers contain footer text or page numbers, and citations cannot point to a page because the page was never recorded. Always print and read a sample of records, count empty or very short pages, and keep a list of skipped files with the reason.

## Key Takeaways
1. Turn every source file into records with clean text and metadata (title, page, date, URL, type, language); one record per page for PDFs.
2. Use a parser that fits each format, remove repeated headers, footers and page numbers, and check samples by eye.
3. Check and record the licence of every collection before you index it.

## Hands-on Exercise
**Task:** Load 20 or more documents from a public collection into a list of records with clean text and metadata, and save it.
**Tools:** Python 3 with pypdf and BeautifulSoup (free); a public collection, such as open-source project documentation or public reports. [VERSION]
**Steps:**
1. Choose your collection and check its licence. Do not use personal or confidential data. [VERIFY]
2. Download at least 20 documents and record each source URL and licence in a CSV file.
3. Write one loader function per format you use (PDF, HTML or Markdown).
4. Clean each document with `drop_repeated_lines` and a page-number pattern.
5. Build records with at least `doc_id`, `title`, `page` (if any), `date`, `url` and `text`.
6. Save them to `records.jsonl`, then print 3 random records and a count of empty or very short pages.
**What good looks like:** A `records.jsonl` file with 20+ documents, clean text without repeated headers, complete metadata, and a short log of skipped or problem files with reasons.
**Time:** about 40 minutes

## Review Flags
- [VERIFY] Licence and terms of use of World Bank reports and of any other example collection shown (course-level flag).
- [VERSION] Parsing libraries (`pypdf`, BeautifulSoup) and their current APIs must be checked at recording time.
