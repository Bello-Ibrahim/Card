# L12 Loss Functions: How Wrong Is the Model? | Presenter Script

Course: AI-05 · Video: 5 min · Words: 720

## Hook
A model makes five predictions. Two are almost perfect, two are a little wrong, and one is badly wrong. Is this a good model? To improve anything, you first need to measure it. And that means turning all those errors into one number.

## Explain
Last time, we met derivatives. Now we need something to take the derivative of. An error, also called a residual, is the prediction minus the truth. A positive error means the model predicted too high. A negative error means too low.

A loss function combines all the errors into a single number that says how wrong the model is overall. A smaller loss means a better fit. Training a model means searching for the weights that make the loss as small as possible. The loss is the score to beat.

The most common loss for predicting numbers is the mean squared error, or M S E. In words: take each error, square it, then take the mean of the squares. On screen, M S E equals the mean of y pred minus y true, squared.

Why square? One, squares are never negative, so minus ten and plus ten do not cancel. Both count as one hundred. Two, big errors count much more. An error of two becomes four, but thirty becomes nine hundred. Three, the square is smooth, which makes gradients easy in the next lesson.

Two related measures help you explain results. R M S E is the square root of M S E, so it is back in the original units, like lira or minutes. And M A E, the mean absolute error, is the mean of the errors without their signs. It is less affected by one big error.

Picture a teacher who marks late homework with a penalty that grows faster and faster. One day late loses one point, two days lose four, five days lose twenty-five. Small delays hardly matter, but one very late assignment costs a lot. That is exactly how M S E treats errors.

## Demonstrate
Emre is a data analyst for a taxi app in Istanbul, Türkiye. He compares five fare predictions with the real fares. All values are invented, in lira.

Trip one: true fare one hundred and twenty, predicted one hundred and ten, error minus ten. Trip two: error five. Trip three: true two hundred, predicted two hundred and thirty, error thirty. Trip four: error minus two. Trip five: exactly right, error zero. Squared, that is one hundred, twenty-five, nine hundred, four and zero.

Add the squares: one thousand and twenty-nine. Divide by five: two hundred and five point eight. That is the M S E. The R M S E is its square root, about fourteen point three lira. And look at trip three. Its nine hundred is about eighty-seven percent of the total. One big mistake dominates the loss.

M A E tells a different story. Ten plus five plus thirty plus two plus zero, divided by five, is nine point four lira: a typical error size. In NumPy, Emre writes a small function called m s e. It takes the mean of the squared differences, and prints two hundred and five point eight.

Emre learns that the model is close on most trips. The biggest gain would come from understanding trip three, perhaps a long airport trip.

A common mistake is reading two hundred and five point eight as the model being that many lira off. It is not. M S E is in squared units. Take the square root first. And only compare M S E values on the same data, because they depend on the scale of the target.

## Recap
Let's recap. First, a loss function turns all prediction errors into one number, and training searches for weights that make it small. Second, M S E is the mean of the squared errors: squaring removes signs and punishes big errors much more. Third, M S E is in squared units, so report R M S E or M A E when you explain error size.

## CTA
Your turn. In the exercise, you calculate an M S E by hand for five predictions, then write your own m s e function in NumPy and test it. It takes about twenty-five minutes. Next: Gradients and the Chain Rule, Intuitively. See you there.

## Thumbnail
Headline: How Wrong Is It?
Image: Navy background, five small squares of different sizes with one very large square, headline in teal Inter Bold.

## Production Notes
- No facts to verify: content.md Review Flags say None. All fares are hypothetical and every calculation was recalculated with NumPy 2.4.
- content.md gives RMSE as 'about 14.3 lira' in the text and 'about 14.35' in the code comment. The voiceover says 'about fourteen point three'; the code slide shows the code comment as written.
- Emre and the Istanbul taxi app are fictional. No real taxi app brands or logos in stock footage.
- Not a screen demo lesson: code appears only on a code slide.
