# L16 Capstone Step 2: Evaluate, Improve and Report | Presenter Script

Course: AI-15 · Video: 5 min · Words: 681

## Hook
Your assistant works in a demo. Now a team lead asks: how good is it, what did you change, and what will it cost? In this final step, you answer with evidence, and a short report that someone else can act on.

## Explain
In the last lesson, you built your assistant. Step two follows a simple loop. Measure, diagnose, change one thing, and measure again. It sounds simple, but it is the habit that separates a demo from a system people can trust.

First, the baseline. Freeze your test set and run the full pipeline once. Record retrieval metrics at the k you use, faithfulness and relevance from your checked judge, the correct refusal rate on unanswerable questions, and cost and latency per query.

Then diagnose. Classify failures by cause, and choose improvements that target the most common cause, not the technique you like most. Make at least two improvements, one at a time, and re-run the same test set after each. Log every run's settings and scores in one results file, so your report tables come straight from data.

Think of a building inspector's report on a new house. It does not only say the house is good. It lists what was tested, the measurements, the repairs made, and the problems still to fix, so the owner can decide what to do next.

Next, deploy. Run the assistant where your user group could reach it, even if that is only a shared internal server, or a free hosting plan for the demo. Keep the API key on the server, and apply your access control filter from lesson thirteen.

## Demonstrate
Let's follow Camila in Belo Horizonte, Brazil. She builds an assistant over a web framework's English documentation, for Brazilian developers who ask in Portuguese. Here are her example results. Her baseline, version one, has a hit rate at five of zero point seven zero, an MRR of zero point five two, faithfulness of zero point eight zero, and four of six correct refusals.

Her diagnosis: most failures are code names, such as function names, plus two Portuguese questions with technical terms. So change one is hybrid search with rank fusion. The hit rate rises to zero point eight three, and faithfulness stays the same. Hybrid search targets exactly that cause.

Change two is a stricter prompt, with reply exactly for refusals, and a citation for every claim. Correct refusals rise to six of six, and faithfulness to zero point nine zero. Every I don't know is now a real, correct answer.

She also tried a reranker. It added time, with no gain on her test set, so she removed it, and she reports that too. Then she prints all runs side by side from her results file, deploys version three, and writes her report. Her report has one results table and five real failure examples.

The report is about two pages, with six parts. Purpose. Design choices, each with its evidence. Metrics before and after. Improvements, including the ones that did not help. Known failures, with real examples. And risks and next steps. A team lead should be able to read it and decide what to do next.

A common mistake is to change several things at once, and then not know which one helped. Change one thing per run, log every run, and report the failed attempts. Honest negative results are evidence too.

## Recap
Let's recap. First, measure a baseline on a frozen test set, diagnose failures by cause, change one thing, and measure again. Second, make at least two improvements that target the most common causes, and report every run. Third, your report states purpose, design choices, before and after metrics, cost per query, known failures and next steps. Evidence first, always.

## CTA
Congratulations. You have finished RAG Systems: Chat with Your Data. You can now build assistants that find the right passages, cite their sources, and say I don't know when they should. Your last task is capstone step two. Evaluate, improve and deploy your assistant, write your two-page report, and submit your capstone using the checklist below. Well done.

## Thumbnail
Headline: Prove It Works
Image: Navy background, a two-page report with a before-and-after results table and a small upward teal line chart, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Licence of the example open-source documentation used in Camila's demo.
- [VERSION] Free hosting plans and their limits (no provider named in the voiceover); Claude model choice and prices for estimating cost per query, read from config. Never say a model ID or price.
- Camila's results (v1 hit@5 0.70, MRR 0.52, faithfulness 0.80, refusals 4 of 6; v2 hit@5 0.83; v3 refusals 6 of 6, faithfulness 0.90) are hypothetical; the voiceover calls them example results and the results slide carries a 'hypothetical results' label. The compare() output on screen must be generated from a runs file containing these example values.
- Portuguese questions shown on screen should be checked by a Portuguese speaker before release.
- Camila in Belo Horizonte is hypothetical; do not name or show the logo of a real web framework unless its documentation licence has been confirmed.
