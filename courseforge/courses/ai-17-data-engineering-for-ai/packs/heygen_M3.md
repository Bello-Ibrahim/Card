# HeyGen Batch Pack: AI-17 M3 (Data Quality and Orchestration)

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

## L11 What Makes Data Bad?

- **Filename:** `ai-17-data-engineering-for-ai_M3_L11_presenter.mp4`
- **Expected length:** about 4.7 minutes (641 words). The quality gate accepts ±10%.

```text
Bad data rarely crashes anything. The pipeline finishes. The dashboard loads. The model trains. It simply learns the wrong thing, and nobody notices until a decision based on it goes wrong.

Welcome to week three, on data quality and orchestration. You can now build models in layers. But how do you know the data inside them is good? It helps to break quality into six dimensions.

Completeness asks: are required values present? Uniqueness asks: is each real event recorded once? Validity asks: do values follow the rules for their type and range, so no body temperature of seventy-three degrees? And consistency asks: do related values agree, so no delivery before the order was placed?

Timeliness asks: is the data recent enough, or has yesterday's file not arrived? And accuracy asks: does the value match reality? The first five can usually be checked with SQL. Accuracy often needs another trusted source, or a human check.

For AI, each problem has a specific effect. Duplicates make some events look more common. Missing values in one group make the model less reliable for that group. Invalid values stretch averages and scales. None of these produce an error message.

So you must look for problems on purpose. This is called profiling: counting missing values, duplicates and out-of-range values per column, before you trust a dataset. DuckDB is a good tool for it. Its summarize command describes every column in one step, and targeted queries count exactly what you care about.

Profiling is like a health check-up. Most people feel fine before one. The doctor still measures blood pressure, because some problems have no symptoms until they are serious.

Here is an invented example. Doctor Samira Haddad leads a small health data team for a network of clinics near Irbid, Jordan. A report shows malaria cases twice as high as last season. Before anyone reacts, she profiles the visits table.

She opens Python, connects to DuckDB, and loads the visits export. Then she runs summarize. Two columns have missing values, the patient ID and the temperature. And the maximum temperature is seventy-three, which is impossible.

Next, a targeted profile in one query. It counts the total rows, the missing patient IDs, the missing temperatures, the extra rows beyond distinct visit IDs, and the temperatures outside a normal human range. On her eleven invented rows, it returns eleven, one, one, three and one.

Three duplicate rows. So she compares the malaria count before and after removing duplicates. The raw count is six. The real count, by distinct visit, is three.

Every malaria visit had been loaded twice, because a sync job ran again after a network error. The disease was not twice as common. The rows were.

Samira lists her issues in order of risk. First, the duplicated visits, which change the disease count. Second, the impossible temperature, probably thirty-seven point three typed wrongly. Third, a visit without a patient ID. Fourth, a missing temperature. She deletes nothing in the raw table. Instead, she writes rules that staging and tests must enforce.

A common mistake is to check only that the pipeline ran successfully. That tells you the SQL was valid, not that the data is right. Profile every new source, and turn each problem into a rule in code.

Let's recap. First, six dimensions describe data quality: completeness, uniqueness, validity, consistency, timeliness and accuracy. Second, bad data does not crash a model. It quietly teaches it the wrong thing, so profile data on purpose. Third, DuckDB's summarize and targeted count queries find missing values, duplicates and out-of-range values quickly.

Now it is your turn. In the exercise, you will profile the course orders table with DuckDB, count missing values, duplicates and out-of-range values, and list your five most serious issues, with the dimension of each. It takes about thirty minutes. Next lesson: Testing Data with dbt.
```

## L12 Testing Data with dbt

- **Filename:** `ai-17-data-engineering-for-ai_M3_L12_presenter.mp4`
- **Expected length:** about 4.8 minutes (666 words). The quality gate accepts ±10%.

