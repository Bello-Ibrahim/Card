# L05 DuckDB: Fast Analytics on Your Laptop

Course: AI-17 · Module: M1 · Objectives: O3, O6 · Video: 5 min (screen demo)

## Hook
What if you could run warehouse-style SQL on a file of millions of rows, on your laptop, with no server to install? DuckDB does exactly that, and it often turns a slow analysis into one that finishes before you look away from the screen.

## Explanation
DuckDB is a free, open-source **in-process** analytical database. "In-process" means it runs inside your Python program or its own command-line tool. There is no server, no user accounts and no network connection. You install it with `pip install duckdb` [VERSION] and query CSV and Parquet files directly, as if they were tables.

Two ideas explain why it is fast for analytics:

- **Column storage.** A normal row database stores each row together. An analytical query such as "average energy per meter" reads only two columns, but a row store must read every column. DuckDB stores and processes data column by column, so it reads only what the query needs.
- **Parquet files.** Parquet is an open, column-based file format. It stores data types, compresses each column and keeps summary statistics, so it is usually much smaller than the same data as CSV and faster to read. CSV is plain text: every query must parse every character again.

When should you choose each database?

| Choose DuckDB when... | Choose PostgreSQL when... |
|---|---|
| One person or one pipeline analyses files locally | Many users or applications read and write at the same time |
| You want fast aggregations on large files | You need a server that is always running |
| You build and export datasets (for example Parquet for ML) | You need user permissions and many small updates |

In this course both are valid: the capstone can use either one.

**Analogy:** A CSV file is like a shopping receipt printed as one long line of text: to find the total spent on fruit, you must read every item. A Parquet file is like a spreadsheet already sorted into columns, with a subtotal at the bottom of each one. You jump straight to the column you need.

## Worked Example
Hiroshi is a backend developer at a hypothetical electricity retailer in Osaka, Japan. He wants the average consumption per smart meter from a large export. He demonstrates the difference between CSV and Parquet with generated data, so no customer data is used.

On-screen steps:

1. In a terminal, run `pip install duckdb`, then open a new file `compare.py`.
2. Type the script:

```python
import duckdb, os, time

con = duckdb.connect()
con.sql("""COPY (SELECT i % 5000 AS meter_id, i // 5000 AS slot,
                        round(random() * 2, 3) AS kwh
                 FROM range(2000000) t(i))
           TO 'readings.csv' (HEADER)""")
con.sql("COPY (SELECT * FROM 'readings.csv') TO 'readings.parquet' (FORMAT parquet)")

for f in ["readings.csv", "readings.parquet"]:
    start = time.perf_counter()
    con.sql(f"SELECT meter_id, avg(kwh) FROM '{f}' GROUP BY meter_id").fetchall()
    secs = time.perf_counter() - start
    print(f, round(os.path.getsize(f) / 1e6, 1), "MB", round(secs, 3), "s")
```

3. Run `python compare.py`. On our 4-core test machine it printed:

```text
readings.csv 28.8 MB 0.121 s
readings.parquet 5.9 MB 0.009 s
```

4. Point out on screen: the same 2 million rows, about five times smaller as Parquet, and the query more than ten times faster. Your exact numbers will differ with your hardware and DuckDB version.

Hiroshi decides to store the monthly exports as Parquet and to keep PostgreSQL for the customer portal, where many users update their details at the same time.

## Common Mistake
Many learners think DuckDB is a replacement for every database. It is designed for analytics by one process at a time, not for a web application where hundreds of users write small updates. Another mistake is to compare timings from a single run: the first run may include file caching. Run each query two or three times and compare the typical result.

## Key Takeaways
1. DuckDB is an in-process analytical database that queries CSV and Parquet files directly from Python or its command line.
2. Column storage and the Parquet format make analytical queries faster and files smaller than row-by-row CSV.
3. Choose DuckDB for local analysis and dataset building, and a server database such as PostgreSQL for shared, always-on, multi-user work.

## Hands-on Exercise
**Task:** Query the same dataset as CSV and as Parquet with DuckDB from Python, compare the file sizes and query times, and write two sentences on what you found.
**Tools:** Python 3, the `duckdb` package (free), a terminal or a Jupyter notebook.
**Steps:**
1. Install DuckDB with `pip install duckdb`.
2. Copy the script from the worked example, or point it at `orders.csv` from L03 plus a larger public CSV of your choice [VERIFY].
3. Run the script three times and record the size and time for each file.
4. Change the query to use a different column, for example `max(kwh)`, and run it again.
5. Write two sentences: one on file size, one on query time, with your numbers.
**What good looks like:** A small table of three runs per format, with Parquet clearly smaller and faster, and two sentences that explain the result with column storage and compression.
**Time:** about 25 minutes

## Review Flags
- [VERSION] DuckDB's Python package interface (`duckdb.connect`, `con.sql`, `COPY ... (FORMAT parquet)`) and file-format support must be checked against the current release; the script was tested with DuckDB 1.5.5 and Python 3.
- [VERIFY] Any public CSV dataset suggested for the exercise: confirm its licence and current download location before naming it.
