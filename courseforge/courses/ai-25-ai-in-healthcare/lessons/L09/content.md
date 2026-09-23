# L09 Bias, Equity and Dataset Shift

Course: AI-25 · Module: M2 · Objectives: O4 · Video: 5 min

## Hook
A tool reports an overall sensitivity of 80%. That single number can hide a tool that finds 90% of cases in one group of patients and only 65% in another. Who are the patients inside the missing 35%?

## Explanation
An AI tool's performance can differ between groups of patients and between care settings. Two related problems cause this.

**Bias across patient groups.** Performance may differ by sex, age, skin tone, ethnicity, language, disability or income. Common causes are:
- **Under-representation:** some groups appear rarely in the training data, so the model learns less about them.
- **Label bias:** the "correct answers" reflect unequal care. For example, if one group was historically diagnosed later, the labels teach the model that pattern.
- **Proxy variables:** a variable such as past healthcare cost or postcode can stand in for income or ethnicity, and carry existing inequality into predictions.
- **Measurement differences:** some devices and methods work less well for some groups, for example image quality on different skin tones.

**Dataset shift.** Performance can fall when the setting changes after training:
- **Population shift:** different ages, disease mix or prevalence.
- **Equipment and process shift:** new scanners, different camera settings, different laboratory methods, or a new way of recording data.
- **Time shift:** clinical practice, coding rules or disease patterns change over time.

The practical rule is: **never accept one overall figure.** Ask for results broken down by relevant patient groups and by site, with the number of patients in each group, because figures from small groups are uncertain.

**Analogy:** A shoe factory that measures only city customers may make excellent shoes that fit badly on people who walk long distances on rough roads. The shoes are not "bad", but they were not designed or tested for everyone who will wear them.

Published real cases of bias in health AI exist and may be added to this course only after they are checked [VERIFY]. The cases in this lesson are hypothetical.

## Worked Example
Dr. Neema Mwakasege works for a hypothetical regional health authority in Tanzania. A supplier offers a tool that flags chest X-rays that may show tuberculosis for clinician review. It was developed with data from large city hospitals using fixed digital X-ray machines. The region wants to use it in rural clinics that use portable machines and serve more older patients and more people living with HIV.

Neema asks for a **synthetic** local check set up to illustrate the risk:

| Site | Patients with the condition | Flagged by tool | Sensitivity |
|---|---|---|---|
| City hospitals | 200 | 184 | 92.0% |
| Rural clinics | 150 | 114 | 76.0% |

In this synthetic example, the tool misses about 1 in 4 cases in rural clinics, compared with about 1 in 12 in city hospitals. Possible reasons include image quality from portable machines, a different patient mix, and different disease appearance in people living with HIV.

Neema does not simply reject the tool. She asks the supplier for results by device type and by HIV status, requests a local silent-mode test in three rural clinics, and makes it clear that clinicians must not treat a negative result as ruling out disease.

## Common Mistake
Many people believe that removing sensitive variables such as sex or ethnicity from the data makes a model fair. It does not. Other variables, such as postcode, device type or past use of services, can carry the same information, and the model may still perform differently across groups. Fairness has to be **measured** in results for each group, not assumed from the list of inputs.

## Key Takeaways
1. Performance can differ across patient groups because of under-representation, label bias, proxy variables and measurement differences.
2. Dataset shift in population, equipment, process or time can reduce performance when a tool moves to a new setting.
3. Always ask for results broken down by patient group and by site, with group sizes, and never rely on one overall figure.

## Hands-on Exercise
**Task:** Compare sensitivity across 3 patient groups and 2 sites in a synthetic results table. Write 3 questions you would ask the tool's supplier.
**Tools:** Pen and paper, a calculator, or Google Sheets / Excel.
**Steps:**
1. Use this **synthetic** table for a hypothetical tool that flags skin photographs for dermatologist review. Groups are skin types on a common 6-point scale, combined into three bands.

| Site | Skin type band | With condition | Flagged |
|---|---|---|---|
| A (city hospital) | I–II | 120 | 108 |
| A (city hospital) | III–IV | 100 | 87 |
| A (city hospital) | V–VI | 40 | 30 |
| B (rural clinic) | I–II | 30 | 24 |
| B (rural clinic) | III–IV | 60 | 45 |
| B (rural clinic) | V–VI | 80 | 52 |

2. Calculate sensitivity (flagged ÷ with condition) for each row, for each site, and overall.
3. Identify the group and site with the lowest sensitivity and note how many patients that figure is based on.
4. Write two possible reasons for the differences, one about bias and one about dataset shift.
5. Write 3 questions for the supplier.
**What good looks like:** Site A: 90.0%, 87.0%, 75.0% (site 86.5%). Site B: 80.0%, 75.0%, 65.0% (site 71.2%). Overall 80.5%. The learner notices that skin type V–VI at Site B is lowest, and that the overall figure hides this. Questions are specific, for example: "How many images of skin types V–VI were in your training data?", "Which cameras were used?", "Do you have results from rural or primary care settings?"
**Time:** about 25 minutes

## Review Flags
- [VERIFY] Any published real case of bias or dataset shift in health AI must be checked against its source before it is added. All cases and figures in this lesson are hypothetical and synthetic; calculations were checked with python3.
