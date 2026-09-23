# L04 Data Modelling: Tables, Keys and Star Schemas

Course: AI-17 · Module: M1 · Objectives: O2, O6 · Video: 5 min

## Hook
Two analysts ask the same question, "How much did we sell last week?", and get two different answers from the same database. Often the reason is not a bug in the SQL. It is that nobody agreed what one row in the table means.

## Explanation
You already know tables and joins from basic SQL. Data modelling is the design work that decides which tables exist and how they connect.

- A **primary key** is a column (or set of columns) that identifies each row uniquely, such as `store_key`.
- A **foreign key** is a column that points to a primary key in another table, such as `store_key` in a sales table.

Analytical warehouses often use a **star schema**. In the centre is a **fact table**, which records events or measurements: sales, trips, payments. Around it are **dimension tables**, which describe the "who, what, where and when" of each event: products, stores, customers, dates. Diagrams of this shape look like a star.

- Facts are long and narrow: many rows, mostly keys and numbers (quantity, price).
- Dimensions are short and wide: fewer rows, many descriptive columns (name, category, city).

The most important decision is the **grain**: what exactly one row of the fact table represents. "One row per product per receipt" is a clear grain. "Sales data" is not. When the grain is clear, every total is easy to calculate, and everyone gets the same answer. When it is unclear, people double count or mix levels, such as daily totals and single receipts in one table.

Why does this matter for AI? A feature table (L08) is built from facts and dimensions. If the grain is wrong, features such as "number of purchases" are wrong too, and the model learns from false counts.

**Analogy:** A star schema is like a library. The fact table is the loan register: one line for each book lent, with a borrower number, a book number and a date. The dimension tables are the catalogue of books and the list of members. The register stays short per line because the details live in the catalogue.

## Worked Example
Efua is a data analyst at a hypothetical grocery chain with shops in Accra, Ghana, and Lagos, Nigeria. She designs a star schema for sales:

- `fact_sales`, grain: **one row per product line on one receipt**. Columns: `receipt_id`, `line_no`, `date_key`, `store_key`, `product_key`, `quantity`, `unit_price`.
- `dim_store`: `store_key` (primary key), `store_name`, `city`, `country`, `currency`.
- `dim_product`: `product_key`, `product_name`, `category`.
- `dim_date`: `date_key`, `date`, `week`, `month`, `is_public_holiday`.

The shops use two currencies, cedi (GHS) and naira (NGN), so Efua keeps `currency` in `dim_store` and never adds the two together. Her revenue query groups by currency:

```sql
SELECT s.country, s.currency, p.category,
       sum(f.quantity * f.unit_price) AS revenue
FROM fact_sales AS f
JOIN dim_store   AS s ON f.store_key   = s.store_key
JOIN dim_product AS p ON f.product_key = p.product_key
GROUP BY s.country, s.currency, p.category
ORDER BY s.country, p.category;
```

On five invented sample lines, DuckDB returned four rows, for example `Ghana | GHS | Staples | 190.00` and `Nigeria | NGN | Staples | 21100.00`. A total across both countries would be meaningless until the amounts are converted to one currency with a documented rate.

Efua also considers a second design: one wide table with every product and store column repeated on every sales line. It is simpler to query, but a store name change would need millions of updates. She chooses the star schema and writes the grain at the top of her design document.

## Common Mistake
Many learners start with the columns they want in a report and only later ask what a row means. They end up with a table where some rows are receipts and some are receipt lines, and totals are counted twice. Write the grain as one sentence before you add any column: "One row in this table is one ...". If you cannot finish the sentence, the design is not ready.

## Key Takeaways
1. Primary keys identify rows; foreign keys connect a fact table to its dimension tables.
2. In a star schema, fact tables hold events and numbers, and dimension tables describe them.
3. Choosing the grain, meaning what one fact row represents, is the most important modelling decision, because every count and feature depends on it.

## Hands-on Exercise
**Task:** Design a star schema for an online bookshop: name the fact table and its grain, 3 dimension tables, and the keys that join them.
**Tools:** Pen and paper, or draw.io (diagrams.net, free).
**Steps:**
1. Write the business question the schema must answer, for example "Which book categories sell best in each country each month?"
2. Name the fact table and write its grain in one sentence.
3. List the fact table's columns: foreign keys and numeric measures (quantity, price, discount).
4. Design 3 dimension tables, for example `dim_book`, `dim_customer` and `dim_date`, each with a primary key and 3 to 5 descriptive columns.
5. Draw lines from each foreign key in the fact table to its dimension.
6. Write one sentence on a design choice, such as where currency or discount lives, and why.
7. Use invented example values only; do not use real customer details.
**What good looks like:** A clear star diagram with one fact table, a one-sentence grain (for example "one row per book per order"), 3 dimensions with primary keys, correct joins and one justified design choice.
**Time:** about 25 minutes

## Review Flags
- None. The grocery chain and its figures are hypothetical, and the SQL was tested in DuckDB on invented sample data.
