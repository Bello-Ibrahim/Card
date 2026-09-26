# HeyGen Batch Pack: AI-13 M2 (Neural Networks for Images)

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

## L06 Image Data and Transforms

- **Filename:** `ai-13-deep-learning-and-neural-networks_M2_L06_presenter.mp4`
- **Expected length:** about 4.8 minutes (663 words). The quality gate accepts ±10%.

```text
Flip a photo of a shirt from left to right, and it is still a shirt. Your network does not know that until you show it. Data augmentation teaches it, but in the wrong place, it makes your validation scores meaningless.

Welcome to module two, where we work with images. A colour image is a tensor with three channels, then height and width. A greyscale image has one channel. A batch adds one more dimension at the front, as you saw in lesson two. Pixels usually arrive as whole numbers from zero to two hundred and fifty-five, and we turn them into decimals from zero to one.

The torchvision library downloads common datasets with one line. In this module, we use Fashion-MNIST. Small greyscale images, twenty-eight pixels square, of clothing items in ten classes, with a standard training and test split. As with any dataset, check its licence before you reuse it outside the course.

Transforms are functions applied to each image as it loads. You chain them together. The first converts the image to a float tensor. The next normalises it, using a mean and a standard deviation from the training set only. This centres the inputs near zero, which helps optimisation.

Augmentations create random changes each time an image loads. Flips, crops with padding, small rotations, or colour changes. The model sees a slightly different version of each image in every epoch, which reduces overfitting.

Choose changes that keep the label true. A left-right flip is fine for clothing. An upside-down shoe is not a realistic input. And for digits, a flipped two is not a two.

Think of a teacher who writes the same maths problem with different numbers each time. The student learns the method, not the page. But the final exam must be a fixed paper. If every student got random questions, the marks would not be comparable.

That is the rule. Validation and test images get the same fixed steps, such as conversion, normalisation and resizing, but nothing random. Otherwise your validation score changes from run to run, and no longer measures how the model does on real images.

Mei Lin is an engineer at an online clothing retailer in Penang, Malaysia. She wants to prototype a product-type classifier with Fashion-MNIST before using her company's own photos.

First, she downloads the training set with no transforms, turns the pixels into decimals, and computes the mean and standard deviation. You should see something like zero point two eight six and zero point three five three.

Next, two pipelines. The training transform adds a random flip and a random crop with padding, then converts and normalises. The evaluation transform only converts and normalises.

She passes the right pipeline to each split. The training set gets the training transform. The test set gets the evaluation transform.

Finally, she loads the same image sixteen times and shows them in a grid. Each copy is shifted a little, and some are flipped. The grid is also a useful check. If the images look destroyed, the augmentation is too strong.

The most common mistake is giving the augmented training transform to the validation or test set, or computing normalisation statistics on all the data. Both make your evaluation less honest. And if you split with random split, both parts share one transform, so create two dataset objects instead.

Let's recap. First, images are tensors of channels, height and width. Convert them to floats, and normalise with the training set's mean and standard deviation. Second, augmentation creates random variations of training images to reduce overfitting. Choose changes that keep the label true. Third, augment training data only. Validation and test data get the same fixed steps, and nothing random.

Now it is your turn. In the exercise below this video, you will load Fashion-MNIST, compute the mean and standard deviation, and show a grid of augmented samples. It takes about twenty-five minutes. In the next lesson, we build convolutional neural networks. See you there.
```

## L07 Convolutional Neural Networks

- **Filename:** `ai-13-deep-learning-and-neural-networks_M2_L07_presenter.mp4`
- **Expected length:** about 4.8 minutes (669 words). The quality gate accepts ±10%.

