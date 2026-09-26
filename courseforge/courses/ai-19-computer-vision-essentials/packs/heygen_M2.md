# HeyGen Batch Pack: AI-19 M2 (Image Classification with Pre-Trained Models)

Course: Computer Vision Essentials. Make one HeyGen video per lesson below, using these settings for every video.

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

## L05 How CNNs Learn Visual Features

- **Filename:** `ai-19-computer-vision-essentials_M2_L05_presenter.mp4`
- **Expected length:** about 5.0 minutes (700 words). The quality gate accepts ±10%.

```text
In lesson three, you chose the blur size and the edge thresholds yourself. But who could write the rules that separate a healthy leaf from a leaf with early rust, in every light and at every angle? A convolutional neural network does not need those rules.

Welcome to week two. This week, we move from hand-made processing to models that learn. And it all starts with one small idea, the filter.

A filter, also called a kernel, is a small grid of numbers, for example three by three. Convolution slides the filter across the image. At each position, it multiplies the filter values by the pixels underneath and adds the results. The output is a new image, called a feature map. It is bright wherever the image matches the filter's pattern.

The numbers decide what the filter detects. Negative values on the left and positive values on the right respond to vertical edges, where dark changes to light. Equal values average the neighbours, which is a blur. The Gaussian blur and Canny functions from lesson three are built from filters like these.

A convolutional neural network, or CNN, stacks many layers of filters. Early layers find edges, colour changes and small textures. Middle layers combine them into corners, circles and stripes. Later layers combine shapes into object parts, like a wheel or the veins of a leaf. A final layer turns all this into a score for each class.

Here is the most important idea. Nobody designs these filters by hand. They start as random numbers, and training adjusts them until the predictions match the labels. If rust spots help separate the classes, some filters become rust spot detectors. This is why a CNN trained on many general photos already has useful early filters, which you will reuse in lesson seven.

Think of a set of stencils, each cut with a small pattern, like a line, a curve or a dot. You slide each stencil across a picture, and it lights up where the picture matches. A CNN starts with blank stencils and cuts its own patterns by studying thousands of labelled pictures.

Let's see filters at work. Leila Haddad inspects printed fabric at a textile workshop in Tripoli, Lebanon. Before training any model, she wants to see what simple filters detect on a fabric photo.

In Colab, she uploads the photo in greyscale and defines three small filters, one for vertical edges, one for blur and one for sharpening. A short loop applies each filter and saves the result.

She shows the original and the three outputs in a two by two grid. The edge map is bright along vertical threads and stripes, and dark on flat areas. The blur softens the weave. And the sharpen filter makes a small defect, like a pulled thread, stand out.

Now she turns the edge filter on its side, by transposing it. Run it again, and the vertical lines fade, while the horizontal threads light up. Same numbers, new direction, new feature.

Finally, she shows the first-layer filters of a pre-trained CNN. Some look like edge detectors at different angles, similar to her hand-made ones. Others are colour blobs. Nobody drew them. They were learned from data.

A common mistake is to believe that each filter detects one named thing, like a wheel filter. Deeper filters usually respond to mixtures of patterns with no simple name. And a CNN learns whatever separates the labels, including shortcuts, like a background colour found in only one class.

Let's recap. First, a filter is a small grid of numbers, and convolution slides it over the image to make a feature map. Second, CNNs stack layers of filters, from edges to shapes to object parts, with a classification layer at the end. Third, those filters are learned from labelled data, which is why pre-trained filters can be reused.

Now it is your turn. In the exercise below this video, you will apply edge, blur and sharpen filters to your own photo, then compare them with the filters a real CNN has learned. It takes about thirty minutes. In the next lesson, we use a complete pre-trained model. Classifying Images with Hugging Face Models. See you there.
```

## L06 Classifying Images with Hugging Face Models

- **Filename:** `ai-19-computer-vision-essentials_M2_L06_presenter.mp4`
- **Expected length:** about 5.0 minutes (692 words). The quality gate accepts ±10%.

