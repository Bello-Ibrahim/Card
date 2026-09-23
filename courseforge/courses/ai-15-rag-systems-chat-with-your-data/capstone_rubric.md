# Capstone Rubric: Evaluated RAG Assistant over a Real Document Collection

## Task
Build and evaluate a RAG assistant over a real document collection for a named user group. Use open-source embeddings, Chroma (default) or pgvector (optional), and the Claude API. You build the assistant in L15 (capstone step 1). In L16 (capstone step 2) you measure retrieval and answer quality with your own test set, make at least two evidence-based improvements, deploy the assistant, and write a 2-page evaluation report. Use a collection whose licence allows your use, and do not index confidential or personal data without written permission.

## Deliverables
- Source code with separate ingestion, answering and interface files, and one configuration file. No API keys, hard-coded model IDs or hard-coded prices in the code.
- A deployed assistant (URL) or a screen recording of it running, showing cited answers, clickable sources and at least one "I don't know" answer.
- The frozen test set (30–50 items, at least 5 unanswerable) and a results log with at least 3 runs.
- A 2-page evaluation report: purpose, design choices, metrics before and after, improvements (including any that did not help), cost and latency per query, known failures, risks and next steps.

## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| Ingestion and retrieval pipeline | O3 | Clean text with complete metadata (title, page or section, date, URL, access level); chunk size chosen from measured results; Chroma or pgvector with working filters; hybrid retrieval and query rewriting for follow-ups. | Clean text and most metadata; reasonable chunking with some evidence; working vector store and hybrid or rewritten queries. | Pipeline runs but metadata is incomplete, chunking is a default with no evidence, or filters do not work. | No working ingestion or retrieval. | 20 |
| Grounded, cited answers | O4 | Every answer cites valid retrieved chunk IDs checked in code; sources shown as title, page and link; unanswerable questions return a clear "I don't know" reply; chunk text is treated as data, not instructions. | Most answers cite valid sources, and most unanswerable questions are refused. | Citations present but not validated, or the assistant often guesses on unanswerable questions. | No citations, or answers are not based on the retrieved documents. | 20 |
| Test set and measurement | O5 | 30–50 checked items with sources and evidence, at least 5 unanswerable; hit@k, recall@k and MRR at the k in use; faithfulness from an LLM judge checked against human labels on 10+ answers; failures classified by cause. | Test set meets the size rules; retrieval and answer metrics reported; some human check of the judge. | Small or unchecked test set, or only one type of metric, or no check of the judge. | No test set or no metrics. | 20 |
| Evidence-based improvements and trade-offs | O6 | At least 2 changes, each made separately and justified by diagnosed failures; before-and-after metrics for each; cost, latency and access control choices justified with numbers; failed attempts reported. | 2 improvements with before-and-after metrics and a reasonable justification, including cost or latency. | Changes made together or without measurement, or justified by opinion only. | No improvement attempted. | 20 |
| Deployed assistant and evaluation report | O7 | Assistant runs for the user group with a notice and working access control; 2-page report is clear, complete (all six parts) and honest about limits, so a team lead could decide on next steps. | Assistant deployed or recorded; report covers most parts clearly. | Assistant only runs locally with no evidence, or the report is missing several parts or is hard to follow. | No working assistant or no report. | 20 |

Total: 100

## Submission Checklist
- My collection's licence allows my use, and I recorded it in the report.
- I did not index confidential or personal data without written permission.
- My code reads the API key, model name and prices from environment variables or configuration.
- Every answer shows valid, clickable sources, and unanswerable questions get an "I don't know" reply.
- My test set has 30–50 checked items, including at least 5 unanswerable questions, and it was frozen before comparisons.
- I reported hit@k, recall@k, MRR, faithfulness and the correct refusal rate at the k my pipeline uses.
- I checked my LLM judge against my own labels on at least 10 answers.
- I made at least 2 improvements, one at a time, and logged every run.
- I reported cost and latency per query from measured usage.
- I tested that restricted documents do not appear for users without access.
- My report is about 2 pages and includes known failures and next steps.
