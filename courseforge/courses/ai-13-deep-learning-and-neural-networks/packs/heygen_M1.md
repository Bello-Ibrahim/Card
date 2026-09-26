# HeyGen Batch Pack: AI-13 M1 (From Classical ML to Neural Networks)

Course: Deep Learning and Neural Networks. Make one HeyGen video per lesson below, using these settings for every video.

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

## L01 Why Deep Learning?

- **Filename:** `ai-13-deep-learning-and-neural-networks_M1_L01_presenter.mp4`
- **Expected length:** about 5.3 minutes (734 words). The quality gate accepts ±10%.

```text
You can already get a strong result from a gradient-boosted model on a clean table in a few minutes. So why spend hours training a neural network on a GPU? Sometimes, you should not. Let's see when deep learning is worth the cost.

Hi, and welcome to Deep Learning and Neural Networks. In this first lesson, we decide when deep learning makes sense, and we get a GPU ready.

The classical models from the scikit-learn course, such as random forests and gradient boosting, work on features that already mean something. Age, income, the number of late payments. A person does most of the work by building those features.

Images, audio and text are different. A colour photo of two hundred and twenty-four by two hundred and twenty-four pixels is about one hundred and fifty thousand numbers. No single pixel means leaf disease or cat.

The useful features are patterns of patterns. Edges, then textures, then shapes, then objects. A neural network learns these features directly from the raw data, layer by layer. This is called representation learning, and it is why deep learning works so well on unstructured data.

But the cost is real. Networks usually need more labelled data, unless you start from a pretrained model. They need more compute. They have more settings to tune and more ways to fail. And it is harder to explain why they made a decision.

Here is a way to picture it. Classical machine learning is like a skilled tailor who works from measurements someone else has taken. Deep learning is a tailor who also learns to take the measurements from photos. More flexible, but slower to learn.

So, a practical rule. On small or medium tables, try a tree-based model first. On images, audio or text, start with a pretrained network. And why a GPU? It runs thousands of simple calculations in parallel, which is exactly what matrix multiplication inside every layer needs.

Meet Dilnoza, a data scientist at a textile company in Tashkent, Uzbekistan. Project A predicts late supplier deliveries from a table of eight thousand orders. Her gradient-boosting model already scores well, so she keeps it.

Project B detects weaving faults in fabric photos. There are no useful columns, only pixels, and hand-made features miss small holes and uneven threads. That is a good case for a convolutional network. Let's prepare the GPU.

Open a new Colab notebook. From the Runtime menu, choose Change runtime type, select a GPU hardware accelerator, and save.

Now run the check cell. It prints the PyTorch version, and whether PyTorch can see a GPU. If it says true, you are ready. If it says false, the code still runs, but on the CPU, and slowly.

Next, the timing cell. It creates a large random matrix of about four thousand by four thousand numbers, multiplies it by itself on the CPU, and then does the same on the GPU.

Run it twice, because the first GPU run includes start-up time. On the second run, you should see something like a GPU that is many times faster. Exact numbers depend on your hardware.

Notice the synchronise calls. GPU work runs in the background, so without them the timer stops too early.

One common mistake is to think deep learning is always better. On small tables, a well-tuned tree model is often just as accurate, faster and easier to explain. Choose deep learning because of the data, not because it is newer.

A quick note on access. Free GPU limits change and are not guaranteed, and Colab is not available everywhere. Every exercise in this course also finishes on a CPU with a smaller data subset, in Colab or a local notebook.

Let's recap. First, neural networks learn features from raw, unstructured data like images, audio and text. On small tables, classical models are often just as good and cheaper. Second, deep learning costs more data, compute, tuning and explanation, so choose it for a reason. Third, check for a GPU in PyTorch, choose a device for your tensors, and synchronise before timing GPU work.

Now it is your turn. In the exercise below this video, you will switch to a GPU runtime, time the matrix multiplication three times on each device, and write two sentences about a project of yours. It takes about twenty minutes. In the next lesson, we learn tensors, the language of PyTorch. See you there.
```

## L02 Tensors: The Language of PyTorch

- **Filename:** `ai-13-deep-learning-and-neural-networks_M1_L02_presenter.mp4`
- **Expected length:** about 5.0 minutes (696 words). The quality gate accepts ±10%.

