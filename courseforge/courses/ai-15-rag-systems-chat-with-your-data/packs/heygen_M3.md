# HeyGen Batch Pack: AI-15 M3 (Grounded Generation and Evaluation)

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

## L09 Grounded Answers with Citations

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M3_L09_presenter.mp4`
- **Expected length:** about 4.9 minutes (689 words). The quality gate accepts ±10%.

```text
Your assistant says tenants must give sixty days' notice. Is that from the guide you indexed, or a rule the model remembered from another country? Without a citation, the user cannot tell. Without a clear I don't know, they cannot tell when to stop trusting it.

Welcome to week three. We start with the heart of RAG: grounded answers that show their sources. In lesson three, our first prompt was only one line. Today we make it strict, and we check the result in code.

A grounded answer uses only the retrieved context, and every claim can be traced to a chunk. Three instructions make this work. Answer only from the context. Cite the chunk ID after each claim. And when the context does not contain the answer, say I don't know, and do not guess.

Give the model the chunks in a clear format. Each chunk sits inside tags, with its ID and its source title and page in the header. The tags also tell the model that the chunk text is material to read, not instructions to follow. We return to that in lesson thirteen.

For an application, JSON is better than brackets in free text. So we ask for a structured output with three fields: the answer, a list of cited IDs, and a found flag. There is also another route. The Claude API has a citations feature that points to the exact passage used. Check the current documentation, because it may not combine with structured outputs in one request.

Think of a good student essay with footnotes. Every important claim points to a page in the course reader. And if the reader does not cover a topic, the student says so, instead of inventing a source. That honesty is what makes the essay trustworthy.

Let's follow Priya. She builds a question-answering tool for a legal aid clinic in Pune, India. Volunteers answer tenants' questions from a public guide to rental rules. Rules differ by place, so the guide is the only source the tool may use. First, she replaces her old one-line prompt with the strict system prompt and the context formatter.

Next, she adds the structured output with answer, citations and found, and a small check in code. It fails if any cited ID was not retrieved, or if the answer says found but cites nothing. On the example, the check passes and prints True.

She asks: how much deposit can a landlord ask for? You'll see something like an answer that cites two chunks, and the check passes. She opens both chunks and confirms the numbers. In the interface, each citation shows the document title and page, with a link.

Now three questions the guide does not cover: rules in another country, a tax question, and a question about a named landlord. At first, the tax question gets a general answer with no citations. After she adds the word exactly to the prompt, and the found check in code, all three return found false and the exact I don't know sentence.

A common mistake is to ask for citations but never check them. Models can cite an ID that was not in the context. Validate IDs in code, and sample answers by hand. The check does not prove support. That is faithfulness, which we measure in lesson twelve. And never hide I don't know as an error.

Let's recap. First, tell the model to answer only from the numbered chunks, cite chunk IDs, and say I don't know when the context does not contain the answer. Second, return the answer, citations and a found flag as structured output, and check in code that every cited ID was retrieved. Third, the API's citations feature can point to exact passages, so check how it fits your request.

Now it is your turn. In the exercise below, change your pipeline so every answer lists its sources, and test it with three questions your documents cannot answer. Treat a clear I don't know as a success. In the next lesson, Building a RAG Test Set, we create the questions that tell us whether all this really works.
```

## L10 Building a RAG Test Set

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M3_L10_presenter.mp4`
- **Expected length:** about 4.9 minutes (680 words). The quality gate accepts ±10%.
- **Pronunciation:** [VERSION] Claude API use for drafting candidate questions (model choice read from the environment; check the current models page). Never say a model ID or price.

