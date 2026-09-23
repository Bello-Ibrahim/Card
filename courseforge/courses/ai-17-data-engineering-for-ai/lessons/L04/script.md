# L04 Data Modelling: Tables, Keys and Star Schemas | Presenter Script

Course: AI-17 · Video: 5 min · Words: 693

## Hook
Two analysts ask the same question. How much did we sell last week? They get two different answers from the same database. Often the reason is not a bug in the SQL. It is that nobody agreed what one row means.

## Explain
Last time, you loaded raw data into PostgreSQL. Before we transform it, we need a design. Data modelling is the work that decides which tables exist, and how they connect.

Two terms first. A primary key is a column that identifies each row uniquely, such as a store key in a store table. A foreign key is a column that points to a primary key in another table, such as the same store key inside a sales table.

Analytical warehouses often use a star schema. In the centre is a fact table, which records events, such as sales, trips or payments. Around it are dimension tables, which describe the who, what, where and when of each event: products, stores, customers and dates.

Facts are long and narrow: many rows, mostly keys and numbers. Dimensions are short and wide: fewer rows, with many descriptive columns, such as a name, a category or a city.

The most important decision is the grain: what exactly one row of the fact table represents. One row per product per receipt is a clear grain. Sales data is not. When the grain is clear, everyone gets the same total. When it is unclear, people count things twice.

This matters for AI too. A feature table, which we build later in the course, comes from facts and dimensions. If the grain is wrong, a feature such as number of purchases is wrong, and the model learns from false counts.

Think of a library. The fact table is the loan register: one line for each book lent, with a borrower number, a book number and a date. The dimensions are the catalogue of books and the list of members.

## Demonstrate
Let's design one. Efua is a data analyst at a grocery chain with shops in Accra, Ghana, and Lagos, Nigeria. She designs a star schema for sales.

Her fact table is fact sales, and she writes its grain first: one row per product line on one receipt. It holds the receipt, the line number, keys for the date, store and product, and two measures, the quantity and the unit price.

Around it are three dimensions. The store dimension holds the name, city, country and currency. The product dimension holds the name and category. And the date dimension holds the week, the month and a public holiday flag.

The shops use two currencies, cedi and naira. So Efua's revenue query joins the fact table to stores and products, multiplies quantity by unit price, and groups by country, currency and category. It never adds the two currencies together.

On five invented sample lines, the query returns four rows. For example, staples in Ghana come to one hundred and ninety cedi, and staples in Nigeria to twenty-one thousand one hundred naira. A total across both countries would be meaningless without a documented exchange rate.

Efua also considers one wide table, with every store and product column repeated on every line. It is simpler to query, but a store name change would need millions of updates. She chooses the star schema.

A common mistake is to start with the report columns, and only later ask what a row means. Before you add any column, finish this sentence: one row in this table is one what? If you cannot finish it, the design is not ready.

## Recap
Let's recap. First, primary keys identify rows, and foreign keys connect a fact table to its dimensions. Second, in a star schema, fact tables hold events and numbers, and dimension tables describe them. Third, the grain is the most important modelling decision, because every count and every feature depends on it.

## CTA
Now it is your turn. In the exercise, you will design a star schema for an online bookshop: a fact table with a one sentence grain, three dimensions, and the keys that join them. It takes about twenty-five minutes. Next lesson: DuckDB, fast analytics on your laptop.

## Thumbnail
Headline: What Is One Row?
Image: Navy background, a star schema with a teal fact table in the centre and four dimension tables around it, headline in teal Inter Bold.

## Production Notes
- No facts to verify: content.md Review Flags are None; the grocery chain and its figures are hypothetical and the SQL was tested in DuckDB on invented sample data.
- Show the revenue query on the code slide exactly as in content.md; the voiceover describes it and does not read it.
- Sample output rows must match content.md: four rows, for example Ghana | GHS | Staples | 190.00 and Nigeria | NGN | Staples | 21100.00.
- Efua and the grocery chain in Accra and Lagos are fictional; stock footage must show no real store names or logos.
