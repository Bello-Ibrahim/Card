# L17 Shaping Features: Text, Categories and Dates | Presenter Script

Course: AI-11 · Video: 5 min · Words: 671

## Hook
To a person, Lima in capitals, Lima with a space, and Lima written normally are the same city. To a computer, they are three different values. And a machine learning model cannot use the word Lima at all. It needs numbers.

## Explain
Last time, we cleaned the order data. Now we shape it for a model. A feature is a column that a model uses to make a prediction. Most models only work with numbers, so text and dates must be converted. We usually do this in four steps.

Step one, clean the text. The str methods work on a whole column at once. Strip removes spaces at the start and end. Lower makes all letters lowercase. And replace swaps one spelling for another. You can chain them, one after another.

Step two, group rare categories. A category that appears only once or twice gives a model very little to learn from. So replace rare values with a shared label, such as other. Choose the threshold, and record it in your cleaning log.

Step three, one-hot encoding. Get dummies creates one new column for each category, with one where the row has that category, and zero elsewhere. Why not just number the cities one, two and three? Because a model would think Lima, number three, is more than Lagos, number two. That has no meaning.

Think of a form with tick boxes, instead of a blank line. A blank line invites many spellings. Tick boxes give every answer the same shape, and a computer can count ticks easily. Each box becomes one column, with one for ticked and zero for empty.

The default output of get dummies depends on your pandas version, so add dtype equals int to always get zeros and ones. Step four, extract date parts. A full date is hard for a model to use, but its parts often matter. The dt tools give you the year, the month, and the day of the week, where zero is Monday.

## Demonstrate
Let's shape the data. Hamza is a data analyst in Rabat, Morocco, helping the same marketplace. He starts from the clean table from the last lesson, with eight orders and no missing values.

First, the city column. We strip the spaces, make it lowercase, and replace the spelling with a space in Hanoi. Value counts shows Lagos three, Lima three, and Hanoi two. Six spellings became three cities.

Next, the date parts. We add a month column and a weekday column. The second of March, twenty twenty-six, is a Monday, so its weekday is zero.

Then Hamza counts the payment methods, and finds those with fewer than two rows. After cleaning, mobile appeared only once, so it becomes other. Finally, get dummies encodes city and payment, with dtype equals int.

Run it. Filter shows only the new city columns. Each row has a single one, in the column for its city. The table also has three new payment columns, for card, cash and other.

A common mistake is encoding before cleaning the text. Then two spellings of Lima become two separate columns, and the model sees two different cities. Standardise first, check with value counts, and only then encode. And never encode columns like names or order numbers, which create hundreds of useless columns. Group rare values, or leave such columns out.

## Recap
Let's recap. First, clean text with strip, lower and replace, and check the result with value counts. Second, group rare categories, then one-hot encode with get dummies and dtype int, so each category becomes a column of zeros and ones. Third, extract useful parts of dates, such as month and weekday, with the dt tools.

## CTA
Now it is your turn. In the exercise below this video, you will standardise a city column, one-hot encode it, and add weekday and month columns from the order date. It takes about twenty-five minutes, and you will use the same steps in your capstone. In the next lesson, we build an ML-ready table. See you there.

## Thumbnail
Headline: Turn Words into Features
Image: Navy background, the words Lima, LIMA and lima merging into one, then splitting into three 0/1 columns, headline in teal Inter Bold.

## Production Notes
- [VERSION] pd.get_dummies default output type is True/False (bool) in pandas 2.0 and later, and 0/1 integers (uint8) in earlier versions. The lesson uses dtype=int so results match; the voiceover says only that the default depends on the version. Outputs were produced with Python 3.11 and pandas 3.0.6, and tested with pandas 2.2.3.
- The order data is synthetic, created for this course. Hamza (Rabat) is fictional.
- Printed outputs on screen must match content.md: value_counts 'lagos 3 / lima 3 / hanoi 2'; the order_date / month / weekday head(3) table (2026-03-02 3 0; 2026-03-02 3 0; 2026-03-03 3 1); and the city_hanoi / city_lagos / city_lima 0/1 table.
- Before the demo, run the L14 and L16 cells on screen (or show them already run) so clean exists.