```text
Training a strong image classifier from zero can take large datasets and many hours of GPU time. Using one that someone else has trained takes about four lines of code. The real skill is knowing what the model was trained on, and when it will be wrong.

In the last lesson, we saw how CNNs learn their own filters. Today, we use a model that has already done all that learning, and we ask a simple question. Can we trust its answers?

The Hugging Face Hub is a public website with many thousands of pre-trained models and datasets. The transformers library downloads a model from the Hub and runs it. The quickest route is a pipeline. It handles the preprocessing, like resizing and colour order, then the model, then turns raw scores into labels.

The code is short. You create a pipeline for image classification with a model name from the Hub, then pass it a photo and ask for the top three results. The first run downloads the model. Later runs use the saved copy.

Each result has a label and a score. The scores add up to one across all the classes the model knows. So a score of zero point nine does not mean a ninety percent chance of being right in the real world. It means the model strongly prefers this label over its other labels.

Before you trust a model, read its model card, the page that describes it on the Hub. Check three things. What data it was trained on. Which labels it can output, because it has no none of these option. And what the licence allows. Also, never send photos of people or private documents to online demo widgets.

Think of a pre-trained model as an expert visitor who has studied a huge encyclopaedia of photos. They name familiar things quickly. But show them something that was never in the encyclopaedia, and they still give the nearest name they know, in the same confident voice.

Tomasz Nowak runs an online marketplace for second-hand furniture in Gdańsk, Poland. He wants to suggest a category for each photo that sellers upload. He tests a general classifier on ten sample photos, with no people in them.

He opens a new Colab notebook, uploads the photos and runs the pipeline on the first one. You'll see something like this. Rocking chair at zero point seven one, folding chair at zero point one two, and park bench at zero point zero four.

Next, a short loop runs all ten photos and collects the results in a table, with the file name and the top three labels. Most chairs, tables and wardrobes get sensible labels.

He opens the model card in a new tab and scrolls to the training data and the label list. This is where he learns what the model can and cannot say.

Then he shows the two photos with the lowest top score. In his test, a sofa bed was labelled studio couch, which is close, but not one of his categories. And a shelf photographed from above was labelled crossword puzzle, probably because its grid looks like a familiar pattern.

His decision? The general model is useful for a first suggestion, but his own categories will need fine-tuning. The common mistake is to treat the top label as the answer. A pipeline always returns labels. Set a minimum score, send low scores to a person, and never compare scores between different models.

Let's recap. First, a Hugging Face pipeline loads a pre-trained model and handles preprocessing, so you can classify images in a few lines. Second, the model card tells you the training data, the label list and the licence, so read it first. Third, a score shows preference, not a guarantee, so use a minimum score and review low-score cases.

Now it is your turn. In the exercise below this video, you will classify ten of your own photos, record the top three labels, and explain two mistakes. It takes about twenty-five minutes. In the next lesson, we teach a model your own categories. Transfer Learning: Fine-Tuning on Your Own Images. See you there.
```

## L07 Transfer Learning: Fine-Tuning on Your Own Images

- **Filename:** `ai-19-computer-vision-essentials_M2_L07_presenter.mp4`
- **Expected length:** about 5.0 minutes (686 words). The quality gate accepts ±10%.

```text
In the last lesson, the general model did not know your categories. Training a new model from zero needs a very large labelled dataset. With transfer learning, around a thousand labelled images and a short Colab session can be enough to teach a model a new task.

Tomasz, in Gdańsk, needed his own furniture categories, and the general model could not give them. Today, we fix that kind of problem. We take a model that already sees well, and teach it a new job.

Remember from lesson five that image models learn general features in their early and middle layers. Edges, textures, shapes and parts. Only the last layer, the classification head, is specific to the original labels.

Transfer learning keeps the pre-trained layers, called the backbone, and replaces the head with a new one that has your classes. This works with little data, because the backbone already knows what an edge or a leaf vein looks like. Your data only teaches the head which combination of features means rust, or healthy.

There are two common levels. With feature extraction, you freeze the backbone and train only the new head. It is fast and needs little data. With full fine-tuning, you also update the backbone, with a small learning rate. It can fit your data better, but needs more data and time. Start with feature extraction.

Keep your train, validation and test splits separate, and check the test split only once, at the end. And remember that free Colab GPUs are useful here, but they are not guaranteed, and sessions are limited. So save your work when training ends.

Think of it like hiring an experienced photographer to sort plant photos. They already understand light, shapes and colours. You only show them a few hundred examples of each disease. A beginner would need years. The photographer needs an afternoon.

Let's try it. Grace Namukasa works for an agricultural advice service in Mbale, Uganda. She wants a model that classifies bean leaf photos as healthy, or as one of two diseases. She uses a public bean leaf photo dataset.

First, in Colab, she opens the runtime settings and chooses a GPU, if one is available. Training is much faster on a GPU. If none is free today, the same code still runs on the processor, only more slowly.

Then she walks through the cell. It loads the dataset and the class names, loads a pre-trained vision model with a new head for three classes, and prepares each image the way the model expects. Here is the key line. A short loop freezes every backbone parameter, so only the new head will learn.

She runs it. Before training, the new head is untrained, so the test accuracy is close to guessing, about one in three. You'll see something like zero point three four. Then the training starts, and the loss goes down, epoch by epoch.

After three epochs, the test accuracy is a clearly higher number. Your numbers will differ, and they are not a benchmark. Finally, she saves the model, because she will measure it properly in the next lesson.

Watch for two common mistakes. Reporting accuracy on the training images only shows that the model remembers them, so report the test split. And unfreezing the whole backbone with a high learning rate on a small dataset can destroy the pre-trained features. When you unfreeze, use a small learning rate.

Let's recap. First, transfer learning reuses a pre-trained backbone and trains a new head for your classes, so it needs much less data and time. Second, start by freezing the backbone and training only the head, and unfreeze later only if you have enough data. Third, keep your splits separate, and report results on the test split.

Now it is your turn. In the exercise below this video, you will fine-tune a small pre-trained model on a public dataset of three to five classes, and compare its test accuracy before and after. Save your best model, because you will need it next. It takes about forty minutes. In the next lesson, Measuring Classification Quality. See you there.
```

