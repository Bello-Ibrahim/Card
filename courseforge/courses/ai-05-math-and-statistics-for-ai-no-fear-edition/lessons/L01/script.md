# L01 Maths for AI Without Fear | Presenter Script

Course: AI-05 · Video: 5 min · Words: 732

## Hook
Many people feel their stomach tighten when they see a page of maths symbols. If that is you, you are in the right place. Machine learning uses a surprisingly small amount of maths, and you can learn it one small step at a time.

## Explain
Hi, and welcome to Math and Statistics for AI, the No-Fear Edition. In this first lesson, we draw a map of the whole course, and you will run your very first line of Python.

A machine learning model is a set of calculations. It turns data into a prediction, and then it improves itself. This course covers the four areas of maths that make that possible. Each one has a clear job inside the model.

First, linear algebra, which means vectors and matrices. It stores the data and makes the predictions. That is Module 1. Second, probability and statistics. They describe data and uncertainty. That is Module 2.

Third, calculus, which means derivatives and gradients. This is how a model learns. It tells the model which way to change its numbers so its errors get smaller. That is Module 3. And fourth, metrics, which turn results into numbers you can judge. That is Module 4, with the capstone, where you build linear regression from scratch.

You already know the maths you need to start. Fractions, percentages and reading a simple graph. We will add new words slowly, and we will always explain a symbol in words before we use it.

Every lesson follows the same three-step routine. First, a picture: a drawing, a graph, or an everyday situation. Second, a small hand calculation with tiny numbers. Third, code: the same calculation in Python with NumPy, a free library for numbers, in Google Colab. The code never replaces your understanding. It checks your work.

Think of it like learning to cook from a recipe. The picture is the photo of the finished dish. The hand calculation is cooking a small portion slowly. The code is the kitchen machine that cooks a large portion quickly.

## Demonstrate
Let's try the routine together. Mariana runs a small bakery in Bogotá, Colombia. She wants her average daily sales of a new cake over five days. The numbers are twelve, fifteen, nine, twenty and fourteen cakes.

Step one, the picture. Five bars of different heights. The average is the height they would all have if you made them level. Step two, the hand calculation. Twelve plus fifteen plus nine plus twenty plus fourteen equals seventy cakes. The mean is the total divided by the number of days. Seventy divided by five equals fourteen cakes per day.

Step three, the code. Open a web browser and go to Google Colab. If Colab asks you to, sign in with a Google account. Then create a new notebook, for example from the File menu.

Click in the first code cell. The first line loads NumPy with the short name n p. The next line creates a NumPy array, which is a list of numbers that NumPy can calculate with quickly. Here it holds Mariana's five sales numbers.

Then we print two things. Sales dot sum adds the numbers. Sales dot mean finds the average. Now run the cell with the play button next to it, or press Shift and Enter together.

And there it is. Seventy, and fourteen point zero. It matches our hand calculation exactly.

One common mistake is to think you must understand every formula perfectly before you are allowed to write code. So people stop at the first hard symbol and decide they are not a maths person. In fact, understanding grows in layers. If a symbol confuses you, go back to the picture and the tiny numbers.

## Recap
Let's recap. First, machine learning uses four areas of maths. Linear algebra stores data and makes predictions, statistics describes data and uncertainty, calculus drives learning, and metrics judge results. Second, every lesson follows the same routine: a picture, a small hand calculation, then code. Third, a NumPy array is a list of numbers you can calculate with, for example with sum and mean.

## CTA
Now it is your turn. In the exercise below this video, you choose five made-up numbers, find their sum and mean on paper, then check them in your own Colab notebook. It takes about fifteen minutes. In the next lesson, we meet vectors: data as lists of numbers. See you there.

## Thumbnail
Headline: Maths Without Fear
Image: Navy background, five teal bars of different heights with a dotted level line through them, headline in teal Inter Bold.

## Production Notes
- [VERSION] Google Colab: confirm current sign-in requirements, free usage limits, how to create a new notebook, and the run button and Shift + Enter shortcut against the live tool before recording the screen demo (scenes 11 to 14).
- [VERSION] Colab AI assistant: the voiceover does not mention it. If the editor adds the privacy reminder from exercise step 8, confirm first that an AI assistant is currently offered inside Colab.
- Mariana, her Bogotá bakery and the sales figures 12, 15, 9, 20 and 14 are hypothetical. Do not show a real bakery name or logo in stock footage.
- The screen recording should use a clean browser profile with no personal bookmarks, emails or account names visible.
