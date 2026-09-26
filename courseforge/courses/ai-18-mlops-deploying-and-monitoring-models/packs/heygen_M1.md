# HeyGen Batch Pack: AI-18 M1 (From Notebook to Reproducible Project)

Course: MLOps: Deploying and Monitoring Models. Make one HeyGen video per lesson below, using these settings for every video.

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

## L01 Why Models Fail After the Notebook

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M1_L01_presenter.mp4`
- **Expected length:** about 5.2 minutes (735 words). The quality gate accepts ±10%.

```text
Your model scored well in the notebook last month. Today a colleague runs the same notebook on a new laptop. First the score is different, then there is an error. Nothing about the model changed. So what broke?

Hi, and welcome to MLOps: Deploying and Monitoring Models. In this first lesson, we look at the gap between it works on my machine, and it works every day for real users.

A notebook is an excellent place to explore. It is a poor place to run a production system. Most production failures of machine learning models are not caused by the algorithm. They come from everything around it. Four groups of problems appear again and again.

The first group is missing or changing dependencies. The notebook imports libraries without fixed versions, and a new release changes a default value. The second group is different data. Training used a file on one laptop, but live data brings new categories, missing values or different units.

The third group is silent errors. A cell ran out of order, a random seed was never set, or a preprocessing step lives only in the notebook. The model still answers, but the answer is wrong, and nothing raises an error. The fourth group is nobody watching. The world changes, and the model slowly becomes less accurate. We call this drift.

MLOps, short for machine learning operations, is the set of practices that closes this gap. You will meet six key terms. An artefact is any file the pipeline produces, such as a model or a Docker image. A model registry stores each model version and marks which one is in production. CI and CD mean every change is tested and built automatically.

Serving means making a model available to other systems, for example through an API. Drift means production data no longer looks like training data. And rollback means returning quickly to the last working version. The central idea is reproducibility. Version the code, the data and the model together, and anyone can rebuild the same model.

Here is a simple picture. A recipe that works in your home kitchen is not ready for a food factory. The factory needs written steps, exact measures, known suppliers and quality checks on every batch. A notebook is the home recipe. An MLOps project is the factory version.

Valentina Rojas is a data scientist at a car insurance company in Chile. The company is hypothetical. She trained a claim fraud classifier in a notebook, and it looked good. Her team deployed it by copying the notebook code into a web service.

Three weeks later, the operations team asked a question. Why does the model flag almost no claims? Valentina investigated, and she found four separate causes.

First, the notebook scaled the claim amount before training, but the service sent raw amounts. Second, the server installed a newer library version, and one default setting had changed. Third, a new claim type appeared in the live data, and the model had never seen it. Fourth, nobody had checked the share of flagged claims since launch, so the problem ran for weeks.

None of these problems was about choosing a better algorithm. Each one had a process fix. Keep preprocessing inside the saved model pipeline. Pin library versions. Check live inputs against the training data. And monitor the prediction rate.

One common mistake is to believe that a high test score means the model is ready. A test score tells you how the model did on one dataset, on one machine, on one day. It says nothing about whether someone else can rebuild it. Treat it as an entry requirement, not the finish line.

Let's recap. First, most production failures come from dependencies, data differences, silent errors and missing monitoring, not from the algorithm. Second, the key terms are artefact, model registry, CI and CD, serving, drift and rollback. Third, versioning code, data and model together makes results reproducible and explainable.

Now it is your turn. In the exercise below this video, you will review a sample notebook from a teammate. You will find at least six problems that would break it in production, and write a fix for each. It takes about twenty minutes.

Everything in this course leads to the capstone, where you deploy and monitor your own model API. In the next lesson, we look at the MLOps lifecycle and maturity levels. See you there.
```

## L02 The MLOps Lifecycle and Maturity Levels

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M1_L02_presenter.mp4`
- **Expected length:** about 4.9 minutes (683 words). The quality gate accepts ±10%.

