# HeyGen Batch Pack: AI-27 M2 (Data, Models and Evaluation)

Course: AI Product Management. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L06 Data Needs: What Your Feature Learns From

- **Filename:** `ai-27-ai-product-management_M2_L06_presenter.mp4`
- **Expected length:** about 5.2 minutes (724 words). The quality gate accepts ±10%.

```text
Your team can choose the best model available and still ship a poor feature. If the data behind it is old, incomplete or collected without permission, the model will faithfully repeat those problems to your users.

This is week two, and we start with data. Every AI feature depends on data in up to three ways, and as a PM, you own the questions about all three.

Training or tuning data is the examples a model learns from, if you train or adapt a model. Context data is information given to the model at the moment of use, such as a product catalogue or a user's order history. And evaluation data is examples with known good answers, used to test quality. Even with a ready made model, you still need context and evaluation data.

Check each source against six points. Source and owner: where does it come from, and who can approve its use? Labels: do the examples include the correct answer, and how consistent are they? Quality: is it accurate, complete and current? Old prices or deleted products create wrong answers.

Coverage: does it represent all your users, such as regions, languages and new customers? Gaps in coverage become quality gaps for those users. Consent and privacy: did users agree to this use, and is any personal data really necessary? Rules differ by country, so involve your privacy or legal team early. And access and cost: how long will it take to get?

A new product, or a new market, often has no usage data yet. This is the cold start problem. You can start with a rule based version and collect data from it. You can use a general model with good context data. You can label a small set of examples by hand. Or you can run a human in the loop version first, so human decisions become labels.

Think of a recipe. It is only as good as its ingredients. A skilled chef with old vegetables still serves a poor meal. And if the kitchen only stocks ingredients for one dish, guests who want something else go hungry. Quality is the freshness of your ingredients. Coverage is the range of dishes you can make.

Let's see an example. Mateo Fuentes is a PM at a hypothetical online grocery service in Chile. When an item is out of stock, pickers in the store choose a substitute. Mateo wants AI to suggest the best substitute, and the picker confirms it.

He fills in a data requirements table. The product catalogue has no personal data, but sizes are missing and categories are used inconsistently. So the team cleans the top five hundred products first. Past substitutions record whether customers accepted or refunded, but not why. They are linked to accounts, so identity is removed, and only the item pair and outcome are used.

Customer dietary preferences are sensitive personal data, and few customers fill them in. They need clear consent and a legal review. And a new store in the south has almost no substitution history at all.

The table leads to two decisions. First, the MVP will not use dietary preferences, because the privacy questions need more time, and the feature works without them. Second, the new store has a cold start problem. So it begins with simple catalogue rules, and picker confirmations build labelled data over time.

A common mistake is thinking lots of data means the right data. A large data set can still lack labels, miss whole user groups, or contain personal data you may not use. And never paste real customer data into an AI tool to check it quickly. Use invented or anonymised examples.

Let's recap. First, an AI feature needs context and evaluation data even with a ready made model, and sometimes training data too. Second, check every source for owner, labels, quality, coverage, consent and access, because each gap becomes a product problem. Third, plan for cold start with rules, hand labelled examples, or a human in the loop version.

Now it is your turn. In the exercise below, complete a data requirements table for your feature, with sources, owners, quality risks, privacy questions and how you would fill the gaps. It takes about twenty five minutes. In the next lesson, we ask a big question: build, buy or use an API? See you there.
```

## L07 Build, Buy or Use an API?

- **Filename:** `ai-27-ai-product-management_M2_L07_presenter.mp4`
- **Expected length:** about 5.0 minutes (699 words). The quality gate accepts ±10%.

