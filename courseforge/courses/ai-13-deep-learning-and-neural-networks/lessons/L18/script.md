# L18 Capstone Step 1: Choose a Task and Build a Baseline | Presenter Script

Course: AI-13 · Video: 5 min · Words: 689

## Hook
The most common reason capstone projects fail is not a bad model. It is a dataset you cannot use, a task with no clear measure of success, or no simple result to compare with. This week, you fix all three.

## Explain
Your capstone has three steps. Choose and baseline, today. Experiment and choose, in the next lesson. And document, in the final lesson. Today's step has four parts.

First, choose a task. It must be image or text classification, with a clear set of labels. Plant diseases, product categories, support-ticket topics or review sentiment. Keep it small enough for free GPU time. A few thousand examples is plenty, and you can use a subset.

Second, choose a public dataset with a clear licence. Read the dataset card. Check the licence and whether it allows your use, the source, and how the labels were made. Avoid personal data, such as faces, names, health records or private messages. And if there is no validation split, create one with a fixed seed.

Third, build a baseline. That is the simplest reasonable model, trained quickly, that gives you a score to beat. For text, TF-IDF with logistic regression from the scikit-learn course is strong. For images, a small CNN, or a frozen pretrained backbone with a new head. Log it in your results table.

Fourth, write an experiment plan with at least three experiments. Each has a hypothesis, the one change you will make, and the metric that decides. Use macro F1 when classes are unbalanced, and accuracy when they are balanced and all errors cost the same.

A baseline is like the time a runner records on the first day of training. Without it, a later time of fifty-two minutes means nothing. With it, the runner knows whether the new plan actually helped.

## Demonstrate
Fatima is a data scientist at a telecoms company in Dakar, Senegal. For her capstone, she chooses public English customer reviews with three sentiment labels. She does not use her employer's customer messages.

She starts on the dataset card. She reads the licence, which allows educational use, and the label description, and writes both into a text cell in her notebook, before any code.

Then she loads the data, and splits off twenty percent of the training set for validation, with a fixed seed. She prints the label names and counts to check the class balance.

Now the baseline. A TF-IDF vectoriser with single words and word pairs, and a balanced logistic regression. She fits it on the training text, and scores macro F1 on the validation split. It takes seconds on a CPU.

She adds the baseline row to her results table, with its config. Then she writes her plan. One, fine-tune a small pretrained encoder with default settings. Two, the same with a learning-rate sweep and warm-up. Three, the best setting with a longer maximum length, because some reviews are long. The test split is not touched.

A common mistake is skipping the baseline, because it will obviously lose. Sometimes it does not. On short texts, TF-IDF can come close to a transformer, at a tiny fraction of the cost. Without a baseline, you cannot show that your deep model is worth it.

Another mistake is choosing a dataset first, and checking the licence later, when changing is expensive. Check it before you write any code.

## Recap
Let's recap. First, choose an image or text classification task, with a public dataset whose licence, source and content you have checked, and no personal data. Second, build a fast baseline and log it. It is the score every later experiment must beat. Third, write a plan with at least three experiments, each with a hypothesis, one change and a decision metric.

## CTA
Now it is your turn. This is capstone step one. In the exercise below this video, you will choose your dataset, train a baseline, and write an experiment plan with at least three experiments. The capstone rubric is on the course page. It takes about an hour. In the next lesson, capstone step two, fine-tune and compare. See you there.

## Thumbnail
Headline: Start With a Baseline
Image: Navy background, a runner's stopwatch next to a simple bar labelled baseline and an empty taller bar with a question mark, headline in teal Inter Bold.

## Production Notes
- [VERIFY] The dataset ID in content.md is a placeholder (your-chosen/dataset). The course team must provide 3 example datasets with confirmed licences and IDs; record the demo with one of them, a three-label English review-sentiment dataset whose card states a licence that allows educational use, and show its card on screen. The voiceover names no dataset.
- The baseline score is not stated (content.md gives none). Show the real printed macro F1; do not add numbers in captions.
- The capstone rubric (capstone_rubric.md) should be linked from the course page under this video.
- Fatima and the Dakar telecoms company are hypothetical; she uses public review text only, never employer data. Stock footage must not show a real operator's name or logo.
