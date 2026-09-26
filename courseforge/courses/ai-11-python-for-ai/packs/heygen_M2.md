# HeyGen Batch Pack: AI-11 M2 (Writing Clean, Reusable Code)

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

## L06 Functions: Package Your Logic

- **Filename:** `ai-11-python-for-ai_M2_L06_presenter.mp4`
- **Expected length:** about 4.9 minutes (672 words). The quality gate accepts ±10%.

```text
You have already used functions many times. Print, len, sum and type are all functions. Someone else wrote them once, and you use them every day. Today, you write your own.

Last time, loops helped us repeat work. Functions help us reuse it. A function is a named block of code that does one job. You define it once, and then you call it, which means run it, as many times as you need.

Here is a function that converts Celsius to Fahrenheit. The word def starts the definition, followed by the name. Inside the brackets is a parameter, called celsius. It is a name for the input the function will receive.

The indented lines are the body. The text in triple quotation marks is a docstring, a short description of what the function does. And return sends the result back to the code that called the function.

When you call it with thirty-five, the value thirty-five is called an argument. Inside the function, celsius becomes thirty-five, and the function returns ninety-five. Return and print are different. Print only shows a value. Return gives it back, so your code can store it, compare it, or use it again.

Think of a function as a recipe card. You write the recipe once, and then cook it many times with different ingredients. The ingredients are the arguments, and the finished dish is the return value. If you improve the recipe, every future meal improves too, because there is only one card to change.

Functions help in three ways. You avoid copying the same code. You give a clear name to a piece of logic. And you can test each piece on its own.

Let's write one in Colab. Kwame prepares a weather summary for a travel website that covers cities on three continents. The temperatures are made up.

We type the function with its docstring and run the cell. Notice that nothing is printed. Defining a function only teaches Python the recipe. It does not cook anything yet.

Now we call it in a loop. We have a small dictionary of three cities, Cairo, Oslo and Manila, with their temperatures. The items method gives us each city and its temperature on every pass. For each one, we print the city and the converted value.

Run it. Cairo is ninety-five degrees Fahrenheit, Oslo is twenty-four point eight, and Manila is eighty-seven point eight. One function, called three times.

Next, Kwame writes a second function called describe. It takes a city, a temperature, and a unit. The unit has a default value, F. If the unit is F, describe calls our first function. Otherwise, it keeps the temperature in Celsius. Parameters with default values always come after those without.

We call it twice for Oslo. The first call gives no unit, so it uses the default, and we get Fahrenheit. The second call names the unit as C, which makes the call easy to read. And we get minus four degrees Celsius.

A common mistake is using print inside a function when you mean return. The function shows a value, but gives back nothing, which Python calls None. If you then try to add one to it, you get an error. Use return when the caller needs the result. A second mistake is defining a function and forgetting to call it. Defining teaches Python the recipe. Calling it cooks the meal.

Let's recap. First, you define a function with def, a name, parameters and an indented body, and you call it with its name and arguments. Second, return sends a result back to the caller, while print only shows it. Third, default values make parameters optional, and a short docstring explains what the function does.

Now it is your turn. In the exercise below this video, you will write a currency conversion function that takes an amount and a rate, and call it for three currencies. Use made-up rates. It takes about twenty minutes. In the next lesson, we learn clean code habits. See you there.
```

## L07 Clean Code Habits

- **Filename:** `ai-11-python-for-ai_M2_L07_presenter.mp4`
- **Expected length:** about 4.8 minutes (671 words). The quality gate accepts ±10%.

