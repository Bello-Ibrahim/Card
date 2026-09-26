# L16 Detecting Data and Prediction Drift | Presenter Script

Course: AI-18 · Video: 5 min · Words: 696

## Hook
Nothing in your code changed, and your tests still pass. But the data your model sees today is not the data it learned from. How do you notice, and what should you do?

## Explain
In the last lesson, we watched our service. Now we look for drift. Drift means production data no longer looks like the training data. Three kinds matter. Data drift is when an input feature changes, for example average alcohol rises. Prediction drift is when the model's outputs change, for example many more good predictions.

Concept drift is when the relationship between the inputs and the true outcome changes. You can only measure it when true labels arrive. To detect data and prediction drift, compare a reference sample, your training data, with a current sample, your recent requests, one feature at a time.

Two methods are common. The Kolmogorov-Smirnov test, or KS, measures the largest gap between two distributions and gives a p-value. But with thousands of rows, even tiny, harmless differences look significant. So do not use the p-value alone.

The population stability index, or PSI, splits the reference into bins, and compares the share of rows in each bin. It measures the size of the shift, not only whether one exists. You will read common rules of thumb for PSI, but they are not a standard. Calibrate on your own data, for example between two normal weeks.

Drift is a signal, not a decision. For each alert, choose one of three responses. Retrain when the change is real, lasting and important, and you have new labels. Investigate when the cause is unclear, because it may be a pipeline bug. Ignore when the feature matters little, or the change is expected and short.

Think of a shop that sells winter coats and notices who walks in. If the customers suddenly look different, the shop first asks why, before it changes its stock.

## Demonstrate
Sofía Castro is a risk analyst at a hypothetical lender in Medellín, Colombia. After an online campaign, many younger applicants with shorter credit histories apply. PSI for age and credit history rises above her calibrated level. Her team investigates first, confirms the change is real, then retrains and reviews fairness, following local lending rules.

Let's simulate the same idea with the wine model. In a notebook, we load a reference sample and a new batch with a different seed. Then we add zero point eight to alcohol in the new batch only.

We run the PSI and KS loop for every feature. Alcohol has a PSI of zero point five zero five, and a KS p-value that is almost zero. The other features have PSI close to zero: zero point zero zero three, zero point zero one one and zero point zero zero six. Only alcohol shifted.

Next, we check prediction drift. We compute PSI on the model's predicted probabilities for both batches. This tells us whether the input shift is also changing the answers.

Finally, we write the decision in the notebook. Investigate. Check whether the alcohol measurement or unit changed at the source. Retrain only if the change is real and labels are available.

The common mistake is to retrain automatically every time a drift test fires. If the cause is a broken pipeline, retraining teaches the model the bug. Investigate first, and keep retraining behind the champion and challenger comparison from lesson fourteen.

## Recap
Let's recap. First, data drift, prediction drift and concept drift are different, and only concept drift needs true labels. Second, use PSI for the size of a shift and KS as support, and calibrate any thresholds on your own data. Third, for each drift alert, decide to retrain, investigate or ignore, and investigate before retraining.

## CTA
In the exercise below this video, you will change one feature in a batch of at least five hundred rows, compute PSI and KS for every feature and for the predictions, calibrate on unchanged data, and write a short decision. It takes about thirty-five minutes. Your capstone needs two drift reports like this.

Now you have every piece. In the next lesson, Capstone Part 1: Build and Automate, you put them together. See you there.

## Thumbnail
Headline: Same Code, Different Data
Image: Navy background, two overlapping histograms (training and today) with a gap between them, headline in teal Inter Bold.

## Production Notes
- [VERIFY] PSI thresholds (below 0.1 little change, 0.1 to 0.25 moderate, above 0.25 large) are commonly quoted rules of thumb, not standards. The voiceover does not state the numbers; it says rules of thumb exist and must be calibrated. If a slide shows them, label them 'rule of thumb, not a standard'.
- [VERIFY] The credit-model drift example (Sofía Castro, Medellín consumer lender) is hypothetical; the voiceover says so and gives no real data.
- [REGION] Lending regulations and fairness review requirements differ by country; the voiceover says only that the review follows local lending rules and states no specific rule.
- PSI and KS outputs (alcohol PSI 0.505 with KS p 1.54e-65; volatile_acidity 0.003, sulphates 0.011, citric_acid 0.006) are real results from the synthetic fallback data (SciPy 1.17.1, NumPy 2.4.6). The voiceover says the KS p-value is almost zero rather than reading the exponent. content.md gives no real value for prediction PSI, so the voiceover states none; show whatever the recording prints.
- The PSI function and loop are shown on screen and never read aloud.
- Credit stock footage must not show identifiable customers, real bank names or logos.
