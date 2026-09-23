# L10 Working Locally: Files and VS Code | Presenter Script

Course: AI-11 · Video: 5 min · Words: 688

## Hook
Colab is excellent for learning and exploring. But many real projects run as scripts on a computer or a server, and they read and write files. Today, you set up Python on your own machine and write a script that turns one file into another.

## Explain
Last time, we imported tested tools. Today, we leave the browser. To work locally, you need two free tools. The first is Python itself. The second is VS Code, a free code editor, with its Python extension, which adds colours, error hints and a run button.

Installation steps differ between Windows, Mac and Linux, so follow the current official instructions for your system. If you cannot install software, for example on a work laptop, you can do this lesson in Colab.

A script is a plain text file whose name ends in dot p y. You run it from a terminal, which is a text window for commands. You type python, then the file name.

Scripts often read and write files. The safe way is the with statement. Open connects to the file, and with closes it automatically when the indented block ends, even if an error happens. The letter w means write a new file, which replaces any old file with the same name. And UTF eight makes sure names with accents or other alphabets are read correctly.

So when should you use a notebook, and when a script? A notebook is like a whiteboard in a meeting room. It is good for thinking out loud and showing your steps. A script is like a printed procedure on a factory wall. It has fixed steps that anyone can run in exactly the same way, every time.

## Demonstrate
Let's build one. Nikolai manages a small guesthouse in Tbilisi, Georgia. He has a CSV file of guests and their home cities, and he wants a summary of how many guests came from each city. The names and cities are made up.

In VS Code, we open a new folder called a i eleven local. Inside it, we create a file called guests dot csv. The first line has the column names, name and city, followed by four guests from Casablanca, Quito and Busan.

Next, a file called summary dot p y. We import the csv module and open the guests file with a with block. The DictReader reads each line as a dictionary, using the first line as keys. So for each row, we can ask for the city.

Then we count the cities in a dictionary. For each row, get looks up the city's count, starting at zero for a new city, and adds one.

Finally, we open summary dot t x t for writing. We write the total number of guests, then one line for each city and its count. The backslash n in the text starts a new line. At the end, we print a short message.

Now we open the terminal and run the script. It prints saved summary. When we open the new file, it shows four guests. Two from Casablanca, one from Quito and one from Busan.

The most common problem is a FileNotFoundError. The script looks for the data file in the terminal's current folder. So open the whole project folder, keep the data next to the script, and run it from there. And be careful with w, because it empties the file. Keep a copy of your original data.

## Recap
Let's recap. First, locally you need Python and VS Code with the Python extension, and you run scripts from the terminal. Second, use with open to read and write files safely, with w to write and UTF eight for international text. Third, notebooks suit exploring and explaining, while scripts suit tasks that must run the same way many times.

## CTA
Now it is your turn. In the exercise below this video, you will write a script that reads a small CSV of made-up names and cities, and writes a summary text file. If you cannot install software, use Colab. It takes about thirty minutes. In the next lesson, we meet pandas, with Series and DataFrames. See you there.

## Thumbnail
Headline: Python on Your Computer
Image: Navy background, a laptop showing an editor with two files, guests.csv and summary.py, and an arrow to summary.txt, headline in teal Inter Bold.

## Production Notes
- [VERSION] Python and VS Code installation steps, the Python extension, File > Open Folder, how to open the terminal, and whether the command is python or python3 differ by operating system and version. Check against the current official instructions before recording. The demo does not show installation step by step; it starts with both tools installed.
- Screen demo uses VS Code (the brief's tool), not Colab. Record on one operating system and note it in the lesson page.
- Printed output and file content on screen must match content.md: 'Saved summary.txt' and 'Guests: 4 / Casablanca: 2 / Quito: 1 / Busan: 1'.
- Nikolai, the Tbilisi guesthouse, and all guest names and cities are made up. Use a clean user account with no personal files or folder names visible.
