# HeyGen Batch Pack: AI-05 M1 (Vectors and Matrices)

Course: Math and Statistics for AI (No-Fear Edition). Make one HeyGen video per lesson below, using these settings for every video.

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

## L01 Maths for AI Without Fear

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M1_L01_presenter.mp4`
- **Expected length:** about 5.2 minutes (729 words). The quality gate accepts ±10%.

```text
Many people feel their stomach tighten when they see a page of maths symbols. If that is you, you are in the right place. Machine learning uses a surprisingly small amount of maths, and you can learn it one small step at a time.

Hi, and welcome to Math and Statistics for AI, the No-Fear Edition. In this first lesson, we draw a map of the whole course, and you will run your very first line of Python.

A machine learning model is a set of calculations. It turns data into a prediction, and then it improves itself. This course covers the four areas of maths that make that possible. Each one has a clear job inside the model.

First, linear algebra, which means vectors and matrices. It stores the data and makes the predictions. That is Module 1. Second, probability and statistics. They describe data and uncertainty. That is Module 2.

Third, calculus, which means derivatives and gradients. This is how a model learns. It tells the model which way to change its numbers so its errors get smaller. That is Module 3. And fourth, metrics, which turn results into numbers you can judge. That is Module 4, with the capstone, where you build linear regression from scratch.

You already know the maths you need to start. Fractions, percentages and reading a simple graph. We will add new words slowly, and we will always explain a symbol in words before we use it.

Every lesson follows the same three-step routine. First, a picture: a drawing, a graph, or an everyday situation. Second, a small hand calculation with tiny numbers. Third, code: the same calculation in Python with NumPy, a free library for numbers, in Google Colab. The code never replaces your understanding. It checks your work.

Think of it like learning to cook from a recipe. The picture is the photo of the finished dish. The hand calculation is cooking a small portion slowly. The code is the kitchen machine that cooks a large portion quickly.

Let's try the routine together. Mariana runs a small bakery in Bogotá, Colombia. She wants her average daily sales of a new cake over five days. The numbers are twelve, fifteen, nine, twenty and fourteen cakes.

Step one, the picture. Five bars of different heights. The average is the height they would all have if you made them level. Step two, the hand calculation. Twelve plus fifteen plus nine plus twenty plus fourteen equals seventy cakes. The mean is the total divided by the number of days. Seventy divided by five equals fourteen cakes per day.

Step three, the code. Open a web browser and go to Google Colab. If Colab asks you to, sign in with a Google account. Then create a new notebook, for example from the File menu.

Click in the first code cell. The first line loads NumPy with the short name n p. The next line creates a NumPy array, which is a list of numbers that NumPy can calculate with quickly. Here it holds Mariana's five sales numbers.

Then we print two things. Sales dot sum adds the numbers. Sales dot mean finds the average. Now run the cell with the play button next to it, or press Shift and Enter together.

And there it is. Seventy, and fourteen point zero. It matches our hand calculation exactly.

One common mistake is to think you must understand every formula perfectly before you are allowed to write code. So people stop at the first hard symbol and decide they are not a maths person. In fact, understanding grows in layers. If a symbol confuses you, go back to the picture and the tiny numbers.

Let's recap. First, machine learning uses four areas of maths. Linear algebra stores data and makes predictions, statistics describes data and uncertainty, calculus drives learning, and metrics judge results. Second, every lesson follows the same routine: a picture, a small hand calculation, then code. Third, a NumPy array is a list of numbers you can calculate with, for example with sum and mean.

Now it is your turn. In the exercise below this video, you choose five made-up numbers, find their sum and mean on paper, then check them in your own Colab notebook. It takes about fifteen minutes. In the next lesson, we meet vectors: data as lists of numbers. See you there.
```

## L02 Vectors: Data as Lists of Numbers

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M1_L02_presenter.mp4`
- **Expected length:** about 5.2 minutes (724 words). The quality gate accepts ±10%.

