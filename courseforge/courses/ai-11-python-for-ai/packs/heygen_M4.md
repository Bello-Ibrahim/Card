# HeyGen Batch Pack: AI-11 M4 (Preparing Data for Machine Learning)

Course: Python for AI. Make one HeyGen video per lesson below, using these settings for every video.

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

## L16 Cleaning Data: Missing Values, Duplicates and Types

- **Filename:** `ai-11-python-for-ai_M4_L16_presenter.mp4`
- **Expected length:** about 4.9 minutes (684 words). The quality gate accepts ±10%.

```text
You found the problems. Now you must decide what to do about each one. There is rarely a single correct answer, and every choice changes what a future model will learn. That is why a good analyst writes down each decision, and the reason for it.

We are now in week four. In lesson fourteen, we audited a messy order file. Today, we clean it. Drop duplicates removes rows that copy an earlier row. Dropna removes rows with missing values. Always give it a subset, the column you care about. Without one, it removes rows with any missing value, which can be far more than you expect.

Fillna fills missing values instead. Use the mean for number columns without extreme values, the median when there are extreme values, the most common value for categories, or a label such as unknown. To fix types, to numeric converts text to numbers, and to datetime converts text to real dates.

Every choice has a cost. Dropping rows loses information. If most missing values come from one city, dropping them removes that city's customers. Filling keeps the rows, but invents numbers, and hides the fact that data was missing. A filled value is a guess.

Cleaning data is like restoring an old building. The restorer decides, room by room, whether to repair, replace or remove. Each decision is photographed and written in a record, so future owners know which walls are original. Your record is a cleaning log. For each problem, it lists the action, the rows affected, and a one-line reason.

Two more rules. Work on a copy, and never overwrite the raw file. And write every cleaning step as code, so it can run again on new data.

Let's clean it. Linh is a junior data analyst at the same marketplace, with shops in Lagos, Hanoi and Lima. She uses the synthetic order data from lesson fourteen.

We make a new table called clean. First, we drop the duplicate. Then we keep only rows with a quantity above zero. Then we drop the row with no order date, and make a copy, so later changes don't affect the original.

Next, the price. We convert it to numbers, so unknown becomes missing, and fill it with the median price. Then we convert the dates to real dates. Finally, we print the shape and the total count of missing values.

Run it. Eight rows and eight columns, and zero missing values. The table went from eleven rows to eight. The price is now a number column, and the order date is a date column.

Now Linh writes her cleaning log in a text cell. The duplicate was counted twice by mistake. Minus two is impossible. A missing date cannot be guessed. The unknown price is filled with the median, because prices vary widely. Dates become real dates for the next lesson. And the five hundred unit order is kept and flagged, while she waits for the Lima shop.

She also notes one cost. Order ten oh seven was one of only two returned orders. So dropping it removes half of the returns. She adds this to the log as a risk.

A common mistake is running dropna with no subset, to be safe. In a real dataset, almost every row has an empty cell somewhere, so this can delete most of your data without any message. Check the shape before and after each step.

Let's recap. First, use drop duplicates, dropna with a subset, fillna, to numeric, to datetime and filters to fix the problems from your audit. Second, dropping loses information and filling invents values, so choose based on the column and the cost. Third, record every decision in a cleaning log, and check the shape after each step.

Now it is your turn. In the exercise below this video, you will clean the messy order file, and write a one-line reason for each decision in your cleaning log. It takes about thirty minutes, and it is great practice for your capstone. In the next lesson, we shape features from text, categories and dates. See you there.
```

## L17 Shaping Features: Text, Categories and Dates

- **Filename:** `ai-11-python-for-ai_M4_L17_presenter.mp4`
- **Expected length:** about 4.8 minutes (665 words). The quality gate accepts ±10%.

