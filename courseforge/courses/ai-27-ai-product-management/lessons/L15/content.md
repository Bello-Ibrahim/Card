# L15 Reviewing and Presenting Your PRD

Course: AI-27 · Module: M3 · Objectives: O5, O6 · Video: 5 min

## Hook
The best time to find the weak point in your AI PRD is before the engineering lead, the legal team or your users find it. A structured review, and an honest presentation of trade-offs, make that possible.

## Explanation
Review your PRD with a checklist of questions that AI features often fail:

1. **Is the problem real?** Is there evidence of user pain, not only interest in AI?
2. **Is AI the right tool?** Would a rule or better design solve it more simply?
3. **Is the scope narrow?** One user, one task, human in the loop, fallback?
4. **Is the data available?** Named sources and owners, coverage of all user groups, consent, and a cold-start plan?
5. **Are failure paths designed?** Wrong, unsure, should not answer and unavailable, each with a user action?
6. **Is the behaviour spec testable?** Could each rule become a test case?
7. **Are the metrics and thresholds clear?** All three layers, numbers set in advance, thresholds for each group?
8. **Are the guardrails owned?** Every guardrail with a named owner, and legal questions listed for each launch country?
9. **Is the rollout safe?** Stages, gate metrics, numeric stop criteria and a tested kill switch?
10. **Is the cost realistic?** Realistic request sizes, higher-usage scenarios and current prices checked?

Then ask for a **critical review**. A peer, or Claude acting as a critical engineering lead, can find questions you did not expect. Treat Claude's questions as prompts for your own thinking, not as final judgements.

**Presenting trade-offs honestly.** Stakeholders need to decide with a clear view of the risks. In your presentation:

- State what the feature will do and what it will not do.
- Show the current evaluation results or, if you have none yet, the thresholds that must be met.
- Name the main trade-off, such as "narrower scope now in exchange for lower risk", and the option you did not choose.
- Say what you do not know yet, and when you will know it.
- Ask for a specific decision.

**Analogy:** Before a long flight, pilots walk around the aircraft with a checklist, even after thousands of flights. The checklist does not assume they are careless. It catches the one thing that is easy to miss. Your review checklist does the same for your PRD.

## Worked Example
Lucía Romero is a PM at a hypothetical agricultural supply distributor in Argentina. Farmers send orders as free-text messages, and staff type them into the order system. Her feature reads each message and fills a draft order, which staff confirm.

She reviews her PRD with the checklist and finds two gaps: no plan for messages that mix product names with local nicknames (question 4), and no fail threshold for wrong quantities (question 7). She adds a coverage note and a zero-tolerance threshold for quantity errors in the test set.

Then she asks Claude to act as a critical engineering lead. It asks, among other things: "What happens when a message contains two orders for different farms?", "How will you know if the product catalogue changes and the model starts using old names?" and "Who is responsible when a confirmed order has a wrong quantity?" Lucía adds a failure path for multi-order messages and a catalogue-change trigger for test-set reruns. For the third question, she writes a clear rule: staff confirmation is the final check, and the confirm screen highlights all quantities.

In her presentation to the operations director, she says: "The feature drafts orders, and staff still confirm each one. We chose this over automatic orders because a wrong quantity is costly. We do not yet know quality for messages with local product nicknames; the pilot will tell us in four weeks. I am asking for approval of a four-week pilot with two staff members."

## Common Mistake
Many PMs present only the benefits and hide the uncertainties, hoping to win approval. When problems appear later, trust is lost. Present the known limits and the unknowns with a plan to learn them. Stakeholders can approve a clear, honest pilot much more easily than they can recover from an unexpected failure.

## Key Takeaways
1. Review an AI PRD with a checklist covering problem, tool choice, scope, data, failure paths, behaviour spec, metrics, guardrails, rollout and cost.
2. Use a peer or Claude as a critical engineering lead to find questions you missed, and decide yourself which ones matter.
3. Present trade-offs honestly: what it will and will not do, the option you did not choose, what is unknown and the decision you need.

## Hands-on Exercise
**Task:** Capstone step 3: review your PRD with the checklist, ask Claude to act as a critical engineering lead and list its questions, then finalise the PRD and evaluation plan.
**Tools:** Your PRD document; Claude (free plan) [VERSION]; FigJam (free plan) for flow updates [VERSION].
**Steps:**
1. Answer the 10 checklist questions for your PRD. Mark each yes, partly or no.
2. Fix every "no" and as many "partly" answers as you can.
3. Remove confidential or personal details from your PRD, then paste it into Claude with this prompt: "Act as a critical engineering lead. List the 10 most important questions you would ask before building this feature."
4. For each question, decide: change the PRD, add it to open questions, or explain why it does not apply.
5. Write a five-sentence stakeholder summary following the structure in this lesson.
6. Check the submission checklist in the capstone rubric and submit.
**What good looks like:** A final PRD and evaluation plan where every checklist question has a clear answer, Claude's questions are handled with visible decisions, and a short, honest summary asks for one specific decision.
**Time:** about 50 minutes

## Review Flags
- [VERSION] Claude free-plan limits and data-use terms, and FigJam free-plan limits, must be checked before recording.
