# HeyGen Batch Pack: AI-24 M3 (Governance and Your Capstone)

Course: AI in Finance and Fintech. Make one HeyGen video per lesson below, using these settings for every video.

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

## L11 Regulatory Principles for AI in Finance

- **Filename:** `ai-24-ai-in-finance-and-fintech_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (681 words). The quality gate accepts ±10%.
- **Pronunciation:** Pronunciation: GDPR, LGPD, NDPA and POPIA are spelled out letter by letter, except POPIA, which is usually said 'po-PEE-ya'; confirm with the reviewer.

```text
Your fintech is launching an AI credit product in three countries. Each has different laws, different regulators and different languages. Do you need to learn three rulebooks from zero? Not completely. Most rulebooks are built on the same small set of principles.

Welcome to the final week. This lesson teaches principles that appear, in different words, in the rules of many countries. It is not legal advice. For any real product, always confirm the local rules with your compliance or legal team.

Principle one is fair treatment. Decisions must not discriminate against protected groups, directly or indirectly. Principle two is explainability and transparency. Customers should know when automated systems support important decisions, and receive understandable reasons, especially for declines. Staff and supervisors must also be able to understand how the model works.

Principle three is data protection. Personal data must be collected for a clear purpose, on a lawful basis, kept to the minimum needed, stored securely, and kept only as long as necessary. People often have rights to access and correct their data. Principle four is model risk management: an inventory of models, independent validation, and ongoing monitoring.

Principle five is accountability. A named person or committee is responsible for each model and its outcomes. The AI decided is never an acceptable answer. Principle six is third-party risk. When a tool comes from a vendor, the institution is still responsible, so it must check the vendor's data use, security, testing, and the right to audit.

You will also hear named laws. Examples include the EU AI Act, adverse action notices in the United States, and data protection laws such as the GDPR in Europe, the LGPD in Brazil, the NDPA in Nigeria and POPIA in South Africa. Treat these only as examples to check with experts, because scope and dates change.

The principles are like the rules of the road. Countries drive on different sides and have different speed limits. But almost all of them require a licence, working brakes and responsibility for accidents. Understand the shared principles, and learning the local version is much faster.

Thandiwe Nkosi is head of compliance at Kopano Credit, a hypothetical fintech in Johannesburg, South Africa. The company plans an AI-supported small-business loan in South Africa, Nigeria and Brazil. So she builds a principles table for the product.

For each principle, she notes what the company already does, and what she must check locally. For fair treatment, they already track approval and error rates by group every month. But she must check which characteristics are protected in each country. For explainability, they already give three plain-language decline reasons. She must check the required content and timing of decline notices.

For data protection, they have a consent screen for bank-statement data. She must confirm the lawful basis and customer rights under each country's law. For accountability, the chief risk officer owns the model, and she must check who signs off for each licence. And for third-party risk, she must check the rules on sending data across borders.

The table does not answer every question. But it shows her exactly which questions to ask local lawyers, which saves time and money.

A common mistake is to assume that a product that follows one country's rules can launch anywhere. Principles travel well. Details do not. Consent rules, data transfer limits and notice requirements can differ a lot.

Let's recap. First, six principles appear in many countries: fair treatment, explainability, data protection, model risk management, accountability and third-party risk. Second, named laws are examples to check with experts, not rules to copy. Third, a principles table turns general knowledge into a clear list of questions for your compliance or legal team.

Now it is your turn. In the exercise below this video, you will complete a principles table for your own country. For each principle, note what you already know and what you must check with your compliance or legal team. It takes about twenty-five minutes, and it will help with your capstone. In the next lesson, we look at model risk management and monitoring. See you there.
```

## L12 Model Risk Management and Monitoring

- **Filename:** `ai-24-ai-in-finance-and-fintech_M3_L12_presenter.mp4`
- **Expected length:** about 4.9 minutes (681 words). The quality gate accepts ±10%.

```text
A fraud model passes every test at launch. Six months later, false alarms have doubled, and a new type of fraud is getting through. Nobody changed the model. So what changed, and whose job was it to notice?

Last time, model risk management was one of our six principles. Now we look at it closely. Model risk is the risk of loss or harm because a model is wrong, is used wrongly, or stops working as intended. Managing it has four main parts.

Part one is a model inventory: a list of every model in use, with its purpose, owner, data, validation date and risk rating. You cannot manage a model you do not know exists, and that includes vendor models and AI assistants. Part two is independent validation. Before launch, and at regular intervals, people who did not build the model test it, and they can require changes before approval.

