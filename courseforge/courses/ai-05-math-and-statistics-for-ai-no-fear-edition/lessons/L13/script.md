# L13 Gradients and the Chain Rule, Intuitively | Presenter Script

Course: AI-05 · Video: 5 min · Words: 694

## Hook
A real model has many weights, not one. If the loss is too high, which weight should you change, in which direction, and by how much? The gradient answers all three questions at once. And the chain rule shows you how to calculate it.

## Explain
In lesson eleven, a function had one input and one slope. But a loss usually depends on several weights. For a simple model, y pred equals w times x plus b, the loss depends on the weight w and the bias b.

A partial derivative is the slope in one direction only. Change one weight a tiny amount, keep every other weight fixed, and see how fast the loss changes. We call it the partial derivative of L with respect to w. The curly d symbol just means partial.

The gradient collects the partial derivatives for every weight into one vector. It points in the direction where the loss increases fastest. So to reduce the loss, we move the weights the opposite way. Each part has a sign, which tells you the direction, and a size, which tells you how strongly the loss reacts.

Now the chain rule. A loss is often built in steps: first a prediction, then an error, then a square. To find how the end reacts to the start, multiply the rates of each step. If the error changes two for each unit of w, and the loss changes minus eight for each unit of error, the loss changes minus sixteen for each unit of w.

Picture a set of connected gears. Turn the first gear once, and the second turns twice. Each turn of the second turns the third three times. So one turn of the first turns the third two times three, which is six times. Each step's rate multiplies the next.

## Demonstrate
Chloé is a researcher at a plant nursery in Montréal, Canada. She has one invented training example. With two litres of a new fertiliser, a plant grew seven centimetres. Her model starts with w equal to one and b equal to one.

Step by step. The prediction is one times two plus one, which is three. The error is prediction minus truth: three minus seven, minus four. The loss is minus four squared, which is sixteen.

Now the chain. The loss is the error squared, so it changes by two times the error: minus eight. The error changes by x, which is two, for each unit of w, and by one for each unit of b. Multiply along the chain. For w: minus eight times two, minus sixteen. For b: minus eight times one, minus eight.

Both parts are negative, so increasing w and b should reduce the loss. That makes sense: a prediction of three is too low. The w part is bigger, because w is multiplied by two, so it has more influence.

To check in code, Chloé nudges one weight a tiny amount up and down, and divides the change in loss by the total nudge. This is a numerical gradient. It prints minus sixteen and minus eight, just like her hand result. Then she takes a small step against the gradient, and the loss falls from sixteen to twelve point nine six.

A common mistake is to move with the gradient instead of against it. The gradient points uphill, so to learn, you subtract it. Another is to stop the chain too early and forget to multiply by x. If your numerical check disagrees, look for a missing link.

## Recap
Let's recap. First, a partial derivative is the slope for one weight with the others fixed, and the gradient collects them into one vector. Second, the gradient points where the loss increases fastest, so learning moves the weights the opposite way. Third, the chain rule multiplies the rates of each step, and you can always check it by nudging each weight.

## CTA
You are doing really well. In the exercise, you calculate a two-weight gradient by hand, then check it in Colab by nudging each weight. It takes about twenty-five minutes. Next, we put it all in a loop, in Gradient Descent Step by Step. See you there.

## Thumbnail
Headline: Which Weight, Which Way?
Image: Navy background, three interlocking teal gears with small arrows showing rotation, headline in teal Inter Bold.

## Production Notes
- No facts to verify: content.md Review Flags say None. Every gradient and code output was recalculated with Python.
- Chloé and the Montréal plant nursery are fictional; the single training example (x = 2 litres, y = 7 cm) is invented.
- Speak ∂L/∂w as 'the partial derivative of L with respect to w'; the slides show the notation.
- Not a screen demo lesson: code appears only on a code slide.
