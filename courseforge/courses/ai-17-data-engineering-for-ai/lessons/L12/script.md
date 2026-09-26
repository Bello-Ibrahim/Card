# L12 Testing Data with dbt | Presenter Script

Course: AI-17 · Video: 5 min · Words: 668

## Hook
In the last lesson, you found problems by looking. That works once. Tomorrow a new file arrives, and nobody will look. dbt tests turn every problem you found into a check that runs automatically, every time.

## Explain
A dbt test is a query that looks for bad rows. If it returns zero rows, the test passes. If it returns rows, the test fails, and dbt shows how many. There are two kinds of tests.

Generic tests are ready-made, and you configure them in YAML, next to your descriptions. dbt Core includes four. Unique means no value appears twice. Not null means no value is missing. Accepted values means every value is in a list you give. And relationships means every value exists in another model, like a foreign key.

Singular tests are your own SQL files in the tests folder. Each one selects the rows that break a business rule, such as: a shipment cannot leave before it is packed.

You also decide what a failure means. By default, a failing test is an error. With the build command, which runs and tests models in order, an error stops every model that depends on the failed one. So bad data does not reach the feature table. For less serious problems, you set the severity to warn. dbt reports the problem, but continues.

A good rule: use error for anything that would make the AI dataset wrong, such as duplicates, broken keys or impossible values. Use warn for things a person should review, such as a few missing optional values.

Tests are like smoke alarms. You install them once, where fire is most likely. After that, you do not check each room every night. The alarm tells you when something is wrong.

## Demonstrate
Let's add tests. Mateo is a data engineer at a coffee exporter in Medellín, Colombia. His staging model for shipments must be reliable, because it feeds a model that predicts shipping delays.

He opens the staging schema file. The shipment ID must be unique and not null. The status must be packed, shipped or delivered. The exporter ID must exist in the exporters model. And a missing number of bags only gives a warning.

Next, a singular test for a business rule. It selects any shipment with zero or fewer bags, or a ship date before the packed date.

He runs the tests for the shipments model. On his three invented rows, the singular test finds two bad rows. Shipment five o two was shipped two days before it was packed, and shipment five o three has minus five bags. The accepted values test also fails, because shipment five o three has the status pending.

Mateo discusses each failure with the business team. Pending is a real status that was missing from the list, so he adds it. The other two are data entry errors, so he asks the source team to correct them, and he leaves the tests as errors.

Finally, he runs build. While the error test fails, the feature table is skipped. Bad rows never reach the model.

A common mistake is to test only the final table. When a test fails there, it is hard to know which step caused it. Test at every layer. And never make a test pass by deleting it, or changing it to warn, without asking why it failed.

## Recap
Let's recap. First, a dbt test is a query that returns bad rows, and zero rows means it passes. Second, generic tests are set in YAML, and singular tests are SQL files for business rules. Third, decide on purpose which failures stop the pipeline and which only warn, and test at every layer.

## CTA
Now it is your turn. In the exercise, you will add at least six tests to your project, including one business rule. Then you break the data on purpose with a lost order, watch a test fail, and fix it in the right place. It takes about thirty-five minutes. Next lesson: Orchestrating with Apache Airflow.

## Thumbnail
Headline: Tests That Never Sleep
Image: Navy background, a row of teal check marks and one red cross over data model boxes, headline in teal Inter Bold.

## Production Notes
- [VERSION] dbt test syntax changes between releases: the data_tests: key (older releases use tests:), the placement of values, to and field (newer releases may expect them under an arguments: key), severity configuration and add-on packages such as dbt_utils must be checked against the current dbt Core release and adapter before recording.
- Screen output must match content.md: the singular test returns 2 rows (shipment 502 shipped two days before packing, shipment 503 with -5 bags); accepted_values fails on shipment 503 with status 'pending'.
- Mateo and the coffee exporter in Medellín, Colombia are fictional; the three shipment rows are invented.
