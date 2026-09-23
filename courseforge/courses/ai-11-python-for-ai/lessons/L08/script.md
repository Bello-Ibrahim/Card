# L08 Errors and How to Fix Them | Presenter Script

Course: AI-11 · Video: 5 min · Words: 693

## Hook
Every programmer, at every level, sees error messages every day. The difference between a beginner and an expert is not the number of errors. It is how quickly they read the message and find the cause.

## Explain
Last time, we learned to write clean code. But even clean code breaks sometimes. When Python cannot run a line, it stops and shows a traceback. That is a report of where the problem happened, and what kind of problem it was.

A traceback can look long and frightening, but you read it in a fixed order. Start at the last line. It gives the error type and a short message. Then look just above it, for the line of your code that caused the problem. Ignore the rest at first.

It is like a doctor's report after a test. You don't read every measurement first. You read the conclusion at the bottom, a broken wrist, then find where it happened. Only then do you look at the details, if you still need them.

Five errors cover most beginner problems. A NameError means Python doesn't know a name, often a spelling mistake, or a cell you haven't run yet. A TypeError means the types don't fit, like adding text and a number. An IndexError means a list position doesn't exist.

A KeyError means a dictionary key doesn't exist, often because of a different spelling or a capital letter. And an IndentationError means the indentation doesn't match the structure, for example a missing indent after a colon. One tip for Colab. A NameError often means you restarted the notebook or skipped a cell, so run the cells above it in order.

Some errors are expected. If a user types the word twelve where you need a number, converting it raises a ValueError. You can handle expected errors with try and except. Python tries the code, and if that named error happens, it runs the except block instead of stopping.

## Demonstrate
Let's fix some real errors. Farida writes a small stock script for a spice shop in Almaty, Kazakhstan. Her staff type the number of boxes they receive. All values are made up.

First, a list of three prices. We ask for the item at position three and run the cell. Python stops with a traceback. Let's read it the right way.

The last line says IndexError, list index out of range. So a list position doesn't exist. Just above, it points to our print line. The list has three items, at positions zero, one and two. So position three is outside it. We change it to two, or minus one for the last item, and it works.

Next, the input problem. Staff sometimes type words instead of numbers. We write a function called ask boxes. Inside a try block, it converts the answer to a whole number and returns it. If a ValueError happens, the except block prints a friendly message and returns None.

We call it twice, once with the text twelve in digits, and once with the word twelve. The first call returns twelve. The second prints our friendly message, then None. Without try, the whole script would stop with a ValueError. With it, the script continues.

A common mistake is to wrap large blocks of code in try, with an except that names no error, just to make the errors go away. This hides real bugs, and the program quietly gives wrong results. Only catch the specific error you expect, around the smallest piece of code. Fix everything else by reading the traceback.

## Recap
Let's recap. First, read a traceback from the bottom. The error type and message come first, then the line that caused it. Second, NameError, TypeError, IndexError, KeyError and IndentationError each point to a typical cause. Third, use try and except with a named error for expected problems, such as bad user input, not to hide bugs.

## CTA
Now it is your turn. In the exercise below this video, you will fix five broken Colab cells, and write down which error each one raised, and why. It takes about twenty minutes. In the next lesson, we explore modules, libraries and installing packages. See you there.

## Thumbnail
Headline: Read the Last Line
Image: Navy background, a red traceback block with its last line highlighted in teal, headline in teal Inter Bold.

## Production Notes
- [VERSION] Traceback layout differs between plain Python and Colab, and message wording changes between Python versions (newer versions add hints such as 'Did you mean'). Check the last-line messages in the current Colab runtime before recording; content.md messages were produced with Python 3.11.
- [VERSION] Check how Colab marks the failing line (arrow and line number) before recording.
- Printed outputs on screen must match content.md: 'IndexError: list index out of range' and '12 / Please type a whole number, such as 12. / None'.
- Farida and the Almaty spice shop are fictional; all values are made up.
