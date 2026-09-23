# L01 Why Models Fail After the Notebook

Course: AI-18 · Module: M1 · Objectives: O1, O2 · Video: 5 min

## Hook
Your model scored well in the notebook last month. Today a colleague tries to run the same notebook on a new laptop and gets a different score, then an error. Nothing about the model changed. So what broke? This lesson is about the gap between "it works on my machine" and "it works every day for real users".

## Explanation
A notebook is an excellent place to explore. It is a poor place to run a production system. Most production failures of machine learning (ML) models are not caused by the algorithm. They come from everything around it.

Four groups of problems appear again and again:

1. **Missing or changing dependencies.** The notebook imports libraries without fixed versions. A new release changes a default value or removes a function, and the result changes or the code fails.
2. **Different data.** Training used a CSV file on one person's laptop. In production the data arrives from a live system, with new categories, missing values or different units.
3. **Silent errors.** A cell was run out of order, a random seed was never set, or a preprocessing step exists only in the notebook and not in the serving code. The model returns an answer, but it is the wrong answer, and nothing raises an error.
4. **Nobody watching.** After deployment, no one checks latency, errors or the quality of predictions. The model slowly becomes less accurate as the world changes. This is called **drift**, and you will measure it in L16.

**MLOps** (machine learning operations) is the set of practices that closes this gap. In this course you will use these key terms:

- **Artefact:** any file produced by the pipeline, such as a trained model, a metrics file or a Docker image.
- **Model registry:** a central store that keeps each model version, its metadata and which version is in production.
- **CI/CD:** continuous integration and continuous delivery. Every change is tested and built automatically.
- **Serving:** making a model available to other systems, for example through an API.
- **Drift:** production data or predictions that no longer look like the training data.
- **Rollback:** returning quickly to the previous working version when a new one causes problems.

The central idea is **reproducibility**. If you version the code, the data and the model together, anyone can rebuild the same model and explain where each prediction came from.

**Analogy:** A recipe that works in your home kitchen is not ready for a food factory. The factory needs written steps, exact measures, the same ingredients from a known supplier, and quality checks on every batch. A notebook is the home recipe. An MLOps project is the factory version: written down, measured, checked and repeatable.

## Worked Example
Valentina Rojas is a data scientist at a hypothetical car insurance company in Chile. She trained a claim-fraud classifier in a notebook, and it looked good. Her team deployed it by copying the notebook's code into a web service.

Three weeks later, the operations team asked why the model flagged almost no claims. Valentina investigated and found four separate causes:

- The notebook scaled the "claim amount" feature before training, but the service code sent raw amounts to the model.
- The server installed a newer version of a library, and one default setting had changed.
- A new claim type had appeared in the live data, and the model had never seen it.
- No one had looked at the share of flagged claims since launch, so the problem ran for weeks before anyone noticed.

None of these problems was about choosing a better algorithm. Each one had a process fix: keep preprocessing inside the saved model pipeline, pin library versions, check live inputs against the training data, and monitor the prediction rate.

## Common Mistake
Many teams believe that a high test score means the model is ready. A test score only tells you how the model performed on one fixed dataset, on one machine, on one day. It says nothing about whether another person can rebuild the model, whether the serving code matches the training code, or whether anyone will notice when performance falls. Treat the test score as one entry requirement for production, not the finish line.

## Key Takeaways
1. Most production ML failures come from dependencies, data differences, silent errors and missing monitoring, not from the algorithm.
2. Key MLOps terms: artefact, model registry, CI/CD, serving, drift and rollback.
3. Versioning code, data and model together makes results reproducible and explainable.

## Hands-on Exercise
**Task:** Review a sample notebook and list at least 6 problems that would stop it from running reliably in production.
**Tools:** A text editor or notes app. Optional: Jupyter (free) to open the notebook.
**Steps:**
1. Read this notebook code, which a hypothetical teammate shared:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv("C:/Users/sam/Desktop/wine_final_v3.csv")
df = df.dropna()
X = df.drop(columns=["quality"]); y = df["quality"] >= 7
X_tr, X_te, y_tr, y_te = train_test_split(X, y)
model = RandomForestClassifier().fit(X_tr, y_tr)
print(model.score(X_te, y_te))
import pickle; pickle.dump(model, open("model.pkl", "wb"))
```
2. List every problem you can find. Think about paths, versions, seeds, data, metrics and what happens after the model is saved.
3. For each problem, write one sentence on how it could fail in production and one possible fix.
4. Group your problems under the four headings from this lesson.
**What good looks like:** At least 6 problems with fixes, for example: hard-coded personal path; no pinned library versions; no random seed in the split or the model; rows silently dropped with no record of how many; accuracy only, with no metric suited to an imbalanced label; no record of which data file produced the model; a pickle file with no version information; no plan to monitor the model after deployment.
**Time:** about 20 minutes

## Review Flags
- None. The worked example is hypothetical and the lesson makes no claims about specific tools, versions or statistics.
