# L10 Deployment Targets and Release Strategies

Course: AI-18 · Module: M2 · Objectives: O6 · Video: 5 min

## Hook
You have a new model version that scored better offline. Do you switch all users to it at once? If it fails, how fast can you switch back, and who decides? A release strategy answers these questions before anything goes wrong.

## Explanation
**Where the model runs.** There are three common deployment targets for a containerised model API:

- **A single server or virtual machine.** You run the container yourself. It is simple and cheap to understand, but you handle restarts, updates and scaling.
- **A container platform**, such as Kubernetes or a managed container service. It restarts failed containers, runs several copies and can shift traffic between versions. It takes more set-up and knowledge.
- **A managed ML service** from a cloud provider. It handles much of the serving for you, but you depend on that provider's features, limits and prices.

Several providers offer free tiers that are useful for learning. Their limits change often, so check the current terms before you plan around them, and do not rely on a free tier for a critical service. [VERSION]

**How new versions are released.** Four strategies matter for models:

1. **Blue-green:** run the old version (blue) and the new version (green) side by side, then switch all traffic at once. Rollback is switching back.
2. **Canary:** send a small share of real traffic, for example 5%, to the new version. Watch errors, latency and prediction quality, then increase the share step by step.
3. **Shadow:** send a copy of real traffic to the new version, but users only see the old version's answers. You compare both sets of predictions with no risk to users. It doubles serving cost for that period.
4. **Rollback plan:** for every release, decide in advance what signal triggers a rollback, who can trigger it, and how. Then test it. With the registry and image tags from earlier lessons, rollback means running the previous image or moving the `champion` alias back.

A **rollback trigger** must be measurable, for example "error rate above 2% for 10 minutes" or "share of positive predictions changes by more than 15 percentage points". Choose the numbers for your own service; these are examples, not standards.

**Analogy:** Releasing a model is like changing the recipe in a restaurant chain. Blue-green is preparing a second kitchen and switching all orders at once. Canary is serving the new recipe in one branch first. Shadow is cooking the new dish in the back for every order and tasting it, while guests still receive the old dish.

## Worked Example
Two hypothetical teams choose strategies.

**A hospital triage tool in Kisumu, Kenya.** Dr. Achieng Odhiambo's team uses a model that suggests how urgent a patient is, to help nurses order the waiting list. A nurse always makes the final decision. A wrong new model could delay urgent care, so the risk to people is high. The team chooses **shadow deployment** first: the new model scores every case for two weeks, but only the old model's suggestion appears on screen. Clinicians review cases where the two models disagree. Only then does the team release with **blue-green**, keeping the old version ready. Rollback trigger: any confirmed case where the new model marked an urgent patient as non-urgent, or a disagreement rate above the level agreed in the review. Local health regulations may also require approval before any change in a clinical tool. [REGION]

**A product recommender in Recife, Brazil.** Lucas Ferreira's team runs recommendations for an online fashion shop. A weaker recommendation costs some sales but harms nobody, and the team wants to learn from real clicks quickly. They choose a **canary**: 5% of traffic for one day, then 25%, then 100%. Rollback trigger: click-through rate for the canary group falls clearly below the old version, or p95 latency rises above the page's budget.

The same technology gives different choices because the cost of a mistake is different.

## Common Mistake
Many teams write a rollback plan but never test it. When the first real incident happens, they discover that the old image was deleted, the alias was renamed or nobody has permission to deploy. Practise the rollback on a normal day, record how long it took, and keep at least the previous image and model version available.

## Key Takeaways
1. Models can run on a single server, a container platform or a managed ML service; each trades control for convenience.
2. Blue-green, canary and shadow releases reduce risk in different ways; choose based on the cost of a mistake.
3. Every release needs a measurable rollback trigger and a rollback procedure that has been tested.

## Hands-on Exercise
**Task:** For 3 scenarios, choose a release strategy and a rollback trigger, and justify each choice in two sentences.
**Tools:** Pen and paper, or any notes app.
**Steps:**
1. Read the three hypothetical scenarios:
   - A bank in Morocco updates a model that flags suspicious card payments in real time.
   - A news website in Indonesia updates a model that orders headlines on its home page.
   - A water utility in Peru updates a monthly batch model that predicts which pipes need inspection.
2. For each scenario, choose blue-green, canary or shadow (or a batch equivalent, such as comparing two batch outputs before publishing).
3. Write one measurable rollback trigger for each scenario.
4. Justify each choice in two sentences: the cost of a mistake and why your strategy controls it.
5. For one scenario, write the rollback steps as a numbered list of at most five actions.
**What good looks like:** Each choice links the strategy to the risk. Triggers are measurable, with a metric, a threshold and a time window. The rollback steps name the previous image or model version and who can run them.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Free hosting tiers for deployment targets change often; the lesson names no specific free limits, and any tier mentioned in the video must be checked before recording.
- [REGION] Approval rules for changes to clinical decision-support tools differ by country; the Kenya example does not state a specific rule.
- All teams and scenarios are hypothetical, and the example rollback thresholds are illustrations, not standards.
