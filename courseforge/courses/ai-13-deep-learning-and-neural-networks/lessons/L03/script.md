# L03 Neurons, Layers and Activations | Presenter Script

Course: AI-13 · Video: 5 min · Words: 694

## Hook
Stack ten linear layers and you might expect a powerful model. In fact, you get a model that can only draw straight lines, just like logistic regression. One small function between the layers changes everything.

## Explain
Last time, we learned to shape tensors. Now we pass them through layers. A neuron computes a weighted sum of its inputs, plus a bias. A linear layer is many neurons side by side, working on a whole batch at once.

A linear layer has one weight for every pair of input and output, plus one bias for each output. Keep that rule in mind, because we will count parameters in a moment.

Here is the surprise. If you stack two linear layers with nothing in between, the result is still one linear function. A straight line of a straight line is still a straight line. Depth adds nothing.

An activation function fixes this. It adds a bend after each hidden layer. ReLU is the default. It keeps positive values and turns negative values into zero. Sigmoid and tanh squash values into a range, but they can slow learning in deep networks. GELU, a smooth version of ReLU, is common in transformers.

Think of each layer as a team in a factory, and the activation as a quality gate between teams. Without the gates, ten teams in a row can only do what one team could do. The gates decide what passes on, so later teams can build new things.

For classification, the last layer has no activation. It outputs raw scores called logits, one per class. The cross-entropy loss applies softmax for you. For a simple chain of layers, use a sequential container. For branches or custom logic, write your own module class. You create the layers in one method and describe the data flow in another, called forward. PyTorch then tracks every parameter for you.

## Demonstrate
Let's build one. Aroha is an engineer at an energy company in Wellington, New Zealand. She wants to classify ten types of fault from seven hundred and eighty-four sensor readings per event.

In Colab, she defines a model called FaultNet. Inside it, a sequential block goes from seven hundred and eighty-four inputs to two hundred and fifty-six, then to one hundred and twenty-eight, then to ten outputs. There is a ReLU after each hidden layer, and nothing after the last one.

Next, she counts the parameters by adding up the size of every weight and bias tensor. The total is two hundred and thirty-five thousand, one hundred and forty-six.

She checks it by hand, layer by layer. Almost two hundred and one thousand parameters sit in the first layer alone. That is typical when the inputs are wide, and in lesson seven you will see why it becomes a problem for images.

Finally, a forward pass. She sends a random batch of sixteen events through the model and gets sixteen rows of ten logits. One row per event, one score per fault type. Softmax turns them into probabilities, but only for reading, never for the loss.

A common mistake is adding softmax as the last layer and then using cross-entropy loss. Softmax is then applied twice. Training still runs, but gradients become small and learning is slower. Output raw logits, and use softmax only to show probabilities. Also, call the model directly, not its forward method, so PyTorch runs its hooks.

## Recap
Let's recap. First, a linear layer is a weighted sum plus a bias for many neurons at once. Its parameter count is inputs times outputs, plus outputs. Second, activations like ReLU add the bend that makes depth useful. Without them, stacked layers collapse into one linear model. Third, build models with a sequential container or a module class, and return raw logits for classification.

## CTA
Now it is your turn. In the exercise below this video, you will build a three-layer network for a ten-class problem, check its parameter count by hand, and then remove the ReLUs and explain what changes. It takes about twenty minutes. In the next lesson, we see how networks learn, with loss and backpropagation. See you there.

## Thumbnail
Headline: Why Layers Need ReLU
Image: Navy background, three stacked layers of nodes with a teal bent line between them, headline in teal Inter Bold.

## Production Notes
- Review flags: none. Run the FaultNet cell once before recording and confirm the printed parameter count 235146 and the output shape torch.Size([16, 10]).
- Hand-count slide must match content.md exactly: 784×256 + 256 = 200,960; 256×128 + 128 = 32,896; 128×10 + 10 = 1,290; total 235,146.
- Aroha and the Wellington energy company are hypothetical; stock footage must not show a real company name or logo.
