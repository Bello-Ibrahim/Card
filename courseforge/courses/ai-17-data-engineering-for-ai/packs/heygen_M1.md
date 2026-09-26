# HeyGen Batch Pack: AI-17 M1 (Data Pipelines and Storage Foundations)

Course: Data Engineering for AI. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L01 What Data Engineers Do for AI

- **Filename:** `ai-17-data-engineering-for-ai_M1_L01_presenter.mp4`
- **Expected length:** about 5.3 minutes (735 words). The quality gate accepts ±10%.

```text
A team spends two days training a model, and two months getting the data ready for it. That is not bad planning. In most AI projects, preparing the data is the biggest part of the work. And that part belongs to data engineers.

Hi, and welcome to Data Engineering for AI. In this first lesson, we look at what data engineers actually do, and why AI depends on their work.

Data engineering is the work of moving data from the places where it is created to the places where it is used, in a form that people and systems can trust.

Every data system has four roles. Sources are where data is created, such as an app database, a payment service or a sensor. Pipelines are the automated steps that copy, clean, join and reshape the data. Storage is where data lives between steps, in a data warehouse or a data lake, which we compare next time. And consumers are the people and systems that use the result.

When the consumer is an AI model, the stakes are higher. A model learns whatever patterns the data contains, including mistakes. If a pipeline sends duplicated rows, the model learns that some events happen twice as often as they really do. If future information slips into the training data, the model looks excellent in testing, and then fails in real use.

So a good pipeline for AI has four qualities. It is reliable: it runs on time, and when it fails, someone knows. It is repeatable: running it again gives the same result. It is tested: automatic checks catch bad values before anyone sees them. And it is documented: anyone can see where each column comes from.

In this course, you build all four with free tools. PostgreSQL and DuckDB for storage, dbt Core for transformations and tests, and Apache Airflow for scheduling.

Here is a simple way to picture it. A data pipeline is like a water treatment plant. River water arrives full of mud and leaves. The plant filters it, treats it and tests it in fixed stages, then sends safe water to every tap, every day.

When the plant works well, nobody notices it. When it fails, everybody downstream notices at once. Good data engineering works the same way.

Let's see this in practice. Tomás is a backend developer at a crop insurance start-up in Córdoba, Argentina. The data science team wants a model that predicts which farms will make a drought claim next season. They ask him for a table of farms with their history.

Before writing any code, Tomás maps the flow. His sources are the policy database, the claims system, daily rainfall files from a weather provider, and field visit notes typed by agents. A nightly pipeline copies, cleans and joins them by farm and date.

Raw copies are kept unchanged, and the cleaned tables feed a final table with one row per farm per season. Three consumers use it: the data science team, the finance team, and a dashboard for regional managers.

The map shows two risks early. First, the rainfall files use weather station codes, not farm IDs. So Tomás needs a lookup table that links each farm to its nearest station.

Second, field visit notes are sometimes written after a claim is paid. If those notes enter the training data, the model will see the answer. So Tomás writes both risks next to the map, and agrees with the data scientists which date each column is based on.

A common mistake is to treat data engineering as a one-time job. In practice, new rows arrive every day, the model is retrained, and sources change their format without warning. Treat every data flow as a system that runs again and again.

Let's recap. First, every data system has sources, pipelines, storage and consumers, and mapping them is your first step. Second, AI models learn from whatever the data contains, so duplicated, missing or future information quietly makes a worse model. Third, a good pipeline for AI is reliable, repeatable, tested and documented, not only fast.

Now it is your turn. In the exercise below this video, you will map the data flow of a ride-hailing app in Jakarta, with four sources, its storage, three consumers and one data risk. It takes about twenty minutes. In the next lesson, we look at ETL, ELT, batch and streaming. See you there.
```

## L02 ETL, ELT, Batch and Streaming

- **Filename:** `ai-17-data-engineering-for-ai_M1_L02_presenter.mp4`
- **Expected length:** about 5.1 minutes (712 words). The quality gate accepts ±10%.

