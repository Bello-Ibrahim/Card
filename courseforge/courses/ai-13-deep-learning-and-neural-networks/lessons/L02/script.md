# L02 Tensors: The Language of PyTorch | Presenter Script

Course: AI-13 · Video: 5 min · Words: 704

## Hook
Your first PyTorch error will probably not be about maths. It will say that two shapes cannot be multiplied. Most beginner bugs in deep learning are shape bugs. Today, you learn to read them and fix them fast.

## Explain
In the last lesson, we got a GPU ready. Now we meet the data structure that lives on it. A tensor is PyTorch's main data structure. If you know NumPy arrays, you already know most of it.

Every tensor has three properties you should check all the time. Its shape, which is the size of each dimension. Its dtype, the number type, such as float for inputs and weights, or a long integer for class labels. And its device, the CPU or the GPU.

Two tensors in one operation must have compatible shapes, and they must be on the same device. Tensors also do two things NumPy arrays cannot. They run on a GPU, and they can record operations for automatic gradients, which we use in lesson four.

In PyTorch, the first dimension is almost always the batch. Images use batch, channels, height, width. Many image libraries put the channels last instead, so you often need to reorder.

Here is a picture to keep in mind. A tensor's shape is like a stack of egg trays. One tray has rows and columns. A stack adds layers. A box of stacks adds one more dimension.

Reshaping moves the eggs into trays of a different size, but the number of eggs never changes. If the sizes do not multiply to the same total, the reshape fails. Reshape and view change the shape. Permute reorders the dimensions. Unsqueeze adds a batch dimension of size one.

Broadcasting follows the same rules as NumPy. Shapes are compared from the right, and a size of one can stretch to match. That is how you subtract one mean per colour channel from a whole batch of images.

## Demonstrate
Let's go to Colab. Tomás is an engineer at an agritech start-up in Valparaíso, Chile. He loads grape photos with an image library and wants to feed them to a network.

He starts with a batch of thirty-two photos, sixty-four pixels square, with the channels last. One permute moves the channels to position one. Now the print shows thirty-two, three, sixty-four, sixty-four, as float numbers on the CPU.

Next, he makes a mean with one value per channel, shaped three, one, one, and subtracts it. Broadcasting stretches it across the whole batch. Then he moves the batch to the GPU.

For a linear layer, he flattens each image into one long row. The minus one tells PyTorch to work out the size, which is twelve thousand two hundred and eighty-eight. He also creates class labels as whole numbers, and picks one image with a new batch dimension.

Now Tomás gets an error. Expected all tensors to be on the same device. His images are on the GPU, but the labels are still on the CPU. The fix is always the same. Move both to one device.

The most common mistake is using reshape when you need permute. Both give the same shape, but reshape only reinterprets the numbers in memory order. The pixels get mixed, and no error appears. The model just learns badly.

Use permute to reorder dimensions, and reshape only to merge or split dimensions that are already in order. And when you predict on one example, always add the batch dimension first.

## Recap
Let's recap. First, check shape, dtype and device for every tensor you create. Most bugs show up in one of the three. Second, PyTorch puts the batch first, and images use batch, channels, height, width. Use permute to reorder, and reshape only to merge or split. Third, broadcasting compares shapes from the right, and every tensor in one operation must be on the same device.

## CTA
Now it is your turn. In the exercise below this video, you will create a batch of thirty-two colour images, move it to the GPU, and fix three shape errors in a provided cell, with one line explaining each fix. It takes about twenty minutes. In the next lesson, we build neurons, layers and activations. See you there.

## Thumbnail
Headline: Most Bugs Are Shape Bugs
Image: Navy background, a stack of egg trays drawn as a 3D grid of teal dots with the shape (32, 3, 64, 64) beside it, headline in teal Inter Bold.

## Production Notes
- Review flags: none. Run every snippet once before recording and confirm the printed shape torch.Size([32, 3, 64, 64]) and the flattened size 12288.
- The device error message on screen must read: Expected all tensors to be on the same device. Trigger it on purpose by leaving labels on the CPU while x is on the GPU, then fix it with labels.to(device).
- On a CPU runtime the device prints cpu; record on a GPU runtime so cuda:0 appears.
- Tomás and the Valparaíso agritech start-up are hypothetical; stock footage must not show a real company name or logo.
