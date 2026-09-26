# HeyGen Batch Pack: AI-27 M3 (Responsible Launch and Your PRD)

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

## L11 Responsible AI Risks and Guardrails

- **Filename:** `ai-27-ai-product-management_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (682 words). The quality gate accepts ±10%.

```text
Most AI harms do not come from bad intentions. They come from a reasonable feature, used at scale, with a risk nobody wrote down. A risk table with a named owner for each guardrail is one of the most useful documents a PM can write.

This is week three. You have a scoped feature, a data plan and an evaluation design. Now we make it safe to launch. Five risk types appear in most AI features.

Unfair outcomes: the feature works worse for some groups, such as speakers of a language, older users or people from certain regions. Privacy: personal data is used or exposed in ways users did not expect. Misuse: people use the feature for harm, such as generating spam or extracting other users' data.

Harmful or false outputs: invented facts, dangerous advice or offensive content. And lack of transparency: users do not know that AI is involved, why it gave a result, or how to challenge it.

Guardrails reduce these risks. Input checks block unsafe or out of scope requests before they reach the model. Output checks filter or flag outputs, such as removing personal data. Human review means a person approves higher risk outputs. Usage limits reduce misuse and control cost. And clear user messages say that AI is involved, and how to reach a person.

Every guardrail needs an owner, a person or team responsible for it working. A guardrail without an owner is often switched off or forgotten.

Legal duties also differ by country, and by how sensitive the use is. This lesson is not legal advice. Write your legal questions down, involve your legal team early, and check the current rules for every country where you launch.

Think of a building. It has smoke detectors, fire doors and exit signs, and someone checks each one regularly. You do not add them after a fire. Guardrails are the safety features of an AI product, and the owners are the people who test the alarms.

Let's build a table. Sofie de Vries is a PM at a hypothetical job platform in the Netherlands. Employers want AI to summarise each applicant's CV against the job requirements. Hiring is a sensitive area, so Sofie brings legal in before design. She keeps the scope narrow. The AI summarises, and it never ranks, scores or rejects applicants.

Unfair outcomes: summaries could be weaker for Dutch CVs, or mention age or nationality. The guardrail is a test set in both languages, and an output check that removes those details. The ML lead owns it. Privacy: CV data could be stored by a provider. Legal approves the data terms, and the privacy officer owns it.

False output: a summary claims a skill the CV does not show. So each claim links to its CV line, and Sofie owns that. Misuse: an employer asks which applicant is best. An input check declines ranking requests, owned by the engineering lead. Transparency: applicants are told AI summaries are used, and how to ask for human review.

Sofie adds one more rule to her PRD. Any future plan to rank applicants needs a new legal review before discovery starts.

A common mistake is treating responsible AI as a legal check just before launch. By then, the risky design choices are built. List risks during scoping, and involve legal early, especially in hiring, lending, health and education.

Let's recap. First, the main risks are unfair outcomes, privacy, misuse, harmful or false outputs, and lack of transparency. Second, guardrails include input and output checks, human review, usage limits and clear user messages, and each needs a named owner. Third, legal duties differ by country and by use, so check the current rules with your legal team early.

Now it is your turn. In the exercise below, complete a risk and guardrail table for your feature, with at least one row for each risk type, and an owner for every guardrail. It takes about twenty five minutes. You will reuse it in your capstone PRD. In the next lesson, we plan the launch: pilots, rollouts and monitoring. See you there.
```

## L12 Launch Strategy: Pilots, Rollouts and Monitoring

- **Filename:** `ai-27-ai-product-management_M3_L12_presenter.mp4`
- **Expected length:** about 4.9 minutes (689 words). The quality gate accepts ±10%.

```text
The most important launch decision is one you make before launch. Which result would make you stop? If you decide that only after you see the data, it is very easy to find a reason to continue.

Last time, you wrote your risks and guardrails. Now we plan the launch. You already know how to launch features. AI features need four additions.

First, a staged rollout. Release to internal users, then a small pilot group, then a share of all users, then everyone. Move to the next stage only when a gate metric, agreed in advance, is met. Second, A B tests where they make sense. Compare users with and without the feature on your online metrics, to see whether it helps, not only whether people use it.

