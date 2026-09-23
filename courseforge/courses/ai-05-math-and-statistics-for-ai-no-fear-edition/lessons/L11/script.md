# L11 Functions, Slopes and Derivatives | Presenter Script

Course: AI-05 · Video: 5 min · Words: 733

## Hook
The word calculus worries many people. Here is a secret. For machine learning, you need one main idea from calculus, and you already use it when you walk up a hill. Is the ground getting steeper or flatter? That feeling is a derivative.

## Explain
This is Module 3. A function is a rule that turns an input into an output. We write f of x. For example, f of x equals x squared means: take the input and multiply it by itself. So f of three is nine.

The slope of a straight line tells you how much the output changes when the input goes up by one. A slope of two means up two for every one step right. But a curve like y equals x squared is flat near zero and gets steeper as x grows. So we ask: what is the slope at one particular point?

Imagine a straight line that just touches the curve at that point, going in the same direction. This is the tangent line. The derivative is a function that gives this slope at every point. For x squared, the derivative is two x. We write f prime of x equals two x. At one, the slope is two. At two, four. At three, six.

You can also estimate a derivative with numbers. Nudge the input by a tiny amount, h, see how much the output changes, and divide. At three, with h equal to zero point zero zero one, you get six point zero zero one. This nudge and measure idea is how you will check gradients in code.

You only need four rules, and no proofs. A fixed number has derivative zero. The power rule turns x squared into two x. A constant multiple stays: five x squared becomes ten x. And for a sum, take each part: x squared plus three x becomes two x plus three.

Why does this matter? The derivative tells a model which way is downhill for its error, and how steep the hill is. Think of a car's speedometer. The trip record shows the distance travelled. The speedometer shows how fast that distance is changing, right now. A derivative is the speedometer of any function.

## Demonstrate
Youssef runs a tile workshop in Fez, Morocco. A square tile with side x centimetres has area x squared. He wants to know: if he makes the side a little longer, how fast does the area grow?

Let's look in Desmos. Open the graphing calculator and type f of x equals x squared. The curve appears. Then type a equals one. Desmos offers to make a slider for a, so accept it.

Now type the tangent line: y equals two a times x minus a, plus f of a. It uses the slope two a, and touches the curve at x equals a.

Move the slider to one, then two, then three. It touches the curve at each point, and it gets steeper each time. The slopes are two, four and six.

Now type f prime of x. Desmos draws the derivative for you: the straight line y equals two x.

Now by hand. At a side of three centimetres, the derivative is two times three, which is six. So a tiny increase of zero point zero zero one centimetres adds about zero point zero zero six square centimetres of area. In code, the nudge method prints about six point zero zero one. The long tail of digits is just rounding, not a mistake.

A common mistake is to confuse a function's value with its slope. At three, f of three is nine, but f prime of three is six. The first says how high. The second says how steep. Positive means going up, negative means going down, and zero means flat here.

## Recap
Let's recap. First, the derivative gives the slope of a function at each point: how fast the output changes when the input changes a little. Second, for x squared the derivative is two x, and four simple rules cover this course. Third, you can check any derivative by nudging the input a tiny amount.

## CTA
Your turn. In the exercise, you draw tangent lines in Desmos at three points, estimate each slope, and compare with two x. It takes about twenty-five minutes. Next, we measure how wrong a model is, in Loss Functions: How Wrong Is the Model? See you there.

## Thumbnail
Headline: How Steep Is It?
Image: Navy background, a teal parabola with a tangent line touching it at one point, headline in teal Inter Bold.

## Production Notes
- [VERSION] Desmos: confirm that function notation f(x)=, automatic slider creation for a, and the f'(x) derivative notation work as described in the live graphing calculator before recording scenes 9 to 12.
- Youssef and the Fez tile workshop are fictional. No real workshop names or logos in stock footage.
- Speak f(x) as 'f of x' and f'(x) as 'f prime of x'; show the notation on slides and in Desmos.
- The code check (scene 13) is shown on a code slide; the long output 6.000999999999479 is a normal rounding effect and the voiceover says so.
