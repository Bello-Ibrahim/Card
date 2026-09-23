# L01 Maths for AI Without Fear

Course: AI-05 · Module: M1 · Objectives: O1 · Video: 5 min (screen demo)

## Hook
Many people feel their stomach tighten when they see a page of maths symbols. If that is you, you are in the right place. Machine learning uses a surprisingly small amount of maths, and you can learn every piece of it one small step at a time.

## Explanation
A machine learning model is a set of calculations that turns data into a prediction and then improves itself. This course covers the four areas of maths that make that possible. Each one has a clear job inside a model.

- **Linear algebra (vectors and matrices)** stores the data and makes the predictions. A house, a customer or a photo becomes a list of numbers, and a prediction is a weighted sum of those numbers. This is Module 1.
- **Probability and statistics** describe data and uncertainty. They tell you what is typical, what is unusual and how much you can trust a result. This is Module 2.
- **Calculus (derivatives and gradients)** is how a model learns. It tells the model which way to change its numbers so that its errors become smaller. This is Module 3.
- **Metrics** turn a model's results into numbers you can judge, such as error and accuracy. This is Module 4, together with the capstone, where you build linear regression from scratch.

You already know the high-school maths this course needs, such as fractions, percentages and reading a simple graph. We will add new vocabulary slowly and always explain a symbol in words before we use it.

Every lesson uses the same three-step routine:

1. **Picture.** First we look at a drawing, a graph or an everyday situation.
2. **Small hand calculation.** Then we do the idea with tiny numbers, on paper or in a spreadsheet.
3. **Code.** Finally we do the same calculation in Python with NumPy, a free library for working with numbers, in Google Colab.

The code never replaces your understanding. It checks your hand calculation and lets you work with bigger data later.

**Analogy:** Learning maths for AI is like learning to cook from a recipe. The picture is the photo of the finished dish, so you know what you are aiming for. The hand calculation is cooking a small portion slowly, one step at a time. The code is the kitchen machine that cooks a large portion quickly, once you know what it should do.

## Worked Example
Mariana runs a small bakery in Bogotá, Colombia. She wants to know her average daily sales of a new cake over five days. The numbers are hypothetical: 12, 15, 9, 20 and 14 cakes.

**Picture:** five bars of different heights. The average is the height they would all have if you made them level.

**Hand calculation:** the total is 12 + 15 + 9 + 20 + 14 = 70 cakes. The mean (average) is the total divided by the number of days: 70 ÷ 5 = 14 cakes per day.

**Code:** a presenter can follow these steps on screen.

1. Open a web browser and go to Google Colab. Sign in with a Google account if Colab asks you to. [VERSION]
2. Create a new notebook, for example from the **File** menu. [VERSION]
3. Click in the first code cell and type:

```python
import numpy as np
sales = np.array([12, 15, 9, 20, 14])
print(sales.sum())   # 70
print(sales.mean())  # 14.0
```

4. Run the cell with the play button next to it, or press Shift + Enter. [VERSION]
5. Check the output: `70` and `14.0`. It matches the hand calculation.

The first line loads NumPy with the short name `np`. The second line creates a NumPy **array**, a list of numbers that NumPy can calculate with quickly. `sales.sum()` adds the numbers and `sales.mean()` finds the average.

## Common Mistake
Many learners believe they must understand every formula perfectly before they are allowed to write code. So they stop at the first difficult symbol and decide they are "not a maths person". In fact, understanding grows in layers. A small example that you calculate yourself teaches more than a page of formulas. If a symbol confuses you, go back to the picture and the tiny numbers, and let the code check your work.

## Key Takeaways
1. Machine learning uses four areas of maths: linear algebra stores data and makes predictions, statistics describes data and uncertainty, calculus drives learning, and metrics judge results.
2. Every lesson follows the same routine: a picture, a small hand calculation, then the same calculation in NumPy.
3. A NumPy array is a list of numbers that NumPy can calculate with, for example with `.sum()` and `.mean()`.

## Hands-on Exercise
**Task:** Open a new Google Colab notebook, import NumPy, create an array of five numbers and print its sum and mean.
**Tools:** Google Colab (free, needs a Google account) [VERSION]; pen and paper.
**Steps:**
1. Choose five numbers from a made-up everyday situation, such as minutes of walking on five days. Use invented numbers, not personal or confidential data from your work.
2. On paper, add the five numbers and divide the total by 5.
3. Open Google Colab and create a new notebook. [VERSION]
4. In the first cell, type `import numpy as np`, create your array with `np.array([...])` and print `.sum()` and `.mean()`.
5. Run the cell and compare the output with your paper answer.
6. Add a text cell above the code that says, in one sentence, what your numbers describe.
7. Check Colab's current sign-in rules and free usage limits so you know what to expect in later lessons. [VERSION]
8. If Colab offers an AI assistant, do not paste personal or confidential information into it.
**What good looks like:** A notebook with one text cell and one code cell. The printed sum and mean match your hand calculation exactly.
**Time:** about 15 minutes

## Review Flags
- [VERSION] Google Colab: confirm current sign-in requirements, free usage limits, the way to create a new notebook, and the run button and Shift + Enter shortcut before scripting the screen demo.
- [VERSION] Colab AI assistant: confirm whether an AI assistant is currently offered inside Colab before the privacy reminder in step 8 is recorded.