```text
Two teams both say, we do MLOps. One has a single script and a checklist. The other has pipelines that retrain and redeploy models without anyone touching a keyboard. Are both teams right?

In the last lesson, we saw why models fail after the notebook. Today you get a map of the whole production lifecycle, and a way to decide what your own team should build next.

The production lifecycle has seven stages, connected in a loop. First, data: collect, clean and version it. Then training, with a reproducible script. Then evaluation on a fixed test set, compared with the current model. Then registration, where the approved model becomes a new version in a registry.

Next comes deployment, for example as an API in a container. Then monitoring of service health, inputs and predictions. And when monitoring shows drift or lower quality, retraining starts the loop again. The loop is the important part. A deployed model is not the end of a project. It is the start of a cycle.

Teams automate this loop to different degrees. We describe this with maturity levels. Several public frameworks use different names and numbers, so treat this as a practical summary, not an official standard. At level zero, everything is manual. A person trains in a notebook, copies a file to a server, and there is little monitoring.

At level one, training, evaluation and registration run as a repeatable pipeline. Deployment may still be manual, but every model version is traceable. At level two, code changes are tested and built automatically, models are promoted by rules plus human approval, and monitoring can trigger retraining.

Higher is not always better. Think of how a bakery grows. A home baker works by hand and tastes each batch. A small shop writes down recipes and uses timers. A factory uses machines and sensors. The home baker does not need a factory. They need the next improvement that stops bad batches.

Let's compare two hypothetical teams. Team A is a two-person start-up in Nairobi, run by Kamau Njoroge and Wairimu Kariuki. Their one model predicts which small shops will reorder stock. Kamau trains it monthly in a notebook and uploads a file to their server.

Nobody records which data produced which file, and nobody checks predictions after release. That is level zero. Their biggest risk is not knowing which model is live, or how to go back. The next single step is to move training into a script, log each run to MLflow, and register each version. It costs a few days, and it makes rollback possible.

Team B is a data science team of twenty people at a large bank in Singapore, led by Tan Wei Ling. They run more than fifty models, and some affect lending decisions. They already have automated training pipelines and a registry. That is level one.

Their biggest risk is slow, inconsistent releases, because each team deploys in its own way. Their next single step is a shared CI and CD pipeline, with automatic tests, quality gates and a required human approval before promotion. Full automatic retraining can wait until releases are stable.

The same framework gives very different advice, because the risks are different. And here is a common mistake. Automating an unstable process only makes the problems happen faster. If you cannot reproduce one training run, automatic retraining will not help you. Build reproducibility first, then automate.

Let's recap. First, the production lifecycle is a loop: data, training, evaluation, registration, deployment, monitoring and retraining. Second, maturity levels describe how much of that loop is automated, from manual work to full CI and CD with monitoring. Third, choose the next single improvement that removes your biggest risk.

In the exercise below this video, you will read about three teams, in Egypt, Vietnam and Germany. You will place each one on a maturity level, then recommend the next single improvement for one of them. It takes about twenty minutes.

In the next lesson, we start building. We turn a notebook into a real project, in Structuring an ML Project for Production. See you there.
```

## L03 Structuring an ML Project for Production

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M1_L03_presenter.mp4`
- **Expected length:** about 4.9 minutes (686 words). The quality gate accepts ±10%.
- **Pronunciation:** [VERSION] The pinned versions in requirements.txt (scikit-learn 1.9.1, pandas 3.0.6) were the versions used to test the code; check and update them before recording. The voiceover does not say version numbers.

```text
If you deleted your laptop today, could a teammate rebuild your model tomorrow, and get exactly the same score? If the honest answer is probably not, this lesson is for you.

Last time, we mapped the MLOps lifecycle. Now we build its first piece. You already know scikit-learn and Git, so we focus only on what changes for production. A production project has five features that a notebook usually lacks.

First, a training script that runs from start to finish with one command. Second, a configuration file for settings such as the random seed, the test size and model parameters. Third, pinned dependencies, so every machine installs the same library versions.

Fourth, fixed random seeds, everywhere randomness appears. Fifth, a clear folder layout under Git. The Git rule in one line: commit code and configuration, but not data files, model files or secrets.

Our running example predicts whether a red wine is good, meaning a quality score of seven or higher, from four features. If the real data file is missing, the loader builds a synthetic practice dataset with a fixed seed, so the course works offline.

