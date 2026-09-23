# L09 Modules, Libraries and Installing Packages | Presenter Script

Course: AI-11 · Video: 5 min · Words: 682

## Hook
How many days until your next holiday? Which name should win a prize draw? You could write that code yourself, but you don't need to. Python already includes tested tools for both, and thousands more are free to install.

## Explain
Last time, we learned to read errors. Today, we use code that other people have already written and tested. A module is a file of Python code that you load into your program with the word import. You can import a whole module, or just one part of it, such as the date tool from datetime.

Python comes with a large standard library. These modules are always available, with nothing to install. Three useful ones are math, for maths functions, datetime, for dates and times, and random, for random numbers and choices.

A library, or package, is a larger collection of modules, often shared for free. Third-party libraries are not part of Python itself, so you install them. For AI work, three matter most. NumPy does fast calculations on large sets of numbers. pandas works with tables of data. And matplotlib draws charts.

Think of the kitchen tools that come with a new flat, like a pot, a pan and a few knives. That is the standard library. Third-party libraries are specialist tools you add later, like a bread machine. Import takes a tool out of the cupboard. Installing is buying the tool and putting it in the cupboard first.

Colab already has many data libraries installed, including pandas and matplotlib. If you need another one, you install it in a code cell with the pip install command. The exact commands change over time. And only install packages from trusted sources. Check the spelling, because a wrong name can install a different, unwanted package.

## Demonstrate
Let's use them. Valentina organises a charity book fair in Bogotá, Colombia. She wants to know how many days remain until the fair, and to pick a prize winner from the volunteers. The date and names are made up.

We import math and random, and the date tool from datetime. First, a quick test of math. The square root of eighty-one is nine, and math ceil rounds four point two up to five. Rounding up is useful for questions like, how many boxes do I need?

Next, two dates. The fair is on the fifth of December, twenty twenty-six. For today, we use a fixed date, so the output is the same every time. We subtract one date from the other and ask for the days. Run it, and there are seventy-three days to go.

Now the prize draw. We make a list of four volunteer names, and random choice picks one. But first we set a seed. The seed makes the random result repeatable, so everyone who runs this gets the same name. That matters in data work, because others must be able to reproduce your results. For a real draw, remove the seed.

Finally, we import pandas with the short nickname p d, which almost all pandas code uses, and print its version. It is already installed. The install command stays as a comment, so we don't run it.

A common mistake is installing packages you already have. Check first by trying the import. If it works, the package is there. If you see a ModuleNotFoundError, install it once, then import again. In Colab, installed packages last only for the current session.

## Recap
Let's recap. First, import loads a module, and the standard library, with math, datetime and random, needs no installation. Second, third-party libraries such as NumPy, pandas and matplotlib add powerful tools, and you install missing ones with pip. Third, use a random seed when others need to reproduce your random results.

## CTA
Now it is your turn. In the exercise below this video, you will use datetime to count the days until a date you care about, and random to pick a winner from a list of made-up names. It takes about fifteen minutes. In the next lesson, we work locally with files and VS Code. See you there.

## Thumbnail
Headline: Borrow Tested Tools
Image: Navy background, an open toolbox with three labelled tools (math, datetime, random) and a delivery box labelled pandas, headline in teal Inter Bold.

## Production Notes
- [VERSION] Check the Colab install command (%pip vs !pip), the libraries pre-installed in Colab, the pandas version printed, and how long installed packages last in a Colab session against the live tool before recording.
- The random.seed(42) output 'Tariq' was produced with Python 3.11; confirm it in the Colab runtime before recording. The voiceover does not name the winner, so it stays correct either way; the screen must show whatever the runtime prints, which should be Tariq.
- The pandas version number on screen depends on the Colab runtime; the voiceover does not say it.
- Judgement call (curriculum): NumPy is named only; its maths use is covered in AI-05.
- Printed outputs on screen must match content.md: '9.0 5' and '73 days to go'. Valentina, the Bogotá book fair, the date and the names are made up.
