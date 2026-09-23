# L04 Loading and Preparing a Document Collection | Presenter Script

Course: AI-15 · Video: 5 min · Words: 685

## Hook
Your first pipeline used one clean text file. Real collections are not clean. PDFs repeat the same header on every page, and web pages include menus and cookie notices. If this noise goes into your index, it comes back out in your answers.

## Explain
In the last lesson, we built a pipeline over one file. Today we prepare a whole collection, so that every later stage gets clean input.

Loading has one goal. Turn every source file into a record, with clean text and useful metadata: a document ID, a title, a page, a date, a link, a document type and a language. For PDFs, keep one record per page, so each citation can point to a page.

Each format needs its own tool. For PDFs, a library such as pypdf extracts text page by page, but scanned PDFs contain images, not text. For HTML, BeautifulSoup can remove menus, headers, footers and scripts. For Markdown, keep the headings, because they help with chunking later. Tables often come out as broken lines, so note which documents rely on them.

Metadata does two jobs. It lets an answer cite the title and page with a link, and it lets retrieval filter by year, type or language. Collect it at load time, because it is hard to recover later. And before you index anything, check and record the licence of the collection.

Think of a kitchen preparing ingredients before cooking. You wash the vegetables, remove the parts you cannot eat, and label each container with its contents and date. If you skip this step, every dish that follows has the same problem.

## Demonstrate
First, a simple and reliable cleaning rule. A line that appears on most pages of the same document is probably a header or footer. This small function counts each line across the pages, and removes any line that appears on at least sixty percent of them.

We test it on three short pages. Each one starts with the same header, Annual Review, then one sentence, then a page number. When we run it, the header is gone from all three pages. The page numbers remain, because each one is different, so we remove them with a small pattern.

Now a full collection. Tanvir is a developer at a development research organisation in Dhaka, Bangladesh. His team wants to ask questions across twenty-five public World Bank reports about education and climate. He downloads the PDFs, and writes the source link and licence of each one into a spreadsheet file.

He loops over the files and extracts text page by page. He cleans each document with the function we just tested, removes page numbers, and builds one record per page, with the ID, title, page, date and link from the spreadsheet. Then he saves everything as JSON Lines, one record per line.

Finally, he prints three random records and reads them. This check finds a problem. Two reports are scanned documents, and their text is empty. He does not index empty pages. He logs the two files in a skipped list, with the reason.

A common mistake is to index raw parser output without looking at it. Then answers contain footer text, and citations cannot point to a page. Always read a sample, and count empty pages. And keep a list of skipped files, with the reason for each one. This list helps you later, when an answer looks strange.

## Recap
Let's recap. First, turn every source file into records with clean text and metadata, and keep one record per page for PDFs. Second, use a parser that fits each format, remove repeated headers, footers and page numbers, and check samples by eye. Third, check and record the licence of every collection before you index it.

## CTA
Now it is your turn. In the exercise below, load twenty or more documents from a public collection into clean records with metadata, save them, and keep a short log of any skipped files. Then print three random records and read them, just like Tanvir did. In the next lesson, Chunking Strategies, we cut these records into pieces that retrieval can use well.

## Thumbnail
Headline: Clean Data, Clean Answers
Image: Navy background, a messy stack of PDF pages with repeated headers on the left turning into neat labelled record cards on the right, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Licence and terms of use of World Bank reports and any other example collection shown. The voiceover names World Bank reports as Tanvir's collection but makes no claim about their licence; confirm the terms before recording, or swap in another public collection.
- [VERSION] Parsing libraries (pypdf, BeautifulSoup) and their current APIs: check at recording time.
- The drop_repeated_lines output shown on screen must match content.md exactly: ['Water access rose.\nPage 1', 'Schools reopened.\nPage 2', 'Budget was stable.\nPage 3']. The voiceover says the header 'Annual Review' is removed and the page numbers remain.
- Tanvir and the Dhaka NGO are hypothetical. Do not show personal data in any record printed on screen.