```text
A feature that costs almost nothing in a demo can become one of your largest monthly bills at scale. The way to avoid that surprise is a simple calculation you can do in a spreadsheet, before you commit.

Last time, we looked at the data your feature needs. Now, where does the AI part come from? There are four common ways.

A foundation model API: you send requests to a general model, such as Claude, and pay per use. It is the fastest start, but you depend on one supplier. You must also check its data terms.

A vendor product: you buy a finished tool. It is fast to launch, with less control. Fine tuning: you adapt a model with your own examples, which needs good labelled data. And an in house model: the most control, but it needs specialist skills, data and time.

Compare the options on five trade offs: cost per request, speed, quality on your test set, data terms, and how hard it is to switch supplier. Many teams start with an API to learn quickly, then revisit the choice when volume and evaluation results are known.

Model APIs usually charge per token. A token is a small piece of text, often part of a word. Input tokens are what you send, including instructions and context. Output tokens are what the model writes. They usually have different prices. So monthly cost is requests, times tokens per request, times price per token, worked out for input and output separately.

One important note. All the prices in this lesson are placeholders for teaching. Real prices differ by model and change over time, so always check the provider's pricing page on the day you plan.

Choosing between an API and your own model is like choosing between a taxi and buying a car. The taxi costs more per trip, but nothing to start, and you can change companies. The car costs a lot at the start and needs maintenance, but may be cheaper if you drive every day.

Let's calculate. Lena Fischer is a PM at a hypothetical accounting software company in Germany. She plans a feature that explains each invoice error in plain language.

She has ten thousand users, each making twenty requests a month. That is two hundred thousand requests. Each request sends fifteen hundred input tokens and gets three hundred output tokens back. Her placeholder prices are one dollar fifty per million input tokens, and six dollars per million output tokens.

Input is three hundred million tokens, so four hundred and fifty dollars. Output is sixty million tokens, so three hundred and sixty dollars. The monthly total is eight hundred and ten dollars, with placeholder prices. That is about eight cents per user per month.

What if usage doubles to forty requests per user? The cost doubles to one thousand six hundred and twenty dollars a month, because cost grows in a straight line with requests.

Lena notices that input tokens are most of the volume. Shorter instructions, or sending only the relevant invoice lines, would lower the cost. She also adds costs that are not model costs: engineering time, evaluation work and monitoring. And she asks the provider whether invoice data is stored or used for training. Legal must approve the data terms before any real data is sent.

A common mistake is estimating cost from a demo with short prompts and a few users. Real requests carry long instructions and documents. Test at double and triple usage.

Let's recap. First, the four options are an API, a vendor product, fine tuning and an in house model, compared on cost, speed, quality, data terms and supplier dependence. Second, API cost is requests times tokens times price, for input and output separately. Third, always use current prices, test higher usage, and check data terms before sending real data.

Now it is your turn. In the exercise below, estimate the monthly cost of your feature for ten thousand users in Google Sheets, using the placeholder prices provided. Then see what happens when usage doubles. It takes about twenty five minutes. In the next lesson, we look at designing evaluation, and the metrics that matter. See you there.
```

## L08 Designing Evaluation: Metrics That Matter

- **Filename:** `ai-27-ai-product-management_M2_L08_presenter.mp4`
- **Expected length:** about 5.0 minutes (693 words). The quality gate accepts ±10%.

