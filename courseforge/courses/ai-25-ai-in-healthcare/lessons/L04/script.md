# L04 Reading Performance Claims | Presenter Script

Course: AI-25 · Video: 5 min · Words: 699

## Hook
A brochure says a tool is ninety percent accurate. You use it on a thousand patients in a screening clinic, and for every correct alert, there are about eleven false ones. Nobody lied. This lesson explains how that happens.

## Explain
In the last lesson, we followed how a clinical model is built and tested. Now we learn to read the numbers that come out of that testing. Every result from a yes or no tool falls into one of four boxes, called a confusion matrix.

From these four boxes come the measures in performance claims. Sensitivity asks: of the people who have the condition, what share does the tool find? Specificity asks: of the people who do not have it, what share does the tool correctly clear? Positive predictive value asks: when the tool says positive, how often is it right?

Sensitivity and specificity describe the tool. But predictive values depend on the tool and on how common the condition is in the people tested. This is called prevalence. When a condition is rare, even a small false positive rate produces many false alarms, compared with the few true cases. A single accuracy number can hide this.

When a condition is rare, a tool that says negative for everyone can have very high accuracy, and still miss every case.

Here is a simple way to picture it. Think of a smoke alarm. A sensitive alarm rarely misses a fire. But in a kitchen where people cook every day, it will often sound for toast. Real fires are rare, so most alarms are false, even though the alarm works exactly as designed.

## Demonstrate
Let's work through an example. All the numbers here are synthetic, created for teaching. Doctor Aigerim Seitkali, a hospital physician in Kazakhstan, is reviewing a hypothetical tool that flags a condition for specialist review. The supplier states a sensitivity of ninety percent and a specificity of ninety percent. She works through a thousand synthetic patients in two settings.

Setting one is a specialist clinic, where the prevalence is ten percent. So one hundred of the thousand patients have the condition. The tool finds ninety of them, and misses ten. Of the nine hundred without the condition, it wrongly flags ninety.

So when the tool says positive, it is right ninety times out of one hundred and eighty. The positive predictive value is fifty percent. Half of the flags are real cases. And when it says negative, it is right ninety-eight point eight percent of the time.

Setting two is general screening, where the prevalence is one percent. Now only ten of the thousand patients have the condition. The tool finds nine and misses one. But of the nine hundred and ninety without the condition, it wrongly flags ninety-nine.

Sensitivity is still ninety percent, and specificity is still ninety percent. But the positive predictive value falls to eight point three percent, while the negative predictive value is ninety-nine point nine percent. Only about one in twelve flags is a true case, and specialists would review about eleven false alarms for each real one.

The tool is identical in both settings. Aigerim concludes that it may be useful in the specialist clinic, but needs a careful review of workload and harm before any use in screening. A common mistake is to read sensitivity as the chance that a positive result is correct. That is positive predictive value, and it falls sharply when a condition is rare.

## Recap
Let's recap. First, sensitivity and specificity describe how the tool behaves in people with and without the condition, while predictive values tell you how far to trust a result. Second, positive predictive value depends on prevalence, so the same tool gives many more false alarms when a condition is rare. Third, check any real figure against its published source and setting.

## CTA
Now it is your turn. In the exercise below this video, you will use a synthetic results table to calculate sensitivity, specificity and positive predictive value at two prevalence levels, and explain the difference in two sentences. It takes about twenty minutes. In the next lesson, we look at levels of evidence, from study to real-world use. See you there.

## Thumbnail
Headline: 90% Accurate? Check Again
Image: Navy background, a brochure badge reading 90% next to a grid of 1,000 small dots with a few teal true alerts and many grey false alerts, headline in teal Inter Bold.

## Production Notes
- Clinical reviewer sign-off required.
- All figures are synthetic, created for teaching; the voiceover says so where numbers appear. Every number on screen must match content.md exactly: Setting 1 (prevalence 10%): TP 90, FP 90, FN 10, TN 810; sensitivity 90.0%, specificity 90.0%, PPV 50.0%, NPV 98.8%. Setting 2 (prevalence 1%): TP 9, FP 99, FN 1, TN 891; sensitivity 90.0%, specificity 90.0%, PPV 8.3%, NPV 99.9%. Calculations were checked with python3 in Stage 2.
- Label every data slide 'Synthetic figures for teaching'.
- [VERIFY] Any real diagnostic performance figure for a named tool must be checked against its published source before it is added. No real tool or figure appears in this lesson.
- Dr. Aigerim Seitkali (Kazakhstan) and the tool are hypothetical. The lesson explains how to read claims; it gives no advice on whether to use any real tool.
