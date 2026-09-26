# L13 Writing the AI PRD: Structure and Scope | Presenter Script

Course: AI-27 · Video: 5 min · Words: 666

## Hook
A standard PRD describes what the product should do. An AI PRD must also describe what it should do when it is wrong, unsure, or asked something it should not answer. This week, you write one.

## Explain
This is where your capstone begins. You will write a complete PRD and evaluation plan for one AI feature, in three steps. The product sections now, the evaluation plan in the next lesson, and a review and final version in the last lesson. Read the capstone rubric before you start, because it shows how your work is marked.

Here is the AI PRD template. You already know the standard sections, such as problem and users, and open questions. So look at what sits between them. Scope and capability. Experience, with the happy path and four failure paths. Data needs. The model behaviour spec. And build approach and cost.

Then the evaluation plan, which you write next time. Failure modes, and how the design reduces each one. Human oversight: who reviews what, and who can stop outputs. Risks and launch guardrails, with owners. Rollout and monitoring. And finally, open questions, each with an owner and a date.

Sections two to eleven are what an AI PRD adds or changes. Each one reuses work from earlier lessons. Your scope, your failure flow, your data table, your cost estimate, your risk table and your rollout plan all have a place here.

The most useful new section is the model behaviour spec. It turns vague wishes, such as helpful and accurate, into specific rules. What the AI must do. What it must never do. How it behaves when unsure, when it refuses, its tone and format, and three to five example inputs with good outputs.

Remember the talented new colleague from lesson one? A normal PRD is like a job description. An AI PRD is more like their induction guide. It explains the tasks, and also what to do when unsure, what they must never do, who checks their work, and when to call a manager.

## Demonstrate
Let's look at an example. Haruto Sato is a PM at a hypothetical industrial equipment company in Japan. Field technicians repair packaging machines at customer sites, and often search long manuals on their phones.

His scope: technicians with at least one year of experience, and one task, finding and summarising repair steps for the three most common machine models, with links to the source pages. Machines without digital manuals are out of scope. The capability is retrieval plus generation.

His behaviour spec says the assistant must answer only from retrieved manual sections, and show the source page for every step. It must never invent a step, a part number or a torque value. When unsure, it says it could not find this in the manual, and suggests calling support. And it refuses requests to bypass safety locks.

For human oversight, a senior technician reviews thirty random answers each week, and can block a manual section that often gives wrong answers. In his FigJam flow, when no section matches, the technician sees the closest sections, and a call support button with the fault already filled in.

A common mistake is filling the template with general statements, such as the model will be accurate and safe. Every rule should be specific enough that a tester could write a test case for it.

## Recap
Let's recap. First, an AI PRD keeps the standard sections, and adds scope, experience for errors, data, a behaviour spec, evaluation, failure modes, oversight, guardrails and monitoring. Second, the behaviour spec turns vague goals into must, must never, unsure and refusal rules, with examples. Third, every statement should be specific enough to build and to test.

## CTA
Now it is your turn. This is capstone step one. In the exercise below, write the problem, users, scope and experience sections of your PRD, update your FigJam flow, and draft your behaviour spec. It takes about forty five minutes. In the next lesson, we write the evaluation plan. See you there.

## Thumbnail
Headline: The AI PRD Template
Image: Navy background, a document with twelve numbered section lines, sections 2 to 11 highlighted in teal, headline in teal Inter Bold.

## Production Notes
- [VERSION] FigJam free-plan limits and Claude free-plan limits and data-use terms must be checked before recording (exercise tools).
- The AI PRD template must appear on slides with all 12 section names exactly as in content.md: 1 Problem and users; 2 Scope and capability; 3 Experience; 4 Data needs; 5 Model behaviour spec; 6 Build approach and cost; 7 Evaluation plan; 8 Failure modes; 9 Human oversight; 10 Risks and launch guardrails; 11 Rollout and monitoring; 12 Open questions.
- The voiceover does not reteach standard PRD sections (problem, users, open questions); it names them and focuses on sections 2 to 11.
- Haruto Sato and the industrial equipment company in Japan are hypothetical; stock footage must not show a real machine brand or logo. Error code E12 and 'Model B' are invented.
