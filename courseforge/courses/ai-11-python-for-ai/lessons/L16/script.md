# L16 Cleaning Data: Missing Values, Duplicates and Types | Presenter Script

Course: AI-11 · Video: 5 min · Words: 686

## Hook
You found the problems. Now you must decide what to do about each one. There is rarely a single correct answer, and every choice changes what a future model will learn. That is why a good analyst writes down each decision, and the reason for it.

## Explain
We are now in week four. In lesson fourteen, we audited a messy order file. Today, we clean it. Drop duplicates removes rows that copy an earlier row. Dropna removes rows with missing values. Always give it a subset, the column you care about. Without one, it removes rows with any missing value, which can be far more than you expect.

Fillna fills missing values instead. Use the mean for number columns without extreme values, the median when there are extreme values, the most common value for categories, or a label such as unknown. To fix types, to numeric converts text to numbers, and to datetime converts text to real dates.

Every choice has a cost. Dropping rows loses information. If most missing values come from one city, dropping them removes that city's customers. Filling keeps the rows, but invents numbers, and hides the fact that data was missing. A filled value is a guess.

Cleaning data is like restoring an old building. The restorer decides, room by room, whether to repair, replace or remove. Each decision is photographed and written in a record, so future owners know which walls are original. Your record is a cleaning log. For each problem, it lists the action, the rows affected, and a one-line reason.

Two more rules. Work on a copy, and never overwrite the raw file. And write every cleaning step as code, so it can run again on new data.

## Demonstrate
Let's clean it. Linh is a junior data analyst at the same marketplace, with shops in Lagos, Hanoi and Lima. She uses the synthetic order data from lesson fourteen.

We make a new table called clean. First, we drop the duplicate. Then we keep only rows with a quantity above zero. Then we drop the row with no order date, and make a copy, so later changes don't affect the original.

Next, the price. We convert it to numbers, so unknown becomes missing, and fill it with the median price. Then we convert the dates to real dates. Finally, we print the shape and the total count of missing values.

Run it. Eight rows and eight columns, and zero missing values. The table went from eleven rows to eight. The price is now a number column, and the order date is a date column.

Now Linh writes her cleaning log in a text cell. The duplicate was counted twice by mistake. Minus two is impossible. A missing date cannot be guessed. The unknown price is filled with the median, because prices vary widely. Dates become real dates for the next lesson. And the five hundred unit order is kept and flagged, while she waits for the Lima shop.

She also notes one cost. Order ten oh seven was one of only two returned orders. So dropping it removes half of the returns. She adds this to the log as a risk.

A common mistake is running dropna with no subset, to be safe. In a real dataset, almost every row has an empty cell somewhere, so this can delete most of your data without any message. Check the shape before and after each step.

## Recap
Let's recap. First, use drop duplicates, dropna with a subset, fillna, to numeric, to datetime and filters to fix the problems from your audit. Second, dropping loses information and filling invents values, so choose based on the column and the cost. Third, record every decision in a cleaning log, and check the shape after each step.

## CTA
Now it is your turn. In the exercise below this video, you will clean the messy order file, and write a one-line reason for each decision in your cleaning log. It takes about thirty minutes, and it is great practice for your capstone. In the next lesson, we shape features from text, categories and dates. See you there.

## Thumbnail
Headline: Clean It, Log It
Image: Navy background, a messy table on the left, a clean table on the right, and a short log card below, headline in teal Inter Bold.

## Production Notes
- [VERSION] The date dtype shows as datetime64[us] in pandas 3 and datetime64[ns] in pandas 2. The voiceover says 'a date column' only. The code was tested without warnings in pandas 3.0.6 and 2.2.3 with Python 3.11.
- The order data is synthetic, created for this course; keep the on-screen label 'Synthetic data, made up for this course'. Linh is fictional.
- Printed output on screen must match content.md: '(8, 8) 0'. The cleaning log in the text cell must match the content.md table, including the median fill value 4.50.
- Before the demo, run the L14 data cell on screen (or show it already run) so orders exists.