```text
In the last lesson, you found problems by looking. That works once. Tomorrow a new file arrives, and nobody will look. dbt tests turn every problem you found into a check that runs automatically, every time.

A dbt test is a query that looks for bad rows. If it returns zero rows, the test passes. If it returns rows, the test fails, and dbt shows how many. There are two kinds of tests.

Generic tests are ready-made, and you configure them in YAML, next to your descriptions. dbt Core includes four. Unique means no value appears twice. Not null means no value is missing. Accepted values means every value is in a list you give. And relationships means every value exists in another model, like a foreign key.

Singular tests are your own SQL files in the tests folder. Each one selects the rows that break a business rule, such as: a shipment cannot leave before it is packed.

You also decide what a failure means. By default, a failing test is an error. With the build command, which runs and tests models in order, an error stops every model that depends on the failed one. So bad data does not reach the feature table. For less serious problems, you set the severity to warn. dbt reports the problem, but continues.

A good rule: use error for anything that would make the AI dataset wrong, such as duplicates, broken keys or impossible values. Use warn for things a person should review, such as a few missing optional values.

Tests are like smoke alarms. You install them once, where fire is most likely. After that, you do not check each room every night. The alarm tells you when something is wrong.

Let's add tests. Mateo is a data engineer at a coffee exporter in Medellín, Colombia. His staging model for shipments must be reliable, because it feeds a model that predicts shipping delays.

He opens the staging schema file. The shipment ID must be unique and not null. The status must be packed, shipped or delivered. The exporter ID must exist in the exporters model. And a missing number of bags only gives a warning.

Next, a singular test for a business rule. It selects any shipment with zero or fewer bags, or a ship date before the packed date.

He runs the tests for the shipments model. On his three invented rows, the singular test finds two bad rows. Shipment five o two was shipped two days before it was packed, and shipment five o three has minus five bags. The accepted values test also fails, because shipment five o three has the status pending.

Mateo discusses each failure with the business team. Pending is a real status that was missing from the list, so he adds it. The other two are data entry errors, so he asks the source team to correct them, and he leaves the tests as errors.

Finally, he runs build. While the error test fails, the feature table is skipped. Bad rows never reach the model.

A common mistake is to test only the final table. When a test fails there, it is hard to know which step caused it. Test at every layer. And never make a test pass by deleting it, or changing it to warn, without asking why it failed.

Let's recap. First, a dbt test is a query that returns bad rows, and zero rows means it passes. Second, generic tests are set in YAML, and singular tests are SQL files for business rules. Third, decide on purpose which failures stop the pipeline and which only warn, and test at every layer.

Now it is your turn. In the exercise, you will add at least six tests to your project, including one business rule. Then you break the data on purpose with a lost order, watch a test fail, and fix it in the right place. It takes about thirty-five minutes. Next lesson: Orchestrating with Apache Airflow.
```

## L13 Orchestrating with Apache Airflow

- **Filename:** `ai-17-data-engineering-for-ai_M3_L13_presenter.mp4`
- **Expected length:** about 5.1 minutes (719 words). The quality gate accepts ±10%.

```text
Your pipeline works when you type three commands in the right order. But who types them at three in the morning, every night? And who notices when the second one fails? An orchestrator does both.

In the last lesson, you added tests to your dbt project. Today, you make the whole pipeline run by itself. The tool is Apache Airflow, an orchestrator. It runs pipelines written as Python files, and it shows every run in a web interface.

Four ideas explain Airflow. The first is the DAG, short for directed acyclic graph. A DAG is one pipeline: a set of tasks and the arrows between them. Acyclic means the arrows never loop back.

The second idea is the task, one step, such as load raw data or run dbt. An operator is the type of task. The bash operator, for example, runs a shell command.

The third idea is dependencies. They set the order. Each task starts only after the one before it succeeds. The fourth is the schedule, which says when the DAG runs, for example daily. Each run also has a logical date, which tells the task which day of data to process.

Behind the scenes, several parts run together: a scheduler, a web server, a database for Airflow's own records, and workers that run the tasks. The simplest local setup is the official Docker Compose file. It needs Docker and enough free memory, so check the documentation for your version.

Airflow two and Airflow three differ in imports, some command names and the web interface. Our code targets Airflow three, and shows the Airflow two imports as comments.

Think of Airflow as a train timetable with a station manager. The timetable says when each train leaves. The rail lines say which train must arrive before another departs. And the manager watches every train and reports delays on the station board.

Let's build it. Katarzyna is a data engineer at a bakery chain in Kraków, Poland. Her dbt project is in a folder called dbt slash shop, and a Python script loads each day's orders.

First, she downloads the official Docker Compose file for her Airflow version, and creates four folders next to it. On Linux, she also writes her user ID into a small environment file.

She mounts her dbt project and scripts into the containers, and makes dbt available inside them, for local testing only. Then she starts Airflow with two commands.

Now the DAG file. It creates a DAG called shop E L T that starts on the first of September, runs daily, and does not catch up on old dates. Inside are three bash tasks. The first runs the load script and passes it the logical date. The second runs dbt, and the third runs the dbt tests.

The last line sets the order: load, then run, then test. The file only defines tasks and dependencies. No real work happens outside a task.

She opens the web interface on port eight thousand and eighty, and signs in with the default local account. She finds shop E L T, switches it on and triggers it manually.

In the graph view, the three tasks turn green, one after another. She opens the log of the dbt run task, and there is the familiar dbt output.

A common mistake is to put heavy work at the top of the DAG file, such as reading a database outside any task. Airflow reads DAG files often to find changes, so that code runs again and again and slows the scheduler. Keep the file light, and put the real work inside the tasks.

Let's recap. First, an Airflow DAG is a pipeline written in Python: tasks, the dependencies between them, and a schedule. Second, the bash operator can run your load script and your dbt commands, and one short line sets their order. Third, the local Docker setup needs enough memory, and Airflow two and three differ, so follow the documentation for your version.

Now it is your turn. In the exercise, you write a DAG with three tasks that load raw data, run your dbt models and run your dbt tests, every day. You trigger it manually, and check that the tasks run in the right order. It takes about forty minutes. Next lesson: Retries, Backfills and Alerts.
```