```text
Code is read far more often than it is written. Your teammates read it. Reviewers read it. And you read it again in three months' time. If you cannot understand your own code next month, it does not matter that it worked today.

In the last lesson, we packaged logic into functions. Today, we make our code easy to read. Clean code is code that a person can read, check and change safely. Python has an official style guide called PEP eight. You don't need to learn all of it. A few habits cover most of what matters.

Habit one is clear names. A name like weekly orders says what the variable holds. A single letter like x does not. Use lowercase words joined by underscores, for variables and for functions. Avoid single letters, except in very short loops.

Habit two is short functions that do one job. If you need the word and to describe a function, it probably does two jobs, so split it. Habit three is comments that explain why, not what. A comment that repeats the code adds nothing. A comment that explains a decision helps the reader.

Habit four is docstrings. Add one line at the top of each function that says what it does and what it returns. Habit five is layout. Indent the same way every time, keep lines short, leave blank lines between parts, and put spaces around the equals sign.

Clean code is like a tidy shared kitchen. Knives go back in the same drawer, jars have labels, and the counter is cleared after cooking. Nobody wastes time searching, and nobody picks up salt thinking it is sugar. A messy kitchen still produces meals, but every cook is slower, and mistakes are more likely.

Improving the structure of code without changing what it does is called refactoring. The output before and after must be the same. So refactor in small steps, and run the code after each step. Then you know which change broke something.

Let's see a real example. Sipho volunteers for a food bank in Durban, South Africa. He wrote a quick script to find the average value of the week's donation orders. The numbers are made up.

Here is the first version. It stores four order values in a list called x, adds them up in a loop, divides by the number of orders, and prints one hundred and eleven point two five. It works. But what are x, t and a? A reader must trace every line to find out.

And here is the clean version. First, x became weekly orders, so the data explains itself. Second, the loop became the built-in sum function, which is shorter and harder to get wrong.

Third, the calculation moved into a function with a clear name and a docstring, so Sipho can reuse it for next week's orders. He ran the script after each change, and the output stayed the same, one hundred and eleven point two five.

A common mistake is thinking that clean code means many comments. Comments that repeat the code quickly become wrong when the code changes. First make the code explain itself with good names and small functions. Then comment only on the reasons behind decisions. A second mistake is changing the behaviour while you refactor. Keep the output identical, and compare it before and after.

Let's recap. First, use clear, descriptive names in lowercase with underscores, and follow the main PEP eight layout rules. Second, keep functions short, give each one a single job, and add a one-line docstring. Third, refactor in small steps, and check that the output does not change.

Now it is your turn. In the exercise below this video, you will refactor a messy twenty-line script about tour guide ratings. You will rename the variables, split it into two functions, and add docstrings, while keeping the output exactly the same. It takes about twenty-five minutes. In the next lesson, we look at errors and how to fix them. See you there.
```

## L08 Errors and How to Fix Them

- **Filename:** `ai-11-python-for-ai_M2_L08_presenter.mp4`
- **Expected length:** about 4.9 minutes (693 words). The quality gate accepts ±10%.