Part three is performance and drift monitoring. After launch, the owner measures the model regularly. For fraud, performance means the share of fraud caught and the false alarm rate. For credit, it means default rates by score band. The owner also watches data drift, score drift and fairness. An amber limit triggers investigation. A red limit triggers action, such as retraining, changing the threshold, or pausing the model.

Part four is the three lines of defence. The first line is the business and model owners, who build, use and monitor the model every day. The second line is independent risk and compliance, who set standards, validate and challenge. The third line is internal audit, which checks that the whole system works.

One question matters in every institution. Who has the authority to pause a model? Write it down before launch, with a fallback process ready, such as rules only or manual review.

Think of a regular vehicle safety inspection. A car that was safe when it left the factory can develop worn brakes and weak tyres. You inspect on a schedule, with clear pass and fail limits, and an inspector can take an unsafe car off the road.

Remember the Lagos card issuer from lesson three? Ifeoma Eze is its head of model risk, and she writes a monitoring plan for the fraud model. Her limits are illustrative, set by the issuer for this model. First, the share of fraud caught, measured monthly once labels mature after sixty days. Amber is below eighty percent. Red is below seventy.

The false alarm rate is checked weekly, with amber above three percent and red above five. The score distribution is compared with launch every month. Missing values in key fields are checked daily. And every quarter, the second line compares false alarm rates across customer groups. Amber is a ratio above one point two five, and red is above one point five.

Red limits go to the model risk committee within two working days. The chief risk officer has the authority to pause the model. If it is paused, the issuer falls back to its fraud rules and extra manual review. And internal audit reviews the whole process once a year.

A common mistake is to treat validation at launch as the end of model risk work. It is the start. Data, customers and fraud patterns change. And a plan without named people, limits and a pause authority is not a monitoring plan.

Let's recap. First, model risk management needs an inventory, independent validation, ongoing monitoring with limits, and clear owners. Second, the three lines of defence separate the people who build and use models, the people who challenge them, and the people who audit the system. Third, decide before launch who can pause a model, and what the fallback process is.

Now it is your turn. In the exercise below this video, you will draft a one-page monitoring plan for the fraud model from lesson three: what to measure, how often, which limits trigger action, and who acts. It takes about thirty minutes. In the next lesson, we start your capstone, by scoping your AI use case proposal. See you there.
```

## L13 Scoping Your AI Use Case Proposal

- **Filename:** `ai-24-ai-in-finance-and-fintech_M3_L13_presenter.mp4`
- **Expected length:** about 4.9 minutes (684 words). The quality gate accepts ±10%.

```text
We should use AI for lending. That is not a proposal. It is a wish. A committee can only say yes to something specific: a clear problem, a clear user, clear data, and a clear way to measure success.

Now we start your capstone: an AI use case proposal for a financial institution, with a risk and compliance assessment. You build it in two steps. The scope in this lesson, and the risk assessment in the next. Choose a use case you know, and use only synthetic or described data, never real customer data.

The proposal template has seven sections. The problem: what is going wrong today, and for whom? The business value. The users, and the decision they make with the output. And the data: which data, from where, with what quality problems and what legal basis?

Then the model approach: rules, a scorecard, a machine learning model, or a language model assistant, and why. Human oversight: where a person reviews, overrides or stops the output. And three to five success measures, including at least one customer or fairness measure.

Keep the scope narrow. Support loan officers in reviewing first-time business loans under a set amount is much better than AI for all lending. A narrow scope makes data, risks and success easier to define.

A free AI assistant can be a useful thinking partner. Ask it what assumptions you are making, what data problems a lender might face, or how your success measures could be misleading. Then write the proposal in your own words. Do not copy its text, do not trust its legal facts without a source, and never paste confidential information.

Scoping is like an architect's first drawing. Before anyone orders bricks, the drawing shows who will live in the house, how many rooms it needs, and where the doors go. Changing a drawing is cheap. Changing a finished building is expensive.

Joy Villanueva is operations manager at Bayanihan Microfinance, a hypothetical microfinance institution in the Philippines. Its loan officers visit small businesses and write long visit notes. Reviewing applications takes too long. Her first idea is an AI that approves loans. After testing her assumptions with an AI assistant, she narrows it down.

The problem: officers spend a large part of each day summarising notes, and applicants wait too long. The value: faster decisions and more visits per officer. She will measure the current baseline in a four-week study before claiming any saving. The users are loan officers and branch supervisors, and the supervisor still makes every lending decision.

