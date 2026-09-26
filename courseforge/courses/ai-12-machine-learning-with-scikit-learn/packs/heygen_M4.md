# HeyGen Batch Pack: AI-12 M4 (Explaining Models and the Capstone)

Course: Machine Learning with scikit-learn. Make one HeyGen video per lesson below, using these settings for every video.

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

## L15 Which Features Matter? Interpreting Models

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M4_L15_presenter.mp4`
- **Expected length:** about 5.0 minutes (695 words). The quality gate accepts ±10%.

```text
A sales manager asks, your model says who will subscribe, so why those people? If your only answer is the algorithm decided, she will not trust it, and she should not. Today you learn three ways to see which features drive a model.

The first way is coefficients, which you met in lesson six. For linear and logistic models, they show the direction and size of each feature's effect, if the features are scaled. They are simple, but they only exist for linear models.

The second way is tree feature importances, in random forests and many tree models. They measure how much each feature improved the splits while the trees were built. They are quick, but they have some known limits, so check them against the third way.

The third way is permutation importance, and it works with any model, including a whole pipeline. It takes one column at a time, shuffles its values randomly, and measures how much the score drops. If the score falls a lot, the model relies on that column. If it barely moves, the model does not need it.

Three limits apply to all of these. Importance is not cause. Changing a feature does not necessarily change the outcome. Correlated features share importance, so if two columns carry the same information, both may look unimportant. And importance describes this model on this data, not the world in general.

Permutation importance is like muting the instruments in a band, one at a time. If the song falls apart without the drums, the drums matter. But if two guitars play the same part, muting either one changes little, and you might wrongly decide that neither guitar matters.

Tan Mei Lin is a data scientist at a bank in Kuala Lumpur, Malaysia. She must explain the term-deposit model to the sales team. She continues in the bank notebook, where the logistic regression pipeline is fitted.

This cell runs permutation importance on the test set, scored by ROC AUC. It shuffles each original column twenty times, and records the average drop and its spread. Then it prints the columns sorted from most to least important.

Shuffling the number of calls lowers ROC AUC by about zero point zero seven eight on average. That is the largest drop. Age follows closely at zero point zero six six, and job at zero point zero six five.

Contact type drops the score by zero point zero three zero. Balance has a mean drop of zero point zero one one, with a spread of zero point zero one two. The spread is larger than the mean, so its effect cannot be separated from zero with this test set.

Then Mei Lin writes three sentences for the sales manager. One. The number of times we have already called a customer in this campaign is the strongest signal. Customers called many times are less likely to subscribe.

Two. Age and job type matter almost as much. Older and retired customers are more likely to say yes. Three. Account balance adds very little once we know the other information. These are patterns in past data, not proof that calling less will make people subscribe.

The most common mistake is to present importance as cause, for example, reduce calls and subscriptions will rise. The model only shows that customers with many calls subscribed less in the past. Perhaps the bank kept calling people who were never interested.

Let's recap. First, coefficients, tree importances and permutation importance each show which features a model relies on, with different strengths and limits. Second, permutation importance works with any pipeline, and should be run on held-out data, with its spread reported. Third, importance is not cause, so say is linked with, and watch for correlated features that share importance.

Now it is your turn. In the exercise below this video, you will calculate permutation importance for your best model, chart it with error bars, and write three plain sentences for a sales manager. It takes about thirty minutes, and it prepares you for the capstone report. In the next lesson, Fairness, Limits and Model Risk, we check who the model serves less well. See you there.
```

## L16 Fairness, Limits and Model Risk

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M4_L16_presenter.mp4`
- **Expected length:** about 5.0 minutes (686 words). The quality gate accepts ±10%.