```text
A fully connected layer that reads a small colour photo and outputs one thousand features needs about one hundred and fifty million weights. A convolutional layer that finds sixty-four patterns in the same photo needs under two thousand. How?

A fully connected network flattens the image into one long row. It ignores the fact that nearby pixels belong together. And a pattern it learns in the top-left corner must be learned again for every other position.

A convolution fixes both problems. A filter is a small grid of weights, for example three by three. It slides across the image, and at each position it computes a weighted sum of the pixels under it. The result is a feature map that is high wherever the pattern appears, for example a vertical edge.

Two ideas make this efficient. Local connections, because each output looks only at a small patch. And weight sharing, because the same filter is used everywhere, so a pattern learned once is found anywhere.

Pooling keeps the largest value in each two by two block, which halves the height and width. This reduces computation, and makes the network less sensitive to small shifts. A small CNN repeats convolution, ReLU and pooling a few times. The image gets smaller while the channels grow. Early layers learn edges, and later layers learn shapes.

Picture a small window that you move across a large map, looking for one symbol, such as a bridge. You use the same window everywhere, so you learn once what a bridge looks like. Then a second person scans your list of bridges, rivers and roads, and finds bigger patterns, like a town.

Rafael is an engineer at an e-commerce company in Recife, Brazil. He compares a CNN with the fully connected network from lesson three, on Fashion-MNIST, using the transforms from the last lesson.

In Colab, he defines the CNN. Two blocks of convolution, ReLU and pooling, with thirty-two and then sixty-four filters. Then flatten, and one linear layer to ten classes. He also defines the fully connected network for comparison.

He counts the parameters. Fifty thousand, one hundred and eighty-six for the CNN, and two hundred and thirty-five thousand, one hundred and forty-six for the other network. The CNN has about one fifth of the parameters.

Next, the most useful debugging tool in this lesson. He passes a dummy batch through the CNN, one layer at a time, and prints the shape after each. He can see the image shrink and the channels grow, and the exact size the linear layer needs.

He trains both models for five epochs with the loop from lesson five, the same optimiser and the same learning rate. You should see something like the CNN reaching a higher validation accuracy. Rafael reports his own measured numbers rather than assuming a result. If you are on a CPU, train on a subset of ten thousand images, so each epoch finishes in a few minutes.

A common mistake is calculating the linear layer's input size by hand, and getting it wrong after changing padding or pooling. The error message shows the real size. Print the shapes, or use a lazy linear layer, which works out its size on the first pass. And greyscale images still need a channel dimension of one.

Let's recap. First, a convolution slides a small shared filter across the image, so it finds a pattern anywhere with very few weights. Second, stacks of convolution, ReLU and pooling shrink the image and grow the channels, moving from edges to shapes to objects. Third, print shapes with a dummy batch to size the final layer, and compare models on parameters as well as accuracy.

Now it is your turn. In the exercise below this video, you will train a small CNN on Fashion-MNIST and compare its accuracy and parameter count with a fully connected network. It takes about forty minutes. In the next lesson, we learn to read learning curves, so you know what to change next. See you there.
```

## L08 Reading Learning Curves

- **Filename:** `ai-13-deep-learning-and-neural-networks_M2_L08_presenter.mp4`
- **Expected length:** about 4.8 minutes (669 words). The quality gate accepts ±10%.

