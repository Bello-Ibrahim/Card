# L17 Capstone Step 1: Build an End-to-End Model

Course: AI-12 · Module: M4 · Objectives: O5, O7 · Video: 6 min (screen demo)

## Hook
You now have every piece: framing, pipelines, metrics, cross-validation, feature engineering, tuning and risk checks. In this lesson you put them together in the right order, on a dataset you choose, and finish with a tested model saved to a file.

## Explanation
Choose a **public business dataset** with a clear target and at least a few thousand rows. Good options include the UCI Bank Marketing or Online Shoppers Purchasing Intention data, a Kaggle telecom churn or hotel booking dataset, or the UCI Seoul Bike data for regression. [VERIFY] Every Kaggle dataset has its own licence, which you must read and cite. Downloading from Kaggle needs a free account, and the steps to connect Colab to Kaggle change over time. [VERSION] Do not use personal or confidential data from your employer, and do not paste such data into Colab or any AI tool.

Then follow this workflow in one notebook:

1. **Frame the problem** (L01): business question, target, features known at prediction time, task type, metric and the cost of each mistake.
2. **Split once** (L03): hold back a test set with `stratify` for classification and a fixed `random_state`. Do not look at it again until step 7.
3. **Baseline** (L08): a `DummyClassifier` or `DummyRegressor` inside the same pipeline. Every model must beat it.
4. **Pipeline** (L05): imputation, scaling and encoding in a ColumnTransformer, with a simple model first.
5. **Compare and improve** (L10 to L13): cross-validate 2 or 3 models and test new features.
6. **Tune** (L14): a randomized search on the best candidate, and, for classification, a threshold chosen from costs (L09).
7. **Final test**: score the chosen pipeline once on the test set.
8. **Save** the fitted pipeline with `joblib`, and record the library versions.

A saved model file only loads reliably with compatible versions of scikit-learn and its dependencies, so write the versions next to the file. [VERSION] **Never load a joblib or pickle file from an untrusted source.** Loading such a file can run any code hidden inside it. Only load files that you or your team created and stored safely.

**Analogy:** An end-to-end project is like following a recipe from shopping to serving. Each step depends on the previous one, and you taste the dish at the end only once, when the guests arrive. If you keep tasting and changing the dish in front of the guests, their opinion is no longer independent.

## Worked Example
Elena Popescu is a junior data scientist at a hypothetical bank in Cluj-Napoca, Romania. She has framed her problem (which customers to call for a term deposit), split the data and built the L05 pipeline. The presenter shows the last part of her notebook:

```python
import joblib, sklearn
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score

baseline = Pipeline([("prep", prep), ("model", DummyClassifier(strategy="prior"))])
print("baseline CV AUC:", cross_val_score(baseline, X_train, y_train, cv=5,
                                          scoring="roc_auc").mean().round(3))
print("model CV AUC:", cross_val_score(pipe, X_train, y_train, cv=5,
                                       scoring="roc_auc").mean().round(3))

final = pipe.fit(X_train, y_train)          # after all tuning is finished
print("test AUC:", round(roc_auc_score(y_test, final.predict_proba(X_test)[:, 1]), 3))

joblib.dump(final, "term_deposit_model.joblib")
print("saved with scikit-learn", sklearn.__version__)
loaded = joblib.load("term_deposit_model.joblib")   # only files you created yourself
print(loaded.predict(X_test.head(3)))
```

Output (scikit-learn 1.9.1, joblib 1.6.0): [VERSION]

```
baseline CV AUC: 0.5
model CV AUC: 0.778
test AUC: 0.752
saved with scikit-learn 1.9.1
[0 0 0]
```

The presenter walks through it step by step:

1. The baseline scores 0.5, which is random ranking. The model scores 0.778 in cross-validation, so it clearly learns something.
2. The single test score, 0.752, is a little lower than the cross-validation mean. That is normal, and it is within the fold spread seen in L10. Elena reports the test score as her final number.
3. The whole pipeline, including preprocessing, is saved to one file. Loading it and predicting on 3 rows confirms that the file works.
4. In Colab, the presenter opens the Files panel and downloads the `.joblib` file, because Colab storage is temporary. [VERSION]

Elena adds a text cell with the scikit-learn version, the chosen threshold of 0.15 from L09, and the date.

## Common Mistake
Learners often save only the model step, `pipe.named_steps["model"]`, without the preprocessing. When the file is loaded later, raw data cannot be passed to it, and people rebuild the preprocessing by hand, often with small differences. Save the whole fitted pipeline. A second mistake is changing the model after seeing the test score and then reporting the new test score as if it were independent.

## Key Takeaways
1. Follow one order: frame, split once, baseline, pipeline, compare, tune, test once, save.
2. Every model must beat a Dummy baseline, and the test set is scored once at the very end.
3. Save the whole fitted pipeline with joblib, record the library versions, and never load model files from untrusted sources.

## Hands-on Exercise
**Task:** Capstone step 1: complete the modelling notebook, from problem framing to a tuned, tested and saved model.
**Tools:** Google Colab (free), scikit-learn, pandas, joblib; a public dataset from UCI or Kaggle (free account needed for Kaggle). [VERIFY]
**Steps:**
1. Choose your dataset, record its source and licence, and write the problem framing in a text cell.
2. Load and inspect the data; remove features that are not known at prediction time.
3. Split once, with a fixed `random_state`, and put the test set aside.
4. Build a Dummy baseline and a first pipeline, and cross-validate both.
5. Compare at least 2 more models and test at least 2 new features with cross-validation.
6. Tune the best model with `RandomizedSearchCV`; for classification, choose a threshold from costs.
7. Score the final pipeline once on the test set and check one subgroup (L16).
8. Save the pipeline with joblib, record the library versions, and download the file.
**What good looks like:** A notebook that runs from top to bottom, a results table (baseline, candidates, tuned model), one final test score, a subgroup check, and a saved model file with versions recorded.
**Time:** about 120 minutes, spread over the week

## Review Flags
- [VERIFY] Availability and licences of suggested datasets (UCI Bank Marketing, UCI Online Shoppers Purchasing Intention, UCI Seoul Bike Sharing Demand, Kaggle telecom churn and hotel booking datasets). Each Kaggle dataset has its own licence.
- [VERSION] Kaggle download steps in Colab (account, API token, commands) and the Colab Files panel may change.
- [VERSION] joblib model files depend on scikit-learn and dependency versions and must not be loaded from untrusted sources. Outputs were recorded with scikit-learn 1.9.1, joblib 1.6.0 and Python 3.11 on synthetic data.
