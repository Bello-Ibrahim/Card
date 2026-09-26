# HeyGen Batch Pack: AI-15 M1 (RAG Foundations)

Course: RAG Systems: Chat with Your Data. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L01 Why RAG? Grounding Answers in Your Data

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M1_L01_presenter.mp4`
- **Expected length:** about 4.9 minutes (675 words). The quality gate accepts ±10%.
- **Pronunciation:** No facts to verify: content.md Review Flags say None. Ingrid and the Bergen marine insurance company are hypothetical; do not show a real insurer's name or logo in stock footage.

```text
Ask a language model about your company's travel policy, and it may give you a confident, well-written answer. But the model has never seen your travel policy. So where did that answer come from? Let's find out, and see how RAG helps.

Hi, and welcome to RAG Systems: Chat with Your Data. In this first lesson, we look at why models need help with your documents, and what retrieval-augmented generation, or RAG, does about it.

A large language model learns from training data that stops at a fixed point in time. So two kinds of knowledge are missing. Anything that happened after training, and anything that was never public, like internal manuals, contracts or support tickets.

When you ask about these things, the model still writes fluent text, because that is what it was trained to do. The result can be a hallucination: an answer that sounds right, but has no source. And because it is well written, it is easy to believe.

Here is a simple way to picture the fix. A closed-book exam tests what a student remembers, and a nervous student may invent an answer. An open-book exam lets the student look up the right page first.

RAG turns the model's closed-book exam into an open-book exam. Before the model answers, the system finds the most relevant passages in your documents and puts them into the prompt. The model's job changes from remembering the answer to reading these passages and reporting what they say, with citations that show which page it used.

A RAG system has six stages, and you will build each one in this course. Loading, chunking, embedding and indexing run when you add documents. Retrieval and generation run for every question.

RAG is not the only option. Long context means pasting whole documents into the prompt, which is fine for a few documents, but slow and costly for hundreds. Fine-tuning is good for style or format, but poor for storing facts. RAG suits large, changing collections that need citations.

Let's see this choice in a real situation. Ingrid is a developer at a marine insurance company in Bergen, Norway. Claims handlers want to ask questions like: does policy type C cover damage from ice in port?

The answers are in about four hundred internal policy documents, and they change every quarter. Long context fails, because the documents do not fit in one prompt, and sending most of them with every question would be costly.

Fine-tuning fails too. Policies change every quarter, and handlers need the exact clause, not a remembered summary. RAG fits. It retrieves the most relevant clauses, the model answers from them, and each answer shows the document and section, so a handler can check it.

Ingrid also notes one risk. Questions that compare two policy types need clauses from both documents. She adds these to her future test questions, because retrieval has to find both. If it finds only one, the answer will be only half right.

One common mistake is to think that RAG makes the model know your documents, so every answer is now safe. The model only knows what retrieval gives it for that question. If the right chunk is missing, it should say I don't know. When an answer is wrong, check retrieval first.

Let's recap. First, a model's training data has a cut-off date and never includes your private documents, so it may give fluent but unsupported answers. Second, RAG has six stages, and the model answers from retrieved passages and cites them. Third, choose RAG for large, changing collections that need citations, long context for a few documents, and fine-tuning for style, not facts.

Now it is your turn. In the exercise below this video, choose a public document collection and write five questions that a model alone cannot answer reliably, with a reason for each. Include one question that needs two documents. Keep the list, because you will use it again. In the next lesson, Embeddings: Meaning as Numbers, we see how a computer measures meaning. See you there.
```

## L02 Embeddings: Meaning as Numbers

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M1_L02_presenter.mp4`
- **Expected length:** about 4.9 minutes (684 words). The quality gate accepts ±10%.
- **Pronunciation:** [VERSION] sentence-transformers API (SentenceTransformer, encode, normalize_embeddings) and current multilingual embedding model names: check at recording time. Do not say the model name in the voiceover; the screen shows whatever model is chosen.