```text
Two pipelines deliver the same sales data. One transforms it before it reaches the warehouse. The other loads it first and transforms it later. Both work. So why does most modern analytics work, including this course, choose the second one?

In the last lesson, we mapped sources, pipelines, storage and consumers. Today we look at two choices every pipeline makes: when to transform the data, and how often to move it.

ETL means extract, transform, load. Data is taken from a source, cleaned and reshaped on a separate server, and only the finished result is loaded into the warehouse. ETL was common when warehouse storage and computing were expensive, so teams stored only what they needed.

ELT means extract, load, transform. Raw data is loaded into the warehouse first, exactly as it arrived, and then transformed there with SQL.

ELT has three advantages for AI work. You keep the raw data, so you can rebuild any table when a rule changes. Transformations are SQL that people can read, review and test. And a new feature for a model can be built from data that is already loaded. This course uses ELT, with PostgreSQL or DuckDB for loading, and dbt Core for transforming.

The second choice is timing. A batch pipeline processes a group of records on a schedule, for example every night at two in the morning. A streaming pipeline processes each event within seconds of its arrival.

Streaming is useful when a late answer has no value, such as blocking a fraudulent card payment. But it needs more infrastructure and is harder to test. Most AI training data is prepared in batches, because a model retrained every day or week does not need second by second updates. In this course, all hands-on work is batch, and streaming is a concept only.

Finally, where does the data live? A data warehouse stores structured tables for SQL analytics. A data lake stores files of any type, such as CSV, Parquet, JSON, images or logs, in cheap storage. Many teams use both: raw files land in a lake, and cleaned tables live in a warehouse.

Here is a picture to remember. ETL is a central kitchen that delivers only finished plates. If a customer wants a change, the kitchen starts again. ELT delivers fresh ingredients to a kitchen in each restaurant, where cooks can prepare new dishes whenever they need them.

And batch is the daily delivery truck, while streaming is a conveyor belt that never stops.

Let's apply this. Aigerim is a data analyst at a logistics company in Almaty, Kazakhstan. She reviews three data needs.

First, a weekly model that predicts parcel volume per depot. The model retrains once a week, so she chooses batch and ELT. Second, an alert when a refrigerated truck goes above eight degrees. A warning two hours late could mean spoiled goods, so that one is streaming. Third, a monthly on-time delivery report. Batch and ELT are enough.

For the parcel volume model, ELT really helps. Last month, the team changed the rule for delivered, to exclude parcels left with a neighbour. Because the raw scan data was already in the warehouse, Aigerim changed one SQL model and rebuilt two years of history in one run. With ETL, she would have needed a new extract from the source system.

A common mistake is to believe streaming is always better, because real time sounds faster. Speed has a cost: more parts, harder testing and harder recovery. Ask one question first. If this answer arrives one hour later, does anyone lose value? If not, choose batch.

Let's recap. First, ETL transforms data before loading it, while ELT loads raw data first and transforms it inside the warehouse, which keeps raw data for rebuilds. Second, batch runs on a schedule, and streaming processes events as they arrive, which is only worth it when minutes matter. Third, warehouses hold structured tables, lakes hold raw files, and many teams use both.

Now try it yourself. In the exercise below this video, you will label six scenarios as batch or streaming, from nightly sales reports in Kenya to card fraud alerts in Brazil, and explain one choice. It takes about fifteen minutes. Next, we get hands-on: Setting Up PostgreSQL and Loading Raw Data.
```

## L03 Setting Up PostgreSQL and Loading Raw Data