```text
Your model finished training, and you do not like the score. You could change ten settings at random. Or you could look at one chart for thirty seconds, and know which setting to change first. That chart is the learning curve.

In the scikit-learn course, your learning curves had training-set size on the x-axis. Here, the x-axis is epochs. A learning curve plots the training loss and the validation loss after every epoch, on the same axes. Plot loss before accuracy, because loss changes smoothly and shows problems earlier.

Four patterns cover most cases. In a healthy run, both losses fall and then flatten, with a small gap. More epochs will not help much. A larger model or better data might.

In overfitting, training loss keeps falling, but validation loss reaches a low point and then rises. The curves separate, because the model is memorising the training set. Fixes include more data or augmentation, regularisation, a smaller model, or stopping earlier.

In underfitting, both losses stay high and close together. The model cannot fit even the training data. Try a larger model, more epochs, a higher learning rate, or better inputs.

When the learning rate is too high, the loss jumps up and down, grows, or becomes not a number. Lower the learning rate, often by three to ten times.

Two more signals. If the training loss is flat from the start, check the loop itself. Is zero grad there? Does the optimiser have the right parameters? Is the model frozen? And if validation loss is lower than training loss, that is often normal when dropout or strong augmentation runs during training only.

Learning curves are like a patient's temperature chart. One reading tells you little. The shape over several days tells the doctor whether the treatment is working, whether the patient is getting worse, or whether the thermometer is broken.

Svetlana is an engineer at an agricultural insurer in Almaty, Kazakhstan. She trained the CNN from lesson seven on ten thousand Fashion-MNIST images for twenty epochs, and saved the losses from each epoch in two lists.

In Colab, she writes a small plotting function. It draws both losses with a legend, finds the epoch with the lowest validation loss, and marks it with a dashed grey line.

She calls it with her saved history. The training loss falls steadily to a low value. The validation loss falls until about epoch six, then rises slowly, while validation accuracy stays almost flat.

Her diagnosis is overfitting after epoch six, made more likely by the small training set. The model at epoch six is better than the final one, even though its training loss is higher.

She makes one change first. She adds augmentation to the training transform, keeps the old curve, trains again, and compares. Note what she does not do. She does not touch the learning rate, because nothing in the curves pointed to it.

A common mistake is looking only at the final accuracy, or only at training loss. The final epoch is often not the best one, and a falling training loss says nothing about new data. Another mistake is reading one noisy epoch as a trend. Look at the direction over several epochs.

And never draw learning curves on the test set. Every decision you make from it uses up its value as a fair check.

Let's recap. First, plot training and validation loss per epoch on one chart. Second, separating curves mean overfitting, two high curves mean underfitting, and jumping or growing loss usually means the learning rate is too high. Third, diagnose first, then change one thing at a time after each diagnosis, and keep the old curve for comparison.

Now it is your turn. In the exercise below this video, you will diagnose four learning curves, labelled A to D, then plot your own CNN's curves and write a one-paragraph diagnosis. It takes about thirty minutes. In the next lesson, we fight overfitting with dropout, weight decay and early stopping. See you there.
```

## L09 Regularisation: Dropout, Weight Decay and Early Stopping

- **Filename:** `ai-13-deep-learning-and-neural-networks_M2_L09_presenter.mp4`
- **Expected length:** about 4.9 minutes (676 words). The quality gate accepts ±10%.

```text
In the last lesson, the validation loss started to rise while the training loss kept falling. The model was learning the training set too well. Today, you add three tools that make it learn the pattern, not the details.

Regularisation is any change that helps a model do better on new data, usually at some cost to its training score. In the scikit-learn course, you met penalties for linear models. Deep networks use the same idea, plus a few of their own.

Dropout randomly switches off a fraction of the units in each training step, and scales up the rest. The network cannot rely on any single unit, so it learns features that are more spread out and more robust. It is active only in train mode. In eval mode, it does nothing. Typical rates are between ten and fifty percent.

Weight decay shrinks every weight a little at each step. This keeps the weights small and the function smoother. It is the deep-learning version of an L2 penalty. With Adam, use the AdamW optimiser, which applies the decay separately.

Early stopping watches the validation loss after every epoch. It saves a copy of the weights whenever the loss improves, and stops when there has been no improvement for a set number of epochs, called the patience. Then you reload the best copy. It also saves GPU time. And remember, augmentation is a regulariser too, often the strongest one for images.

Think of a student who practises with one set of past exam questions. They can memorise the answers and still fail a new exam. A student who practises with different questions, sometimes with parts hidden, must learn the method.

Dropout hides parts of the question. Weight decay stops the student from building very complicated rules. And early stopping is the teacher saying, stop now, you are starting to memorise.

Hamid is an engineer at an argan-oil cooperative in Agadir, Morocco. His quality-check CNN overfits after a few epochs. Let's add all three tools in Colab.

First, he adds a dropout layer with a rate of zero point three, just before the final linear layer. Then he switches the optimiser to AdamW, with a weight decay of zero point zero one.

Next, the early-stopping block around his loop from lesson five, with a patience of three. After each epoch, if the validation loss improves, he saves a deep copy of the weights. If not, he counts a bad epoch, and after three in a row, he stops.

At the end, he loads the best weights back into the model. Then he runs two experiments with the same data, seed and learning rate. The original model, and the regularised one.

He plots both validation curves on one chart. You should see something like this. The regularised model's validation loss stays lower for longer, and the gap between training and validation gets smaller. He compares the best scores, not the final ones, and records both runs in a small table.

A common mistake is saving the best model without a real copy. That only stores links to the live weights, which keep changing. At the end, best is simply the last model. Use a deep copy, or save to a file. And add regularisers one at a time, or you cannot tell which one helped.

Let's recap. First, dropout switches off random units during training only, and weight decay keeps weights small. Both reduce overfitting, at some cost to the training fit. Second, early stopping keeps the checkpoint with the best validation loss, and stops after a set number of epochs without improvement. Third, judge each regulariser by comparing validation curves across runs that change one thing at a time.

Now it is your turn. In the exercise below this video, you will add dropout and weight decay to your own CNN, use early stopping, and compare the validation curves before and after. It takes about forty minutes. In the next lesson, we save a lot of training time with transfer learning and pretrained CNNs. See you there.
```

