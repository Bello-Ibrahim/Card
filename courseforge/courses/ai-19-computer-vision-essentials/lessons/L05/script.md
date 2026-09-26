# L05 How CNNs Learn Visual Features | Presenter Script

Course: AI-19 · Video: 5 min · Words: 706

## Hook
In lesson three, you chose the blur size and the edge thresholds yourself. But who could write the rules that separate a healthy leaf from a leaf with early rust, in every light and at every angle? A convolutional neural network does not need those rules.

## Explain
Welcome to week two. This week, we move from hand-made processing to models that learn. And it all starts with one small idea, the filter.

A filter, also called a kernel, is a small grid of numbers, for example three by three. Convolution slides the filter across the image. At each position, it multiplies the filter values by the pixels underneath and adds the results. The output is a new image, called a feature map. It is bright wherever the image matches the filter's pattern.

The numbers decide what the filter detects. Negative values on the left and positive values on the right respond to vertical edges, where dark changes to light. Equal values average the neighbours, which is a blur. The Gaussian blur and Canny functions from lesson three are built from filters like these.

A convolutional neural network, or CNN, stacks many layers of filters. Early layers find edges, colour changes and small textures. Middle layers combine them into corners, circles and stripes. Later layers combine shapes into object parts, like a wheel or the veins of a leaf. A final layer turns all this into a score for each class.

Here is the most important idea. Nobody designs these filters by hand. They start as random numbers, and training adjusts them until the predictions match the labels. If rust spots help separate the classes, some filters become rust spot detectors. This is why a CNN trained on many general photos already has useful early filters, which you will reuse in lesson seven.

Think of a set of stencils, each cut with a small pattern, like a line, a curve or a dot. You slide each stencil across a picture, and it lights up where the picture matches. A CNN starts with blank stencils and cuts its own patterns by studying thousands of labelled pictures.

## Demonstrate
Let's see filters at work. Leila Haddad inspects printed fabric at a textile workshop in Tripoli, Lebanon. Before training any model, she wants to see what simple filters detect on a fabric photo.

In Colab, she uploads the photo in greyscale and defines three small filters, one for vertical edges, one for blur and one for sharpening. A short loop applies each filter and saves the result.

She shows the original and the three outputs in a two by two grid. The edge map is bright along vertical threads and stripes, and dark on flat areas. The blur softens the weave. And the sharpen filter makes a small defect, like a pulled thread, stand out.

Now she turns the edge filter on its side, by transposing it. Run it again, and the vertical lines fade, while the horizontal threads light up. Same numbers, new direction, new feature.

Finally, she shows the first-layer filters of a pre-trained CNN. Some look like edge detectors at different angles, similar to her hand-made ones. Others are colour blobs. Nobody drew them. They were learned from data.

A common mistake is to believe that each filter detects one named thing, like a wheel filter. Deeper filters usually respond to mixtures of patterns with no simple name. And a CNN learns whatever separates the labels, including shortcuts, like a background colour found in only one class.

## Recap
Let's recap. First, a filter is a small grid of numbers, and convolution slides it over the image to make a feature map. Second, CNNs stack layers of filters, from edges to shapes to object parts, with a classification layer at the end. Third, those filters are learned from labelled data, which is why pre-trained filters can be reused.

## CTA
Now it is your turn. In the exercise below this video, you will apply edge, blur and sharpen filters to your own photo, then compare them with the filters a real CNN has learned. It takes about thirty minutes. In the next lesson, we use a complete pre-trained model. Classifying Images with Hugging Face Models. See you there.

## Thumbnail
Headline: Filters That Learn Themselves
Image: Navy background, a close-up of patterned fabric on the left and a grid of small glowing filter squares on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] torchvision model names, the weights="DEFAULT" argument, and whether PyTorch and torchvision are pre-installed in Colab must be checked at recording time. OpenCV function names (filter2D, convertScaleAbs) must be checked against the OpenCV version in Colab. The OpenCV code in content.md was tested with opencv-python-headless on a synthetic image.
- Run outputs: content.md gives no exact printed mean values for the three filters, so the voiceover does not state any numbers. Describe the images only.
- Scene with the first-layer filters: prepare the image in advance from a pre-trained CNN (for example resnet18 conv1 weights, first 16 filters, each normalised to 0-1). The voiceover says only that some look like edge detectors and some like colour blobs.
- Leila Haddad and the Tripoli textile workshop are fictional. The fabric photo must show no people, no brand labels and no logos.
- Screen recording: clean browser profile, no account names or other tabs visible.
