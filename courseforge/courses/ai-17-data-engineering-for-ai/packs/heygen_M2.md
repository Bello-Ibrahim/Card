# HeyGen Batch Pack: AI-17 M2 (Transforming Data with dbt)

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

## L06 dbt Core: Project Setup and First Model

- **Filename:** `ai-17-data-engineering-for-ai_M2_L06_presenter.mp4`
- **Expected length:** about 4.9 minutes (687 words). The quality gate accepts ±10%.

```text
Imagine forty SQL scripts that must run in a certain order, and only one person knows the order. dbt Core replaces that person's memory with a project. Every transformation is a file, and the tool works out what to run, and when.

Welcome to week two. Your raw data is loaded, and now we transform it. dbt Core is a command-line tool for the T in ELT. In this lesson, you install it, connect it to your database, and run a first model.

You write each transformation as a model. A model is a SQL file that contains one select statement. dbt wraps it in the right create view or create table command, runs the models in the right order, and reports the result. Because models are plain text files, you can keep them in Git, review them and test them.

dbt Core needs three things. First, an adapter for your database: a separate package for PostgreSQL, and another for DuckDB. Second, a profile, usually in your home folder, that says how to connect. Keep passwords out of the project folder. Third, a project: a folder with a project file and a models folder.

You will use four main commands. Debug checks the connection. Run builds the models. Test runs your tests, which we cover in week three. And build runs and tests everything in order. By default, a model becomes a view, and one configuration line turns it into a table.

Think of dbt as a recipe book with a smart kitchen assistant. You write each recipe on its own card, and say which other recipes it needs. The assistant reads all the cards, decides the cooking order, and tells you if a dish failed.

Let's set it up. Leila is a data analyst for a group of guesthouses in Marrakesh, Morocco. Her raw bookings are already in a DuckDB file, in a raw bookings table.

First, she creates and activates a virtual environment. Then she installs dbt Core with the DuckDB adapter. If you use PostgreSQL, you install the PostgreSQL adapter instead.

Next, she creates a project called riad bookings, and chooses DuckDB when the tool asks for the adapter.

Now the profile. She opens the profiles file in her home folder, and points the development target to her DuckDB file, with one thread. A PostgreSQL profile would list the host, port, user and database, and read the password from an environment variable.

She runs debug, and the connection test passes.

Then she deletes the example models, and writes her first model. It simply selects the booking ID, guest country and check-in date from the raw bookings table.

She runs dbt. The log shows one view model created, and a summary line that reports success. Finally, she counts the rows in the new view, and the count matches the raw table.

Notice one thing. The raw table name is written directly into the SQL of this first model. That works, but dbt does not know where the data comes from. In the next lesson, Leila replaces it with a declared source, so dbt can track it.

A common mistake is to keep the profile, with a real database password, inside the project folder, and then push it to a public repository. Keep the profile in your home folder, read secrets from environment variables, and add local credential files to the ignore list. And never paste passwords into an AI chat when you ask for help with an error.

Let's recap. First, a dbt model is one select statement in a SQL file, and dbt turns it into a view or a table, in the right order. Second, dbt needs an adapter, a profile and a project folder. Third, use debug to test the connection and run to build models, and keep credentials out of the project.

Now it is your turn. In the exercise, you will install dbt with one adapter, create a project, and build a first model from your raw orders table. The new view should have nine rows. It takes about thirty-five minutes. Next lesson: Sources, Staging Models and the ref function.
```

## L07 Sources, Staging Models and ref()

- **Filename:** `ai-17-data-engineering-for-ai_M2_L07_presenter.mp4`
- **Expected length:** about 4.9 minutes (692 words). The quality gate accepts ±10%.

