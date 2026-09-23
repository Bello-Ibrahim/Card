# L04 How Networks Learn: Loss and Backpropagation | Presenter Script

Course: AI-13 · Video: 5 min · Words: 701

## Hook
The network from the last lesson has two hundred and thirty-five thousand parameters, all set to random values. Nobody will tune them by hand. So how does each one know which way to move? The answer is one line of code.

## Explain
Training needs three parts. The first is a loss function. It gives one number that says how wrong the model is on a batch.

For classes, use cross-entropy loss. It takes raw logits and whole-number class labels. For numbers, use mean squared error, with predictions and targets of the same shape. For yes or no labels, or several labels at once, there is a binary version that takes one logit per label.

The second part is gradients. A quick recap from the maths course. The gradient tells you how much the loss changes, and in which direction, if you move one parameter a little. Backpropagation is the chain rule, applied layer by layer from the loss back to the inputs.

You never write it yourself. PyTorch's autograd records every operation on tensors that need gradients. Then one call to backward fills in the gradient of every parameter.

The third part is gradient descent. Each parameter moves a small step against its gradient. The learning rate sets the step size. Too small, and training is slow. Too large, and the loss jumps around or grows.

Picture walking downhill in thick fog. You cannot see the valley, but you can feel the slope under your feet. At each step, you move a little in the steepest downhill direction. Very long steps can take you past the valley and up the other side.

Two details matter in code. Gradients add up with every backward call, so you reset them to zero before the next step. And the update itself must not be recorded, so you do it inside a no-grad block.

## Demonstrate
Bilal is a data scientist at a logistics company in Lahore, Pakistan. Before he trusts optimisers, he tests gradient descent on a function he can check by hand. W minus three, squared. The lowest point is at three, and at zero the gradient should be minus six.

In Colab, he creates w at zero and asks PyTorch to track its gradient. He computes the loss, calls backward, and prints the gradient. Minus six, exactly as the hand calculation said.

Now the loop. For ten steps, he computes the loss, calls backward, moves w against the gradient inside a no-grad block, and resets the gradient to zero. The learning rate is zero point one.

After ten steps, w is about two point six eight, close to three. The plot shows the loss falling quickly at first, and then more slowly. Each step moves w twenty percent of the remaining distance.

Then Bilal changes the learning rate to one point one. Now each step overshoots. W moves further from three every time, and the loss grows. You will see this same pattern in real learning curves in lesson eight.

In real training, an optimiser does the update and the reset for every parameter at once. Adam, which adapts the step size for each parameter, is a common default.

The most common mistake is forgetting to zero the gradients. They keep adding up, so the steps grow larger and larger. The loss may fall, then jump or become not a number. It looks like a learning-rate problem, but it is not.

## Recap
Let's recap. First, the loss is one number for how wrong the model is. Use cross-entropy with logits and integer labels for classes, and mean squared error for numbers. Second, backward uses autograd to compute every gradient by the chain rule. Gradients accumulate, so reset them every step. Third, gradient descent moves parameters against the gradient, and the learning rate sets the step size.

## CTA
Now it is your turn. In the exercise below this video, you will pick a function with a known minimum, check its gradient with autograd, take ten manual steps, and plot the loss for a good and a bad learning rate. It takes about twenty-five minutes. In the next lesson, we put it all together in the training loop. See you there.

## Thumbnail
Headline: Walking Downhill in Fog
Image: Navy background, a teal loss curve shaped like a valley with small footsteps walking down it through soft fog, headline in teal Inter Bold.

## Production Notes
- Review flags: none. Run the snippet before recording and confirm the printed values: w.grad = tensor(-6.) and w after 10 steps = 2.678.
- For the lr = 1.1 comparison, change only the lr value in the same cell and re-run; the plotted loss must grow. Record both plots.
- Bilal and the Lahore logistics company are hypothetical; stock footage must not show a real company name or logo.
