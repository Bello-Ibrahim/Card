# L07 Measuring and Reducing Bias

Course: AI-24 · Module: M2 · Objectives: O4, O5 · Video: 5 min (screen demo)

## Hook
Two analysts check the same credit model. One reports that it is unfair to Group B. The other reports that it protects Group B from bad loans. Both used correct numbers. How can that be?

## Explanation
The **approval-rate ratio** from L06 only looks at decisions, not whether they were right. Error rates by group add that view.

- **False rejection rate:** of the applicants who would have repaid, what share did the model decline? These are good customers wrongly turned away.
- **Bad-loan approval rate:** of the applicants who would not have repaid, what share did the model approve? These cause losses and can harm borrowers with debt they cannot manage.

Different measures can disagree. A model can have a lower approval rate and a higher false rejection rate for Group B, while also approving fewer bad loans for Group B. In general you cannot make all of them equal at once, so a team must **choose which measure matters most for the decision** and explain why.

One more caution: for declined applicants, we never see whether they would have repaid. In real data, false rejection rates are estimates. In our synthetic data, we know the answer, which makes it good for learning.

Some people use a threshold for the approval-rate ratio. The best known is the "four-fifths" (0.8) ratio. It comes from US employment practice, not credit law, and it should be treated only as a rough rule of thumb that a gap needs investigating [REGION] [VERIFY]. It is not a legal safe harbour for lending in any country this course covers.

The main options to reduce bias are:

1. **Remove or change proxies:** test the model without features that stand in for protected characteristics.
2. **Rebalance the data:** add or reweight examples so the model learns from enough cases in each group.
3. **Add human review:** send applications near the threshold, or in groups with high false rejection rates, to a trained credit officer.
4. **Monitor results:** measure the same fairness numbers every month, because they can change after launch.

**Analogy:** A single fairness measure is like judging a doctor only by how many patients they send home. A doctor who sends everyone home looks efficient but misses sick patients. You need to know how many decisions were right for each group of patients, not only how many were made.

## Worked Example
Alejandro Ruiz is a risk analyst at Crédito Solar, a hypothetical consumer lender in Mexico. He runs the course's ready-made Google Colab notebook on 1,300 synthetic loan decisions. The notebook contains this short code:

```python
import pandas as pd
counts = [("A",1,1,520),("A",1,0,80),("A",0,1,60),("A",0,0,140),
          ("B",1,1,265),("B",1,0,95),("B",0,1,15),("B",0,0,125)]
df = pd.DataFrame([r[:3] for r in counts for _ in range(r[3])],
                  columns=["group","repaid","approved"])
s = df.groupby("group").agg(applicants=("approved","size"),
                            approval_rate=("approved","mean"))
good, bad = df[df.repaid == 1], df[df.repaid == 0]
s["false_rejection_rate"] = 1 - good.groupby("group")["approved"].mean()
s["bad_loans_approved_rate"] = bad.groupby("group")["approved"].mean()
print(s.round(3))
print("Approval-rate ratio:", round(s.approval_rate.min() / s.approval_rate.max(), 3))
```

The output is:

```text
       applicants  approval_rate  false_rejection_rate  bad_loans_approved_rate
group
A             800          0.725                 0.133                    0.300
B             500          0.560                 0.264                    0.107
Approval-rate ratio: 0.772
```

Group B has a lower approval rate (56.0% against 72.5%) and a ratio of 0.772. Group B's good payers are declined about twice as often as Group A's (26.4% against 13.3%). But the model approves far fewer bad loans for Group B (10.7% against 30.0%). Alejandro reports the false rejection rate to his credit committee as the main measure, because it shows good customers being turned away, and recommends human review for Group B applications near the threshold.

## Common Mistake
Many teams report only the measure that makes their model look fair. Report at least two measures, explain the choice, and show the numbers that look bad too. A committee cannot manage a risk that it was not shown.

## Key Takeaways
1. Approval-rate ratios compare decisions; error rates by group, such as false rejection rates, show whether those decisions were right.
2. Fairness measures can disagree, so choose and justify the main measure for each decision, and treat the four-fifths ratio only as a rough rule of thumb.
3. Reduce bias by removing proxies, rebalancing data, adding human review and monitoring results, and test again after every change.

## Hands-on Exercise
**Task:** Run the ready-made Colab notebook, compare false rejection rates by group, and recommend a fairness measure.
**Tools:** Google Colab (free, needs a Google account) [VERSION]; the course's ready-made notebook. No coding is required.
**Steps:**
1. Open the notebook link from the course page.
2. Save your own copy with File > Save a copy in Drive [VERSION].
3. Choose Runtime > Run all [VERSION]. Wait until the output table appears under the code.
4. Check that your output matches the table in this lesson.
5. Find the approval-rate ratio, and the false rejection rate for each group.
6. Change the number 95 in the counts line to 45 and the number 265 to 315, then run again. Note what changes.
7. Write 3 sentences: which fairness measure you would report to a credit committee, why, and what action you would recommend.
**What good looks like:** The notebook runs without errors, you quote the correct numbers (after step 6, the ratio rises to 0.91 and Group B's false rejection rate falls to 12.5%), and your 3 sentences name one main measure, explain its link to customer harm, and propose one concrete action.
**Time:** about 30 minutes

## Review Flags
- [REGION] [VERIFY] The "four-fifths" ratio comes from US employment practice and is not a general credit rule; confirm it is presented only as a heuristic.
- [VERSION] Google Colab free-tier limits and menu names (Save a copy in Drive, Run all) must be checked before recording.
- Screen demo: the presenter follows the Exercise steps 1–6 on screen with the ready-made notebook. The code and output were run with Python on the synthetic data and match the lesson.
