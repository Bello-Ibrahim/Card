# L06 Data Protection Principles Across the AI Lifecycle

Course: AI-30 · Module: M2 · Objectives: O2 · Video: 5 min

## Hook
You already know the data protection principles. But what does "data minimisation" mean when a data scientist says, "The model will be better if we give it everything"? This lesson shows how the familiar principles apply at each stage of an AI system's life.

## Explanation
This lesson is educational and is not legal advice. The GDPR and the NDPA both set out core principles, in [the principles article of the GDPR] and [the principles section of the NDPA] [VERIFY] [REGION]. Their wording is similar but not identical, so check both texts.

The principles you know are: **lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality (security); and accountability.** AI does not change these principles. It changes where the pressure falls. A simple AI lifecycle has five stages:

1. **Data collection.** Data is gathered or reused from existing systems. *Main pressure:* purpose limitation. Data collected to handle claims or run accounts is now used for a new purpose. You must check whether the new purpose is compatible or needs its own basis (see L07).
2. **Training.** The model learns patterns from the data. *Main pressure:* data minimisation and fairness. Teams want more fields and more history. Some fields, such as postcode, can act as a proxy for ethnicity or income and create unfair outcomes.
3. **Testing and validation.** The model is checked before use. *Main pressure:* accuracy and fairness. Testing should check error rates for different groups, not only the overall score.
4. **Deployment.** The model makes or supports real decisions. *Main pressure:* transparency and security. People must be told about the processing in clear words, and the system must be protected against attacks such as attempts to extract training data.
5. **Retirement.** The model is replaced or switched off. *Main pressure:* storage limitation. Training datasets, copies and old models may still hold personal data long after they are needed.

**Accountability** runs across all five stages: you must be able to show how you applied each principle.

**Analogy:** Think of water flowing through a treatment plant. The safety standards are the same at every point, but each stage has its own main danger: dirt at the intake, chemicals at treatment, leaks in the pipes. Inspectors check the standard where the danger is greatest. Data protection principles work the same way across the AI lifecycle.

## Worked Example
Youssef Benali is DPO at a hypothetical insurer in Casablanca, Morocco, which also sells travel insurance to customers in France. The claims team wants to train a model to flag possibly fraudulent claims, using ten years of claim files. Because French customers are included, the GDPR is likely to apply, as well as Moroccan law [VERIFY] [REGION].

Youssef applies **data minimisation** stage by stage:

- **Collection:** does the model need all ten years? Fraud patterns change, and older files may reflect products the company no longer sells. The team agrees to test whether five years give similar results.
- **Fields:** the files contain names, ID numbers, medical notes from travel claims and free-text comments. The team removes names and ID numbers before training and replaces them with codes. Medical notes are health data, a special category, so they are excluded unless a clear need and a valid condition are shown.
- **Testing:** the team checks whether the model flags claims from some nationalities more often.
- **Retirement:** the team sets a rule to delete the training copy when the model is retrained.

The result is a smaller dataset with a documented reason for each field.

## Common Mistake
Many learners think removing names makes the data anonymous. Coded or "pseudonymised" data is still personal data if the organisation, or someone else, can link it back to a person. True anonymisation is hard, especially with rich datasets. Treat pseudonymisation as a security control, not as a way to leave data protection law behind.

## Key Takeaways
1. The same data protection principles apply at every AI stage: collection, training, testing, deployment and retirement.
2. Each stage has a main pressure point, such as purpose limitation at collection and storage limitation at retirement.
3. Pseudonymised data is still personal data; this lesson is educational, not legal advice.

## Hands-on Exercise
**Task:** Draw the 5 stages of an AI lifecycle and write, for each stage, the one data protection principle most at risk and one control that protects it.
**Tools:** Paper, a whiteboard app or a slide tool; the principles sections of the GDPR and the NDPA from official sources [VERIFY].
**Steps:**
1. Choose a hypothetical AI system, such as a model that predicts which customers of an energy company will miss a payment.
2. Draw five boxes in a row: collection, training, testing, deployment, retirement.
3. Under each box, write the principle most at risk and one sentence on why.
4. Add one practical control for each stage, such as "field-by-field justification" or "deletion date for training copies".
5. Use invented details only. Do not paste real customer data into any AI tool.
**What good looks like:** Five stages, a different or well-justified principle for each, and concrete controls that a project team could actually carry out.
**Time:** about 20 minutes

## Review Flags
- Legal/compliance reviewer sign-off required before release.
- [VERIFY] [REGION] The wording of the principles in the GDPR and the NDPA, and the placeholders for their articles and sections, must be checked (curriculum flag).
- [VERIFY] [REGION] Whether the GDPR and Moroccan law apply to the hypothetical Casablanca insurer must be confirmed by the legal reviewer.
- [VERIFY] Official sources for the exercise must be chosen, with date recorded.
