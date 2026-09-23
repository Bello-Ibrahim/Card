# L11 What Makes Data Bad?

Course: AI-17 · Module: M3 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
Bad data rarely crashes anything. The pipeline finishes, the dashboard loads and the model trains. It simply learns the wrong thing, and nobody notices until a decision based on it goes wrong.

## Explanation
Data quality is easier to discuss when you break it into six dimensions:

| Dimension | Question | Example problem |
|---|---|---|
| Completeness | Are required values present? | Missing customer ID |
| Uniqueness | Is each real event recorded once? | The same visit loaded twice |
| Validity | Do values follow the rules for their type and range? | A body temperature of 73 °C |
| Consistency | Do related values agree across rows and tables? | A delivery date before the order date |
| Timeliness | Is the data recent enough for its use? | Yesterday's file has not arrived |
| Accuracy | Does the value match reality? | A wrong price typed by a clerk |

The first five can usually be checked with SQL. Accuracy often needs a comparison with another trusted source or a human check.

For AI, each problem has a specific effect. Duplicates make some events look more common. Missing values in one group make the model less reliable for that group. Invalid values stretch averages and scales. None of these produce an error message, so you must look for them on purpose. This is called **profiling**: counting missing values, duplicates and out-of-range values per column before you trust a dataset.

DuckDB is a good profiling tool. Its `SUMMARIZE` command shows the minimum, maximum, approximate distinct count and null percentage for every column of a table in one step [VERSION]. Targeted queries then count exactly what you care about.

**Analogy:** Profiling data is like a health check-up. Most people feel fine before a check-up. The doctor still measures blood pressure and temperature, because some problems have no symptoms until they are serious.

## Worked Example
This example is hypothetical [VERIFY]. Dr. Samira Haddad leads a small health-data team for a network of clinics near Irbid, Jordan. A report shows malaria cases twice as high as last season. Before anyone reacts, she profiles the `visits` table.

On-screen steps:

1. Open Python, connect to DuckDB and load the visits export.
2. Run `SUMMARIZE visits;` and point out the null percentage of `patient_id` and `temp_c`, and the maximum temperature of 73.0.
3. Run a targeted profile:

```sql
SELECT count(*)                            AS total_rows,
       count(*) - count(patient_id)        AS missing_patient,
       count(*) - count(temp_c)            AS missing_temp,
       count(*) - count(DISTINCT visit_id) AS duplicate_rows,
       count(*) FILTER (WHERE temp_c NOT BETWEEN 34 AND 43) AS temp_out_of_range
FROM visits;
```

On her 11 invented rows, DuckDB returned `11 | 1 | 1 | 3 | 1`.

4. Find the duplicates and compare the malaria count before and after:

```sql
SELECT count(*) FILTER (WHERE diagnosis = 'malaria')                  AS malaria_raw,
       count(DISTINCT visit_id) FILTER (WHERE diagnosis = 'malaria') AS malaria_real
FROM visits;
```

The result was `6 | 3`. Every malaria visit had been loaded twice, because a sync job ran again after a network error. The disease was not twice as common; the rows were.

Samira lists her issues in order of risk: (1) duplicated visits, which change the disease count; (2) the impossible temperature of 73.0, probably 37.3 typed wrongly; (3) one visit without a patient ID; (4) one missing temperature. She does not delete anything in the raw table. She writes the rules that staging and tests must enforce (L12).

## Common Mistake
Many learners only check whether a pipeline "ran successfully". A successful run tells you that the SQL was valid, not that the data is right. Another mistake is to fix problems by hand in a spreadsheet: the fix is lost the next time the data loads. Profile every new source, write down each problem, and turn each one into a rule in code.

## Key Takeaways
1. Six dimensions help you describe data quality: completeness, uniqueness, validity, consistency, timeliness and accuracy.
2. Bad data does not crash a model; it quietly teaches it the wrong thing, so you must profile data on purpose.
3. DuckDB's `SUMMARIZE` and targeted `count` queries find missing values, duplicates and out-of-range values quickly.

## Hands-on Exercise
**Task:** Profile a messy dataset with DuckDB: count missing values, duplicates and out-of-range values per column, and list your 5 most serious issues.
**Tools:** Python 3 with DuckDB (free); the course sample `raw.orders` from L03, or a public dataset such as a city open-data file [VERIFY].
**Steps:**
1. Load the dataset into DuckDB with all columns as text, as in L03.
2. Run `SUMMARIZE` on the table and note anything surprising.
3. Write one query that counts missing values in each important column.
4. Find duplicates with `GROUP BY` on the ID column and `HAVING count(*) > 1`.
5. Count values outside a sensible range or list, for example amounts below 0 or status values not in your expected list.
6. List your 5 most serious issues, and for each one write the dimension it belongs to and its likely effect on a model.
7. If you use a public dataset, check that it has no personal data, and do not paste rows into AI tools.
**What good looks like:** A short report with the queries, their real outputs and 5 ranked issues, each linked to a quality dimension and a possible effect on an AI use case. For the course sample, the list includes the duplicated order, the `TEST` row, the missing amount and the inconsistent status text.
**Time:** about 30 minutes

## Review Flags
- [VERIFY] The clinic duplicate-visit example is hypothetical and must stay presented as hypothetical; the figures come from invented sample data run in DuckDB 1.5.5.
- [VERIFY] Any public dataset suggested for the exercise: confirm its licence and current download location, and that it contains no personal data.
- [VERSION] DuckDB's `SUMMARIZE` output columns and the `FILTER` clause must be checked against the current DuckDB release.
