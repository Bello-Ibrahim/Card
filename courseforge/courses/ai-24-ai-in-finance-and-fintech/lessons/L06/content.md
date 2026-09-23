# L06 Fairness in Credit Decisions

Course: AI-24 · Module: M2 · Objectives: O4 · Video: 5 min

## Hook
A credit model never sees an applicant's gender or ethnicity. Its designers removed those columns on purpose. Can it still treat one group of customers unfairly? Yes, and this lesson shows how.

## Explanation
A credit decision affects whether a person can start a business, buy a home or handle an emergency. That is why fairness is a central question for any credit model.

**Protected characteristics** are personal traits that the law in many countries says must not be the basis for unfair treatment. Common examples include sex or gender, race or ethnicity, religion, age, disability and marital status. The exact list, and the exceptions, differ by country [REGION]. Always check the list that applies to your institution with your compliance team.

There are two forms of discrimination to understand.

- **Direct discrimination** means treating someone less favourably because of a protected characteristic, for example a rule that declines applicants of a certain religion. This is usually easy to see in a rule or a data field.
- **Indirect discrimination** means applying a rule that looks neutral to everyone but puts one protected group at a clear disadvantage, without a good and proportionate reason. In AI, this is the more common risk, and it is harder to see.

Indirect discrimination often happens through **proxy variables**. A proxy is a feature that is closely linked to a protected characteristic. Examples in finance include:

- **Postcode or district**, which can be linked to ethnicity or income.
- **Phone type or operating system**, which can be linked to income or age.
- **First name or language settings**, which can be linked to ethnicity or gender.
- **Gaps in employment**, which can be linked to caring responsibilities and therefore to gender.

Removing the protected column does not remove the pattern. The model can "rebuild" it from proxies. So fairness must be checked by **looking at outcomes by group**, not only at the list of inputs. To do this, institutions need some reliable way to know or estimate group membership for testing, which raises its own privacy questions [REGION].

A first, simple measure is the **approval rate** for each group and the **ratio** between the lowest and the highest rate. A ratio of 1.0 means equal approval rates. A lower ratio means a larger gap. A gap is not automatic proof of discrimination, because groups can differ in real repayment ability. But a gap is a signal that must be investigated and explained.

**Analogy:** Imagine a set of scales in a market that is slightly wrong for one type of container. Every time a customer uses that container, the scales show the wrong weight. The error is small, but it happens every time, to the same customers. A biased model works the same way: a small error, repeated automatically on thousands of decisions, becomes a large unfair result.

## Worked Example
Priya Raman is a credit risk analyst at Maple Ridge Credit, a hypothetical consumer lender. The lender's model does not use gender. Priya tests its decisions on a synthetic sample, grouped by gender for testing only:

| Group | Applicants | Approved | Approval rate |
|---|---|---|---|
| Men | 400 | 280 | 70.0% |
| Women | 300 | 165 | 55.0% |

The ratio between the lowest and the highest rate is 55.0 ÷ 70.0 ≈ **0.79**.

Priya looks for explanations. She finds that "months in continuous employment" is one of the model's strongest features. In the sample, women more often have short career breaks for childcare. Employment gaps may be acting as a proxy for gender. She also checks whether the groups differ in actual repayment behaviour, because that would be a legitimate reason for part of the gap.

Her note to the credit committee does not say "the model is sexist". It says: "There is a 15-percentage-point gap in approval rates. One feature may act as a proxy. We recommend testing the model without it and comparing error rates by group (see L07)."

## Common Mistake
Many teams believe that a model is fair if it does not use protected characteristics as inputs. This is called "fairness through unawareness", and it does not work well, because proxies carry the same information. The correct approach is to measure outcomes by group, investigate every large gap, and document the reasons and actions.

## Key Takeaways
1. Direct discrimination uses a protected characteristic; indirect discrimination uses a neutral-looking rule or feature that disadvantages a protected group.
2. Proxy variables such as postcode, phone type or employment gaps can bring bias back into a model that does not use protected data.
3. Check fairness by measuring outcomes, such as approval rates and their ratio, by group, then investigate the reasons behind any gap.

## Hands-on Exercise
**Task:** Calculate approval rates by group and the ratio between the lowest and highest rate on synthetic loan decisions.
**Tools:** Google Sheets (free) and the course's synthetic loan-decisions file.
**Steps:**
1. Open the synthetic loan-decisions file. It has a group column and an approved column (1 or 0). It contains no real customer data.
2. In a summary table, use COUNTIF to count applicants per group.
3. Use COUNTIFS to count approved applicants per group.
4. Calculate each group's approval rate: approved ÷ applicants.
5. Calculate the ratio: lowest approval rate ÷ highest approval rate.
6. Look at the other columns and note 2 features that could be proxies for the group, and 1 legitimate reason that could explain part of the gap.
**What good looks like:** Correct counts and rates, a ratio with two decimal places, and a short note that treats the gap as a signal to investigate, not as proof, with at least one possible proxy named.
**Time:** about 25 minutes

## Review Flags
- [REGION] The list of protected characteristics, and the legal tests for direct and indirect discrimination, differ by country; confirm with local law.
- [REGION] Rules on collecting or estimating protected characteristics for fairness testing differ by country and data protection law.