```text
To a person, Lima in capitals, Lima with a space, and Lima written normally are the same city. To a computer, they are three different values. And a machine learning model cannot use the word Lima at all. It needs numbers.

Last time, we cleaned the order data. Now we shape it for a model. A feature is a column that a model uses to make a prediction. Most models only work with numbers, so text and dates must be converted. We usually do this in four steps.

Step one, clean the text. The str methods work on a whole column at once. Strip removes spaces at the start and end. Lower makes all letters lowercase. And replace swaps one spelling for another. You can chain them, one after another.

Step two, group rare categories. A category that appears only once or twice gives a model very little to learn from. So replace rare values with a shared label, such as other. Choose the threshold, and record it in your cleaning log.

Step three, one-hot encoding. Get dummies creates one new column for each category, with one where the row has that category, and zero elsewhere. Why not just number the cities one, two and three? Because a model would think Lima, number three, is more than Lagos, number two. That has no meaning.

Think of a form with tick boxes, instead of a blank line. A blank line invites many spellings. Tick boxes give every answer the same shape, and a computer can count ticks easily. Each box becomes one column, with one for ticked and zero for empty.

The default output of get dummies depends on your pandas version, so add dtype equals int to always get zeros and ones. Step four, extract date parts. A full date is hard for a model to use, but its parts often matter. The dt tools give you the year, the month, and the day of the week, where zero is Monday.

Let's shape the data. Hamza is a data analyst in Rabat, Morocco, helping the same marketplace. He starts from the clean table from the last lesson, with eight orders and no missing values.

First, the city column. We strip the spaces, make it lowercase, and replace the spelling with a space in Hanoi. Value counts shows Lagos three, Lima three, and Hanoi two. Six spellings became three cities.

Next, the date parts. We add a month column and a weekday column. The second of March, twenty twenty-six, is a Monday, so its weekday is zero.

Then Hamza counts the payment methods, and finds those with fewer than two rows. After cleaning, mobile appeared only once, so it becomes other. Finally, get dummies encodes city and payment, with dtype equals int.

Run it. Filter shows only the new city columns. Each row has a single one, in the column for its city. The table also has three new payment columns, for card, cash and other.

A common mistake is encoding before cleaning the text. Then two spellings of Lima become two separate columns, and the model sees two different cities. Standardise first, check with value counts, and only then encode. And never encode columns like names or order numbers, which create hundreds of useless columns. Group rare values, or leave such columns out.

Let's recap. First, clean text with strip, lower and replace, and check the result with value counts. Second, group rare categories, then one-hot encode with get dummies and dtype int, so each category becomes a column of zeros and ones. Third, extract useful parts of dates, such as month and weekday, with the dt tools.

Now it is your turn. In the exercise below this video, you will standardise a city column, one-hot encode it, and add weekday and month columns from the order date. It takes about twenty-five minutes, and you will use the same steps in your capstone. In the next lesson, we build an ML-ready table. See you there.
```

## L18 Building an ML-Ready Table

- **Filename:** `ai-11-python-for-ai_M4_L18_presenter.mp4`
- **Expected length:** about 4.7 minutes (652 words). The quality gate accepts ±10%.

