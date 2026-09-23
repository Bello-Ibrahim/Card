# L12 Launch Strategy: Pilots, Rollouts and Monitoring

Course: AI-27 · Module: M3 · Objectives: O5 · Video: 5 min

## Hook
The most important launch decision is one you make before launch: which result would make you stop? If you decide that only after you see the data, it is very easy to find a reason to continue.

## Explanation
You already know how to launch features. AI features need four additions.

**1. Staged rollout.** Release to a small group first, then widen in steps. A common pattern is: internal users, then a small pilot group, then a share of all users, then everyone. Move to the next stage only when a pre-agreed **gate metric** is met.

**2. A/B tests where they make sense.** Compare users with the feature against users without it on your online metrics (L08). This shows whether the feature helps, not only whether people use it. Check the sample size with your data team, and make sure fairness checks cover the groups in your test set.

**3. Feedback loops.** Collect user signals, such as "helpful" or "wrong" buttons, edits and reports. Review a sample of real outputs by hand every week, because users do not report most errors.

**4. Monitoring over time.** AI quality can change after launch even if you change nothing. User behaviour changes, new products or topics appear, and a provider may update a model. This is called **drift**. Monitor quality, guardrail metrics, cost and response time on a dashboard, and rerun your test set whenever the model, prompt or data changes.

Two more parts are essential:

- **Stop criteria, written in advance:** the specific results that pause the rollout, such as "harmful output rate above our limit" or "complaint rate doubles from baseline".
- **A kill switch:** a way to switch the AI feature off quickly and return users to the non-AI fallback (L05), without a new app release. Test it before launch.

**Analogy:** A new restaurant often has a soft launch. First it serves friends and family, then a few evenings for the public with a small menu, then the full opening. At each step, the owners watch what goes wrong in the kitchen. And they decide in advance that if the kitchen cannot serve safely, they close for the evening, whoever is waiting at the door.

## Worked Example
Elif Yilmaz is a PM at a hypothetical ride-hailing app in Turkey. Her new feature reads a rider's complaint after a trip and suggests a category and a draft reply to the support agent, who edits and sends it.

Her rollout plan:

| Stage | Who | Gate metric to move on | Stop criteria |
|---|---|---|---|
| 1. Internal | 10 support agents in one city, 2 weeks | At least 80% of suggested categories accepted without change; no drafts with invented refund promises in the weekly sample | Any draft that exposes another rider's personal data |
| 2. Pilot | All agents in one city, 4 weeks | Median handling time lower than the baseline; complaint re-open rate not higher than the baseline | Re-open rate higher than baseline for 2 weeks in a row; harmful output above the agreed limit |
| 3. Wider rollout | 25%, then 50%, then 100% of agents in all cities | Same metrics stay within limits at each step; Turkish and English quality both above target | Any stop criterion from stage 2; quality drop after a model update |

Monitoring after launch: a weekly dashboard with acceptance rate, handling time, re-open rate, cost per complaint and response time; a weekly review of 50 random drafts by a senior agent; and a rerun of the test set after every prompt or model change. The support operations lead can use the kill switch, which returns agents to the normal empty reply form.

## Common Mistake
Teams often set stop criteria as vague statements, such as "if quality drops significantly". When results come in, nobody agrees what "significantly" means, and the rollout continues. Write stop criteria as numbers compared with a baseline, name who can press the kill switch, and test the kill switch before stage 1.

## Key Takeaways
1. Roll out AI features in stages, with a gate metric that must be met before each next stage.
2. Monitor for drift with dashboards, weekly human review of samples and test-set reruns after every change.
3. Write numeric stop criteria before launch, and have a tested kill switch that returns users to the non-AI fallback.

## Hands-on Exercise
**Task:** Write a rollout plan with 3 stages, the metric that allows each next stage, and the stop criteria.
**Tools:** Google Sheets or a document; optional: FigJam (free plan) for a visual timeline [VERSION].
**Steps:**
1. Define 3 stages: who is included and for how long.
2. For each stage, write one gate metric with a number, using your metric tree from L08.
3. For each stage, write at least one numeric stop criterion compared with a baseline.
4. List what you will monitor after launch and how often.
5. Name who can use the kill switch and describe what users see when it is used.
**What good looks like:** Three clear stages, numeric gates and stop criteria, a monitoring plan that includes human review of samples, and a named kill-switch owner.
**Time:** about 25 minutes

## Review Flags
- [VERSION] FigJam free-plan limits must be checked before recording.