- **Filename:** `ai-17-data-engineering-for-ai_M1_L03_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
The first rule of an ELT pipeline sounds strange. When data arrives, do not fix it. Load it exactly as it came, errors included. Today you will set up PostgreSQL, and learn why that rule saves you later.

In the last lesson, we chose ELT: load first, transform later. Now we build the load step. PostgreSQL is a free, open-source relational database, and in this course it plays the role of a small warehouse.

You can run it in two ways. With Docker, one command starts PostgreSQL in a container. It works the same on Windows, macOS and Linux, and is easy to delete later. Or you can use a native installer, which needs no Docker, but the steps differ by system and release.

Inside the database, a schema is a named folder for tables. We create a schema called raw, and put every source table there, unchanged. Later layers, such as staging and marts, go in other schemas.

Why keep raw data exactly as it arrived? First, rebuilds. If a cleaning rule is wrong, you fix the rule and run it again. You never need a new copy from the source. Second, evidence. When a number looks wrong, you can prove whether the problem was in the source or in your pipeline.

Third, safety. If every column is loaded as text, a strange value, such as two dots meaning no data, never makes the load fail. You deal with it later, in the staging layer.

Think of an accountant who keeps the original receipts in a box. She makes clean spreadsheets from them, but never writes on the receipts. If a total is wrong, the receipts show what really happened.

Let's load some data. Mariana is a data analyst at a rural development charity in Cusco, Peru. She has a small file of development indicators for Andean countries, with five rows. Notice two of them: one value is empty, and one is two dots, a placeholder for no data.

First, in a terminal, she starts PostgreSQL in Docker with one command. It gives the container a name, sets a password and opens the usual port.

Next, she copies the file into the container, and opens the SQL shell.

Now she creates the raw schema, and a raw table with four columns. Every column is text, even the year and the value. That is on purpose. A numeric column would reject the two dots, and the whole load would stop. Then she loads the file with the copy command, telling it that the file is CSV with a header row.

After every load, check two things. She counts the rows, and gets five, the same number as in the file. Then she asks the information schema for each column's data type. Every column shows text.

Mariana writes both problems in her notes: the empty value, which PostgreSQL stores as null, and the two dots. She does not change them in the raw table. A staging model will convert the dots to null later.

A common mistake is to set strict types in the raw table, such as a numeric value column, or to clean the file in a spreadsheet first. Then the load fails on the dots, or the spreadsheet silently changes dates and leading zeros. Type conversion is a transformation, and it belongs in staging.

Let's recap. First, PostgreSQL can run in Docker or from a native installer, and a raw schema holds source data exactly as it arrived. Second, loading every raw column as text means strange values never stop the load. Third, after every load, check the row count and the column types, and write down any problems you see.

Now it is your turn. In the exercise, you will load the course orders file into a raw table, expect nine rows, and list at least four problems without changing anything. Look for an empty amount, a duplicated order, a test row and a capital letter where it should not be. It takes about thirty minutes. Next lesson: Data Modelling, with tables, keys and star schemas.
```

## L04 Data Modelling: Tables, Keys and Star Schemas

- **Filename:** `ai-17-data-engineering-for-ai_M1_L04_presenter.mp4`
- **Expected length:** about 5.0 minutes (691 words). The quality gate accepts ±10%.

```text
Two analysts ask the same question. How much did we sell last week? They get two different answers from the same database. Often the reason is not a bug in the SQL. It is that nobody agreed what one row means.

Last time, you loaded raw data into PostgreSQL. Before we transform it, we need a design. Data modelling is the work that decides which tables exist, and how they connect.

Two terms first. A primary key is a column that identifies each row uniquely, such as a store key in a store table. A foreign key is a column that points to a primary key in another table, such as the same store key inside a sales table.

Analytical warehouses often use a star schema. In the centre is a fact table, which records events, such as sales, trips or payments. Around it are dimension tables, which describe the who, what, where and when of each event: products, stores, customers and dates.

Facts are long and narrow: many rows, mostly keys and numbers. Dimensions are short and wide: fewer rows, with many descriptive columns, such as a name, a category or a city.

The most important decision is the grain: what exactly one row of the fact table represents. One row per product per receipt is a clear grain. Sales data is not. When the grain is clear, everyone gets the same total. When it is unclear, people count things twice.

This matters for AI too. A feature table, which we build later in the course, comes from facts and dimensions. If the grain is wrong, a feature such as number of purchases is wrong, and the model learns from false counts.

Think of a library. The fact table is the loan register: one line for each book lent, with a borrower number, a book number and a date. The dimensions are the catalogue of books and the list of members.

Let's design one. Efua is a data analyst at a grocery chain with shops in Accra, Ghana, and Lagos, Nigeria. She designs a star schema for sales.

Her fact table is fact sales, and she writes its grain first: one row per product line on one receipt. It holds the receipt, the line number, keys for the date, store and product, and two measures, the quantity and the unit price.

Around it are three dimensions. The store dimension holds the name, city, country and currency. The product dimension holds the name and category. And the date dimension holds the week, the month and a public holiday flag.

The shops use two currencies, cedi and naira. So Efua's revenue query joins the fact table to stores and products, multiplies quantity by unit price, and groups by country, currency and category. It never adds the two currencies together.

On five invented sample lines, the query returns four rows. For example, staples in Ghana come to one hundred and ninety cedi, and staples in Nigeria to twenty-one thousand one hundred naira. A total across both countries would be meaningless without a documented exchange rate.

Efua also considers one wide table, with every store and product column repeated on every line. It is simpler to query, but a store name change would need millions of updates. She chooses the star schema.

A common mistake is to start with the report columns, and only later ask what a row means. Before you add any column, finish this sentence: one row in this table is one what? If you cannot finish it, the design is not ready.

Let's recap. First, primary keys identify rows, and foreign keys connect a fact table to its dimensions. Second, in a star schema, fact tables hold events and numbers, and dimension tables describe them. Third, the grain is the most important modelling decision, because every count and every feature depends on it.

Now it is your turn. In the exercise, you will design a star schema for an online bookshop: a fact table with a one sentence grain, three dimensions, and the keys that join them. It takes about twenty-five minutes. Next lesson: DuckDB, fast analytics on your laptop.
```

