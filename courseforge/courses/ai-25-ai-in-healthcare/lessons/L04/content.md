# L04 Reading Performance Claims

Course: AI-25 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
A brochure says a tool is "90% accurate". You use it on 1,000 patients in a screening clinic, and for every correct alert there are about eleven false ones. Nobody lied. This lesson explains how that happens.

## Explanation
Every result from a yes/no tool falls into one of four boxes, called a **confusion matrix**:

| | Condition present | Condition absent |
|---|---|---|
| **Tool says positive** | True positive (TP) | False positive (FP) |
| **Tool says negative** | False negative (FN) | True negative (TN) |

From these four numbers come the measures you will see in performance claims:

- **Sensitivity** = TP / (TP + FN). Of the people who have the condition, what share does the tool find?
- **Specificity** = TN / (TN + FP). Of the people who do not have the condition, what share does the tool correctly clear?
- **Positive predictive value (PPV)** = TP / (TP + FP). When the tool says positive, how often is it right?
- **Negative predictive value (NPV)** = TN / (TN + FN). When the tool says negative, how often is it right?

Sensitivity and specificity describe the tool. PPV and NPV depend on the tool **and** on how common the condition is in the people tested, called **prevalence**. When a condition is rare, most people tested do not have it, so even a small false-positive rate produces many false alarms compared with the few true cases.

"Accuracy" alone, meaning (TP + TN) / total, can hide this. When a condition is rare, a tool that says "negative" for everyone can have very high accuracy and still miss every case.

**Analogy:** Think of a smoke alarm. A sensitive alarm rarely misses a fire, but in a kitchen where people cook every day it will often sound for toast. Real fires are rare, so most alarms are false, even though the alarm works exactly as designed.

Any real performance figure for a named tool must be checked against its published source, including the setting and the patients it was measured in [VERIFY]. In this course, all figures are synthetic.

## Worked Example
All numbers below are **synthetic** and created for teaching. Dr. Aigerim Seitkali, a hospital physician in Kazakhstan, is reviewing a hypothetical tool that flags a condition for specialist review. The supplier states a sensitivity of 90% and a specificity of 90%. She works through 1,000 synthetic patients in two settings.

**Setting 1: specialist clinic, prevalence 10% (100 of 1,000 patients have the condition).**

| | Present (100) | Absent (900) |
|---|---|---|
| Tool positive | TP = 90 | FP = 90 |
| Tool negative | FN = 10 | TN = 810 |

- Sensitivity = 90 / 100 = 90.0%
- Specificity = 810 / 900 = 90.0%
- PPV = 90 / (90 + 90) = 50.0%
- NPV = 810 / (810 + 10) = 98.8%

**Setting 2: general screening, prevalence 1% (10 of 1,000 patients have the condition).**

| | Present (10) | Absent (990) |
|---|---|---|
| Tool positive | TP = 9 | FP = 99 |
| Tool negative | FN = 1 | TN = 891 |

- Sensitivity = 9 / 10 = 90.0%
- Specificity = 891 / 990 = 90.0%
- PPV = 9 / (9 + 99) = 8.3%
- NPV = 891 / (891 + 1) = 99.9%

The tool is identical in both settings. But in screening, only about 1 in 12 positive flags is a true case, and specialists would review about 11 false alarms for each real one. Aigerim concludes that the tool may be useful in the specialist clinic but needs a careful workload and harm review before any use in screening.

## Common Mistake
Many people read sensitivity as "the chance that a positive result is correct". That is PPV, not sensitivity, and PPV falls sharply when a condition is rare. Always ask for the prevalence in the study population and calculate what PPV would be in your own setting before judging a claim.

## Key Takeaways
1. Sensitivity and specificity describe how the tool behaves in people with and without the condition; PPV and NPV describe how far you can trust a positive or negative result.
2. PPV depends on prevalence: the same tool gives many more false alarms when the condition is rare.
3. Check any real figure against its published source and the setting where it was measured; do not rely on a single "accuracy" number.

## Hands-on Exercise
**Task:** Using the synthetic results table, calculate sensitivity, specificity and positive predictive value at two different disease prevalence levels. Explain the difference in two sentences.
**Tools:** Pen and paper, a calculator, or Google Sheets / Excel.
**Steps:**
1. Use these **synthetic** results for a hypothetical tool tested on 1,000 people in each setting.
   Setting A (prevalence 20%): TP = 170, FN = 30, FP = 40, TN = 760.
   Setting B (prevalence 2%): TP = 17, FN = 3, FP = 49, TN = 931.
2. Draw a confusion matrix for each setting.
3. Calculate sensitivity, specificity and PPV for each setting. Round to one decimal place.
4. Write two sentences explaining why PPV changes while sensitivity and specificity do not.
5. Optional: set up the formulas in a spreadsheet so you can change the prevalence and watch PPV change.
**What good looks like:** Setting A: sensitivity 85.0%, specificity 95.0%, PPV 81.0%. Setting B: sensitivity 85.0%, specificity 95.0%, PPV 25.8%. The explanation says that the tool behaves the same way, but with fewer true cases in Setting B, false positives make up a much larger share of all positive results.
**Time:** about 20 minutes

## Review Flags
- Clinical reviewer sign-off required.
- [VERIFY] Any real diagnostic performance figure for a named tool must be checked against its published source before it is added. This lesson uses synthetic figures only; all calculations were checked with python3.