```text
Every programmer, at every level, sees error messages every day. The difference between a beginner and an expert is not the number of errors. It is how quickly they read the message and find the cause.

Last time, we learned to write clean code. But even clean code breaks sometimes. When Python cannot run a line, it stops and shows a traceback. That is a report of where the problem happened, and what kind of problem it was.

A traceback can look long and frightening, but you read it in a fixed order. Start at the last line. It gives the error type and a short message. Then look just above it, for the line of your code that caused the problem. Ignore the rest at first.

It is like a doctor's report after a test. You don't read every measurement first. You read the conclusion at the bottom, a broken wrist, then find where it happened. Only then do you look at the details, if you still need them.

Five errors cover most beginner problems. A NameError means Python doesn't know a name, often a spelling mistake, or a cell you haven't run yet. A TypeError means the types don't fit, like adding text and a number. An IndexError means a list position doesn't exist.

A KeyError means a dictionary key doesn't exist, often because of a different spelling or a capital letter. And an IndentationError means the indentation doesn't match the structure, for example a missing indent after a colon. One tip for Colab. A NameError often means you restarted the notebook or skipped a cell, so run the cells above it in order.

Some errors are expected. If a user types the word twelve where you need a number, converting it raises a ValueError. You can handle expected errors with try and except. Python tries the code, and if that named error happens, it runs the except block instead of stopping.

Let's fix some real errors. Farida writes a small stock script for a spice shop in Almaty, Kazakhstan. Her staff type the number of boxes they receive. All values are made up.

First, a list of three prices. We ask for the item at position three and run the cell. Python stops with a traceback. Let's read it the right way.

The last line says IndexError, list index out of range. So a list position doesn't exist. Just above, it points to our print line. The list has three items, at positions zero, one and two. So position three is outside it. We change it to two, or minus one for the last item, and it works.

Next, the input problem. Staff sometimes type words instead of numbers. We write a function called ask boxes. Inside a try block, it converts the answer to a whole number and returns it. If a ValueError happens, the except block prints a friendly message and returns None.

We call it twice, once with the text twelve in digits, and once with the word twelve. The first call returns twelve. The second prints our friendly message, then None. Without try, the whole script would stop with a ValueError. With it, the script continues.

A common mistake is to wrap large blocks of code in try, with an except that names no error, just to make the errors go away. This hides real bugs, and the program quietly gives wrong results. Only catch the specific error you expect, around the smallest piece of code. Fix everything else by reading the traceback.

Let's recap. First, read a traceback from the bottom. The error type and message come first, then the line that caused it. Second, NameError, TypeError, IndexError, KeyError and IndentationError each point to a typical cause. Third, use try and except with a named error for expected problems, such as bad user input, not to hide bugs.

Now it is your turn. In the exercise below this video, you will fix five broken Colab cells, and write down which error each one raised, and why. It takes about twenty minutes. In the next lesson, we explore modules, libraries and installing packages. See you there.
```

## L09 Modules, Libraries and Installing Packages

- **Filename:** `ai-11-python-for-ai_M2_L09_presenter.mp4`
- **Expected length:** about 4.9 minutes (675 words). The quality gate accepts ±10%.
- **Pronunciation:** The pandas version number on screen depends on the Colab runtime; the voiceover does not say it.

```text
How many days until your next holiday? Which name should win a prize draw? You could write that code yourself, but you don't need to. Python already includes tested tools for both, and thousands more are free to install.

Last time, we learned to read errors. Today, we use code that other people have already written and tested. A module is a file of Python code that you load into your program with the word import. You can import a whole module, or just one part of it, such as the date tool from datetime.

Python comes with a large standard library. These modules are always available, with nothing to install. Three useful ones are math, for maths functions, datetime, for dates and times, and random, for random numbers and choices.

A library, or package, is a larger collection of modules, often shared for free. Third-party libraries are not part of Python itself, so you install them. For AI work, three matter most. NumPy does fast calculations on large sets of numbers. pandas works with tables of data. And matplotlib draws charts.

Think of the kitchen tools that come with a new flat, like a pot, a pan and a few knives. That is the standard library. Third-party libraries are specialist tools you add later, like a bread machine. Import takes a tool out of the cupboard. Installing is buying the tool and putting it in the cupboard first.

Colab already has many data libraries installed, including pandas and matplotlib. If you need another one, you install it in a code cell with the pip install command. The exact commands change over time. And only install packages from trusted sources. Check the spelling, because a wrong name can install a different, unwanted package.

Let's use them. Valentina organises a charity book fair in Bogotá, Colombia. She wants to know how many days remain until the fair, and to pick a prize winner from the volunteers. The date and names are made up.

We import math and random, and the date tool from datetime. First, a quick test of math. The square root of eighty-one is nine, and math ceil rounds four point two up to five. Rounding up is useful for questions like, how many boxes do I need?

Next, two dates. The fair is on the fifth of December, twenty twenty-six. For today, we use a fixed date, so the output is the same every time. We subtract one date from the other and ask for the days. Run it, and there are seventy-three days to go.

Now the prize draw. We make a list of four volunteer names, and random choice picks one. But first we set a seed. The seed makes the random result repeatable, so everyone who runs this gets the same name. That matters in data work, because others must be able to reproduce your results. For a real draw, remove the seed.

Finally, we import pandas with the short nickname p d, which almost all pandas code uses, and print its version. It is already installed. The install command stays as a comment, so we don't run it.

A common mistake is installing packages you already have. Check first by trying the import. If it works, the package is there. If you see a ModuleNotFoundError, install it once, then import again. In Colab, installed packages last only for the current session.

Let's recap. First, import loads a module, and the standard library, with math, datetime and random, needs no installation. Second, third-party libraries such as NumPy, pandas and matplotlib add powerful tools, and you install missing ones with pip. Third, use a random seed when others need to reproduce your random results.

Now it is your turn. In the exercise below this video, you will use datetime to count the days until a date you care about, and random to pick a winner from a list of made-up names. It takes about fifteen minutes. In the next lesson, we work locally with files and VS Code. See you there.
```

