# L10 Working with Data Scientists and Engineers

Course: AI-27 · Module: M2 · Objectives: O2, O4 · Video: 5 min

## Hook
"When will it be ready?" is a normal question for most features. For an AI feature, the honest answer is often, "We do not know yet if it will be good enough." A PM who plans for that answer builds trust. A PM who ignores it gets surprises.

## Explanation
AI work is less predictable than traditional feature work, because the team does not know in advance whether a model, a prompt or a data set will reach the quality target. Some ideas reach it quickly. Others need several attempts, and a few never reach it with the available data. This is a normal part of the work, not a sign of a weak team.

So plan in **experiment cycles** instead of fixed launch dates. Each cycle has:

1. **A question:** "Can we reach at least 85% pass rate on our test set for the common cases?"
2. **A time box:** for example, two weeks.
3. **An agreed evaluation:** the test set and metrics from L08 and L09.
4. **A decision at the end:** continue to the next step, change the approach, or stop.

**Shared vocabulary** makes these conversations faster. As a PM you do not need to build models, but you should use these terms correctly: test set, baseline, precision and recall (for classification), latency (response time), prompt, context, fine-tuning, and drift (quality changing over time because inputs change).

**What a PM should ask for**, and what the team should expect to share:

- **Assumptions:** what the team believes about the data and users, written down so everyone can check them.
- **Evaluation results:** scores on the agreed test set, broken down by case type and user group.
- **Known limits:** where the model fails, which inputs it should not receive, and which languages or groups are weaker.
- **Model documentation:** which model or vendor is used, its version, its data terms, and what changed since the last cycle.

In return, the PM gives the team a clear problem, the scope and the failure experience (L05), the cost limits (L07), and fast decisions at the end of each cycle.

**Analogy:** Planning AI work is like planning a journey across the sea by sailing boat instead of by train. A train has a timetable. A sailing crew knows the destination and the route, but checks the wind every day and agrees in advance at which ports they will decide to continue or wait. Experiment cycles are those ports.

## Worked Example
Wanjiru Kamau is a PM at a hypothetical savings and loans cooperative app in Kenya. She wants a feature that sorts incoming member messages into topics, such as "loan question", "payment problem" and "account access", so that the right staff member replies first.

Her head of product asks for a launch date. The data scientist, Otieno, says he cannot promise the quality in a fixed time: messages arrive in English, Kiswahili and a mix of both, and there are only a few hundred labelled examples.

Instead of a date, Wanjiru and Otieno agree on a two-week experiment:

- **Question:** Can a classifier reach at least 85% accuracy on 200 labelled test messages, including at least 60 in Kiswahili or mixed language?
- **Evaluation:** accuracy overall and by language; precision for "payment problem", because wrong urgent flags waste staff time.
- **Decision at the end:** if the target is met, run a pilot with one support team; if it is close, spend one more cycle on labelling more messages; if it is far below, switch to a simpler rule-based routing and collect labels.

At the end of week two, Otieno shares results: good accuracy in English, lower in mixed-language messages. Wanjiru does not treat this as a failure. She chooses the "close" path, and the team labels more mixed-language messages. Her head of product gets a clear update: what was learned, the next decision point and the fallback.

## Common Mistake
Many PMs pass a fixed date from leadership directly to the technical team and then treat missing the quality target as a delivery failure. This pushes teams to launch below the quality bar. Replace the date with a time-boxed experiment, a clear quality target and a decision rule, and share them with leadership before the work starts.

## Key Takeaways
1. AI timelines are less predictable because quality is not known in advance, so plan in time-boxed experiment cycles with a decision at the end.
2. Ask the technical team for assumptions, evaluation results by group, known limits and model documentation.
3. Give the team a clear problem, scope, failure design, cost limits and fast decisions in return.

## Hands-on Exercise
**Task:** Write a one-page brief for your technical team with the feature goal, your assumptions and 5 open questions.
**Tools:** Google Docs or any document; optional: Claude (free plan) to review your brief [VERSION].
**Steps:**
1. Write the feature goal and the user problem in two or three sentences.
2. Write the scope: user, task, human in the loop, fallback (from L05).
3. List at least 4 assumptions about data, users, quality and cost.
4. Propose one experiment cycle: question, time box, evaluation and decision rule.
5. Write 5 open questions for the team, such as "Which languages are weakest in our data?"
6. Optional: ask Claude to read your brief as a data scientist and list anything unclear. Remove confidential details first.
**What good looks like:** One page that a data scientist could act on, with testable assumptions, a specific experiment with a decision rule, and open questions that the PM cannot answer alone.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Claude free-plan limits and data-use terms must be checked before recording.
