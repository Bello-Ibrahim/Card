# L07 Sources, Staging Models and ref() | Presenter Script

Course: AI-17 · Video: 5 min · Words: 692

## Hook
A column called amt in one table, Amount in another, and order value USD in a third. Dates stored as text. A test row someone forgot to delete. Every raw table has problems like these. The staging layer is where you fix them once, for everyone.

## Explain
Last time, you built a first dbt model that read the raw table directly. Today we organise the project properly, in layers. Each layer has one job, which makes the project easier to read and to change.

Sources are the raw tables, declared in a YAML file. dbt does not build them. It only reads them. Staging models come next: one model per source table. They rename columns to one style, cast types, trim spaces, and remove rows that are clearly not real data. Then intermediate and mart models join and aggregate them to answer questions.

Staging never joins, never aggregates, and never changes what the data means. It only makes the data consistent, so that every later model can trust the same clean columns.

Two functions connect the layers. The source function points to a declared raw table. The ref function points to another model. When you use them instead of writing table names, dbt builds a dependency graph. It knows which model must be built first, and it can draw the lineage graph. If the raw schema moves, you change one line in the YAML file, not every model.

Staging is like preparing ingredients before cooking. You wash the vegetables, peel them and cut them to the same size, but you do not decide on the dish yet. Because everything is prepared the same way, any cook can use it for any recipe.

## Demonstrate
Let's build a staging model. Sipho is a backend developer at an online craft marketplace in Durban, South Africa. His raw export is the course orders file, with a duplicated order, a test row, a missing amount, and one status written with a capital letter.

First, he creates a staging folder, and a sources file inside it. The file declares one source called raw, in the raw schema, with one table: orders.

Next, the staging model. It reads the source with the source function, and keeps only distinct rows. Then it casts the order ID to a whole number, the date to a real date, and the amount to a decimal, turning empty text into null.

It lowercases and trims the status, uppercases the country code, and removes the test customer. Notice the names: lowercase with underscores, the unit in the amount name, and a clear suffix for codes.

He deletes the first model from last lesson, because staging replaces it. Then he runs only the staging model, and the log shows success.

He queries the result. Seven rows from nine: the duplicate of order ten o seven and the test row are gone. Order ten o five now says delivered in lowercase. And order ten o six still has a null amount. Sipho keeps it, because a missing amount is a fact about the data, and a test will report it later.

From now on, later models never read the raw table directly. A mart starts from the staging model, using ref. So dbt always builds staging first.

A common mistake is to put business logic in staging, such as keeping only delivered orders. Then a team that needs cancelled orders writes its own copy of the cleaning rules. Keep every real row in staging. Business decisions belong in marts.

## Recap
Let's recap. First, declare raw tables as sources and read them with source, and read other models with ref, so dbt knows the build order. Second, build one staging model per source that renames, casts and cleans, without changing meaning. Third, remove only rows that are clearly not real data, such as exact duplicates and test rows.

## CTA
Now it is your turn. In the exercise, you will declare your raw orders table as a source, build your own staging model, and write down the row count before and after, with a reason for each removed row. It takes about thirty minutes. Next lesson: Building Marts and Feature Tables for AI.

## Thumbnail
Headline: Clean It Once
Image: Navy background, messy column names on the left flowing through a teal staging box into tidy lowercase names on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] dbt YAML source syntax, the source() and ref() functions and the default schema name for query results (main with dbt-duckdb) must be checked against the current dbt Core release and adapter.
- Screen output must match content.md: 7 rows from the 9 raw rows; order_id INTEGER, order_date DATE, amount_usd DECIMAL(10,2); order 1005 status 'delivered'; order 1006 amount NULL.
- Sipho and the craft marketplace in Durban, South Africa are fictional; the orders file is the course sample from L03.
