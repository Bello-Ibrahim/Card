# L06 Logistic Regression for Yes/No Questions

Course: AI-12 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Will this customer subscribe? Yes or no. But a bank calling thousands of people wants more than yes or no. It wants to know *how likely* each person is to say yes, so it can call the most promising customers first. Logistic regression gives you that number.

## Explanation
Despite its name, **logistic regression** is a classification model. It works in two stages:

1. It combines the features into one score: each feature is multiplied by a weight, called a **coefficient**, and the results are added up with a starting value, the intercept.
2. It squeezes that score into a **probability** between 0 and 1.

`predict_proba(X)` returns these probabilities, one column per class. For a yes/no problem, column 1 is the probability of "yes". `predict(X)` applies a **threshold** of 0.5: a probability of 0.5 or more becomes 1, and anything lower becomes 0. The threshold is a business choice, not a law of nature, and in L09 you will move it.

Coefficients give a first look inside the model:

- A **positive** coefficient pushes the probability of "yes" up as the feature increases.
- A **negative** coefficient pushes it down.
- The size shows the strength of the push, but only if features are on comparable scales. That is why we scale numeric features first. For one-hot columns, the coefficient compares that category with the others.

Two cautions. Coefficients describe what the model learned from this data; they do not prove cause and effect. And when features are strongly related to each other, the model can share the weight between them in unstable ways. You will look at better interpretation tools in L15.

`LogisticRegression` uses regularisation by default, which keeps coefficients small to reduce overfitting. `max_iter=1000` gives the solver enough steps to finish on most data.

**Analogy:** Logistic regression is like a panel of judges giving points. Each feature is a judge who adds or removes points, and some judges have a stronger voice than others. The total is turned into a percentage, and the bank decides how high the percentage must be before it picks up the phone.

## Worked Example
Priya Nair is a marketing analyst at a hypothetical bank in Kochi, India. She wants to know which customer groups respond to term-deposit calls. She continues in the course notebook, where the setup cell and `pipe` from L05 have already run.

On screen, the presenter runs:

```python
import pandas as pd

names = pipe.named_steps["prep"].get_feature_names_out()
coefs = pd.Series(pipe.named_steps["model"].coef_[0], index=names)
print(coefs.sort_values().round(2))

print(pipe.predict_proba(X_test.head(3))[:, 1].round(2))
print(pipe.predict(X_test.head(3)))
```

Output (scikit-learn 1.9.1, pandas 3.0.6): [VERSION]

```
num__calls               -0.69
cat__contact_telephone   -0.36
cat__job_technician      -0.34
cat__job_admin           -0.24
cat__job_services        -0.24
cat__contact_cellular     0.36
num__balance              0.42
num__age                  0.58
cat__job_retired          0.82
dtype: float64
[0.03 0.02 0.17]
[0 0 0]
```

The presenter reads the results in plain words:

- **Largest positive:** being retired (0.82), older age (0.58) and a higher balance (0.42) raise the probability of subscribing.
- **Largest negative:** more calls in this campaign (−0.69), telephone contact (−0.36) and technician jobs (−0.34) lower it.
- The first three test customers have probabilities of 3%, 2% and 17%. All are below 0.5, so all are predicted "no".

Priya notes that in this data the prefix `num__` or `cat__` comes from the ColumnTransformer step names. She also notes that "more calls lowers the probability" could mean that repeated calls annoy people, or simply that the bank keeps calling people who were never interested. The model cannot tell which.

## Common Mistake
Many learners compare coefficients of unscaled features and conclude that "balance matters most" because its coefficient looks large or small only due to its units. Without scaling, a coefficient per one unit of income cannot be compared with a coefficient per one year of age. Always read coefficients from a pipeline that scales numeric features, and describe them as associations, not causes.

## Key Takeaways
1. Logistic regression is a classifier that outputs a probability; `predict` turns it into yes or no with a 0.5 threshold by default.
2. Positive coefficients push the probability of "yes" up and negative ones push it down; compare sizes only after scaling.
3. Coefficients show what the model learned from this data, not what causes the outcome.

## Hands-on Exercise
**Task:** Train logistic regression on the Bank Marketing data and list the 3 features with the largest positive and negative coefficients.
**Tools:** Google Colab (free), scikit-learn, pandas; your L05 pipeline and data.
**Steps:**
1. Open your L05 notebook and run all cells so that `pipe` is fitted.
2. Get the feature names with `pipe.named_steps["prep"].get_feature_names_out()`.
3. Build a pandas Series of `coef_[0]` indexed by those names and sort it.
4. Write down the 3 largest positive and the 3 largest negative coefficients.
5. Print `predict_proba` for 5 test customers next to `predict`, and check that the 0.5 rule explains the predictions.
6. Write one plain-language sentence for each of your 6 features, using "is linked with" rather than "causes".
**What good looks like:** A sorted table of coefficients, 6 clear sentences, and one note on a feature whose effect could have more than one explanation.
**Time:** about 25 minutes

## Review Flags
- [VERSION] `get_feature_names_out`, `named_steps` and `LogisticRegression` defaults (regularisation, solver) depend on the installed version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11 on the synthetic stand-in data; real Bank Marketing results will differ.
