# L15 Reviewing and Presenting Your PRD | Presenter Script

Course: AI-27 · Video: 5 min · Words: 640

## Hook
The best time to find the weak point in your AI PRD is before the engineering lead, the legal team or your users find it. A structured review, and an honest presentation of trade offs, make that possible.

## Explain
You now have a full PRD and an evaluation plan. In this final lesson, capstone step three, you review it and present it. Start with a checklist of ten questions that AI features often fail.

Is the problem real, with evidence of user pain? Is AI the right tool, or would a rule be simpler? Is the scope narrow? Is the data available, with owners, coverage and consent? And are the failure paths designed, each with a user action?

Is the behaviour spec testable? Are the metrics and thresholds clear, and set in advance for each group? Does every guardrail have an owner? Is the rollout safe, with numeric stop criteria and a tested kill switch? And is the cost realistic, with current prices checked?

Then ask for a critical review. A peer, or Claude acting as a critical engineering lead, can find questions you did not expect. Treat those questions as prompts for your own thinking, not as final judgements.

When you present, be honest about trade offs. Say what the feature will do, and what it will not do. Show the evaluation results, or the thresholds that must be met. Name the main trade off, and the option you did not choose. Say what you do not know yet, and when you will know it. Then ask for one specific decision.

Before a long flight, pilots walk around the aircraft with a checklist, even after thousands of flights. The checklist does not assume they are careless. It catches the one thing that is easy to miss. Your review checklist does the same for your PRD.

## Demonstrate
Let's see it in action. Lucía Romero is a PM at a hypothetical agricultural supply distributor in Argentina. Farmers send orders as free text messages. Her feature reads each message and fills a draft order, which staff confirm.

The checklist finds two gaps. There is no plan for messages that mix product names with local nicknames, and no fail threshold for wrong quantities. She adds a coverage note, and a zero tolerance threshold for quantity errors.

Then Claude, acting as a critical engineering lead, asks questions such as, what happens when a message contains two orders for different farms? And who is responsible when a confirmed order has a wrong quantity? Lucía adds a failure path for multi order messages. And she writes a clear rule: staff confirmation is the final check, and the confirm screen highlights all quantities.

To the operations director, she says: the feature drafts orders, and staff still confirm each one. We chose this over automatic orders, because a wrong quantity is costly. We do not yet know quality for local nicknames, and the pilot will tell us in four weeks. I am asking for approval of a four week pilot with two staff members.

A common mistake is presenting only the benefits. Stakeholders can approve an honest pilot much more easily than they can recover from a surprise failure.

## Recap
Let's recap. First, review your AI PRD with a checklist covering problem, tool choice, scope, data, failure paths, behaviour spec, metrics, guardrails, rollout and cost. Second, use a peer or Claude as a critical engineering lead, and decide yourself which questions matter. Third, present trade offs honestly, and ask for one clear decision.

## CTA
Congratulations! You have reached the end of AI Product Management. For capstone step three, review your PRD with the checklist, ask Claude for its critical questions, and record your decision for each one. Then check the submission checklist in the capstone rubric, and submit your PRD and evaluation plan. Well done, and good luck with your AI feature.

## Thumbnail
Headline: Find the Weak Point First
Image: Navy background, a pilot's pre-flight checklist on a clipboard beside a PRD document with ticks, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude free-plan limits and data-use terms, and FigJam free-plan limits, must be checked before recording (exercise tools).
- Lucía Romero and the agricultural supply distributor in Argentina are hypothetical; stock footage must not show a real company, product brand or logo.
- Claude's questions in the worked example are shown as the example questions from content.md, not as a live recording; Claude's review is described as prompts for the PM's own thinking, not final judgements.
- This is the last lesson: the CTA congratulates learners and points to the capstone submission and the submission checklist in the capstone rubric.