```text
Your model finds sixty-seven percent of subscribers overall. That sounds acceptable. But what if it finds ninety percent in one age group, and thirty percent in another? An average can hide a group for which the model fails.

In the last lesson, you asked which features drive a model. Now we ask who it serves less well. A single overall score describes the average customer, but real decisions affect individual people and groups. Before a model is used, check three kinds of risk.

First, subgroup performance. Split the test results by meaningful groups, such as region, age band or channel, and calculate the key metric for each group. Also count the positive cases in each group. A recall based on five people is very uncertain.

Some attributes, such as gender or ethnicity, may be sensitive or legally protected. Whether you may collect and use them, even for checking fairness, depends on local law and company policy.

Second, data risks. A rare positive class leads to low recall, unless you adjust the threshold or the class weights. Customer behaviour and prices change over time, so a model trained on last year's data can slowly become less accurate. And if some groups are rare in the training data, the model has less to learn from for them.

Third, impact risk. For each type of mistake, ask who is affected, and how badly. An unneeded marketing call is a small cost. A wrongly refused loan, or a missed health check, is serious. The higher the impact, the more human review the model needs. Write all this down in a short risk note.

A school's average exam result can look good while one class is failing badly. A careful head teacher looks at each class, not only the school average. Subgroup checks are that class-by-class view.

Nomvula Dlamini is a data analyst at a bank in Durban, South Africa. Her team plans to use the term-deposit model with the threshold of zero point one five chosen in lesson nine. She checks recall by age band on the test set.

We continue in the bank notebook. This cell groups test customers into three age bands, and applies the threshold of zero point one five. Then it keeps only the real subscribers, and for each band, counts them and calculates the share the model found. Among real subscribers, that share is the recall.

For customers aged fifty-one to seventy-nine, there are forty subscribers, and the model finds zero point seven two, or seventy-two percent of them.

For ages thirty-one to fifty, there are fifteen subscribers, and recall is only zero point five three. Fifty-three percent. That is the weakest group.

The youngest group, eighteen to thirty, has a recall of zero point six zero. But it has only five subscribers in the test set, so that number could easily change with a different sample.

Nomvula writes her risk note. Lower recall for ages thirty-one to fifty: review a lower threshold or better features. Too few young subscribers to judge: collect more data. Behaviour may change when interest rates change: check recall by group every month, and retrain when it falls below an agreed level.

A common mistake is to check subgroups with accuracy. With a rare positive class, a group can have high accuracy simply because few of its members subscribe. Use recall or precision for the positive class, and always show group sizes next to the scores.

Let's recap. First, overall scores can hide groups where the model fails, so check the key metric for each meaningful subgroup, with group sizes. Second, class imbalance, data that changes over time, and unrepresentative data are common model risks. Third, ask what happens when the model is wrong, and write a risk note with one mitigation for each risk.

Now it is your turn. In the exercise below this video, you will compare recall across three subgroups and write a short risk note. You will reuse it in your capstone. It takes about thirty minutes. In the next lesson, Capstone Step 1: Build an End-to-End Model, you put every piece together. See you there.
```

## L17 Capstone Step 1: Build an End-to-End Model

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M4_L17_presenter.mp4`
- **Expected length:** about 5.0 minutes (696 words). The quality gate accepts ±10%.

```text
You now have every piece. In this lesson, you put them together in the right order, on a dataset you choose, and finish with a tested model saved to a file. This is the first step of your capstone project.

First, choose a public business dataset with a clear target and at least a few thousand rows. UCI and Kaggle are good places to look. Read the licence of the dataset you choose, and cite it. And do not use personal or confidential data from your employer, in Colab or in any AI tool.

Then follow one order in one notebook. Frame the problem, including the cost of each mistake. Split once, with a fixed random state, and do not look at the test set again until the end. Build a dummy baseline that every model must beat. Then a pipeline, with a simple model first.

Next, cross-validate two or three models, and test new features. Tune the best candidate with a random search, and for classification, choose a threshold from costs. Only then, score the chosen pipeline once on the test set. Finally, save the fitted pipeline, and record the library versions.

A saved model only loads reliably with compatible library versions, so write the versions next to the file. And never load a model file from an untrusted source. Loading such a file can run any code hidden inside it.

An end-to-end project is like following a recipe from shopping to serving. Each step depends on the one before. And you taste the dish at the end only once, when the guests arrive. If you keep tasting and changing it in front of them, their opinion is no longer independent.

Elena Popescu is a junior data scientist at a bank in Cluj-Napoca, Romania. She has framed her problem, which customers to call for a term deposit. She has split the data and built the pipeline from lesson five. Here is the last part of her notebook.

This cell cross-validates a dummy baseline and the real pipeline. Then it fits the final pipeline, scores it once on the test set, saves it to a file with the library version, loads it back, and predicts three customers.

Notice that the baseline sits inside the same pipeline, with the same preprocessing and five folds as the real model. So the comparison is fair. The only difference is the model at the end, and the baseline simply predicts the share of subscribers for everyone.

The baseline scores zero point five, which is random ranking. The model scores zero point seven seven eight in cross-validation, so it clearly learns something.

