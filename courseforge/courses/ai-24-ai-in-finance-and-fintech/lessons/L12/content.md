# L12 Model Risk Management and Monitoring

Course: AI-24 · Module: M3 · Objectives: O5 · Video: 5 min

## Hook
A fraud model passes every test at launch. Six months later, false alarms have doubled and a new type of fraud is getting through. Nobody changed the model. What changed, and whose job was it to notice?

## Explanation
**Model risk** is the risk of loss or harm because a model is wrong, is used wrongly, or stops working as intended. Model risk management gives every model a clear life cycle and clear owners. It has four main parts.

**1. Model inventory.** A list of every model in use, with its purpose, owner, data, validation date, risk rating and status. You cannot manage a model you do not know exists. This includes vendor models and AI assistants used in customer-facing work.

**2. Independent validation.** Before launch, and at regular intervals, people who did not build the model test it. They check the data, the method, the performance, the fairness results and the limits of use. They can require changes before approval.

**3. Performance and drift monitoring.** After launch, the owner measures the model regularly. Typical measures are:
- **Performance:** for fraud, the share of fraud caught and the false alarm rate; for credit, default rates by score band.
- **Data drift:** whether the input data has changed, such as new merchant types, a new customer segment or missing fields.
- **Score drift:** whether the distribution of scores has moved.
- **Fairness:** error rates by group (L07).
Each measure has limits. An amber limit triggers investigation; a red limit triggers action, which can include retraining, changing the threshold or pausing the model.

**4. The three lines of defence.** This is a common governance framework:
- **First line:** the business and model owners who build and use the model and monitor it every day.
- **Second line:** independent risk and compliance teams who set standards, validate models and challenge the first line.
- **Third line:** internal audit, which checks that the whole system works.

Some supervisors publish model risk guidance, for example the US supervisory guidance known as SR 11-7 [REGION] [VERIFY]. This course teaches the general framework, which you should match to your local supervisor's expectations.

A key question in every institution: **who has the authority to pause a model?** It must be written down before launch, with a fallback process, such as rules only or manual review, ready to use.

**Analogy:** Model monitoring is like a regular vehicle safety inspection. A car that was safe when it left the factory can develop worn brakes and weak tyres. You do not wait for an accident to check them. You inspect on a schedule, you have clear pass and fail limits, and an inspector can take an unsafe car off the road.

## Worked Example
Ifeoma Eze is head of model risk at the hypothetical Lagos card issuer from L03. She writes a monitoring plan for its fraud model. The limits below are illustrative, set by the issuer for this model.

| Measure | How often | Amber limit | Red limit | Who acts |
|---|---|---|---|---|
| Share of fraud caught (labels matured after 60 days) | Monthly | Below 80% | Below 70% | Fraud model owner (first line) |
| False alarm rate | Weekly | Above 3% | Above 5% | Fraud model owner |
| Score distribution compared with launch | Monthly | Moderate shift | Large shift | Model owner, reported to model risk |
| Missing values in key fields | Daily | Above 2% | Above 5% | Data engineering |
| False alarm rate by customer group | Quarterly | Ratio of highest to lowest above 1.25 | Above 1.5 | Model risk (second line) |

Red limits go to the model risk committee within two working days. The chief risk officer has the authority to pause the model. If it is paused, the issuer falls back to its fraud rules and extra manual review. Internal audit reviews the whole process once a year.

## Common Mistake
Many teams treat validation at launch as the end of model risk work. It is the start. Data, customers and fraud patterns change, so a model that was safe at launch may not stay safe. A plan without named people, limits and a pause authority is not a monitoring plan.

## Key Takeaways
1. Model risk management needs an inventory, independent validation, ongoing monitoring with limits, and clear owners.
2. The three lines of defence separate the people who build and use models, the people who challenge them, and the people who audit the system.
3. Decide before launch who can pause a model and what the fallback process is.

## Hands-on Exercise
**Task:** Draft a one-page monitoring plan for the fraud model from L03.
**Tools:** Google Sheets or Google Docs (free). Optional: Claude or ChatGPT (free plan) to check your plan for gaps [VERSION].
**Steps:**
1. Create a table with the columns: Measure, How often, Amber limit, Red limit, Who acts.
2. Add at least 5 measures, covering performance, data drift, score drift, data quality and fairness.
3. Set a limit for each one and a short reason for it.
4. Name the role (not a real person) that acts at each limit.
5. Write two sentences on who can pause the model and what the fallback process is.
6. Optional: ask an AI assistant, "What is missing from this monitoring plan?" Add only suggestions that you can justify.
**What good looks like:** A one-page plan with at least 5 measures, clear amber and red limits, named roles from the first and second lines, and a written pause authority and fallback.
**Time:** about 30 minutes

## Review Flags
- [REGION] [VERIFY] Confirm that US supervisory model risk guidance SR 11-7 is current before recording; the lesson teaches the three lines of defence as a general framework.
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
