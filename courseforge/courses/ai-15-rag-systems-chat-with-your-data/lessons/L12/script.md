# L12 Measuring Answer Quality: Faithfulness and Relevance | Presenter Script

Course: AI-15 · Video: 5 min · Words: 592

## Hook
Retrieval found the right chunk. The model wrote a fluent answer with two citations. But one sentence says something the chunk never said. Retrieval metrics cannot see this problem. You need to check the answer itself.

## Explain
In the last lesson, we measured retrieval. Today we measure the answers, with two metrics that matter most in RAG.

Faithfulness means every claim in the answer is supported by the retrieved chunks. An answer can be true in the real world, and still be unfaithful, if it adds facts the context does not contain. Answer relevance means the answer addresses the question that was asked, completely. And for unanswerable questions, we score correct refusals separately.

Checking every answer by hand is slow, so we ask a model to act as a judge. It gets the question, the chunks and the answer, plus a clear rubric, and returns a structured verdict: faithful yes, partly or no, a list of unsupported claims, and a relevance score from one to three. The judge never sees the expected answer.

Think of a new teaching assistant who marks exam papers with a marking guide. The assistant is fast. But before you trust their marks, the lead teacher marks a sample of the same papers. If they mostly agree, and the differences make sense, the assistant can mark the rest.

## Demonstrate
So a judge must be checked. This small function compares the judge's labels with yours. In the example with five answers, agreement is zero point eight, and there is one difference, on the second answer. The judge said yes, and the human said partly. Read every disagreement like this one.

Now a real evaluation. Kwame is a developer for an agricultural advice service in Kumasi, Ghana. Extension officers ask about crop guidance. He runs twenty-five test questions, twenty answerable and five unanswerable, and saves the question, chunks and answer for each one to a file.

For the twenty answerable ones, he calls the judge with his rubric, and saves the verdicts. You'll see something like a list of verdicts, each with a faithfulness label and any unsupported claims. Before he opens that file, he labels ten answers himself.

Agreement is eight of ten. In both differences, the judge said yes, but the answer added a planting month that was not in the chunks. He changes the rubric: list every claim first, then check each one. He judges again, and agreement rises to nine of ten.

His example results: sixteen of twenty faithful, three partly and one not faithful, and four of five correct refusals. The unfaithful answers share a pattern. The model filled gaps with general farming knowledge, so he strengthens the only from the chunks instruction.

The model API is paid, so keep evaluation small. Use your test set, not thousands of questions. Save answers so you can judge again without generating again. For larger runs, consider batch processing.

## Recap
Let's recap. First, faithfulness checks that every claim is supported by the retrieved chunks, answer relevance checks that the answer addresses the question, and refusals are scored separately. Second, a model judge needs a clear rubric and a structured output, and must be checked against your own labels. Third, keep evaluation cheap with small sets, saved outputs and batches.

## CTA
Now it is your turn. In the exercise below, score twenty answers for faithfulness with a model judge, label ten yourself, and report how often you agree. Explain each disagreement. That completes week three. In the next lesson, Access Control, Freshness and Security, we start preparing your assistant for real users.

## Thumbnail
Headline: Is Every Claim Supported?
Image: Navy background, an answer paragraph with each sentence linked by thin teal lines to source chunks, one sentence with no line marked in amber, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude API batch processing option (interface, discount and delivery time), forced tool use for the judge, and model choice (check the current models page). The voiceover mentions batch processing for larger runs but states no price, discount or delivery time.
- Content check: content.md asks for a forced tool call for the judge, while L08 warns that some current models reject a forced tool_choice. The voiceover says 'structured verdict'. Record the demo with the method that works at recording time. [VERSION]
- [VERSION] Optional open-source RAG evaluation libraries and their metric definitions; none is named in the voiceover.
- The agreement function is tested plain Python: the screen must show exactly 0.8 [(1, 'yes', 'partly')].
- Kwame's results (8 then 9 of 10 agreement; 16 faithful, 3 partly, 1 no; 4 of 5 correct refusals) are hypothetical; the voiceover calls them example results. Judge verdicts on screen come from a real run.
- Kwame and the Kumasi agricultural advice service are hypothetical.
