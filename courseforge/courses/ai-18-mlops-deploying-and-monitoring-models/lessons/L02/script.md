# L02 The MLOps Lifecycle and Maturity Levels | Presenter Script

Course: AI-18 · Video: 5 min · Words: 685

## Hook
Two teams both say, we do MLOps. One has a single script and a checklist. The other has pipelines that retrain and redeploy models without anyone touching a keyboard. Are both teams right?

## Explain
In the last lesson, we saw why models fail after the notebook. Today you get a map of the whole production lifecycle, and a way to decide what your own team should build next.

The production lifecycle has seven stages, connected in a loop. First, data: collect, clean and version it. Then training, with a reproducible script. Then evaluation on a fixed test set, compared with the current model. Then registration, where the approved model becomes a new version in a registry.

Next comes deployment, for example as an API in a container. Then monitoring of service health, inputs and predictions. And when monitoring shows drift or lower quality, retraining starts the loop again. The loop is the important part. A deployed model is not the end of a project. It is the start of a cycle.

Teams automate this loop to different degrees. We describe this with maturity levels. Several public frameworks use different names and numbers, so treat this as a practical summary, not an official standard. At level zero, everything is manual. A person trains in a notebook, copies a file to a server, and there is little monitoring.

At level one, training, evaluation and registration run as a repeatable pipeline. Deployment may still be manual, but every model version is traceable. At level two, code changes are tested and built automatically, models are promoted by rules plus human approval, and monitoring can trigger retraining.

Higher is not always better. Think of how a bakery grows. A home baker works by hand and tastes each batch. A small shop writes down recipes and uses timers. A factory uses machines and sensors. The home baker does not need a factory. They need the next improvement that stops bad batches.

## Demonstrate
Let's compare two hypothetical teams. Team A is a two-person start-up in Nairobi, run by Kamau Njoroge and Wairimu Kariuki. Their one model predicts which small shops will reorder stock. Kamau trains it monthly in a notebook and uploads a file to their server.

Nobody records which data produced which file, and nobody checks predictions after release. That is level zero. Their biggest risk is not knowing which model is live, or how to go back. The next single step is to move training into a script, log each run to MLflow, and register each version. It costs a few days, and it makes rollback possible.

Team B is a data science team of twenty people at a large bank in Singapore, led by Tan Wei Ling. They run more than fifty models, and some affect lending decisions. They already have automated training pipelines and a registry. That is level one.

Their biggest risk is slow, inconsistent releases, because each team deploys in its own way. Their next single step is a shared CI and CD pipeline, with automatic tests, quality gates and a required human approval before promotion. Full automatic retraining can wait until releases are stable.

The same framework gives very different advice, because the risks are different. And here is a common mistake. Automating an unstable process only makes the problems happen faster. If you cannot reproduce one training run, automatic retraining will not help you. Build reproducibility first, then automate.

## Recap
Let's recap. First, the production lifecycle is a loop: data, training, evaluation, registration, deployment, monitoring and retraining. Second, maturity levels describe how much of that loop is automated, from manual work to full CI and CD with monitoring. Third, choose the next single improvement that removes your biggest risk.

## CTA
In the exercise below this video, you will read about three teams, in Egypt, Vietnam and Germany. You will place each one on a maturity level, then recommend the next single improvement for one of them. It takes about twenty minutes.

In the next lesson, we start building. We turn a notebook into a real project, in Structuring an ML Project for Production. See you there.

## Thumbnail
Headline: How Mature Is Your MLOps?
Image: Navy background, a teal circular loop of seven small icons with a three-step staircase beside it, headline in teal Inter Bold.

## Production Notes
- No facts to verify: content.md Review Flags are None. The maturity levels are a practical summary, not an official standard; the voiceover says so and the slides must not name any published framework.
- The Nairobi start-up (Kamau Njoroge, Wairimu Kariuki) and the Singapore bank team (Tan Wei Ling) are hypothetical. Stock footage must not show a real bank name or logo.