```text
How does a computer see a flat for rent, a customer or a song? It cannot see them at all. It sees a short list of numbers. Once you understand that list, you understand how almost all machine learning data is stored.

In the last lesson, you ran your first NumPy cell. Today we meet the most basic building block of all: the vector. A vector is an ordered list of numbers that describes one thing. Ordered means the position of each number matters.

Imagine a flat in Lisbon, described by three numbers: size in square metres, number of rooms, and age in years. The vector seventy-five, three, twenty means seventy-five square metres, three rooms and twenty years old. Swap the first two numbers and you describe a very strange flat.

Each position is called a component, and each component is one feature of the thing we describe. The number of components is the dimension. This flat vector has dimension three. A vector with two components, like three, one, can be drawn as an arrow from the origin: three steps right and one step up.

You need three operations. One, adding vectors. First plus first, second plus second. So three, one plus one, two equals four, three. Two, multiplying by a number. Two times three, one equals six, two. The arrow keeps its direction but becomes twice as long. A single number like this is called a scalar, because it scales the vector.

Three, length, also called the norm. For a 2D vector, square each component, add them, and take the square root. For three, four: three squared plus four squared is nine plus sixteen, which is twenty-five, and the square root of twenty-five is five. In NumPy, n p dot linalg dot norm does this for any dimension.

Here is a simple picture. A vector is like a row on a recipe card: two eggs, three hundred grams of flour, one cup of milk. The order matters, because everyone must agree which number means eggs. Doubling the recipe multiplies every amount by two, exactly like a scalar.

Inês is a data analyst at an estate agency in Lisbon, Portugal. She describes flats as size, rooms and age. Flat A is seventy-five, three, twenty.

A client asks: what would twice this flat look like? Two times seventy-five, three, twenty gives one hundred and fifty, six, forty. Inês notices the age is silly, because a larger flat is not older. The maths always works, but you must check that the result makes sense.

Now let's see it in 2D with Desmos. Open the Desmos graphing calculator in your browser. In the first line, type a equals three, one. In the second, b equals one, two. Desmos shows two points. Then use the vector function to draw an arrow from the origin to each point.

To add them, place arrow b at the end of arrow a. Then draw one arrow from the origin to a plus b. It ends at four, three, which is exactly the sum we calculated by hand.

Now type two a. The point six, two appears. It is in the same direction as a, but twice as far from the origin.

Finally, Inês checks everything in Colab. She creates a and b as NumPy arrays, then prints a plus b, two times a, and the length of three, four. The output is four, three, then six, two, then five point zero. Everything agrees.

A common mistake is adding vectors whose components mean different things. For example, one flat stored as size, rooms, age, and another as rooms, size, age. NumPy adds them without any warning, and the result is nonsense. So keep the same feature order, and write it down in your notebook.

Let's recap. First, a vector is an ordered list of numbers that describes one thing, and each position is one feature. Second, you add vectors component by component, and a scalar multiplies every component. Third, the length, or norm, is the square root of the sum of the squared components.

Now it is your turn. In the exercise, you draw two vectors in Desmos, add them, and check with NumPy. Then you describe three things from your own work as vectors. It takes about twenty minutes. Next time: the dot product, weighted sums and similarity. See you there.
```

## L03 The Dot Product: Weighted Sums and Similarity

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M1_L03_presenter.mp4`
- **Expected length:** about 5.2 minutes (721 words). The quality gate accepts ±10%.

```text
If a courier needs two minutes for every kilometre and five minutes for every stop, how long will a trip take? You can answer that in your head. Without noticing, you just did the most common calculation in machine learning.

Last time, we learned that a vector is a list of numbers. Today we combine two vectors into one number, with the dot product. In words: multiply the matching components, then add the results.

Take a equals two, five and b equals eight, three. First components: two times eight is sixteen. Second components: five times three is fifteen. Add them: sixteen plus fifteen is thirty-one. So a dot b equals thirty-one. In NumPy, you write n p dot dot, with a and b inside.

Why does this matter? Many models predict with a weighted sum. Each feature has a weight that says how much it matters. The prediction is weight times feature, for every feature, all added together. That is exactly a dot product of weights and features.

Later, we also add a starting value called the bias. So a one-feature model reads: y equals w times x plus b. In words, the prediction is the weight times the input, plus a starting value.

The dot product also measures similarity. Imagine taste scores for spicy, sweet and sour, from zero to four. Customer A is one, two, zero. Customer B is two, four, zero. Customer C is zero, zero, three. A dot B is two plus eight plus zero, which is ten. A dot C is zero. A and B like the same things. A and C share nothing.