```text
Your first PyTorch error will probably not be about maths. It will say that two shapes cannot be multiplied. Most beginner bugs in deep learning are shape bugs. Today, you learn to read them and fix them fast.

In the last lesson, we got a GPU ready. Now we meet the data structure that lives on it. A tensor is PyTorch's main data structure. If you know NumPy arrays, you already know most of it.

Every tensor has three properties you should check all the time. Its shape, which is the size of each dimension. Its dtype, the number type, such as float for inputs and weights, or a long integer for class labels. And its device, the CPU or the GPU.

Two tensors in one operation must have compatible shapes, and they must be on the same device. Tensors also do two things NumPy arrays cannot. They run on a GPU, and they can record operations for automatic gradients, which we use in lesson four.

In PyTorch, the first dimension is almost always the batch. Images use batch, channels, height, width. Many image libraries put the channels last instead, so you often need to reorder.

Here is a picture to keep in mind. A tensor's shape is like a stack of egg trays. One tray has rows and columns. A stack adds layers. A box of stacks adds one more dimension.

Reshaping moves the eggs into trays of a different size, but the number of eggs never changes. If the sizes do not multiply to the same total, the reshape fails. Reshape and view change the shape. Permute reorders the dimensions. Unsqueeze adds a batch dimension of size one.

Broadcasting follows the same rules as NumPy. Shapes are compared from the right, and a size of one can stretch to match. That is how you subtract one mean per colour channel from a whole batch of images.

Let's go to Colab. Tomás is an engineer at an agritech start-up in Valparaíso, Chile. He loads grape photos with an image library and wants to feed them to a network.

He starts with a batch of thirty-two photos, sixty-four pixels square, with the channels last. One permute moves the channels to position one. Now the print shows thirty-two, three, sixty-four, sixty-four, as float numbers on the CPU.

Next, he makes a mean with one value per channel, shaped three, one, one, and subtracts it. Broadcasting stretches it across the whole batch. Then he moves the batch to the GPU.

For a linear layer, he flattens each image into one long row. The minus one tells PyTorch to work out the size, which is twelve thousand two hundred and eighty-eight. He also creates class labels as whole numbers, and picks one image with a new batch dimension.

Now Tomás gets an error. Expected all tensors to be on the same device. His images are on the GPU, but the labels are still on the CPU. The fix is always the same. Move both to one device.

The most common mistake is using reshape when you need permute. Both give the same shape, but reshape only reinterprets the numbers in memory order. The pixels get mixed, and no error appears. The model just learns badly.

Use permute to reorder dimensions, and reshape only to merge or split dimensions that are already in order. And when you predict on one example, always add the batch dimension first.

Let's recap. First, check shape, dtype and device for every tensor you create. Most bugs show up in one of the three. Second, PyTorch puts the batch first, and images use batch, channels, height, width. Use permute to reorder, and reshape only to merge or split. Third, broadcasting compares shapes from the right, and every tensor in one operation must be on the same device.

Now it is your turn. In the exercise below this video, you will create a batch of thirty-two colour images, move it to the GPU, and fix three shape errors in a provided cell, with one line explaining each fix. It takes about twenty minutes. In the next lesson, we build neurons, layers and activations. See you there.
```

## L03 Neurons, Layers and Activations

- **Filename:** `ai-13-deep-learning-and-neural-networks_M1_L03_presenter.mp4`
- **Expected length:** about 5.0 minutes (684 words). The quality gate accepts ±10%.

