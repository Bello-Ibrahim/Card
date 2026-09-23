# L10 Working Locally: Files and VS Code

Course: AI-11 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Colab is excellent for learning and exploring. But many real projects run as scripts on a computer or a server, and they read and write files. Today you set up Python on your own machine and write a script that turns one file into another.

## Explanation
To work locally you need two free tools:

- **Python** itself, from python.org, or from your operating system's app store or package manager. [VERSION]
- **VS Code** (Visual Studio Code), a free code editor, with its **Python extension**, which adds colours, error hints and a Run button. [VERSION]

Installation steps differ between Windows, macOS and Linux, and between versions. Follow the current official instructions for your system. [VERSION] If you cannot install software, for example on a work laptop, you can do this lesson in Colab.

A **script** is a plain text file ending in `.py`. You run it from a **terminal** (a text window for commands). In VS Code, open the terminal from the menu and type `python summary.py` (on some systems, `python3 summary.py`). [VERSION]

Scripts often read and write files. The safe way is the `with` statement:

```python
with open("guests.csv", encoding="utf-8") as f:
    text = f.read()
```

`open()` connects to the file, and `with` closes it automatically when the indented block ends, even if an error happens. Use `"w"` as the second argument to write a new file (this replaces any existing file with the same name). `encoding="utf-8"` makes sure names with accents or other alphabets are read correctly. For CSV files (comma-separated values), the standard library `csv` module splits each line into columns for you.

**Notebook or script?** Use a notebook to explore data, try ideas and explain results with text and charts. Use a script for a task that must run the same way many times, such as a nightly report, or code that other programs will use.

**Analogy:** A notebook is like a whiteboard in a meeting room: good for thinking out loud and showing steps. A script is like a printed procedure pinned to the wall of a factory: fixed steps that anyone can run in exactly the same way every time.

## Worked Example
Nikolai manages a small guesthouse in Tbilisi, Georgia. He has a CSV file of guests and their home cities, and he wants a text summary of how many guests came from each city. The names and cities are made up.

The presenter does this on screen:

1. Create a folder called `ai11-local` and open it in VS Code with **File > Open Folder**. [VERSION]
2. Create a file `guests.csv` with this content:

```
name,city
Samira,Casablanca
Diego,Quito
Hana,Busan
Emeka,Casablanca
```

3. Create a file `summary.py`:

```python
import csv

with open("guests.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

cities = {}
for row in rows:
    cities[row["city"]] = cities.get(row["city"], 0) + 1

with open("summary.txt", "w", encoding="utf-8") as out:
    out.write(f"Guests: {len(rows)}\n")
    for city, count in cities.items():
        out.write(f"{city}: {count}\n")
print("Saved summary.txt")
```

`csv.DictReader` reads each line as a dictionary, using the first line as keys, so `row["city"]` gives the city. `cities.get(..., 0) + 1` counts each city: it starts at 0 for a new city. `\n` means "new line".

4. Open the terminal and run `python summary.py`. It prints `Saved summary.txt`.
5. Open `summary.txt`:

```
Guests: 4
Casablanca: 2
Quito: 1
Busan: 1
```

## Common Mistake
The most common problem is `FileNotFoundError`. The script looks for `guests.csv` in the terminal's current folder, not necessarily in the folder where the script is saved. Open the whole project folder in VS Code, keep the data file next to the script, and run the script from that folder. A second mistake is opening a file with `"w"` when you meant to read it, which empties the file. Keep a copy of original data files.

## Key Takeaways
1. Locally you need Python and VS Code with the Python extension; run scripts from the terminal with `python file.py`.
2. Use `with open(...)` to read and write files safely, with `"w"` to write and `encoding="utf-8"` for international text.
3. Notebooks suit exploring and explaining; scripts suit tasks that must run the same way many times.

## Hands-on Exercise
**Task:** In VS Code (or Colab if you cannot install software), write a script that reads a small CSV of names and cities and writes a summary text file.
**Tools:** Python and VS Code with the Python extension (free). Colab is the fallback: create the CSV with the file panel or by writing it from code.
**Steps:**
1. Install Python and VS Code, following the official instructions for your system.
2. Create a project folder and a `people.csv` file with at least 6 made-up names and cities, with at least one city repeated. Do not use real customers' personal data.
3. Write `summary.py` that reads the CSV with `csv.DictReader` inside a `with` block.
4. Count the people per city and write the total and each city count to `summary.txt`.
5. Run the script from the terminal, and open the output file to check it.
**What good looks like:** The script runs from the terminal without errors and creates `summary.txt` with a correct total and one line per city. The counts add up to the total.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Python and VS Code installation steps, the Python extension, the File > Open Folder menu, how to open the terminal and whether the command is python or python3 all differ by operating system and version. Check them against the current official instructions before recording.
