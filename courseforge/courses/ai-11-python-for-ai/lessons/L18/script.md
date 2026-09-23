# L18 Building an ML-Ready Table | Presenter Script

Course: AI-11 · Video: 5 min · Words: 657

## Hook
Imagine a model that predicts returned orders perfectly in testing, and then fails completely with real customers. One common reason is a column that secretly contained the answer. Today, you build a table a model can learn from honestly.

## Explain
Last time, we turned text, categories and dates into numbers. Now we put it all together. An ML-ready table has a simple shape. One row per example, such as one order. One target column, the value you want to predict. And feature columns, all numeric, with no missing values.

Some columns must be removed before training. First, identifiers, such as an order number or a customer name. They are unique labels, not information. A model could memorise them, and that memory would be useless for new orders. Also remove raw columns you have already converted, like the original date.

Second, leaky columns. Data leakage happens when a feature contains information you would not have at the moment of prediction, often because it is created after the outcome. A refund exists only because an order was returned. So it reveals the answer.

Leakage is like an exam with the answers printed faintly on the back of the question paper. A student who notices them gets full marks, but learns nothing, and fails the next exam. A model with a leaky column is that student.

To test any column for leakage, ask one question. At the moment I want to make the prediction, would I already know this value? If the answer is no, remove it.

## Demonstrate
Let's build one. Anjali is a data analyst in Pune, India. The marketplace asks her to prepare a table for a future model that predicts whether an order will be returned. She starts from Hamza's encoded table.

First, she looks at the returned and refund columns side by side. See the pattern? The refund is above zero only when the order was returned. That is leakage.

Next, she makes a copy called ml. The target, returned, becomes one for yes and zero for no. The comparison with yes gives True or False, and as type int turns that into one or zero. Then she drops three columns. The order number, which is an identifier. The refund, which leaks. And the order date, which is already converted.

Run it. Eight rows and eleven columns. The target, plus quantity, price, month, weekday, three city columns and three payment columns.

She checks that every column is numeric. The answer is True. Then she saves the table as a CSV file. Index equals False stops pandas from writing the row labels as an extra column.

Finally, Anjali adds a warning to her notes. Only one order out of eight was returned. That is enough to practise the steps, but far too few for a real model. A real project needs many examples of each outcome.

A common mistake is keeping every column, because more data seems better. Identifiers and leaky columns make a model look better in testing, and worse in real use. The opposite mistake also happens, removing useful features because they look similar to the target. Ask the timing question for each column, and write down why you kept or removed it.

## Recap
Let's recap. First, an ML-ready table has one row per example, one target column, and only numeric features with no missing values. Second, remove identifiers, leaky columns and raw columns you have already converted. Third, save the result with index equals False, and note any limits, such as too few examples of one outcome.

## CTA
Now it is your turn. In the exercise below this video, you will choose a target and five features, explain why you removed two columns, and save an ML-ready CSV. It takes about twenty-five minutes. Training models comes in the next course, Machine Learning with scikit-learn. But first, your capstone. In the next lesson, you choose, load and audit a public dataset. See you there.

## Thumbnail
Headline: No Answers in Features
Image: Navy background, a clean numeric table with one teal target column and a crossed-out refund column, headline in teal Inter Bold.

## Production Notes
- [VERSION] The Colab file panel and its download option must be checked against the live interface before recording.
- Judgement call (curriculum): the course ends at an ML-ready table; train/test splits, scaling and modelling are left to AI-12. The voiceover names the next course only as 'the next course, Machine Learning with scikit-learn'.
- The order data is synthetic, created for this course. Anjali (Pune) is fictional.
- Printed outputs on screen must match content.md: the returned / refund head(3) table (no 0.0 / yes 12.0 / no 0.0), '(8, 11)', the 11-column list, and 'True'.
- Before the demo, run the L14, L16 and L17 cells on screen (or show them already run) so encoded exists.
