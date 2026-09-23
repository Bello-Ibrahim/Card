# L17 Capstone Step 1: Build an End-to-End Model | Presenter Script

Course: AI-12 · Video: 5 min · Words: 704

## Hook
You now have every piece. In this lesson, you put them together in the right order, on a dataset you choose, and finish with a tested model saved to a file. This is the first step of your capstone project.

## Explain
First, choose a public business dataset with a clear target and at least a few thousand rows. UCI and Kaggle are good places to look. Read the licence of the dataset you choose, and cite it. And do not use personal or confidential data from your employer, in Colab or in any AI tool.

Then follow one order in one notebook. Frame the problem, including the cost of each mistake. Split once, with a fixed random state, and do not look at the test set again until the end. Build a dummy baseline that every model must beat. Then a pipeline, with a simple model first.

Next, cross-validate two or three models, and test new features. Tune the best candidate with a random search, and for classification, choose a threshold from costs. Only then, score the chosen pipeline once on the test set. Finally, save the fitted pipeline, and record the library versions.

A saved model only loads reliably with compatible library versions, so write the versions next to the file. And never load a model file from an untrusted source. Loading such a file can run any code hidden inside it.

An end-to-end project is like following a recipe from shopping to serving. Each step depends on the one before. And you taste the dish at the end only once, when the guests arrive. If you keep tasting and changing it in front of them, their opinion is no longer independent.

## Demonstrate
Elena Popescu is a junior data scientist at a bank in Cluj-Napoca, Romania. She has framed her problem, which customers to call for a term deposit. She has split the data and built the pipeline from lesson five. Here is the last part of her notebook.

This cell cross-validates a dummy baseline and the real pipeline. Then it fits the final pipeline, scores it once on the test set, saves it to a file with the library version, loads it back, and predicts three customers.

Notice that the baseline sits inside the same pipeline, with the same preprocessing and five folds as the real model. So the comparison is fair. The only difference is the model at the end, and the baseline simply predicts the share of subscribers for everyone.

The baseline scores zero point five, which is random ranking. The model scores zero point seven seven eight in cross-validation, so it clearly learns something.

The single test score is zero point seven five two. It is a little lower than the cross-validation mean, but within the spread you saw in lesson ten. Elena reports it as her final number.

The whole pipeline, including preprocessing, is saved to one file, with scikit-learn version one point nine point one. Loading it back and predicting three customers confirms that the file works.

Colab storage is temporary, so we download the file from the Files panel. Elena also adds a text cell with the library version, her chosen threshold of zero point one five from lesson nine, and the date.

A common mistake is to save only the model step, without the preprocessing. When the file is loaded later, raw data cannot be passed to it, and people rebuild the preprocessing by hand, often with small differences. Save the whole fitted pipeline.

## Recap
Let's recap. First, follow one order: frame, split once, baseline, pipeline, compare, tune, test once, and save. Second, every model must beat a dummy baseline, and the test set is scored once, at the very end. Third, save the whole fitted pipeline, record the library versions, and never load model files from untrusted sources.

## CTA
Now it is your turn. This is capstone step one. In the exercise below this video, you will complete your modelling notebook, from framing to a tuned, tested and saved model, with a subgroup check. Plan about two hours, spread over the week. In the next lesson, Capstone Step 2: Report to Stakeholders, you will explain your results. See you there.

## Thumbnail
Headline: Frame, Build, Test, Save
Image: Navy background, a horizontal path of eight numbered stepping stones from 'frame' to 'save', ending at a file icon, headline in teal Inter Bold.

## Production Notes
- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The L17 cell uses Pipeline, prep, pipe, X_train, y_train, X_test and y_test from those cells. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERIFY] Availability and licences of the suggested datasets (UCI Bank Marketing, UCI Online Shoppers Purchasing Intention, UCI Seoul Bike Sharing Demand, Kaggle telecom churn and hotel booking datasets), and that Kaggle needs a free account. The voiceover names only UCI and Kaggle as places to look and tells learners to read and record each licence; it does not name specific datasets.
- [VERSION] Kaggle download steps in Colab (account, API token, commands) and the Colab Files panel may change. Check the download step in scene 13 against the live interface.
- [VERSION] joblib model files depend on scikit-learn and dependency versions and must not be loaded from untrusted sources. Outputs were recorded with scikit-learn 1.9.1, joblib 1.6.0 and Python 3.11 on synthetic data; re-run before recording and update the spoken scores and version if they differ.
- Screen scenes 8 to 13 use one cell copied exactly from the content.md Worked Example.
- Elena Popescu and the Cluj-Napoca bank are fictional; the data is synthetic.
