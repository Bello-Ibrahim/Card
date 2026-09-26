# L12 Launch Strategy: Pilots, Rollouts and Monitoring | Presenter Script

Course: AI-27 · Video: 5 min · Words: 689

## Hook
The most important launch decision is one you make before launch. Which result would make you stop? If you decide that only after you see the data, it is very easy to find a reason to continue.

## Explain
Last time, you wrote your risks and guardrails. Now we plan the launch. You already know how to launch features. AI features need four additions.

First, a staged rollout. Release to internal users, then a small pilot group, then a share of all users, then everyone. Move to the next stage only when a gate metric, agreed in advance, is met. Second, A B tests where they make sense. Compare users with and without the feature on your online metrics, to see whether it helps, not only whether people use it.

Third, feedback loops. Collect signals such as helpful or wrong buttons, edits and reports. And review a sample of real outputs by hand every week, because users do not report most errors.

Fourth, monitoring over time. AI quality can change after launch even if you change nothing. User behaviour changes, new topics appear, and a provider may update a model. This is called drift. So track quality, guardrails, cost and response time on a dashboard, and rerun your test set whenever the model, prompt or data changes.

Two more parts are essential. Stop criteria, written in advance, such as the complaint rate doubling from the baseline. And a kill switch, a way to turn the AI feature off quickly and return users to the non AI fallback, without a new app release. Test it before launch.

Think of a new restaurant with a soft launch. First it serves friends and family, then a few public evenings with a small menu, then the full opening. And the owners decide in advance that if the kitchen cannot serve safely, they close for the evening, whoever is waiting at the door.

## Demonstrate
Let's see a plan. Elif Yilmaz is a PM at a hypothetical ride hailing app in Turkey. Her feature reads a rider's complaint after a trip, and suggests a category and a draft reply to the support agent, who edits and sends it.

Stage one is internal: ten agents in one city for two weeks. To move on, at least eighty percent of suggested categories must be accepted without change, with no invented refund promises in the weekly sample. Any draft that exposes another rider's personal data stops the rollout.

Stage two is a pilot with all agents in one city, for four weeks. Handling time must be lower than the baseline, and the complaint re open rate no higher. If the re open rate is above the baseline for two weeks in a row, or harmful output passes the agreed limit, the rollout stops.

Stage three widens to twenty five, then fifty, then one hundred percent of agents in all cities. The same metrics must stay within limits at each step, with quality above target in both Turkish and English. A quality drop after a model update also stops the rollout.

After launch, Elif watches a weekly dashboard, a senior agent reviews fifty random drafts each week, and the test set is rerun after every change. The support operations lead owns the kill switch, which returns agents to the normal empty reply form.

A common mistake is a vague stop criterion, such as if quality drops significantly. Nobody agrees what significantly means. Write numbers against a baseline, and name who presses the kill switch.

## Recap
Let's recap. First, roll out AI features in stages, with a gate metric that must be met before each next stage. Second, monitor for drift with dashboards, weekly human review of samples, and test set reruns after every change. Third, write numeric stop criteria before launch, and have a tested kill switch that returns users to the fallback.

## CTA
Now it is your turn. In the exercise below, write a rollout plan with three stages, a gate metric for each, and numeric stop criteria. It takes about twenty five minutes. From the next lesson, you start your capstone: writing the AI PRD, its structure and scope. See you there.

## Thumbnail
Headline: Decide When to Stop
Image: Navy background, three stepping stones labelled 1, 2, 3 leading to a door, with a red stop switch beside them, headline in teal Inter Bold.

## Production Notes
- [VERSION] FigJam free-plan limits must be checked before recording (optional exercise tool).
- Elif Yilmaz and the ride-hailing app in Turkey are hypothetical; stock footage must not show a real ride-hailing brand, app screen or logo.
- The rollout table figures (10 agents for 2 weeks, 80 percent accepted, 4-week pilot, 25, 50 then 100 percent, 50 random drafts a week) come from the content.md worked example.
