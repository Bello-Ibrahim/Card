# L14 Finding Data Quality Problems | Presenter Script

Course: AI-11 · Video: 5 min · Words: 673

## Hook
A machine learning model learns whatever is in its data, including the mistakes. If a quantity of minus two, or a copied row, goes into training, the model treats it as truth. So before you clean anything, you need to find the problems.

## Explain
Last time, we summarised clean practice data. Real data is rarely clean. A data audit is a systematic check of a dataset for problems, done before cleaning. You don't fix anything yet. You make a list.

Think of a mechanic's inspection before a repair. The mechanic walks around the car with a checklist. Tyres, lights, brakes, oil. They write down every problem first, and only then decide what to fix, and in what order. If you start repairs too early, you fix the first thing you notice, and miss the dangerous one.

Five checks find most problems. First, missing values. Is na, followed by sum, counts the empty cells in each column. Second, duplicates, which are rows that copy an earlier row exactly. Third, wrong types. A price column stored as text means at least one value could not be read as a number.

Fourth, inconsistent categories. Unique lists every different spelling, and to a computer, Lima in capitals is a different value. Fifth, impossible values and outliers. An impossible value cannot be true, like a negative quantity. An outlier is possible but unusual. Outliers need a human decision, not automatic deletion.

For each problem, write down what you found, where, and the code that found it. This list becomes your cleaning plan in lesson sixteen.

## Demonstrate
Let's audit a real-looking file. Oluwaseun is an operations analyst for an online marketplace with shops in Lagos, Hanoi and Lima. He receives an export of recent orders. The data is synthetic, made up for this course.

We paste one cell that holds eleven orders as CSV text, and read it into a DataFrame called orders. We use this same file for the next three lessons.

Now three checks. First, missing values. A short extra step keeps only the columns that have at least one. One order date and one payment method are missing. Second, duplicates. There is one copied row. Third, the city spellings. Six different spellings, for only three cities.

Dtypes shows that the price and the date are both stored as text. To find the bad price, we try to convert the column to numbers. Any value that fails becomes missing, and we show those rows. It is order ten oh five, with the price unknown.

Finally, the quantity. The minimum is minus two, which is impossible. The median is two. And the maximum is five hundred. That is possible, but very unusual.

Here is Oluwaseun's audit list. One duplicate row. A missing date and a missing payment method. A price stored as text. Dates stored as text. Six spellings for three cities. An impossible quantity of minus two. And a possible outlier of five hundred units, to confirm with the Lima shop. Each item has the order number and the code that found it.

A common mistake is fixing the first problem you see, like deleting the five hundred unit order. It may be a real bulk order from a genuine customer. Complete the audit first. And look at the minimum, median and maximum, not only the mean. Here, one outlier pulls the mean quantity up to forty-seven, which describes no real order.

## Recap
Let's recap. First, audit before you clean. List every problem, and the code that found it. Second, use five checks for missing values, copies, wrong types, spellings and extreme values. Third, impossible values are errors, but outliers are questions that need a human decision.

## CTA
Now it is your turn. In the exercise below this video, you will audit the messy order file, and list every problem you find, with the code that found it. Mark each one as an error, or as a question for a person. It takes about twenty-five minutes. In the next lesson, we explore data with charts. See you there.

## Thumbnail
Headline: Audit Before You Clean
Image: Navy background, a clipboard checklist next to a data table with several cells circled in orange, headline in teal Inter Bold.

## Production Notes
- The order data is synthetic, created for this course; label it on screen as 'Synthetic data, made up for this course'. Prices are in US dollars. Oluwaseun and the marketplace are fictional.
- [VERSION] Text column dtype names (str in pandas 3, object in earlier versions) and printed output formats differ between pandas versions. content.md outputs were produced with Python 3.11 and pandas 3.0.6. The voiceover says 'text' and does not name the dtype.
- Curriculum [VERIFY] flag for Gapminder does not apply: this lesson uses only the synthetic order data.
- Printed outputs on screen must match content.md: 'order_date 1 / payment 1 / dtype: int64', '1', "['Lagos', 'lagos ', 'Hanoi', 'Lima', 'LIMA', 'Ha Noi']", the order 1005 'unknown' row, and 'min -2.0 / 50% 2.0 / max 500.0'.
- Stock footage of market or delivery scenes must show no readable shop names or logos.
