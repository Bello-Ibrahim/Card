# L09 Modules, Libraries and Installing Packages

Course: AI-11 · Module: M2 · Objectives: O1, O3 · Video: 5 min (screen demo)

## Hook
How many days until your next holiday? Which name should win a prize draw? You could write that code yourself, but you do not need to. Python already includes tested tools for both, and thousands more are free to install.

## Explanation
A **module** is a file of Python code that you can load into your program with `import`. Python comes with a large **standard library**: modules that are always available, with nothing to install. Three useful ones:

- `math`: square roots, rounding up and down, and other maths functions.
- `datetime`: dates, times and the difference between them.
- `random`: random numbers and random choices.

You can import a whole module (`import math`, then `math.sqrt(81)`) or one part of it (`from datetime import date`, then `date(2026, 12, 5)`).

A **library** or **package** is a larger collection of modules, often written by other people and shared for free. **Third-party** libraries are not part of Python itself; you install them. The most important ones for AI work:

- **NumPy**: fast calculations on large sets of numbers. Many other libraries are built on it. (Its maths is covered in AI-05.)
- **pandas**: tables of data, which you will use from L11.
- **matplotlib**: charts.

**Analogy:** The standard library is like the kitchen tools that come with a new flat: a pot, a pan, a few knives. Third-party libraries are like specialist tools you add later, such as a bread machine. `import` takes a tool out of the cupboard. Installing a package is buying the tool and putting it in the cupboard first.

Colab already has many data libraries installed, including pandas and matplotlib. If you need another one, you install it in a code cell with `%pip install package-name`. On your own computer, you install it in a terminal with `pip install package-name` (L10). The exact commands and the list of pre-installed libraries change over time. [VERSION]

Only install packages from trusted sources, and check the spelling of the name: a wrongly spelled package name can install a different, unwanted package.

## Worked Example
Valentina organises a charity book fair in Bogotá, Colombia. She wants to know how many days remain until the fair and to pick a prize winner from the volunteers. The date and names are made up.

The presenter types this into a new Colab cell:

```python
import math
import random
from datetime import date

print(math.sqrt(81), math.ceil(4.2))
fair = date(2026, 12, 5)
today = date(2026, 9, 23)
print((fair - today).days, "days to go")
```

```
9.0 5
73 days to go
```

`math.ceil` rounds up, which is useful for questions such as "how many boxes do I need?". Subtracting two dates gives a time difference, and `.days` turns it into a whole number. In real use, write `today = date.today()` to use the current date. Here a fixed date is used so the output is the same every time you run it.

Now the prize draw:

```python
random.seed(42)
names = ["Tariq", "Ingrid", "Chen", "Adaeze"]
print(random.choice(names))
```

```
Tariq
```

`random.seed(42)` makes the "random" result repeatable: with the same seed you get the same choice each time. This is important in data work, because other people must be able to reproduce your results. Remove the seed for a real draw.

Finally, the presenter checks the installed pandas version, then shows the install command without running it:

```python
import pandas as pd
print(pd.__version__)
# %pip install some-package-name
```

The version number printed depends on the Colab runtime. [VERSION] `import pandas as pd` gives the library a short nickname; almost all pandas code you will see uses `pd`.

## Common Mistake
Beginners sometimes run `%pip install pandas` in every notebook, or try `import` with a package that is not installed and get `ModuleNotFoundError`. Check first: try the `import`. If it works, the package is already there. If you get `ModuleNotFoundError`, install it once with `%pip install`, then run the import again. In Colab, installed packages last only for the current session, so a new session may need the install cell again. [VERSION]

## Key Takeaways
1. `import` loads a module; the standard library (`math`, `datetime`, `random`) needs no installation.
2. Third-party libraries such as NumPy, pandas and matplotlib add powerful tools; install missing ones with `%pip` in Colab or `pip` locally.
3. Use `random.seed()` when you need random results that others can reproduce.

## Hands-on Exercise
**Task:** Use the datetime module to calculate how many days remain until a date of your choice, and use random to pick a winner from a list of names.
**Tools:** Google Colab (free).
**Steps:**
1. Import `date` from `datetime`, and import `random`.
2. Create a date for an event you care about, such as a birthday or a holiday.
3. Print the number of days from `date.today()` to that date with an f-string.
4. Create a list of at least 5 made-up names. Do not use real people's personal data.
5. Pick a winner with `random.choice()`. Run the cell 3 times and note whether the winner changes.
6. Add `random.seed(7)` before the choice, run it 3 times again, and explain the difference in a text cell.
**What good looks like:** A correct day count (check it with a calendar), a random winner, and a clear sentence explaining that the seed makes the choice repeatable.
**Time:** about 15 minutes

## Review Flags
- [VERSION] Install commands in Colab (%pip vs !pip), the list of libraries pre-installed in Colab, the pandas version printed and how long installed packages last in a Colab session must be checked against the live tool.
- The random.seed(42) output ("Tariq") was produced with Python 3.11; confirm it in the Colab runtime before recording.
