# L01 Why RAG? Grounding Answers in Your Data

Course: AI-15 · Module: M1 · Objectives: O1, O2 · Video: 5 min

## Hook
Ask a language model about your company's travel policy and it may give a confident, well-written answer. But the model has never seen your travel policy. So where did the answer come from? This lesson explains why, and how retrieval-augmented generation (RAG) helps.

## Explanation
A large language model (LLM) learns from training data that stops at a fixed point in time. So two kinds of knowledge are missing: anything after training, and anything never public, such as internal manuals, contracts or tickets. When you ask about these, the model still produces fluent text, because that is what it was trained to do. The result can be a hallucination: an answer that sounds right but has no source.

**Retrieval-augmented generation (RAG)** adds a search step before the model answers. The system finds the most relevant passages in your documents and puts them into the prompt, and the model is told to answer from them and cite them. Its job changes from "remember the answer" to "read these passages and report what they say".

**Analogy:** A closed-book exam tests what a student remembers, and a nervous student may invent an answer. An open-book exam lets the student look up the right page first. RAG turns the model's closed-book exam into an open-book exam, and the citations show which page the student used.

A RAG system has six stages. You will build each of them in this course:

1. **Loading:** read documents and keep metadata such as title, page and date.
2. **Chunking:** split documents into short passages called chunks.
3. **Embedding:** turn each chunk into a vector that represents its meaning.
4. **Indexing:** store vectors and metadata in a vector database such as Chroma or pgvector.
5. **Retrieval:** embed the question and find the closest chunks (the top-k results).
6. **Generation:** send the question and chunks to the LLM, which writes a grounded, cited answer.

Stages 1 to 4 run when documents are added (the ingestion pipeline). Stages 5 and 6 run for every question (the query pipeline).

**When to choose RAG.** RAG is not the only way to give a model your data. Compare three options:

- **Long context:** paste whole documents into the prompt. Good for a few documents; slow and costly for hundreds, because every question pays for all the text again.
- **Fine-tuning:** train the model further on your data. Good for style, format or a narrow task; poor for storing facts, because the model still answers from memory, cannot easily cite, and must be retrained when documents change.
- **RAG:** retrieve only the relevant parts per question. Suits large or changing collections, can cite sources, and documents can be updated without retraining.

RAG reduces hallucinations but does not remove them. If retrieval returns the wrong passages, the answer can still be wrong, which is why Week 3 is about evaluation.

## Worked Example
Ingrid is a developer at a hypothetical marine insurance company in Bergen, Norway. Claims handlers want to ask questions such as "Does policy type C cover damage from ice in port?" The answers are in about 400 internal policy documents that change every quarter.

Long context fails: the documents do not fit in one prompt, and sending a large part of them with every question would be costly. Fine-tuning fails: policies change every quarter, and handlers need the exact clause, not a remembered summary. RAG fits: it retrieves the most relevant clauses, the model answers from them, and each answer shows the document and section so a handler can check it.

She notes one risk: questions that compare two policy types need clauses from both documents. She adds these to her future test questions.

## Common Mistake
Many developers think RAG makes a model "know" their documents, so any answer is now safe. The model knows only what retrieval gives it for that question. If the right chunk is missing, the model either says it does not know (good) or fills the gap from memory (bad). When an answer is wrong, check retrieval first, and always tell the model to say "I don't know" when the context does not contain the answer.

## Key Takeaways
1. A model's training data has a cut-off date and never includes your private documents, so it may produce fluent but unsupported answers about them.
2. RAG has six stages: loading, chunking, embedding, indexing, retrieval and generation. The model answers from retrieved passages and cites them.
3. Choose RAG for large, changing collections that need citations; long context for a few documents; and fine-tuning for style or task format, not for storing facts.

## Hands-on Exercise
**Task:** For a public document collection of your choice, write 5 questions that a model alone cannot answer reliably, and explain why.
**Tools:** A text editor or notes app. Optional: a free chat assistant to test your questions without any documents.
**Steps:**
1. Choose a public collection, for example the documentation of an open-source project you use, or public reports from an international organisation. Check that you are allowed to use it. Do not use private or confidential company documents in this course unless you have permission.
2. Write 5 questions whose answers are in the collection. Include at least one question about a recent document, one about a precise number or name, and one that needs information from two documents.
3. For each question, write one sentence explaining why a model without the documents may fail: recent information, private or specialised content, exact numbers, or a need to combine sources.
4. Optional: ask a chat assistant the questions without any documents, and note which answers are wrong or vague.
5. Keep the list. You will reuse it when you build your first pipeline in L03 and your test set in L10.
**What good looks like:** Five specific questions, each linked to a named document in the collection, each with a clear reason. At least one question needs two sources, and none can be answered from general knowledge alone.
**Time:** about 20 minutes

## Review Flags
- None. The lesson uses a hypothetical example and general concepts only; no product versions or statistics need checking.
