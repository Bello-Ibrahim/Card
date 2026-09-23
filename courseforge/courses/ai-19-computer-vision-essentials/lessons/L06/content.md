# L06 Classifying Images with Hugging Face Models

Course: AI-19 · Module: M2 · Objectives: O2, O3 · Video: 5 min (screen demo)

## Hook
Training a strong image classifier from zero can take large datasets and many hours of GPU time. Using one that someone else has already trained takes about four lines of code. The skill is not the four lines. The skill is knowing what the model was trained on, and when it will be wrong.

## Explanation
The **Hugging Face Hub** is a public website that hosts many thousands of pre-trained models and datasets. The `transformers` library can download a model from the Hub and run it. The quickest route is a **pipeline**: one object that handles preprocessing (resize, normalise, RGB order), the model and post-processing (turning raw scores into labels).

```python
from transformers import pipeline

clf = pipeline("image-classification",
               model="google/vit-base-patch16-224")
results = clf("photo.jpg", top_k=3)
for r in results:
    print(f"{r['label']:<30} {r['score']:.2f}")
```

The task name `"image-classification"`, the argument names and the model ID can change between library versions, so check them against the current documentation. [VERSION] The first run downloads the model weights, which can take a minute. Later runs use the cached copy.

Each result is a dictionary with a `label` and a `score`. The scores come from a **softmax**, so they add up to 1 across all classes the model knows. A score of 0.90 does not mean "90% chance of being correct in the real world". It means the model prefers this label strongly compared with its other labels.

Before you trust a model, read its **model card**: the page on the Hub that describes it. Look for four things:

1. **Training data.** Many general classifiers were trained on ImageNet-style data with about 1,000 everyday classes. [VERIFY] If your images look very different, for example microscope slides or satellite images, expect poor results.
2. **Label list.** The model can only output labels it was trained on. It has no "none of these" option unless one was included.
3. **Input expectations.** Image size and colour order are handled by the pipeline, but image style still matters.
4. **Licence and limits.** Check what use the licence allows, and read any known limitations.

Do not send photos of people or private documents to online demo widgets on model pages. In Colab, the model runs inside your session.

**Analogy:** A pre-trained model is like an expert visitor who has studied a large encyclopaedia of photos. They name familiar things quickly and confidently. But if you show them something that was never in their encyclopaedia, they still give the nearest name they know, with the same confident voice.

## Worked Example
Tomasz Nowak runs an online marketplace for second-hand furniture in Gdańsk, Poland. He wants to suggest a category for each photo that sellers upload. He tests a general classifier on 10 sample photos.

**On screen (presenter steps):**
1. Open a new Colab notebook and upload 10 furniture photos with no people in them.
2. Run the pipeline cell above with the first photo and show the top 3 labels.
3. Loop over all 10 photos and collect the results in a pandas DataFrame with the columns `file`, `label_1`, `score_1`, `label_2`, `label_3`.
4. Open the model card on the Hub in a new tab and scroll to the training data and the label list. [VERSION]
5. Display the two photos with the lowest top score next to their labels.

Example output for one photo:

```text
rocking chair                  0.71
folding chair                  0.12
park bench                     0.04
```

Tomasz sees that most chairs, tables and wardrobes get sensible labels. Two results are wrong. A modern sofa bed is labelled "studio couch", which is close but not in his category list. A wooden shelf photographed from above is labelled "crossword puzzle", probably because the grid of shelves looks like a grid pattern the model knows. He decides that the general model is useful for a first suggestion, but that his own categories will need fine-tuning, which is the topic of L07.

## Common Mistake
Many developers treat the top label as the answer and ignore the score and the label list. A pipeline always returns labels, even for an image that fits none of them. Set a minimum score for automatic decisions, send low-score images to a person, and map the model's labels to your own categories deliberately. Also, do not compare scores between different models: each model's scores have their own scale.

## Key Takeaways
1. A Hugging Face pipeline loads a pre-trained model and handles preprocessing, so you can classify images in a few lines of code.
2. The model card tells you the training data, the label list and the licence; read it before you trust the model.
3. Scores show how strongly the model prefers a label, not a guarantee; use a minimum score and review low-score cases.

## Hands-on Exercise
**Task:** Classify 10 of your own photos with a pre-trained model, record the top 3 labels and scores for each, and note 2 cases where the model was wrong and a likely reason.
**Tools:** Google Colab; the `transformers` library (install with `pip` if it is missing [VERSION]); an image classification model from the Hugging Face Hub; 10 of your own photos of objects, food, plants or places, with no people and no private documents.
**Steps:**
1. Open a new Colab notebook and upload your 10 photos.
2. Create the pipeline and run it on one photo to check that it works.
3. Loop over all photos with `top_k=3` and store the results in a DataFrame.
4. Open the model card and write down the training data and the number of labels. [VERSION]
5. Mark each result as "correct", "close" or "wrong".
6. For 2 wrong results, write a likely reason: a missing label, an unusual angle, poor lighting, a busy background or an image style unlike the training data.
**What good looks like:** A table with 10 rows showing the top 3 labels and scores, a note on the model's training data, and 2 clear explanations of errors that link the error to the image or to the label list.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Hugging Face `transformers` pipeline task name (`image-classification`), the `top_k` argument, the model ID `google/vit-base-patch16-224` and the Hub model card layout must be checked at recording time. Code was checked for syntax only; the printed labels and scores are example output.
- [VERIFY] Confirm the training data and number of labels stated on the chosen model's card before the lesson describes it.
