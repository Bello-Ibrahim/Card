# L10 Documentation and Lineage | Presenter Script

Course: AI-17 · Video: 5 min · Words: 697

## Hook
A data scientist asks: where does days since last come from, and does it include cancelled orders? If the answer lives only in your memory, every question interrupts you. And when you leave the team, the answer leaves with you.

## Explain
Last time, we made models incremental. Today we make them understandable. In dbt, documentation lives next to the code. You add a description to each model and its important columns, in a YAML file. The same file will hold your tests later.

Because descriptions sit in the project, they are reviewed and versioned with the SQL. When the SQL changes, the description changes in the same step.

Two commands build a documentation site. The first, generate, reads the project and the database, and writes a catalogue of every model, column, type and description. The second, serve, starts a small local web server and opens the site in your browser.

The site includes the lineage graph. It shows every source and model as a box, with arrows that follow your source and ref calls. You did not draw this graph. dbt built it from your code. That is why using ref instead of written table names matters.

Lineage helps in two directions. Upstream: a number looks wrong, so you follow the arrows back to its staging model and source. Downstream: a source is about to change a column, so you follow the arrows forward to see every model and consumer it will affect.

Good descriptions are short and specific. Say what one row means, the unit of each number, the time window of each feature, and anything a reader might misunderstand, such as excludes cancelled orders.

Lineage is like the family tree at the front of a long novel. When a character appears in chapter twenty, you check the tree to see who their parents are. You do not reread the whole book.

## Demonstrate
Let's document a feature table. Priya is an analytics engineer at a microfinance lender in Pune, India. Loan officers ask many questions about her borrower feature table.

She opens the schema file in the marts folder. For the model, she writes the grain, one row per borrower per feature date, the rule that it uses only repayments before that date, and what it is used for.

Then she describes two columns. The borrower ID is an internal ID, not a national ID. And late payments in one hundred and eighty days counts instalments paid more than seven days late, in the hundred and eighty days before the feature date.

She runs generate, then serve, and the site opens in her browser. She opens the feature table, and shows the descriptions and column types.

Now the lineage graph. Two paths lead into the feature table: raw repayments through staging repayments, and raw borrowers through staging borrowers. She clicks staging repayments to show every model downstream of it.

Now Priya can answer in three sentences. The feature comes from raw repayments, received every night from the loan system. Staging converts the dates and removes test loans. The feature table counts instalments paid more than seven days late, in the hundred and eighty days before the feature date.

A common mistake is a description that only repeats the column name, such as late payments in one hundred and eighty days. That adds nothing. Answer what a new reader would ask: what counts as late, which dates are included, and where the value comes from. And update descriptions in the same change as the SQL, not once and then forget.

## Recap
Let's recap. First, dbt descriptions live in YAML next to the models, so documentation is versioned and reviewed with the code. Second, generate and serve build a documentation site, with a lineage graph created from source and ref. Third, lineage lets you trace a value upstream to its source, and see what a change affects downstream.

## CTA
Now it is your turn. In the exercise, you will document three models and their key columns, generate the site, and use the lineage graph to explain where one feature column comes from, in three sentences. It takes about thirty minutes. Next week is about data quality, starting with: What Makes Data Bad?

## Thumbnail
Headline: Where Does This Come From?
Image: Navy background, a lineage graph of teal boxes and arrows from raw tables to a feature table, one path highlighted, headline in teal Inter Bold.

## Production Notes
- [VERSION] dbt docs generate and dbt docs serve behaviour (default port, browser opening) and the layout of the documentation site and lineage graph view must be checked against the current dbt Core release before recording.
- Priya and the microfinance lender in Pune, India are fictional; borrower data is invented. The borrower_id description stresses that it is not a national ID; keep that visible on screen.
- Screen lineage must show exactly: raw.repayments → stg_repayments → fct_borrower_features and raw.borrowers → stg_borrowers → fct_borrower_features.