```text
A column called amt in one table, Amount in another, and order value USD in a third. Dates stored as text. A test row someone forgot to delete. Every raw table has problems like these. The staging layer is where you fix them once, for everyone.

Last time, you built a first dbt model that read the raw table directly. Today we organise the project properly, in layers. Each layer has one job, which makes the project easier to read and to change.

Sources are the raw tables, declared in a YAML file. dbt does not build them. It only reads them. Staging models come next: one model per source table. They rename columns to one style, cast types, trim spaces, and remove rows that are clearly not real data. Then intermediate and mart models join and aggregate them to answer questions.

Staging never joins, never aggregates, and never changes what the data means. It only makes the data consistent, so that every later model can trust the same clean columns.

Two functions connect the layers. The source function points to a declared raw table. The ref function points to another model. When you use them instead of writing table names, dbt builds a dependency graph. It knows which model must be built first, and it can draw the lineage graph. If the raw schema moves, you change one line in the YAML file, not every model.

Staging is like preparing ingredients before cooking. You wash the vegetables, peel them and cut them to the same size, but you do not decide on the dish yet. Because everything is prepared the same way, any cook can use it for any recipe.

Let's build a staging model. Sipho is a backend developer at an online craft marketplace in Durban, South Africa. His raw export is the course orders file, with a duplicated order, a test row, a missing amount, and one status written with a capital letter.

First, he creates a staging folder, and a sources file inside it. The file declares one source called raw, in the raw schema, with one table: orders.

Next, the staging model. It reads the source with the source function, and keeps only distinct rows. Then it casts the order ID to a whole number, the date to a real date, and the amount to a decimal, turning empty text into null.

It lowercases and trims the status, uppercases the country code, and removes the test customer. Notice the names: lowercase with underscores, the unit in the amount name, and a clear suffix for codes.

He deletes the first model from last lesson, because staging replaces it. Then he runs only the staging model, and the log shows success.

He queries the result. Seven rows from nine: the duplicate of order ten o seven and the test row are gone. Order ten o five now says delivered in lowercase. And order ten o six still has a null amount. Sipho keeps it, because a missing amount is a fact about the data, and a test will report it later.

From now on, later models never read the raw table directly. A mart starts from the staging model, using ref. So dbt always builds staging first.

A common mistake is to put business logic in staging, such as keeping only delivered orders. Then a team that needs cancelled orders writes its own copy of the cleaning rules. Keep every real row in staging. Business decisions belong in marts.

Let's recap. First, declare raw tables as sources and read them with source, and read other models with ref, so dbt knows the build order. Second, build one staging model per source that renames, casts and cleans, without changing meaning. Third, remove only rows that are clearly not real data, such as exact duplicates and test rows.

Now it is your turn. In the exercise, you will declare your raw orders table as a source, build your own staging model, and write down the row count before and after, with a reason for each removed row. It takes about thirty minutes. Next lesson: Building Marts and Feature Tables for AI.
```

## L08 Building Marts and Feature Tables for AI

- **Filename:** `ai-17-data-engineering-for-ai_M2_L08_presenter.mp4`
- **Expected length:** about 4.9 minutes (683 words). The quality gate accepts ±10%.

