# L08 Designing Evaluation: Metrics That Matter

Course: AI-27 · Module: M2 · Objectives: O5 · Video: 5 min

## Hook
Your summary feature scores 95 on an accuracy test. Users still stop using it, and nobody knows why. One number told you the model was good. It did not tell you whether the product was.

## Explanation
Evaluate an AI feature on three layers. Each layer answers a different question.

1. **Offline quality:** "Is the output good?" Measured on a test set before launch and after each change. Examples: accuracy for a classifier, or rubric scores for generated text (such as "complete, correct and no invented facts").
2. **Online product results:** "Does it help users?" Measured with real users. Examples: task success, time saved, adoption (how many eligible users try it), repeat use, and how often users edit or reject the output.
3. **Guardrail metrics:** "Is it safe and sustainable?" These must stay inside limits, even if quality improves. Examples: rate of harmful or invented content, response time, cost per request and complaint rate.

Connect them in a **metric tree**. At the top is the product goal. Under it are the online metrics that show progress towards the goal. Under those are the offline metrics that you expect to drive them. Next to the tree sit the guardrails. Give each metric a **target** (what good looks like) and, for guardrails, a **limit** (what you will not accept).

**Why one number is never enough.** High offline quality with low adoption means the feature solves the wrong problem or is hard to find. High adoption with rising complaints means users try it and are disappointed. Good quality at a cost you cannot afford is not a product. Each layer catches failures the others miss.

**Analogy:** A hospital does not judge a doctor only by exam results. It also looks at whether patients recover (the outcome) and whether safety rules are followed (the guardrails). A doctor with excellent exam results but poor patient outcomes needs attention, and so does a feature with a high offline score but poor product results.

## Worked Example
Thandiwe Mokoena is a PM at a hypothetical law firm in South Africa that builds internal tools. Lawyers read long contracts and want an AI summary of key terms: parties, dates, payment terms and termination rights. A lawyer always reads the summary before using it.

Her metric tree:

- **Goal:** lawyers review contracts faster without missing key terms.
  - **Online:** median review time per contract (target: lower than the current baseline); share of eligible contracts where the summary is opened (target: a majority in the pilot group); share of summaries that lawyers mark "needed major correction" (target: low and falling).
    - **Offline:** on a test set of 60 contracts labelled by senior lawyers, share of key terms correctly captured (target: at least 95%); share of summaries with any invented term (target: 0 in the test set).
- **Guardrails:** response time under 30 seconds; cost per summary under the budget agreed with finance; no contract data sent to a provider whose data terms legal has not approved.

Thandiwe explains her most important metric to the team: "invented terms" is separate from "correct terms". A summary can capture 9 of 10 key terms and still invent a termination date that does not exist. For lawyers, an invented term is much worse than a missing one, so it gets its own metric with a strict target.

She writes the baseline review time before the pilot starts. Without it, "faster" cannot be measured.

## Common Mistake
Teams often choose metrics that are easy to measure, such as the number of summaries generated, instead of metrics that show value. Usage counts only show that the feature runs. Tie every metric to a question in the tree, measure a baseline before launch, and give each metric a target before you see the results, so the targets are not adjusted to match the data.

## Key Takeaways
1. Evaluate AI features on three layers: offline quality, online product results and guardrail metrics.
2. A metric tree connects the product goal to online and offline metrics, with guardrails beside it and a target or limit for each.
3. No single metric is enough, because each layer catches failures that the others miss.

## Hands-on Exercise
**Task:** Build a metric tree for your feature with at least one metric in each layer and a target for each.
**Tools:** FigJam (free plan) or Google Sheets [VERSION].
**Steps:**
1. Write your product goal in one sentence at the top of the board.
2. Add 2 or 3 online metrics that show progress towards the goal.
3. Under each online metric, add at least one offline quality metric you expect to drive it.
4. Beside the tree, add at least 2 guardrail metrics, including one for harmful or invented content and one for cost or response time.
5. Give each metric a target or limit, and note how you will get the baseline.
6. Mark the one metric that would make you stop the launch if it failed.
**What good looks like:** A clear tree with all three layers, specific and measurable metrics, a target for each set before any results, and one clearly marked stop metric.
**Time:** about 25 minutes

## Review Flags
- [VERSION] FigJam free-plan limits and Google Sheets features must be checked before recording.
