# L04 Matrices: A Whole Dataset at Once | Presenter Script

Course: AI-05 · Video: 5 min · Words: 702

## Hook
You already know how to read a spreadsheet. Each row is one record, and each column is one kind of information. Good news: that is almost exactly what a matrix is. You have been using matrices for years without the name.

## Explain
In the last lesson, we made one prediction with a dot product. Today we store a whole dataset at once. A matrix is a rectangle of numbers, arranged in rows and columns. In machine learning, it follows one simple rule.

Each row is one example, like one day, one customer or one flat. Each column is one feature, like temperature, age or price. So each row is a vector, and a matrix is many vectors stacked on top of each other.

The shape of a matrix is rows by columns. A matrix with four rows and three columns has shape four by three. In NumPy, capital X dot shape tells you. Check the shape first in any dataset, because it tells you how many examples and features you have.

To get one number, give its row and its column. But careful: NumPy counts from zero, not one. So X, row one, column two means the second row and the third column. A colon means all rows, so colon, two gives every value in column two. And X with just one number gives a whole row.

The transpose flips a matrix, so rows become columns. The first row becomes the first column. A four by three matrix becomes three by four. In NumPy you write X dot T. You will need it in the capstone, when you calculate gradients.

Think of a cinema seating plan. To find one seat, you need a row and a seat number. A whole row is one line of seats. A column is every seat with the same number, from front to back. Transposing is like turning the plan on its side.

## Demonstrate
Let's meet Zofia. She manages a bicycle rental shop in Kraków, Poland. She records four days in a spreadsheet, with three columns: temperature in degrees Celsius, rain in millimetres, and bikes rented. The numbers are invented.

Here is the table. Day one: eighteen degrees, no rain, one hundred and twenty bikes. Day two: twenty-two, two, ninety-five. Day three: fifteen, ten, forty. Day four: twenty-five, no rain, one hundred and fifty bikes. Four rows, three columns. So the shape is four by three.

By hand: row one, the second day, is twenty-two, two, ninety-five. Column two, bikes rented, is one hundred and twenty, ninety-five, forty, one hundred and fifty. And the value at row one, column two, is ninety-five.

In code, Zofia types the table into a NumPy array, one inner list per row. Then she prints the shape, the bikes column, row one, the single value, and the shape of the transpose. The results are four by three, the four bike numbers, the second day, ninety-five, and three by four.

Then Zofia notices something important. Bikes rented is the value she wants to predict, so it should not sit with the inputs. We usually split the table into a feature matrix X, with temperature and rain, and a target vector y, with bikes rented. You will do this in the capstone.

The most common mistake is counting from one. You want the first column, you write colon, one, and you get the second column. In NumPy, the first column is colon, zero. And remember: row first, then column. If a result looks strange, print the shape and compare with your table.

## Recap
Let's recap. First, a data matrix stores one example per row and one feature per column, and its shape is rows by columns. Second, NumPy counts from zero, so row one, column two is the second row and the third column. Third, the transpose swaps rows and columns, so four by three becomes three by four.

## CTA
Your turn. In the exercise, you invent a small sales table with six rows and three columns, build it in NumPy, select a column and a row, and transpose it. It takes about twenty minutes. Next, we put matrices to work, in Matrix Multiplication as Many Predictions. See you there.

## Thumbnail
Headline: Your Spreadsheet Is a Matrix
Image: Navy background, a small spreadsheet grid morphing into a bracketed matrix of numbers, headline in teal Inter Bold.

## Production Notes
- No facts to verify: content.md Review Flags say None. All data is hypothetical and the NumPy output was run and confirmed.
- Zofia and the Kraków bicycle rental shop are fictional; the four days of data (18, 0, 120 / 22, 2, 95 / 15, 10, 40 / 25, 0, 150) are invented. No real shop names or logos in stock footage.
- Not a screen demo lesson: code appears only on code slides. Say shapes as 'four by three'; the slides show 4 × 3.