The single test score is zero point seven five two. It is a little lower than the cross-validation mean, but within the spread you saw in lesson ten. Elena reports it as her final number.

The whole pipeline, including preprocessing, is saved to one file, with scikit-learn version one point nine point one. Loading it back and predicting three customers confirms that the file works.

Colab storage is temporary, so we download the file from the Files panel. Elena also adds a text cell with the library version, her chosen threshold of zero point one five from lesson nine, and the date.

A common mistake is to save only the model step, without the preprocessing. When the file is loaded later, raw data cannot be passed to it, and people rebuild the preprocessing by hand, often with small differences. Save the whole fitted pipeline.

Let's recap. First, follow one order: frame, split once, baseline, pipeline, compare, tune, test once, and save. Second, every model must beat a dummy baseline, and the test set is scored once, at the very end. Third, save the whole fitted pipeline, record the library versions, and never load model files from untrusted sources.

Now it is your turn. This is capstone step one. In the exercise below this video, you will complete your modelling notebook, from framing to a tuned, tested and saved model, with a subgroup check. Plan about two hours, spread over the week. In the next lesson, Capstone Step 2: Report to Stakeholders, you will explain your results. See you there.
```

## L18 Capstone Step 2: Report to Stakeholders

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M4_L18_presenter.mp4`
- **Expected length:** about 5.1 minutes (706 words). The quality gate accepts ±10%.

```text
ROC AUC zero point seven five, recall zero point six seven, at a threshold of zero point one five. To a data scientist, that is a clear result. To a sales director, it means nothing. And a model that nobody understands will not be used.

In the last lesson, you built, tested and saved your model. Your last task is to explain it in the language of the business. A stakeholder report is one page, for people who make decisions, not for people who build models.

It answers six questions, in order. What decision does the model support? What does it do, in one or two sentences, with no algorithm names? How well does it perform, in business terms? What are its limits? What are the risks? And what do you recommend?

Performance in business terms means counts that people can picture. Precision becomes, of every hundred customers we call, about this many subscribe. Recall becomes, we reach about this many out of every ten who would subscribe. And always compare with the current way of working.

Write for a busy reader. Use short sentences and plain words. Put the most important numbers in one small table, and add a summary of three sentences at the top: what the model does, how much it helps, and what you recommend.

Be honest about uncertainty. Round your numbers, and say what they are based on, such as tested on five hundred past customers the model had not seen. If an AI assistant helps with wording, share only summary numbers and your own text, never customer data.

A good report is like a weather forecast on the evening news. The forecaster does not explain the physics of air pressure. She says, seventy percent chance of rain tomorrow afternoon, take an umbrella. You get the result, how sure it is, and what to do.

Kwame Mensah is a data analyst at a bank in Accra, Ghana. His model is the term-deposit pipeline from this course, with the threshold of zero point one five from lesson nine.

On a test set of five hundred past customers, sixty had subscribed. The model selected one hundred and thirty-seven customers to call, and forty of them had subscribed. It missed the other twenty subscribers.

Kwame turns these counts into business statements. If we call the customers the model selects, about twenty-nine of every hundred calls lead to a subscription. If we call customers at random, about twelve of every hundred do.

The model's list reaches about two out of every three customers who would subscribe, while calling only about a quarter of all customers. And it works less well for customers aged thirty-one to fifty, where it reaches about half of the subscribers.

His summary for the head of retail, Isabel Duarte, reads: We built a score that ranks customers by how likely they are to open a term deposit. In a test on five hundred past customers, calling the top-ranked quarter reached two thirds of the subscribers, with more than twice as many subscriptions per call as random calling.

We recommend a one-month trial in one region, with a monthly check of results by age group. His limits section notes that the test used past data only, some age groups had few subscribers, and call outcomes may change with interest rates.

A common mistake is to copy the classification report into the stakeholder report, or to describe the method in detail. Readers stop at the first unknown term. Another is to hide the limits. Stakeholders who later find a hidden weakness stop trusting both the model and its author.

Let's recap. First, a one-page report covers the problem, what the model does, performance in business terms, limits, risks, and a recommendation. Second, turn metrics into counts people can picture, and compare with a baseline. Third, start with a three-sentence summary, avoid jargon, and state limits and risks honestly.

Congratulations. You have finished Machine Learning with scikit-learn. Your last exercise is capstone step two: write your one-page report and three-sentence summary, and ask someone without a data background to read it. It takes about an hour. Then submit your notebook, your model file and your report as your capstone. Well done, and good luck.
```