```text
How do I reset my password? I can't log in, I forgot my passcode. These two sentences share almost no words. A keyword search would not match them. Yet a good retrieval system must treat them as the same question.

In the last lesson, we saw the six stages of RAG. Today we look at the stage that makes meaning searchable: embeddings.

An embedding model takes a piece of text and returns a vector, a fixed-length list of numbers, often a few hundred long. The model is trained so that texts with similar meanings get vectors that point in similar directions.

Similar meaning means similar direction. Different meaning means a different direction. That is the whole idea, and it is why embeddings can match two questions that share almost no words, like our password example.

Think of a large library where the librarian places each book on a map by topic, not by title. Books about river pollution end up near books about water treatment, even if their titles share no words.

An embedding places each text at a point on a map of meaning. We measure how close two points are with cosine similarity. It is close to one for very similar meaning, and near zero for unrelated text. If the vectors are normalised, it is simply the dot product. And it can even be negative.

Three practical points matter for RAG. Embed chunks and questions with the same model, because different models make different maps. Multilingual models place the same meaning in different languages close together. And some models expect a short prefix for queries and passages, so read the model card.

Let's try it in a notebook. We use the free, open-source sentence-transformers library, which runs locally. First we load a multilingual model that we chose on the model hub, after checking its card and its licence.

Next we write three sentences. The password question in English, the same question in French, and an unrelated sentence about an invoice. We encode them with normalised vectors, and multiply the matrix by itself to get every pairwise similarity.

You'll see something like this. The shape shows three vectors, each a few hundred numbers long, depending on the model. The English and French password sentences score high with each other, and both score low with the invoice sentence.

Now a real case. Farid builds a help assistant for a tour operator in Marrakesh. Guests write in Arabic, French and English, but the booking policies are only in French. He embeds three policy passages and three guest questions, one in each language, and prints a six by six matrix.

Each question scores highest with the matching French policy, even the Arabic one. But one pair surprises him. A question about bags on the bus scores almost as high with the transfer passage as with the luggage passage, because both mention the bus. Close topics can compete.

Farid learns that embeddings capture topic and meaning, but close topics can compete. He writes two notes for later. Add the section title to each chunk, which we cover in lesson five, and consider reranking, which we cover in lesson seven.

A common mistake is to treat a score as a fixed measure of truth, like anything above zero point seven is relevant. Scores are not comparable between models. Use them to rank results, and never mix vectors from two models in one index.

Let's recap. First, an embedding model turns text into a vector, so that texts with similar meanings are close together, measured with cosine similarity. Second, chunks and questions must use the same model, and multilingual models can match across languages. Third, use similarity to rank passages, and choose any cut-off only by testing on your own data.

Now it is your turn. In the exercise below, embed twelve sentences on four topics in English, French and Arabic, and plot a similarity heatmap. Look for the four bright blocks, and write a short, honest note on any weak matches. In the next lesson, Your First RAG Pipeline, we connect everything and get our first cited answer.
```

## L03 Your First RAG Pipeline

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M1_L03_presenter.mp4`
- **Expected length:** about 5.0 minutes (695 words). The quality gate accepts ±10%.
- **Pronunciation:** [VERSION] Claude API model: read from the CLAUDE_MODEL environment variable, set after checking the current models page at recording time. Never show or say a model ID or price in the voiceover; blur the terminal line if a model ID is visible.

```text
You know the six stages of RAG, and you know how embeddings work. Now we connect them. In about forty lines of Python, you will ask a question about a real report and get an answer that cites its sources.

The goal today is a pipeline that works from end to end, not a perfect one. Each later lesson improves one stage.

There are four steps. First, load one text file and cut it into fixed-size pieces with a small overlap. Second, store the chunks in a local Chroma collection, which calls a sentence-transformers model to embed them for us. Third, send the question to Chroma and get the closest chunks with their IDs. Fourth, send the numbered chunks and the question to the Claude API.

The system prompt is short and strict. Answer only from the context chunks. Cite the chunk IDs. And if the context does not contain the answer, say I don't know. These three rules turn a chatbot into a grounded assistant.

You set up the Anthropic software kit and your API key in the previous course. Remember that the Claude API is paid. So use a smaller model while you develop, keep runs short, and read the model name from an environment variable, instead of writing it into your code.

Think of this first pipeline as a bicycle built from basic parts. It has wheels, brakes and pedals, and it moves. It is not fast or comfortable yet, but you can ride it, and you can see which part to upgrade next.

Let's follow Lucía, a data analyst at an energy research institute in Santiago, Chile. She has a public sixty-page report on renewable energy policy, saved as plain text. First she sets two environment variables in the terminal: her API key, and the model to use. The API is paid, so she picks a smaller model for development.

Here is the script. The chunk function cuts the text into pieces with overlap. A persistent Chroma client saves the index to disk, and each chunk gets an ID like c zero, c one, and so on, plus a source in its metadata. One tip. If you run the add step again with the same IDs, delete the folder first, or use upsert instead.

