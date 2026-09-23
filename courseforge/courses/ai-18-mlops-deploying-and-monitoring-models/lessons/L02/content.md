# L02 The MLOps Lifecycle and Maturity Levels

Course: AI-18 · Module: M1 · Objectives: O1, O6 · Video: 5 min

## Hook
Two teams both say "we do MLOps". One has a single script and a checklist. The other has pipelines that retrain and redeploy models without a person touching a keyboard. Are both teams right? This lesson gives you a map to answer that question, and to decide what your own team should build next.

## Explanation
The production ML lifecycle has seven stages connected in a loop:

1. **Data:** collect, clean and version the data used for training.
2. **Training:** run a reproducible training script with a fixed configuration.
3. **Evaluation:** measure the model on a fixed test set and compare it with the current model.
4. **Registration:** store the approved model as a new version in a model registry.
5. **Deployment:** serve the model, for example as an API in a container.
6. **Monitoring:** watch service health, inputs and predictions.
7. **Retraining:** when monitoring shows drift or lower quality, collect new data and start again.

The loop is the important part. A deployed model is not the end of a project. It is the start of a cycle that repeats for as long as the model is in use.

Teams automate this loop to different degrees. A simple way to describe this is with **maturity levels**. Several public frameworks exist and they use different names and numbers, so treat the following as a practical summary, not an official standard:

- **Level 0, manual:** a person trains in a notebook, copies a file to a server and deploys by hand. There is little or no monitoring.
- **Level 1, automated training pipeline:** training, evaluation and registration run as a repeatable pipeline. Deployment may still be manual, but every model version is traceable.
- **Level 2, automated CI/CD:** code changes are tested and built automatically, models are promoted through the registry by rules plus human approval, and monitoring can trigger retraining.

Higher is not always better. Each level costs time to build and maintain. The right level depends on how many models you run, how often the data changes, and how much damage a bad prediction can cause. A good question to ask is: "What is the next single step that removes our biggest risk?"

**Analogy:** Think of how a bakery grows. A home baker works by hand and tastes each batch. A small shop writes down recipes and uses timers. A large factory uses machines, sensors and automatic quality checks. The home baker does not need a factory. They need the next improvement that stops bad batches.

## Worked Example
Compare two hypothetical teams.

**Team A** is a two-person start-up in Nairobi, Kenya, run by Kamau Njoroge and Wairimu Kariuki. They have one model that predicts which small shops will reorder stock. Kamau trains it monthly in a notebook and uploads a file to their server. There is no record of which data produced which file, and nobody checks predictions after release. This is **Level 0**. Their biggest risk is not knowing which model is live or how to go back to the previous one. The next single step: move training into a script, log each run to MLflow (L04), and register each version (L05). This costs a few days and makes rollback possible.

**Team B** is a data science team of twenty people at a large bank in Singapore, led by Tan Wei Ling. They run more than fifty models, and some of them affect lending decisions. They already have automated training pipelines and a registry: **Level 1**. Their biggest risk is slow, inconsistent releases, because each team deploys in its own way. Their next single step: a shared CI/CD pipeline with automatic tests, quality gates and a required human approval before promotion (L11 to L14). Full automation of retraining can wait until the release process is stable.

The same framework gives very different advice to each team, because their risks are different.

## Common Mistake
Many learners believe that every team should aim for full automation as quickly as possible. Automating an unstable or poorly understood process only makes the problems happen faster. A team that cannot yet reproduce one training run will not benefit from automatic retraining. Build reproducibility and traceability first, then automate the steps that are repeated most often and cause the most errors.

## Key Takeaways
1. The production ML lifecycle is a loop: data, training, evaluation, registration, deployment, monitoring and retraining.
2. Maturity levels describe how much of this loop is automated, from manual work to full CI/CD with monitoring.
3. Choose the next single improvement that removes your biggest risk, rather than aiming for maximum automation.

## Hands-on Exercise
**Task:** Place three hypothetical teams on a maturity level and recommend the next single improvement for one of them.
**Tools:** Pen and paper, or any notes app.
**Steps:**
1. Read the three descriptions:
   - **Team 1:** A logistics company in Egypt retrains its route-time model by running a script every week. Each run is logged and registered, but a person copies the new model file to the server by hand.
   - **Team 2:** A university research group in Vietnam has a promising crop-disease model in a notebook. A partner organisation now wants to use it daily.
   - **Team 3:** An online retailer in Germany tests and builds every code change automatically, promotes models after an approval step, and retrains when drift alerts fire.
2. Assign a level (0, 1 or 2) to each team and write one sentence of evidence for each.
3. Choose one team. Write its biggest risk and the next single improvement, in three or four sentences.
4. Note one improvement that team should **not** make yet, and why.
**What good looks like:** Team 1 is Level 1, Team 2 is Level 0 and Team 3 is Level 2. The recommendation names a concrete risk, such as "no way to roll back" or "manual copying can deploy the wrong file", and proposes one proportionate step, such as automating deployment of the registered model.
**Time:** about 20 minutes

## Review Flags
- None. The maturity levels are presented as a practical summary rather than an official standard, and all teams are hypothetical.
