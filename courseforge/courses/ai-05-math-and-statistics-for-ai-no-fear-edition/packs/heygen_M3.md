# HeyGen Batch Pack: AI-05 M3 (Calculus for Learning)

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

## L11 Functions, Slopes and Derivatives

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M3_L11_presenter.mp4`
- **Expected length:** about 5.2 minutes (732 words). The quality gate accepts ±10%.

```text
The word calculus worries many people. Here is a secret. For machine learning, you need one main idea from calculus, and you already use it when you walk up a hill. Is the ground getting steeper or flatter? That feeling is a derivative.

This is Module 3. A function is a rule that turns an input into an output. We write f of x. For example, f of x equals x squared means: take the input and multiply it by itself. So f of three is nine.

The slope of a straight line tells you how much the output changes when the input goes up by one. A slope of two means up two for every one step right. But a curve like y equals x squared is flat near zero and gets steeper as x grows. So we ask: what is the slope at one particular point?

Imagine a straight line that just touches the curve at that point, going in the same direction. This is the tangent line. The derivative is a function that gives this slope at every point. For x squared, the derivative is two x. We write f prime of x equals two x. At one, the slope is two. At two, four. At three, six.

You can also estimate a derivative with numbers. Nudge the input by a tiny amount, h, see how much the output changes, and divide. At three, with h equal to zero point zero zero one, you get six point zero zero one. This nudge and measure idea is how you will check gradients in code.

You only need four rules, and no proofs. A fixed number has derivative zero. The power rule turns x squared into two x. A constant multiple stays: five x squared becomes ten x. And for a sum, take each part: x squared plus three x becomes two x plus three.

Why does this matter? The derivative tells a model which way is downhill for its error, and how steep the hill is. Think of a car's speedometer. The trip record shows the distance travelled. The speedometer shows how fast that distance is changing, right now. A derivative is the speedometer of any function.

Youssef runs a tile workshop in Fez, Morocco. A square tile with side x centimetres has area x squared. He wants to know: if he makes the side a little longer, how fast does the area grow?

Let's look in Desmos. Open the graphing calculator and type f of x equals x squared. The curve appears. Then type a equals one. Desmos offers to make a slider for a, so accept it.

Now type the tangent line: y equals two a times x minus a, plus f of a. It uses the slope two a, and touches the curve at x equals a.

Move the slider to one, then two, then three. It touches the curve at each point, and it gets steeper each time. The slopes are two, four and six.

Now type f prime of x. Desmos draws the derivative for you: the straight line y equals two x.

Now by hand. At a side of three centimetres, the derivative is two times three, which is six. So a tiny increase of zero point zero zero one centimetres adds about zero point zero zero six square centimetres of area. In code, the nudge method prints about six point zero zero one. The long tail of digits is just rounding, not a mistake.

A common mistake is to confuse a function's value with its slope. At three, f of three is nine, but f prime of three is six. The first says how high. The second says how steep. Positive means going up, negative means going down, and zero means flat here.

Let's recap. First, the derivative gives the slope of a function at each point: how fast the output changes when the input changes a little. Second, for x squared the derivative is two x, and four simple rules cover this course. Third, you can check any derivative by nudging the input a tiny amount.

Your turn. In the exercise, you draw tangent lines in Desmos at three points, estimate each slope, and compare with two x. It takes about twenty-five minutes. Next, we measure how wrong a model is, in Loss Functions: How Wrong Is the Model? See you there.
```

## L12 Loss Functions: How Wrong Is the Model?

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M3_L12_presenter.mp4`
- **Expected length:** about 5.1 minutes (715 words). The quality gate accepts ±10%.
- **Pronunciation:** No facts to verify: content.md Review Flags say None. All fares are hypothetical and every calculation was recalculated with NumPy 2.4.

