# L06 Image Data and Transforms | Presenter Script

Course: AI-13 · Video: 5 min · Words: 628

## Hook
Flip a photo of a shirt from left to right, and it is still a shirt. Your network does not know that until you show it. Data augmentation teaches it, but in the wrong place, it makes your validation scores meaningless.

## Explain
Welcome to module two, where we work with images. A colour image is a tensor with three channels, then height and width. A greyscale image has one channel. Pixels usually arrive as whole numbers from zero to two hundred and fifty-five, and we turn them into decimals from zero to one.

The torchvision library downloads common datasets with one line. In this module, we use Fashion-MNIST. Small greyscale images, twenty-eight pixels square, of clothing items in ten classes, with a standard training and test split. As with any dataset, check its licence before you reuse it outside the course.

Transforms are functions applied to each image as it loads. You chain them together. The first converts the image to a float tensor. The next normalises it, using a mean and a standard deviation from the training set only.

Augmentations create random changes each time an image loads. Flips, crops with padding, small rotations, or colour changes. The model sees a slightly different version of each image in every epoch, which reduces overfitting.

Choose changes that keep the label true. A left-right flip is fine for clothing. An upside-down shoe is not a realistic input. And for digits, a flipped two is not a two.

Think of a teacher who writes the same maths problem with different numbers each time. The student learns the method, not the page. But the final exam must be a fixed paper. If every student got random questions, the marks would not be comparable.

That is the rule. Validation and test images get the same fixed steps, such as conversion, normalisation and resizing, but nothing random.

## Demonstrate
Mei Lin is an engineer at an online clothing retailer in Penang, Malaysia. She wants to prototype a product-type classifier with Fashion-MNIST before using her company's own photos.

First, she downloads the training set with no transforms, turns the pixels into decimals, and computes the mean and standard deviation. You should see something like zero point two eight six and zero point three five three.

Next, two pipelines. The training transform adds a random flip and a random crop with padding, then converts and normalises. The evaluation transform only converts and normalises.

She passes the right pipeline to each split. The training set gets the training transform. The test set gets the evaluation transform.

Finally, she loads the same image sixteen times and shows them in a grid. Each copy is shifted a little, and some are flipped. The grid is also a useful check. If the images look destroyed, the augmentation is too strong.

The most common mistake is giving the augmented training transform to the validation or test set, or computing normalisation statistics on all the data. Both make your evaluation less honest. And if you split with random split, both parts share one transform, so create two dataset objects instead.

## Recap
Let's recap. First, images are tensors of channels, height and width. Convert them to floats, and normalise with the training set's mean and standard deviation. Second, augmentation creates random variations of training images to reduce overfitting. Choose changes that keep the label true. Third, augment training data only. Validation and test data get the same fixed steps, and nothing random.

## CTA
Now it is your turn. In the exercise below this video, you will load Fashion-MNIST, compute the mean and standard deviation, and show a grid of augmented samples. It takes about twenty-five minutes. In the next lesson, we build convolutional neural networks. See you there.

## Thumbnail
Headline: Augment Training Data Only
Image: Navy background, a grid of the same small shirt image flipped and shifted in different ways, one fixed image to the side labelled exam, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Fashion-MNIST licence and source must be confirmed before the dataset is named and used in the recording. The voiceover names the dataset but makes no licence claim; it only tells learners to check the licence before reuse.
- [VERSION] Check the torchvision transforms API in Colab at recording time: classic transforms compared with transforms.v2. The demo uses classic transforms, as in content.md.
- Mean and standard deviation are said as 'something like 0.286 and 0.353' (content.md: values from the team's CPU test run). Show the real printed values.
- Mei Lin and the Penang clothing retailer are hypothetical; stock footage must not show a real store name or logo.
