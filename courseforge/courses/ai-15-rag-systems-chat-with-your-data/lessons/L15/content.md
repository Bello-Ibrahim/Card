# L15 Capstone Step 1: Build Your RAG Assistant

Course: AI-15 · Module: M4 · Objectives: O3, O4, O7 · Video: 5 min (screen demo)

## Hook
You have built every stage of a RAG system in separate exercises. Now you put them together for real users with a real collection. The question changes from "does this technique work?" to "would these people trust this assistant with their work?"

## Explanation
Your capstone is a RAG assistant for a named user group over a real document collection. Step 1 (this lesson) is the build. Step 2 (L16) is evaluation, improvement and the report.

**Choose the collection and users together.** A good capstone has a clear pair, for example:

- Public health guidance for clinic staff in Kenya.
- Open-source project documentation for developers in Brazil, with questions in Portuguese and documents in English.
- Public agricultural bulletins for farm advisers, or a city's published regulations for small business owners.

Check three things before you start: the licence allows your use [VERIFY]; the collection has at least 30 documents or 300 chunks, so retrieval is not trivial; and you can write test questions that real users would ask. Do not use confidential company documents or personal data unless you have written permission. For health, legal or financial topics, show a notice that the assistant supports but does not replace professional judgement.

**Required pipeline.** Reuse your code from earlier lessons:

1. **Loading** with clean text and metadata: title, page or section, date, URL, type, language, access level (L04).
2. **Chunking** with the size you chose from evidence, and titles in chunks (L05).
3. **Indexing** in Chroma (default) or pgvector (optional) with metadata filters (L06).
4. **Hybrid retrieval** with BM25, RRF and optionally a reranker (L07), plus query rewriting for follow-ups (L08).
5. **Grounded generation** with the Claude API, chunk-ID citations, validated sources and the "I don't know" reply (L09).
6. A **simple web interface** that shows the answer and clickable sources.

Keep the project organised so step 2 is easy: `ingest.py` builds the index, `rag.py` contains `answer_with_sources()`, and `app.py` is the interface. Put settings such as chunk size, k, `MODEL` and prices in one `config.py` file, read from environment variables where needed.

A minimal Streamlit interface: [VERSION]

```python
import streamlit as st
from rag import answer_with_sources

st.title("Clinic Guidance Assistant")
st.caption("Answers come only from the indexed guidance. Check the sources.")
question = st.chat_input("Ask a question")
if question:
    st.chat_message("user").write(question)
    result = answer_with_sources(question, role="staff")
    with st.chat_message("assistant"):
        st.write(result["answer"])
        for src in result["sources"]:
            st.markdown(f"- [{src['title']}, p.{src['page']}]({src['url']})")
```

Run it with `streamlit run app.py`.

**Analogy:** Building the capstone is like assembling a kitchen from parts you tested one by one: the oven works, the tap works, the fridge works. Now you connect them in one room for a specific cook, and discover problems that only appear when the parts work together.

## Worked Example
Wanjiru is a developer volunteering for a hypothetical network of community clinics near Kisumu, Kenya. Clinic staff need quick answers from public health guidance documents, such as vaccination schedules and referral steps. [VERIFY] licence and reuse terms of the public health guidance.

On screen, follow her build:

1. She collects 45 public guidance PDFs, records each URL and licence, and runs `ingest.py`. The log shows 2 scanned files skipped.
2. She chooses 800-character sentence chunks with section titles, based on a quick hit@5 check.
3. She stores 2,900 chunks in Chroma with metadata, including `year`, so answers prefer current guidance.
4. She connects hybrid retrieval, reranking and the grounded prompt with a forced tool output for answer, citations and `found`.
5. She builds the Streamlit app with a notice at the top and clickable sources.
6. She asks 5 real-style questions, including one in Kiswahili, and one about a drug not in the guidance. The last one returns "I don't know. The documents do not contain this information."

She writes her open issues in a `NOTES.md` file: tables in dosage charts are sometimes split, and two guidance versions overlap. These become her first candidates for improvement in L16.

## Common Mistake
Learners often choose a collection that is too small or too easy, such as one document, and then every metric looks perfect. Others choose a huge collection and spend the whole week on ingestion. Aim for a collection that is realistic but manageable, and make the pipeline work end to end on a small part before loading everything.

## Key Takeaways
1. Choose a real, licensed collection and a named user group together, and check that real users would ask questions it can answer.
2. Combine the stages you built: clean metadata, evidence-based chunking, Chroma or pgvector, hybrid retrieval, query rewriting and grounded, cited answers.
3. Organise the code into ingestion, answering and interface files with one configuration file, so evaluation in step 2 is easy.

## Hands-on Exercise
**Task:** Capstone step 1: build the RAG assistant over your chosen collection, with cited answers in a simple web interface.
**Tools:** Python 3, sentence-transformers, Chroma (or pgvector), rank_bm25, the anthropic SDK (paid; use a smaller model while building), Streamlit or FastAPI. [VERSION]
**Steps:**
1. Write one paragraph naming your user group, the collection, its licence and 3 example questions. [VERIFY]
2. Build `ingest.py` and index the collection; record skipped files.
3. Build `rag.py` with hybrid retrieval, query rewriting and grounded answers with validated citations.
4. Build `app.py` with a notice and clickable sources.
5. Test with 5 questions, including 1 unanswerable and 1 follow-up.
6. Record a short screen video or screenshots of the working assistant.
**What good looks like:** A working assistant that answers from the collection, shows valid sources for every answer, says "I don't know" when it should, and has a clear project structure and notes on known issues.
**Time:** about 120 minutes

## Review Flags
- [VERIFY] Licences of the example collections: public health guidance and open-source documentation (course-level flag).
- [VERSION] Streamlit chat API (`chat_input`, `chat_message`) and all libraries used in the pipeline; Claude model choice (check the current models page).
- Health example: the assistant must display a notice that it does not replace professional judgement.
