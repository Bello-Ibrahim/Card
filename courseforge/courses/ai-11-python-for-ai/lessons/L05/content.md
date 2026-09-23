# L05 Repeating Work with Loops

Course: AI-11 · Module: M1 · Objectives: O2, O3 · Video: 5 min (screen demo)

## Hook
Adding up 4 numbers by hand is easy. Adding up 40,000 rows of sales is not. Computers are very good at doing the same small job again and again without getting tired. The tool for this in Python is the loop.

## Explanation
A **for loop** runs the same block of code once for each item in a collection:

```python
for count in boxes:
    print(count)
```

Read this as "for each item in `boxes`, call it `count`, and run the indented code". On the first pass `count` is the first item, on the second pass it is the second item, and so on until the list ends. As with `if`, the line ends with a colon and the body is indented.

A very common pattern is the **running total**. You create a variable at 0 before the loop, and add to it inside the loop.

`range()` gives a sequence of numbers to loop over. `range(1, 4)` gives 1, 2 and 3: it starts at the first number and stops **before** the second.

A **while loop** repeats as long as a condition stays true. It is useful when you do not know in advance how many passes you need, for example "keep asking until the user types a valid number". It is also easier to get wrong, because if the condition never becomes false, the loop never ends. In Colab you can stop a running cell with the stop button next to it.

**Analogy:** A for loop is like a cashier at a supermarket. The cashier picks up each item in the basket, one after another, scans it and adds its price to the total on the screen. The cashier does not need to know in advance how many items there are. When the basket is empty, the cashier stops and shows the total.

When is a loop the right tool? Use one when you must do the same steps for every item and you need to see or change something at each step. For simple totals, Python also has built-in functions: `sum()`, `max()`, `min()` and `len()`. They do the loop for you. In week 3 you will see that pandas does most loops for you too, and much faster.

## Worked Example
Ayşe manages a small textile workshop in İzmir, Türkiye. She records how many boxes of towels the team packs each day. The numbers are made up.

The presenter types the loop and runs it:

```python
boxes = [12, 9, 15, 11]
total = 0
for count in boxes:
    total = total + count
    print("Running total:", total)
print("Average:", total / len(boxes))
```

```
Running total: 12
Running total: 21
Running total: 36
Running total: 47
Average: 11.75
```

The `print` inside the loop runs 4 times, once per day. The last `print` is not indented, so it runs once, after the loop ends. Moving it inside the loop by mistake would print the average 4 times.

Next, a quick look at `range()` and a `while` loop:

```python
for day in range(1, 4):
    print("Day", day)
stock = 5
while stock > 0:
    stock = stock - 2
print("Stock after loop:", stock)
```

```
Day 1
Day 2
Day 3
Stock after loop: -1
```

The presenter asks: "Why is the stock -1 and not 0?" Trace it: 5 becomes 3, then 1, then -1. Only then is `stock > 0` false. This is why you trace loops by hand.

Finally, the built-in shortcut gives the same total, plus the best day:

```python
print(sum(boxes), max(boxes))
```

```
47 15
```

## Common Mistake
The most common mistake is putting the starting value inside the loop, such as writing `total = 0` as the first line of the loop body. The total is then reset on every pass, and the final result is only the last item. Create the running total **before** the loop, update it **inside** the loop, and use the result **after** the loop. Check the indentation of each line to see which of these three places it is in.

## Key Takeaways
1. A for loop runs its indented block once for each item in a list or `range()`.
2. For a running total, create the variable before the loop, update it inside, and use it after.
3. A while loop repeats while a condition is true; trace it carefully so it ends where you expect.

## Hands-on Exercise
**Task:** Loop over a list of 7 daily sales figures from a café in Lima, and print the weekly total, the average and the best day.
**Tools:** Google Colab (free).
**Steps:**
1. Create a list called `daily_sales` with 7 made-up numbers, one for each day from Monday to Sunday.
2. Create a second list with the 7 day names in the same order.
3. Use a for loop and a running total to calculate the weekly total. Print it after the loop.
4. Calculate and print the average (total divided by 7, or by `len(daily_sales)`).
5. Find the best day. Hint: find the highest value with `max()`, then use `daily_sales.index(best)` to find its position, and use that position in the day-names list.
6. Check your loop total against `sum(daily_sales)`.
**What good looks like:** The loop total and `sum()` give the same number, the average is correct, and the output names the correct best day, such as "Best day: Saturday (410)".
**Time:** about 20 minutes

## Review Flags
- None. All sales and box figures are made up, and every output was produced by running the code with Python 3.11. The Colab stop button is described in general terms only.