The model is a scikit-learn pipeline, a scaler plus logistic regression. So preprocessing is saved inside the model file. This avoids the mismatch we saw in the last lesson, where the service skipped a scaling step.

Think of it this way. A notebook is like cooking from memory. A production project is like a printed recipe card, with exact amounts, oven temperature and cooking time. Anyone with the card and the same ingredients gets the same dish.

Let's watch Aarav Mehta, an ML engineer at a hypothetical grocery chain in Pune, refactor the wine notebook. In a terminal, he creates the project folder and starts Git. Then he creates a virtual environment and installs four packages.

Next, the configuration file. It holds the seed, the test size and the model settings. When he wants to try a new setting, he changes this file, not the code. And because the seed lives here, every function that uses randomness gets the same value.

Now the training script. It reads the configuration, loads the data, and splits it using the seed from the file. It builds the pipeline, trains it, and measures the F1 score. Then it saves the model and writes the score to a small metrics file. Notice that the scaler is inside the pipeline, so the saved file carries its own preprocessing.

He pins the exact versions he tested with, using pip freeze. The file now lists every library with an exact version number. Your versions may differ from ours. What matters is that you pin the ones you actually tested.

Now the real test. He runs the script twice. On our synthetic data, both runs print an F1 of zero point five five six eight. The score is modest, because the practice data is deliberately noisy. The point is that it is identical.

Finally, he adds the model file, the metrics file and the data folder to the ignore file, and commits. Git status shows no model or data files.

A common mistake is to set the seed in the model but forget the data split, or the reverse. The score then moves a little on every run, and you cannot tell if your change caused it. Set the seed in one place, and pass it everywhere.

Let's recap. First, a production project has a training script, a configuration file, pinned dependencies, fixed seeds and a clear layout under Git. Second, keep preprocessing inside the saved pipeline, so training and serving use the same steps. Third, test reproducibility directly: run training twice and compare.

In the exercise below this video, you will refactor a notebook into this structure, run it twice, and prove the results are identical. It takes about forty minutes. Check that git status shows no data or model files. Keep this project safe, because it becomes the base of your capstone at the end of the course.

In the next lesson, we record every training run automatically, in Experiment Tracking with MLflow. See you there.
```

## L04 Experiment Tracking with MLflow

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M1_L04_presenter.mp4`
- **Expected length:** about 4.9 minutes (682 words). The quality gate accepts ±10%.

```text
Last week you tried twelve model settings. Which one gave the best score, with which data, and where is that model file now? If the answer lives in a spreadsheet, or only in your memory, you need experiment tracking.

In the last lesson, we made training reproducible. Now we record it. Experiment tracking saves every training run automatically. It stores the parameters, meaning settings such as C. It stores the metrics, such as F1. And it stores the artefacts, such as the trained model file.

MLflow is a free, open-source tool for this. Its tracking part has three ideas. An experiment groups related runs, such as wine quality. A run is one execution of your training code. And the tracking store is where runs are saved. For this course, a local database file is enough. Teams usually share a tracking server, so everyone sees the same history.

You add only a few lines to the training code. You point MLflow at the store and name the experiment. Then, for each value of C, you start a run, train the pipeline, and log the parameter, the F1 score and the model. You also give an input example, so MLflow records the expected input columns.

Think of it as a laboratory notebook that writes itself. Every experiment gets a page, with the date, the exact settings and the results. And a sample is kept in the fridge, so you can repeat or check it later. Nobody has to remember anything, because the notebook remembers for them.

Let's meet Beatriz Carvalho. She works for a hypothetical wine cooperative in Portugal, and she wants to predict which red wines tasters will rate as good. In our demo, we use the offline synthetic data from lesson three, so you can follow without a download.

In a terminal in the project folder, she installs MLflow. She creates a small tracking script with the loop you just saw, and runs it. Three runs are logged, one for each value of C. Each run gets a clear name that includes its setting, so she can find it again later without guessing.

Next, she starts the MLflow interface, pointing it at the same database file. She opens the local address that it prints, and clicks the wine quality experiment. The table shows all three runs, with their names.

She selects all three runs and clicks Compare. Now the parameter C and the F1 score sit side by side. With C of one, F1 is zero point five five seven. With C of zero point one, it is zero point five three eight. With C of zero point zero one, it drops to zero point four six one.

Beatriz chooses C of one. The strongest regularisation clearly underfits. She opens the best run and shows the Artifacts tab, where the saved model folder waits. The difference between C of one and C of zero point one is small, so on more data she might check both again. Her scores on the real dataset will be different.

A common mistake is to log only the best run. The poor runs matter too, because they show what you already tried and why you rejected it. So log every run, and never delete a run because it looks bad. And never log secrets or personal data. Anyone who can open the tracking server can read them.

Let's recap. First, experiment tracking records the parameters, metrics and artefacts of every training run. Second, in MLflow, experiments group runs, and the interface lets you compare runs and open their saved models. Third, log every run, including poor ones, and choose a model with a metric that fits your problem.

In the exercise below this video, you will log at least three runs with different settings, compare them in the interface, and write down which run you would choose, and why. It takes about thirty-five minutes. You will need this tracking for your capstone.

In the next lesson, we keep only the models that matter, and version them properly, in Model Registry and Data Versioning. See you there.
```

