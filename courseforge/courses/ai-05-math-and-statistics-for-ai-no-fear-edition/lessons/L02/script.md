# L02 Vectors: Data as Lists of Numbers | Presenter Script

Course: AI-05 · Video: 5 min · Words: 730

## Hook
How does a computer see a flat for rent, a customer or a song? It cannot see them at all. It sees a short list of numbers. Once you understand that list, you understand how almost all machine learning data is stored.

## Explain
In the last lesson, you ran your first NumPy cell. Today we meet the most basic building block of all: the vector. A vector is an ordered list of numbers that describes one thing. Ordered means the position of each number matters.

Imagine a flat in Lisbon, described by three numbers: size in square metres, number of rooms, and age in years. The vector seventy-five, three, twenty means seventy-five square metres, three rooms and twenty years old. Swap the first two numbers and you describe a very strange flat.

Each position is called a component, and each component is one feature of the thing we describe. The number of components is the dimension. This flat vector has dimension three. A vector with two components, like three, one, can be drawn as an arrow from the origin: three steps right and one step up.

You need three operations. One, adding vectors. First plus first, second plus second. So three, one plus one, two equals four, three. Two, multiplying by a number. Two times three, one equals six, two. The arrow keeps its direction but becomes twice as long. A single number like this is called a scalar, because it scales the vector.

Three, length, also called the norm. For a 2D vector, square each component, add them, and take the square root. For three, four: three squared plus four squared is nine plus sixteen, which is twenty-five, and the square root of twenty-five is five. In NumPy, n p dot linalg dot norm does this for any dimension.

Here is a simple picture. A vector is like a row on a recipe card: two eggs, three hundred grams of flour, one cup of milk. The order matters, because everyone must agree which number means eggs. Doubling the recipe multiplies every amount by two, exactly like a scalar.

## Demonstrate
Inês is a data analyst at an estate agency in Lisbon, Portugal. She describes flats as size, rooms and age. Flat A is seventy-five, three, twenty.

A client asks: what would twice this flat look like? Two times seventy-five, three, twenty gives one hundred and fifty, six, forty. Inês notices the age is silly, because a larger flat is not older. The maths always works, but you must check that the result makes sense.

Now let's see it in 2D with Desmos. Open the Desmos graphing calculator in your browser. In the first line, type a equals three, one. In the second, b equals one, two. Desmos shows two points. Then use the vector function to draw an arrow from the origin to each point.

To add them, place arrow b at the end of arrow a. Then draw one arrow from the origin to a plus b. It ends at four, three, which is exactly the sum we calculated by hand.

Now type two a. The point six, two appears. It is in the same direction as a, but twice as far from the origin.

Finally, Inês checks everything in Colab. She creates a and b as NumPy arrays, then prints a plus b, two times a, and the length of three, four. The output is four, three, then six, two, then five point zero. Everything agrees.

A common mistake is adding vectors whose components mean different things. For example, one flat stored as size, rooms, age, and another as rooms, size, age. NumPy adds them without any warning, and the result is nonsense. So keep the same feature order, and write it down in your notebook.

## Recap
Let's recap. First, a vector is an ordered list of numbers that describes one thing, and each position is one feature. Second, you add vectors component by component, and a scalar multiplies every component. Third, the length, or norm, is the square root of the sum of the squared components.

## CTA
Now it is your turn. In the exercise, you draw two vectors in Desmos, add them, and check with NumPy. Then you describe three things from your own work as vectors. It takes about twenty minutes. Next time: the dot product, weighted sums and similarity. See you there.

## Thumbnail
Headline: Data as Arrows
Image: Navy background, two teal arrows from the origin and a third arrow showing their sum, headline in teal Inter Bold.

## Production Notes
- [VERSION] Desmos: confirm that typing a point such as a=(3,1), the vector() function and expressions such as a+b and 2a still work as described in the live graphing calculator before recording scenes 10 to 12.
- [VERSION] Google Colab: confirm the interface before recording scene 13.
- Inês and the Lisbon estate agency are hypothetical; the flat vector [75, 3, 20] is invented. Do not show a real agency name or logo in stock footage.
- Speak vectors as lists, for example 'seventy-five, three, twenty'; the slides and screen show the square brackets.
