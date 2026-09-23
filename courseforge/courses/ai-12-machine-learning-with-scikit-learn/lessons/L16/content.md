# L16 Fairness, Limits and Model Risk

Course: AI-12 · Module: M4 · Objectives: O6 · Video: 6 min (screen demo)

## Hook
Your model finds 67% of subscribers overall. That sounds acceptable. But what if it finds 90% in one age group and 30% in another? An average can hide a group for which the model fails, and those people may be treated unfairly because of it.

## Explanation
A single overall score describes the average customer. Real decisions affect individual people and groups. Before a model is used, check three kinds of risk.

**1. Subgroup performance.** Split the test results by meaningful groups, such as region, age band, product or channel, and calculate the key metric for each group. Look for groups where the model is much worse. Also count how many positive cases each group has: a recall based on 5 people is very uncertain, and a larger sample is needed before you draw conclusions. Some attributes, such as gender or ethnicity, may be sensitive or legally protected in your country. Whether you may collect and use them, even for checking fairness, depends on local law and company policy. [REGION]

**2. Data risks.**
- **Class imbalance:** a rare positive class leads to low recall unless you adjust the threshold (L09) or use settings such as `class_weight="balanced"`.
- **Data that changes over time:** customer behaviour, prices and economic conditions change. A model trained on last year's data may slowly become less accurate. This is often called **drift**. Monitoring it is covered in AI-18.
- **Unrepresentative data:** if some groups are rare in training data, the model has less to learn from for them.

**3. Impact risk: what happens if the model is wrong?** For each type of mistake, ask who is affected and how badly. An unneeded marketing call is a small cost. A wrongly refused loan or a missed health check is serious. The higher the impact, the more human review and checking the model needs.

Write this down in a short **risk note**: each risk, the evidence, and one mitigation, such as a group-specific review, more data, a different threshold, or a human decision for borderline cases.

**Analogy:** A school's average exam result can look good while one class is failing badly. A careful head teacher looks at each class, not only the school average, and asks what happens to the students who fall behind. Subgroup checks are that class-by-class view.

## Worked Example
Nomvula Dlamini is a data analyst at a hypothetical bank in Durban, South Africa. Her team plans to use the term-deposit model with the 0.15 threshold chosen in L09. She checks recall by age band on the test set. This is a hypothetical case with synthetic data, used on purpose to avoid claims about real organisations.

On screen, the presenter continues from the L05 notebook and runs:

```python
import pandas as pd

threshold = 0.15                      # chosen in L09
results = pd.DataFrame({
    "age_band": pd.cut(X_test["age"], bins=[17, 30, 50, 80],
                       labels=["18-30", "31-50", "51-79"]),
    "actual": y_test,
    "pred": (pipe.predict_proba(X_test)[:, 1] >= threshold).astype(int),
})
buyers = results[results["actual"] == 1]
summary = buyers.groupby("age_band", observed=True).agg(
    positives=("actual", "size"), recall=("pred", "mean"))
print(summary.round(2))
```

Output (scikit-learn 1.9.1, pandas 3.0.6): [VERSION]

```
          positives  recall
age_band
18-30             5    0.60
31-50            15    0.53
51-79            40    0.72
```

Among real subscribers only, the mean of `pred` is the recall. The presenter reads it: the model finds 72% of subscribers aged 51 to 79, but only 53% of those aged 31 to 50. The youngest group has only 5 subscribers in the test set, so its 60% could easily change with a different sample.

Nomvula's risk note:

- **Lower recall for ages 31 to 50.** Mitigation: review whether a lower threshold for all customers, or better features, closes the gap; check again with cross-validated predictions.
- **Too few young subscribers to judge.** Mitigation: collect more data or combine several test periods before drawing conclusions.
- **Behaviour may change when interest rates change.** Mitigation: check recall by group every month and retrain when it falls below an agreed level.

## Common Mistake
Learners often check subgroups with accuracy. With a rare positive class, a group can have high accuracy simply because few of its members subscribe, while the model misses most of those who do. Use the metric that matches the business risk, usually recall or precision for the positive class, and always show the group sizes next to the scores.

## Key Takeaways
1. Overall scores can hide groups where the model fails; check the key metric for each meaningful subgroup, with group sizes.
2. Class imbalance, data that changes over time and unrepresentative data are common model risks.
3. Ask what happens when the model is wrong, and write a risk note with one mitigation for each risk.

## Hands-on Exercise
**Task:** Compare recall across 3 subgroups in your model and write a short risk note with one mitigation for each risk.
**Tools:** Google Colab (free), scikit-learn, pandas; your best pipeline and chosen threshold.
**Steps:**
1. Choose one grouping column that makes business sense, such as age band, region or contact channel. Create bands with `pd.cut` if needed.
2. Apply your chosen threshold to the test-set probabilities.
3. For each group, calculate the number of positive cases and the recall.
4. Mark any group with fewer than 20 positive cases as "too small to judge".
5. Write a risk note with at least 3 risks: one from your subgroup table, one about data that changes over time, and one about the cost of a wrong prediction.
6. Add one practical mitigation for each risk.
**What good looks like:** A small table with group sizes and recall, a clear statement about which group is weakest, and a risk note that a manager can act on. Do not paste real customer data into AI tools while writing the note.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11 on synthetic data. `pd.cut` and the `observed` argument of `groupby` should be checked against the Colab pandas version.
- [REGION] Rules on collecting and using sensitive or protected attributes (for example gender or ethnicity) for fairness checks differ by country and sector.
- The bank and subgroup failure are hypothetical on purpose (curriculum flag), to avoid unverified claims about real organisations.
