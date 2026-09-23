# L11 Measuring Retrieval Quality | Presenter Script

Course: AI-15 · Video: 5 min · Words: 682

## Hook
If the right chunk never reaches the model, the answer cannot be both correct and grounded. So before you judge answers, measure retrieval. It is fast, it needs no model calls, and it shows exactly where your pipeline loses information.

## Explain
In the last lesson, we built a test set. For each answerable question, we know which chunks are relevant: the ones from the expected source that contain the evidence phrase. Retrieval returns a ranked list. Three metrics compare the two.

Hit rate at k is the share of questions where at least one relevant chunk is in the top k. It asks: does the model get a chance to see the answer? Recall at k is the share of each question's relevant chunks found in the top k. It matters when an answer needs several chunks, such as a comparison.

Mean reciprocal rank, or MRR, shows how high the first relevant chunk is. Rank one scores one. Rank two scores a half. Rank four scores a quarter. Nothing found scores zero. This matters when you pass only a few chunks to the model. Skip unanswerable questions here. We test those with answer metrics next time.

Think of a doctor's basic measurements: temperature, pulse and blood pressure. They quickly tell you that something is wrong, and how serious it is. But to treat the patient, the doctor still has to examine them and find the cause. Retrieval metrics work the same way.

## Demonstrate
Here is the metrics function in plain Python. We test it on three questions. The first finds its chunk at rank one. The second finds one of its two relevant chunks, at rank three. The third finds nothing. The result: hit rate zero point six six seven, recall zero point five, and MRR zero point four four four.

Now a real comparison. Hana is an engineer at an insurance company in Prague, Czech Republic. Her assistant answers questions about claims procedures. Version A uses vector search only. Version B uses the same chunks, with hybrid search. She runs both over thirty-two answerable test questions, and saves the top ten IDs for each.

She computes the metrics at five, because her pipeline passes five chunks to the model. Here are her example results. Version A has a hit rate of zero point seven two, and an MRR of zero point five one. Version B reaches zero point eight four and zero point six three. B is better.

But numbers do not say why. So she lists the five questions that B still fails, and opens the retrieved chunks and the relevant chunk for each one. Two are chunking problems, where a table was split. One is embeddings, with a Czech legal term. One is a vague question. One is parsing, a scanned appendix.

The failure analysis gives her a clear next step. Fix table chunking first, because it causes the most failures. Other common causes are missing keywords, where hybrid search helps, and vague questions, where rewriting helps. Parsing problems need the text extracted again.

A common mistake is to report hit at ten, when you only pass five chunks to the model. Report metrics at the k you actually use, add MRR, and always read the failures. And after re-chunking, do not match relevant chunks by their old IDs. Match by source and evidence phrase instead.

## Recap
Let's recap. First, hit rate and recall at k show whether relevant chunks reach the model, and MRR shows how high the first one is ranked. Second, measure at the k your pipeline really uses, on answerable questions from a frozen test set. Third, classify each failure by cause, to decide what to fix next.

## CTA
Now it is your turn. In the exercise below, compute hit rate, recall at five and MRR for two versions of your pipeline, and classify the causes of five failures. Then write one sentence on what you would fix first, and why. It needs no model calls, so it costs nothing to run. In the next lesson, Measuring Answer Quality: Faithfulness and Relevance, we check the answers themselves.

## Thumbnail
Headline: Did Retrieval Find It?
Image: Navy background, a ranked list of five chunk cards with the correct one highlighted in teal at rank two, small gauges for hit rate and MRR, headline in teal Inter Bold.

## Production Notes
- Content.md Review Flags: None. The metrics code is plain Python and was tested: the screen must show exactly {'hit@k': 0.667, 'recall@k': 0.5, 'mrr': 0.444}.
- Hana's results (A: hit@5 0.72, MRR 0.51; B: hit@5 0.84, MRR 0.63) and her five classified failures are hypothetical; the voiceover calls them example results and the slide carries a 'hypothetical results' label.
- This lesson makes no API calls; no model names or costs appear.
- Hana and the Prague insurance company are hypothetical; the Czech legal term shown on screen should be an invented or generic example.
