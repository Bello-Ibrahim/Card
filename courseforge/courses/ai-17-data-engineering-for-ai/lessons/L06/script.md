# L06 dbt Core: Project Setup and First Model | Presenter Script

Course: AI-17 · Video: 5 min · Words: 690

## Hook
Imagine forty SQL scripts that must run in a certain order, and only one person knows the order. dbt Core replaces that person's memory with a project. Every transformation is a file, and the tool works out what to run, and when.

## Explain
Welcome to week two. Your raw data is loaded, and now we transform it. dbt Core is a command-line tool for the T in ELT. In this lesson, you install it, connect it to your database, and run a first model.

You write each transformation as a model. A model is a SQL file that contains one select statement. dbt wraps it in the right create view or create table command, runs the models in the right order, and reports the result. Because models are plain text files, you can keep them in Git, review them and test them.

dbt Core needs three things. First, an adapter for your database: a separate package for PostgreSQL, and another for DuckDB. Second, a profile, usually in your home folder, that says how to connect. Keep passwords out of the project folder. Third, a project: a folder with a project file and a models folder.

You will use four main commands. Debug checks the connection. Run builds the models. Test runs your tests, which we cover in week three. And build runs and tests everything in order. By default, a model becomes a view, and one configuration line turns it into a table.

Think of dbt as a recipe book with a smart kitchen assistant. You write each recipe on its own card, and say which other recipes it needs. The assistant reads all the cards, decides the cooking order, and tells you if a dish failed.

## Demonstrate
Let's set it up. Leila is a data analyst for a group of guesthouses in Marrakesh, Morocco. Her raw bookings are already in a DuckDB file, in a raw bookings table.

First, she creates and activates a virtual environment. Then she installs dbt Core with the DuckDB adapter. If you use PostgreSQL, you install the PostgreSQL adapter instead.

Next, she creates a project called riad bookings, and chooses DuckDB when the tool asks for the adapter.

Now the profile. She opens the profiles file in her home folder, and points the development target to her DuckDB file, with one thread. A PostgreSQL profile would list the host, port, user and database, and read the password from an environment variable.

She runs debug, and the connection test passes.

Then she deletes the example models, and writes her first model. It simply selects the booking ID, guest country and check-in date from the raw bookings table.

She runs dbt. The log shows one view model created, and a summary line that reports success. Finally, she counts the rows in the new view, and the count matches the raw table.

Notice one thing. The raw table name is written directly into the SQL of this first model. That works, but dbt does not know where the data comes from. In the next lesson, Leila replaces it with a declared source, so dbt can track it.

A common mistake is to keep the profile, with a real database password, inside the project folder, and then push it to a public repository. Keep the profile in your home folder, read secrets from environment variables, and add local credential files to the ignore list. And never paste passwords into an AI chat when you ask for help with an error.

## Recap
Let's recap. First, a dbt model is one select statement in a SQL file, and dbt turns it into a view or a table, in the right order. Second, dbt needs an adapter, a profile and a project folder. Third, use debug to test the connection and run to build models, and keep credentials out of the project.

## CTA
Now it is your turn. In the exercise, you will install dbt with one adapter, create a project, and build a first model from your raw orders table. The new view should have nine rows. It takes about thirty-five minutes. Next lesson: Sources, Staging Models and the ref function.

## Thumbnail
Headline: Your First dbt Model
Image: Navy background, a terminal window with a green success line and a stack of SQL file cards arranged in order, headline in teal Inter Bold.

## Production Notes
- [VERIFY] dbt Core's open-source licence terms: the voiceover calls dbt Core a command-line tool and does not describe its licence; confirm before adding 'free and open source' on screen.
- [VERSION] dbt Core package and adapter names (dbt-core, dbt-duckdb, dbt-postgres), the dbt init prompts, the profile keys, the default schema for dbt-duckdb (main) and the run log wording must be checked against the current releases before recording.
- The profile path /home/leila/data/riad.duckdb is an example; make sure no real password or connection string appears on screen. The PostgreSQL profile reads the password from an environment variable.
- Leila and the guesthouses in Marrakesh, Morocco are fictional; the bookings data is invented.