```text
Imagine a model that predicts returned orders perfectly in testing, and then fails completely with real customers. One common reason is a column that secretly contained the answer. Today, you build a table a model can learn from honestly.

Last time, we turned text, categories and dates into numbers. Now we put it all together. An ML-ready table has a simple shape. One row per example, such as one order. One target column, the value you want to predict. And feature columns, all numeric, with no missing values.

Some columns must be removed before training. First, identifiers, such as an order number or a customer name. They are unique labels, not information. A model could memorise them, and that memory would be useless for new orders. Also remove raw columns you have already converted, like the original date.

Second, leaky columns. Data leakage happens when a feature contains information you would not have at the moment of prediction, often because it is created after the outcome. A refund exists only because an order was returned. So it reveals the answer.

Leakage is like an exam with the answers printed faintly on the back of the question paper. A student who notices them gets full marks, but learns nothing, and fails the next exam. A model with a leaky column is that student.

To test any column for leakage, ask one question. At the moment I want to make the prediction, would I already know this value? If the answer is no, remove it.

Let's build one. Anjali is a data analyst in Pune, India. The marketplace asks her to prepare a table for a future model that predicts whether an order will be returned. She starts from Hamza's encoded table.

First, she looks at the returned and refund columns side by side. See the pattern? The refund is above zero only when the order was returned. That is leakage.

Next, she makes a copy called ml. The target, returned, becomes one for yes and zero for no. The comparison with yes gives True or False, and as type int turns that into one or zero. Then she drops three columns. The order number, which is an identifier. The refund, which leaks. And the order date, which is already converted.

Run it. Eight rows and eleven columns. The target, plus quantity, price, month, weekday, three city columns and three payment columns.

She checks that every column is numeric. The answer is True. Then she saves the table as a CSV file. Index equals False stops pandas from writing the row labels as an extra column.

Finally, Anjali adds a warning to her notes. Only one order out of eight was returned. That is enough to practise the steps, but far too few for a real model. A real project needs many examples of each outcome.

A common mistake is keeping every column, because more data seems better. Identifiers and leaky columns make a model look better in testing, and worse in real use. The opposite mistake also happens, removing useful features because they look similar to the target. Ask the timing question for each column, and write down why you kept or removed it.

Let's recap. First, an ML-ready table has one row per example, one target column, and only numeric features with no missing values. Second, remove identifiers, leaky columns and raw columns you have already converted. Third, save the result with index equals False, and note any limits, such as too few examples of one outcome.

Now it is your turn. In the exercise below this video, you will choose a target and five features, explain why you removed two columns, and save an ML-ready CSV. It takes about twenty-five minutes. Training models comes in the next course, Machine Learning with scikit-learn. But first, your capstone. In the next lesson, you choose, load and audit a public dataset. See you there.
```

## L19 Capstone Step 1: Choose, Load and Audit a Public Dataset

- **Filename:** `ai-11-python-for-ai_M4_L19_presenter.mp4`
- **Expected length:** about 4.7 minutes (650 words). The quality gate accepts ±10%.

```text
Until now, you have worked with small practice tables. Real public datasets are bigger, messier, and more interesting. In this lesson, you choose one, ask your own question about it, and find out what condition it is in.

Last time, we built an ML-ready table. Now it is time for your capstone. It is a notebook that takes a real public dataset from raw file to an ML-ready table. It has two steps. Today, you choose, load and audit. In the next lesson, you clean, explore and document.

A good first dataset has a clear question you care about, and a manageable size, from a few hundred to a few hundred thousand rows. It comes as a table, with one row per example. It has a clear licence and a named source. And it has some imperfections, or there is nothing to audit.

Good places to browse include World Bank Open Data, Our World in Data, the UCI Machine Learning Repository, and Kaggle. Licences differ between sites and between datasets, so always read the licence on the dataset's own page, and write it in your notebook.

Also check that the data contains no personal information about people who can be identified. If it does, choose another dataset. And never upload personal or confidential data from your job into Colab, or into any AI tool.

Choosing a dataset is like choosing a used car. You check the papers first, the licence and the source. Then you look under the bonnet, which is the audit, before you drive anywhere. A few scratches are fine, if you know where they are. But a car with no papers is a risk, however good it looks.

Let's set up a capstone notebook. Yusuf is an agricultural extension officer in Kampala, Uganda. His question, which is just an example, is this. In countries with similar rainfall, is fertiliser use linked to cereal yield?

He creates a new notebook and adds five text headings, in order. Question, Source, Load, Audit, and Cleaning log. The cleaning log stays empty until the next lesson. Under Source, he records the name, the web address, the download date and the licence.

Then he uploads the downloaded file with the Colab file panel, loads it with read csv, and takes a first look with head and info.

Next, he writes a reusable audit function, so he can run the same checks again after cleaning. It prints the shape, the number of duplicate rows, the missing values in each column that has some, and the list of text columns.

To show that it works, we test it on the synthetic order data from lesson fourteen. Eleven rows, one duplicate, a missing date and payment, and five text columns. Exactly what we found by hand.

On his real data, Yusuf runs the audit, then describe, unique on the category columns, and a quick histogram. He writes each problem in the Audit section, marked as an error or needing a decision.

A common mistake is choosing a dataset that is too large or complex, and spending the whole week on loading problems. Before you commit, ask one question. Does this table have a column I can use as a target, and columns that could explain it? If not, choose again now.

Let's recap. First, choose a public dataset with a clear question, a manageable size, a table format, and a licence that allows your use. Second, record the source, download date and licence before any analysis. Third, audit the data with reusable code, and list every problem before you start cleaning.

Now it is your turn. This exercise is step one of your capstone. Choose a dataset, write your question, load the data, and complete a full audit in your notebook. Give yourself about forty-five minutes. In the next and final lesson, Capstone Step Two, you clean, explore and document your notebook. See you there.
```