## L05 Model Registry and Data Versioning

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M1_L05_presenter.mp4`
- **Expected length:** about 4.8 minutes (671 words). The quality gate accepts ±10%.

```text
A customer complains about a prediction made three weeks ago. Which model version made it? What data trained that model, and which commit of your code? If you cannot answer in two minutes, you cannot debug, audit or roll back.

In the last lesson, experiment tracking recorded every run. A model registry is different. It records only the models you decided to keep, and gives each one a clear name, a version number and a status.

In MLflow, a registered model has a name, such as wine quality classifier. Each time you register a model under that name, MLflow creates a new version: one, two, three, and so on. A version never changes after it is created.

To mark which version is in use, current MLflow releases use aliases. An alias is a movable name that points to one version. For example, champion for the production model, and challenger for a candidate. The serving code always loads the champion. To promote or roll back, you simply move the alias. No code changes.

Older releases used fixed stages instead, such as staging and production. This course uses aliases. If your team's server is older, check which method it supports.

A version is only reproducible if you also know its inputs. So record two tags on every version. First, a data hash. This is a short fingerprint of the exact training data. If one value changes, the hash changes. Second, the Git commit ID, which points to the exact code that trained the model.

Think of a library catalogue. Each edition of a book has a fixed number, and the catalogue records the publisher and the printing. A recommended edition label can move from one edition to another, without anyone reprinting the books.

Let's watch Yusuf Demir, an ML engineer at a hypothetical logistics company in Izmir, Türkiye. First, he commits the current code, so the commit ID means something. Then he runs a registration script. It finds the best run by F1, registers its model, adds the two tags, and sets the champion alias.

In the MLflow interface, he clicks Models, and there is the wine quality classifier with version one. He opens it. The champion alias is there, with the data hash and the Git commit as tags.

Next, he changes C in the configuration file, trains, and registers again. Version two appears. But the champion alias still points to version one, because nothing moves until he decides.

Now he promotes it, with one line of Python that moves the alias to version two. He refreshes the page, and champion now points to version two. Then he moves it back to version one. That is a rollback, and it took one line.

One more detail. When Yusuf registered twice on the same data and the same commit, both versions had the same data hash, starting with b f c two five zero. This proves the tags describe the inputs, not the time of the run.

A common mistake is to use the registry like a folder, with names like final, final two or new best. The version number already identifies the model. Use aliases for status and tags for origin. And never put credentials or personal data in tags or descriptions.

Let's recap. First, a model registry stores chosen models as numbered versions that never change. Second, aliases such as champion mark which version is in use, and moving an alias promotes or rolls back without code changes. Third, tag every version with a data hash and a Git commit, so it can be rebuilt and explained.

In the exercise below this video, you will register your best model, add a second version, choose the champion, and tag each version with its data hash and commit. Then you load the champion and make one prediction. It takes about thirty-five minutes, and your capstone needs exactly this.

That completes week one. In the next lesson, we serve the champion to the world, in Designing a Prediction API with FastAPI. See you there.
```
