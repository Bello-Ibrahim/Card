# L13 Writing the AI PRD: Structure and Scope

Course: AI-27 · Module: M3 · Objectives: O6 · Video: 5 min

## Hook
A standard PRD describes what the product should do. An AI PRD must also describe what the product should do when it is wrong, unsure or asked something it should not answer. This week, you write one.

## Explanation
**The capstone brief.** Write a complete PRD and evaluation plan for one AI feature, using the work from earlier lessons. You write it in three steps: the product sections now (L13), the evaluation plan (L14), and a review and final version (L15). The capstone rubric describes how it is marked. Read it before you start.

You already know the standard PRD sections, so this template only lists them briefly and adds the AI-specific sections in detail.

**AI PRD template**

1. **Problem and users** (standard): the user, the pain and the evidence (L03).
2. **Scope and capability:** the one user, one task, capability type (L02), what is out of scope, and why AI is needed instead of a rule.
3. **Experience:** the happy path and the four failure paths: wrong, unsure, should not answer, unavailable (L05). Link your FigJam flow.
4. **Data needs:** your data requirements table: sources, owners, quality, coverage, consent, cold-start plan (L06).
5. **Model behaviour spec:** what the AI must do, must never do, how it behaves when unsure, when it refuses, its tone and format, and 3 to 5 example inputs with good outputs.
6. **Build approach and cost:** build, buy or API, with your cost estimate and placeholder prices marked (L07).
7. **Evaluation plan:** metric tree, test set and thresholds (written in L14).
8. **Failure modes:** a list of the ways it can fail, how likely each is, and how the design or guardrails reduce it.
9. **Human oversight:** who reviews what, when, and what authority they have to change or stop outputs.
10. **Risks and launch guardrails:** your risk table with owners (L11), and the legal questions for your launch countries.
11. **Rollout and monitoring:** stages, gate metrics, stop criteria, kill switch and dashboard (L12).
12. **Open questions** (standard), with an owner and a date for each.

Sections 2 to 11 are what an AI PRD adds or changes. The **model behaviour spec** is the most useful new section. It turns vague wishes such as "helpful and accurate" into specific rules that engineers can build and testers can check.

**Analogy:** A normal PRD is like a job description: tasks and results. An AI PRD is more like the induction guide for the talented new colleague from L01. It explains the tasks, and also what to do when unsure, what they must never do, who checks their work, and when to call a manager.

## Worked Example
Haruto Sato is a PM at a hypothetical industrial equipment company in Japan. Field technicians repair packaging machines at customer sites and often search long manuals on their phones. Haruto's feature: a technician describes a fault, and the assistant finds the relevant manual sections and summarises the repair steps, with links to the source pages.

Parts of his PRD:

**Scope:** technicians with at least one year of experience; one task: find and summarise repair procedures for the three most common machine models. Out of scope: machine models without digital manuals, and any instruction not found in a manual. Capability: retrieval plus generation.

**Model behaviour spec (extract):**
- Must: answer only from retrieved manual sections; show the source page for every step; answer in Japanese or English to match the question.
- Must never: invent a step, a part number or a torque value; give steps for a different model without saying so.
- When unsure: say "I could not find this in the manual for model X", list the closest sections, and suggest calling the support desk.
- Refuse: requests to bypass safety locks, with a message that points to the safety procedure.
- Example: input "Model B, error E12, film not cutting" → a short list of steps from the cutter section, with page links.

**Human oversight:** a senior technician reviews 30 random answers each week and can add a manual section to a block list if answers from it are often wrong.

**Failure path in FigJam:** when no section matches, the technician sees the closest sections and a "Call support" button, with the fault description already filled in.

## Common Mistake
Many learners fill the template with general statements, such as "the model will be accurate and safe". These cannot be built or tested. Every line in the behaviour spec should be specific enough that a tester could write a test case for it, such as "never gives a torque value that is not in the retrieved section".

## Key Takeaways
1. An AI PRD keeps the standard sections and adds scope with capability, experience for errors, data needs, a model behaviour spec, evaluation, failure modes, human oversight, guardrails and monitoring.
2. The model behaviour spec turns vague goals into specific must, must-never, unsure and refusal rules with examples.
3. Every statement in the PRD should be specific enough to build and to test.

## Hands-on Exercise
**Task:** Capstone step 1: write the problem, users, scope and experience sections of your PRD, with a FigJam flow for the happy and failure paths.
**Tools:** Google Docs or any document; FigJam (free plan) [VERSION]; optional: Claude (free plan) [VERSION].
**Steps:**
1. Copy the 12 template headings into a new document.
2. Write sections 1 and 2 using your work from L03 to L05.
3. Update your FigJam flow from L05 so it shows the happy path and all four failure paths. Link or paste a screenshot into section 3.
4. Draft section 5, the model behaviour spec, with at least 3 must rules, 3 must-never rules, the unsure behaviour, a refusal rule and 3 examples.
5. Optional: ask Claude to find any rule in your behaviour spec that is too vague to test. Do not paste confidential information.
6. Leave sections 7 to 12 with notes; you complete them in L14 and L15.
**What good looks like:** A clear problem with evidence, a narrow scope, a complete flow with four failure paths, and a behaviour spec where every rule could become a test case.
**Time:** about 45 minutes

## Review Flags
- [VERSION] FigJam free-plan limits and Claude free-plan limits and data-use terms must be checked before recording.
