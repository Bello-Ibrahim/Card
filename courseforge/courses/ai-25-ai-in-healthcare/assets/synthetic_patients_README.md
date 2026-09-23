# Synthetic Patient Dataset (AI-25, Lesson L02)

**SYNTHETIC DATA FOR TEACHING ONLY. Not real patients.**

`synthetic_patients.csv` has 500 rows, one per fictional adult clinic patient. A computer generated every value. No row describes a real person, and the districts are made up. Use it for the L02 hands-on exercise (listing variables, counting missing values, checking who is represented and thinking about privacy risks). Do not use it to draw any clinical conclusion.

## Columns

| Column | What it holds | Missing |
|---|---|---|
| `patient_id` | Fake ID, `SYN-0001` to `SYN-0500` | 0 |
| `age` | Age in whole years (18–90) | 0 |
| `sex` | `F` or `M` | 0 |
| `district` | Fictional district: Central Ward, Harbour Ward, Hill District, Lakeside District, North Valley | 0 |
| `district_type` | `urban` (Central Ward, Harbour Ward) or `rural` (the other three) | 0 |
| `bmi` | Body mass index, kg/m², one decimal place | 60 (12%) |
| `systolic_bp_mmhg` | Systolic blood pressure, mmHg | 20 (4%) |
| `smoking_status` | `never`, `former` or `current` | 155 (31%) |
| `diabetes_diagnosis` | `yes` or `no` | 0 |
| `hba1c_percent` | HbA1c, % | 290 (58%) |
| `last_visit_date` | Date of last visit, `YYYY-MM-DD`, between 2024-01-01 and 2025-12-31 | 0 |

A missing value is an empty cell, so `COUNTBLANK` in Google Sheets, Excel or LibreOffice Calc counts it.

## Patterns built in for the exercise

- **Missing data is not random.** HbA1c is recorded for 161 of the 166 patients with a diabetes diagnosis, but for only 49 of the 334 without one. A model trained on this data could learn "HbA1c present" as a sign of diabetes. This comes from how the data was recorded, not from the patients.
- **BMI and smoking status are missed more often in the rural districts** (the generator gives rural rows twice the chance of a blank in these two columns: 55% of rural rows lack smoking status against 25% of urban rows, and 19% lack BMI against 10%).
- **The sample is unrepresentative.** 400 of 500 rows (80%) come from the two urban districts. North Valley has only 20 patients.
- **Privacy risk if the data were real.** Exact age, a small district and a diagnosis together could point to one person, especially in North Valley. Grouping ages into bands and removing exact dates would reduce the risk.

The missing rates match the worked example in L02 (smoking status 31%, HbA1c 58%, BMI 12%, systolic blood pressure 4%). The clinical values are rough, made-up distributions; they are not reference ranges and are not suitable for any clinical use.

## How it was generated

`make_synthetic_patients.py` (in this folder) uses only the Python standard library and a fixed random seed (`2025`), so running it again produces the same file:

```
python make_synthetic_patients.py
```

Steps in the script:

1. Assign each row to a district with fixed counts (Central Ward 220, Harbour Ward 180, Hill District 45, Lakeside District 35, North Valley 20), then shuffle.
2. Draw age, sex and BMI from simple random distributions. The chance of a diabetes diagnosis rises with age and BMI. Systolic blood pressure rises with age and BMI and is a little higher with diabetes. HbA1c is drawn higher for patients with diabetes.
3. Blank HbA1c for all but 210 patients, keeping it for about 97% of patients with diabetes and filling the remaining slots from patients without diabetes.
4. Blank a fixed number of cells in `smoking_status`, `bmi` and `systolic_bp_mmhg`, with rural rows twice as likely to be chosen for BMI and smoking status.
5. Write the CSV and print a summary of missing values.
