# L10 Building a RAG Test Set | Presenter Script

Course: AI-15 · Video: 5 min · Words: 681

## Hook
You changed the chunk size, added hybrid search and rewrote the prompt. Is the system better now? If your answer is, it feels better, you do not know. A small, careful test set turns that feeling into numbers you can compare.

## Explain
In the last lesson, we made answers cite their sources. Before we can measure anything in the next two lessons, we need the questions to measure with.

A RAG test set is a list of questions, each with what you need to judge retrieval and the answer. For a course project, thirty to fifty questions is a good size. Small enough to check by hand and cheap to run, but large enough to show real differences.

Each item has the question in a real user's words, a short expected answer, and the source document. It also has an evidence phrase, a few exact words from the source, so you can find the right chunk whatever the chunk size. And it records whether the question is answerable, its type and its language.

Cover real use, and the hard cases. Different document types and languages. Facts, numbers, codes, and questions that need two sources. A few vague questions, because real users write them. And at least five unanswerable questions on nearby topics, to test whether the system says I don't know.

Think of a restaurant that tests a new recipe. The chef tastes the same dishes before and after the change, including a few difficult orders, so the comparison is fair. A different random dish each time tells you nothing. Your test set is that fixed set of dishes.

## Demonstrate
Let's follow Thandiwe. She runs a research library service at a university in Cape Town, South Africa. Her assistant covers sixty public policy reports in English, and a few summaries in isiZulu and Afrikaans. She gives the model one chunk at a time, and asks it to draft two questions, a short answer and an evidence phrase for each.

You'll see something like fifty drafts. Many copy the chunk's exact words, which makes retrieval look better than it is. So she reviews every one in a spreadsheet. She deletes fourteen that simply repeat a sentence, and rewrites ten to sound like students, like: what did that report say about youth jobs?

Then she writes six unanswerable questions herself, on topics close to the collection but not in it. She adds four questions in isiZulu and Afrikaans, checked by colleagues who speak those languages. A machine check does not replace a native speaker. These questions show whether the multilingual model really works for her users.

Before using the file, she validates it with a short script. It checks for duplicate IDs, makes sure every answerable item has a source and evidence, and counts the mix. The result: forty items, six unanswerable, four types and three languages.

Finally, she saves the file in version control, and agrees a rule with her team. Nobody tunes the system and edits the test set at the same time. Otherwise, the before and after scores are measured on different questions, and the comparison means nothing.

A common mistake is to use drafted questions without checking them. They are often too easy, sometimes wrong, and rarely unanswerable. So check and edit every single item by hand. And never send confidential or personal documents to any API for drafting, unless your organisation allows it.

## Recap
Let's recap. First, a RAG test set of thirty to fifty items records the question, expected answer, source, evidence phrase, answerability, type and language. Second, include different document types, languages, hard cases and at least five unanswerable questions. Third, a model can draft candidates, but a person must check every item, and the set must be frozen before you compare.

## CTA
Now it is your turn. In the exercise below, build a thirty-question test set for your collection, with at least five unanswerable questions, validate it, and tag it as version one. You will use it for the rest of the course, including the capstone. In the next lesson, Measuring Retrieval Quality, we put it to work.

## Thumbnail
Headline: From Feeling to Numbers
Image: Navy background, a clipboard checklist of questions with teal ticks and a few grey 'not in docs' marks, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude API use for drafting candidate questions (model choice read from the environment; check the current models page). Never say a model ID or price.
- Drafted questions shown on screen come from a real API run; the voiceover says 'you'll see something like'.
- Thandiwe's check_testset summary must match content.md: 40 items, 6 unanswerable (34 answerable), 4 types, 3 languages. Prepare testset.jsonl so that the real run prints exactly these counts.
- The isiZulu and Afrikaans questions shown on screen need a native-speaker check before release (course-wide human review item).
- Thandiwe and the Cape Town university library service are hypothetical; the 60 policy reports must be public documents. Do not show personal data.