Recommendation systems use this idea to find similar users or products. Long vectors give bigger dot products, so people often divide by both lengths. This is called cosine similarity, and it is always between minus one and one. For A and B it is exactly one, because B is just A doubled.

Here is an everyday picture. A dot product is like a shopping bill. The quantities in your basket are the features, and the prices are the weights. Multiply each quantity by its price, add everything up, and you get one total. A prediction is the bill for one example.

Let's use it. Dewi is an operations planner for a delivery start-up in Jakarta, Indonesia. Her team estimates that each kilometre adds about two minutes, and each stop adds about five minutes. These numbers are invented for the example.

Her weight vector is two, five: minutes per kilometre, and minutes per stop. Tomorrow's first trip is eight kilometres with three stops, so the feature vector is eight, three. Picture two bars stacked on top of each other, one for distance time and one for stop time.

By hand: two times eight is sixteen minutes for distance. Five times three is fifteen minutes for stops. The total is thirty-one minutes. In code, Dewi makes two NumPy arrays, w and x, and prints n p dot of w and x. The answer is thirty-one again.

Dewi also learns to read the weights. If the trip had one more stop, the prediction would rise by five minutes, the weight for stops. Each weight tells you how much the prediction changes when its feature grows by one. You will use this same reading in the capstone.

A common mistake is to multiply the matching components and forget to add them. In NumPy, w star x gives sixteen, fifteen, which is still a vector. N p dot gives thirty-one, one number. And if the vectors have different lengths, NumPy stops with an error. That error is helpful: every feature needs exactly one weight.

Let's recap. First, the dot product multiplies matching components and adds the results, giving one number. Second, a model's prediction is often a weighted sum of features, which is a dot product of weights and features. Third, a large dot product, or a cosine similarity close to one, means two vectors point in a similar direction, and zero means they share nothing.

Your turn. In the exercise, you calculate three dot products by hand, check them with n p dot, and make a price prediction for a small invented product. It takes about twenty minutes. Next, we store a whole dataset at once, in Matrices: A Whole Dataset at Once. See you there.
```

## L04 Matrices: A Whole Dataset at Once

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M1_L04_presenter.mp4`
- **Expected length:** about 5.0 minutes (694 words). The quality gate accepts ±10%.
- **Pronunciation:** No facts to verify: content.md Review Flags say None. All data is hypothetical and the NumPy output was run and confirmed. Not a screen demo lesson: code appears only on code slides. Say shapes as 'four by three'; the slides show 4 × 3.

```text
You already know how to read a spreadsheet. Each row is one record, and each column is one kind of information. Good news: that is almost exactly what a matrix is. You have been using matrices for years without the name.

In the last lesson, we made one prediction with a dot product. Today we store a whole dataset at once. A matrix is a rectangle of numbers, arranged in rows and columns. In machine learning, it follows one simple rule.

Each row is one example, like one day, one customer or one flat. Each column is one feature, like temperature, age or price. So each row is a vector, and a matrix is many vectors stacked on top of each other.

The shape of a matrix is rows by columns. A matrix with four rows and three columns has shape four by three. In NumPy, capital X dot shape tells you. Check the shape first in any dataset, because it tells you how many examples and features you have.

To get one number, give its row and its column. But careful: NumPy counts from zero, not one. So X, row one, column two means the second row and the third column. A colon means all rows, so colon, two gives every value in column two. And X with just one number gives a whole row.

The transpose flips a matrix, so rows become columns. The first row becomes the first column. A four by three matrix becomes three by four. In NumPy you write X dot T. You will need it in the capstone, when you calculate gradients.

Think of a cinema seating plan. To find one seat, you need a row and a seat number. A whole row is one line of seats. A column is every seat with the same number, from front to back. Transposing is like turning the plan on its side.

Let's meet Zofia. She manages a bicycle rental shop in Kraków, Poland. She records four days in a spreadsheet, with three columns: temperature in degrees Celsius, rain in millimetres, and bikes rented. The numbers are invented.

Here is the table. Day one: eighteen degrees, no rain, one hundred and twenty bikes. Day two: twenty-two, two, ninety-five. Day three: fifteen, ten, forty. Day four: twenty-five, no rain, one hundred and fifty bikes. Four rows, three columns. So the shape is four by three.

By hand: row one, the second day, is twenty-two, two, ninety-five. Column two, bikes rented, is one hundred and twenty, ninety-five, forty, one hundred and fifty. And the value at row one, column two, is ninety-five.

In code, Zofia types the table into a NumPy array, one inner list per row. Then she prints the shape, the bikes column, row one, the single value, and the shape of the transpose. The results are four by three, the four bike numbers, the second day, ninety-five, and three by four.

Then Zofia notices something important. Bikes rented is the value she wants to predict, so it should not sit with the inputs. We usually split the table into a feature matrix X, with temperature and rain, and a target vector y, with bikes rented. You will do this in the capstone.

The most common mistake is counting from one. You want the first column, you write colon, one, and you get the second column. In NumPy, the first column is colon, zero. And remember: row first, then column. If a result looks strange, print the shape and compare with your table.

Let's recap. First, a data matrix stores one example per row and one feature per column, and its shape is rows by columns. Second, NumPy counts from zero, so row one, column two is the second row and the third column. Third, the transpose swaps rows and columns, so four by three becomes three by four.

Your turn. In the exercise, you invent a small sales table with six rows and three columns, build it in NumPy, select a column and a row, and transpose it. It takes about twenty minutes. Next, we put matrices to work, in Matrix Multiplication as Many Predictions. See you there.
```

