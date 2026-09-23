# L14 Evaluating Deep Models Properly | Presenter Script

Course: AI-13 · Video: 5 min · Words: 698

## Hook
You change the learning rate, and accuracy goes up by one point. Is the new setting better? Run the old setting again with a different random seed, and it may move by one point on its own. So how much is just chance?

## Explain
A quick recap from the scikit-learn course. Use three splits. Training to fit the weights. Validation to make choices, such as epochs and hyperparameters. And test, to measure the final choice once. Look beyond one number. A confusion matrix and per-class scores show which classes get confused.

Deep models add two reasons to be careful. First, randomness is everywhere. The seed controls the new layer's starting weights, the shuffling order, dropout and augmentation. Two runs with the same settings but different seeds can give noticeably different scores, especially on small datasets.

So run important settings with three or more seeds, and report the mean and the spread. If two settings' ranges overlap a lot, you have not shown that one is better.

Second, many choices use up the validation set. Every time you look at validation results and change something, you fit your decisions a little to that split. After many experiments, the validation score becomes optimistic. That is why the test set stays locked until the end.

Finally, error analysis turns a score into a plan. Collect the misclassified validation examples, read them, and group them. Wrong or unclear labels, examples that really belong to two classes, very short or unusual inputs, or a pattern the model has not learned.

One football match does not tell you which team is stronger. A lucky goal can decide it. A league of many matches is fairer. Several seeds are a small league for your models. And error analysis is watching the recording of the matches you lost.

## Demonstrate
Ayesha is an engineer at a non-profit in Dhaka, Bangladesh, that sorts English news summaries by topic for a media-monitoring project. She uses the AG News setup from the last lesson, and wants a result she can trust.

In Colab, she has wrapped her training code in a function that takes a seed and returns the validation predictions and labels. The function sets the seed everywhere, so each run can be repeated. The same seed always gives the same result.

She runs it with seeds zero, one and two, computes macro F1 for each, and prints the mean, standard deviation, minimum and maximum. This is the number she reports, not the best single run.

Next, a confusion matrix for one run, with the four topic names. Then she lists the first ten misclassified validation examples, with the true label, the predicted label, and the start of the text.

She reads them and groups them. Most errors are between Business and Science and Technology. Summaries about technology companies' earnings could fit either label. A few look mislabelled.

Her conclusion. A larger model may help a little, but the class definitions themselves overlap, and she writes this down as a limitation. Each error group points to a different fix. Clean the labels, change the class definitions, collect data, or change the model.

A common mistake is comparing two settings with one run each, when the difference is smaller than normal seed variation. Another is doing error analysis on the test set. It then becomes a second validation set, and the final score is no longer honest.

Do error analysis on validation data, and keep the test set for the final, single check.

## Recap
Let's recap. First, keep separate validation and test splits. Make every choice on validation, and use test once, at the end. Second, run key settings with at least three seeds, and report the mean and spread before claiming that one is better. Third, read and group misclassified examples, to find whether the problem is the labels, the class definitions, the data or the model.

## CTA
Now it is your turn. In the exercise below this video, you will run your text model with three seeds, report the mean and spread, and review ten misclassified examples to find a pattern. It takes about forty minutes. In the next lesson, we debug common training problems. See you there.

## Thumbnail
Headline: Is It Better, Really?
Image: Navy background, three overlapping score ranges drawn as teal bars with dots for three seeds, next to a small confusion matrix, headline in teal Inter Bold.

## Production Notes
- [VERIFY] AG News dataset licence and source (carried from L13) must be confirmed before the dataset is used in the recording.
- run_experiment is the learner's own L13 code wrapped in a function; define it in a cell above the demo before recording. It must set the seed in TrainingArguments and in any subset shuffling.
- No scores are stated in the voiceover (content.md gives none). Show the real mean, std, min and max printed by the notebook; do not add numbers in captions.
- Three seeded runs take time on the free GPU; pre-run them and speed up the training segment in the edit.
- Ayesha and the Dhaka non-profit are hypothetical; stock footage must not show a real organisation's name or logo.
