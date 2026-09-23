# L05 Repeating Work with Loops | Presenter Script

Course: AI-11 · Video: 5 min · Words: 697

## Hook
Adding up four numbers by hand is easy. Adding up forty thousand rows of sales is not. Computers are very good at doing the same small job again and again, without getting tired. In Python, the tool for this is the loop.

## Explain
Last time, our code made decisions. Now it will repeat work. A for loop runs the same block of code once for each item in a collection. Read this example as, for each item in boxes, call it count, and run the indented code.

On the first pass, count is the first item. On the second pass, it is the second item, and so on, until the list ends. Just like if, the line ends with a colon, and the body is indented.

Think of a cashier at a supermarket. The cashier picks up each item in the basket, one after another, scans it, and adds its price to the total. The cashier doesn't need to know how many items there are. When the basket is empty, the cashier stops and shows the total.

That is a very common pattern, called the running total. You create a variable at zero before the loop, and add to it inside the loop. You can also loop over range, which gives a sequence of numbers. It starts at the first number, and stops before the second.

A while loop is different. It repeats as long as a condition stays true. It is useful when you don't know how many passes you need. But be careful. If the condition never becomes false, the loop never ends. In Colab, you can stop a running cell with the stop button next to it.

When is a loop the right tool? Use one when you must do the same steps for every item. For simple totals, Python also has built-in functions, such as sum, max, min and len. They do the loop for you. And in week three, you will see that pandas does most loops for you too.

## Demonstrate
Let's see a loop in action. Ayşe manages a small textile workshop in İzmir, in Türkiye. She records how many boxes of towels her team packs each day. The numbers are made up.

We store four days of boxes in a list, and set the total to zero. Inside the loop, we add each day's count to the total and print it. After the loop, not indented, we print the average.

Run it. The running total grows from twelve to forty-seven, one line per day. Then the average appears once, eleven point seven five, because that line runs after the loop ends.

Next, a quick look at range and a while loop. The for loop prints day one, day two and day three. Then the stock starts at five, and the while loop takes away two, while the stock is above zero. The result is minus one. Why not zero?

Let's trace it. Five becomes three, then one, then minus one. Only then is the condition false. This is why we trace loops by hand. Finally, the built-in shortcut. Sum and max give forty-seven, and the best day, fifteen.

Here is the most common mistake with loops. It is putting the starting value inside the loop. Then the total resets on every pass, and you only get the last item. Create the total before the loop, update it inside, and use it after. The indentation of each line shows you which of these three places it is in.

## Recap
Let's recap. First, a for loop runs its indented block once for each item in a list or a range. Second, for a running total, create the variable before the loop, update it inside, and use it after. Third, a while loop repeats while a condition is true, so trace it carefully to check where it ends.

## CTA
Now it is your turn. In the exercise below this video, you will loop over seven daily sales figures from a café in Lima, and print the weekly total, the average and the best day. It takes about twenty minutes. In the next lesson, we package our logic into functions. See you there.

## Thumbnail
Headline: Let the Loop Work
Image: Navy background, a circular arrow around a stack of boxes with a counter showing 47, headline in teal Inter Bold.

## Production Notes
- [VERSION] Check the Colab button for stopping a running cell against the live interface before recording.
- Ayşe and her İzmir textile workshop are fictional; all box and sales figures are made up.
- Printed outputs on screen must match content.md exactly: 'Running total: 12 / 21 / 36 / 47' and 'Average: 11.75'; 'Day 1 / Day 2 / Day 3' and 'Stock after loop: -1'; '47 15'.
- Stock -1 question: pause on screen for about two seconds before revealing the trace (5 → 3 → 1 → -1).
