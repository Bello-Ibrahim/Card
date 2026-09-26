# L08 Designing Evaluation: Metrics That Matter | Presenter Script

Course: AI-27 · Video: 5 min · Words: 693

## Hook
Your summary feature scores ninety five on an accuracy test. Users still stop using it, and nobody knows why. One number told you the model was good. It did not tell you whether the product was.

## Explain
So far, you have scoped a feature and checked its data and cost. Now, how will you know if it is good? Evaluate an AI feature on three layers. Each layer answers a different question.

Offline quality asks, is the output good? You measure it on a test set before launch and after each change, for example accuracy, or rubric scores for generated text. Online product results ask, does it help users? You measure them with real users: task success, time saved, adoption, repeat use, and how often users edit or reject the output.

Guardrail metrics ask, is it safe and sustainable? These must stay inside limits, even if quality improves. Examples are the rate of harmful or invented content, response time, cost per request and complaint rate.

Connect the layers in a metric tree. The product goal sits at the top. Under it are the online metrics that show progress. Under those are the offline metrics you expect to drive them. The guardrails sit beside the tree. Each metric gets a target, and each guardrail gets a limit you will not accept.

Why is one number never enough? High offline quality with low adoption means the feature solves the wrong problem, or is hard to find. High adoption with rising complaints means users try it and are disappointed. And good quality at a cost you cannot afford is not a product.

Think of a hospital. It does not judge a doctor only by exam results. It also looks at whether patients recover, and whether safety rules are followed. A doctor with excellent exams but poor patient outcomes needs attention. So does a feature with a high offline score but poor product results.

## Demonstrate
Let's build a tree. Thandiwe Mokoena is a PM at a hypothetical law firm in South Africa that builds internal tools. Lawyers want an AI summary of key terms in long contracts, such as parties, dates, payment terms and termination rights. A lawyer always reads the summary before using it.

Her goal is that lawyers review contracts faster without missing key terms. Online, she tracks median review time against the current baseline, how often lawyers open the summary, and how often they mark it as needing major correction. Each metric has a target set before the pilot.

Offline, she uses sixty contracts labelled by senior lawyers. The target is at least ninety five percent of key terms captured correctly, and zero summaries with an invented term. Her guardrails are a response time under thirty seconds, cost within the agreed budget, and no data sent to a provider whose terms legal has not approved.

Her most important metric is invented terms, kept separate from correct terms. A summary can capture nine of ten key terms and still invent a termination date. For lawyers, an invented term is much worse than a missing one, so it gets its own strict target.

She also records the baseline review time before the pilot starts. Without it, faster cannot be measured.

A common mistake is choosing metrics that are easy to count, such as summaries generated. Usage only shows that the feature runs. Set every target before you see the results. Tie every metric to a question in the tree, and measure a baseline before launch.

## Recap
Let's recap. First, evaluate AI features on three layers: offline quality, online product results and guardrail metrics. Second, a metric tree connects the product goal to online and offline metrics, with guardrails beside it, and a target or limit for each. Third, no single metric is enough, because each layer catches failures the others miss.

## CTA
Now it is your turn. In the exercise below, build a metric tree for your feature, with at least one metric in each layer, a target for each, and one stop metric clearly marked. It takes about twenty five minutes. In the next lesson, we build a test set and run evaluations, live on screen. See you there.

## Thumbnail
Headline: One Number Is Never Enough
Image: Navy background, a metric tree with a goal at the top, branches for online and offline metrics, and a guardrail column beside it, headline in teal Inter Bold.

## Production Notes
- [VERSION] FigJam free-plan limits and Google Sheets features must be checked before recording (exercise tools).
- Thandiwe Mokoena and the law firm in South Africa are hypothetical; no real firm names or logos in stock footage. The targets (95 percent, zero invented terms, under 30 seconds, test set of 60 contracts) come from the content.md worked example.
