# L08 Errors and How to Fix Them

Course: AI-11 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Every programmer, at every level, sees error messages every day. The difference between a beginner and an experienced programmer is not the number of errors. It is how quickly they read the message and find the cause.

## Explanation
When Python cannot run a line, it stops and shows a **traceback**: a report of where the problem happened and what kind of problem it was. A traceback can look long and frightening, but you read it in a fixed order:

1. **Start at the last line.** It gives the error type and a short message, for example `IndexError: list index out of range`.
2. **Then look just above it** for the line of your code that caused the problem. Colab often marks it with an arrow and a line number. [VERSION]
3. Ignore the rest at first. The upper lines show the path Python took to get there, which is useful later.

Five errors cover most beginner problems:

| Error | What it means | Typical cause |
|---|---|---|
| NameError | Python does not know this name | A spelling mistake, or a cell not run yet |
| TypeError | The operation does not fit these types | Adding text and a number |
| IndexError | The list position does not exist | Asking for item 3 in a list of 3 (positions 0–2) |
| KeyError | The dictionary key does not exist | A different spelling or capital letter |
| IndentationError | The indentation does not match the structure | A missing indent after a colon |

In Colab, a NameError often means you restarted the notebook or skipped a cell. Run the cells above it in order.

Some errors are **expected**. If a user types "twelve" where you need a number, `int()` raises a **ValueError**. You can handle expected errors with `try` and `except`: Python tries the code in the `try` block, and if a named error happens, it runs the `except` block instead of stopping.

**Analogy:** A traceback is like a doctor's report after a test. You do not read every measurement first. You read the conclusion at the bottom ("broken wrist"), then find where it happened ("left arm, after a fall"). Only then do you look at the details, if you still need them.

## Worked Example
Farida writes a small stock script for a spice shop in Almaty, Kazakhstan. Staff type the number of boxes received. All values are made up.

The presenter runs this cell on screen:

```python
prices = [4, 6, 9]
print(prices[3])
```

The last line of the traceback says:

```
IndexError: list index out of range
```

The presenter reads it aloud: "IndexError, so a list position does not exist." The line above points to `print(prices[3])`. The list has 3 items at positions 0, 1 and 2, so position 3 is outside it. The fix is `prices[2]`, or `prices[-1]` for the last item.

Next, the input problem. Staff sometimes type words instead of numbers:

```python
def ask_boxes(answer):
    try:
        return int(answer)
    except ValueError:
        print("Please type a whole number, such as 12.")
        return None

print(ask_boxes("12"))
print(ask_boxes("twelve"))
```

```
12
Please type a whole number, such as 12.
None
```

Without `try`, the second call would stop the whole script with `ValueError: invalid literal for int() with base 10: 'twelve'`. With it, the script gives a helpful message and continues.

## Common Mistake
A common mistake is to use `try` with a bare `except:` (no error name) around large blocks of code, "to make the errors go away". This hides every problem, including real bugs such as a spelling mistake, and the program quietly produces wrong results. Only catch the specific error you expect, such as `ValueError`, around the smallest piece of code that can raise it. Fix everything else by reading the traceback.

## Key Takeaways
1. Read a traceback from the bottom: the error type and message first, then the line that caused it.
2. NameError, TypeError, IndexError, KeyError and IndentationError each point to a typical cause.
3. Use `try` and `except SomeError` for expected problems, such as bad user input, not to hide bugs.

## Hands-on Exercise
**Task:** Fix 5 broken Colab cells, and write down which error each one raised and why.
**Tools:** Google Colab (free).
**Steps:**
1. Put each of these in its own code cell and run it:
   - Cell 1: `print(totl)`
   - Cell 2: `print("Total: " + 5)`
   - Cell 3: `items = ["tea", "salt"]` then `print(items[2])`
   - Cell 4: `price = {"tea": 2.5}` then `print(price["Tea"])`
   - Cell 5: `def greet():` then `print("hi")` on the next line with no indent
2. For each cell, copy the last line of the traceback into a text cell.
3. Next to it, write in one sentence why the error happened.
4. Fix each cell and run it again until it works.
5. Bonus: wrap `int(input("Boxes? "))` in `try` and `except ValueError`, and test it with a word.
**What good looks like:** A text cell with 5 rows: NameError, TypeError, IndexError, KeyError and IndentationError, each with a correct one-sentence cause. All 5 fixed cells run without errors.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Traceback layout differs between plain Python and Colab, and error message wording can change between Python versions (newer versions add hints such as "Did you mean"). The last-line messages shown were produced with Python 3.11; check them in the current Colab runtime before recording.