## L14 Retries, Backfills and Alerts

- **Filename:** `ai-17-data-engineering-for-ai_M3_L14_presenter.mp4`
- **Expected length:** about 4.9 minutes (682 words). The quality gate accepts ±10%.

```text
Your pipeline will fail. A server restarts, a file arrives late, a password expires. The question is not whether it fails, but what happens next. Does it recover by itself? And does it leave clean data behind?

In the last lesson, you built a DAG that runs every night. Today, you make it safe to fail. Four design choices help: retries, idempotent tasks, backfills and alerts.

First, retries. Many failures are temporary, such as a network timeout. Airflow can try a task again automatically. You set how many times, and how long to wait between tries. The wait gives the other system time to recover.

Second, idempotent tasks. A task is idempotent when running it twice for the same date gives the same result as running it once. A load that only adds rows is not idempotent, because a retry doubles the data. A load that first deletes that date's rows, and then inserts them again, is idempotent. Retries are only safe when tasks are idempotent.

Third, backfills. When a pipeline was down, or a rule changed, you rerun it for past dates. Each run receives its logical date, so the task loads the right day. Again, this is only safe with idempotent tasks.

Fourth, alerts. When a task still fails after all its retries, a person must know. Airflow can call a Python function on failure, and that function can send an email or a chat message.

A good pipeline is like a postal service. If nobody is home, the courier tries again tomorrow, not twice at the same door today. Every parcel has a tracking number, so a second attempt never creates a second parcel. And if delivery fails three times, the sender is told.

Tariq is a data engineer at a pharmacy chain in Karachi, Pakistan. Every night, each store's sales file arrives with the date in its name. Last week, the file server was down for three nights.

First, he makes the load script idempotent. It receives the logical date, deletes that date's rows from the raw sales table, and then inserts the rows from that day's file.

He runs it twice for the first of September, on a small sample file. The table holds three rows after each run, not six.

Next, he adds default arguments to the DAG from the last lesson: three retries, ten minutes apart, and a failure function. Here it only prints an alert line. In real use, it would send a message to the team.

Now he breaks it on purpose. He renames the sales file for one date and triggers the DAG. The task waits and tries again. After three retries, it fails, and the alert line appears in the log.

He restores the file and clears the failed task. This time it succeeds.

Then he backfills the three missed nights, from the first to the third of September, with the backfill command for his Airflow version, inside the container. Finally, he counts rows per load date. Each date appears once, with its own count. Running the backfill again would change nothing, because the load is idempotent.

A common mistake is to set many retries and think the pipeline is now reliable. If a task adds data, a retry can leave doubled rows. And if the error is permanent, retries only delay the alert. Make tasks idempotent first, and use a few retries with a delay.

Let's recap. First, retries with a delay handle temporary failures, but they are only safe when tasks are idempotent. Second, an idempotent task gives the same result when you run it twice, for example by deleting and reloading one date's rows. Third, backfills rerun past dates using the logical date, and alerts make sure a person knows when retries are not enough.

Now it is your turn. In the exercise, you make one task fail on purpose and watch the retries. Then you fix it, run a backfill for three past dates, and run it again to check that no rows are doubled. It takes about forty minutes. Next lesson: Preparing Datasets for Machine Learning.
```
