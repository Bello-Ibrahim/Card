# L05 DuckDB: Fast Analytics on Your Laptop | Presenter Script

Course: AI-17 · Video: 5 min · Words: 685

## Hook
What if you could run warehouse-style SQL on a file of millions of rows, on your laptop, with no server to install? DuckDB does exactly that. And it often finishes before you look away from the screen.

## Explain
Last time, we designed tables with keys and a clear grain. Today we meet the second database in this course. DuckDB is a free, open-source, in-process analytical database.

In-process means it runs inside your Python program, or its own command-line tool. There is no server, no user accounts and no network connection. You install it with one pip command, and query CSV and Parquet files directly, as if they were tables.

Two ideas explain why it is fast. The first is column storage. A normal row database stores each row together, which is great for updating one customer at a time. But a query such as average energy per meter needs only two columns, and a row store must still read every column. DuckDB works column by column, so it reads only what the query needs.

The second idea is Parquet, an open, column-based file format. It stores data types, compresses each column and keeps summary statistics. So it is usually much smaller than the same data as CSV, and faster to read. CSV is plain text, so every query must read every character again.

Picture a long shopping receipt. To find the total spent on fruit, you must read every item. A Parquet file is like a spreadsheet already sorted into columns, with a subtotal at the bottom of each one. You jump straight to the column you need.

So when should you choose each database? Choose DuckDB when one person or one pipeline analyses files locally, and when you build datasets, such as Parquet files for machine learning. Choose PostgreSQL when many users read and write at the same time, and you need a server that is always running. In this course, the capstone can use either one.

## Demonstrate
Let's measure the difference. Hiroshi is a backend developer at an electricity retailer in Osaka, Japan. He wants the average use per smart meter. He uses generated data, so no customer data appears.

In a terminal, he installs DuckDB, and opens a new Python file called compare.

First, the script connects to DuckDB, and generates two million meter readings for five thousand meters. It writes them to a CSV file, then copies the same data into a Parquet file.

Then, for each file, it runs the same query, the average reading per meter, and prints the file size in megabytes and the time the query took.

He runs the script. On our four-core test machine, the CSV file is twenty-eight point eight megabytes, and the query takes about a tenth of a second. The Parquet file is only five point nine megabytes, and the query takes nine thousandths of a second.

Same two million rows, about five times smaller, and more than ten times faster. Your exact numbers will differ with your hardware and DuckDB version. Hiroshi stores monthly exports as Parquet, and keeps PostgreSQL for the customer portal.

Two common mistakes. DuckDB is not a replacement for every database. It is not built for a web app where hundreds of users write small updates. And do not trust a single timing run. Run each query two or three times, and compare the typical result.

## Recap
Let's recap. First, DuckDB is an in-process analytical database that queries CSV and Parquet files directly. Second, column storage and Parquet make analytical queries faster and files smaller. Third, choose DuckDB for local analysis and building datasets, and a server database such as PostgreSQL for shared, always-on work.

## CTA
Now it is your turn. In the exercise, you will run this comparison yourself three times, try a different column, and write two sentences on file size and query time. You can use the script from this video, or the orders file from lesson three. It takes about twenty-five minutes. Next week we start transforming data, with dbt Core: Project Setup and First Model.

## Thumbnail
Headline: CSV or Parquet?
Image: Navy background, a laptop with two file icons side by side, a large CSV and a much smaller teal Parquet file, headline in teal Inter Bold.

## Production Notes
- [VERSION] DuckDB's Python package interface (duckdb.connect, con.sql, COPY ... (FORMAT parquet)) and file-format support must be checked against the current release; the script was tested with DuckDB 1.5.5 and Python 3.
- [VERIFY] Any public CSV dataset suggested for the exercise: the voiceover names none; confirm licence and download location before showing one on screen.
- Screen output must match content.md exactly: readings.csv 28.8 MB 0.121 s and readings.parquet 5.9 MB 0.009 s. Sizes and timings are machine-specific; the voiceover says 'on our machine'. If a re-recording gives different timings, show the content.md output as a still or re-test and update content.md first.
- Hiroshi and the electricity retailer in Osaka are fictional; the data is generated, so no customer data appears on screen.