Third, feedback loops. Collect signals such as helpful or wrong buttons, edits and reports. And review a sample of real outputs by hand every week, because users do not report most errors.

Fourth, monitoring over time. AI quality can change after launch even if you change nothing. User behaviour changes, new topics appear, and a provider may update a model. This is called drift. So track quality, guardrails, cost and response time on a dashboard, and rerun your test set whenever the model, prompt or data changes.

Two more parts are essential. Stop criteria, written in advance, such as the complaint rate doubling from the baseline. And a kill switch, a way to turn the AI feature off quickly and return users to the non AI fallback, without a new app release. Test it before launch.

Think of a new restaurant with a soft launch. First it serves friends and family, then a few public evenings with a small menu, then the full opening. And the owners decide in advance that if the kitchen cannot serve safely, they close for the evening, whoever is waiting at the door.

Let's see a plan. Elif Yilmaz is a PM at a hypothetical ride hailing app in Turkey. Her feature reads a rider's complaint after a trip, and suggests a category and a draft reply to the support agent, who edits and sends it.

Stage one is internal: ten agents in one city for two weeks. To move on, at least eighty percent of suggested categories must be accepted without change, with no invented refund promises in the weekly sample. Any draft that exposes another rider's personal data stops the rollout.

Stage two is a pilot with all agents in one city, for four weeks. Handling time must be lower than the baseline, and the complaint re open rate no higher. If the re open rate is above the baseline for two weeks in a row, or harmful output passes the agreed limit, the rollout stops.

Stage three widens to twenty five, then fifty, then one hundred percent of agents in all cities. The same metrics must stay within limits at each step, with quality above target in both Turkish and English. A quality drop after a model update also stops the rollout.

After launch, Elif watches a weekly dashboard, a senior agent reviews fifty random drafts each week, and the test set is rerun after every change. The support operations lead owns the kill switch, which returns agents to the normal empty reply form.

A common mistake is a vague stop criterion, such as if quality drops significantly. Nobody agrees what significantly means. Write numbers against a baseline, and name who presses the kill switch.

Let's recap. First, roll out AI features in stages, with a gate metric that must be met before each next stage. Second, monitor for drift with dashboards, weekly human review of samples, and test set reruns after every change. Third, write numeric stop criteria before launch, and have a tested kill switch that returns users to the fallback.

Now it is your turn. In the exercise below, write a rollout plan with three stages, a gate metric for each, and numeric stop criteria. It takes about twenty five minutes. From the next lesson, you start your capstone: writing the AI PRD, its structure and scope. See you there.
```

## L13 Writing the AI PRD: Structure and Scope

- **Filename:** `ai-27-ai-product-management_M3_L13_presenter.mp4`
- **Expected length:** about 4.9 minutes (688 words). The quality gate accepts ±10%.

```text
A standard PRD describes what the product should do. An AI PRD must also describe what it should do when it is wrong, unsure, or asked something it should not answer. This week, you write one.

This is where your capstone begins. You will write a complete PRD and evaluation plan for one AI feature, in three steps. The product sections now, the evaluation plan in the next lesson, and a review and final version in the last lesson. Read the capstone rubric before you start, because it shows how your work is marked.

Here is the AI PRD template. You already know the standard sections, such as problem and users, and open questions. So look at what sits between them. Scope and capability. Experience, with the happy path and four failure paths. Data needs. The model behaviour spec. And build approach and cost.

Then the evaluation plan, which you write next time. Failure modes, and how the design reduces each one. Human oversight: who reviews what, and who can stop outputs. Risks and launch guardrails, with owners. Rollout and monitoring. And finally, open questions, each with an owner and a date.

Sections two to eleven are what an AI PRD adds or changes. Each one reuses work from earlier lessons. Your scope, your failure flow, your data table, your cost estimate, your risk table and your rollout plan all have a place here.

The most useful new section is the model behaviour spec. It turns vague wishes, such as helpful and accurate, into specific rules. What the AI must do. What it must never do. How it behaves when unsure, when it refuses, its tone and format, and three to five example inputs with good outputs.

Remember the talented new colleague from lesson one? A normal PRD is like a job description. An AI PRD is more like their induction guide. It explains the tasks, and also what to do when unsure, what they must never do, who checks their work, and when to call a manager.