```text
You changed the chunk size, added hybrid search and rewrote the prompt. Is the system better now? If your answer is, it feels better, you do not know. A small, careful test set turns that feeling into numbers you can compare.

In the last lesson, we made answers cite their sources. Before we can measure anything in the next two lessons, we need the questions to measure with.

A RAG test set is a list of questions, each with what you need to judge retrieval and the answer. For a course project, thirty to fifty questions is a good size. Small enough to check by hand and cheap to run, but large enough to show real differences.

Each item has the question in a real user's words, a short expected answer, and the source document. It also has an evidence phrase, a few exact words from the source, so you can find the right chunk whatever the chunk size. And it records whether the question is answerable, its type and its language.

Cover real use, and the hard cases. Different document types and languages. Facts, numbers, codes, and questions that need two sources. A few vague questions, because real users write them. And at least five unanswerable questions on nearby topics, to test whether the system says I don't know.

Think of a restaurant that tests a new recipe. The chef tastes the same dishes before and after the change, including a few difficult orders, so the comparison is fair. A different random dish each time tells you nothing. Your test set is that fixed set of dishes.

Let's follow Thandiwe. She runs a research library service at a university in Cape Town, South Africa. Her assistant covers sixty public policy reports in English, and a few summaries in isiZulu and Afrikaans. She gives the model one chunk at a time, and asks it to draft two questions, a short answer and an evidence phrase for each.

You'll see something like fifty drafts. Many copy the chunk's exact words, which makes retrieval look better than it is. So she reviews every one in a spreadsheet. She deletes fourteen that simply repeat a sentence, and rewrites ten to sound like students, like: what did that report say about youth jobs?

Then she writes six unanswerable questions herself, on topics close to the collection but not in it. She adds four questions in isiZulu and Afrikaans, checked by colleagues who speak those languages. A machine check does not replace a native speaker. These questions show whether the multilingual model really works for her users.

Before using the file, she validates it with a short script. It checks for duplicate IDs, makes sure every answerable item has a source and evidence, and counts the mix. The result: forty items, six unanswerable, four types and three languages.

Finally, she saves the file in version control, and agrees a rule with her team. Nobody tunes the system and edits the test set at the same time. Otherwise, the before and after scores are measured on different questions, and the comparison means nothing.

A common mistake is to use drafted questions without checking them. They are often too easy, sometimes wrong, and rarely unanswerable. So check and edit every single item by hand. And never send confidential or personal documents to any API for drafting, unless your organisation allows it.

Let's recap. First, a RAG test set of thirty to fifty items records the question, expected answer, source, evidence phrase, answerability, type and language. Second, include different document types, languages, hard cases and at least five unanswerable questions. Third, a model can draft candidates, but a person must check every item, and the set must be frozen before you compare.

Now it is your turn. In the exercise below, build a thirty-question test set for your collection, with at least five unanswerable questions, validate it, and tag it as version one. You will use it for the rest of the course, including the capstone. In the next lesson, Measuring Retrieval Quality, we put it to work.
```

## L11 Measuring Retrieval Quality

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (680 words). The quality gate accepts ±10%.

```text
If the right chunk never reaches the model, the answer cannot be both correct and grounded. So before you judge answers, measure retrieval. It is fast, it needs no model calls, and it shows exactly where your pipeline loses information.

In the last lesson, we built a test set. For each answerable question, we know which chunks are relevant: the ones from the expected source that contain the evidence phrase. Retrieval returns a ranked list. Three metrics compare the two.

Hit rate at k is the share of questions where at least one relevant chunk is in the top k. It asks: does the model get a chance to see the answer? Recall at k is the share of each question's relevant chunks found in the top k. It matters when an answer needs several chunks, such as a comparison.

Mean reciprocal rank, or MRR, shows how high the first relevant chunk is. Rank one scores one. Rank two scores a half. Rank four scores a quarter. Nothing found scores zero. This matters when you pass only a few chunks to the model. Skip unanswerable questions here. We test those with answer metrics next time.

Think of a doctor's basic measurements: temperature, pulse and blood pressure. They quickly tell you that something is wrong, and how serious it is. But to treat the patient, the doctor still has to examine them and find the cause. Retrieval metrics work the same way.

Here is the metrics function in plain Python. We test it on three questions. The first finds its chunk at rank one. The second finds one of its two relevant chunks, at rank three. The third finds nothing. The result: hit rate zero point six six seven, recall zero point five, and MRR zero point four four four.

Now a real comparison. Hana is an engineer at an insurance company in Prague, Czech Republic. Her assistant answers questions about claims procedures. Version A uses vector search only. Version B uses the same chunks, with hybrid search. She runs both over thirty-two answerable test questions, and saves the top ten IDs for each.

She computes the metrics at five, because her pipeline passes five chunks to the model. Here are her example results. Version A has a hit rate of zero point seven two, and an MRR of zero point five one. Version B reaches zero point eight four and zero point six three. B is better.

But numbers do not say why. So she lists the five questions that B still fails, and opens the retrieved chunks and the relevant chunk for each one. Two are chunking problems, where a table was split. One is embeddings, with a Czech legal term. One is a vague question. One is parsing, a scanned appendix.

The failure analysis gives her a clear next step. Fix table chunking first, because it causes the most failures. Other common causes are missing keywords, where hybrid search helps, and vague questions, where rewriting helps. Parsing problems need the text extracted again.

A common mistake is to report hit at ten, when you only pass five chunks to the model. Report metrics at the k you actually use, add MRR, and always read the failures. And after re-chunking, do not match relevant chunks by their old IDs. Match by source and evidence phrase instead.

Let's recap. First, hit rate and recall at k show whether relevant chunks reach the model, and MRR shows how high the first one is ranked. Second, measure at the k your pipeline really uses, on answerable questions from a frozen test set. Third, classify each failure by cause, to decide what to fix next.

Now it is your turn. In the exercise below, compute hit rate, recall at five and MRR for two versions of your pipeline, and classify the causes of five failures. Then write one sentence on what you would fix first, and why. It needs no model calls, so it costs nothing to run. In the next lesson, Measuring Answer Quality: Faithfulness and Relevance, we check the answers themselves.
```

