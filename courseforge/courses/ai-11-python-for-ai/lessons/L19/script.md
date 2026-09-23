# L19 Capstone Step 1: Choose, Load and Audit a Public Dataset | Presenter Script

Course: AI-11 · Video: 5 min · Words: 653

## Hook
Until now, you have worked with small practice tables. Real public datasets are bigger, messier, and more interesting. In this lesson, you choose one, ask your own question about it, and find out what condition it is in.

## Explain
Last time, we built an ML-ready table. Now it is time for your capstone. It is a notebook that takes a real public dataset from raw file to an ML-ready table. It has two steps. Today, you choose, load and audit. In the next lesson, you clean, explore and document.

A good first dataset has a clear question you care about, and a manageable size, from a few hundred to a few hundred thousand rows. It comes as a table, with one row per example. It has a clear licence and a named source. And it has some imperfections, or there is nothing to audit.

Good places to browse include World Bank Open Data, Our World in Data, the UCI Machine Learning Repository, and Kaggle. Licences differ between sites and between datasets, so always read the licence on the dataset's own page, and write it in your notebook.

Also check that the data contains no personal information about people who can be identified. If it does, choose another dataset. And never upload personal or confidential data from your job into Colab, or into any AI tool.

Choosing a dataset is like choosing a used car. You check the papers first, the licence and the source. Then you look under the bonnet, which is the audit, before you drive anywhere. A few scratches are fine, if you know where they are. But a car with no papers is a risk, however good it looks.

## Demonstrate
Let's set up a capstone notebook. Yusuf is an agricultural extension officer in Kampala, Uganda. His question, which is just an example, is this. In countries with similar rainfall, is fertiliser use linked to cereal yield?

He creates a new notebook and adds five text headings, in order. Question, Source, Load, Audit, and Cleaning log. The cleaning log stays empty until the next lesson. Under Source, he records the name, the web address, the download date and the licence.

Then he uploads the downloaded file with the Colab file panel, loads it with read csv, and takes a first look with head and info.

Next, he writes a reusable audit function, so he can run the same checks again after cleaning. It prints the shape, the number of duplicate rows, the missing values in each column that has some, and the list of text columns.

To show that it works, we test it on the synthetic order data from lesson fourteen. Eleven rows, one duplicate, a missing date and payment, and five text columns. Exactly what we found by hand.

On his real data, Yusuf runs the audit, then describe, unique on the category columns, and a quick histogram. He writes each problem in the Audit section, marked as an error or needing a decision.

A common mistake is choosing a dataset that is too large or complex, and spending the whole week on loading problems. Before you commit, ask one question. Does this table have a column I can use as a target, and columns that could explain it? If not, choose again now.

## Recap
Let's recap. First, choose a public dataset with a clear question, a manageable size, a table format, and a licence that allows your use. Second, record the source, download date and licence before any analysis. Third, audit the data with reusable code, and list every problem before you start cleaning.

## CTA
Now it is your turn. This exercise is step one of your capstone. Choose a dataset, write your question, load the data, and complete a full audit in your notebook. Give yourself about forty-five minutes. In the next and final lesson, Capstone Step Two, you clean, explore and document your notebook. See you there.

## Thumbnail
Headline: Choose Your Real Dataset
Image: Navy background, a magnifying glass over a large data table with a licence tag attached, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Licence terms of World Bank Open Data, Our World in Data, the UCI Machine Learning Repository and Kaggle datasets (Kaggle licences vary per dataset, and Kaggle needs a free account). The voiceover names the four sources only as places to browse and tells learners to check each licence on the dataset's own page; it makes no claim about any licence.
- [VERSION] Uploading files through the Colab file panel must be checked against the live interface before recording.
- Yusuf's question is hypothetical; no dataset or result is claimed. Screen scenes use a placeholder file name (file_name.csv) and do not show a real dataset's contents or findings. If the team wants to show a real file, pick one whose licence has been checked and add it to these notes.
- The audit function demo runs on the synthetic order data from L14. Printed output must match content.md: 'Shape: (11, 8) / Duplicate rows: 1 / Missing values: / order_date 1 / payment 1 / dtype: int64 / Text columns: ['city', 'order_date', 'unit_price', 'payment', 'returned']'.
- Stock footage of farms or fields must show no readable brand names or logos.
