# L03 Train/Test Split and Why It Matters | Presenter Script

Course: AI-12 · Video: 5 min · Words: 700

## Hook
In the last lesson, the decision tree predicted every training row correctly. That sounds perfect, but it tells us almost nothing. Today you will see a model with a perfect training score lose more than a quarter of it on new data.

## Explain
The goal of a model is generalisation. That means good predictions on new cases. To estimate it, we hold back part of the data as a test set. The model never sees it during training. We train on the training set, and we measure on the test set.

scikit-learn does this with one function, and three settings matter. The test size keeps a share of rows for testing, often between twenty and thirty percent. A fixed random state makes the split repeatable. And stratifying by the target keeps the same share of each class in both sets, which matters when one class is rare.

Comparing the two scores tells you a lot. If the training score is high and the test score is much lower, the model is overfitting. It has learned the noise in the training rows, not the general pattern. If both scores are low, it is underfitting, too simple for the pattern. A good fit has both scores reasonably high, and close together.

Remember this. A very high training score on its own is never evidence of a good model. A flexible model, such as a tree with no depth limit, can almost always reach close to one hundred percent on its own training data.

Think of a fair exam. If a teacher gives the exact questions from the homework, a student who memorised the answers scores one hundred percent. But that score does not show whether the student understands. The test set is the fair exam for your model.

## Demonstrate
Fatima Zahra is an analyst at an insurance company in Casablanca, Morocco. Before she uses real claims data, she tests the idea on synthetic data, with some label noise added, as real data has.

In a new Colab cell, we create one thousand synthetic rows, split them, and train two decision trees. One tree has no depth limit. The other can ask only three questions in a row. For each tree, we print the training score and the test score.

Before we read the results, look at the split. It returns four pieces, in a fixed order: training features, test features, then training targets and test targets. Mixing up this order is a common bug.

Now the first line of output. The deep tree scores one point zero on training data. That is one hundred percent. But on the test data, it scores only zero point seven two eight. It memorised the training rows, including the noisy labels.

The second line is the shallow tree. Its training score is lower, zero point eight five three. But its test score is higher, zero point eight one two. And its two scores are much closer together.

Fatima chooses the shallow tree as her starting point, and she writes a note in her notebook. The training score of one point zero was a warning sign, not a success.

A common mistake is to use the test set again and again. You try a setting, check the test score, change the setting, and check again. After many rounds, your choices are fitted to the test set, and the final score is too optimistic. Keep the test set for one final check. To choose between settings, you will use cross-validation in lesson ten.

## Recap
Let's recap. First, hold back a test set, and use a fixed random state and stratification for repeatable, balanced splits. Second, a big gap between a high training score and a lower test score means overfitting, and two low scores mean underfitting. Third, a high training score alone proves nothing, so keep the test set for the final check only.

## CTA
Now it is your turn. In the exercise below this video, you will compare a deep and a shallow tree, then change the random seed and watch the test scores move. It takes about twenty minutes. In the next lesson, Preprocessing: Scaling and Encoding, you will prepare mixed data for a model. See you there.

## Thumbnail
Headline: 100% Is a Warning
Image: Navy background, two score cards side by side: 'train 1.0' in grey and 'test 0.728' in amber, a small exam paper icon, headline in teal Inter Bold.

## Production Notes
- [VERSION] Outputs were recorded with scikit-learn 1.9.1 and Python 3.11. make_classification and train_test_split results can change between versions; re-run the cell in the current Colab version before recording and update every spoken and captioned score if the output differs.
- Screen scenes 8 to 12 use one Colab cell, copied exactly from the content.md Worked Example. It runs on its own and needs no earlier setup cell.
- Scene 9: content.md asks the presenter to point clearly to the order of the four outputs of the split; keep the highlight on screen for at least three seconds.
- Fatima Zahra and the Casablanca insurance company are fictional; the data is synthetic.
- Speak scores as decimals, for example 'zero point seven two eight'; the screen shows the exact output.
