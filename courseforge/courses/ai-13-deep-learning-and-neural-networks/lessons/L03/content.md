# L03 Neurons, Layers and Activations

Course: AI-13 · Module: M1 · Objectives: O1, O2 · Video: 5 min (screen demo)

## Hook
Stack ten linear layers on top of each other and you might expect a powerful model. In fact, you get a model that can only draw straight lines, exactly like logistic regression. One small function between the layers changes that.

## Explanation
A **neuron** computes a weighted sum of its inputs plus a bias: `z = w·x + b`. A **linear layer** (`nn.Linear(in_features, out_features)`) is many neurons side by side. In matrix form it computes `x @ W.T + b` for a whole batch at once. It has `in × out` weights and `out` biases.

If you stack two linear layers with nothing in between, the result is still one linear function, because a linear function of a linear function is linear. Depth adds nothing.

An **activation function** adds non-linearity after each hidden layer, so the network can bend its decision boundary and build complex features from simple ones:

- **ReLU**: `max(0, z)`. The default choice for hidden layers: fast, simple and it does not saturate for positive inputs.
- **Sigmoid** and **tanh**: squash values into a range. They saturate for large inputs, which can slow learning in deep networks (L15).
- **GELU**: a smooth version of ReLU, common in transformers (L12).

For classification, the **last layer has no activation** in PyTorch. It outputs raw scores called **logits**, one per class. The loss function `nn.CrossEntropyLoss` applies softmax internally (L04).

**Building models.** For a simple chain of layers, use `nn.Sequential`. For anything with branches or custom logic, subclass `nn.Module`: create layers in `__init__` and describe the data flow in `forward`. PyTorch then tracks all parameters for you through `model.parameters()`.

**Analogy:** Think of each layer as a team in a factory, and the activation as a quality gate between teams. Without the gates, ten teams in a row can only do what one team could do, because every step just scales and adds. The gates decide what passes on and what is dropped, and that lets later teams build new things from earlier results.

## Worked Example
Aroha is an ML engineer at a hypothetical energy company in Wellington, New Zealand. She wants to classify 10 types of fault from 784 sensor readings per event.

**Screen demo steps:**

1. Define the model as a subclass of `nn.Module`.
2. Count the parameters.
3. Run a forward pass on random data and check the output shape.

```python
import torch
from torch import nn

class FaultNet(nn.Module):
    def __init__(self, n_in=784, n_classes=10):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_in, 256), nn.ReLU(),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, n_classes),       # logits, no activation
        )
    def forward(self, x):
        return self.net(x)

model = FaultNet()
n_params = sum(p.numel() for p in model.parameters())
print(n_params)                               # 235146

x = torch.randn(16, 784)                      # batch of 16 events
logits = model(x)
print(logits.shape)                           # torch.Size([16, 10])
probs = logits.softmax(dim=1)                 # only for reading, not for the loss
```

Aroha checks the count by hand: 784×256 + 256 = 200,960; 256×128 + 128 = 32,896; 128×10 + 10 = 1,290. The total is 235,146. Most parameters are in the first layer, which is typical when inputs are wide. In L07 you will see why this becomes a problem for images.

## Common Mistake
Many learners add `nn.Softmax` as the last layer and then use `nn.CrossEntropyLoss`. The loss already applies log-softmax, so softmax is applied twice. Training still runs, but the gradients become small and learning is slower and less stable. Output raw logits from the model, and apply `softmax` only when you want to show probabilities. A second mistake is calling `model.forward(x)` directly; call `model(x)` instead, so that PyTorch runs its hooks.

## Key Takeaways
1. A linear layer is a weighted sum plus a bias for many neurons at once; its parameter count is `in × out + out`.
2. Activations such as ReLU add the non-linearity that makes depth useful; without them, stacked linear layers collapse into one linear model.
3. Build models with `nn.Sequential` or an `nn.Module` subclass, and return raw logits for classification.

## Hands-on Exercise
**Task:** Build a 3-layer network for a 10-class problem, print its parameter count, and run one forward pass on random data.
**Tools:** Google Colab (free, CPU is enough for this exercise); PyTorch.
**Steps:**
1. Choose an input size, for example 20 features for a tabular problem or 784 for a flattened 28×28 image.
2. Build a network with two hidden layers, ReLU activations and a 10-unit output layer, using an `nn.Module` subclass.
3. Print the model and its parameter count, and check the count by hand for each layer.
4. Pass a random batch of shape `(8, input_size)` and confirm the output shape is `(8, 10)`.
5. Remove both ReLU layers, and write two sentences on why the model can now only learn a linear decision boundary.
**What good looks like:** A working model, a parameter count that matches your hand calculation, the correct output shape, no softmax in the model, and a clear explanation of why activations matter.
**Time:** about 20 minutes

## Review Flags
- None. The lesson uses stable, core PyTorch modules and a hypothetical example; the parameter count must be confirmed by running the snippet before recording.
