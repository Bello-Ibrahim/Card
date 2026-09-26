# L07 Transfer Learning: Fine-Tuning on Your Own Images | Presenter Script

Course: AI-19 · Video: 5 min · Words: 693

## Hook
In the last lesson, the general model did not know your categories. Training a new model from zero needs a very large labelled dataset. With transfer learning, around a thousand labelled images and a short Colab session can be enough to teach a model a new task.

## Explain
Tomasz, in Gdańsk, needed his own furniture categories, and the general model could not give them. Today, we fix that kind of problem. We take a model that already sees well, and teach it a new job.

Remember from lesson five that image models learn general features in their early and middle layers. Edges, textures, shapes and parts. Only the last layer, the classification head, is specific to the original labels.

Transfer learning keeps the pre-trained layers, called the backbone, and replaces the head with a new one that has your classes. This works with little data, because the backbone already knows what an edge or a leaf vein looks like. Your data only teaches the head which combination of features means rust, or healthy.

There are two common levels. With feature extraction, you freeze the backbone and train only the new head. It is fast and needs little data. With full fine-tuning, you also update the backbone, with a small learning rate. It can fit your data better, but needs more data and time. Start with feature extraction.

Keep your train, validation and test splits separate, and check the test split only once, at the end. And remember that free Colab GPUs are useful here, but they are not guaranteed, and sessions are limited. So save your work when training ends.

Think of it like hiring an experienced photographer to sort plant photos. They already understand light, shapes and colours. You only show them a few hundred examples of each disease. A beginner would need years. The photographer needs an afternoon.

## Demonstrate
Let's try it. Grace Namukasa works for an agricultural advice service in Mbale, Uganda. She wants a model that classifies bean leaf photos as healthy, or as one of two diseases. She uses a public bean leaf photo dataset.

First, in Colab, she opens the runtime settings and chooses a GPU, if one is available. Training is much faster on a GPU. If none is free today, the same code still runs on the processor, only more slowly.

Then she walks through the cell. It loads the dataset and the class names, loads a pre-trained vision model with a new head for three classes, and prepares each image the way the model expects. Here is the key line. A short loop freezes every backbone parameter, so only the new head will learn.

She runs it. Before training, the new head is untrained, so the test accuracy is close to guessing, about one in three. You'll see something like zero point three four. Then the training starts, and the loss goes down, epoch by epoch.

After three epochs, the test accuracy is a clearly higher number. Your numbers will differ, and they are not a benchmark. Finally, she saves the model, because she will measure it properly in the next lesson.

Watch for two common mistakes. Reporting accuracy on the training images only shows that the model remembers them, so report the test split. And unfreezing the whole backbone with a high learning rate on a small dataset can destroy the pre-trained features. When you unfreeze, use a small learning rate.

## Recap
Let's recap. First, transfer learning reuses a pre-trained backbone and trains a new head for your classes, so it needs much less data and time. Second, start by freezing the backbone and training only the head, and unfreeze later only if you have enough data. Third, keep your splits separate, and report results on the test split.

## CTA
Now it is your turn. In the exercise below this video, you will fine-tune a small pre-trained model on a public dataset of three to five classes, and compare its test accuracy before and after. Save your best model, because you will need it next. It takes about forty minutes. In the next lesson, Measuring Classification Quality. See you there.

## Thumbnail
Headline: New Head, Same Brain
Image: Navy background, a bean leaf photo beside a simple network diagram whose last block glows teal, headline in teal Inter Bold.

## Production Notes
- [VERIFY] The bean leaf dataset: Hub ID AI-Lab-Makerere/beans, its licence, column names image and labels, and that it was collected in Uganda. The voiceover says only 'a public bean leaf photo dataset' and does not state where it was collected or where it is hosted.
- [VERIFY] The recommended way to save a model from Colab (Google Drive mount or push to the Hub). The voiceover only says 'saves the model', matching the trainer.save_model() screen step.
- [VERSION] Google Colab GPU availability, session limits and the Runtime menu path change and are not guaranteed. The voiceover says 'a GPU, if one is available'.
- [VERSION] Hugging Face transformers and datasets APIs (TrainingArguments arguments, with_transform, base_model) and the checkpoint ID google/vit-base-patch16-224-in21k. Code was checked for syntax only.
- Run outputs: content.md gives 'before: 0.34' only as example output and no exact 'after' value. The voiceover says 'you'll see something like zero point three four' and 'a clearly higher number'. Do not add an on-screen caption with a specific after value.
- Grace Namukasa and the Mbale advice service are fictional. Stock footage of bean plants must show no identifiable farmers.
- Screen recording: clean browser profile, no account names or other tabs visible.
