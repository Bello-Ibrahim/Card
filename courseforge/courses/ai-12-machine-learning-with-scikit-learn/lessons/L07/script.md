# L07 Decision Trees and k-Nearest Neighbours | Presenter Script

Course: AI-12 · Video: 5 min · Words: 721

## Hook
Two models, two very different ideas. One asks a series of yes or no questions. The other asks, which past cases look most like this one? Both are easy to understand, and both show clearly how a model can be too simple, or too flexible.

## Explain
In lesson three, you saw a deep tree memorise its training data. Let's look at trees more closely. A decision tree is a flowchart. At each point, it asks a question about one feature, such as, is age above forty-five? It sends the row left or right, and at the end a leaf gives the prediction.

The most important setting is the maximum depth, the number of questions in a row. A shallow tree asks too few questions and misses real patterns. That is underfitting. A very deep tree keeps splitting until each leaf holds only a handful of training rows. It memorises noise. That is overfitting.

k-nearest neighbours does not build rules. To predict, it finds the k training rows closest to the new row, and takes a vote. It measures closeness as a distance across all features, so scaling matters. A small k follows single noisy points, and a very large k smooths away real differences.

The best way to see this is a validation curve. You plot the training and test scores while you change one setting. Where the training score keeps rising, but the test score stops rising or falls, the model has started to overfit.

A tree is like the game Twenty Questions. A few good questions find the answer. But with a thousand very specific questions, you are describing one person, not learning about people. And k-nearest neighbours is like asking your closest neighbours for advice. Useful, but only if you measure close fairly.

## Demonstrate
Mateo Fernández works for a farming cooperative in Argentina. He wants to understand model flexibility before he predicts crop problems. He uses the same synthetic data and split as lesson three.

This cell trains twenty trees, with depths from one to twenty. For each tree, it records the training score and the test score. Then it plots both lines, so we can see the whole story at once.

At depth one, the tree scores zero point six eight nine on training data and zero point six four eight on test data. Too simple. At depth four, the test score is at its highest, zero point eight two eight, with training at zero point eight six five.

After that, training keeps rising. At depth eight, it is zero point nine four seven, but test has fallen to zero point seven nine two. From depth thirteen to twenty, training is a perfect one, and test drops to zero point seven two eight. That is overfitting.

Next, k-nearest neighbours on the wine data. This cell trains the same model twice. Once on the raw measurements, and once inside a small pipeline that scales the features first. Then it prints both test scores.

Without scaling, the test accuracy is zero point seven two two. With scaling, it jumps to zero point nine six three. One wine feature has values in the hundreds or thousands, so without scaling, it decides the distance almost alone.

A common mistake is to choose the depth or k with the highest training score. For trees, that is always the deepest tree. For k-nearest neighbours, it is k equals one, because each training row is its own nearest neighbour. Both choices overfit. Choose settings using held-out data, and later with cross-validation and tuning.

## Recap
Let's recap. First, a decision tree asks yes or no questions, so limit its depth or leaf size to stop it memorising the training data. Second, k-nearest neighbours predicts from the most similar training rows, so always scale features first. Third, a plot of training and test scores against one setting shows where underfitting ends and overfitting begins.

## CTA
Now it is your turn. In the exercise below this video, you will vary the depth from one to twenty, plot both scores, and mark where your model starts to overfit. Then you will do the same for k-nearest neighbours. It takes about thirty minutes. In the next lesson, Accuracy Is Not Enough: The Confusion Matrix, we look at better ways to measure. See you there.

## Thumbnail
Headline: Too Simple, Too Flexible
Image: Navy background, a validation curve with a teal training line rising to 1.0 and an amber test line peaking then falling, headline in teal Inter Bold.

## Production Notes
- Setup before recording: in a fresh Colab runtime, run the L03 cell first (content.md L03 Worked Example: make_classification, the stratified split with random_state=42, and the imports of train_test_split and DecisionTreeClassifier). The first L07 cell uses that X_train and X_test. Do not run the L05 bank setup cell in the same runtime, because it overwrites X_train and y_train.
- [VERSION] Outputs were recorded with scikit-learn 1.9.1, matplotlib 3.11 and Python 3.11. Tree results and the wine split can change between versions; re-run before recording and update the spoken scores (depth table and 0.722 / 0.963) if they differ.
- Screen scenes 8 to 10 use the first L07 cell (depth loop and plot); scenes 11 and 12 use the second cell (KNN on wine), both copied exactly from content.md. The depth table values come from the train_acc and test_acc lists; show them as a small overlay table on the plot, as content.md lists them.
- Mateo Fernández and the Argentine farming cooperative are fictional; the data is synthetic and the wine data ships with scikit-learn.
