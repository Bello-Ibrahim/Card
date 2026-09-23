# L06 Logistic Regression for Yes/No Questions | Presenter Script

Course: AI-12 · Video: 5 min · Words: 710

## Hook
Will this customer subscribe? Yes or no. But a bank calling thousands of people wants more than yes or no. It wants to know how likely each person is to say yes, so it can call the most promising customers first.

## Explain
In the last lesson, you built a pipeline with logistic regression at the end. Today we look inside it. Despite its name, logistic regression is a classification model, and it works in two stages.

First, it combines the features into one score. Each feature is multiplied by a weight, called a coefficient, and the results are added up with a starting value. Second, it squeezes that score into a probability between zero and one.

The model can give you these probabilities directly. Its normal prediction applies a threshold of zero point five. A probability of zero point five or more becomes yes, and anything lower becomes no. The threshold is a business choice, not a law of nature, and in lesson nine you will move it.

A positive coefficient pushes the probability of yes up as the feature increases. A negative one pushes it down. The size shows the strength, but only if features are on comparable scales. That is why we scale numbers first. For one-hot columns, the coefficient compares that category with the others.

Two cautions. Coefficients describe what the model learned from this data. They do not prove cause and effect. And when features are strongly related, the model can share weight between them in unstable ways.

Think of a panel of judges giving points. Each feature is a judge who adds or removes points, and some judges have a stronger voice. The total becomes a percentage, and the bank decides how high it must be before it picks up the phone.

## Demonstrate
Priya Nair is a marketing analyst at a bank in Kochi, India. She wants to know which customer groups respond to term-deposit calls. She continues in the course notebook, where the setup cell and the pipeline from lesson five have already run.

This cell takes the readable feature names from the preprocessing step, pairs them with the model's coefficients, and sorts them. Then it prints the probability of yes for the first three test customers, and the model's yes or no decision for each.

At the bottom of the list are the largest positive coefficients. Being retired has the strongest push, zero point eight two. Then older age, zero point five eight, and a higher balance, zero point four two. These raise the probability of subscribing.

At the top are the largest negative ones. More calls in this campaign, minus zero point six nine. Telephone contact, minus zero point three six. And technician jobs, minus zero point three four. These lower the probability.

Now the first three test customers. Their probabilities of yes are three percent, two percent and seventeen percent. All are below zero point five, so all three are predicted no. The prefixes num and cat simply come from the step names in the column transformer.

Priya notes one thing. More calls lowers the probability. That could mean repeated calls annoy people. Or it could mean the bank keeps calling people who were never interested. The model cannot tell which.

A common mistake is to compare coefficients of features that were not scaled. A weight per unit of income cannot be compared with a weight per year of age. Always read coefficients from a pipeline that scales numbers, and describe them as associations, not causes.

## Recap
Let's recap. First, logistic regression is a classifier that outputs a probability, and by default it turns that into yes or no at zero point five. Second, positive coefficients push the probability of yes up, and negative ones push it down, but compare sizes only after scaling. Third, coefficients show what the model learned from this data, not what causes the outcome.

## CTA
Now it is your turn. In the exercise below this video, you will list the three largest positive and negative coefficients in your own pipeline, and describe each one in plain words, using is linked with rather than causes. It takes about twenty-five minutes. In the next lesson, Decision Trees and k-Nearest Neighbours, we meet two new models. See you there.

## Thumbnail
Headline: How Likely Is Yes?
Image: Navy background, a probability dial from 0 to 1 with a needle near 0.17 and a 0.5 marker, a phone icon beside it, headline in teal Inter Bold.

## Production Notes
- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] get_feature_names_out, named_steps and LogisticRegression defaults (regularisation, solver) depend on the installed version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11 on the synthetic stand-in data; re-run before recording and update the spoken coefficients and probabilities if they differ.
- Screen scenes 9 to 13 use one cell copied exactly from the content.md Worked Example.
- Speak negative coefficients as 'minus zero point six nine'; the screen shows -0.69. Speak probabilities as percentages, as content.md does (3%, 2% and 17%).
- Priya Nair and the Kochi bank are fictional; the data is synthetic.
