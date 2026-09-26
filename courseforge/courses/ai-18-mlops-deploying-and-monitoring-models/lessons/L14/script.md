# L14 Automating Retraining and Promotion | Presenter Script

Course: AI-18 · Video: 5 min · Words: 680

## Hook
Every month, someone retrains the model by hand, looks at one number, and deploys it. What if the new model is worse, and that person is on holiday? Automation can do the routine work. A person should still own the decision.

## Explain
Last lesson, we published images automatically. Now we automate the model itself. A retraining pipeline has three steps. First, retrain on the latest data, and register the result as a new version with the alias challenger.

Second, compare the challenger with the current champion, on the same fixed test set, with the same metric. The challenger must win by a clear margin, not by noise. In our script, it must beat the champion's F1 score by more than zero point zero one.

Third, promote only if the challenger wins, and only after a person approves. Promotion moves the champion alias to the new version, and keeps the old one as previous. So rollback stays one simple step.

In GitHub Actions, a schedule trigger runs the workflow on a timetable, for example every Monday at three in the morning, UTC. A manual trigger adds a run button for testing. For the approval, the promote job uses an environment with required reviewers. It waits until an approved person clicks approve. The timetable uses UTC, so check the time in your own country.

Think of a sports team choosing a goalkeeper. The challenger and the champion play the same training match. The challenger replaces the champion only after a clearly better performance, and the coach still signs the decision.

## Demonstrate
Nimal Perera is an ML engineer at a hypothetical tea exporter in Kandy, Sri Lanka. He builds the pipeline for the wine model.

Before the workflow, he tests the three scripts locally. The first trains and registers a challenger, using the training script from lesson four. The second loads both models by alias, scores them on the fixed test set, and succeeds only on a clear win. The third moves the aliases.

First, he creates an environment called production in the repository settings, and adds himself as a required reviewer. Then he adds the retrain workflow, with the schedule, the manual trigger, and the two jobs.

He does not wait for Monday. In the Actions tab, he chooses the retrain workflow and clicks run workflow. In the job log, the comparison prints the champion F1 as zero point five five six eight, and the challenger F1 as zero point five three eight zero. The challenger lost.

So the promote job is skipped. In the MLflow registry, champion still points to the same version. Nothing changed, and nobody had to check.

Next, he changes the challenger's training settings so that it wins, and runs the workflow again. This time, the promote job stops and waits for review. Everything before this step ran on its own, but the final step needs a person. He clicks review deployments, then approve.

He refreshes the registry. Champion now points to the new version, and previous points to the old one. If the new model causes trouble, rollback is one alias change.

The common mistake is to compare the challenger's score from its own training run with the champion's score from months ago. Different test data makes the comparison meaningless. Score both models now, on the same fixed test set. If fairness across groups matters, compare that too.

## Recap
Let's recap. First, a retraining pipeline retrains, compares challenger and champion on the same test set, and promotes only on a clear win. Second, promotion moves the champion alias and keeps the old version as previous, so rollback stays one step. Third, a scheduled workflow can do the routine work, but a person approves the final promotion.

## CTA
In the exercise below this video, you will build this scheduled workflow, run it once when the challenger loses and once when it wins, approve the promotion, and check the aliases. Add two sentences on your winning margin. It takes about forty-five minutes.

That completes week three. Next week we watch our model in production, starting with Monitoring Model Services. See you there.

## Thumbnail
Headline: Challenger vs Champion
Image: Navy background, two model icons facing each other on a scoreboard, a small person icon holding an approve button, headline in teal Inter Bold.

## Production Notes
- [VERSION] Scheduled workflows, workflow_dispatch, environments with required reviewers and their availability for private repositories depend on the GitHub plan. Check the interface labels (Environments, Run workflow, Review deployments, Approve) before recording.
- [VERSION] MLflow aliases (not stages) are used for champion, challenger and previous; checked against MLflow 3.16.1.
- The YAML was checked for valid syntax with PyYAML but not run on GitHub; record the Actions runs, the skipped promote job and the approval from a real run. The workflow file and scripts are shown on screen and never read aloud.
- 'champion F1=0.5568  challenger F1=0.5380' is a real output on the synthetic fallback data. content.md gives no real scores for the winning run, so the voiceover states none; show whatever the recording prints.
- No secrets on screen: the workflow reads MLFLOW_TRACKING_URI from a repository secret. Blur the tracking server address in the MLflow UI if it is not local.
- Nimal Perera and the Kandy tea exporter are hypothetical.
