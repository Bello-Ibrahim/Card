# L14 Automating Retraining and Promotion

Course: AI-18 · Module: M3 · Objectives: O3, O6 · Video: 5 min (screen demo)

## Hook
Every month someone retrains the model by hand, looks at one number and decides to deploy it. What if the new model is worse on the cases that matter, and the person is on holiday? Automation can do the routine work, but a person should still own the final decision.

## Explanation
A retraining pipeline has three steps:

1. **Retrain** on the latest data and register the result as a new version with the alias `challenger`.
2. **Compare** the challenger with the current **champion** on the **same fixed test set**, with the same metric. The challenger must win by a clear margin, not by noise.
3. **Promote** only if the challenger wins, and only after a person approves. Promotion moves the `champion` alias to the new version and keeps the old one as `previous` for rollback.

The comparison script, `compare.py`, reads the tracking server address from the `MLFLOW_TRACKING_URI` environment variable:

```python
import sys, mlflow
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from data import load_data

NAME = "wine-quality-clf"
X, y = load_data()
_, X_te, _, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

def score(alias):
    model = mlflow.sklearn.load_model(f"models:/{NAME}@{alias}")
    return f1_score(y_te, model.predict(X_te))

champ, chall = score("champion"), score("challenger")
print(f"champion F1={champ:.4f}  challenger F1={chall:.4f}")
sys.exit(0 if chall > champ + 0.01 else 1)     # must win by a clear margin
```

`promote.py` moves the aliases:

```python
from mlflow import MlflowClient
NAME, client = "wine-quality-clf", MlflowClient()
old = client.get_model_version_by_alias(NAME, "champion").version
new = client.get_model_version_by_alias(NAME, "challenger").version
client.set_registered_model_alias(NAME, "previous", old)
client.set_registered_model_alias(NAME, "champion", new)
```

In GitHub Actions, a `schedule` trigger runs the workflow on a cron timetable (in UTC), and `workflow_dispatch` adds a manual "Run workflow" button. The human approval uses an **environment** with required reviewers: the `promote` job waits until an approved person clicks **Approve**. [VERSION]

```yaml
on:
  schedule:
    - cron: "0 3 * * 1"      # Mondays 03:00 UTC
  workflow_dispatch:
jobs:
  retrain:
    runs-on: ubuntu-latest
    env:
      MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}
    outputs:
      promote: ${{ steps.compare.outputs.promote }}
    steps:
      # checkout, setup-python and pip install as in L12
      - run: python add_challenger.py
      - id: compare
        run: |
          if python compare.py; then echo "promote=true" >> "$GITHUB_OUTPUT"
          else echo "promote=false" >> "$GITHUB_OUTPUT"; fi
  promote:
    needs: retrain
    if: needs.retrain.outputs.promote == 'true'
    runs-on: ubuntu-latest
    environment: production
    env:
      MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}
    steps:
      # checkout, setup-python and pip install as in L12
      - run: python promote.py
```

`add_challenger.py` is your training script from L04, registering its model and setting the `challenger` alias.

**Analogy:** This is like a sports team choosing a goalkeeper. The challenger and the champion play the same training match. The challenger replaces the champion only after a clearly better performance, and the coach still signs the decision.

## Worked Example
Nimal Perera is an ML engineer at a hypothetical tea exporter in Kandy, Sri Lanka. He demonstrates the pipeline on screen:

1. Open **Settings**, then **Environments**, create `production` and add himself as a required reviewer. [VERSION]
2. Add `retrain.yml` (with the full checkout and install steps) and commit.
3. In **Actions**, choose the `retrain` workflow and click **Run workflow** to test it without waiting for Monday. [VERSION]
4. Open the `retrain` job log. The real output of our test was `champion F1=0.5568  challenger F1=0.5380`. The challenger lost.
5. Show that the `promote` job was skipped, and the registry still shows `champion` on the same version.
6. Change the challenger's training settings so that it wins, run again, and show the `promote` job waiting for review. Click **Review deployments**, then **Approve**. [VERSION]
7. Refresh the MLflow registry: `champion` now points to the new version, and `previous` points to the old one.

## Common Mistake
Many learners compare the challenger's score from its own training run with the champion's score from months ago. The two numbers come from different test data, so the comparison means nothing. Always score both models now, on the same fixed test set. If the business also cares about fairness across groups or specific error types, compare those too before approving.

## Key Takeaways
1. A retraining pipeline retrains, compares challenger and champion on the same test set, and promotes only on a clear win.
2. Promotion moves the `champion` alias and keeps the old version as `previous`, so rollback stays one step.
3. A scheduled workflow can do the routine work, but a person approves the final promotion through an environment review.

## Hands-on Exercise
**Task:** Build a scheduled workflow that retrains, compares challenger and champion, and updates the registry only when the challenger wins. Add a manual approval step before promotion.
**Tools:** GitHub Actions (schedules, environments) [VERSION], MLflow, your `wine-api` project.
**Steps:**
1. Write `add_challenger.py`, `compare.py` and `promote.py`, and test them locally.
2. Create a `production` environment with yourself as the required reviewer.
3. Add `retrain.yml` with `schedule` and `workflow_dispatch` triggers.
4. Run it manually once when the challenger loses, and once when it wins.
5. Approve the promotion and check the aliases in the registry.
6. Write two sentences on how you chose the winning margin.
**What good looks like:** One run where promotion is skipped and one where it waits for approval and then moves `champion`. The `previous` alias exists. No credentials appear in the workflow file.
**Time:** about 45 minutes

## Review Flags
- [VERSION] Scheduled workflows, `workflow_dispatch`, environments with required reviewers and their availability for private repositories depend on the GitHub plan; check the interface labels (Environments, Run workflow, Review deployments) before recording.
- [VERSION] MLflow aliases (not stages) are used for champion, challenger and previous; checked against MLflow 3.16.1.
- The YAML excerpt was checked for valid syntax with PyYAML as a complete file with full steps; it was not run on GitHub. The F1 values are real outputs on the synthetic fallback data.
