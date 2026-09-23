# L03 Setting Up PostgreSQL and Loading Raw Data | Presenter Script

Course: AI-17 · Video: 5 min · Words: 680

## Hook
The first rule of an ELT pipeline sounds strange. When data arrives, do not fix it. Load it exactly as it came, errors included. Today you will set up PostgreSQL, and learn why that rule saves you later.

## Explain
In the last lesson, we chose ELT: load first, transform later. Now we build the load step. PostgreSQL is a free, open-source relational database, and in this course it plays the role of a small warehouse.

You can run it in two ways. With Docker, one command starts PostgreSQL in a container. It works the same on Windows, macOS and Linux, and is easy to delete later. Or you can use a native installer, which needs no Docker, but the steps differ by system and release.

Inside the database, a schema is a named folder for tables. We create a schema called raw, and put every source table there, unchanged. Later layers, such as staging and marts, go in other schemas.

Why keep raw data exactly as it arrived? First, rebuilds. If a cleaning rule is wrong, you fix the rule and run it again. You never need a new copy from the source. Second, evidence. When a number looks wrong, you can prove whether the problem was in the source or in your pipeline.

Third, safety. If every column is loaded as text, a strange value, such as two dots meaning no data, never makes the load fail. You deal with it later, in the staging layer.

Think of an accountant who keeps the original receipts in a box. She makes clean spreadsheets from them, but never writes on the receipts. If a total is wrong, the receipts show what really happened.

## Demonstrate
Let's load some data. Mariana is a data analyst at a rural development charity in Cusco, Peru. She has a small file of development indicators for Andean countries, with five rows. Notice two of them: one value is empty, and one is two dots, a placeholder for no data.

First, in a terminal, she starts PostgreSQL in Docker with one command. It gives the container a name, sets a password and opens the usual port.

Next, she copies the file into the container, and opens the SQL shell.

Now she creates the raw schema, and a raw table with four columns. Every column is text, even the year and the value. That is on purpose. A numeric column would reject the two dots, and the whole load would stop. Then she loads the file with the copy command, telling it that the file is CSV with a header row.

After every load, check two things. She counts the rows, and gets five, the same number as in the file. Then she asks the information schema for each column's data type. Every column shows text.

Mariana writes both problems in her notes: the empty value, which PostgreSQL stores as null, and the two dots. She does not change them in the raw table. A staging model will convert the dots to null later.

A common mistake is to set strict types in the raw table, such as a numeric value column, or to clean the file in a spreadsheet first. Then the load fails on the dots, or the spreadsheet silently changes dates and leading zeros. Type conversion is a transformation, and it belongs in staging.

## Recap
Let's recap. First, PostgreSQL can run in Docker or from a native installer, and a raw schema holds source data exactly as it arrived. Second, loading every raw column as text means strange values never stop the load. Third, after every load, check the row count and the column types, and write down any problems you see.

## CTA
Now it is your turn. In the exercise, you will load the course orders file into a raw table, expect nine rows, and list at least four problems without changing anything. Look for an empty amount, a duplicated order, a test row and a capital letter where it should not be. It takes about thirty minutes. Next lesson: Data Modelling, with tables, keys and star schemas.

## Thumbnail
Headline: Load It. Don't Fix It.
Image: Navy background, a CSV file icon dropping unchanged into a teal box labelled raw, headline in teal Inter Bold.

## Production Notes
- [VERSION] PostgreSQL installation steps (Docker image tag postgres:17, native installers) and default settings differ by operating system and release; check the docker run, docker cp and psql commands against the current release before recording.
- [VERIFY] World Bank development indicators: the voiceover does not name the dataset; confirm licence and download location before showing it on screen.
- Screen output must match content.md: count 5 in PostgreSQL, every column type text. The note that DuckDB shows VARCHAR stays in the lesson page, not in the voiceover.
- Mariana and the charity in Cusco, Peru are fictional; the indicator values in indicators.csv are invented for teaching.
- The password course_pw is for a local teaching container only; show it on screen as in content.md.
