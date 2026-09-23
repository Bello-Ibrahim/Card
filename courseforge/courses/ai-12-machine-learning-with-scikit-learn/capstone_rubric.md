# Capstone Rubric: End-to-End Predictive Model with a Stakeholder Report

## Task
Build and evaluate an end-to-end predictive model on a real business problem. Choose a public business dataset from UCI or Kaggle, frame the problem, build and tune a scikit-learn pipeline, evaluate it honestly on held-out data, check performance for subgroups, and explain the results in a one-page report for non-technical readers. You build the model in L17 (capstone step 1) and write the report in L18 (capstone step 2). Use public data only. Do not use personal or confidential data from your employer, and do not paste such data into Colab or any AI tool.

## Deliverables
- A Colab notebook (shared link or .ipynb file) that runs from top to bottom without errors, with the problem framing, dataset source and licence in text cells.
- A results table with a Dummy baseline, at least 3 candidate models, and the tuned model, each with cross-validated mean and standard deviation.
- One final test-set score for the chosen pipeline, and, for classification, the chosen threshold with its cost reasoning.
- A subgroup check for at least 3 groups, with group sizes, and a short risk note.
- The saved pipeline (.joblib) with the scikit-learn version recorded.
- A one-page stakeholder report with a 3-sentence executive summary.

## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| Problem framing and pipeline | O3, O7 | Precise target and business question; every feature known at prediction time; leakage checked; one pipeline with imputation, scaling and encoding fitted on training data only; notebook runs cleanly. | Clear framing and a working pipeline, with minor gaps in the leakage check. | Framing is vague, or some preprocessing is done outside the pipeline. | No clear target, or the notebook does not run. | 20 |
| Honest evaluation | O4 | Dummy baseline, 3+ models compared with suitable metrics and stratified cross-validation (mean and spread); confusion matrix or error plot interpreted; test set used once. | Baseline and models compared with suitable metrics and cross-validation; test set used once. | Only one metric or one split; baseline missing; spread not reported. | Only training scores, or the test set was used for tuning. | 25 |
| Improvement and justified choices | O5 | At least 2 engineered features tested and kept or dropped with evidence; randomized or grid search on the pipeline; threshold chosen from costs; trade-offs explained. | Features and tuning attempted with cross-validation, with a short justification. | Tuning or feature work done without evidence of improvement. | No attempt to improve the first model. | 20 |
| Subgroups, limits and risk | O6 | Recall or another key metric for 3+ subgroups with group sizes; small groups marked; risk note with a mitigation for each risk; importance described as association, not cause. | Subgroup table and risk note with mostly specific mitigations. | Subgroups checked with accuracy only, or risks listed without mitigations. | No subgroup check or risk discussion. | 20 |
| Stakeholder report | O6, O7 | One page with no unexplained jargon; performance stated as counts with a baseline comparison; honest limits; clear, testable recommendation; strong 3-sentence summary. | Clear report with business numbers and a recommendation; minor jargon. | Report relies on technical metrics or omits limits. | Report missing or not understandable to a non-technical reader. | 15 |

Total: 100

## Submission Checklist
- My dataset is public, and I recorded its source and licence.
- My notebook runs from top to bottom without errors in a fresh Colab session.
- Every feature is known at the moment of prediction, and I explained any columns I removed.
- All preprocessing is inside one pipeline, fitted on training data only.
- My results table includes a Dummy baseline and cross-validated mean and standard deviation for each model.
- I used the test set only once, after all tuning and threshold choices.
- I checked at least 3 subgroups, with group sizes, and wrote a risk note with mitigations.
- I saved the whole pipeline with joblib and recorded the scikit-learn version. I did not load any model file from an untrusted source.
- My report fits on one page, starts with a 3-sentence summary, and states performance in business terms.
- I did not paste personal or confidential data into any AI tool.
