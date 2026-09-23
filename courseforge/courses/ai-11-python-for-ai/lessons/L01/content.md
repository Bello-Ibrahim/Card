# L01 Welcome to Python and Google Colab

Course: AI-11 · Module: M1 · Objectives: O1 · Video: 5 min (screen demo)

## Hook
Most of the AI tools you hear about were prepared, tested or trained with the same programming language: Python. In the next five minutes you will write your first line of Python, run it, and see the result, without installing anything on your computer.

## Explanation
A **program** is a list of instructions that a computer follows exactly, in order. A **programming language** is a way to write those instructions so that both people and computers can read them.

Python is the most common language for data and AI work, for two reasons:

- **It is readable.** Python code often looks close to plain English. A line such as `print("Hello")` does what it says: it prints (shows) the word Hello.
- **It has a very large set of free libraries.** A library is a package of ready-made code that other people wrote and shared. For data and AI there are free libraries for tables of data, charts, maths and machine learning. You will use one of them, pandas, from week 3.

In this course you write Python in **Google Colab**, a free notebook that runs in your web browser. The code runs on a computer owned by Google, not on your own machine, so you only need a browser and a Google account. [VERSION]

A Colab notebook is made of **cells**. There are two kinds:

- **Code cells** hold Python. When you run a code cell, the result appears directly below it.
- **Text cells** hold notes, headings and explanations, written in plain language.

**Analogy:** A notebook is like a scientist's lab notebook. On one page the scientist writes what they plan to test and why. Next to it they record the experiment and its result. In Colab, text cells are the notes and code cells are the experiments, and they sit side by side so anyone can follow the work later.

Your notebook is saved to your Google Drive, in a folder that Colab creates. The free version of Colab has limits, for example on how long a session can stay open and how much computing power you get. These limits change, so check the current details on the Colab website. [VERSION]

Colab may not be available in every country or on every network. If you cannot use it, you can install Python and VS Code on your own computer. Lesson L10 shows how. [REGION]

## Worked Example
Here is what the presenter does on screen. Follow along in your own browser.

1. Open colab.research.google.com and sign in with a Google account. [VERSION]
2. Choose **New notebook**. A notebook called "Untitled0.ipynb" opens with one empty code cell. [VERSION]
3. Click the file name at the top and rename it "L01 first notebook".
4. Click inside the code cell and type:

```python
print("Habari! Karibu kwenye Python.")
print(7 * 24)
```

5. Press **Shift + Enter**, or click the round play button to the left of the cell. The first run can take a few seconds while Colab connects. [VERSION]

The output appears under the cell:

```
Habari! Karibu kwenye Python.
168
```

The first line prints a greeting in Swahili. The text is inside quotation marks, so Python shows it exactly as written. The second line has no quotation marks, so Python calculates 7 × 24 (the hours in a week) and prints the answer.

6. Choose **+ Text** to add a text cell. Type a heading such as "My first notebook" and one sentence about what the code does.
7. Open the **File** menu and choose **Save**. The notebook is now in your Google Drive. [VERSION]

## Common Mistake
Many beginners type code into a text cell and wonder why nothing happens. Text cells do not run code: they only display notes. Check the cell type before you type. A code cell has a play button on its left side. A second common mistake is forgetting the quotation marks around text. `print(Habari)` produces an error, because Python thinks `Habari` is a name it should already know. You will learn to read these error messages in L08.

**Safety note:** Colab notebooks are stored in your Google account and can be shared. Do not type passwords, ID numbers or other personal or confidential data into a notebook.

## Key Takeaways
1. Python is widely used for AI because it is readable and has many free libraries for data and machine learning.
2. Google Colab runs Python in your browser. Code cells run code; text cells hold your notes.
3. Run a cell with Shift + Enter, and the result appears directly below it.

## Hands-on Exercise
**Task:** Create your first Colab notebook with a greeting and a personal goal.
**Tools:** Google Colab (free, in a web browser) and a Google account. If Colab is not available to you, read L10 and use Python in VS Code instead.
**Steps:**
1. Open Colab and create a new notebook. Rename it "AI-11 my notebook".
2. In the first code cell, write a `print()` line that shows a greeting in your own language. Run it.
3. Add a second line that prints the result of a calculation, such as the number of minutes in a day (`24 * 60`). Run the cell again.
4. Add a text cell above the code. Write your first name and one goal for this course, for example "I want to clean my shop's sales data".
5. Save the notebook and check that it appears in your Google Drive.
**What good looks like:** A saved notebook with one text cell (name and goal) and one code cell that shows two lines of output: your greeting and a correct calculation. No error messages.
**Time:** about 15 minutes

## Review Flags
- [VERSION] Google Colab interface details must be checked against the live tool before scripting: the New notebook option, the default file name, the play button, the + Text button, the File > Save menu and the first-connection delay. Free-tier limits and session length also change.
- [REGION] Google Colab may not be available in every country or on every network. The lesson points to local Python with VS Code (L10) as the fallback; Jupyter is another option.