Let's look at an example. Haruto Sato is a PM at a hypothetical industrial equipment company in Japan. Field technicians repair packaging machines at customer sites, and often search long manuals on their phones.

His scope: technicians with at least one year of experience, and one task, finding and summarising repair steps for the three most common machine models, with links to the source pages. Machines without digital manuals, and any instruction not found in a manual, are out of scope. The capability is retrieval plus generation.

His behaviour spec says the assistant must answer only from retrieved manual sections, and show the source page for every step. It must never invent a step, a part number or a torque value. When unsure, it says it could not find this in the manual, and suggests calling support. And it refuses requests to bypass safety locks.

For human oversight, a senior technician reviews thirty random answers each week, and can block a manual section that often gives wrong answers. In his FigJam flow, when no section matches, the technician sees the closest sections, and a call support button with the fault already filled in.

A common mistake is filling the template with general statements, such as the model will be accurate and safe. Every rule should be specific enough that a tester could write a test case for it. For example, never gives a torque value that is not in the retrieved section.

Let's recap. First, an AI PRD keeps the standard sections, and adds scope, experience for errors, data, a behaviour spec, evaluation, failure modes, oversight, guardrails and monitoring. Second, the behaviour spec turns vague goals into must, must never, unsure and refusal rules, with examples. Third, every statement should be specific enough to build and to test.

Now it is your turn. This is capstone step one. In the exercise below, write the problem, users, scope and experience sections of your PRD, update your FigJam flow, and draft your behaviour spec. It takes about forty five minutes. In the next lesson, we write the evaluation plan. See you there.
```

## L14 Writing the Evaluation Plan

- **Filename:** `ai-27-ai-product-management_M3_L14_presenter.mp4`
- **Expected length:** about 5.0 minutes (698 words). The quality gate accepts ±10%.

```text
We will evaluate it carefully is not a plan. A plan says what you measure, on which data, against which number, at which moment, and who decides what happens next.

Last time, you wrote the product sections of your PRD. Today is capstone step two. Your evaluation plan turns the metric tree and the test set into a schedule of decisions. It has five parts.

First, test set design: its size, the case types and their shares, who writes the expected behaviour, and how the set is updated. Add new cases from real failures after launch, but keep a fixed core set, so results stay comparable over time.

Second, the rubric and rating method. Define each score with an example. Humans are the reference. If you use an LLM as judge, write a spot check rule, such as humans rate at least twenty percent of judge scored cases, and every case in a weak language.

Third, metrics and thresholds. Each metric gets a pass threshold, good enough to continue. Critical metrics also get a fail threshold that means stop or roll back. Set them before you see results. Critical failures, such as invented refunds or exposed personal data, usually have a threshold of zero.

Fourth, three evaluation moments. Before launch, the test set must pass before any user sees the feature. During the pilot, online metrics against a baseline, and weekly human review. After launch, a dashboard, regular sample reviews and test set reruns after every change. Fifth, a review schedule, with who decides to continue, fix or stop.

Think of the inspection schedule for a new bridge. Engineers test the design before building, and the structure before opening. They inspect it on a fixed schedule after opening, with clear limits that close the bridge. Nobody decides the limits after seeing the cracks.

Let's see an example. Dewi Lestari is a PM at a hypothetical telecom company in Indonesia. Her feature drafts replies for support agents answering messages about data packages, billing and network problems. Agents edit and send each draft.

Her test set has one hundred and fifty invented cases: seventy common, thirty edge, thirty split between formal Indonesian, informal Indonesian and English, and twenty that should refuse or redirect. Two senior agents write the expected behaviour. New failure cases are added every month, but the core one hundred and fifty stay fixed.

The rubric gives two for correct, one for needs editing, and zero for wrong or an invented offer. An LLM judge scores the full set after each change. Senior agents rate a random thirty of those cases, plus every informal language case and every refusal case.

Before launch, the whole set must pass at eighty percent or more, and falling below seventy percent means stop. Each language group must reach seventy five percent, with a stop below sixty five. Invented offers or refunds must be zero, and all twenty refusal cases must redirect correctly.

During the pilot, more than half of drafts should be sent with light or no editing by week four. Handling time must beat the baseline, and the complaint re open rate must not stay above it for two weeks. Dewi and the operations lead meet every two weeks to decide, and the operations lead owns the kill switch.