## L10 Working Locally: Files and VS Code

- **Filename:** `ai-11-python-for-ai_M2_L10_presenter.mp4`
- **Expected length:** about 4.9 minutes (687 words). The quality gate accepts ±10%.

```text
Colab is excellent for learning and exploring. But many real projects run as scripts on a computer or a server, and they read and write files. Today, you set up Python on your own machine and write a script that turns one file into another.

Last time, we imported tested tools. Today, we leave the browser. To work locally, you need two free tools. The first is Python itself. The second is VS Code, a free code editor, with its Python extension, which adds colours, error hints and a run button.

Installation steps differ between Windows, Mac and Linux, so follow the current official instructions for your system. If you cannot install software, for example on a work laptop, you can do this lesson in Colab.

A script is a plain text file whose name ends in dot p y. You run it from a terminal, which is a text window for commands. You type python, then the file name.

Scripts often read and write files. The safe way is the with statement. Open connects to the file, and with closes it automatically when the indented block ends, even if an error happens. The letter w means write a new file, which replaces any old file with the same name. And UTF eight makes sure names with accents or other alphabets are read correctly.

So when should you use a notebook, and when a script? A notebook is like a whiteboard in a meeting room. It is good for thinking out loud and showing your steps. A script is like a printed procedure on a factory wall. It has fixed steps that anyone can run in exactly the same way, every time.

Let's build one. Nikolai manages a small guesthouse in Tbilisi, Georgia. He has a CSV file of guests and their home cities, and he wants a summary of how many guests came from each city. The names and cities are made up.

In VS Code, we open a new folder called a i eleven local. Inside it, we create a file called guests dot csv. The first line has the column names, name and city, followed by four guests from Casablanca, Quito and Busan.

Next, a file called summary dot p y. We import the csv module and open the guests file with a with block. The DictReader reads each line as a dictionary, using the first line as keys. So for each row, we can ask for the city.

Then we count the cities in a dictionary. For each row, get looks up the city's count, starting at zero for a new city, and adds one.

Finally, we open summary dot t x t for writing. We write the total number of guests, then one line for each city and its count. The backslash n in the text starts a new line. At the end, we print a short message.

Now we open the terminal and run the script. It prints saved summary. When we open the new file, it shows four guests. Two from Casablanca, one from Quito and one from Busan.

The most common problem is a FileNotFoundError. The script looks for the data file in the terminal's current folder. So open the whole project folder, keep the data next to the script, and run it from there. And be careful with w, because it empties the file. Keep a copy of your original data.

Let's recap. First, locally you need Python and VS Code with the Python extension, and you run scripts from the terminal. Second, use with open to read and write files safely, with w to write and UTF eight for international text. Third, notebooks suit exploring and explaining, while scripts suit tasks that must run the same way many times.

Now it is your turn. In the exercise below this video, you will write a script that reads a small CSV of made-up names and cities, and writes a summary text file. If you cannot install software, use Colab. It takes about thirty minutes. In the next lesson, we meet pandas, with Series and DataFrames. See you there.
```
