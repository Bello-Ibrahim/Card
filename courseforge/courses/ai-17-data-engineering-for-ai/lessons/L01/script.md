# L01 What Data Engineers Do for AI | Presenter Script

Course: AI-17 · Video: 5 min · Words: 738

## Hook
A team spends two days training a model, and two months getting the data ready for it. That is not bad planning. In most AI projects, preparing the data is the biggest part of the work. And that part belongs to data engineers.

## Explain
Hi, and welcome to Data Engineering for AI. In this first lesson, we look at what data engineers actually do, and why AI depends on their work.

Data engineering is the work of moving data from the places where it is created to the places where it is used, in a form that people and systems can trust.

Every data system has four roles. Sources are where data is created, such as an app database, a payment service or a sensor. Pipelines are the automated steps that copy, clean, join and reshape the data. Storage is where data lives between steps, in a data warehouse or a data lake, which we compare next time. And consumers are the people and systems that use the result.

When the consumer is an AI model, the stakes are higher. A model learns whatever patterns the data contains, including mistakes. If a pipeline sends duplicated rows, the model learns that some events happen twice as often as they really do. If future information slips into the training data, the model looks excellent in testing, and then fails in real use.

So a good pipeline for AI has four qualities. It is reliable: it runs on time, and when it fails, someone knows. It is repeatable: running it again gives the same result. It is tested: automatic checks catch bad values before anyone sees them. And it is documented: anyone can see where each column comes from.

In this course, you build all four with free tools. PostgreSQL and DuckDB for storage, dbt Core for transformations and tests, and Apache Airflow for scheduling.

Here is a simple way to picture it. A data pipeline is like a water treatment plant. River water arrives full of mud and leaves. The plant filters it, treats it and tests it in fixed stages, then sends safe water to every tap, every day.

When the plant works well, nobody notices it. When it fails, everybody downstream notices at once. Good data engineering works the same way.

## Demonstrate
Let's see this in practice. Tomás is a backend developer at a crop insurance start-up in Córdoba, Argentina. The data science team wants a model that predicts which farms will make a drought claim next season. They ask him for a table of farms with their history.

Before writing any code, Tomás maps the flow. His sources are the policy database, the claims system, daily rainfall files from a weather provider, and field visit notes typed by agents. A nightly pipeline copies, cleans and joins them by farm and date.

Raw copies are kept unchanged, and the cleaned tables feed a final table with one row per farm per season. Three consumers use it: the data science team, the finance team, and a dashboard for regional managers.

The map shows two risks early. First, the rainfall files use weather station codes, not farm IDs. So Tomás needs a lookup table that links each farm to its nearest station.

Second, field visit notes are sometimes written after a claim is paid. If those notes enter the training data, the model will see the answer. So Tomás writes both risks next to the map, and agrees with the data scientists which date each column is based on.

A common mistake is to treat data engineering as a one-time job. In practice, new rows arrive every day, the model is retrained, and sources change their format without warning. Treat every data flow as a system that runs again and again.

## Recap
Let's recap. First, every data system has sources, pipelines, storage and consumers, and mapping them is your first step. Second, AI models learn from whatever the data contains, so duplicated, missing or future information quietly makes a worse model. Third, a good pipeline for AI is reliable, repeatable, tested and documented, not only fast.

## CTA
Now it is your turn. In the exercise below this video, you will map the data flow of a ride-hailing app in Jakarta, with four sources, its storage, three consumers and one data risk. It takes about twenty minutes. In the next lesson, we look at ETL, ELT, batch and streaming. See you there.

## Thumbnail
Headline: Before the Model: Data
Image: Navy background, a clean pipeline of teal boxes flowing from raw source icons to a small model icon, headline in teal Inter Bold.

## Production Notes
- No facts to verify: content.md Review Flags are None and all examples are hypothetical.
- Tomás and the crop insurance start-up in Córdoba, Argentina are fictional; stock footage must show no real company names or logos.
- The 'two days versus two months' line in the hook is an illustration, not a statistic; keep it phrased as a scenario.
