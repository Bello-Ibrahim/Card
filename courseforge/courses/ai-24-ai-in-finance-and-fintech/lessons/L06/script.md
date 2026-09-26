# L06 Fairness in Credit Decisions | Presenter Script

Course: AI-24 · Video: 5 min · Words: 719

## Hook
A credit model never sees an applicant's gender or ethnicity. Its designers removed those columns on purpose. Can it still treat one group of customers unfairly? Yes. And this lesson shows how.

## Explain
Welcome to week two. Last time, we saw that credit models learn from past decisions. A credit decision affects whether a person can start a business, buy a home or handle an emergency. That is why fairness is a central question for any credit model.

Protected characteristics are personal traits that the law in many countries says must not be the basis for unfair treatment. Common examples include gender, ethnicity, religion, age, disability and marital status. The exact list differs by country, so always check it with your compliance team.

There are two forms of discrimination. Direct discrimination means treating someone less favourably because of a protected characteristic. It is usually easy to see. Indirect discrimination means a rule that looks neutral, but puts one protected group at a clear disadvantage without a good reason. In AI, this is the more common risk, and it is harder to see.

Indirect discrimination often comes through proxy variables. A proxy is a feature closely linked to a protected characteristic. Postcode can be linked to ethnicity or income. Phone type can be linked to income or age. And gaps in employment can be linked to caring responsibilities, and therefore to gender.

Removing the protected column does not remove the pattern. The model can rebuild it from proxies. So fairness must be checked by looking at outcomes by group, not only at the list of inputs.

A first, simple measure is the approval rate for each group, and the ratio between the lowest and the highest rate. A ratio of one means equal approval rates. A lower ratio means a larger gap. A gap is not automatic proof of discrimination. But it is a signal that must be investigated and explained.

Imagine a set of market scales that is slightly wrong for one type of container. Every time a customer uses that container, the weight is wrong. The error is small, but it happens every time, to the same customers. A biased model works the same way, on thousands of decisions.

## Demonstrate
Priya Raman is a credit risk analyst at Maple Ridge Credit, a hypothetical consumer lender. The model does not use gender. Priya tests its decisions on a synthetic sample, grouped by gender for testing only. Of four hundred men, two hundred and eighty were approved. That is seventy percent. Of three hundred women, one hundred and sixty-five were approved. That is fifty-five percent.

The ratio is fifty-five divided by seventy, which is about zero point seven nine. So Priya looks for explanations. One of the model's strongest features is months in continuous employment. In the sample, women more often have short career breaks for childcare. So employment gaps may be acting as a proxy for gender.

She also checks whether the groups differ in actual repayment, because that would be a legitimate reason for part of the gap. Her note to the credit committee does not say the model is sexist. It says there is a fifteen percentage point gap, one feature may act as a proxy, and the team should test the model without it and compare error rates by group.

A common mistake is to believe a model is fair if it does not use protected characteristics. This is called fairness through unawareness, and it does not work well, because proxies carry the same information.

## Recap
Let's recap. First, direct discrimination uses a protected characteristic, while indirect discrimination uses a neutral-looking rule or feature that disadvantages a protected group. Second, proxy variables such as postcode, phone type or employment gaps can bring bias back into a model. Third, check fairness by measuring outcomes by group, such as approval rates and their ratio, then investigate the reasons behind any gap.

## CTA
Now it is your turn. In the exercise below this video, you will open a synthetic set of loan decisions in Google Sheets, calculate the approval rate for each group, and the ratio between the lowest and highest rate. Then note what could explain the gap. It takes about twenty-five minutes. In the next lesson, we look at measuring and reducing bias. See you there.

## Thumbnail
Headline: Fair Without Gender Data?
Image: Navy background, a market scale tipped slightly to one side with two groups of simple person icons, headline in teal Inter Bold.

## Production Notes
- [REGION] The list of protected characteristics, and the legal tests for direct and indirect discrimination, differ by country. The script says 'in many countries' and tells learners to check with their compliance team; keep that wording.
- [REGION] Rules on collecting or estimating protected characteristics for fairness testing differ by country and data protection law. The script mentions only that this raises privacy questions.
- Figures must match content.md exactly: men 400 applicants, 280 approved, 70.0%; women 300 applicants, 165 approved, 55.0%; ratio 0.79 (spoken 'zero point seven nine'); gap 15 percentage points.
- Priya Raman and Maple Ridge Credit are fictional; the sample is synthetic and grouped by gender for testing only. Do not name or suggest any real lender.
