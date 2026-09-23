"""Generate synthetic_patients.csv for AI-25 (AI in Healthcare), Lesson L02.

SYNTHETIC DATA FOR TEACHING ONLY. Not real patients.

Every value is drawn from a seeded random generator; no row describes a real person.
The data is built to reproduce the teaching points in L02:
  * missing values that are NOT random (HbA1c recorded mostly for patients with diabetes);
  * approximate missing rates: smoking status 31%, HbA1c 58%, BMI 12%, systolic BP 4%;
  * an unrepresentative sample: 80% of rows come from two urban districts.

Uses only the Python standard library. Run:  python make_synthetic_patients.py
"""
import csv
import datetime as dt
import os
import random

SEED = 2025
N = 500
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "synthetic_patients.csv")

# Fictional districts: two urban districts supply 80% of rows (400 of 500).
URBAN = [("Central Ward", 220), ("Harbour Ward", 180)]
RURAL = [("Hill District", 45), ("Lakeside District", 35), ("North Valley", 20)]

# Exact numbers of blank cells, so the percentages match L02.
MISSING = {"smoking_status": 155, "hba1c_percent": 290, "bmi": 60, "systolic_bp_mmhg": 20}


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def main():
    rng = random.Random(SEED)

    districts = []
    for name, count in URBAN + RURAL:
        districts += [(name, "urban" if (name, count) in URBAN else "rural")] * count
    rng.shuffle(districts)

    rows = []
    for i, (district, dtype) in enumerate(districts, start=1):
        age = int(clamp(rng.gauss(54, 15), 18, 90))
        sex = rng.choice(["F", "M"])
        bmi = round(clamp(rng.gauss(26.5, 4.5), 16.0, 45.0), 1)
        p_diab = 0.12 + 0.004 * (age - 18) + 0.02 * max(0.0, bmi - 25)
        diabetes = rng.random() < clamp(p_diab, 0.05, 0.6)
        smoking = rng.choices(["never", "former", "current"], weights=[55, 25, 20])[0]
        sbp = int(round(clamp(rng.gauss(118 + 0.45 * age + 0.6 * (bmi - 25) + (6 if diabetes else 0), 14), 90, 210)))
        hba1c = round(clamp(rng.gauss(7.6, 1.2) if diabetes else rng.gauss(5.4, 0.4), 4.2, 13.0), 1)
        last_visit = dt.date(2024, 1, 1) + dt.timedelta(days=rng.randrange(0, 730))
        rows.append({
            "patient_id": f"SYN-{i:04d}",
            "age": age,
            "sex": sex,
            "district": district,
            "district_type": dtype,
            "bmi": bmi,
            "systolic_bp_mmhg": sbp,
            "smoking_status": smoking,
            "diabetes_diagnosis": "yes" if diabetes else "no",
            "hba1c_percent": hba1c,
            "last_visit_date": last_visit.isoformat(),
        })

    # HbA1c: keep it for about 97% of patients with diabetes; fill the remaining
    # "recorded" slots with a small share of patients without diabetes. Blank the rest.
    n_keep = N - MISSING["hba1c_percent"]
    diab = [r for r in rows if r["diabetes_diagnosis"] == "yes"]
    non = [r for r in rows if r["diabetes_diagnosis"] == "no"]
    keep_diab = rng.sample(diab, min(len(diab), round(0.97 * len(diab)), n_keep))
    keep_non = rng.sample(non, n_keep - len(keep_diab))
    kept = {id(r) for r in keep_diab + keep_non}
    for r in rows:
        if id(r) not in kept:
            r["hba1c_percent"] = ""

    # Other columns: blank a fixed number of cells. BMI and smoking are missed more
    # often in rural districts (a recording-process pattern learners can find).
    for col in ("smoking_status", "bmi", "systolic_bp_mmhg"):
        weights = [2.0 if (r["district_type"] == "rural" and col != "systolic_bp_mmhg") else 1.0 for r in rows]
        idx = list(range(N))
        chosen = set()
        while len(chosen) < MISSING[col]:
            chosen.add(rng.choices(idx, weights=weights)[0])
        for j in chosen:
            rows[j][col] = ""

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # Summary for the README / instructor.
    print(f"Wrote {N} rows to {OUT}")
    for col in rows[0]:
        blanks = sum(1 for r in rows if r[col] == "")
        print(f"  {col:20s} missing {blanks:3d} ({100 * blanks / N:.0f}%)")
    n_d = len(diab)
    print(f"  diabetes 'yes': {n_d} ({100 * n_d / N:.0f}%); HbA1c recorded for "
          f"{len(keep_diab)} with diabetes and {len(keep_non)} without")
    urban = sum(1 for r in rows if r["district_type"] == "urban")
    print(f"  urban rows: {urban} ({100 * urban / N:.0f}%)")


if __name__ == "__main__":
    main()