```text
A model makes five predictions. Two are almost perfect, two are a little wrong, and one is badly wrong. Is this a good model? To improve anything, you first need to measure it. And that means turning all those errors into one number.

Last time, we met derivatives. Now we need something to take the derivative of. An error, also called a residual, is the prediction minus the truth. A positive error means the model predicted too high. A negative error means too low.

A loss function combines all the errors into a single number that says how wrong the model is overall. A smaller loss means a better fit. Training a model means searching for the weights that make the loss as small as possible. The loss is the score to beat.

The most common loss for predicting numbers is the mean squared error, or M S E. In words: take each error, square it, then take the mean of the squares. On screen, M S E equals the mean of y pred minus y true, squared.

Why square? One, squares are never negative, so minus ten and plus ten do not cancel. Both count as one hundred. Two, big errors count much more. An error of two becomes four, but thirty becomes nine hundred. Three, the square is smooth, which makes gradients easy in the next lesson.

Two related measures help you explain results. R M S E is the square root of M S E, so it is back in the original units, like lira or minutes. And M A E, the mean absolute error, is the mean of the errors without their signs. It is less affected by one big error.

Picture a teacher who marks late homework with a penalty that grows faster and faster. One day late loses one point, two days lose four, five days lose twenty-five. Small delays hardly matter, but one very late assignment costs a lot. That is exactly how M S E treats errors.

Emre is a data analyst for a taxi app in Istanbul, Türkiye. He compares five fare predictions with the real fares. All values are invented, in lira.

Trip one: true fare one hundred and twenty, predicted one hundred and ten, error minus ten. Trip two: error five. Trip three: true two hundred, predicted two hundred and thirty, error thirty. Trip four: error minus two. Trip five: exactly right, error zero. Squared, that is one hundred, twenty-five, nine hundred, four and zero.

Add the squares: one thousand and twenty-nine. Divide by five: two hundred and five point eight. That is the M S E. The R M S E is its square root, about fourteen point three lira. And look at trip three. Its nine hundred is about eighty-seven percent of the total. One big mistake dominates the loss.

M A E tells a different story. Ten plus five plus thirty plus two plus zero, divided by five, is nine point four lira: a typical error size. In NumPy, Emre writes a small function called m s e. It takes the mean of the squared differences, and prints two hundred and five point eight.

Emre learns that the model is close on most trips. The biggest gain would come from understanding trip three, perhaps a long airport trip.

A common mistake is reading two hundred and five point eight as the model being that many lira off. It is not. M S E is in squared units. Take the square root first. And only compare M S E values on the same data, because they depend on the scale of the target.

Let's recap. First, a loss function turns all prediction errors into one number, and training searches for weights that make it small. Second, M S E is the mean of the squared errors: squaring removes signs and punishes big errors much more. Third, M S E is in squared units, so report R M S E or M A E when you explain error size.

Your turn. In the exercise, you calculate an M S E by hand for five predictions, then write your own m s e function in NumPy and test it. It takes about twenty-five minutes. Next: Gradients and the Chain Rule, Intuitively. See you there.
```

## L13 Gradients and the Chain Rule, Intuitively

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M3_L13_presenter.mp4`
- **Expected length:** about 5.0 minutes (692 words). The quality gate accepts ±10%.
- **Pronunciation:** No facts to verify: content.md Review Flags say None. Every gradient and code output was recalculated with Python.

```text
A real model has many weights, not one. If the loss is too high, which weight should you change, in which direction, and by how much? The gradient answers all three questions at once. And the chain rule shows you how to calculate it.

In lesson eleven, a function had one input and one slope. But a loss usually depends on several weights. For a simple model, y pred equals w times x plus b, the loss depends on the weight w and the bias b.

A partial derivative is the slope in one direction only. Change one weight a tiny amount, keep every other weight fixed, and see how fast the loss changes. We call it the partial derivative of L with respect to w. The curly d symbol just means partial.

The gradient collects the partial derivatives for every weight into one vector. It points in the direction where the loss increases fastest. So to reduce the loss, we move the weights the opposite way. Each part has a sign, which tells you the direction, and a size, which tells you how strongly the loss reacts.

Now the chain rule. A loss is often built in steps: first a prediction, then an error, then a square. To find how the end reacts to the start, multiply the rates of each step. If the error changes two for each unit of w, and the loss changes minus eight for each unit of error, the loss changes minus sixteen for each unit of w.

Picture a set of connected gears. Turn the first gear once, and the second turns twice. Each turn of the second turns the third three times. So one turn of the first turns the third two times three, which is six times. Each step's rate multiplies the next.

Chloé is a researcher at a plant nursery in Montréal, Canada. She has one invented training example. With two litres of a new fertiliser, a plant grew seven centimetres. Her model starts with w equal to one and b equal to one.

Step by step. The prediction is one times two plus one, which is three. The error is prediction minus truth: three minus seven, minus four. The loss is minus four squared, which is sixteen.

Now the chain. The loss is the error squared, so it changes by two times the error: minus eight. The error changes by x, which is two, for each unit of w, and by one for each unit of b. Multiply along the chain. For w: minus eight times two, minus sixteen. For b: minus eight times one, minus eight.