## L08 Measuring Classification Quality

- **Filename:** `ai-19-computer-vision-essentials_M2_L08_presenter.mp4`
- **Expected length:** about 4.9 minutes (685 words). The quality gate accepts ±10%.

```text
A model reports eighty-six percent accuracy. That sounds good, until you learn that it misses most of the glass bottles it was built to find. One number can hide the most important failure. Today, you learn to see what that number hides.

In the last lesson, you fine-tuned a model and saw one accuracy number. Accuracy is the share of all predictions that are correct. It is a useful first number, but it treats every image the same.

When one class is much larger than the others, we call the data unbalanced. Then a model can reach high accuracy by doing well on the large class and badly on the small ones.

A confusion matrix shows every combination of true class and predicted class. The rows are the true classes, and the columns are the predictions. The diagonal holds the correct answers. Every cell off the diagonal is a specific kind of mistake, like glass predicted as plastic.

From it, you get two numbers per class. Precision asks, of all the images the model called this class, how many really were? Low precision means false alarms. Recall asks, of all the images that really were this class, how many did the model find? Low recall means missed cases.

Which matters more depends on the cost of each mistake. If a missed diseased leaf can spread to a whole field, focus on recall. If a false alarm stops a production line, focus on precision. The F1 score combines both, and the macro average gives every class the same weight.

Think of a school's overall exam pass rate. A school with ninety percent passes may still fail almost every student in one small class. The confusion matrix is the report for each class, and looking at the wrong images is like talking to the students who failed.

Sipho Dlamini builds a recycling sorter for a waste company in Durban, South Africa. His model classifies items on a belt as plastic, glass or metal. His test set has eighty plastic, fifteen glass and five metal items, just like the real belt.

In Colab, he prints the confusion matrix and the classification report. Accuracy is zero point eight six. But look at recall. For glass and metal, it is only zero point four zero.

He plots the matrix, and the reason is clear. Nine glass items and three metal items were predicted as plastic. The model has learned to say plastic when it is unsure, because plastic dominates the training data.

Numbers tell you which classes fail. To learn why, you look at the images. He filters the wrong predictions and shows eight of them in a grid, with the true and the predicted label on each.

Then he groups the wrong images by likely cause and counts each group. Of the nine wrong glass images, seven show clear bottles under strong top lighting, where glass looks shiny, like plastic. So he plans two fixes. More glass images under the belt's real lighting, and class weights, so mistakes on small classes cost more.

A common mistake is to balance the test set by removing images from the large class. The test set should reflect the real data, or your numbers promise results you will not get. Keep a realistic test set, and report precision and recall for each class, plus the macro average. If the small classes matter, balance the training data, or use class weights.

Let's recap. First, accuracy can hide poor results on small classes when data is unbalanced, so always check per-class results. Second, the confusion matrix shows which classes are mixed up, precision counts false alarms, and recall counts missed cases. Third, look at the wrong images and group them by cause, to decide what to fix first.

Now it is your turn. In the exercise below this video, you will build a confusion matrix for your fine-tuned model, calculate precision and recall, and explain its most common mistake. It takes about thirty minutes. Next week, we find where objects are, not just what they are. Object Detection: Boxes, Classes and IoU. See you there.
```