```text
A churn model gets an excellent score in testing, and fails in its first month of real use. The data was clean. The code had no bugs. The problem was one column. It quietly used information from after the date it was meant to predict.

Last time, you cleaned raw data in a staging model. Now we build the final layer. Marts join and aggregate staging models into tables that answer a business question, such as revenue per store per month. A mart has a clear grain, and a name that says what it holds.

A feature table is a special mart for machine learning. It has one row per entity at a given date, such as one row per customer on the first of March. And it has feature columns that describe the entity, such as purchases in the last ninety days, or days since the last login.

It also has a feature date, sometimes called a cut-off date. That is the moment the prediction would be made. And it often has a label, the thing to predict, calculated from events after that date.

The golden rule is simple. Features may only use data from before the feature date. If a feature uses later events, the model learns from the future. This is called data leakage. Test results look excellent, and real results are poor, because in real use the future is not available.

Keep the feature date in one place, not repeated in every model. dbt variables do this. You define the feature date once in the project file, and read it wherever you need it.

Think of a student preparing for an exam, using only lessons taught before the exam date. If the practice test includes the real exam answers, the practice score is perfect. But it tells you nothing about how the student will really do.

Let's build one. Juliana is a data engineer at a prepaid mobile network in Recife, Brazil. The data science team wants to predict which customers will stop recharging in March. Her staging model has one row per recharge, with the customer, the date and the amount.

First, she adds a variable to the project file. The feature date is the first of March, twenty twenty-six.

Next, she creates the feature model in the marts folder. For each customer, it counts recharges, adds up the spend, finds the last recharge date, and works out the days since that recharge.

The most important part is the filter. It keeps only recharges before the feature date, and within the ninety days before it. Both limits come from the same variable.

She runs the model and queries the table. On eight invented recharges, it returns three rows, one per customer. Customer M one recharged three times, spent seventy reais, and last recharged nine days before the feature date.

But M one also recharged on the fifth of March, and M three on the tenth. Without the date filter, those recharges would enter the features, and recharged recently would perfectly predict did not churn. That is leakage. Juliana writes the feature date and window next to each column, so the data scientists know what each value means.

A common mistake is to build features from the whole table, because more data seems better. For every feature, ask one question. Would I know this value on the feature date? If not, filter the rows by date first.

Let's recap. First, marts join and aggregate staging models, and a feature table is a mart with one row per entity at a feature date. Second, features may only use data from before that date, and using later data is leakage. Third, store the feature date once, as a dbt variable, and document the date and window for every feature.

Now it is your turn. In the exercise, you will build a feature table from your staged orders, with one row per customer and at least four features, and a small table of the date each one is based on. It takes about thirty-five minutes. Next lesson: Incremental Models and Changing Data.
```

## L09 Incremental Models and Changing Data

- **Filename:** `ai-17-data-engineering-for-ai_M2_L09_presenter.mp4`
- **Expected length:** about 4.9 minutes (685 words). The quality gate accepts ±10%.

```text
Your events table grows every day. On the first day, the model builds in seconds. A year later, it rebuilds the whole history every night, even though only yesterday's rows are new. Incremental models let dbt process only what changed.

Last time, you built a feature table. So far, every model was rebuilt completely on each run. That is simple and safe, and it is the right default. But for large tables that only grow, it becomes slow, and on cloud warehouses, expensive.

An incremental model is built in full the first time. On later runs, dbt selects only new or changed rows, and adds them to the existing table. Two pieces of Jinja control this. The first is true when the table already exists and this is not a full refresh. The second refers to the existing table, so you can ask: what is my latest timestamp?

A unique key tells dbt which column identifies a row. If a row with the same key arrives again, dbt replaces it, instead of adding a duplicate.

A different problem is data that changes. A customer moves to a new city, and the source simply overwrites the old address. If a model needs to know where the customer lived in January, the history is gone. A dbt snapshot solves this. On every run, it compares the source with the last version, and keeps old versions with valid from and valid to dates.

The trade-off is complexity. Late rows can be missed, a wrong filter can create duplicates, and a change in logic only applies to new rows, until you run a full refresh.

Think of a phone book. A full rebuild reprints the whole book every day. An incremental model prints only the new pages and adds them to the binder. And a snapshot keeps the old pages when a number changes, stamped with the dates they were valid.

Let's try it. An is an analytics engineer at a language-learning app in Hanoi, Vietnam. The raw events table receives app events every day.

She creates an events model, and its first line sets the materialisation to incremental, with the event ID as the unique key. The model selects the event columns, casts the timestamp, and adds a column that records when dbt loaded each row.

Then the key part. Only on incremental runs, a filter keeps events newer than the latest timestamp already in the table.

The first run builds the full table, with three events. She inserts two new events for the next day, and runs the same command again. This time, only the two new rows are selected. A third run, with no new data, selects nothing.

Now she checks for duplicates, grouping by event ID and keeping any ID that appears more than once. The check returns no rows. The table has five rows and five distinct IDs, and the loaded at column shows that the first three rows kept their original load time.

An also tracks changes in user profiles with a snapshot. In recent dbt releases, it can be defined in YAML. It watches the country and plan columns, and she runs the snapshot command every day, before the models.

A common mistake is to make every model incremental from day one. On small tables, it saves nothing and adds risk. Start with full rebuilds. Switch only large, slow models, and add a small look-back window, such as the last three days, with a unique key.

Let's recap. First, incremental models build the full table once, then process only new or changed rows. Second, a unique key prevents duplicates when rows arrive again, and snapshots keep the history of records that change. Third, incremental logic adds new ways to fail, so use it only for large, slow tables, and always test for duplicates.

Now it is your turn. In the exercise, you will turn your orders mart into an incremental model, add two new orders, and run it twice. You should see seven rows, then nine, then nine again, with no duplicates. It takes about thirty-five minutes. Next lesson: Documentation and Lineage.
```

