# L19 Capstone Step 1: Choose, Load and Audit a Public Dataset

Course: AI-11 · Module: M4 · Objectives: O5, O7 · Video: 5 min (screen demo)

## Hook
Until now you have worked with small practice tables. Real public datasets are bigger, messier and more interesting. In this lesson you choose one, ask your own question about it, and find out what condition it is in.

## Explanation
The capstone is a notebook that takes a real public dataset from raw file to an ML-ready table. It has two steps: this lesson (choose, load and audit) and L20 (clean, explore and document).

**Choosing a dataset.** Good first datasets have:

- **A clear question** you care about, such as "Which factors are linked to crop yield?" or "How does air quality change by month?"
- **A manageable size**: roughly a few hundred to a few hundred thousand rows, and 5 to 30 columns.
- **A table format** such as CSV, with one row per example.
- **A clear licence** that allows your use, and a named source you can cite.
- **Some imperfections.** A dataset that is already perfectly clean gives you nothing to audit.

**Suggested sources** (all free to browse):

- World Bank Open Data: country indicators on economy, health and education. [VERIFY]
- Our World in Data: charts and downloadable data on many global topics. [VERIFY]
- UCI Machine Learning Repository: datasets prepared for machine learning practice. [VERIFY]
- Kaggle: a very large collection of user-shared datasets. It needs a free account, and licences vary from dataset to dataset. [VERIFY]

**Check the licence** on the dataset's own page before you use it, and write it in your notebook. Some licences require you to credit the source; some do not allow commercial use. Also check that the data does not contain personal information about identifiable people. If it does, choose a different dataset. Never upload personal or confidential data from your job into Colab or any AI tool for this project.

**The notebook template.** Create these text-cell headings in order:

1. **Question**: one or two sentences.
2. **Source**: name, web address, download date and licence.
3. **Load**: the code that reads the file.
4. **Audit**: the checks from L14 and a list of problems.
5. **Cleaning log**: empty for now; you fill it in L20.

**Analogy:** Choosing a dataset is like choosing a used car. You check the papers first (the licence and the source), then you look under the bonnet (the audit) before you drive anywhere. A car with a few scratches is fine if you know where they are. A car with no papers is a risk, however good it looks.

## Worked Example
Yusuf is an agricultural extension officer in Kampala, Uganda. His hypothetical question: "In countries with similar rainfall, is fertiliser use linked to cereal yield?" He finds a country-level table on one of the suggested sources, reads the licence on the dataset page, and records it.

The presenter shows the steps on screen:

1. Create a new Colab notebook named "Capstone - cereal yield" and add the 5 template headings.
2. Upload the downloaded CSV with the Colab file panel, or read it directly from its web address. [VERSION]
3. Load and look: `df = pd.read_csv("file_name.csv")`, then `df.head()` and `df.info()`.
4. Define a reusable audit function, so the same checks can run again after cleaning:

```python
def audit(df):
    """Print a short data-quality report for a DataFrame."""
    print("Shape:", df.shape)
    print("Duplicate rows:", df.duplicated().sum())
    print("Missing values:")
    print(df.isna().sum()[lambda s: s > 0])
    print("Text columns:", df.select_dtypes(exclude="number").columns.tolist())
```

To show that it works, the presenter first runs it on the synthetic order data from L14:

```
Shape: (11, 8)
Duplicate rows: 1
Missing values:
order_date    1
payment       1
dtype: int64
Text columns: ['city', 'order_date', 'unit_price', 'payment', 'returned']
```

5. Run `audit(df)` on the real dataset, then add `describe()`, `unique()` on category columns, and a quick histogram of the main number columns.
6. Write the problem list in the Audit section, marking each item as "error" or "needs a decision".

## Common Mistake
Many learners choose a dataset that is too large or too complex, such as millions of rows or many linked files, and spend the whole week on loading problems. Others choose a question the data cannot answer. Before you commit, open the file, check the columns, and ask: "Does this table contain a column I can use as a target, and columns that could explain it?" If not, choose another dataset now, not in L20.

## Key Takeaways
1. Choose a public dataset with a clear question, a manageable size, a table format and a licence that allows your use.
2. Record the source, download date and licence in the notebook before any analysis.
3. Audit the data with reusable code and list every problem before you start cleaning.

## Hands-on Exercise
**Task:** Capstone step 1: choose a dataset, write your question, load the data, and complete a full data-quality audit in your notebook.
**Tools:** Google Colab (free) with pandas; one of the suggested sources (Kaggle needs a free account).
**Steps:**
1. Browse at least 2 sources and shortlist 3 datasets. Choose one, and write one sentence on why.
2. Create the notebook with the 5 template headings.
3. Write your question, and record the source, web address, download date and licence.
4. Load the data and run `head()`, `info()` and `describe()`.
5. Run the `audit()` function, check category spellings with `unique()` or `value_counts()`, and look for impossible values and outliers.
6. Write a problem list with the code that found each problem, and choose a possible target column.
**What good looks like:** A notebook with a clear question, a complete source and licence record, working load code, and an audit list of at least 4 problems (or a clear statement that a check found none), each backed by code.
**Time:** about 45 minutes

## Review Flags
- [VERIFY] Licence terms of World Bank Open Data, Our World in Data, the UCI Machine Learning Repository and Kaggle datasets (Kaggle licences vary per dataset, and Kaggle needs a free account).
- [VERSION] Uploading files through the Colab file panel must be checked against the live interface.
- Yusuf's question is hypothetical; no dataset or result is claimed.
