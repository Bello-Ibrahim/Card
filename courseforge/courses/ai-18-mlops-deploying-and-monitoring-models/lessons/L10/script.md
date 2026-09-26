# L10 Deployment Targets and Release Strategies | Presenter Script

Course: AI-18 · Video: 5 min · Words: 727

## Hook
You have a new model version that scored better offline. Do you switch all users to it at once? If it fails, how fast can you switch back, and who decides? A release strategy answers these questions before anything goes wrong.

## Explain
In the last lesson, we measured our container's speed. Now, where does it run? There are three common targets. A single server is simple, but you handle restarts, updates and scaling yourself. A container platform restarts failed containers, runs several copies and can shift traffic between versions, but it takes more set-up and knowledge.

A managed ML service from a cloud provider does much of the serving for you, but you depend on its features, limits and prices. Free tiers are useful for learning, but they change often. Check the current terms, and never rely on a free tier for a critical service.

Now, how do new versions reach users? Blue-green runs the old and new versions side by side, then switches all traffic at once. Rollback is switching back. Canary sends a small share of real traffic, say five percent, to the new version. You watch errors, latency and prediction quality, then increase the share step by step.

Shadow sends a copy of real traffic to the new version, but users only see the old version's answers. You compare both sets of predictions with no risk to users, but serving costs double for that period. And every release needs a rollback plan: what signal triggers it, who can trigger it, and how.

A rollback trigger must be measurable. For example, an error rate above two percent for ten minutes. Choose the numbers for your own service. These are examples, not standards. With our registry and image tags, rollback means running the previous image, or moving the champion alias back.

Think of a restaurant chain changing a recipe. Blue-green prepares a second kitchen and switches all orders at once. Canary serves the new recipe in one branch first. Shadow cooks the new dish in the back for every order and tastes it, while guests still receive the old dish.

## Demonstrate
Let's look at two hypothetical teams. In Kisumu, Kenya, Doctor Achieng Odhiambo's team uses a model that suggests how urgent each patient is, to help nurses order the waiting list. A nurse always makes the final decision. But a wrong new model could delay urgent care, so the risk to people is high.

So the team starts with shadow deployment. For two weeks, the new model scores every case, but only the old suggestion appears on screen. Clinicians review the cases where the two models disagree. Only then do they release with blue-green, keeping the old version ready. Local regulations may also require approval before any change.

In Recife, Brazil, Lucas Ferreira's team runs product recommendations for an online fashion shop. A weaker recommendation costs some sales, but harms nobody, and they want to learn from real clicks quickly. They choose a canary: five percent of traffic for one day, then twenty-five percent, then everyone.

Their rollback trigger is simple. If the canary group's click-through rate falls clearly below the old version, or the p ninety-five latency goes over the page's budget, they switch back. The same technology leads to different choices, because the cost of a mistake is different.

A common mistake is to write a rollback plan but never test it. Then, in the first real incident, the old image was deleted, or nobody has permission to deploy. Practise the rollback on a normal day, and keep the previous image and model version available.

## Recap
Let's recap. First, models can run on a single server, a container platform or a managed ML service, and each trades control for convenience. Second, blue-green, canary and shadow releases reduce risk in different ways, so choose by the cost of a mistake. Third, every release needs a measurable rollback trigger and a tested rollback procedure.

## CTA
In the exercise below this video, you will choose a release strategy and a rollback trigger for three scenarios, a bank in Morocco, a news site in Indonesia and a water utility in Peru. It takes about twenty-five minutes. Your capstone demo will include a real rollback.

That completes week two. Next week we automate everything, starting with Testing ML Code and Models. See you there.

## Thumbnail
Headline: Release Safely, Roll Back Fast
Image: Navy background, three traffic paths labelled blue-green, canary and shadow with a teal curved rollback arrow, headline in teal Inter Bold.

## Production Notes
- [VERSION] Free hosting tiers for deployment targets change often; the voiceover names no provider and no free limits. Do not add any tier details on slides without checking them.
- [REGION] Approval rules for changes to clinical decision-support tools differ by country; the Kenya example says only that local regulations may require approval and states no specific rule.
- The rollback thresholds (2% error rate for 10 minutes, 15 percentage points, 5% then 25% canary steps) are illustrations, not standards; the voiceover says so.
- Dr. Achieng Odhiambo's Kisumu hospital team and Lucas Ferreira's Recife fashion shop are hypothetical. Hospital stock footage must not show identifiable patients or a real hospital name.
- This is a concept lesson (not in screen_demo_lessons): slides and stock only.
