# L03 Your First RAG Pipeline

Course: AI-15 · Module: M1 · Objectives: O1, O3, O4 · Video: 5 min (screen demo)

## Hook
You now know the six stages of RAG and how embeddings work. In this lesson you connect them. In about 40 lines of Python you will ask a question about a real report and get an answer that cites the passages it used.

## Explanation
The goal today is a pipeline that works end to end, not a perfect one. Every later lesson improves one stage. Here is the plan:

1. **Load and chunk:** read one text file and cut it into fixed-size pieces with a small overlap.
2. **Embed and index:** store the chunks in a local Chroma collection. Chroma calls a sentence-transformers model for us through an embedding function.
3. **Retrieve:** send the question to Chroma and get the top-k closest chunks with their IDs.
4. **Generate:** send the numbered chunks and the question to the Claude API with a system prompt that asks for a grounded answer with citations.

You set up the Anthropic SDK and your API key in AI-14. The Claude API is paid, so use a smaller model during development and keep test runs short. Never hard-code a model ID: read it from an environment variable that you set after checking the current models page. [VERSION]

```python
import os
import anthropic
import chromadb
from chromadb.utils import embedding_functions

MODEL = os.environ["CLAUDE_MODEL"]  # check the current models page [VERSION]
EMBED_MODEL = "your-embedding-model"  # [VERSION] [VERIFY licence]

def chunk(text, size=800, overlap=100):
    step = size - overlap
    return [text[i:i + size] for i in range(0, len(text), step)]

chunks = chunk(open("report.txt", encoding="utf-8").read())

db = chromadb.PersistentClient(path="./rag_db")  # [VERSION]
ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
col = db.get_or_create_collection("report", embedding_function=ef)
col.add(ids=[f"c{i}" for i in range(len(chunks))], documents=chunks,
        metadatas=[{"source": "report.txt"} for _ in chunks])

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
SYSTEM = ("Answer only from the context chunks. Cite chunk IDs like [c3]. "
          "If the context does not contain the answer, say: I don't know.")

def ask(question, k=4):
    res = col.query(query_texts=[question], n_results=k)
    context = "\n\n".join(f"[{i}] {d}" for i, d in
                          zip(res["ids"][0], res["documents"][0]))
    msg = client.messages.create(
        model=MODEL, max_tokens=500, system=SYSTEM,
        messages=[{"role": "user",
                   "content": f"Context:\n{context}\n\nQuestion: {question}"}])
    return msg.content[0].text, res["ids"][0]
```

Note three details. First, `query` returns lists of lists, one list per question, so we take index `[0]`. Second, the chunk IDs travel with the text, which lets the model cite them. Third, `PersistentClient` saves the index to disk, so later runs can skip ingestion. If you re-run the `add` line with the same IDs, delete the folder first or use `upsert` instead. [VERSION]

**Analogy:** This first pipeline is like a bicycle built from basic parts: it has wheels, brakes and pedals, and it moves. It is not fast or comfortable yet, but you can ride it, and you can see which part to upgrade next.

## Worked Example
Lucía is a data analyst at a hypothetical energy research institute in Santiago, Chile. She loads a public 60-page report on renewable energy policy, saved as plain text, and runs the pipeline.

On screen, follow her steps:

1. Set the environment variables `ANTHROPIC_API_KEY` and `CLAUDE_MODEL` in the terminal.
2. Run the script once to build the index and check the chunk count with `col.count()`.
3. Call `ask("What target does the report set for solar capacity?")`.
4. Print the answer and the retrieved IDs side by side.

Example output (the API was not run for this script; wording will differ):

```
The report sets a target for solar capacity in the national plan [c41],
and says progress is reviewed every two years [c42].
Retrieved: ['c41', 'c42', 'c7', 'c88']
```

Lucía opens chunks c41 and c42 and confirms the claims are there. Then she asks about a topic the report does not cover, electric vehicle sales, and the model replies "I don't know." Finally, she asks a question whose answer sits in a table. The answer is incomplete, because the fixed-size chunk cut the table in half. She writes this down for L05.

## Common Mistake
Many learners judge the pipeline only by reading the final answers. When an answer is wrong, they change the prompt. Often the real problem is retrieval: the right chunk was never in the top-k list. Always print the retrieved IDs and open them. If the answer is not in the retrieved chunks, fix retrieval; if it is there and the answer is still wrong, fix generation.

## Key Takeaways
1. A minimal RAG pipeline is chunk, embed and store in Chroma, retrieve the top-k chunks, then send numbered chunks and the question to the Claude API.
2. Keep chunk IDs with the text so the model can cite them, and tell it to say "I don't know" when the context does not contain the answer.
3. When an answer is wrong, first check whether the right chunk was retrieved, before changing the prompt.

## Hands-on Exercise
**Task:** Build the minimal pipeline over one public report and ask it 5 questions, noting which answers are correct.
**Tools:** Python 3, chromadb, sentence-transformers and the anthropic SDK (free to install); a Claude API key (paid, keep runs small); one public report saved as text. [VERSION]
**Steps:**
1. Choose one public report whose licence allows reuse, and save it as `report.txt`. Do not use confidential or personal documents. [VERIFY]
2. Install the libraries: `pip install chromadb sentence-transformers anthropic`.
3. Set `ANTHROPIC_API_KEY` and `CLAUDE_MODEL` (a smaller, lower-cost model for development).
4. Run the code above and check `col.count()`.
5. Ask 5 questions, including 1 whose answer is not in the report. Reuse questions from L01 if they fit.
6. For each question, record the answer, the retrieved IDs, whether the answer is correct, and whether the right chunk was retrieved.
**What good looks like:** A working script, a table of 5 questions with answers, retrieved IDs and correct/incorrect labels, and the unanswerable question answered with "I don't know". Each wrong answer is labelled as a retrieval or a generation problem.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Claude API: model choice is read from an environment variable; the current models page must be checked at recording time. The Claude API is paid; confirm current pricing guidance for learners. [VERIFY] realistic cost per learner (course-level flag).
- [VERSION] Chroma client API: `PersistentClient`, `get_or_create_collection`, `add`, `upsert`, `query` return format and `SentenceTransformerEmbeddingFunction`; the API changed between major versions.
- [VERSION] Embedding model name; [VERIFY] its licence and the licence of the example report.
- The example output is illustrative and must be replaced by a real run.