## L10 Transfer Learning with Pretrained CNNs

- **Filename:** `ai-13-deep-learning-and-neural-networks_M2_L10_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
You have about a thousand labelled photos of bean leaves. That is far too few to train a deep CNN from scratch. But what if a network that has already seen a huge number of everyday photos only had to learn the last step?

This is transfer learning. You reuse a network trained on a large dataset, such as ImageNet, for a new task. Its early and middle layers have learned general visual features, like edges, textures and shapes, that are useful for almost any photo. Only the last layer is specific to its original one thousand classes.

The recipe has two stages. First, feature extraction. Load the pretrained model, freeze the backbone so its weights do not change, replace the final layer with a new one for your classes, and train only that new layer. It is fast, and it needs little data.

Second, fine-tuning. Unfreeze the last block or two, and train them together with the new layer, with a smaller learning rate for the pretrained part. You adjust its features gently, instead of destroying them.

Think of an experienced chef learning a new cuisine. The chef already knows how to cut, season and control heat. Feature extraction is following new recipes with old skills. Fine-tuning is carefully adjusting a few techniques as well.

Two details are easy to miss. Preprocess images exactly the way the model was trained, and in torchvision, the weights object gives you those transforms. And use the newer weights argument. Older tutorials use a different option that newer versions no longer support. Pretrained checkpoints also have their own licences, so check them before you use a model in a product.

Grace is a data scientist at an agricultural extension service in Mbale, Uganda. Farmers send her leaf photos, and she wants to classify them as healthy, angular leaf spot or bean rust. She uses a public bean-leaf dataset from the Hugging Face Hub.

In Colab, she loads ResNet eighteen with its default pretrained weights, and freezes every parameter. Then she replaces the final layer with a new one that has three outputs. Only this new head can learn. Everything else keeps what it learned before.

She counts the trainable parameters. Only one thousand five hundred and thirty-nine, which is five hundred and twelve features times three classes, plus three biases. So each epoch is fast, even on a CPU.

Next, she loads the dataset and applies the pretrained model's own transforms to every image. A small collate function stacks the images and labels into batches of thirty-two.

Stage one trains only the head for a few epochs. For stage two, she unfreezes the last block, and builds a new optimiser with two learning rates. A small one for the pretrained block, and a larger one for the head.

Grace compares three runs on the validation split. Her CNN trained from scratch, the frozen ResNet, and the fine-tuned ResNet. You should see something like both pretrained runs doing clearly better on this small dataset. She reports her own measured numbers.

A common mistake is changing what is trainable, but forgetting to rebuild the optimiser. Build the optimiser after you set which layers learn, and print the trainable count. Also, never use your own normalisation values, such as the Fashion-MNIST ones, with a pretrained model. Its features would then receive inputs in a range they never saw during pretraining.

Let's recap. First, transfer learning reuses a pretrained backbone's general features. Freeze it, replace the final layer, and train the new head first. Second, fine-tune a few top layers afterwards with a smaller learning rate, and rebuild the optimiser whenever you change what is trainable. Third, preprocess with the pretrained weights' own transforms, and check the licences of both the checkpoint and the dataset.

Now it is your turn. In the exercise below this video, you will fine-tune a pretrained ResNet on the bean-leaf dataset, and compare it with your CNN trained from scratch. It takes about forty-five minutes. In the next module, we move to text, starting with tokens and embeddings. See you there.
```