## L20 Capstone Step 2: Clean, Explore and Document

- **Filename:** `ai-11-python-for-ai_M4_L20_presenter.mp4`
- **Expected length:** about 5.0 minutes (700 words). The quality gate accepts ±10%.

```text
A notebook that only works on your screen, in the order you happened to run the cells, is not finished. A finished notebook runs from top to bottom for anyone, and explains every decision. Today, you get your capstone to that point.

In the last lesson, you chose a dataset, wrote a question and ran an audit. Now you complete the notebook in four parts. Part one is cleaning. Work through your audit list, print the shape after each step, and add a row to your cleaning log for every decision. Then run your audit function again, to show the problems are gone.

Part two is exploring, with three or more charts. A histogram, a bar chart and a scatter plot, each with a title, axis labels with units, and one sentence of insight. Describe patterns, but don't claim causes. Part three is the ML-ready table, following lesson eighteen.

Part four is checking reproducibility. A notebook is reproducible when it gives the same results every time it runs from a fresh start. Hidden problems appear only after a restart. For example, a variable from a cell you later deleted. So restart the session, run all cells, and fix every error, until it completes cleanly.

It is like testing a recipe by giving it to a friend, and watching them cook it in their own kitchen. If they need to ask which pan, the recipe is not finished. Restart and run all is your notebook cooking in a clean kitchen, with nobody to ask.

Simple assert checks help too. An assert does nothing if its condition is true, and stops with your message if it is false. When you are ready, share a Colab link, or save a copy to GitHub. But first, check for passwords, keys or personal data, and check that the licence allows sharing.

Let's look at a finished notebook. Camila is a secondary school teacher in Asunción, Paraguay. For her capstone, she uses an example dataset of daily air quality readings. Her audit found missing readings, dates stored as text, and a few negative pollution values.

First, her final checks. To keep the demo short, we run them on the order table from lesson eighteen. One assert checks that no values are missing. Another checks that every column is numeric. Both pass, and we see eight rows and eleven columns.

Now her notebook's structure. It starts with the question and the source, with the licence and download date. Then loading and the audit, ending with a problem list. Then cleaning, one decision per cell, and the log. For example, negative readings were removed, because pollution cannot be below zero.

Next, three labelled charts, each with a sentence of insight. Then the ML-ready table, with the removed columns and their reasons, and the saved file. And finally, a short Limits section. For example, one station is missing a full month, so that month's pattern is uncertain.

Last, we restart the session and run all cells. Then we scroll from top to bottom. Every cell has run, and there are no errors. The notebook is ready to share.

The most common problem is a notebook that only works on its author's computer. It reads a file from a local folder, or a file uploaded in an earlier session. After a restart, the file is gone. Load from a stable web address where the licence allows, or explain how to get the file. Then test with restart and run all.

Let's recap. First, a complete capstone has a question, a source, an audit, a justified cleaning log, three or more labelled charts, an ML-ready table and a note on limits. Second, restart and run all cells to prove your notebook is reproducible, and use assert to check key conditions. Third, share it only after checking for private data and licence terms.

Congratulations. Four weeks ago, you wrote your first line of Python. Today, you can clean and explore a real dataset. Now finish your capstone. Run it from top to bottom, check it against the rubric, and submit your shared link. It takes about an hour. When you are ready, Machine Learning with scikit-learn is your next step. Well done.
```
