# L01 Why RAG? Grounding Answers in Your Data | Presenter Script

Course: AI-15 · Video: 5 min · Words: 685

## Hook
Ask a language model about your company's travel policy, and it may give you a confident, well-written answer. But the model has never seen your travel policy. So where did that answer come from? Let's find out, and see how RAG helps.

## Explain
Hi, and welcome to RAG Systems: Chat with Your Data. In this first lesson, we look at why models need help with your documents, and what retrieval-augmented generation, or RAG, does about it.

A large language model learns from training data that stops at a fixed point in time. So two kinds of knowledge are missing. Anything that happened after training, and anything that was never public, like internal manuals, contracts or support tickets.

When you ask about these things, the model still writes fluent text, because that is what it was trained to do. The result can be a hallucination: an answer that sounds right, but has no source. And because it is well written, it is easy to believe.

Here is a simple way to picture the fix. A closed-book exam tests what a student remembers, and a nervous student may invent an answer. An open-book exam lets the student look up the right page first.

RAG turns the model's closed-book exam into an open-book exam. Before the model answers, the system finds the most relevant passages in your documents and puts them into the prompt. The model's job changes from remembering the answer to reading these passages and reporting what they say, with citations that show which page it used.

A RAG system has six stages, and you will build each one in this course. Loading, chunking, embedding and indexing run when you add documents. Retrieval and generation run for every question.

RAG is not the only option. Long context means pasting whole documents into the prompt, which is fine for a few documents, but slow and costly for hundreds. Fine-tuning is good for style or format, but poor for storing facts. RAG suits large, changing collections that need citations.

## Demonstrate
Let's see this choice in a real situation. Ingrid is a developer at a marine insurance company in Bergen, Norway. Claims handlers want to ask questions like: does policy type C cover damage from ice in port?

The answers are in about four hundred internal policy documents, and they change every quarter. Long context fails, because the documents do not fit in one prompt, and sending most of them with every question would be costly.

Fine-tuning fails too. Policies change every quarter, and handlers need the exact clause, not a remembered summary. RAG fits. It retrieves the most relevant clauses, the model answers from them, and each answer shows the document and section, so a handler can check it.

Ingrid also notes one risk. Questions that compare two policy types need clauses from both documents. She adds these to her future test questions, because retrieval has to find both. If it finds only one, the answer will be only half right.

One common mistake is to think that RAG makes the model know your documents, so every answer is now safe. The model only knows what retrieval gives it for that question. If the right chunk is missing, it should say I don't know. When an answer is wrong, check retrieval first.

## Recap
Let's recap. First, a model's training data has a cut-off date and never includes your private documents, so it may give fluent but unsupported answers. Second, RAG has six stages, and the model answers from retrieved passages and cites them. Third, choose RAG for large, changing collections that need citations, long context for a few documents, and fine-tuning for style, not facts.

## CTA
Now it is your turn. In the exercise below this video, choose a public document collection and write five questions that a model alone cannot answer reliably, with a reason for each. Include one question that needs two documents. Keep the list, because you will use it again. In the next lesson, Embeddings: Meaning as Numbers, we see how a computer measures meaning. See you there.

## Thumbnail
Headline: Open-Book Answers
Image: Navy background, an open book with a glowing highlighted passage and a thin teal line leading to a speech bubble, headline in teal Inter Bold.

## Production Notes
- No facts to verify: content.md Review Flags say None. Ingrid and the Bergen marine insurance company are hypothetical; do not show a real insurer's name or logo in stock footage.
- L01 is not a screen demo lesson: diagrams and stock only, as planned in curriculum.json.
- Keep the six-stage diagram from scene 6 as a reusable asset; later lessons refer back to it.
