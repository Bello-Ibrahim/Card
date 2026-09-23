# L03 Finding AI Opportunities in Your Product

Course: AI-27 · Module: M1 · Objectives: O3 · Video: 5 min

## Hook
Ask any team to "find places for AI" and you will get a long list in an hour. Most of the list will be features nobody asked for. The skill is not generating ideas. It is finding the few ideas that start from a real user problem.

## Explanation
A strong AI opportunity usually has three ingredients at the same time:

1. **A real user pain.** Users already lose time, money or confidence at this step. You can point to evidence: support tickets, drop-off in a funnel, interview notes or workarounds users have built.
2. **A repeated judgement task.** Someone, the user or your staff, makes the same kind of decision again and again, and the decision needs judgement across varied cases. Examples: "Is this answer correct?", "Which of these fits me?", "What should I write back?" If the task is rare, or if a simple rule can decide it, AI adds little.
3. **Available data.** Examples of the task exist, or you can create them: past decisions, labelled content, documents or behaviour logs. You will study data needs in detail in L06. At this stage, simply ask, "Could we get examples of good and bad outcomes?"

A useful method is to **walk the user journey**. Take each step in the journey and ask: where do users struggle, where do they wait, where do they make a judgement, and where do our staff do repetitive reviewing? Mark those points. Then check each one against the three ingredients.

Also look behind the product. Some of the best opportunities are internal: helping support staff, content moderators or sales teams do repeated judgement tasks faster. Internal features often have lower risk, because a trained employee sees the AI output before any customer does.

**Analogy:** A good doctor does not start with the newest medicine and look for a patient. They start with the symptoms, find the cause and then choose a treatment. AI is one possible treatment. The user pain is the symptom, and the journey walk is the examination.

The common trap is **solution-first thinking**: adding AI because it is popular, a competitor has it, or leadership asked for "an AI feature". These features are hard to measure, because nobody defined the problem they solve. When you hear "we need AI", translate it into a question: "Which user problem, at which step, would this solve?"

## Worked Example
Camila Rocha is a PM at a hypothetical language-learning app in Brazil. Learners study English and Spanish on their phones. Leadership wants "more AI" in the product.

Camila walks the user journey with her team: sign-up, placement test, daily lessons, speaking practice, reviewing mistakes and renewing the subscription. She collects evidence at each step from support tickets, app reviews and interview notes.

Here are some candidate ideas and what the check shows:

| Idea | Real pain? | Repeated judgement? | Data available? | Keep? |
|---|---|---|---|---|
| Feedback on spoken answers | Yes: learners say they do not know if their speaking is correct | Yes: every speaking exercise | Partly: recordings exist, but consent for use must be checked | Keep, with a data question |
| Explanation of each mistake in the learner's own words | Yes: many tickets ask "why is this wrong?" | Yes: every wrong answer | Yes: lesson content and wrong answers | Keep |
| AI mascot that chats about the weather | No evidence of pain | No | Not relevant | Remove |
| AI-written push notifications | Weak: no clear user problem | Low | Yes | Remove for now |
| Suggested review plan based on past mistakes | Yes: learners forget old words | Yes: daily | Yes: answer history | Keep |

The mascot was the idea leadership liked most. Camila does not argue about taste. She shows that no user evidence supports it and that the three kept ideas each connect to a measurable problem. The discussion moves from "do we have AI?" to "which learner problem do we solve first?"

## Common Mistake
Many PMs judge an opportunity by how impressive the demo would be. An impressive demo of a feature that solves no real problem still fails. Always start the opportunity description with the user and the pain, such as "Learners who make a grammar mistake do not understand why", before you name any AI capability.

## Key Takeaways
1. A strong AI opportunity combines a real user pain, a repeated judgement task and data you can get.
2. Walk the user journey and the internal workflow to find judgement points, then test each against the three ingredients.
3. Translate "we need AI" into "which user problem, at which step?", and remove ideas that have no evidence of pain.

## Hands-on Exercise
**Task:** Use Claude to generate 10 AI opportunities for a product you know, then remove any that do not start from a real user problem.
**Tools:** Claude (free plan) [VERSION]; Google Sheets or a document.
**Steps:**
1. Choose a product you know well. Write a short, general description of its users and main journey steps. Do not paste confidential data, internal metrics or user information into Claude.
2. Ask Claude: "Here is a product and its user journey. Suggest 10 AI feature opportunities. For each, name the journey step, the user problem and the AI capability type."
3. Copy the 10 ideas into a sheet with columns: idea, step, user problem, repeated judgement (yes/no), data available (yes/no/unknown), evidence of pain.
4. For each idea, fill in the evidence column from what you actually know: tickets, research, analytics or your own observation. Write "none" if you have none.
5. Remove every idea with "none" as evidence or "no" for repeated judgement. Keep at least 3.
6. Save the sheet. You will score the remaining ideas in L04.
**What good looks like:** A sheet where each kept idea names a specific user, step and pain with some evidence, and at least 3 ideas are removed with a clear reason. The kept list is shorter and more specific than Claude's original list.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Claude free-plan limits and data-use terms must be checked before recording.