```text
Your summary feature scores ninety five on an accuracy test. Users still stop using it, and nobody knows why. One number told you the model was good. It did not tell you whether the product was.

So far, you have scoped a feature and checked its data and cost. Now, how will you know if it is good? Evaluate an AI feature on three layers. Each layer answers a different question.

Offline quality asks, is the output good? You measure it on a test set before launch and after each change, for example accuracy, or rubric scores for generated text. Online product results ask, does it help users? You measure them with real users: task success, time saved, adoption, repeat use, and how often users edit or reject the output.

Guardrail metrics ask, is it safe and sustainable? These must stay inside limits, even if quality improves. Examples are the rate of harmful or invented content, response time, cost per request and complaint rate.

Connect the layers in a metric tree. The product goal sits at the top. Under it are the online metrics that show progress. Under those are the offline metrics you expect to drive them. The guardrails sit beside the tree. Each metric gets a target, and each guardrail gets a limit you will not accept.

Why is one number never enough? High offline quality with low adoption means the feature solves the wrong problem, or is hard to find. High adoption with rising complaints means users try it and are disappointed. And good quality at a cost you cannot afford is not a product.

Think of a hospital. It does not judge a doctor only by exam results. It also looks at whether patients recover, and whether safety rules are followed. A doctor with excellent exams but poor patient outcomes needs attention. So does a feature with a high offline score but poor product results.

Let's build a tree. Thandiwe Mokoena is a PM at a hypothetical law firm in South Africa that builds internal tools. Lawyers want an AI summary of key terms in long contracts, such as parties, dates, payment terms and termination rights. A lawyer always reads the summary before using it.

Her goal is that lawyers review contracts faster without missing key terms. Online, she tracks median review time against the current baseline, how often lawyers open the summary, and how often they mark it as needing major correction. Each metric has a target set before the pilot.

Offline, she uses sixty contracts labelled by senior lawyers. The target is at least ninety five percent of key terms captured correctly, and zero summaries with an invented term. Her guardrails are a response time under thirty seconds, cost within the agreed budget, and no data sent to a provider whose terms legal has not approved.

Her most important metric is invented terms, kept separate from correct terms. A summary can capture nine of ten key terms and still invent a termination date. For lawyers, an invented term is much worse than a missing one, so it gets its own strict target.

She also records the baseline review time before the pilot starts. Without it, faster cannot be measured.

A common mistake is choosing metrics that are easy to count, such as summaries generated. Usage only shows that the feature runs. Set every target before you see the results. Tie every metric to a question in the tree, and measure a baseline before launch.

Let's recap. First, evaluate AI features on three layers: offline quality, online product results and guardrail metrics. Second, a metric tree connects the product goal to online and offline metrics, with guardrails beside it, and a target or limit for each. Third, no single metric is enough, because each layer catches failures the others miss.

Now it is your turn. In the exercise below, build a metric tree for your feature, with at least one metric in each layer, a target for each, and one stop metric clearly marked. It takes about twenty five minutes. In the next lesson, we build a test set and run evaluations, live on screen. See you there.
```

## L09 Building a Test Set and Running Evaluations

- **Filename:** `ai-27-ai-product-management_M2_L09_presenter.mp4`
- **Expected length:** about 5.0 minutes (696 words). The quality gate accepts ±10%.

```text
Test an AI feature only with questions from a team meeting, and it will pass. Real users will ask everything else. A good test set is your chance to meet those users before launch.

Last time, you designed a metric tree. Today, we build the test set behind your offline metrics, and run it live. A test set is a fixed list of inputs, with a clear idea of what a good output looks like.

Include four types of case. Common cases, the questions most users ask. Edge cases, unusual but valid inputs, such as a deadline passed by one day. Different users and languages, every group you serve. And should refuse cases, requests the feature must decline, such as asking for another person's data.

Score each output with a three point rubric. Two is a pass: correct, complete and following policy. One is partial. Zero is a fail: wrong, inventing policy, or answering something it should refuse. Write the criteria before you run anything, and report the pass rate for each case type, because an average hides weak groups.

Human rating is the reference. LLM as judge means asking a model to score outputs against your rubric. It is fast, but it can be too generous, prefer long answers and miss policy errors. So use it only with human spot checks, and look at every disagreement.

Think of a driving test. A test only on empty roads on sunny days tells you little. A good test includes night driving, rain and a sudden obstacle. Your edge cases and refusal cases are the night driving and the rain.

Let's run one. Maria Santos is a PM at a hypothetical home goods shop in the Philippines. Her feature answers questions about returns, using the shop's return policy. In Google Sheets, she creates columns for ID, type, input, expected behaviour, output, human score and judge score.

She fills twenty rows with invented cases: eight common, five edge, four language, and three should refuse. All cases are invented, with no real customer data. She pastes each input into Claude with the policy, and copies the answer into the output column. Then she scores each answer with the rubric.

Next, she opens a new Claude chat, gives it the rubric, and sends one case at a time, asking for a score of zero, one or two with one reason. She records each score in the judge column.

Now she adds formulas for the pass rate, the pass rate for each type, and the agreement between her and the judge. Her human pass rate is twelve of twenty, or sixty percent. By type, common cases pass at seventy five percent, but edge cases only at forty percent.

The judge gives fourteen passes, which is seventy percent. It agrees with Maria on fifteen of twenty cases, which is seventy five percent. It scores higher than Maria on four cases, and lower on one.

She filters the rows where the two scores differ, and reads each one. The biggest miss is case sixteen. The answer in Cebuano was wrong, but the judge gave it a two. So the judge is too generous, and weak on less common languages. Every judge score in those languages needs human review.

A common mistake is letting the judge replace human rating because it is faster. Keep humans as the reference, and never report a judge only score without saying so. The judge then inherits blind spots, such as a language it handles poorly.

Let's recap. First, a test set needs common cases, edge cases, different users and languages, and cases that should be refused, with the rubric written first. Second, report the pass rate for each case type, because averages hide weak groups. Third, LLM as judge is useful but limited. Measure its agreement with humans, and review every disagreement.

Now it is your turn. In the exercise below, write a twenty case test set in Google Sheets, run each case through Claude, and score the outputs with a three point rubric, just as Maria did. It takes about forty minutes. In the next lesson, we look at working with data scientists and engineers. See you there.
```