```text
Stack ten linear layers and you might expect a powerful model. In fact, you get a model that can only draw straight lines, just like logistic regression. One small function between the layers changes everything.

Last time, we learned to shape tensors. Now we pass them through layers. A neuron computes a weighted sum of its inputs, plus a bias. A linear layer is many neurons side by side, working on a whole batch at once.

A linear layer has one weight for every pair of input and output, plus one bias for each output. Keep that rule in mind, because we will count parameters in a moment.

Here is the surprise. If you stack two linear layers with nothing in between, the result is still one linear function. A straight line of a straight line is still a straight line. Depth adds nothing.

An activation function fixes this. It adds a bend after each hidden layer. ReLU is the default. It keeps positive values and turns negative values into zero. Sigmoid and tanh squash values into a range, but they can slow learning in deep networks. GELU, a smooth version of ReLU, is common in transformers.

Think of each layer as a team in a factory, and the activation as a quality gate between teams. Without the gates, ten teams in a row can only do what one team could do. The gates decide what passes on, so later teams can build new things.

For classification, the last layer has no activation. It outputs raw scores called logits, one per class. The cross-entropy loss applies softmax for you. For a simple chain of layers, use a sequential container. For branches or custom logic, write your own module class. You create the layers in one method and describe the data flow in another, called forward. PyTorch then tracks every parameter for you.

Let's build one. Aroha is an engineer at an energy company in Wellington, New Zealand. She wants to classify ten types of fault from seven hundred and eighty-four sensor readings per event.

In Colab, she defines a model called FaultNet. Inside it, a sequential block goes from seven hundred and eighty-four inputs to two hundred and fifty-six, then to one hundred and twenty-eight, then to ten outputs. There is a ReLU after each hidden layer, and nothing after the last one.

Next, she counts the parameters by adding up the size of every weight and bias tensor. The total is two hundred and thirty-five thousand, one hundred and forty-six.

She checks it by hand, layer by layer. Almost two hundred and one thousand parameters sit in the first layer alone. That is typical when the inputs are wide, and in lesson seven you will see why it becomes a problem for images.

Finally, a forward pass. She sends a random batch of sixteen events through the model and gets sixteen rows of ten logits. One row per event, one score per fault type. Softmax turns them into probabilities, but only for reading, never for the loss.

A common mistake is adding softmax as the last layer and then using cross-entropy loss. Softmax is then applied twice. Training still runs, but gradients become small and learning is slower. Output raw logits, and use softmax only to show probabilities. Also, call the model directly, not its forward method, so PyTorch runs its hooks.

Let's recap. First, a linear layer is a weighted sum plus a bias for many neurons at once. Its parameter count is inputs times outputs, plus outputs. Second, activations like ReLU add the bend that makes depth useful. Without them, stacked layers collapse into one linear model. Third, build models with a sequential container or a module class, and return raw logits for classification.

Now it is your turn. In the exercise below this video, you will build a three-layer network for a ten-class problem, check its parameter count by hand, and then remove the ReLUs and explain what changes. It takes about twenty minutes. In the next lesson, we see how networks learn, with loss and backpropagation. See you there.
```

## L04 How Networks Learn: Loss and Backpropagation

- **Filename:** `ai-13-deep-learning-and-neural-networks_M1_L04_presenter.mp4`
- **Expected length:** about 5.0 minutes (693 words). The quality gate accepts ±10%.

```text
The network from the last lesson has two hundred and thirty-five thousand parameters, all set to random values. Nobody will tune them by hand. So how does each one know which way to move? The answer is one line of code.

Training needs three parts. The first is a loss function. It gives one number that says how wrong the model is on a batch.

For classes, use cross-entropy loss. It takes raw logits and whole-number class labels. For numbers, use mean squared error, with predictions and targets of the same shape. For yes or no labels, or several labels at once, there is a binary version that takes one logit per label.

The second part is gradients. A quick recap from the maths course. The gradient tells you how much the loss changes, and in which direction, if you move one parameter a little. Backpropagation is the chain rule, applied layer by layer from the loss back to the inputs.

You never write it yourself. PyTorch's autograd records every operation on tensors that need gradients. Then one call to backward fills in the gradient of every parameter.

The third part is gradient descent. Each parameter moves a small step against its gradient. The learning rate sets the step size. Too small, and training is slow. Too large, and the loss jumps around or grows.

Picture walking downhill in thick fog. You cannot see the valley, but you can feel the slope under your feet. At each step, you move a little in the steepest downhill direction. Very long steps can take you past the valley and up the other side.

Two details matter in code. Gradients add up with every backward call, so you reset them to zero before the next step. And the update itself must not be recorded, so you do it inside a no-grad block.

Bilal is a data scientist at a logistics company in Lahore, Pakistan. Before he trusts optimisers, he tests gradient descent on a function he can check by hand. W minus three, squared. The lowest point is at three, and at zero the gradient should be minus six.

In Colab, he creates w at zero and asks PyTorch to track its gradient. He computes the loss, calls backward, and prints the gradient. Minus six, exactly as the hand calculation said.

Now the loop. For ten steps, he computes the loss, calls backward, moves w against the gradient inside a no-grad block, and resets the gradient to zero. The learning rate is zero point one.

After ten steps, w is about two point six eight, close to three. The plot shows the loss falling quickly at first, and then more slowly. Each step moves w twenty percent of the remaining distance.

Then Bilal changes the learning rate to one point one. Now each step overshoots. W moves further from three every time, and the loss grows. You will see this same pattern in real learning curves in lesson eight.

In real training, an optimiser does the update and the reset for every parameter at once. Adam, which adapts the step size for each parameter, is a common default.

The most common mistake is forgetting to zero the gradients. They keep adding up, so the steps grow larger and larger. The loss may fall, then jump or become not a number. It looks like a learning-rate problem, but it is not.

Let's recap. First, the loss is one number for how wrong the model is. Use cross-entropy with logits and integer labels for classes, and mean squared error for numbers. Second, backward uses autograd to compute every gradient by the chain rule. Gradients accumulate, so reset them every step. Third, gradient descent moves parameters against the gradient, and the learning rate sets the step size.

Now it is your turn. In the exercise below this video, you will pick a function with a known minimum, check its gradient with autograd, take ten manual steps, and plot the loss for a good and a bad learning rate. It takes about twenty-five minutes. In the next lesson, we put it all together in the training loop. See you there.
```