## L05 Matrix Multiplication as Many Predictions

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M1_L05_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
In lesson three you made one prediction with one dot product. But a real model may need to make a million predictions. Do you write a million lines of code? No. You write one short line, and matrix multiplication does the rest.

Here is the key idea. Multiplying a data matrix by a weight vector does one dot product for every row. Each row is one example, so each dot product is one prediction. The result is a vector, with one prediction per example.

Say X has three rows and two columns, and w has two numbers. The prediction for row zero is row zero dot w. The same for row one, and for row two. In NumPy, you write X, the at symbol, w. The at symbol means matrix multiplication.

Now the shape rule. Write the two shapes side by side: three by two, and two by one. The two inner numbers must be equal, here two and two. That makes sense: every row has two features, so we need one weight for each. The two outer numbers give the result: three by one, one prediction for each of the three examples.

If the inner numbers are different, say three by two and three by one, the multiplication is not defined, and NumPy stops with an error. That error is your friend. It tells you the number of weights does not match the number of features. And order matters: X times w is not the same as w times X.

Picture a cashier with a price list. Each customer's basket is one row. The price list is the weight vector. The cashier makes one bill for every customer in the queue, with the same list. Matrix multiplication serves the whole queue in one go.

Linh runs an online clothing shop in Hanoi, Viet Nam. In this invented example, a shirt costs ten and a pair of socks costs three. Three orders arrived today. Order zero: two shirts and one pair of socks. Order one: three and four. Order two: five and two.

By hand, one dot product per row. Order zero: two times ten plus one times three, which is twenty plus three, twenty-three. Order one: thirty plus twelve, forty-two. Order two: fifty plus six, fifty-six. Three by two times two by one gives three by one. Three totals.

Now in Colab. Linh creates the matrix X from the three orders, and the weights w, ten and three. She prints both shapes. X is three by two. Notice that NumPy shows w as just two, comma. That is a plain vector with two numbers, and NumPy treats it as two by one when you multiply.

Next, she prints X at w. The output is twenty-three, forty-two, fifty-six. Exactly our hand calculation, in one short line.

Now let's make a mistake on purpose. Linh adds a third weight and runs the cell again. NumPy stops with a value error. It says there is a mismatch in the core dimension, and that size three is different from two. In plain words: the matrix has two columns, but you gave three weights.

A common mistake is to fix a shape error by changing the data until the error goes away, for example by adding a column of zeros. The code runs, but the model is wrong. Instead, read both shapes, find the inner numbers that differ, and ask why.

Let's recap. First, X at w does one dot product per row, so it predicts for every example at once. Second, the inner sizes must match: three by two times two by one works, and the outer sizes give the result, three by one. Third, a shape error means the weights do not match the features, so read the shapes first.

Well done: that completes Module 1. In the exercise, you multiply a three by two matrix by a vector by hand, check it with the at operator, and explain one shape error. It takes about twenty minutes. Next, we start statistics with Describing Data: Mean, Median and Spread. See you there.
```