## L10 Working with Data Scientists and Engineers

- **Filename:** `ai-27-ai-product-management_M2_L10_presenter.mp4`
- **Expected length:** about 5.0 minutes (697 words). The quality gate accepts ±10%.

```text
When will it be ready? For an AI feature, the honest answer is often, we do not know yet if it will be good enough. A PM who plans for that answer builds trust. A PM who ignores it gets surprises.

You now have metrics and a test set. The next step is working well with the people who build the feature.

AI work is less predictable than traditional feature work. The team does not know in advance if a model, a prompt or a data set will reach the quality target. Some ideas reach it quickly. Others need several attempts, and a few never reach it with the available data. This is normal, not a sign of a weak team.

So plan in experiment cycles instead of fixed launch dates. Each cycle has a question, such as can we reach an eighty five percent pass rate on common cases? It has a time box, for example two weeks. It has an agreed evaluation. And it ends with a decision: continue, change the approach, or stop.

Shared vocabulary makes these talks faster. You do not need to build models, but use these terms correctly: test set, baseline, precision and recall, latency, prompt, context, fine tuning, and drift, which is quality changing over time because inputs change.

Ask the team for four things: written assumptions, evaluation results broken down by case type and user group, known limits, and model documentation, including the model version, data terms and what changed. In return, give them a clear problem, the scope, the failure design, the cost limits and fast decisions.

Think of crossing the sea by sailing boat instead of by train. A train has a timetable. A sailing crew knows the destination and the route, but checks the wind every day. They agree in advance at which ports they will decide to continue or wait. Experiment cycles are those ports.

Let's see an example. Wanjiru Kamau is a PM at a hypothetical savings and loans cooperative app in Kenya. She wants to sort member messages into topics, such as loan question, payment problem and account access, so the right staff member replies first.

Her head of product asks for a launch date. The data scientist, Otieno, cannot promise quality in a fixed time. Messages arrive in English, Kiswahili and a mix of both, and there are only a few hundred labelled examples.

So they agree on a two week experiment. Can a classifier reach at least eighty five percent accuracy on two hundred test messages, with at least sixty in Kiswahili or mixed language? They will measure accuracy by language, and precision for payment problems, because wrong urgent flags waste staff time.

The decision rule is written first. If the target is met, run a pilot with one support team. If it is close, spend one more cycle labelling messages. If it is far below, switch to simple rule based routing, and collect labels.

After two weeks, Otieno shares the results: good accuracy in English, lower in mixed language messages. Wanjiru does not treat this as a failure. She chooses the close path. Her head of product gets a clear update: what was learned, the next decision point, and the fallback.

A common mistake is passing a fixed date straight from leadership to the team, then treating a missed quality target as a delivery failure. That pushes teams to launch below the bar. Instead, share a time boxed experiment, a quality target and a decision rule with leadership before the work starts.

Let's recap. First, AI timelines are less predictable, because quality is not known in advance, so plan in time boxed experiment cycles with a decision at the end. Second, ask the team for assumptions, results by group, known limits and model documentation. Third, give them a clear problem, scope, failure design, cost limits and fast decisions in return.

Now it is your turn. In the exercise below, write a one page brief for your technical team, with the feature goal, your assumptions, one experiment cycle and five open questions. It takes about twenty five minutes. Next week, we start with responsible AI risks and guardrails. See you there.
```