The data is visit notes, application forms and repayment history. Known problems: notes in English, Filipino and local languages, and handwritten forms. The approach is a language model assistant that summarises notes and lists missing documents. No credit score, and no approval decisions. The officer checks and signs every summary.

Her success measures are time from visit to decision, the share of summaries with errors, officer satisfaction, and approval and error rates by client group. That last one checks that clients who write in local languages are not disadvantaged.

The assistant helped Joy notice an assumption she had missed: that all notes are written in one language. She did not copy its wording. She used its questions. A common mistake is to describe the technology first and the problem last. Committees fund solutions to problems, not technologies. And never claim exact savings without a baseline.

Let's recap. First, a strong proposal answers seven questions: problem, value, users, data, model approach, human oversight and success measures. Second, a narrow, specific scope makes data, risks and success easier to define and approve. Third, use an AI assistant to test your assumptions, but write the proposal in your own words and check every fact.

Now it is your turn. This exercise is capstone step one. Fill in the problem, value, data and success-measure sections of the template, and use Claude or ChatGPT to test your assumptions. Keep a short log of what it suggested. It takes about forty-five minutes. In the final lesson, we build the risk and compliance assessment. See you there.
```

## L14 Risk and Compliance Assessment

- **Filename:** `ai-24-ai-in-finance-and-fintech_M3_L14_presenter.mp4`
- **Expected length:** about 4.9 minutes (680 words). The quality gate accepts ±10%.

```text
Every AI proposal promises benefits. But the committee's real question is different. What could go wrong, how bad would it be, and what will you do about it? A clear risk register answers that question on one page.

In the last lesson, you scoped your proposal. Now, in this final lesson, you assess its risks. A risk register lists the main risks of your use case in a table, one row per risk.

For each risk, you write what could go wrong, as a cause and an effect. You give it a category. You rate likelihood and impact from one to three, and multiply them for a score from one to nine. Then you add controls, an owner, and a residual rating after the controls.

Cover all six categories from this course. Fairness means outcomes are worse for some groups. Privacy means data is used without a lawful basis, or shared too widely. Explainability means staff or customers cannot understand the outputs.

Security covers data leaks, manipulation of the model, or misuse of the assistant. Third-party covers a vendor that changes its model, uses your data for its own purposes, or stops the service. And operational covers errors, drift, staff over-trusting outputs, or no fallback process.

Then make a recommendation. Go means risks are low or well controlled, so you launch with monitoring. Pilot means the value looks real, but some risks are uncertain, so you test at small scale for a set time. No-go means a high risk cannot be controlled, or the value does not justify it.

A pilot is not a way to avoid a decision. It needs a clear end date, clear measures, and a named person who decides what happens next.

A risk register is like a pre-flight checklist. The pilot does not refuse to fly because things can go wrong. She lists what could go wrong, checks each control, and flies only when the list is complete. If a critical item fails, the flight waits.

Rafael Dizon is a compliance officer at Bayanihan Microfinance. He builds the register for Joy's visit-note assistant from the last lesson. The fairness risk: summaries of notes in local languages contain more errors. Likelihood two, impact three, score six. Controls: test error rates by language before launch, and officers check every summary. Residual three.

Other rows cover explainability, staff pasting data into public tools, and a vendor changing its model. The operational risk is officers signing summaries without reading them. Likelihood three, impact two. With random supervisor checks and error monitoring, the residual is four, the highest in the register.

The fairness risk needs evidence that only a real test can give. So Rafael recommends a pilot: two branches, three months, with a stop rule if the summary error rate for any language group is clearly higher than for English notes. The credit committee chair decides at the end.

Your capstone also needs a short principles check. For each of the six principles from lesson eleven, write one line on how your proposal meets it, and what must be confirmed locally. Then write your recommendation in one paragraph, with reasons. For a pilot, give its scope, length and stop rule.

A common mistake is weak controls, such as be careful or monitor the model. A control says who does what, how often, and what happens at a limit. And do not score every risk as one. Committees trust honest registers more.

Let's recap. First, a risk register records each risk with its category, likelihood, impact, score, controls, owner and residual rating. Second, cover fairness, privacy, explainability, security, third-party and operational risks, with specific controls for each. Third, end with a clear go, pilot or no-go recommendation, and give any pilot an end date, measures and a named decision-maker.

Congratulations on reaching the end of AI in Finance and Fintech. Your last exercise is capstone step two. Complete the risk register in Google Sheets, add a principles check, and finish with your recommendation. Check it against the rubric and checklist, then submit your capstone proposal. Well done, and good luck.
```