## L05 DuckDB: Fast Analytics on Your Laptop

- **Filename:** `ai-17-data-engineering-for-ai_M1_L05_presenter.mp4`
- **Expected length:** about 4.9 minutes (674 words). The quality gate accepts ±10%.

```text
What if you could run warehouse-style SQL on a file of millions of rows, on your laptop, with no server to install? DuckDB does exactly that. And it often finishes before you look away from the screen.

Last time, we designed tables with keys and a clear grain. Today we meet the second database in this course. DuckDB is a free, open-source, in-process analytical database.

In-process means it runs inside your Python program, or its own command-line tool. There is no server, no user accounts and no network connection. You install it with one pip command, and query CSV and Parquet files directly, as if they were tables.

Two ideas explain why it is fast. The first is column storage. A normal row database stores each row together, which is great for updating one customer at a time. But a query such as average energy per meter needs only two columns, and a row store must still read every column. DuckDB works column by column, so it reads only what the query needs.

The second idea is Parquet, an open, column-based file format. It stores data types, compresses each column and keeps summary statistics. So it is usually much smaller than the same data as CSV, and faster to read. CSV is plain text, so every query must read every character again.

Picture a long shopping receipt. To find the total spent on fruit, you must read every item. A Parquet file is like a spreadsheet already sorted into columns, with a subtotal at the bottom of each one. You jump straight to the column you need.

So when should you choose each database? Choose DuckDB when one person or one pipeline analyses files locally, and when you build datasets, such as Parquet files for machine learning. Choose PostgreSQL when many users read and write at the same time, and you need a server that is always running. In this course, the capstone can use either one.

Let's measure the difference. Hiroshi is a backend developer at an electricity retailer in Osaka, Japan. He wants the average use per smart meter. He uses generated data, so no customer data appears.

In a terminal, he installs DuckDB, and opens a new Python file called compare.

First, the script connects to DuckDB, and generates two million meter readings for five thousand meters. It writes them to a CSV file, then copies the same data into a Parquet file.

Then, for each file, it runs the same query, the average reading per meter, and prints the file size in megabytes and the time the query took.

He runs the script. On our four-core test machine, the CSV file is twenty-eight point eight megabytes, and the query takes about a tenth of a second. The Parquet file is only five point nine megabytes, and the query takes nine thousandths of a second.

Same two million rows, about five times smaller, and more than ten times faster. Your exact numbers will differ with your hardware and DuckDB version. Hiroshi stores monthly exports as Parquet, and keeps PostgreSQL for the customer portal.

Two common mistakes. DuckDB is not a replacement for every database. It is not built for a web app where hundreds of users write small updates. And do not trust a single timing run. Run each query two or three times, and compare the typical result.

Let's recap. First, DuckDB is an in-process analytical database that queries CSV and Parquet files directly. Second, column storage and Parquet make analytical queries faster and files smaller. Third, choose DuckDB for local analysis and building datasets, and a server database such as PostgreSQL for shared, always-on work.

Now it is your turn. In the exercise, you will run this comparison yourself three times, try a different column, and write two sentences on file size and query time. You can use the script from this video, or the orders file from lesson three. It takes about twenty-five minutes. Next week we start transforming data, with dbt Core: Project Setup and First Model.
```
