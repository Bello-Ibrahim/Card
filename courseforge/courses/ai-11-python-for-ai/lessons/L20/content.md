# L20 Capstone Step 2: Clean, Explore and Document

Course: AI-11 · Module: M4 · Objectives: O6, O7 · Video: 5 min (screen demo)

## Hook
A notebook that only works on your screen, in the order you happened to run the cells, is not finished. A finished notebook runs from top to bottom for anyone, and explains every decision along the way. Today you get your capstone to that point.

## Explanation
In L19 you chose a dataset, wrote a question and audited the data. Now you complete the notebook in four parts.

**1. Clean, with a justified log.** Work through your audit list with the tools from L16 and L17: remove duplicates, handle missing values, fix types, standardise text and deal with impossible values. After each step, print the shape. Add a row to the cleaning log for each decision: problem, action, rows affected and a one-line reason. Then run your `audit()` function again to show that the problems are gone.

**2. Explore with 3 or more charts.** Use the chart types from L15 to explore your question: a histogram for a key number column, a bar chart comparing groups (often from a `groupby` table), and a scatter plot for a relationship. Each chart needs a title, axis labels with units and one sentence of insight below it. Describe patterns without claiming causes.

**3. Build the ML-ready table.** Following L18, choose the target, keep numeric features, remove identifiers and leaky columns, and save the table to CSV.

**4. Check reproducibility.** A notebook is **reproducible** when it gives the same results every time it runs from a fresh start. Hidden problems appear only after a restart: a variable you created in a cell you later deleted, or cells that only work in a certain order. In Colab, use the menu option that restarts the session and runs all cells. [VERSION] Fix every error and run it again until it completes without errors.

Simple `assert` checks help: `assert condition, "message"` does nothing if the condition is True and stops with an AssertionError and your message if it is False.

**Analogy:** Checking reproducibility is like testing a recipe by giving it to a friend and watching them cook it in their own kitchen. If they need to ask "which pan?" or "when do I add the salt?", the recipe is not finished. "Restart and run all" is your notebook cooking in a clean kitchen with nobody to ask.

**Sharing.** You can share the notebook with a Colab link (use the Share button and choose who can view), or save a copy to a GitHub repository from the File menu. [VERSION] Before you share, check that the notebook contains no passwords, API keys or personal data, and that the data licence allows sharing.

## Worked Example
Camila is a secondary-school teacher in Asunción, Paraguay. For her capstone she uses a hypothetical public dataset of daily air-quality readings. Her audit found missing readings, a date column stored as text and a few negative pollution values.

The presenter shows the final checks from her notebook. To keep the demo short, they are shown on the order table `ml` from L18:

```python
assert ml.isna().sum().sum() == 0, "missing values remain"
assert ml.select_dtypes("number").shape[1] == ml.shape[1], "non-numeric column"
print("Checks passed:", ml.shape)
```

```
Checks passed: (8, 11)
```

Then the presenter walks through the finished structure of Camila's notebook:

1. **Question** and **Source** (with licence and download date).
2. **Load** and **Audit**, ending with a problem list.
3. **Cleaning**, one decision per cell, and the cleaning log table: for example, "Negative readings (14 rows): removed, because a pollution level cannot be below 0."
4. **Exploration**: 3 labelled charts, each with one sentence of insight.
5. **ML-ready table**: target, features, removed columns with reasons, and the saved CSV.
6. **Limits**: 2 or 3 sentences, such as "Readings from one station are missing for a full month, so the monthly pattern for that station is uncertain."

Finally, the presenter uses the Colab option to restart and run all cells, and scrolls from top to bottom to show that every cell has run without errors. [VERSION]

## Common Mistake
The most common problem is a notebook that works only on the author's computer: it reads a file from a local folder such as `C:/Users/...`, or it depends on a file that was uploaded in a previous session. After a restart, the file is gone. Load data from a stable web address where the licence allows it, or explain clearly in the notebook where to download the file and how to upload it. Then test with "restart and run all".

## Key Takeaways
1. A complete capstone notebook has a question, source, audit, justified cleaning log, 3+ labelled charts with insights, an ML-ready table and a note on limits.
2. Restart and run all cells to prove the notebook is reproducible, and use `assert` to check key conditions.
3. Share with a Colab link or a GitHub copy, only after checking for private data and licence terms.

## Hands-on Exercise
**Task:** Capstone step 2: finish, run from top to bottom without errors, and share your data-cleaning and exploration notebook.
**Tools:** Google Colab (free) with pandas and matplotlib; optional free GitHub account.
**Steps:**
1. Clean the data, one decision per cell, and complete the cleaning log with a reason for each row.
2. Run `audit()` again and compare the result with your L19 audit.
3. Make at least 3 labelled charts, each with one sentence of insight.
4. Build and save the ML-ready table, and list the removed columns with reasons.
5. Add a "Limits" section of 2 or 3 sentences.
6. Add at least 2 `assert` checks, then restart and run all cells. Fix any errors and repeat.
7. Check for private data, then share a Colab view link or save a copy to GitHub.
**What good looks like:** A notebook that runs from top to bottom without errors after a restart, with every section from the template complete, and a link that a reviewer can open. See the capstone rubric for the full criteria.
**Time:** about 60 minutes

## Review Flags
- [VERSION] The Colab menu option that restarts the session and runs all cells, the Share button options and the File menu option to save a copy to GitHub must be checked against the live interface before recording.
- Camila's dataset and findings are hypothetical, and the demo code runs on the synthetic order data.
