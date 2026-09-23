# L05 Model Registry and Data Versioning

Course: AI-18 · Module: M1 · Objectives: O2, O3 · Video: 5 min (screen demo)

## Hook
A customer complains about a prediction made three weeks ago. Which model version made it? What data trained that model, and which commit of your code? If you cannot answer in two minutes, you cannot debug, audit or roll back.

## Explanation
Experiment tracking (L04) records every run. A **model registry** records only the models you decided to keep, and gives each one a clear name, version number and status.

In MLflow, a **registered model** has a name, such as `wine-quality-clf`. Each time you register a run's model under that name, MLflow creates a new **version**: 1, 2, 3 and so on. Versions never change after they are created.

To mark which version is in use, current MLflow releases use **aliases**: movable names that point to one version, such as `champion` for the production model and `challenger` for a candidate. Serving code loads `models:/wine-quality-clf@champion`. To promote or roll back, you move the alias; no code changes. Older MLflow releases used fixed **stages** ("Staging", "Production", "Archived") instead. Newer releases mark stages as deprecated and recommend aliases. [VERSION] This course uses aliases. If your team's server is older, check which method it supports. [VERSION]

A model version is only reproducible if you also know its inputs. Record two things as **tags** on every version:

- A **data hash:** a short fingerprint of the exact training data. If one value changes, the hash changes.
- A **Git commit ID:** the exact code that trained the model.

Tools such as DVC can version large data files, but a hash tag is enough to start and needs no extra tool.

```python
import hashlib, subprocess
import mlflow, pandas as pd
from mlflow import MlflowClient
from data import load_data

NAME = "wine-quality-clf"
mlflow.set_tracking_uri("sqlite:///mlflow.db")
client = MlflowClient()

X, y = load_data()
data_hash = hashlib.sha256(pd.util.hash_pandas_object(X.assign(y=y)).values).hexdigest()[:12]
commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()

best = mlflow.search_runs(experiment_names=["wine-quality"], order_by=["metrics.f1 DESC"]).iloc[0]
mv = mlflow.register_model(f"runs:/{best.run_id}/model", NAME)
client.set_model_version_tag(NAME, mv.version, "data_sha256", data_hash)
client.set_model_version_tag(NAME, mv.version, "git_commit", commit)
client.set_registered_model_alias(NAME, "champion", mv.version)
```

**Analogy:** A model registry is like a library catalogue. Each book edition has a fixed number, and the catalogue records the publisher and printing. A "recommended edition" label can move from one edition to another without anyone reprinting the books.

## Worked Example
Yusuf Demir is an ML engineer at a hypothetical logistics company in Izmir, Türkiye. He has the wine model from L04 and demonstrates the registry on screen:

1. Commit the current code with Git, so the commit ID is meaningful.
2. Run `python register.py` (the code above). The terminal prints "Created version '1' of model 'wine-quality-clf'". [VERSION]
3. Open the MLflow interface and click **Models**. Show `wine-quality-clf` with version 1. [VERSION]
4. Open version 1. Show the `champion` alias and the tags `data_sha256` and `git_commit`. [VERSION]
5. Change `C` in the configuration, train and register again. Version 2 appears, and the alias still points to version 1.
6. In Python, move the alias: `client.set_registered_model_alias(NAME, "champion", 2)`. Refresh the interface: `champion` now points to version 2.
7. Move it back to version 1. This is a rollback, and it took one line.

When Yusuf ran the registration twice on the same data and commit, both versions had the same data hash, `bfc250d53981`, and the same commit. This proves that the tags describe the inputs, not the time of the run.

## Common Mistake
Many learners use the registry as a folder of files and name versions "final", "final2" or "new_best". The version number already identifies the model. What people need is the **status** and the **origin**. Use aliases for status (`champion`, `challenger`) and tags for origin (data hash, commit, training metric). Also, do not store credentials or personal data in tags or descriptions.

## Key Takeaways
1. A model registry stores chosen models as numbered, unchangeable versions under one name.
2. Aliases such as `champion` mark which version is in use; moving an alias promotes or rolls back without code changes.
3. Tag every version with a data hash and a Git commit ID so it can be rebuilt and explained.

## Hands-on Exercise
**Task:** Register your best model, add a second version, mark one as the production version, and record the data hash and Git commit for each.
**Tools:** MLflow (free), Git, your `wine-api` project.
**Steps:**
1. Commit your current code.
2. Write `register.py` to register the best run from L04 and add `data_sha256` and `git_commit` tags.
3. Set the `champion` alias on version 1.
4. Change one setting, retrain, commit and register version 2 with its own tags.
5. Decide which version should be `champion` and set the alias. Write one sentence explaining your choice.
6. Load the model with `mlflow.pyfunc.load_model("models:/wine-quality-clf@champion")` and make one prediction to prove it works.
7. Screenshot the registry page showing both versions, the alias and the tags.
**What good looks like:** Two versions, each with a data hash and a commit ID. Exactly one version carries `champion`. You can explain how to roll back in one command.
**Time:** about 35 minutes

## Review Flags
- [VERSION] MLflow stages versus aliases: confirm that the current release still marks stages as deprecated and recommends aliases, and check the interface labels (Models page, alias and tag display). Tested with MLflow 3.16.1.
- [VERSION] Printed registration messages may differ between MLflow releases.
- The data hash shown is a real output from the synthetic fallback data.