## L12 Measuring Answer Quality: Faithfulness and Relevance

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M3_L12_presenter.mp4`
- **Expected length:** about 5.0 minutes (704 words). The quality gate accepts ±10%.

```text
Retrieval found the right chunk. The model wrote a fluent answer with two citations. But one sentence says something the chunk never said. The citations look fine. But retrieval metrics cannot see this problem. You need to check the answer itself.

In the last lesson, we measured retrieval. Today we measure the answers, with two metrics that matter most in RAG. Both need care, because the judge is also a model.

Faithfulness means every claim in the answer is supported by the retrieved chunks. An answer can be true in the real world, and still be unfaithful, if it adds facts the context does not contain. Answer relevance means the answer addresses the question that was asked, completely. And for unanswerable questions, we score correct refusals separately.

Checking every answer by hand is slow, so we ask a model to act as a judge. It gets the question, the chunks and the answer, plus a clear rubric, and returns a structured verdict: faithful yes, partly or no, a list of unsupported claims, and a relevance score from one to three. The judge never sees the expected answer.

Two rules for the judge. Use a different prompt, and if possible a different or stronger model, than the one that wrote the answer. And score faithfulness against the chunks only. Comparing with the expected answer measures correctness, which is useful, but it is a different question.

Think of a new teaching assistant who marks exam papers with a marking guide. The assistant is fast. But before you trust their marks, the lead teacher marks a sample of the same papers. If they mostly agree, and the differences make sense, the assistant can mark the rest.

So a judge must be checked. This small function compares the judge's labels with yours. In the example with five answers, agreement is zero point eight, and there is one difference, on the second answer. The judge said yes, and the human said partly. Read every disagreement like this one.

Now a real evaluation. Kwame is a developer for an agricultural advice service in Kumasi, Ghana. Extension officers ask about crop guidance. He runs twenty-five test questions, twenty answerable and five unanswerable, and saves the question, chunks and answer for each one to a file.

For the twenty answerable ones, he calls the judge with his rubric, and saves the verdicts. You'll see something like a list of verdicts, each with a faithfulness label and any unsupported claims. Before he opens that file, he labels ten answers himself.

Agreement is eight of ten. In both differences, the judge said yes, but the answer added a planting month that was not in the chunks. He changes the rubric: list every claim first, then check each one. He judges again, and agreement rises to nine of ten.

His example results: sixteen of twenty faithful, three partly and one not faithful, and four of five correct refusals. The unfaithful answers share a pattern. The model filled gaps with general farming knowledge, so he strengthens the only from the chunks instruction.

A common mistake is to report a judge's score as if it were the truth. Without a human check on a sample, you do not know if the judge is strict, generous or random.

The model API is paid, so keep evaluation small. Use your test set, not thousands of questions. Save answers so you can judge again without generating again. For larger runs, consider batch processing. And if you use an open-source evaluation library, read how it defines each metric, because definitions differ.

Let's recap. First, faithfulness checks that every claim is supported by the retrieved chunks, answer relevance checks that the answer addresses the question, and refusals are scored separately. Second, a model judge needs a clear rubric and a structured output, and must be checked against your own labels. Third, keep evaluation cheap with small sets, saved outputs and batches.

Now it is your turn. In the exercise below, score twenty answers for faithfulness with a model judge, label ten yourself, and report how often you agree. Explain each disagreement. That completes week three. In the next lesson, Access Control, Freshness and Security, we start preparing your assistant for real users.
```
