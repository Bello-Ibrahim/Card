# Screen Demo Pack: AI-18 L14 Automating Retraining and Promotion

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L14_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Open add_challenger.py and highlight the challenger alias being set
2. Open compare.py and highlight score('champion'), score('challenger') and the exit rule chall > champ + 0.01
3. Open promote.py and highlight the two set_registered_model_alias lines
4. Run the three scripts locally against the tracking server

**Narration over this clip (for pacing)**

> Before the workflow, he tests the three scripts locally. The first trains and registers a challenger, using the training script from lesson four. The second loads both models by alias, scores them on the fixed test set, and succeeds only on a clear win. The third moves the aliases.

## Clip 2: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L14_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open Settings, then Environments
2. Create the environment production
3. Add himself as a required reviewer and save
4. Open .github/workflows/retrain.yml and highlight the schedule, workflow_dispatch, the retrain job and the promote job with environment: production
5. Commit the workflow

**Narration over this clip (for pacing)**

> First, he creates an environment called production in the repository settings, and adds himself as a required reviewer. Then he adds the retrain workflow, with the schedule, the manual trigger, and the two jobs.

## Clip 3: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L14_screen_3.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Open the Actions tab and choose the retrain workflow
2. Click Run workflow
3. Open the retrain job log
4. Highlight 'champion F1=0.5568  challenger F1=0.5380'

**Narration over this clip (for pacing)**

> He does not wait for Monday. In the Actions tab, he chooses the retrain workflow and clicks run workflow. In the job log, the comparison prints the champion F1 as zero point five five six eight, and the challenger F1 as zero point five three eight zero. The challenger lost.

## Clip 4: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L14_screen_4.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Show the promote job marked as skipped in the run summary
2. Open the MLflow UI, Models, wine-quality-clf
3. Show the champion alias on the same version as before

**Narration over this clip (for pacing)**

> So the promote job is skipped. In the MLflow registry, champion still points to the same version. Nothing changed, and nobody had to check.

## Clip 5: scene 12

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L14_screen_5.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Change the training settings in add_challenger.py and commit
2. Click Run workflow again
3. Show the promote job waiting for review
4. Click Review deployments, select production, click Approve

**Narration over this clip (for pacing)**

> Next, he changes the challenger's training settings so that it wins, and runs the workflow again. This time, the promote job stops and waits for review. Everything before this step ran on its own, but the final step needs a person. He clicks review deployments, then approve.

## Clip 6: scene 13

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L14_screen_6.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Refresh the MLflow registry page
2. Show champion on the new version
3. Show previous on the old version

**Narration over this clip (for pacing)**

> He refreshes the registry. Champion now points to the new version, and previous points to the old one. If the new model causes trouble, rollback is one alias change.

## Production notes for this lesson

- [VERSION] Scheduled workflows, workflow_dispatch, environments with required reviewers and their availability for private repositories depend on the GitHub plan. Check the interface labels (Environments, Run workflow, Review deployments, Approve) before recording.
- [VERSION] MLflow aliases (not stages) are used for champion, challenger and previous; checked against MLflow 3.16.1.
- The YAML was checked for valid syntax with PyYAML but not run on GitHub; record the Actions runs, the skipped promote job and the approval from a real run. The workflow file and scripts are shown on screen and never read aloud.
- 'champion F1=0.5568  challenger F1=0.5380' is a real output on the synthetic fallback data. content.md gives no real scores for the winning run, so the voiceover states none; show whatever the recording prints.
- No secrets on screen: the workflow reads MLFLOW_TRACKING_URI from a repository secret. Blur the tracking server address in the MLflow UI if it is not local.
- Nimal Perera and the Kandy tea exporter are hypothetical.
