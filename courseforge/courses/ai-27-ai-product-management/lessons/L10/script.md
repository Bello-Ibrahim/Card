# L10 Working with Data Scientists and Engineers | Presenter Script

Course: AI-27 · Video: 5 min · Words: 697

## Hook
When will it be ready? For an AI feature, the honest answer is often, we do not know yet if it will be good enough. A PM who plans for that answer builds trust. A PM who ignores it gets surprises.

## Explain
You now have metrics and a test set. The next step is working well with the people who build the feature.

AI work is less predictable than traditional feature work. The team does not know in advance if a model, a prompt or a data set will reach the quality target. Some ideas reach it quickly. Others need several attempts, and a few never reach it with the available data. This is normal, not a sign of a weak team.

So plan in experiment cycles instead of fixed launch dates. Each cycle has a question, such as can we reach an eighty five percent pass rate on common cases? It has a time box, for example two weeks. It has an agreed evaluation. And it ends with a decision: continue, change the approach, or stop.

Shared vocabulary makes these talks faster. You do not need to build models, but use these terms correctly: test set, baseline, precision and recall, latency, prompt, context, fine tuning, and drift, which is quality changing over time because inputs change.

Ask the team for four things: written assumptions, evaluation results broken down by case type and user group, known limits, and model documentation, including the model version, data terms and what changed. In return, give them a clear problem, the scope, the failure design, the cost limits and fast decisions.

Think of crossing the sea by sailing boat instead of by train. A train has a timetable. A sailing crew knows the destination and the route, but checks the wind every day. They agree in advance at which ports they will decide to continue or wait. Experiment cycles are those ports.

## Demonstrate
Let's see an example. Wanjiru Kamau is a PM at a hypothetical savings and loans cooperative app in Kenya. She wants to sort member messages into topics, such as loan question, payment problem and account access, so the right staff member replies first.

Her head of product asks for a launch date. The data scientist, Otieno, cannot promise quality in a fixed time. Messages arrive in English, Kiswahili and a mix of both, and there are only a few hundred labelled examples.

So they agree on a two week experiment. Can a classifier reach at least eighty five percent accuracy on two hundred test messages, with at least sixty in Kiswahili or mixed language? They will measure accuracy by language, and precision for payment problems, because wrong urgent flags waste staff time.

The decision rule is written first. If the target is met, run a pilot with one support team. If it is close, spend one more cycle labelling messages. If it is far below, switch to simple rule based routing, and collect labels.

After two weeks, Otieno shares the results: good accuracy in English, lower in mixed language messages. Wanjiru does not treat this as a failure. She chooses the close path. Her head of product gets a clear update: what was learned, the next decision point, and the fallback.

A common mistake is passing a fixed date straight from leadership to the team, then treating a missed quality target as a delivery failure. That pushes teams to launch below the bar. Instead, share a time boxed experiment, a quality target and a decision rule with leadership before the work starts.

## Recap
Let's recap. First, AI timelines are less predictable, because quality is not known in advance, so plan in time boxed experiment cycles with a decision at the end. Second, ask the team for assumptions, results by group, known limits and model documentation. Third, give them a clear problem, scope, failure design, cost limits and fast decisions in return.

## CTA
Now it is your turn. In the exercise below, write a one page brief for your technical team, with the feature goal, your assumptions, one experiment cycle and five open questions. It takes about twenty five minutes. Next week, we start with responsible AI risks and guardrails. See you there.

## Thumbnail
Headline: Ports, Not Timetables
Image: Navy background, a sailing boat on a route line with three port markers, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude free-plan limits and data-use terms must be checked before recording (optional exercise tool).
- Wanjiru Kamau, the data scientist Otieno and the savings and loans cooperative app in Kenya are hypothetical; no real app or logo in stock footage.
- The experiment numbers (85 percent accuracy, 200 test messages, at least 60 in Kiswahili or mixed language, two weeks) come from the content.md worked example.
