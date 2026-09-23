# L04 Experiment Tracking with MLflow

Course: AI-18 · Module: M1 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Last week you tried twelve model settings. Which one gave the best score, with which data, and where is that model file now? If the answer is in a spreadsheet you updated by hand, or only in your memory, you need experiment tracking.

## Explanation
**Experiment tracking** records every training run automatically: its **parameters** (settings such as `C`), its **metrics** (such as F1) and its **artefacts** (files such as the trained model). You can then compare runs side by side and reload any model later.

MLflow is a free, open-source tool for this. Its tracking part has three ideas:

- An **experiment** groups related runs, such as "wine-quality".
- A **run** is one execution of your training code.
- The **tracking store** is where runs are saved. For this course, a local SQLite file (`mlflow.db`) is enough. Teams usually run a shared tracking server.

You add a few lines to your training code:

```python
import mlflow
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("wine-quality")

for C in [0.01, 0.1, 1.0]:
    with mlflow.start_run(run_name=f"logreg-C-{C}"):
        model = make_pipeline(StandardScaler(), LogisticRegression(C=C, max_iter=1000))
        model.fit(X_tr, y_tr)
        mlflow.log_param("C", C)
        mlflow.log_metric("f1", f1_score(y_te, model.predict(X_te)))
        mlflow.sklearn.log_model(model, name="model", input_example=X_te.head(2))
```

The imports and data split are the same as in `train.py` from L03. The `input_example` lets MLflow record the expected input columns. In MLflow 3.x the model is named with `name=`; older releases used `artifact_path=`. [VERSION] In the release we tested (3.16.1), scikit-learn models are saved in the "skops" format by default, and tree-based models such as random forests need extra trusted-type settings to save. Our logistic regression pipeline saves without extra settings. Check the documentation for your version. [VERSION]

**Analogy:** Experiment tracking is like a laboratory notebook that writes itself. Every experiment gets a page with the date, the exact settings, the results and a sample kept in the fridge, so you can repeat or check it later.

## Worked Example
Beatriz Carvalho works for a hypothetical wine cooperative in Portugal. She wants to predict which red wines tasters will rate as "good". She uses the public Wine Quality dataset, which contains physicochemical measurements and quality scores for Portuguese "vinho verde" wines. It is available from the UCI Machine Learning Repository. [VERIFY] Check the current licence and download address before you use it in a course or product. [VERIFY]

In the recorded demo we use the offline synthetic fallback from L03, so learners can follow without a download. The presenter follows these steps:

1. Open a terminal in the `wine-api` folder and run `pip install mlflow`. [VERSION]
2. Create `track.py` with the code above and run `python track.py`.
3. Start the interface: `mlflow ui --backend-store-uri sqlite:///mlflow.db`. Open the address it prints, usually `http://127.0.0.1:5000`. [VERSION]
4. Click the **wine-quality** experiment. Show the three runs in the table. [VERSION]
5. Select all three runs and click **Compare**. Show the parameter `C` and the metric `f1` side by side. [VERSION]
6. Open the best run and show the **Artifacts** tab with the saved `model` folder. [VERSION]

On the synthetic data the three runs gave these real results:

| Run | C | F1 |
|---|---|---|
| logreg-C-1.0 | 1.0 | 0.557 |
| logreg-C-0.1 | 0.1 | 0.538 |
| logreg-C-0.01 | 0.01 | 0.461 |

Beatriz would choose `C = 1.0`. The strongest regularisation (`C = 0.01`) clearly underfits. Her scores on the real dataset will be different.

## Common Mistake
Many learners log only the final, best run. Tracking is most useful when it also records the runs that failed or scored poorly, because they show what you already tried and why you rejected it. Log every run, give runs clear names, and do not delete runs because they look bad. Also, never log secrets or personal data as parameters or artefacts: anyone who can open the tracking server can read them.

## Key Takeaways
1. Experiment tracking records the parameters, metrics and artefacts of every training run.
2. In MLflow, experiments group runs; the interface lets you compare runs and open their saved models.
3. Log every run, including poor ones, and choose a model based on a metric that fits your problem.

## Hands-on Exercise
**Task:** Log at least 3 training runs with different settings to MLflow, compare them in the interface, and write down which run you would choose and why.
**Tools:** MLflow (free, open source), scikit-learn, your `wine-api` project from L03.
**Steps:**
1. Install MLflow in your virtual environment and add it to `requirements.txt`.
2. Add tracking code to your training script, with a loop or a configuration value for at least 3 settings.
3. Run the script and start `mlflow ui` with the same tracking store.
4. Compare the runs in the interface and take a screenshot of the comparison.
5. Open the best run's artefacts and confirm that the model was saved.
6. Write three to five sentences: which run you choose, which metric you used, and why that metric fits the task.
**What good looks like:** At least 3 named runs with parameters, an F1 (or similar) metric and a saved model each. The written choice names the metric and explains the trade-off, for example "C = 0.01 underfits; the difference between 0.1 and 1.0 is small, so I would check it on more data".
**Time:** about 35 minutes

## Review Flags
- [VERIFY] Wine Quality dataset: confirm the licence and current location on the UCI Machine Learning Repository, and the description of its origin (Portuguese vinho verde).
- [VERSION] MLflow interface labels (experiment list, Compare, Artifacts tab), the `mlflow ui` command and default port, the `name=` versus `artifact_path=` argument, and the skops default serialisation were checked against MLflow 3.16.1 only.
- F1 values come from a real run on the synthetic fallback data, not the real dataset.