The ask function queries Chroma for the top four chunks, joins them with their IDs in square brackets, and sends them to Claude with the strict system prompt. It returns both the answer and the retrieved IDs, so we can always check them.

She runs the script once to build the index, and checks the chunk count. Then she asks: what target does the report set for solar capacity? You'll see something like this. An answer that states the target and cites two chunk IDs, with the four retrieved IDs printed next to it.

Lucía opens the two cited chunks and confirms the claims. Then she asks about a topic the report does not cover, and gets, I don't know. That is the right answer. A question whose answer sits in a table gets an incomplete answer, because a fixed-size chunk cut the table in half. She notes this for lesson five.

A common mistake is to change the prompt every time an answer is wrong. Often the right chunk was never retrieved. Always print the retrieved IDs and open them. Not there? Fix retrieval. There, but still wrong? Fix generation.

Let's recap. First, a minimal RAG pipeline chunks, embeds and stores text in Chroma, retrieves the top chunks, and sends them with the question to the Claude API. Second, keep chunk IDs with the text so the model can cite them, and tell it to say I don't know. Third, when an answer is wrong, check retrieval before you change the prompt.

Now build your own. In the exercise below, run the pipeline over one public report and ask it five questions, including one it cannot answer. For each one, record the answer, the retrieved IDs, and whether it was a retrieval or a generation problem. In the next lesson, Loading and Preparing a Document Collection, we move from one clean file to a real collection.
```

## L04 Loading and Preparing a Document Collection

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M1_L04_presenter.mp4`
- **Expected length:** about 4.9 minutes (684 words). The quality gate accepts ±10%.

```text
Your first pipeline used one clean text file. Real collections are not clean. PDFs repeat the same header on every page, and web pages include menus and cookie notices. If this noise goes into your index, it comes back out in your answers.

In the last lesson, we built a pipeline over one file. Today we prepare a whole collection, so that every later stage gets clean input.

Loading has one goal. Turn every source file into a record, with clean text and useful metadata: a document ID, a title, a page, a date, a link, a document type and a language. For PDFs, keep one record per page, so each citation can point to a page.

Each format needs its own tool. For PDFs, a library such as pypdf extracts text page by page, but scanned PDFs contain images, not text. For HTML, BeautifulSoup can remove menus, headers, footers and scripts. For Markdown, keep the headings, because they help with chunking later. Tables often come out as broken lines, so note which documents rely on them.

Metadata does two jobs. It lets an answer cite the title and page with a link, and it lets retrieval filter by year, type or language. Collect it at load time, because it is hard to recover later. And before you index anything, check and record the licence of the collection.

Think of a kitchen preparing ingredients before cooking. You wash the vegetables, remove the parts you cannot eat, and label each container with its contents and date. If you skip this step, every dish that follows has the same problem.

First, a simple and reliable cleaning rule. A line that appears on most pages of the same document is probably a header or footer. This small function counts each line across the pages, and removes any line that appears on at least sixty percent of them.

We test it on three short pages. Each one starts with the same header, Annual Review, then one sentence, then a page number. When we run it, the header is gone from all three pages. The page numbers remain, because each one is different, so we remove them with a small pattern.

Now a full collection. Tanvir is a developer at a development research organisation in Dhaka, Bangladesh. His team wants to ask questions across twenty-five public World Bank reports about education and climate. He downloads the PDFs, and writes the source link and licence of each one into a spreadsheet file.

He loops over the files and extracts text page by page. He cleans each document with the function we just tested, removes page numbers, and builds one record per page, with the ID, title, page, date and link from the spreadsheet. Then he saves everything as JSON Lines, one record per line.

Finally, he prints three random records and reads them. This check finds a problem. Two reports are scanned documents, and their text is empty. He does not index empty pages. He logs the two files in a skipped list, with the reason.

A common mistake is to index raw parser output without looking at it. Then answers contain footer text, and citations cannot point to a page. Always read a sample, and count empty pages. And keep a list of skipped files, with the reason for each one. This list helps you later, when an answer looks strange.

Let's recap. First, turn every source file into records with clean text and metadata, and keep one record per page for PDFs. Second, use a parser that fits each format, remove repeated headers, footers and page numbers, and check samples by eye. Third, check and record the licence of every collection before you index it.

Now it is your turn. In the exercise below, load twenty or more documents from a public collection into clean records with metadata, save them, and keep a short log of any skipped files. Then print three random records and read them, just like Tanvir did. In the next lesson, Chunking Strategies, we cut these records into pieces that retrieval can use well.
```
