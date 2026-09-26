# L11 What Makes Data Bad? | Presenter Script

Course: AI-17 · Video: 5 min · Words: 651

## Hook
Bad data rarely crashes anything. The pipeline finishes. The dashboard loads. The model trains. It simply learns the wrong thing, and nobody notices until a decision based on it goes wrong.

## Explain
Welcome to week three, on data quality and orchestration. You can now build models in layers. But how do you know the data inside them is good? It helps to break quality into six dimensions.

Completeness asks: are required values present? Uniqueness asks: is each real event recorded once? Validity asks: do values follow the rules for their type and range, so no body temperature of seventy-three degrees? And consistency asks: do related values agree, so no delivery before the order was placed?

Timeliness asks: is the data recent enough, or has yesterday's file not arrived? And accuracy asks: does the value match reality? The first five can usually be checked with SQL. Accuracy often needs another trusted source, or a human check.

For AI, each problem has a specific effect. Duplicates make some events look more common. Missing values in one group make the model less reliable for that group. Invalid values stretch averages and scales. None of these produce an error message.

So you must look for problems on purpose. This is called profiling: counting missing values, duplicates and out-of-range values per column, before you trust a dataset. DuckDB is a good tool for it. Its summarize command describes every column in one step, and targeted queries count exactly what you care about.

Profiling is like a health check-up. Most people feel fine before one. The doctor still measures blood pressure, because some problems have no symptoms until they are serious.

## Demonstrate
Here is an invented example. Doctor Samira Haddad leads a small health data team for a network of clinics near Irbid, Jordan. A report shows malaria cases twice as high as last season. Before anyone reacts, she profiles the visits table.

She opens Python, connects to DuckDB, and loads the visits export. Then she runs summarize. Two columns have missing values, the patient ID and the temperature. And the maximum temperature is seventy-three, which is impossible.

Next, a targeted profile in one query. It counts the total rows, the missing patient IDs, the missing temperatures, the extra rows beyond distinct visit IDs, and the temperatures outside a normal human range. On her eleven invented rows, it returns eleven, one, one, three and one.

Three duplicate rows. So she compares the malaria count before and after removing duplicates. The raw count is six. The real count, by distinct visit, is three.

Every malaria visit had been loaded twice, because a sync job ran again after a network error. The disease was not twice as common. The rows were.

Samira lists her issues in order of risk. First, the duplicated visits, which change the disease count. Second, the impossible temperature, probably thirty-seven point three typed wrongly. Third, a visit without a patient ID. Fourth, a missing temperature. She deletes nothing in the raw table. Instead, she writes rules that staging and tests must enforce.

A common mistake is to check only that the pipeline ran successfully. That tells you the SQL was valid, not that the data is right. Profile every new source, and turn each problem into a rule in code.

## Recap
Let's recap. First, six dimensions describe data quality: completeness, uniqueness, validity, consistency, timeliness and accuracy. Second, bad data does not crash a model. It quietly teaches it the wrong thing, so profile data on purpose. Third, DuckDB's summarize and targeted count queries find missing values, duplicates and out-of-range values quickly.

## CTA
Now it is your turn. In the exercise, you will profile the course orders table with DuckDB, count missing values, duplicates and out-of-range values, and list your five most serious issues, with the dimension of each. It takes about thirty minutes. Next lesson: Testing Data with dbt.

## Thumbnail
Headline: Bad Data Never Crashes
Image: Navy background, a green 'run successful' tick next to a data table with hidden red duplicate rows, headline in teal Inter Bold.

## Production Notes
- [VERIFY] The clinic duplicate-visit example is hypothetical and must stay presented as hypothetical: the voiceover says 'an invented example' and the stock and screen visuals must not show a real clinic, logo or patient. Figures come from invented sample data run in DuckDB 1.5.5.
- [VERIFY] Any public dataset suggested for the exercise: the voiceover names none; confirm licence, download location and that it holds no personal data before showing one.
- [VERSION] DuckDB's SUMMARIZE output columns and the FILTER clause must be checked against the current DuckDB release.
- Screen output must match content.md exactly: the profile query returns 11 | 1 | 1 | 3 | 1, the malaria query returns 6 | 3, and SUMMARIZE shows a maximum temp_c of 73.0.
- Dr. Samira Haddad and the clinics near Irbid, Jordan are fictional.
