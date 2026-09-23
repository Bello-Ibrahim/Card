# L14 Gradient Descent Step by Step | Presenter Script

Course: AI-05 · Video: 5 min · Words: 685

## Hook
You now know how to measure how wrong a model is, the loss, and which way is downhill, the gradient. Put those two ideas in a loop, and you have the engine that trains almost every modern machine learning model.

## Explain
It fits in about six lines of code. Gradient descent finds the weights that make the loss small. Start somewhere, look at the slope, take a small step downhill, and repeat. Each step calculates the gradient, moves each weight a little against it, and repeats until the loss stops falling.

Here is the update rule. The new weight equals the old weight minus the learning rate times the gradient. If the slope is positive, the weight goes down. If it is negative, the weight goes up. Either way, the loss falls. Near the bottom the slope is close to zero, so the steps get smaller by themselves.

The learning rate sets the step size. You choose it, often something like zero point one or zero point zero one. Too small, and learning is very slow. About right, and the loss falls quickly and settles. Too large, and each step jumps past the bottom, so the loss can grow. That is called diverging.

Picture walking downhill in thick fog. You cannot see the valley, but you can feel the slope under your feet. You take a step downhill, feel the slope again, and take another step.

Short steps are safe, but slow. Very long steps might carry you across the valley and up the other side. And plotting the loss against the step number gives a loss curve, the most important picture for checking that training works.

## Demonstrate
Aroha is a junior machine learning engineer in Wellington, New Zealand. Before trusting her code on real data, she tests it on a toy loss: w minus three, squared. The minimum is at w equals three, where the loss is zero. She starts at w equals zero, with a learning rate of zero point one.

The derivative is two times w minus three. Step one: the gradient is minus six, so w becomes zero point six, and the loss is five point seven six. Step two: w becomes one point zero eight. Step three: one point four six four. The loss falls from nine to five point seven six, three point six nine, and two point three six.

Now in Colab. Aroha types a function called descend. It starts w at zero. In a loop, it calculates the gradient, steps against it, and saves the loss after each step. It runs for thirty steps.

Then she runs it for three learning rates, zero point zero one, zero point one and one point one. She prints the final weight for each, and plots the loss curves. The vertical axis uses a log scale, where each grid line is ten times the one below.

Look at the output. With zero point zero one, w has only reached about one point three six after thirty steps: too slow. With zero point one, it is two point nine nine six three, very close to three. With one point one, it is about minus seven hundred and nine. It jumped across the valley, further every time. That is divergence.

A common mistake: when the loss grows, learners rewrite their gradient formula. Often the formula is fine, and the learning rate is simply too large. First, try one ten times smaller. And always plot the loss curve. It should fall, then flatten.

## Recap
Let's recap. First, gradient descent repeats one update: the new weight equals the old weight minus the learning rate times the gradient. Second, the learning rate sets the step size. Too small is slow, and too large overshoots and can diverge. Third, always plot the loss curve. It should fall and then flatten out.

## CTA
You have now built the engine of machine learning. In the exercise, you write your own descend loop in Colab, try three learning rates, and plot the curves. It takes about thirty minutes. Next, we start Module 4 with Classification Metrics: Confusion Matrix, Precision and Recall. See you there.

## Thumbnail
Headline: Walking Downhill in Fog
Image: Navy background, a U-shaped curve with small teal dots stepping down towards the bottom, headline in teal Inter Bold.

## Production Notes
- [VERSION] Google Colab and Matplotlib: confirm the current Colab interface and that plt.yscale("log") and plt.legend() behave as shown before recording the screen scenes. Outputs (0.01 → 1.3635, 0.1 → 2.9963, 1.1 → −709.1289) were checked with Python and NumPy 2.4.
- Aroha and the Wellington setting are fictional. The toy loss (w − 3)² is a teaching example.
- Say the update rule as 'the new weight equals the old weight minus the learning rate times the gradient'; the slide shows the formula.
- Optional hero B-roll (scene 5): if the stock search finds a suitable misty hillside walker, use stock instead and drop the hero clip.
