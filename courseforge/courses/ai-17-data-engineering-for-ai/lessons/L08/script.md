# L08 Building Marts and Feature Tables for AI | Presenter Script

Course: AI-17 · Video: 5 min · Words: 686

## Hook
A churn model gets an excellent score in testing, and fails in its first month of real use. The data was clean. The code had no bugs. The problem was one column. It quietly used information from after the date it was meant to predict.

## Explain
Last time, you cleaned raw data in a staging model. Now we build the final layer. Marts join and aggregate staging models into tables that answer a business question, such as revenue per store per month. A mart has a clear grain, and a name that says what it holds.

A feature table is a special mart for machine learning. It has one row per entity at a given date, such as one row per customer on the first of March. And it has feature columns that describe the entity, such as purchases in the last ninety days, or days since the last login.

It also has a feature date, sometimes called a cut-off date. That is the moment the prediction would be made. And it often has a label, the thing to predict, calculated from events after that date.

The golden rule is simple. Features may only use data from before the feature date. If a feature uses later events, the model learns from the future. This is called data leakage. Test results look excellent, and real results are poor, because in real use the future is not available.

Keep the feature date in one place, not repeated in every model. dbt variables do this. You define the feature date once in the project file, and read it wherever you need it.

Think of a student preparing for an exam, using only lessons taught before the exam date. If the practice test includes the real exam answers, the practice score is perfect. But it tells you nothing about how the student will really do.

## Demonstrate
Let's build one. Juliana is a data engineer at a prepaid mobile network in Recife, Brazil. The data science team wants to predict which customers will stop recharging in March. Her staging model has one row per recharge, with the customer, the date and the amount.

First, she adds a variable to the project file. The feature date is the first of March, twenty twenty-six.

Next, she creates the feature model in the marts folder. For each customer, it counts recharges, adds up the spend, finds the last recharge date, and works out the days since that recharge.

The most important part is the filter. It keeps only recharges before the feature date, and within the ninety days before it. Both limits come from the same variable.

She runs the model and queries the table. On eight invented recharges, it returns three rows, one per customer. Customer M one recharged three times, spent seventy reais, and last recharged nine days before the feature date.

But M one also recharged on the fifth of March, and M three on the tenth. Without the date filter, those recharges would enter the features, and recharged recently would perfectly predict did not churn. That is leakage. Juliana writes the feature date and window next to each column, so the data scientists know what each value means.

A common mistake is to build features from the whole table, because more data seems better. For every feature, ask one question. Would I know this value on the feature date? If not, filter the rows by date first.

## Recap
Let's recap. First, marts join and aggregate staging models, and a feature table is a mart with one row per entity at a feature date. Second, features may only use data from before that date, and using later data is leakage. Third, store the feature date once, as a dbt variable, and document the date and window for every feature.

## CTA
Now it is your turn. In the exercise, you will build a feature table from your staged orders, with one row per customer and at least four features, and a small table of the date each one is based on. It takes about thirty-five minutes. Next lesson: Incremental Models and Changing Data.

## Thumbnail
Headline: Don't Leak the Future
Image: Navy background, a timeline with a teal feature-date line; data points after the line are crossed out in red, headline in teal Inter Bold.

## Production Notes
- [VERSION] dbt vars syntax in dbt_project.yml and date arithmetic (date - date, interval '90 days') must be checked for the chosen adapter; the SQL was tested in DuckDB 1.5.5.
- Screen output must match content.md exactly: three rows, M01 | 2026-03-01 | 3 | 70.0 | 2026-02-20 | 9; M02 | 2026-03-01 | 1 | 10.0 | 2026-01-02 | 58; M03 | 2026-03-01 | 1 | 50.0 | 2026-02-27 | 2.
- Juliana and the prepaid mobile network in Recife, Brazil are fictional; the eight recharges are invented.
