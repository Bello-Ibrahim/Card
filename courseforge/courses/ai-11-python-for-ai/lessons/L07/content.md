# L07 Clean Code Habits

Course: AI-11 · Module: M2 · Objectives: O3 · Video: 5 min

## Hook
Code is read far more often than it is written: by your teammates, by reviewers, and by you in three months' time. If you cannot understand your own code next month, it does not matter that it worked today.

## Explanation
Clean code is code that a person can read, check and change safely. Python has an official style guide called **PEP 8**. You do not need to learn all of it. These habits cover most of what matters:

1. **Clear names.** `weekly_orders` says what a variable holds; `x` does not. Use lowercase words joined by underscores for variables and functions (`average_order_value`). Avoid single letters, except for very short loops.
2. **Short functions that do one job.** If you need the word "and" to describe a function, it probably does two jobs. Split it.
3. **Comments that explain why, not what.** `# add 1 to i` repeats the code. `# the first row is a header, so skip it` explains a decision the reader cannot see.
4. **Docstrings.** One line in triple quotation marks at the top of each function, saying what it does and what it returns.
5. **Layout.** Indent with 4 spaces, put one blank line between parts of a script (PEP 8 suggests two between top-level functions), keep lines short (PEP 8 suggests at most 79 characters), and put spaces around `=` and operators such as `+`. [VERIFY]

**Refactoring** means improving the structure of code without changing what it does. The output before and after must be the same. Refactor in small steps and run the code after each step, so you know which change broke something.

**Analogy:** Clean code is like a tidy shared kitchen. Knives go back in the same drawer, jars have labels, and the counter is cleared after cooking. Nobody wastes time searching, and nobody picks up a jar of salt thinking it is sugar. A messy kitchen still produces meals, but every cook is slower and mistakes are more likely.

## Worked Example
Sipho volunteers for a food bank in Durban, South Africa. He wrote a quick script to find the average value of the week's donation orders. The numbers are made up. This lesson uses before-and-after code slides.

**Before:**

```python
x = [120, 80, 45, 200]
t = 0
for i in x:
    t = t + i
a = t / len(x)
print(a)
```

It prints `111.25`, and it works. But what are `x`, `t` and `a`? A reader must trace every line to find out.

**After:**

```python
def average_order_value(order_values):
    """Return the mean of a list of order values."""
    return sum(order_values) / len(order_values)

weekly_orders = [120, 80, 45, 200]
print(average_order_value(weekly_orders))
```

It still prints `111.25`. The changes, one at a time:

- `x` became `weekly_orders`, so the data explains itself.
- The loop became the built-in `sum()`, which is shorter and harder to get wrong.
- The calculation moved into a function with a descriptive name and a docstring, so it can be reused for next week's orders.

Sipho ran the script after each change and checked that the output was still `111.25`.

## Common Mistake
Beginners often think clean code means adding many comments. Comments that repeat the code (`# loop over the list`) add reading time and quickly become wrong when the code changes. First make the code explain itself with good names and small functions. Then add comments only for the reasons behind decisions. A second mistake is "refactoring" and changing the behaviour at the same time. Keep the output identical, and compare it before and after.

## Key Takeaways
1. Use clear, descriptive names in lowercase with underscores, and follow the main PEP 8 layout rules.
2. Keep functions short, give each one job, and add a one-line docstring.
3. Refactor in small steps and check that the output does not change.

## Hands-on Exercise
**Task:** Refactor a provided 20-line messy script: rename variables, split it into 2 functions, and add docstrings.
**Tools:** Google Colab (free).
**Steps:**
1. Copy this script into a code cell. It summarises made-up customer ratings for three tour guides. Run it and note the output.

```python
d = {"Rosa": [7, 9, 8], "Ibrahim": [5, 6, 9], "Keiko": [10, 8, 9]}
r = []
for k in d:
    s = 0
    for v in d[k]:
        s = s + v
    m = s / len(d[k])
    if m >= 8:
        g = "high"
    else:
        g = "normal"
    r.append(k + ": " + str(round(m, 1)) + " " + g)
for l in r:
    print(l)
t = 0
for k in d:
    t = t + len(d[k])
print("ratings:", t)
```

```
Rosa: 8.0 high
Ibrahim: 6.7 normal
Keiko: 9.0 high
ratings: 9
```

2. Rename every one-letter variable, for example `d` to `ratings_by_guide`. Run the cell.
3. Create a function `mean_rating(ratings)` that returns the average. Run the cell.
4. Create a function `rating_band(average)` that returns "high" or "normal". Run the cell.
5. Add a docstring to each function, and use an f-string for the printed line.
**What good looks like:** The output is exactly the same 4 lines as before. There are no one-letter names, there are 2 functions with docstrings, and a new reader can understand the script without tracing every line.
**Time:** about 25 minutes

## Review Flags
- [VERIFY] The PEP 8 details quoted (79-character line length, 4-space indentation, two blank lines between top-level functions) should be checked against the current text of PEP 8.
- Not a screen demo lesson: use before-and-after code slides. All figures are made up, and every output was produced by running the code with Python 3.11.
