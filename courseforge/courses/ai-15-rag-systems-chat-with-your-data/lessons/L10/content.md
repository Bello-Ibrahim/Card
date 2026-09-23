# L10 Building a RAG Test Set

Course: AI-15 · Module: M3 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
You changed the chunk size, added hybrid search and rewrote the prompt. Is the system better now? If your answer is "it feels better", you do not know. A small, careful test set turns that feeling into numbers you can compare.

## Explanation
A **RAG test set** is a list of questions, each with the information needed to judge both retrieval and the answer. A useful size for a course project is **30–50 questions**. That is small enough to check by hand and cheap to run, but large enough to show real differences.

Each item should contain:

- `question`: written the way a real user would ask.
- `expected_answer`: a short reference answer.
- `source`: the document ID (and page or section) that contains the answer.
- `evidence`: a short exact phrase from the source, so you can find the right chunk whatever the chunk size.
- `answerable`: `true` or `false`.
- `type` and `language`: for example "fact", "comparison", "number", "follow-up"; "en", "fr".

```json
{"id": "t07", "question": "Which regions had the largest fall in school enrolment?",
 "expected_answer": "The northern and coastal regions.", "source": "rep-12#p4",
 "evidence": "largest decline in the northern and coastal", "answerable": true,
 "type": "comparison", "language": "en"}
```

**Coverage.** A good test set looks like real use, and also includes hard cases:

- Different document types (reports, FAQs, tables) and languages.
- Simple facts, numbers, names and codes, and questions that need two sources.
- **Unanswerable questions** (at least 5, or about 15%): questions on nearby topics that the documents do not cover. These test whether the system says "I don't know".
- A few vague or badly written questions, because real users write them.

**Drafting with an LLM, then checking by hand.** Writing 40 questions by hand is slow. You can give the model one chunk at a time and ask it to draft a question, a short answer and an evidence phrase. This is fast, but drafted questions often copy the chunk's exact words, which makes retrieval look better than it is. So you **check and edit every item by hand**: rewrite questions in a user's words, delete trivial ones, fix answers, and write the unanswerable questions yourself. Do not send confidential or personal documents to any API for drafting unless your organisation allows it.

Validate the file with a short script before you use it:

```python
import json
from collections import Counter

def check_testset(path):
    items = [json.loads(line) for line in open(path, encoding="utf-8")]
    ids = [it["id"] for it in items]
    assert len(ids) == len(set(ids)), "duplicate ids"
    for it in items:
        if it["answerable"]:
            assert it["source"] and it["evidence"], f"{it['id']} missing source"
    print(len(items), "items")
    print("unanswerable:", sum(not it["answerable"] for it in items))
    print("types:", Counter(it["type"] for it in items))
    print("languages:", Counter(it["language"] for it in items))
```

**Analogy:** A test set is like the set of test dishes a restaurant cooks before it changes a recipe. The chef tastes the same dishes before and after the change, including a few difficult orders, so the comparison is fair. Tasting a different random dish each time tells you nothing about the change.

## Worked Example
Thandiwe runs a hypothetical research library service at a university in Cape Town, South Africa. Her RAG assistant covers 60 public policy reports in English and a few summaries in isiZulu and Afrikaans.

On screen, follow her process:

1. She asks the LLM to draft 2 questions for each of 25 selected chunks, giving 50 drafts in `drafts.jsonl`.
2. She reviews them in a spreadsheet. She deletes 14 that simply repeat a sentence from the chunk, and rewrites 10 to sound like students ("what did that report say about youth jobs?").
3. She writes 6 unanswerable questions herself, on topics close to the collection but not in it.
4. She adds 4 questions in isiZulu and Afrikaans, checked by colleagues who speak those languages.
5. She runs `check_testset` and gets 40 items: 34 answerable, 6 unanswerable, 4 types, 3 languages.

She saves the file in version control and agrees a rule with her team: nobody tunes the system by looking at test answers and editing the test set at the same time.

## Common Mistake
The most common mistake is to use LLM-drafted questions without checking them. They are often too easy, sometimes wrong, and they rarely include unanswerable cases. A second mistake is to keep changing the test set while tuning, so "before" and "after" scores are measured on different questions. Freeze a version before you compare.

## Key Takeaways
1. A RAG test set of 30–50 items records question, expected answer, source, evidence phrase, answerability, type and language.
2. Include different document types, languages, hard cases and at least 5 unanswerable questions.
3. An LLM can draft candidates, but every item must be checked and edited by a person, and the set must be frozen before comparisons.

## Hands-on Exercise
**Task:** Build a 30-question test set for your collection, including at least 5 unanswerable questions.
**Tools:** Python 3, a spreadsheet or text editor, optionally the Claude API for drafting (paid; draft in small batches). [VERSION]
**Steps:**
1. Select 15–20 chunks from different documents and types.
2. Optional: ask the LLM to draft one question, answer and evidence phrase for each chunk.
3. Review every draft: rewrite in a user's words, fix answers, delete trivial ones.
4. Add your own questions, including 2 comparisons and 5 unanswerable questions.
5. Save as `testset.jsonl` and run `check_testset`.
6. Commit the file and tag it as version 1.
**What good looks like:** 30+ checked items with complete fields, at least 5 unanswerable questions, a mix of types (and languages, if your collection has them), and a clean validation output.
**Time:** about 50 minutes

## Review Flags
- [VERSION] Claude API use for drafting candidate questions (model choice; check the current models page).