## L10 Documentation and Lineage

- **Filename:** `ai-17-data-engineering-for-ai_M2_L10_presenter.mp4`
- **Expected length:** about 5.0 minutes (697 words). The quality gate accepts ±10%.

```text
A data scientist asks: where does days since last come from, and does it include cancelled orders? If the answer lives only in your memory, every question interrupts you. And when you leave the team, the answer leaves with you.

Last time, we made models incremental. Today we make them understandable. In dbt, documentation lives next to the code. You add a description to each model and its important columns, in a YAML file. The same file will hold your tests later.

Because descriptions sit in the project, they are reviewed and versioned with the SQL. When the SQL changes, the description changes in the same step.

Two commands build a documentation site. The first, generate, reads the project and the database, and writes a catalogue of every model, column, type and description. The second, serve, starts a small local web server and opens the site in your browser.

The site includes the lineage graph. It shows every source and model as a box, with arrows that follow your source and ref calls. You did not draw this graph. dbt built it from your code. That is why using ref instead of written table names matters.

Lineage helps in two directions. Upstream: a number looks wrong, so you follow the arrows back to its staging model and source. Downstream: a source is about to change a column, so you follow the arrows forward to see every model and consumer it will affect.

Good descriptions are short and specific. Say what one row means, the unit of each number, the time window of each feature, and anything a reader might misunderstand, such as excludes cancelled orders.

Lineage is like the family tree at the front of a long novel. When a character appears in chapter twenty, you check the tree to see who their parents are. You do not reread the whole book.

Let's document a feature table. Priya is an analytics engineer at a microfinance lender in Pune, India. Loan officers ask many questions about her borrower feature table.

She opens the schema file in the marts folder. For the model, she writes the grain, one row per borrower per feature date, the rule that it uses only repayments before that date, and what it is used for.

Then she describes two columns. The borrower ID is an internal ID, not a national ID. And late payments in one hundred and eighty days counts instalments paid more than seven days late, in the hundred and eighty days before the feature date.

She runs generate, then serve, and the site opens in her browser. She opens the feature table, and shows the descriptions and column types.

Now the lineage graph. Two paths lead into the feature table: raw repayments through staging repayments, and raw borrowers through staging borrowers. She clicks staging repayments to show every model downstream of it.

Now Priya can answer in three sentences. The feature comes from raw repayments, received every night from the loan system. Staging converts the dates and removes test loans. The feature table counts instalments paid more than seven days late, in the hundred and eighty days before the feature date.

A common mistake is a description that only repeats the column name, such as late payments in one hundred and eighty days. That adds nothing. Answer what a new reader would ask: what counts as late, which dates are included, and where the value comes from. And update descriptions in the same change as the SQL, not once and then forget.

Let's recap. First, dbt descriptions live in YAML next to the models, so documentation is versioned and reviewed with the code. Second, generate and serve build a documentation site, with a lineage graph created from source and ref. Third, lineage lets you trace a value upstream to its source, and see what a change affects downstream.

Now it is your turn. In the exercise, you will document three models and their key columns, generate the site, and use the lineage graph to explain where one feature column comes from, in three sentences. It takes about thirty minutes. Next week is about data quality, starting with: What Makes Data Bad?
```
