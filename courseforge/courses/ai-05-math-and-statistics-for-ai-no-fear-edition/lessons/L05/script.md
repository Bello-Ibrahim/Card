# L05 Matrix Multiplication as Many Predictions | Presenter Script

Course: AI-05 · Video: 5 min · Words: 685

## Hook
In lesson three you made one prediction with one dot product. But a real model may need to make a million predictions. Do you write a million lines of code? No. You write one short line, and matrix multiplication does the rest.

## Explain
Here is the key idea. Multiplying a data matrix by a weight vector does one dot product for every row. Each row is one example, so each dot product is one prediction. The result is a vector, with one prediction per example.

Say X has three rows and two columns, and w has two numbers. The prediction for row zero is row zero dot w. The same for row one, and for row two. In NumPy, you write X, the at symbol, w. The at symbol means matrix multiplication.

Now the shape rule. Write the two shapes side by side: three by two, and two by one. The two inner numbers must be equal, here two and two. That makes sense: every row has two features, so we need one weight for each. The two outer numbers give the result: three by one, one prediction for each of the three examples.

If the inner numbers are different, say three by two and three by one, the multiplication is not defined, and NumPy stops with an error. That error is your friend. It tells you the number of weights does not match the number of features. And order matters: X times w is not the same as w times X.

Picture a cashier with a price list. Each customer's basket is one row. The price list is the weight vector. The cashier makes one bill for every customer in the queue, with the same list. Matrix multiplication serves the whole queue in one go.

## Demonstrate
Linh runs an online clothing shop in Hanoi, Viet Nam. In this invented example, a shirt costs ten and a pair of socks costs three. Three orders arrived today. Order zero: two shirts and one pair of socks. Order one: three and four. Order two: five and two.

By hand, one dot product per row. Order zero: two times ten plus one times three, which is twenty plus three, twenty-three. Order one: thirty plus twelve, forty-two. Order two: fifty plus six, fifty-six. Three by two times two by one gives three by one. Three totals.

Now in Colab. Linh creates the matrix X from the three orders, and the weights w, ten and three. She prints both shapes. X is three by two. Notice that NumPy shows w as just two, comma. That is a plain vector with two numbers, and NumPy treats it as two by one when you multiply.

Next, she prints X at w. The output is twenty-three, forty-two, fifty-six. Exactly our hand calculation, in one short line.

Now let's make a mistake on purpose. Linh adds a third weight and runs the cell again. NumPy stops with a value error. It says there is a mismatch in the core dimension, and that size three is different from two. In plain words: the matrix has two columns, but you gave three weights.

A common mistake is to fix a shape error by changing the data until the error goes away, for example by adding a column of zeros. The code runs, but the model is wrong. Instead, read both shapes, find the inner numbers that differ, and ask why.

## Recap
Let's recap. First, X at w does one dot product per row, so it predicts for every example at once. Second, the inner sizes must match: three by two times two by one works, and the outer sizes give the result, three by one. Third, a shape error means the weights do not match the features, so read the shapes first.

## CTA
Well done: that completes Module 1. In the exercise, you multiply a three by two matrix by a vector by hand, check it with the at operator, and explain one shape error. It takes about twenty minutes. Next, we start statistics with Describing Data: Mean, Median and Spread. See you there.

## Thumbnail
Headline: Many Predictions, One Line
Image: Navy background, a 3 × 2 matrix times a 2 × 1 vector producing a column 23, 42, 56, headline in teal Inter Bold.

## Production Notes
- [VERSION] NumPy: the @ operator is stable, but confirm the exact wording of the shape-mismatch ValueError against the current NumPy version before recording scene 13. The message in content.md ('mismatch in its core dimension', 'size 3 is different from 2') was checked with NumPy 2.4; the voiceover paraphrases it so it survives small wording changes.
- [VERSION] Google Colab: confirm the interface before recording the screen scenes.
- Linh, the Hanoi clothing shop and the prices (shirt 10, socks 3) are hypothetical. No real brand names or logos in stock footage.