Both parts are negative, so increasing w and b should reduce the loss. That makes sense: a prediction of three is too low. The w part is bigger, because w is multiplied by two, so it has more influence.

To check in code, Chloé nudges one weight a tiny amount up and down, and divides the change in loss by the total nudge. This is a numerical gradient. It prints minus sixteen and minus eight, just like her hand result. Then she takes a small step against the gradient, and the loss falls from sixteen to twelve point nine six.

A common mistake is to move with the gradient instead of against it. The gradient points uphill, so to learn, you subtract it. Another is to stop the chain too early and forget to multiply by x. If your numerical check disagrees, look for a missing link.

Let's recap. First, a partial derivative is the slope for one weight with the others fixed, and the gradient collects them into one vector. Second, the gradient points where the loss increases fastest, so learning moves the weights the opposite way. Third, the chain rule multiplies the rates of each step, and you can always check it by nudging each weight.

You are doing really well. In the exercise, you calculate a two-weight gradient by hand, then check it in Colab by nudging each weight. It takes about twenty-five minutes. Next, we put it all in a loop, in Gradient Descent Step by Step. See you there.
```

## L14 Gradient Descent Step by Step

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M3_L14_presenter.mp4`
- **Expected length:** about 4.9 minutes (685 words). The quality gate accepts ±10%.
- **Pronunciation:** Say the update rule as 'the new weight equals the old weight minus the learning rate times the gradient'; the slide shows the formula.

```text
You now know how to measure how wrong a model is, the loss, and which way is downhill, the gradient. Put those two ideas in a loop, and you have the engine that trains almost every modern machine learning model.

It fits in about six lines of code. Gradient descent finds the weights that make the loss small. Start somewhere, look at the slope, take a small step downhill, and repeat. Each step calculates the gradient, moves each weight a little against it, and repeats until the loss stops falling.

Here is the update rule. The new weight equals the old weight minus the learning rate times the gradient. If the slope is positive, the weight goes down. If it is negative, the weight goes up. Either way, the loss falls. Near the bottom the slope is close to zero, so the steps get smaller by themselves.

The learning rate sets the step size. You choose it, often something like zero point one or zero point zero one. Too small, and learning is very slow. About right, and the loss falls quickly and settles. Too large, and each step jumps past the bottom, so the loss can grow. That is called diverging.

Picture walking downhill in thick fog. You cannot see the valley, but you can feel the slope under your feet. You take a step downhill, feel the slope again, and take another step.

Short steps are safe, but slow. Very long steps might carry you across the valley and up the other side. And plotting the loss against the step number gives a loss curve, the most important picture for checking that training works.

Aroha is a junior machine learning engineer in Wellington, New Zealand. Before trusting her code on real data, she tests it on a toy loss: w minus three, squared. The minimum is at w equals three, where the loss is zero. She starts at w equals zero, with a learning rate of zero point one.

The derivative is two times w minus three. Step one: the gradient is minus six, so w becomes zero point six, and the loss is five point seven six. Step two: w becomes one point zero eight. Step three: one point four six four. The loss falls from nine to five point seven six, three point six nine, and two point three six.

Now in Colab. Aroha types a function called descend. It starts w at zero. In a loop, it calculates the gradient, steps against it, and saves the loss after each step. It runs for thirty steps.

Then she runs it for three learning rates, zero point zero one, zero point one and one point one. She prints the final weight for each, and plots the loss curves. The vertical axis uses a log scale, where each grid line is ten times the one below.

Look at the output. With zero point zero one, w has only reached about one point three six after thirty steps: too slow. With zero point one, it is two point nine nine six three, very close to three. With one point one, it is about minus seven hundred and nine. It jumped across the valley, further every time. That is divergence.

A common mistake: when the loss grows, learners rewrite their gradient formula. Often the formula is fine, and the learning rate is simply too large. First, try one ten times smaller. And always plot the loss curve. It should fall, then flatten.

Let's recap. First, gradient descent repeats one update: the new weight equals the old weight minus the learning rate times the gradient. Second, the learning rate sets the step size. Too small is slow, and too large overshoots and can diverge. Third, always plot the loss curve. It should fall and then flatten out.

You have now built the engine of machine learning. In the exercise, you write your own descend loop in Colab, try three learning rates, and plot the curves. It takes about thirty minutes. Next, we start Module 4 with Classification Metrics: Confusion Matrix, Precision and Recall. See you there.
```