## L05 The Training Loop

- **Filename:** `ai-13-deep-learning-and-neural-networks_M1_L05_presenter.mp4`
- **Expected length:** about 4.9 minutes (678 words). The quality gate accepts ±10%.
- **Pronunciation:** The dataset is synthetic (make_classification); say so on screen. Folasade and the Ibadan microfinance lender are hypothetical; stock footage must not show a real company name or logo.

```text
In scikit-learn, training is one line. You call fit. In PyTorch, you write the loop yourself. That sounds like extra work, but it is why PyTorch is so flexible. Every later lesson is a small change to the loop you write today.

First, the data. A dataset answers two questions. How many examples are there, and what is example number i? For data already in tensors, a ready-made tensor dataset is enough. A data loader wraps it and gives you mini-batches, shuffled for training and in a fixed order for validation.

One step processes one batch and updates the weights once. One epoch is one full pass over the training data. With eight thousand examples and a batch size of sixty-four, one epoch has one hundred and twenty-five steps. Smaller batches give noisier but more frequent updates. Larger batches use the GPU better, but need more memory.

The core loop has five lines, always in this order. Clear the old gradients. Run the forward pass. Compute the loss. Compute the gradients with backward. Then let the optimiser update the weights.

Validation needs two switches. Eval mode changes how layers such as dropout behave. The no-grad block stops autograd from recording, which saves memory and time. You need both. Then switch back to train mode for the next epoch.

Think of a language class. Each batch is one lesson with a few exercises. The teacher marks them, explains each error, and the student adjusts. An epoch is the whole textbook once. Validation is a mock exam. There is no feedback, and the student does not study from it.

Folasade is a data scientist at a microfinance lender in Ibadan, Nigeria. She has a table of eight thousand loans with twenty features, and a logistic regression baseline. Does a small network do better? In the demo, a synthetic table stands in for her data.

She creates the synthetic data, splits it, and fits the scaler on the training part only, as in the scikit-learn course. Then she fits the logistic regression baseline and prints its validation score.

Next, she wraps the arrays in tensor datasets, with float features and long integer labels. The training loader uses batches of sixty-four and shuffles. The validation loader uses bigger batches and does not shuffle.

The model is small. Twenty inputs, sixty-four hidden units with ReLU, and two outputs. She moves it to the device, and chooses the Adam optimiser and cross-entropy loss.

Now the loop, for ten epochs. Train mode, then for each batch, the five lines. After that, eval mode and no grad, and she counts correct predictions on the validation set. Each epoch prints its validation accuracy.

She compares both scores on the same validation split. On data like this, you should see something like a network that is only slightly better, or about the same. Folasade records that honestly. The network costs more, so it must earn its place.

A common mistake is forgetting eval mode and no grad during validation, or forgetting to switch back to train mode. With dropout, scores look noisy and too low. Or the model trains with dropout switched off. Put train mode at the top of the training part, and eval mode with no grad around validation, every epoch. And never shuffle or augment the validation data in a way that changes it.

Let's recap. First, a dataset returns single examples, and a data loader turns them into shuffled mini-batches. A step is one batch, and an epoch is one full pass. Second, the core loop is always zero grad, forward, loss, backward, step. Third, use train mode for training, eval mode with no grad for validation, and compare against a classical baseline on the same split.

Now it is your turn. In the exercise below this video, you will write a full training and validation loop for a small tabular classifier, and compare it with a logistic regression on the same split. It takes about thirty-five minutes. In the next lesson, we move to images, with image data and transforms. See you there.
```
