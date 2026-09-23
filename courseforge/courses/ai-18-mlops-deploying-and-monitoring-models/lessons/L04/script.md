# L04 Experiment Tracking with MLflow | Presenter Script

Course: AI-18 · Video: 5 min · Words: 684

## Hook
Last week you tried twelve model settings. Which one gave the best score, with which data, and where is that model file now? If the answer lives in a spreadsheet, or only in your memory, you need experiment tracking.

## Explain
In the last lesson, we made training reproducible. Now we record it. Experiment tracking saves every training run automatically. It stores the parameters, meaning settings such as C. It stores the metrics, such as F1. And it stores the artefacts, such as the trained model file.

MLflow is a free, open-source tool for this. Its tracking part has three ideas. An experiment groups related runs, such as wine quality. A run is one execution of your training code. And the tracking store is where runs are saved. For this course, a local database file is enough. Teams usually share a tracking server, so everyone sees the same history.

You add only a few lines to the training code. You point MLflow at the store and name the experiment. Then, for each value of C, you start a run, train the pipeline, and log the parameter, the F1 score and the model. You also give an input example, so MLflow records the expected input columns.

Think of it as a laboratory notebook that writes itself. Every experiment gets a page, with the date, the exact settings and the results. And a sample is kept in the fridge, so you can repeat or check it later. Nobody has to remember anything, because the notebook remembers for them.

## Demonstrate
Let's meet Beatriz Carvalho. She works for a hypothetical wine cooperative in Portugal, and she wants to predict which red wines tasters will rate as good. In our demo, we use the offline synthetic data from lesson three, so you can follow without a download.

In a terminal in the project folder, she installs MLflow. She creates a small tracking script with the loop you just saw, and runs it. Three runs are logged, one for each value of C. Each run gets a clear name that includes its setting, so she can find it again later without guessing.

Next, she starts the MLflow interface, pointing it at the same database file. She opens the local address that it prints, and clicks the wine quality experiment. The table shows all three runs, with their names.

She selects all three runs and clicks Compare. Now the parameter C and the F1 score sit side by side. With C of one, F1 is zero point five five seven. With C of zero point one, it is zero point five three eight. With C of zero point zero one, it drops to zero point four six one.

Beatriz chooses C of one. The strongest regularisation clearly underfits. She opens the best run and shows the Artifacts tab, where the saved model folder waits. The difference between C of one and C of zero point one is small, so on more data she might check both again. Her scores on the real dataset will be different.

A common mistake is to log only the best run. The poor runs matter too, because they show what you already tried and why you rejected it. So log every run, and never delete a run because it looks bad. And never log secrets or personal data. Anyone who can open the tracking server can read them.

## Recap
Let's recap. First, experiment tracking records the parameters, metrics and artefacts of every training run. Second, in MLflow, experiments group runs, and the interface lets you compare runs and open their saved models. Third, log every run, including poor ones, and choose a model with a metric that fits your problem.

## CTA
In the exercise below this video, you will log at least three runs with different settings, compare them in the interface, and write down which run you would choose, and why. It takes about thirty-five minutes. You will need this tracking for your capstone.

In the next lesson, we keep only the models that matter, and version them properly, in Model Registry and Data Versioning. See you there.

## Thumbnail
Headline: Track Every Run
Image: Navy background, a clean table of three runs with one row highlighted in teal and a small lab-notebook icon, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Wine Quality dataset: confirm the licence, current location on the UCI Machine Learning Repository, and the description of its origin (Portuguese vinho verde). The voiceover does not state these; it only says the demo uses the offline synthetic data.
- [VERSION] MLflow interface labels (experiment list, Compare, Artifacts tab), the mlflow ui command and its default port 5000, the name= versus artifact_path= argument, and the skops default serialisation were checked against MLflow 3.16.1 only. Re-check before recording and update screen_steps if labels moved.
- F1 values 0.557, 0.538 and 0.461 are real results on the synthetic fallback data, not the real dataset; they must match on screen.
- Beatriz Carvalho and the wine cooperative are hypothetical.
- The tracking store is a local SQLite file; do not show any shared tracking server address or credentials on screen.
