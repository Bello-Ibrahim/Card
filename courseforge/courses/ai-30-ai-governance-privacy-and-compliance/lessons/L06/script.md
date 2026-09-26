# L06 Data Protection Principles Across the AI Lifecycle | Presenter Script

Course: AI-30 · Video: 5 min · Words: 688

## Hook
You already know the data protection principles. But what does data minimisation mean when a data scientist says, the model will be better if we give it everything? Today we see how the familiar principles apply at each stage of an AI system's life.

## Explain
Welcome to module two, on data protection law and AI. As always, this course is educational and is not legal advice. The GDPR and the NDPA both set out core principles. Their wording is similar, but not identical, so always check both texts.

The principles you know are lawfulness, fairness and transparency, purpose limitation, data minimisation, accuracy, storage limitation, security, and accountability. AI does not change these principles. It changes where the pressure falls.

A simple AI lifecycle has five stages. First, data collection, where data is gathered or reused from other systems. The main pressure here is purpose limitation. Data collected to handle claims is now used for a new purpose, so you must check whether that purpose is compatible or needs its own basis.

Second, training. Here the pressure is on data minimisation and fairness. Teams want more fields and more history. And some fields, such as postcode, can act as a proxy for ethnicity or income, and create unfair outcomes.

Third, testing, where the pressure is on accuracy and fairness. Test error rates for different groups, not only the overall score. Fourth, deployment, where the pressure is on transparency and security. Tell people about the processing in clear words, and protect the system against attacks.

Fifth, retirement. The pressure is on storage limitation, because old datasets, copies and models may still hold personal data long after they are needed. And accountability runs across all five stages. You must be able to show how you applied each principle.

Think of water flowing through a treatment plant. The safety standards are the same at every point, but each stage has its own main danger: dirt at the intake, chemicals at treatment, leaks in the pipes. Inspectors check where the danger is greatest. The principles work the same way.

## Demonstrate
Let's see data minimisation in action. Youssef Benali is the data protection officer at a fictional insurer in Casablanca, Morocco, which also sells travel insurance to customers in France. So the GDPR may apply, alongside Moroccan law.

The claims team wants to train a model to flag possibly fraudulent claims, using ten years of claim files. Youssef asks: does the model need all ten years? Fraud patterns change, and older files reflect products the company no longer sells. The team agrees to test whether five years give similar results.

Next, the fields. The files contain names, ID numbers, medical notes from travel claims and free-text comments. The team replaces names and ID numbers with codes before training. Medical notes are health data, a special category, so they are left out unless a clear need and a valid condition are shown.

For testing, the team checks whether the model flags claims from some nationalities more often. And for retirement, it sets a rule to delete the training copy when the model is retrained. The result is a smaller dataset, with a documented reason for each field.

A common mistake is to think that removing names makes data anonymous. Coded, or pseudonymised, data is still personal data if someone can link it back to a person. True anonymisation is hard. So treat pseudonymisation as a security control, not as a way to leave data protection law behind.

## Recap
Let's recap. First, the same data protection principles apply at every AI stage: collection, training, testing, deployment and retirement. Second, each stage has a main pressure point, such as purpose limitation at collection and storage limitation at retirement. Third, pseudonymised data is still personal data.

## CTA
In the exercise below this video, you will draw the five stages of an AI lifecycle. For each stage, write the one principle most at risk, and one control that protects it. Use the principles as written in the official texts of both laws.

In the next lesson, we look at one principle more closely: the lawful basis for AI processing. See you there.

## Thumbnail
Headline: Principles at Every Stage
Image: Navy background, a teal five-stage loop from data collection to retirement with a small shield icon at each stage, headline in teal Inter Bold.

## Production Notes
- Legal/compliance reviewer sign-off required before release.
- Disclaimer spoken once in scene 2 (educational, not legal advice).
- [VERIFY] [REGION] Principles: content.md placeholders [the principles article of the GDPR] and [the principles section of the NDPA]. The wording of each principle in the two laws is similar but not identical and must be checked. The voiceover names the principles in general terms only.
- [VERIFY] [REGION] Whether the GDPR and Moroccan law apply to the fictional Casablanca insurer must be confirmed by the legal reviewer. The voiceover says only that the GDPR may apply alongside Moroccan law (scene 9).
- [VERIFY] Official sources for the exercise must be chosen, with date recorded.
- Youssef Benali and the Casablanca insurer are fictional. Stock footage must not show real insurer branding or readable claim files.