A common mistake is setting thresholds only for the overall pass rate. A feature can pass overall, while failing a whole language group, or answering requests it should refuse. Add thresholds for each case type and user group.

Let's recap. First, an evaluation plan covers test set design, the rubric and rating method, metrics with thresholds, three evaluation moments and a review schedule with owners. Second, set pass and fail thresholds before seeing results, for each user group, with zero tolerance for critical failures. Third, evaluation continues after launch.

Now it is your turn. This is capstone step two. In the exercise below, write your evaluation plan, with your test set design, rubric, a threshold table of at least six metrics, and a review schedule. Start from your twenty cases from lesson nine. It takes about forty five minutes. In the final lesson, we review and present your PRD. See you there.
```

## L15 Reviewing and Presenting Your PRD

- **Filename:** `ai-27-ai-product-management_M3_L15_presenter.mp4`
- **Expected length:** about 5.0 minutes (695 words). The quality gate accepts ±10%.

```text
The best time to find the weak point in your AI PRD is before the engineering lead, the legal team or your users find it. A structured review, and an honest presentation of trade offs, make that possible.

You now have a full PRD and an evaluation plan. In this final lesson, capstone step three, you review it and present it. Start with a checklist of ten questions that AI features often fail.

Is the problem real, with evidence of user pain? Is AI the right tool, or would a rule be simpler? Is the scope narrow? Is the data available, with owners, coverage and consent? And are the failure paths designed, each with a user action?

Is the behaviour spec testable? Are the metrics and thresholds clear, and set in advance for each group? Does every guardrail have an owner? Is the rollout safe, with numeric stop criteria and a tested kill switch? And is the cost realistic, with current prices checked?

Then ask for a critical review. A peer, or Claude acting as a critical engineering lead, can find questions you did not expect. Treat those questions as prompts for your own thinking, not as final judgements.

When you present, be honest about trade offs. Say what the feature will do, and what it will not do. Show the evaluation results, or the thresholds that must be met. Name the main trade off, and the option you did not choose. Say what you do not know yet, and when you will know it. Then ask for one specific decision.

Before a long flight, pilots walk around the aircraft with a checklist, even after thousands of flights. The checklist does not assume they are careless. It catches the one thing that is easy to miss. Your review checklist does the same for your PRD.

Let's see it in action. Lucía Romero is a PM at a hypothetical agricultural supply distributor in Argentina. Farmers send orders as free text messages. Her feature reads each message and fills a draft order, which staff confirm.

The checklist finds two gaps. There is no plan for messages that mix product names with local nicknames, and no fail threshold for wrong quantities. She adds a coverage note, and a zero tolerance threshold for quantity errors. Both gaps were easy to miss, and both were cheap to fix on paper.

Then Claude, acting as a critical engineering lead, asks questions such as, what happens when a message contains two orders for different farms? And who is responsible when a confirmed order has a wrong quantity? Lucía adds a failure path for multi order messages. And she writes a clear rule: staff confirmation is the final check, and the confirm screen highlights all quantities.

Claude also asks how she will know if the product catalogue changes, and the model starts using old names. So she adds a catalogue change trigger for test set reruns.

To the operations director, she says: the feature drafts orders, and staff still confirm each one. We chose this over automatic orders, because a wrong quantity is costly. We do not yet know quality for local nicknames, and the pilot will tell us in four weeks. I am asking for approval of a four week pilot with two staff members.

A common mistake is presenting only the benefits. Stakeholders can approve an honest pilot much more easily than they can recover from a surprise failure. Present the known limits, and a plan to learn the unknowns.

Let's recap. First, review your AI PRD with a checklist covering problem, tool choice, scope, data, failure paths, behaviour spec, metrics, guardrails, rollout and cost. Second, use a peer or Claude as a critical engineering lead, and decide yourself which questions matter. Third, present trade offs honestly, and ask for one clear decision.

Congratulations! You have reached the end of AI Product Management. For capstone step three, review your PRD with the checklist, ask Claude for its critical questions, and record your decision for each one. Then check the submission checklist in the capstone rubric, and submit your PRD and evaluation plan. Well done, and good luck with your AI feature.
```
