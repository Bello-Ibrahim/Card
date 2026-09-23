# L07 Convolutional Neural Networks | Presenter Script

Course: AI-13 · Video: 5 min · Words: 679

## Hook
A fully connected layer that reads a small colour photo and outputs one thousand features needs about one hundred and fifty million weights. A convolutional layer that finds sixty-four patterns in the same photo needs under two thousand. How?

## Explain
A fully connected network flattens the image into one long row. It ignores the fact that nearby pixels belong together. And a pattern it learns in the top-left corner must be learned again for every other position.

A convolution fixes both problems. A filter is a small grid of weights, for example three by three. It slides across the image, and at each position it computes a weighted sum of the pixels under it. The result is a feature map that is high wherever the pattern appears, for example a vertical edge.

Two ideas make this efficient. Local connections, because each output looks only at a small patch. And weight sharing, because the same filter is used everywhere, so a pattern learned once is found anywhere.

Pooling keeps the largest value in each two by two block, which halves the height and width. This reduces computation, and makes the network less sensitive to small shifts. A small CNN repeats convolution, ReLU and pooling a few times. The image gets smaller while the channels grow. Early layers learn edges, and later layers learn shapes.

Picture a small window that you move across a large map, looking for one symbol, such as a bridge. You use the same window everywhere, so you learn once what a bridge looks like. Then a second person scans your list of bridges, rivers and roads, and finds bigger patterns, like a town.

## Demonstrate
Rafael is an engineer at an e-commerce company in Recife, Brazil. He compares a CNN with the fully connected network from lesson three, on Fashion-MNIST, using the transforms from the last lesson.

In Colab, he defines the CNN. Two blocks of convolution, ReLU and pooling, with thirty-two and then sixty-four filters. Then flatten, and one linear layer to ten classes. He also defines the fully connected network for comparison.

He counts the parameters. Fifty thousand, one hundred and eighty-six for the CNN, and two hundred and thirty-five thousand, one hundred and forty-six for the other network. The CNN has about one fifth of the parameters.

Next, the most useful debugging tool in this lesson. He passes a dummy batch through the CNN, one layer at a time, and prints the shape after each. He can see the image shrink and the channels grow, and the exact size the linear layer needs.

He trains both models for five epochs with the loop from lesson five, the same optimiser and the same learning rate. You should see something like the CNN reaching a higher validation accuracy. Rafael reports his own measured numbers rather than assuming a result. If you are on a CPU, train on a subset of ten thousand images, so each epoch finishes in a few minutes.

A common mistake is calculating the linear layer's input size by hand, and getting it wrong after changing padding or pooling. The error message shows the real size. Print the shapes, or use a lazy linear layer, which works out its size on the first pass. And greyscale images still need a channel dimension of one.

## Recap
Let's recap. First, a convolution slides a small shared filter across the image, so it finds a pattern anywhere with very few weights. Second, stacks of convolution, ReLU and pooling shrink the image and grow the channels, moving from edges to shapes to objects. Third, print shapes with a dummy batch to size the final layer, and compare models on parameters as well as accuracy.

## CTA
Now it is your turn. In the exercise below this video, you will train a small CNN on Fashion-MNIST and compare its accuracy and parameter count with a fully connected network. It takes about forty minutes. In the next lesson, we learn to read learning curves, so you know what to change next. See you there.

## Thumbnail
Headline: Small Filters, Big Results
Image: Navy background, a small teal 3×3 grid sliding across a greyscale clothing image and lighting up edges, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Fashion-MNIST licence and source (carried from L06): confirm before the dataset is used in the recording.
- Parameter counts on screen must match content.md: 50186 for the CNN and 235146 for the fully connected network.
- Accuracy: content.md gives no numbers. The voiceover says 'you should see something like the CNN reaching a higher validation accuracy'. Show the real measured values; do not add numbers in captions.
- Hook figures (about 150 million weights for a 224×224×3 → 1,000 fully connected layer; under 2,000 for 64 filters of 3×3×3 plus biases) are from content.md.
- On CPU, train on a 10,000-image subset so each epoch takes a few minutes; speed up the training segment in the edit.
- Rafael and the Recife e-commerce company are hypothetical; stock footage must not show a real company name or logo.
