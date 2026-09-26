# L06 Classifying Images with Hugging Face Models | Presenter Script

Course: AI-19 · Video: 5 min · Words: 700

## Hook
Training a strong image classifier from zero can take large datasets and many hours of GPU time. Using one that someone else has trained takes about four lines of code. The real skill is knowing what the model was trained on, and when it will be wrong.

## Explain
In the last lesson, we saw how CNNs learn their own filters. Today, we use a model that has already done all that learning, and we ask a simple question. Can we trust its answers?

The Hugging Face Hub is a public website with many thousands of pre-trained models and datasets. The transformers library downloads a model from the Hub and runs it. The quickest route is a pipeline. It handles the preprocessing, like resizing and colour order, then the model, then turns raw scores into labels.

The code is short. You create a pipeline for image classification with a model name from the Hub, then pass it a photo and ask for the top three results. The first run downloads the model. Later runs use the saved copy.

Each result has a label and a score. The scores add up to one across all the classes the model knows. So a score of zero point nine does not mean a ninety percent chance of being right in the real world. It means the model strongly prefers this label over its other labels.

Before you trust a model, read its model card, the page that describes it on the Hub. Check three things. What data it was trained on. Which labels it can output, because it has no none of these option. And what the licence allows. Also, never send photos of people or private documents to online demo widgets.

Think of a pre-trained model as an expert visitor who has studied a huge encyclopaedia of photos. They name familiar things quickly. But show them something that was never in the encyclopaedia, and they still give the nearest name they know, in the same confident voice.

## Demonstrate
Tomasz Nowak runs an online marketplace for second-hand furniture in Gdańsk, Poland. He wants to suggest a category for each photo that sellers upload. He tests a general classifier on ten sample photos, with no people in them.

He opens a new Colab notebook, uploads the photos and runs the pipeline on the first one. You'll see something like this. Rocking chair at zero point seven one, folding chair at zero point one two, and park bench at zero point zero four.

Next, a short loop runs all ten photos and collects the results in a table, with the file name and the top three labels. Most chairs, tables and wardrobes get sensible labels.

He opens the model card in a new tab and scrolls to the training data and the label list. This is where he learns what the model can and cannot say.

Then he shows the two photos with the lowest top score. In his test, a sofa bed was labelled studio couch, which is close, but not one of his categories. And a shelf photographed from above was labelled crossword puzzle, probably because its grid looks like a familiar pattern.

His decision? The general model is useful for a first suggestion, but his own categories will need fine-tuning. The common mistake is to treat the top label as the answer. A pipeline always returns labels. Set a minimum score, send low scores to a person, and never compare scores between different models.

## Recap
Let's recap. First, a Hugging Face pipeline loads a pre-trained model and handles preprocessing, so you can classify images in a few lines. Second, the model card tells you the training data, the label list and the licence, so read it first. Third, a score shows preference, not a guarantee, so use a minimum score and review low-score cases.

## CTA
Now it is your turn. In the exercise below this video, you will classify ten of your own photos, record the top three labels, and explain two mistakes. It takes about twenty-five minutes. In the next lesson, we teach a model your own categories. Transfer Learning: Fine-Tuning on Your Own Images. See you there.

## Thumbnail
Headline: Four Lines, Real Classifier
Image: Navy background, a photo of a wooden rocking chair with three label bars beside it showing scores, headline in teal Inter Bold.

## Production Notes
- [VERSION] Hugging Face transformers pipeline task name (image-classification), the top_k argument, the model ID google/vit-base-patch16-224 and the Hub model card layout must be checked at recording time. Install transformers with pip if it is missing in Colab.
- [VERIFY] The training data and number of labels on the chosen model's card (content.md mentions ImageNet-style data with about 1,000 classes [VERIFY]). The voiceover does not state the dataset or the number of labels; it only tells learners to read the card.
- Run outputs: content.md marks the printed labels and scores as example output (code checked for syntax only). The voiceover therefore says 'you'll see something like' before rocking chair 0.71, folding chair 0.12, park bench 0.04, and describes the 'studio couch' and 'crossword puzzle' errors as what happened in Tomasz's test. If the recorded run gives different labels, keep the 'something like' wording and show the real output; re-record the error scene if the two wrong labels do not appear.
- Privacy: the 10 furniture photos contain no people and no private documents. Do not use the online demo widget on the model page with photos of people.
- Tomasz Nowak and his Gdańsk marketplace are fictional; no real marketplace name or logo on screen.
- Screen recording: clean browser profile, no account names or other tabs visible.
