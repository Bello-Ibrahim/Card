# L03 Structuring an ML Project for Production

Course: AI-18 · Module: M1 · Objectives: O2, O4 · Video: 5 min (screen demo)

## Hook
If you deleted your laptop today, could a teammate rebuild your model tomorrow and get exactly the same score? If the honest answer is "probably not", this lesson is for you.

## Explanation
You already know scikit-learn and Git, so we focus only on what changes for production. A production project has five features that a notebook usually lacks:

1. **A training script** (`train.py`) that runs from start to finish with one command.
2. **A configuration file** (`config.yaml`) for settings such as the random seed, test size and model parameters. You change settings without editing code.
3. **Pinned dependencies** (`requirements.txt` with exact versions), so every machine installs the same libraries.
4. **Fixed random seeds** everywhere randomness appears: the data split, the model and any synthetic data.
5. **A clear folder layout under Git**, with generated files excluded.

A layout that works for the rest of this course:

```text
wine-api/
  data.py          # load_data(): real CSV or offline fallback
  train.py         # one command: python train.py
  config.yaml
  requirements.txt
  tests/
  .gitignore       # model.joblib, mlflow.db, data/*.csv
```

Git recap, in one line: commit code and configuration, not data files, model files or secrets. You will version data and models with hashes and a registry in L05.

Our running example predicts whether a red wine is "good" (quality 7 or higher) from four features: `alcohol`, `volatile_acidity`, `sulphates` and `citric_acid`. `load_data()` reads the Wine Quality CSV if it exists in `data/`, and otherwise builds a synthetic dataset with the same column names and a fixed seed, so the course also works offline. The synthetic data is for practice only. The model is a scikit-learn pipeline (scaler plus logistic regression), so preprocessing is saved inside the model file. This avoids the training-serving mismatch from L01.

**Analogy:** A notebook is like cooking from memory. A production project is like a printed recipe card with exact amounts, oven temperature and cooking time. Anyone with the card and the same ingredients gets the same dish.

## Worked Example
Aarav Mehta, an ML engineer at a hypothetical grocery chain in Pune, India, refactors the wine notebook on screen. The presenter follows these steps:

1. In a terminal, create the folder and start Git: `mkdir wine-api && cd wine-api && git init`.
2. Create a virtual environment and install packages: `python -m venv .venv`, activate it, then `pip install scikit-learn pandas pyyaml joblib`.
3. Create `config.yaml`:
```yaml
seed: 42
test_size: 0.2
model:
  C: 1.0
  max_iter: 1000
```
4. Create `train.py`:
```python
import json, yaml, joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from data import load_data

cfg = yaml.safe_load(open("config.yaml"))
X, y = load_data(seed=cfg["seed"])
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=cfg["test_size"], random_state=cfg["seed"], stratify=y)
model = make_pipeline(StandardScaler(), LogisticRegression(**cfg["model"]))
model.fit(X_tr, y_tr)
f1 = f1_score(y_te, model.predict(X_te))
joblib.dump(model, "model.joblib")
json.dump({"f1": round(f1, 4)}, open("metrics.json", "w"))
print(f"F1 = {f1:.4f}")
```
5. Pin the exact versions: `pip freeze > requirements.txt`. The file contains lines such as `scikit-learn==1.9.1` and `pandas==3.0.6`. Your versions may differ; pin the versions you tested with. [VERSION]
6. Run `python train.py` twice. On the synthetic fallback data, both runs print `F1 = 0.5568`. The score is modest because the synthetic data is deliberately noisy; the point here is that it is identical.
7. Add `model.joblib`, `metrics.json` and `data/*.csv` to `.gitignore`, then commit.

## Common Mistake
Many learners set `random_state` in the model but forget the data split, or the reverse. The score then changes a little on every run, and they cannot tell whether a change in the score came from their code or from randomness. Set the seed in one place, the configuration file, and pass it to every function that uses randomness.

## Key Takeaways
1. A production ML project has a training script, a configuration file, pinned dependencies, fixed seeds and a clear layout under Git.
2. Keep preprocessing inside the saved model pipeline so training and serving always use the same steps.
3. Test reproducibility directly: run training twice and confirm the results are identical.

## Hands-on Exercise
**Task:** Refactor a scikit-learn notebook into a `train.py` script with a configuration file and a pinned requirements file, then prove it is reproducible.
**Tools:** Python 3, scikit-learn, pandas, PyYAML and joblib (all free); Git; any code editor.
**Steps:**
1. Start from your own notebook or the L01 sample notebook.
2. Create the folder layout shown above and a `data.py` with a `load_data()` function. Download the Wine Quality CSV into `data/` if you can; otherwise use a synthetic fallback with a fixed seed.
3. Move every setting (seed, test size, model parameters) into `config.yaml`.
4. Write `train.py` so that it reads the configuration, trains, evaluates and saves the model and metrics.
5. Create a clean virtual environment, install the packages and run `pip freeze > requirements.txt`.
6. Run `python train.py` twice and compare the two `metrics.json` files.
7. Commit the code, configuration and requirements. Check that no data, model files or credentials are committed.
**What good looks like:** One command trains the model. Both runs produce identical metrics. `git status` shows no model or data files. A teammate could clone the repository, install `requirements.txt` and get the same score.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Library versions in the example `requirements.txt` (scikit-learn 1.9.1, pandas 3.0.6) were the versions used to test the code; check and update them before recording.
- [VERIFY] The Wine Quality dataset licence and download location are checked in L04; the synthetic fallback keeps this lesson independent of it.
- Judgement call carried from the curriculum: Git basics are a prerequisite, so the lesson gives a one-line recap only.
